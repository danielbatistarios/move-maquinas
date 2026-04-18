#!/usr/bin/env python3
"""
Script Master — Aplica as 14 alterações do Márcio em todas as páginas live.
Move Máquinas SEO — 30/03/2026
"""

import os
import re
import glob
import json
from itertools import cycle

BASE = "/Users/jrios/move-maquinas-seo"
R2 = "https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/assets/clark"

# ============================================================
# BANCO DE IMAGENS R2 — por tipo de serviço
# ============================================================

IMG_COMBUSTAO = [
    f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c60-80_application-for-web_01.jpg",
    f"{R2}/empilhadeira-combustao/gts-25-30-33/gts20-33-application-1039443432.jpg",
    f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c60-80_detail_operator_compartment-for-web.jpg",
    f"{R2}/empilhadeira-combustao/gts-25-30-33/clark_gts20-33_clipped-for-web.jpg",
    f"{R2}/empilhadeira-combustao/gts-25-30-33/clark_gts20-33_clipped_2-for-web.jpg",
    f"{R2}/empilhadeira-combustao/gts-25-30-33/gts25_100years.jpg",
    f"{R2}/empilhadeira-combustao/c60-70-75-80/c80_01.jpg",
    f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c70_clipped-for-web.jpg",
    f"{R2}/empilhadeira-combustao/l25-30-35/l20-launch-header.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_1.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_2.jpg",
]

IMG_TRANSPALETEIRA = [
    f"{R2}/transpaleteira/wpio15/wpio15_einsatz_img_4275.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16_application1.jpg",
    f"{R2}/transpaleteira/wpio20/wpio20_application-2.jpg",
    f"{R2}/transpaleteira/pwio20/clark_pwio20_01-.jpg",
    f"{R2}/transpaleteira/wpio15/wpio15_einsatz_img_4292.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16_application2.jpg",
    f"{R2}/transpaleteira/wpio20/wpio20_application-3.jpg",
    f"{R2}/transpaleteira/pwio20/clark_pwio20_03-.jpg",
    f"{R2}/transpaleteira/wpio15/wpio15_einsatz_laden_img_4262.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16_application3.jpg",
    f"{R2}/transpaleteira/wpio20/wpio20_application-4.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16_application4.jpg",
    f"{R2}/transpaleteira/wpio15/clark_wpio12-freisteller.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16-clipped2.jpg",
    f"{R2}/transpaleteira/wpio20/wpio20-10.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16-detail.jpg",
]

IMG_ARTICULADA_TESOURA = [
    f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c60-80_application-for-web_01.jpg",
    f"{R2}/empilhadeira-combustao/gts-25-30-33/gts20-33-application-1039443432.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_1.jpg",
    f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c60-80_detail_operator_compartment-for-web.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_2.jpg",
    f"{R2}/empilhadeira-combustao/gts-25-30-33/gts25_100years.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_3.jpg",
    f"{R2}/empilhadeira-combustao/c60-70-75-80/c80_01.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16_application1.jpg",
    f"{R2}/transpaleteira/wpio15/wpio15_einsatz_img_4275.jpg",
    f"{R2}/empilhadeira-combustao/l25-30-35/l20-launch-header.jpg",
    f"{R2}/transpaleteira/wpio20/wpio20_application-2.jpg",
]

IMG_CURSO = [
    f"{R2}/empilhadeira-combustao/gts-25-30-33/gts20-33-application-1039443432.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_1.jpg",
    f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c60-80_application-for-web_01.jpg",
    f"{R2}/transpaleteira/swx16/clark_swx16_application1.jpg",
    f"{R2}/empilhadeira-combustao/l25-30-35/l20-launch-header.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_2.jpg",
    f"{R2}/empilhadeira-combustao/gts-25-30-33/clark_gts20-33_clipped-for-web.jpg",
    f"{R2}/transpaleteira/wpio15/wpio15_einsatz_img_4275.jpg",
    f"{R2}/empilhadeira-combustao/c60-70-75-80/c80_01.jpg",
    f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_3.jpg",
]

# Cidades ordenadas para rotação determinística
CIDADES = [
    "anapolis", "aparecida", "brasilia", "caldas-novas", "formosa",
    "inhumas", "itumbiara", "luziania", "senador-canedo", "trindade",
    "uruacu", "valparaiso-de-goias"
]

def get_city_from_filename(fn):
    """Extrai prefixo da cidade do nome do arquivo."""
    base = os.path.basename(fn)
    for c in sorted(CIDADES, key=len, reverse=True):
        if base.startswith(c):
            return c
    return None

def get_service_type(fn):
    """Identifica tipo de serviço pelo nome do arquivo."""
    base = os.path.basename(fn)
    if "empilhadeira-combustao" in base:
        return "combustao"
    elif "articulada" in base:
        return "articulada"
    elif "tesoura" in base:
        return "tesoura"
    elif "transpaleteira" in base:
        return "transpaleteira"
    elif "curso" in base:
        return "curso"
    elif "hub" in base:
        return "hub"
    return "outro"

def get_unique_images(city, service_type):
    """Retorna 4 imagens únicas para a combinação cidade+serviço."""
    if service_type == "combustao":
        pool = IMG_COMBUSTAO
    elif service_type == "transpaleteira":
        pool = IMG_TRANSPALETEIRA
    elif service_type in ("articulada", "tesoura"):
        pool = IMG_ARTICULADA_TESOURA
    elif service_type == "curso":
        pool = IMG_CURSO
    else:
        return []

    city_idx = CIDADES.index(city) if city in CIDADES else 0
    # Offset por tipo de serviço para mais variação
    type_offset = {"combustao": 0, "articulada": 1, "tesoura": 2,
                   "transpaleteira": 3, "curso": 4}.get(service_type, 0)

    start = (city_idx * 4 + type_offset) % len(pool)
    imgs = []
    for i in range(4):
        imgs.append(pool[(start + i) % len(pool)])
    return imgs


# ============================================================
# SUBSTITUIÇÕES DE TEXTO (Itens 1-11, 14)
# ============================================================

def apply_text_fixes(html, filename):
    """Aplica todas as substituições de texto."""

    # --- Item 1: Nome da empresa → "Movemáquinas" ---
    html = html.replace("Move Maquinas", "Movemáquinas")
    html = html.replace("Move Máquinas", "Movemáquinas")
    # No schema.org JSON
    html = html.replace('"name":"Move Maquinas"', '"name":"Movemáquinas"')
    html = html.replace('"name":"Move Máquinas"', '"name":"Movemáquinas"')
    html = html.replace('"name": "Move Maquinas"', '"name": "Movemáquinas"')
    html = html.replace('"name": "Move Máquinas"', '"name": "Movemáquinas"')

    # --- Item 2: Remover "suporte 24h" → "horário comercial" ---
    html = html.replace("suporte 24h", "suporte em horário comercial")
    html = html.replace("suporte 24/7", "suporte em horário comercial")
    html = html.replace("Suporte 24h", "Suporte em horário comercial")
    html = html.replace("Assistência 24h", "Assistência em horário comercial")
    html = html.replace("Assistencia 24h", "Assistencia em horario comercial")
    html = html.replace("suporte técnico 24/7", "suporte técnico em horário comercial")
    html = html.replace("suporte tecnico 24/7", "suporte tecnico em horario comercial")
    html = re.sub(r'[Rr]esposta em at[eé] 24\s*h', 'Resposta em horário comercial', html)
    html = re.sub(r'[Ee]quipe t[eé]cnica mobile 24\s*h', 'Equipe técnica mobile em horário comercial', html)

    # --- Item 3: 13 cidades → 18 cidades ---
    html = re.sub(r'1[23] cidades', '18 cidades', html)

    # --- Item 4: +2.000 formados → +4.000 ---
    html = re.sub(r'\+\s*2\.?000\s*profissionais', '+4.000 profissionais', html)
    html = re.sub(r'mais de 2\.?000\s*profissionais', 'mais de 4.000 profissionais', html, flags=re.IGNORECASE)
    html = re.sub(r'\+2\.?000', '+4.000', html)

    # --- Item 5: Contatos com nomes Gabriel/Kaio ---
    # Em links de WhatsApp/telefone, adicionar nomes quando possível
    # Isso é mais complexo — só aplica em contextos de footer/contato
    html = re.sub(
        r'(<a[^>]*(?:wa\.me|tel:[^"]*982637300)[^>]*>[^<]*</a>)\s*(?!Gabriel)',
        r'\1 Gabriel — Locação',
        html
    )

    # --- Item 6: Links tel: → wa.me ---
    html = html.replace('href="tel:+5562982637300"', 'href="https://wa.me/5562982637300"')
    html = html.replace('href="tel:+55629826-37300"', 'href="https://wa.me/5562982637300"')
    html = html.replace("href='tel:+5562982637300'", "href='https://wa.me/5562982637300'")
    html = html.replace('href="tel:+5562981753350"', 'href="https://wa.me/5562981753350"')
    html = html.replace("href='tel:+5562981753350'", "href='https://wa.me/5562981753350'")

    # --- Item 7: "Centro-Oeste" → estados explícitos ---
    html = html.replace("todo o Centro-Oeste", "Goiás, DF, Tocantins e Mato Grosso")
    html = html.replace("Todo o Centro-Oeste", "Goiás, DF, Tocantins e Mato Grosso")
    html = html.replace("no Centro-Oeste", "em Goiás, DF, Tocantins e Mato Grosso")
    html = html.replace("do Centro-Oeste", "de Goiás, DF, Tocantins e Mato Grosso")
    # Cuidado: manter "Referência no Centro-Oeste" como está em H2s contextuais
    # Reverter caso tenha substituído dentro de H2
    html = html.replace(
        "Referência em Goiás, DF, Tocantins e Mato Grosso",
        "Referência no Centro-Oeste"
    )

    # --- Item 8: "Localização" → "Sede" ---
    html = html.replace("Nossa Localização em Goiânia", "Nossa Sede em Goiânia")
    html = html.replace("Nossa Localizacao em Goiania", "Nossa Sede em Goiania")
    html = html.replace("Nossa localização em Goiânia", "Nossa Sede em Goiânia")

    # --- Item 9: NR-35 → NR-18/NR-35 (só em páginas de plataforma) ---
    svc = get_service_type(filename)
    if svc in ("articulada", "tesoura"):
        # Substituir NR-35 por NR-18/NR-35 quando não já inclui NR-18
        html = re.sub(r'(?<!NR-18/)NR-35', 'NR-18/NR-35', html)
        # Evitar NR-18/NR-18/NR-35
        html = html.replace("NR-18/NR-18/NR-35", "NR-18/NR-35")

    # --- Item 10: Adicionar horário de funcionamento ---
    # Isso requer contexto específico — só aplica onde já tem contato/schema
    # Adicionar openingHours no schema se não existe
    if '"openingHoursSpecification"' not in html and '"LocalBusiness"' in html:
        opening_hours = ',"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"18:00"}]'
        # Inserir antes do último } do LocalBusiness
        html = html.replace('"sameAs":[', opening_hours + ',"sameAs":[', 1)

    # --- Item 11: Preços explícitos → "sob consulta" ---
    # priceRange no schema
    html = re.sub(
        r'"priceRange"\s*:\s*"R\$[^"]*"',
        '"priceRange": "$$"',
        html
    )
    # Meta descriptions com preço
    html = re.sub(r'A partir de R\$\s*[\d.]+/m[eê]s\.?', 'Valor sob consulta.', html)
    html = re.sub(r'a partir de R\$\s*[\d.]+/m[eê]s\.?', 'valor sob consulta.', html)
    html = re.sub(r'a partir de R\$\s*[\d.]+ mensais', 'valor sob consulta', html)
    html = re.sub(r'A partir de R\$\s*[\d.]+ mensais', 'Valor sob consulta', html)
    # Price cards: R$2.800 → Consultar
    html = re.sub(
        r'(<div class="price__card-value">)\s*R\$\s*2\.?800\s*(</div>)',
        r'\1Consultar\2',
        html
    )
    html = re.sub(
        r'(<div class="price__card-value">)\s*R\$\s*4\.?[05]00\s*(</div>)',
        r'\1Sob consulta\2',
        html
    )
    # Equip card prices in hubs
    html = re.sub(
        r'(<div class="equip-card__price">)\s*R\$\s*[\d.]+\s*(<small>)',
        r'\1Consultar \2',
        html
    )
    html = re.sub(
        r'(<div class="equip-card__price">)\s*A partir de R\$\s*[\d.]+\s*(<small>)',
        r'\1Consultar \2',
        html
    )
    # Hero lead com preço
    html = re.sub(r'A partir de R\$[\d.]+/m[eê]s\.', 'Valor sob consulta.', html)
    # Compare sections
    html = re.sub(r'A partir R\$[\d.]+', 'Sob consulta', html)
    html = re.sub(r'R\$2\.800 a R\$4\.[05]00/m[eê]s', 'valor sob consulta', html)
    html = re.sub(r'R\$[\d.]+ a R\$[\d.]+/m[eê]s', 'valor sob consulta', html)

    # --- Item 14: Garantir FCO (não FINAME) ---
    # Nenhum arquivo tem FINAME, mas por segurança:
    html = html.replace("FINAME", "FCO")
    html = html.replace("Finame", "FCO")
    html = html.replace("finame", "FCO")

    # --- Fix: áreaServed com acento ---
    html = html.replace('"áreaServed"', '"areaServed"')

    # --- Fix: preçonnect typo ---
    html = html.replace('rel="preçonnect"', 'rel="preconnect"')

    return html


def replace_pexels_images(html, filename):
    """Substitui imagens Pexels por R2, únicas por cidade+serviço."""
    city = get_city_from_filename(filename)
    svc = get_service_type(filename)

    if not city or svc in ("hub", "outro"):
        return html

    new_imgs = get_unique_images(city, svc)
    if not new_imgs:
        return html

    # Encontrar todas as URLs Pexels no arquivo
    pexels_pattern = r'https://images\.pexels\.com/photos/\d+/pexels-photo-\d+\.jpeg\?[^"\']*'
    pexels_urls = re.findall(pexels_pattern, html)

    # Substituir cada uma pela imagem R2 correspondente
    seen = set()
    unique_pexels = []
    for url in pexels_urls:
        if url not in seen:
            seen.add(url)
            unique_pexels.append(url)

    for i, pexels_url in enumerate(unique_pexels):
        if i < len(new_imgs):
            html = html.replace(pexels_url, new_imgs[i])

    return html


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def get_all_live_files():
    """Retorna todos os arquivos live para processar."""
    patterns = [
        os.path.join(BASE, "*-V2.html"),
        os.path.join(BASE, "*-BUILT.html"),
        os.path.join(BASE, "*-FINAL.html"),
    ]
    special = [
        "home.html", "home-index.html", "goiania-go-index.html",
        "goiania-articulada.html", "venda-clark.html", "servicos.html",
        "author-marcio-lima.html",
    ]

    files = []
    for p in patterns:
        files.extend(glob.glob(p))
    for s in special:
        path = os.path.join(BASE, s)
        if os.path.exists(path):
            files.append(path)

    # Hub V2s
    files.extend(glob.glob(os.path.join(BASE, "*-hub-V2.html")))

    # Ref pages
    files.extend(glob.glob(os.path.join(BASE, "ref-goiania-*.html")))

    return sorted(set(files))


def main():
    files = get_all_live_files()
    print(f"Total de arquivos para processar: {len(files)}")

    stats = {
        "processados": 0,
        "alterados": 0,
        "pexels_removidos": 0,
        "precos_removidos": 0,
        "nome_corrigido": 0,
    }

    for filepath in files:
        filename = os.path.basename(filepath)

        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()

        # Aplicar substituições de texto
        html = apply_text_fixes(original, filename)

        # Contar Pexels antes da troca
        pexels_before = len(re.findall(r'pexels\.com', html))

        # Substituir imagens Pexels
        html = replace_pexels_images(html, filename)

        pexels_after = len(re.findall(r'pexels\.com', html))

        if html != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            stats["alterados"] += 1

            if pexels_before > pexels_after:
                stats["pexels_removidos"] += (pexels_before - pexels_after)

            if "Move Maquinas" in original or "Move Máquinas" in original:
                stats["nome_corrigido"] += 1

            changes = []
            if "Move Maquinas" in original or "Move Máquinas" in original:
                changes.append("nome")
            if "24h" in original and "24h" not in html:
                changes.append("24h")
            if pexels_before > pexels_after:
                changes.append(f"pexels({pexels_before}→{pexels_after})")
            if re.search(r'R\$\s*2\.?800', original) and not re.search(r'R\$\s*2\.?800', html):
                changes.append("precos")

            print(f"  ✓ {filename} [{', '.join(changes) if changes else 'outros'}]")
        else:
            print(f"  · {filename} [sem alterações]")

        stats["processados"] += 1

    print(f"\n{'='*60}")
    print(f"RESUMO:")
    print(f"  Processados: {stats['processados']}")
    print(f"  Alterados:   {stats['alterados']}")
    print(f"  Imagens Pexels removidas: {stats['pexels_removidos']}")
    print(f"  Nomes corrigidos: {stats['nome_corrigido']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
