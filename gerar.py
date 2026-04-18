#!/usr/bin/env python3
"""
gerar.py — Automação de LP para Move Maquinas
Lê Google Sheets → Gera HTML via Claude API → Atualiza Sheets

Uso:
  python gerar.py               # processa todas as páginas na fila
  python gerar.py --limite 5    # processa as próximas 5
  python gerar.py --id 42       # processa uma página específica
"""

import os
import re
import json
import hashlib
import argparse
from datetime import datetime
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials
import anthropic

from prompts import (
    PROMPT_01_FULL,
    PROMPT_01_CONTEXT_ONLY,
    PROMPT_02_VISUAL,
    PROMPT_03_HTML,
)

# ─── Configuração ─────────────────────────────────────────────────────────────

SHEET_ID         = os.getenv("SHEET_ID", "1_ap9dZhzgReHMsnSF38M5I02s4LM-JCZoDni5sJpV_U")
CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS", "credentials.json")
CLAUDE_MODEL     = "claude-sonnet-4-6"
OUTPUT_DIR       = Path("./output")
TEMPLATES_DIR    = Path("./templates")
CKB_FILE         = Path("./ckb-move-maquinas.md")

OUTPUT_DIR.mkdir(exist_ok=True)
TEMPLATES_DIR.mkdir(exist_ok=True)

# ─── Famílias de cross-linking A5 ─────────────────────────────────────────────

FAMILIAS: dict[str, list[str]] = {
    "plataformas": [
        "aluguel-de-plataforma-elevatoria-articulada",
        "aluguel-de-plataforma-elevatoria-diesel",
        "aluguel-de-plataforma-elevatoria-eletrica",
    ],
    "empilhadeiras": [
        "aluguel-de-empilhadeira-combustao",
        "aluguel-de-empilhadeira-eletrica",
        "aluguel-de-empilhadeira-camara-fria",
        "aluguel-de-empilhadeira-retratil",
    ],
    "movimentacao": [
        "aluguel-de-transpaleteira",
        "aluguel-de-rebocador",
    ],
    "armazem": [
        "aluguel-de-empilhadeira-retratil",
        "aluguel-de-selecionadora",
        "aluguel-de-transpaleteira",
    ],
    "curso": [
        "curso-de-operador-de-empilhadeira",
        "aluguel-de-empilhadeira-combustao",
        "aluguel-de-empilhadeira-eletrica",
    ],
}

# Variantes de âncora por tipo
ANCORAS: dict[str, list[str]] = {
    "A1": [
        "{servico}",
        "Locação de {produto}",
        "{produto} para Locação — Move Maquinas",
        "{produtos} Disponíveis para Alugar em {estado}",
    ],
    "A2": [
        "Aluguel de {produto} em {cidade}",
        "Locação de {produto} em {cidade}",
        "Alugue sua {produto} em {cidade} com a Move Maquinas",
        "{produtos} para Alugar em {cidade}",
    ],
    "A3": [
        "Aluguel de {produto} em {cidade}",
        "Locação de {produto} em {cidade}",
        "{produto} em {cidade} — Move Maquinas",
        "{produto} para Alugar em {cidade}",
    ],
    "A4": [
        "Aluguel de {produto} em {cidade_destino}",
        "Locação de {produto} em {cidade_destino}",
        "Alugue sua {produto} em {cidade_destino} com a Move Maquinas",
        "{produtos} para Alugar em {cidade_destino}",
    ],
    "A5": [
        "Aluguel de {produto_destino} em {cidade}",
        "Locação de {produto_destino} em {cidade}",
        "Alugue sua {produto_destino} em {cidade} com a Move Maquinas",
        "{produto_destino} para Alugar em {cidade}",
    ],
    "A6": [
        "Equipamentos em {cidade}",
        "Locação de Equipamentos em {cidade}",
        "Move Maquinas em {cidade}",
        "Máquinas para Alugar em {cidade}",
    ],
}

# ─── Âncora determinística ────────────────────────────────────────────────────

def ancora(tipo: str, seed: str, **kwargs) -> str:
    """Seleciona variante de âncora via MD5(seed) % 4 e preenche os placeholders."""
    variantes = ANCORAS[tipo]
    idx = int(hashlib.md5(seed.encode()).hexdigest(), 16) % 4
    return variantes[idx].format(**kwargs)


def ancora_breadcrumb(tipo: str, **kwargs) -> str:
    """Breadcrumb sempre usa variante 0 (Exata)."""
    return ANCORAS[tipo][0].format(**kwargs)

# ─── Google Sheets ────────────────────────────────────────────────────────────

def conectar_sheets() -> gspread.Spreadsheet:
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    client = gspread.authorize(creds)
    return client.open_by_key(SHEET_ID)


def ler_aba(sheet: gspread.Spreadsheet, nome: str) -> list[dict]:
    ws = sheet.worksheet(nome)
    return ws.get_all_records()


def atualizar_celula(sheet: gspread.Spreadsheet, aba: str, row: int, col: int, valor):
    ws = sheet.worksheet(aba)
    ws.update_cell(row, col, valor)


def registrar_log(sheet: gspread.Spreadsheet, entrada: dict):
    ws = sheet.worksheet("AUDIT_LOG")
    ws.append_row([
        entrada.get("timestamp", datetime.now().isoformat()),
        entrada.get("page_url", ""),
        entrada.get("acao", ""),
        entrada.get("status", ""),
        entrada.get("detalhe", ""),
    ])

# ─── Helpers de dados ─────────────────────────────────────────────────────────

def encontrar_cidade(cities: list[dict], city_slug: str) -> dict:
    for c in cities:
        if c["city_slug"] == city_slug:
            return c
    raise ValueError(f"Cidade não encontrada: {city_slug}")


def encontrar_servico(services: list[dict], service_slug: str) -> dict:
    for s in services:
        if s["service_slug"] == service_slug:
            return s
    raise ValueError(f"Serviço não encontrado: {service_slug}")


def familia_do_servico(service_slug: str) -> str:
    for familia, slugs in FAMILIAS.items():
        if service_slug in slugs:
            return familia
    return ""


def cross_servicos(service_slug: str, city_slug: str, pages: list[dict]) -> list[dict]:
    """Retorna City LPs da mesma família, mesma cidade, já publicadas."""
    familia = familia_do_servico(service_slug)
    if not familia:
        return []

    slugs_familia = [s for s in FAMILIAS[familia] if s != service_slug]
    resultado = []
    for page in pages:
        if (
            page["city_slug"] == city_slug
            and page["service_slug"] in slugs_familia
            and page["status"] == "✅ Concluído"
        ):
            resultado.append(page)
    return resultado[:3]  # máx 3 cross-serviços

# ─── MAPA_DE_LINKS ────────────────────────────────────────────────────────────

def montar_mapa_links(
    page: dict,
    cidade: dict,
    servico: dict,
    pages: list[dict],
) -> str:
    city_slug    = page["city_slug"]
    city_label   = page["city_label"]
    service_slug = page["service_slug"]
    produto      = servico["product_label"]
    produtos     = servico["product_label_plural"]
    estado       = page["state_sigla"]
    url_page     = page["url"]

    linhas = [
        f"[MAPA_DE_LINKS]",
        f"Página: {url_page}",
        f"Serviço: {page['service_label']}",
        f"Produto: {produto}",
        f"Cidade: {city_label} | {estado} | Tier {page['city_tier']}",
        "",
        "LINKS OBRIGATÓRIOS DE SAÍDA:",
    ]

    # A1 — breadcrumb para Hub Nacional
    linhas += [
        f"  [BREADCRUMB] [A1] → {servico['hub_url']}",
        f'    anchor: "{ancora_breadcrumb("A1", servico=page["service_label"], produto=produto, produtos=produtos, estado=estado)}"',
    ]

    # A6 — breadcrumb para Hub de Cidade
    linhas += [
        f"  [BREADCRUMB] [A6] → /{city_slug}/",
        f'    anchor: "{ancora_breadcrumb("A6", cidade=city_label)}"',
    ]

    # A4 — ring anterior
    ring_ant = cidade.get("ring_anterior", "")
    if ring_ant:
        url_ant = f"/{ring_ant}/{service_slug}"
        city_ant_data = next((c for c in [] if c["city_slug"] == ring_ant), None)
        city_ant_label = ring_ant.split("-")[0].title()
        linhas += [
            f"  [BODY]       [A4] → {url_ant}",
            f'    anchor: "{ancora("A4", ring_ant + service_slug, produto=produto, produtos=produtos, cidade_destino=city_ant_label)}"',
        ]

    # A4 — ring próximo
    ring_prox = cidade.get("ring_proximo", "")
    if ring_prox:
        url_prox = f"/{ring_prox}/{service_slug}"
        city_prox_label = ring_prox.split("-")[0].title()
        linhas += [
            f"  [BODY]       [A4] → {url_prox}",
            f'    anchor: "{ancora("A4", city_slug + ring_prox, produto=produto, produtos=produtos, cidade_destino=city_prox_label)}"',
        ]

    # A5 — cross-serviço da mesma família
    for cross in cross_servicos(service_slug, city_slug, pages):
        serv_dest_label = cross["service_label"].replace("Aluguel de ", "")
        url_cross = cross["url"]
        linhas += [
            f"  [CTA]        [A5] → {url_cross}",
            f'    anchor: "{ancora("A5", cross["service_slug"] + city_slug, produto_destino=serv_dest_label, cidade=city_label)}"',
        ]

    # Links esperados de entrada
    linhas += [
        "",
        "LINKS ESPERADOS DE ENTRADA (referência — não gerar):",
        f"  ← {servico['hub_url']}  (A2 card ou A3 grid)",
        f"  ← /{city_slug}/         (A6 down)",
    ]
    if ring_ant:
        linhas.append(f"  ← /{ring_ant}/{service_slug}  (A4 recíproco)")
    if ring_prox:
        linhas.append(f"  ← /{ring_prox}/{service_slug}  (A4 recíproco)")

    linhas.append("[/MAPA_DE_LINKS]")
    return "\n".join(linhas)

# ─── Claude API ───────────────────────────────────────────────────────────────

def chamar_claude(client: anthropic.Anthropic, prompt: str) -> tuple[str, int]:
    """Chama Claude e retorna (resposta, tokens_usados)."""
    msg = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}],
    )
    tokens = msg.usage.input_tokens + msg.usage.output_tokens
    return msg.content[0].text, tokens


def gerar_completo(
    client: anthropic.Anthropic,
    page: dict,
    cidade: dict,
    servico: dict,
    mapa_links: str,
    ckb: str,
) -> tuple[str, int]:
    """Geração completa via 3 prompts (primeira cidade do serviço)."""
    total_tokens = 0
    keyword    = page["service_label"] + " em " + page["city_label"]
    city_label = page["city_label"]
    estado     = page["state_sigla"]
    canonical  = f"https://movemaquinas.com.br{page['url']}"

    breadcrumb = (
        f"Home > {page['service_label']} > {city_label}"
    )

    # Prompt 01 — conteúdo
    p1 = PROMPT_01_FULL.format(
        keyword=keyword,
        ckb=ckb,
        mapa_links=mapa_links,
        city_label=city_label,
        breadcrumb=breadcrumb,
        contexto_cidade=cidade.get("contexto", ""),
    )
    conteudo, t1 = chamar_claude(client, p1)
    total_tokens += t1
    print(f"    ✓ Prompt 01 ({t1} tokens)")

    # Prompt 02 — estratégia visual
    p2 = PROMPT_02_VISUAL.format(conteudo=conteudo)
    estrategia, t2 = chamar_claude(client, p2)
    total_tokens += t2
    print(f"    ✓ Prompt 02 ({t2} tokens)")

    # Prompt 03 — HTML final
    p3 = PROMPT_03_HTML.format(
        conteudo=conteudo,
        estrategia_visual=estrategia,
        mapa_links=mapa_links,
        breadcrumb=breadcrumb,
        canonical_url=canonical,
    )
    html, t3 = chamar_claude(client, p3)
    total_tokens += t3
    print(f"    ✓ Prompt 03 ({t3} tokens)")

    return html, total_tokens


def gerar_contexto_cidade(
    client: anthropic.Anthropic,
    page: dict,
    cidade: dict,
) -> tuple[str, int]:
    """Gera apenas o parágrafo de contexto local (demais cidades)."""
    p = PROMPT_01_CONTEXT_ONLY.format(
        service_label=page["service_label"],
        city_label=page["city_label"],
        state_sigla=page["state_sigla"],
        contexto_cidade=cidade.get("contexto", ""),
    )
    return chamar_claude(client, p)

# ─── Template ─────────────────────────────────────────────────────────────────

def salvar_template(service_slug: str, html: str):
    path = TEMPLATES_DIR / f"template-{service_slug}.html"
    path.write_text(html, encoding="utf-8")


def carregar_template(service_slug: str) -> str:
    path = TEMPLATES_DIR / f"template-{service_slug}.html"
    if not path.exists():
        raise FileNotFoundError(f"Template não encontrado: {path}")
    return path.read_text(encoding="utf-8")


def preencher_template(template: str, page: dict, cidade: dict, contexto: str, mapa_links: str) -> str:
    """Substitui variáveis no template HTML."""
    city_label  = page["city_label"]
    state_sigla = page["state_sigla"]
    url         = page["url"]
    canonical   = f"https://movemaquinas.com.br{url}"
    keyword     = page["service_label"] + " em " + city_label

    replacements = {
        "{{cidade}}":        city_label,
        "{{estado}}":        state_sigla,
        "{{keyword}}":       keyword,
        "{{canonical_url}}": canonical,
        "{{contexto_local}}": contexto,
        "{{mapa_links_json}}": json.dumps({"mapa": mapa_links}),
    }

    result = template
    for placeholder, valor in replacements.items():
        result = result.replace(placeholder, valor)

    # Substitui todas as menções da cidade original pela nova cidade
    # (estratégia simples — funciona para ~95% dos casos)
    cidade_template_match = re.search(r'<h1[^>]*>(.*?)</h1>', template, re.IGNORECASE)
    if cidade_template_match:
        h1_original = cidade_template_match.group(1)
        # Extrai cidade do H1 original (após "em ")
        match_cidade = re.search(r'\bem\s+(.+?)(?:\s*<|$)', h1_original, re.IGNORECASE)
        if match_cidade:
            cidade_original = match_cidade.group(1).strip()
            result = result.replace(cidade_original, city_label)

    return result

# ─── Patch de HTMLs existentes ────────────────────────────────────────────────

def patch_adicionar_link(filepath: Path, selector_class: str, city_slug: str, href: str, texto: str) -> bool:
    """Adiciona href em um slot sem link dentro do HTML existente."""
    if not filepath.exists():
        return False

    html = filepath.read_text(encoding="utf-8")
    pattern = rf'(<a[^>]*class="[^"]*{re.escape(selector_class)}[^"]*"[^>]*data-slug="{re.escape(city_slug)}"[^>]*)>'
    replacement = rf'\1 href="{href}">'
    new_html, count = re.subn(pattern, replacement, html)

    if count > 0:
        filepath.write_text(new_html, encoding="utf-8")
        return True
    return False


def patch_hub_nacional(service_slug: str, city_slug: str, href: str, texto: str):
    """Adiciona href no Hub Nacional para a cidade recém-publicada."""
    filepath = OUTPUT_DIR / f"hub-{service_slug}.html"
    return patch_adicionar_link(filepath, "city-link", city_slug, href, texto)


def patch_hub_cidade(city_slug: str, service_slug: str, href: str, texto: str):
    """Adiciona serviço no Hub de Cidade."""
    filepath = OUTPUT_DIR / f"hub-cidade-{city_slug}.html"
    return patch_adicionar_link(filepath, "service-link", service_slug, href, texto)


def patch_ring(ring_city_slug: str, service_slug: str, new_city_slug: str, href: str, texto: str):
    """Adiciona link recíproco A4 na cidade do ring."""
    filename = f"{ring_city_slug}-{service_slug}.html"
    filepath = OUTPUT_DIR / filename
    return patch_adicionar_link(filepath, "ring-link", new_city_slug, href, texto)


def patch_cross_servico(city_slug: str, service_slug_existente: str, service_slug_novo: str, href: str, texto: str):
    """Adiciona link A5 recíproco na LP de serviço existente."""
    filename = f"{city_slug}-{service_slug_existente}.html"
    filepath = OUTPUT_DIR / filename
    return patch_adicionar_link(filepath, "cross-service-link", service_slug_novo, href, texto)

# ─── Validação gate anti-órfã ─────────────────────────────────────────────────

def validar_gate(page: dict, cidade: dict, servico: dict, pages: list[dict]) -> tuple[bool, str]:
    """Verifica se a página pode ser publicada (gate anti-órfã)."""
    city_slug    = page["city_slug"]
    service_slug = page["service_slug"]

    # Hub Nacional deve ter o slot da cidade
    hub_file = OUTPUT_DIR / f"hub-{service_slug}.html"
    if not hub_file.exists():
        return False, f"Hub Nacional não encontrado: hub-{service_slug}.html"

    # Hub de Cidade deve existir
    hub_cidade = OUTPUT_DIR / f"hub-cidade-{city_slug}.html"
    if not hub_cidade.exists():
        return False, f"Hub de Cidade não encontrado: hub-cidade-{city_slug}.html"

    # Ring: ao menos 1 cidade publicada (mesmo serviço)
    ring_ant  = cidade.get("ring_anterior", "")
    ring_prox = cidade.get("ring_proximo", "")

    ring_publicado = False
    for p in pages:
        if p["service_slug"] == service_slug and p["status"] == "✅ Concluído":
            if p["city_slug"] in [ring_ant, ring_prox]:
                ring_publicado = True
                break

    # Para T1 (primeira cidade do ring), permite publicar sem ring
    if not ring_publicado and page.get("city_tier", 3) > 1:
        return False, f"Ring não tem cidade publicada para {service_slug}"

    return True, "ok"

# ─── Processamento principal ──────────────────────────────────────────────────

def processar_pagina(
    page: dict,
    row_num: int,
    sheet: gspread.Spreadsheet,
    client: anthropic.Anthropic,
    all_pages: list[dict],
    cities: list[dict],
    services: list[dict],
    ckb: str,
):
    city_slug    = page["city_slug"]
    service_slug = page["service_slug"]
    city_label   = page["city_label"]
    service_label = page["service_label"]

    print(f"\n{'─'*60}")
    print(f"  Processando: {service_label} em {city_label}")
    print(f"  URL: {page['url']}")

    try:
        cidade  = encontrar_cidade(cities, city_slug)
        servico = encontrar_servico(services, service_slug)
    except ValueError as e:
        print(f"  ❌ Erro: {e}")
        atualizar_celula(sheet, "PAGES", row_num, 10, "❌ Erro")
        atualizar_celula(sheet, "PAGES", row_num, 15, str(e))
        return

    # Marcar como iniciado
    atualizar_celula(sheet, "PAGES", row_num, 10, "🔄 Iniciado")

    # Validar gate
    ok, motivo = validar_gate(page, cidade, servico, all_pages)
    if not ok:
        print(f"  ⚠️  Gate bloqueou: {motivo}")
        atualizar_celula(sheet, "PAGES", row_num, 10, "⏳ Fila")
        atualizar_celula(sheet, "PAGES", row_num, 15, f"Gate: {motivo}")
        return

    # Montar MAPA_DE_LINKS
    mapa_links = montar_mapa_links(page, cidade, servico, all_pages)

    try:
        is_template = str(page.get("is_template", "FALSE")).upper() == "TRUE"
        template_existe = (TEMPLATES_DIR / f"template-{service_slug}.html").exists()

        if is_template or not template_existe:
            # Geração completa
            print(f"  📝 Geração completa (template)")
            html, tokens = gerar_completo(client, page, cidade, servico, mapa_links, ckb)
            salvar_template(service_slug, html)
            # Marcar template como gerado no Sheets
            for i, s in enumerate(services):
                if s["service_slug"] == service_slug:
                    ws = sheet.worksheet("SERVICES")
                    ws.update_cell(i + 2, 7, "TRUE")  # col G = template_gerado
                    break
        else:
            # Template fill + contexto
            print(f"  ⚡ Template fill (economia de tokens)")
            template = carregar_template(service_slug)
            contexto, tokens = gerar_contexto_cidade(client, page, cidade)
            print(f"    ✓ Contexto gerado ({tokens} tokens)")
            html = preencher_template(template, page, cidade, contexto, mapa_links)

    except Exception as e:
        print(f"  ❌ Erro na geração: {e}")
        atualizar_celula(sheet, "PAGES", row_num, 10, "❌ Erro")
        atualizar_celula(sheet, "PAGES", row_num, 15, str(e))
        registrar_log(sheet, {
            "page_url": page["url"],
            "acao": "geracao",
            "status": "❌",
            "detalhe": str(e),
        })
        return

    # Salvar HTML
    arquivo = f"{city_slug}-{service_slug}.html"
    filepath = OUTPUT_DIR / arquivo
    filepath.write_text(html, encoding="utf-8")
    print(f"  💾 Salvo: {filepath}")

    # Atualizar Sheets
    atualizar_celula(sheet, "PAGES", row_num, 10, "✅ Concluído")
    atualizar_celula(sheet, "PAGES", row_num, 11, arquivo)
    atualizar_celula(sheet, "PAGES", row_num, 12, page["url"])
    atualizar_celula(sheet, "PAGES", row_num, 13, tokens)
    atualizar_celula(sheet, "PAGES", row_num, 14, datetime.now().strftime("%Y-%m-%d %H:%M"))

    # Atualizar servicos_publicados na aba CITIES
    for i, c in enumerate(cities):
        if c["city_slug"] == city_slug:
            publicados = c.get("servicos_publicados", "")
            if service_slug not in publicados:
                novo = f"{publicados},{service_slug}".strip(",")
                ws = sheet.worksheet("CITIES")
                col_idx = list(c.keys()).index("servicos_publicados") + 1
                ws.update_cell(i + 2, col_idx, novo)
            break

    # Patches em páginas existentes
    print(f"  🔗 Aplicando patches...")

    patched = 0
    href = f"/{city_slug}/{service_slug}"

    if patch_hub_nacional(service_slug, city_slug, href, f"Aluguel de {servico['product_label']} em {city_label}"):
        patched += 1
        registrar_log(sheet, {"page_url": f"/hub-{service_slug}", "acao": "patch_hub_nacional", "status": "✅", "detalhe": f"href adicionado para {city_slug}"})

    if patch_hub_cidade(city_slug, service_slug, href, service_label):
        patched += 1
        registrar_log(sheet, {"page_url": f"/{city_slug}/", "acao": "patch_hub_cidade", "status": "✅", "detalhe": f"{service_slug} adicionado"})

    ring_ant  = cidade.get("ring_anterior", "")
    ring_prox = cidade.get("ring_proximo", "")
    for ring_slug in [ring_ant, ring_prox]:
        if ring_slug and patch_ring(ring_slug, service_slug, city_slug, href, city_label):
            patched += 1

    for cross in cross_servicos(service_slug, city_slug, all_pages):
        if patch_cross_servico(city_slug, cross["service_slug"], service_slug, href, service_label):
            patched += 1

    print(f"  ✅ Concluído | {tokens} tokens | {patched} patches")

    registrar_log(sheet, {
        "page_url": page["url"],
        "acao": "geracao_completa" if (is_template or not template_existe) else "template_fill",
        "status": "✅",
        "detalhe": f"{tokens} tokens | {patched} patches",
    })

# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Move Maquinas LP Generator")
    parser.add_argument("--limite", type=int, default=0, help="Máximo de páginas a processar")
    parser.add_argument("--id",     type=int, default=0, help="Processa apenas a página com este ID")
    args = parser.parse_args()

    print("🚀 Move Maquinas LP Generator")
    print(f"   Modelo: {CLAUDE_MODEL}")
    print(f"   Output: {OUTPUT_DIR.resolve()}")

    # Conectar serviços
    print("\n📊 Conectando ao Google Sheets...")
    sheet = conectar_sheets()
    print("   ✓ Sheets conectado")

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    print("   ✓ Claude API pronta")

    # Ler dados
    all_pages = ler_aba(sheet, "PAGES")
    cities    = ler_aba(sheet, "CITIES")
    services  = ler_aba(sheet, "SERVICES")
    ckb       = CKB_FILE.read_text(encoding="utf-8") if CKB_FILE.exists() else ""

    # Filtrar fila
    fila = []
    for i, page in enumerate(all_pages):
        row_num = i + 2  # +2 porque Sheets começa em 1 e tem header

        if args.id and page.get("id") != args.id:
            continue

        if page.get("status", "") == "⏳ Fila":
            fila.append((page, row_num))

    if args.limite:
        fila = fila[:args.limite]

    print(f"\n📋 {len(fila)} página(s) na fila")

    total_tokens = 0
    for page, row_num in fila:
        processar_pagina(page, row_num, sheet, client, all_pages, cities, services, ckb)

    print(f"\n{'═'*60}")
    print(f"✅ Finalizado | {len(fila)} páginas processadas")


if __name__ == "__main__":
    main()
