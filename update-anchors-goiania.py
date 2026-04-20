"""
Script de atualização de âncoras — Goiânia (piloto v2)
Regra central: toda âncora de serviço DEVE conter o verbo de intenção
(aluguel, locação, alugar, locar) — só varia o restante.

Zonas protegidas: nav header (.hdr), footer de serviços (.ft__col)
"""

import re
import os

BASE = "/Users/jrios/move-maquinas-seo/goiania-go"

# ---------------------------------------------------------------------------
# Pool corrigido: verbo de intenção sempre presente
# Variamos: aluguel/locação/alugar/locar + contexto (polo, uso, NR, modelo)
# ---------------------------------------------------------------------------

CHANGES = {

    # ===== HUB GOIÂNIA =====
    # Links de cidades vizinhas — destino é hub de cidade, não LP de serviço
    # Âncora correta: "aluguel de equipamentos em CIDADE" com variações
    "index.html": [
        ("/aparecida-de-goiania-go/",
         "Aparecida de Goiânia (8 km)",
         "aluguel de equipamentos em Aparecida de Goiânia"),
        ("/senador-canedo-go/",
         "Senador Canedo (18 km)",
         "locação de máquinas no DASC Senador Canedo"),
        ("/trindade-go/",
         "Trindade (25 km)",
         "aluguel de empilhadeira em Trindade GO"),
        ("/anapolis-go/",
         "Anápolis (55 km)",
         "locação de equipamentos no DAIA Anápolis"),
        ("/inhumas-go/",
         "Inhumas (40 km)",
         "aluguel de máquinas em Inhumas GO"),
        ("/brasilia-df/",
         "Brasília (209 km)",
         "locação de equipamentos pesados em Brasília DF"),
    ],

    # ===== LP EMPILHADEIRA =====
    "aluguel-de-empilhadeira-combustao/index.html": [
        # Breadcrumb
        ("/goiania-go/",
         "Equipamentos em Goiânia",
         "locação de equipamentos em Goiânia"),
        # Serviços irmãos — verbo de intenção + variação de contexto
        ("/goiania-go/aluguel-de-plataforma-elevatoria-tesoura",
         "Aluguel de Plataforma Tesoura em Goiânia",
         "locação de plataforma tesoura para obra em Goiânia"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-articulada",
         "Aluguel de Plataforma Articulada em Goiânia",
         "alugar plataforma articulada em Goiânia GO"),
        ("/goiania-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira em Goiânia",
         "locação de transpaleteira elétrica no Polo da Moda Goiânia"),
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "Curso de Operador de Empilhadeira em Goiânia",
         "habilitação NR-11 para operador de empilhadeira em Goiânia"),
        # Body texto contextual
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "curso de operador de empilhadeira",
         "treinamento NR-11 para operador em Goiânia"),
        ("/goiania-go/",
         "Goiânia",
         "aluguel de equipamentos em Goiânia GO"),
        # Cobertura — verbo + polo da cidade de destino
        ("/aparecida-de-goiania-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira em Aparecida de Goiânia",
         "locação de empilhadeira no DAIAG Aparecida de Goiânia"),
        ("/anapolis-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira em Anápolis",
         "aluguel de empilhadeira no DAIA Anápolis GO"),
        ("/trindade-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira em Trindade",
         "locação de empilhadeira em Trindade GO"),
        ("/senador-canedo-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira em Senador Canedo",
         "alugar empilhadeira no DASC Senador Canedo"),
        # Footer editorial (não é footer de nav)
        ("/goiania-go/",
         "Todos os equipamentos em Goiânia",
         "ver todos os equipamentos para locação em Goiânia"),
        ("/cidades-atendidas",
         "Cidades atendidas pela Movemáquinas",
         "cidades com disponibilidade de aluguel em GO e DF"),
        # Segunda âncora de NR-11 no FAQ
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "curso de operador de empilhadeira",
         "capacitação NR-11 para operador de empilhadeira"),
    ],

    # ===== LP PLATAFORMA ARTICULADA =====
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/goiania-go/",
         "Equipamentos em Goiânia",
         "locação de equipamentos em Goiânia"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-tesoura",
         "Aluguel de Plataforma Tesoura em Goiânia",
         "alugar plataforma tesoura em Goiânia GO"),
        ("/goiania-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira a Combustão em Goiânia",
         "locação de empilhadeira Clark no Distrito Industrial Leste GO"),
        ("/goiania-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira em Goiânia",
         "aluguel de transpaleteira para galpão em Goiânia"),
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "Curso de Operador de Empilhadeira em Goiânia",
         "habilitação NR-11 para operadores em Goiânia"),
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "treinamento para operadores",
         "treinamento NR-35 e NR-11 para locação segura em Goiânia"),
        ("/goiania-go/",
         "Goiânia",
         "aluguel de equipamentos em Goiânia GO"),
        # Cobertura
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-articulada",
         "Aluguel de Plataforma Articulada em Aparecida de Goiânia",
         "locação de plataforma articulada no DIMAG Aparecida de Goiânia"),
        ("/anapolis-go/aluguel-de-plataforma-elevatoria-articulada",
         "Aluguel de Plataforma Articulada em Anápolis",
         "aluguel de plataforma articulada no DAIA Anápolis"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-articulada",
         "Aluguel de Plataforma Articulada em Brasília",
         "locação de plataforma articulada no SIA Brasília DF"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-articulada",
         "Aluguel de Plataforma Articulada em Trindade",
         "alugar plataforma articulada em Trindade GO"),
        ("/goiania-go/",
         "Todos os equipamentos em Goiânia",
         "ver todos os equipamentos para locação em Goiânia"),
        ("/cidades-atendidas",
         "Cidades atendidas pela Movemáquinas",
         "cidades com disponibilidade de aluguel em GO e DF"),
    ],

    # ===== LP PLATAFORMA TESOURA =====
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/goiania-go/",
         "Equipamentos em Goiânia",
         "locação de equipamentos em Goiânia"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-articulada",
         "Aluguel de Plataforma Articulada em Goiânia",
         "locação de plataforma articulada para fachada em Goiânia"),
        ("/goiania-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira a Combustão em Goiânia",
         "aluguel de empilhadeira Clark no Ceasa Goiânia"),
        ("/goiania-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira em Goiânia",
         "locação de transpaleteira elétrica para armazém em Goiânia"),
        ("/goiania-go/",
         "Goiânia",
         "aluguel de equipamentos em Goiânia GO"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-articulada",
         "plataforma articulada",
         "aluguel de plataforma articulada em Goiânia"),
        # Cobertura
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-tesoura",
         "Aluguel de Plataforma Tesoura em Aparecida de Goiânia",
         "locação de plataforma tesoura no DAIAG Aparecida de Goiânia"),
        ("/anapolis-go/aluguel-de-plataforma-elevatoria-tesoura",
         "Aluguel de Plataforma Tesoura em Anápolis",
         "aluguel de plataforma tesoura no Porto Seco Anápolis"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura",
         "Aluguel de Plataforma Tesoura em Senador Canedo",
         "locação de plataforma tesoura no DASC Senador Canedo"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura",
         "Aluguel de Plataforma Tesoura em Brasília",
         "alugar plataforma tesoura no SIA Brasília DF"),
        ("/goiania-go/",
         "Todos os equipamentos em Goiânia",
         "ver todos os equipamentos para locação em Goiânia"),
        ("/cidades-atendidas",
         "Cidades atendidas pela Movemáquinas",
         "cidades com disponibilidade de aluguel em GO e DF"),
    ],

    # ===== LP TRANSPALETEIRA =====
    "aluguel-de-transpaleteira/index.html": [
        ("/goiania-go/",
         "Equipamentos em Goiânia",
         "locação de equipamentos em Goiânia"),
        ("/goiania-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira a Combustão em Goiânia",
         "locação de empilhadeira Clark para empresa em Goiânia"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-tesoura",
         "Aluguel de Plataforma Tesoura em Goiânia",
         "aluguel de plataforma tesoura para obra em Goiânia"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-articulada",
         "Aluguel de Plataforma Articulada em Goiânia",
         "locação de plataforma articulada em Goiânia GO"),
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "Curso de Operador de Empilhadeira em Goiânia",
         "habilitação NR-11 para operador de empilhadeira em Goiânia"),
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "curso de operador",
         "treinamento NR-11 para operador de empilhadeira"),
        ("/goiania-go/",
         "Goiânia",
         "aluguel de equipamentos em Goiânia GO"),
        ("/goiania-go/curso-de-operador-de-empilhadeira",
         "capacitação de operadores",
         "capacitação NR-11 para operador de empilhadeira em Goiânia"),
        # Cobertura
        ("/aparecida-de-goiania-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira em Aparecida de Goiânia",
         "locação de transpaleteira elétrica no DAIAG Aparecida GO"),
        ("/anapolis-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira em Anápolis",
         "aluguel de transpaleteira para depósito no DAIA Anápolis"),
        ("/senador-canedo-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira em Senador Canedo",
         "locação de transpaleteira no DASC Senador Canedo"),
        ("/trindade-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira em Trindade",
         "alugar transpaleteira Clark em Trindade GO"),
        ("/goiania-go/",
         "Todos os equipamentos em Goiânia",
         "ver todos os equipamentos para locação em Goiânia"),
        ("/cidades-atendidas",
         "Cidades atendidas pela Movemáquinas",
         "cidades com disponibilidade de aluguel em GO e DF"),
    ],

    # ===== LP CURSO =====
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/goiania-go/",
         "Goiânia",
         "aluguel de equipamentos em Goiânia GO"),
        # Cobertura de cursos em outras cidades
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira",
         "Curso de Operador de Empilhadeira em Aparecida de Goiânia",
         "curso NR-11 para operador de empilhadeira em Aparecida de Goiânia"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira",
         "Curso de Operador de Empilhadeira em Anápolis",
         "habilitação NR-11 para operador no DAIA Anápolis"),
        ("/trindade-go/curso-de-operador-de-empilhadeira",
         "Curso de Operador de Empilhadeira em Trindade",
         "treinamento NR-11 para operador de empilhadeira em Trindade GO"),
        ("/senador-canedo-go/curso-de-operador-de-empilhadeira",
         "Curso de Operador de Empilhadeira em Senador Canedo",
         "curso de operador de empilhadeira em Senador Canedo"),
        ("/goiania-go/",
         "Todos os equipamentos em Goiânia",
         "ver equipamentos para locação em Goiânia"),
        # Serviços irmãos — verbo de intenção presente
        ("/goiania-go/aluguel-de-empilhadeira-combustao",
         "Aluguel de Empilhadeira a Combustão",
         "locação de empilhadeira Clark em Goiânia"),
        ("/goiania-go/aluguel-de-transpaleteira",
         "Aluguel de Transpaleteira",
         "aluguel de transpaleteira elétrica no Polo da Moda Goiânia"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-articulada",
         "Plataforma Articulada",
         "locação de plataforma articulada para obra em Goiânia"),
        ("/goiania-go/aluguel-de-plataforma-elevatoria-tesoura",
         "Plataforma Tesoura",
         "aluguel de plataforma tesoura em Goiânia GO"),
        ("/cidades-atendidas",
         "Cidades atendidas",
         "cidades com disponibilidade de aluguel em GO e DF"),
    ],
}

# ---------------------------------------------------------------------------
# Engine de substituição
# ---------------------------------------------------------------------------

NAV_PATTERN = re.compile(
    r'(<header\b[^>]*>.*?</header>)',
    re.DOTALL | re.IGNORECASE
)
FOOTER_NAV_PATTERN = re.compile(
    r'(<div\s+class="[^"]*ft__col[^"]*"[^>]*>.*?</div>)',
    re.DOTALL | re.IGNORECASE
)

def strip_zone(html, pattern):
    zones = []
    def replacer(m):
        idx = len(zones)
        zones.append(m.group(0))
        return f"__ZONE_{idx}__"
    cleaned = pattern.sub(replacer, html)
    return cleaned, zones

def restore_zones(html, zones):
    for idx, content in enumerate(zones):
        html = html.replace(f"__ZONE_{idx}__", content)
    return html

def make_link_pattern(href, old_text):
    h = re.escape(href)
    t = re.escape(old_text.strip())
    return re.compile(
        r'(<a\b[^>]*href=["\']' + h + r'["\'][^>]*>)\s*' + t + r'\s*(</a>)',
        re.IGNORECASE | re.DOTALL
    )

def make_link_pattern_with_span(href, old_text):
    """Para links que contêm <span>SVG</span> antes do texto."""
    h = re.escape(href)
    t = re.escape(old_text.strip())
    return re.compile(
        r'(<a\b[^>]*href=["\']' + h + r'["\'][^>]*>)'
        r'(<span[^>]*>.*?</span>)\s*' + t + r'\s*(</a>)',
        re.IGNORECASE | re.DOTALL
    )

def apply_changes(filepath, changes, dry_run=False):
    with open(filepath, encoding="utf-8") as fh:
        original = fh.read()

    html = original
    applied = []
    skipped = []

    html, nav_zones = strip_zone(html, NAV_PATTERN)
    html, ft_zones = strip_zone(html, FOOTER_NAV_PATTERN)

    for href, old_text, new_text in changes:
        # Tenta padrão simples primeiro
        pat = make_link_pattern(href, old_text)
        match = pat.search(html)
        if match:
            html = pat.sub(f'{match.group(1)}{new_text}{match.group(2)}', html, count=1)
            applied.append((href, old_text, new_text))
            continue

        # Tenta padrão com <span> interno (ícones SVG)
        pat_span = make_link_pattern_with_span(href, old_text)
        match_span = pat_span.search(html)
        if match_span:
            html = pat_span.sub(
                lambda m: f'{m.group(1)}{m.group(2)}{new_text}{m.group(3)}',
                html, count=1
            )
            applied.append((href, old_text, new_text))
            continue

        skipped.append((href, old_text))

    html = restore_zones(html, nav_zones)
    html = restore_zones(html, ft_zones)

    if not dry_run and html != original:
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(html)

    return original, html, applied, skipped


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

print("=" * 70)
print("ANCHOR UPDATE v2 — goiania-go (piloto)")
print("Regra: verbo de intenção sempre presente (aluguel/locação/alugar/locar)")
print("=" * 70)

all_applied = {}
all_skipped = {}

for rel_path, changes in CHANGES.items():
    filepath = os.path.join(BASE, rel_path)
    original, updated, applied, skipped = apply_changes(filepath, changes, dry_run=False)
    all_applied[rel_path] = applied
    all_skipped[rel_path] = skipped

    page_label = rel_path.replace("/index.html", "") or "index"
    print(f"\n--- {page_label} ---")
    print(f"  Aplicadas: {len(applied)}")
    for href, old, new in applied:
        print(f"    ANTES : [{old}]")
        print(f"    DEPOIS: [{new}]")
    if skipped:
        print(f"  Nao encontradas: {len(skipped)}")
        for href, old in skipped:
            print(f"    ? [{old}] -> {href}")

print("\n" + "=" * 70)
total_a = sum(len(v) for v in all_applied.values())
total_s = sum(len(v) for v in all_skipped.values())
print(f"TOTAL aplicadas: {total_a} | nao encontradas: {total_s}")
print("=" * 70)
