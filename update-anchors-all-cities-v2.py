#!/usr/bin/env python3
"""
Anchor text update — 12 cidades (exceto Goiânia) — v2
Textos old_text extraídos do HTML real em 2026-04-20.
Regra: verbo de intenção sempre presente nas âncoras de serviço.
"""

import re, os, sys

BASE = "/Users/jrios/move-maquinas-seo"

NAV_PATTERN = re.compile(r'(<header\b[^>]*>.*?</header>)', re.DOTALL | re.IGNORECASE)
FOOTER_NAV_PATTERN = re.compile(r'(<div\s+class="[^"]*ft__col[^"]*"[^>]*>.*?</div>)', re.DOTALL | re.IGNORECASE)

def make_link_pattern(href, old_text):
    t = re.escape(old_text.strip())
    return re.compile(
        r'(<a\b[^>]*href=["\']' + re.escape(href) + r'["\'][^>]*>)\s*' + t + r'\s*(</a>)',
        re.IGNORECASE | re.DOTALL
    )

def make_link_pattern_with_span(href, old_text):
    t = re.escape(old_text.strip())
    return re.compile(
        r'(<a\b[^>]*href=["\']' + re.escape(href) + r'["\'][^>]*>)(<span[^>]*>.*?</span>)\s*' + t + r'\s*(</a>)',
        re.IGNORECASE | re.DOTALL
    )

def strip_zone(html, pattern):
    zones = []
    def replacer(m):
        zones.append(m.group(0))
        return f'__ZONE_{len(zones)-1}__'
    return pattern.sub(replacer, html), zones

def restore_zones(html, zones):
    for i, z in enumerate(zones):
        html = html.replace(f'__ZONE_{i}__', z)
    return html

def apply_changes(filepath, changes, dry_run=False):
    if not os.path.exists(filepath):
        print(f"  MISSING: {filepath}")
        return 0, 0
    with open(filepath, encoding='utf-8') as f:
        html = f.read()

    html, nav_zones = strip_zone(html, NAV_PATTERN)
    html, footer_zones = strip_zone(html, FOOTER_NAV_PATTERN)

    applied = 0
    not_found = []

    for href, old_text, new_text in changes:
        pat = make_link_pattern(href, old_text)
        new_html, n = pat.subn(lambda m: m.group(1) + new_text + m.group(2), html)
        if n == 0:
            pat_span = make_link_pattern_with_span(href, old_text)
            new_html2, n2 = pat_span.subn(lambda m: m.group(1) + m.group(2) + new_text + m.group(3), html)
            if n2 > 0:
                html = new_html2
                applied += n2
                if not dry_run:
                    print(f"    ANTES (span): {old_text}")
                    print(f"    DEPOIS: {new_text}")
            else:
                not_found.append((old_text, href))
        else:
            html = new_html
            applied += n
            if not dry_run:
                print(f"    ANTES : {old_text}")
                print(f"    DEPOIS: {new_text}")

    html = restore_zones(html, nav_zones)
    html = restore_zones(html, footer_zones)

    if not dry_run and applied > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    for old, href in not_found:
        print(f"    ? [{old}] -> {href}")

    return applied, len(not_found)


# =============================================================================
# DADOS POR CIDADE — textos extraídos do HTML real
# =============================================================================

# Polos industriais por cidade (para ancoras de cobertura regional no hub)
# Hub changes já aplicados na v1 — não repetir aqui.
# Esta v2 foca apenas nas LPs (breadcrumbs + irmãos body).

APARECIDA = {
    # breadcrumb: "Equipamentos em Aparecida de Goiânia" -> "locação de equipamentos em Aparecida de Goiânia"
    # irmãos: padrão longo "Aluguel de X em Aparecida de Goiânia"
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/aparecida-de-goiania-go/", "Equipamentos em Aparecida de Goiânia", "locação de equipamentos em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-tesoura", "Aluguel de Plataforma Tesoura em Aparecida de Goiânia", "aluguel de plataforma tesoura no DAIAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-articulada", "Aluguel de Plataforma Articulada em Aparecida de Goiânia", "locação de plataforma articulada no DIMAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira em Aparecida de Goiânia", "aluguel de transpaleteira elétrica em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "Curso de Operador de Empilhadeira em Aparecida de Goiânia", "habilitação NR-11 para operador de empilhadeira em Aparecida GO"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "curso de operador de empilhadeira", "curso de operador NR-11 em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "curso NR-11 em Aparecida de Goiânia", "habilitação NR-11 no DAIAG Aparecida GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/aparecida-de-goiania-go/", "Equipamentos em Aparecida de Goiânia", "locação de equipamentos em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-tesoura", "Aluguel de Plataforma Tesoura em Aparecida de Goiânia", "aluguel de plataforma tesoura para obra no DAIAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão em Aparecida de Goiânia", "locação de empilhadeira a combustão no DIMAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira em Aparecida de Goiânia", "aluguel de transpaleteira elétrica em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "Curso de Operador de Empilhadeira em Aparecida de Goiânia", "habilitação NR-11 para operador de empilhadeira em Aparecida GO"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "treinamento para operadores", "treinamento NR-11 para operadores em Aparecida de Goiânia"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/aparecida-de-goiania-go/", "Equipamentos em Aparecida de Goiânia", "locação de equipamentos em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-articulada", "Aluguel de Plataforma Articulada em Aparecida de Goiânia", "locação de plataforma articulada para fachada no DAIAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão em Aparecida de Goiânia", "aluguel de empilhadeira a combustão no DIMAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira em Aparecida de Goiânia", "locação de transpaleteira elétrica em Aparecida de Goiânia"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/aparecida-de-goiania-go/", "Equipamentos em Aparecida de Goiânia", "locação de equipamentos em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão em Aparecida de Goiânia", "aluguel de empilhadeira a combustão no DAIAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-tesoura", "Aluguel de Plataforma Tesoura em Aparecida de Goiânia", "locação de plataforma tesoura para obra em Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-articulada", "Aluguel de Plataforma Articulada em Aparecida de Goiânia", "aluguel de plataforma articulada no DIMAG Aparecida GO"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "Curso de Operador de Empilhadeira em Aparecida de Goiânia", "habilitação NR-11 para operador de empilhadeira em Aparecida GO"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "curso de operador", "curso de operador de empilhadeira em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/curso-de-operador-de-empilhadeira", "curso em Aparecida de Goiânia", "habilitação NR-11 no DAIAG Aparecida de Goiânia"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/aparecida-de-goiania-go/", "Equipamentos em Aparecida de Goiânia", "locação de equipamentos em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no DAIAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Aparecida de Goiânia"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Aparecida GO", "locação de plataforma articulada no DIMAG Aparecida GO"),
        ("/aparecida-de-goiania-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Aparecida de Goiânia GO", "aluguel de plataforma tesoura para obra em Aparecida GO"),
    ],
}

ANAPOLIS = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/anapolis-go/", "Equipamentos em Anápolis", "locação de equipamentos em Anápolis GO"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "NR-11", "habilitação NR-11 para operadores no DAIA Anápolis"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "curso de operador de empilhadeira", "curso de operador de empilhadeira em Anápolis GO"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "curso NR-11 em Anápolis", "habilitação NR-11 para empilhadeira no DAIA Anápolis"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/anapolis-go/", "Equipamentos em Anápolis", "locação de equipamentos em Anápolis GO"),
        ("/anapolis-go/aluguel-de-plataforma-elevatoria-tesoura", "Aluguel de Plataforma Tesoura em Anápolis", "aluguel de plataforma tesoura para obra no Porto Seco Anápolis"),
        ("/anapolis-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão em Anápolis", "locação de empilhadeira a combustão no DAIA Anápolis GO"),
        ("/anapolis-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira em Anápolis", "aluguel de transpaleteira elétrica em Anápolis GO"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "Curso de Operador de Empilhadeira em Anápolis", "habilitação NR-11 para operador de empilhadeira em Anápolis GO"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "treinamento para operadores", "treinamento NR-11 para operadores no DAIA Anápolis"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "curso de operador NR-11", "habilitação NR-11 para empilhadeira no Porto Seco Anápolis"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/anapolis-go/", "Equipamentos em Anápolis", "locação de equipamentos em Anápolis GO"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "NR-18/NR-35", "habilitação NR-35 para trabalho em altura no DAIA Anápolis"),
        ("/anapolis-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para fachada no DAIA Anápolis", "locação de plataforma articulada para reforma no Porto Seco Anápolis"),
        ("/anapolis-go/aluguel-de-empilhadeira-combustao", "empilhadeira a combustão", "aluguel de empilhadeira a combustão no DAIA Anápolis GO"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/anapolis-go/", "Equipamentos em Anápolis", "locação de equipamentos em Anápolis GO"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "NR-11", "habilitação NR-11 para operadores no DAIA Anápolis"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "curso de operador", "curso de operador de empilhadeira em Anápolis GO"),
        ("/anapolis-go/curso-de-operador-de-empilhadeira", "curso NR-11 em Anápolis", "habilitação NR-11 para empilhadeira no Porto Seco Anápolis"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/anapolis-go/", "Anápolis", "locação de equipamentos em Anápolis GO"),
        ("/anapolis-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no DAIA Anápolis GO"),
        ("/anapolis-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Anápolis GO"),
        ("/anapolis-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Anápolis", "locação de plataforma articulada no Porto Seco Anápolis GO"),
        ("/anapolis-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Anápolis GO", "aluguel de plataforma tesoura para obra em Anápolis GO"),
    ],
}

SENADOR_CANEDO = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/senador-canedo-go/", "Equipamentos em Senador Canedo", "locação de equipamentos em Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura", "Aluguel de Plataforma Tesoura em Senador Canedo", "aluguel de plataforma tesoura no DASC Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada", "Aluguel de Plataforma Articulada em Senador Canedo", "locação de plataforma articulada no Complexo Petroquímico Canedo"),
        ("/senador-canedo-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira em Senador Canedo", "aluguel de transpaleteira elétrica em Senador Canedo GO"),
        ("/senador-canedo-go/curso-de-operador-de-empilhadeira", "Curso de Operador de Empilhadeira em Senador Canedo", "habilitação NR-11 para operador de empilhadeira em Senador Canedo"),
        ("/senador-canedo-go/curso-de-operador-de-empilhadeira", "curso de operador de empilhadeira", "curso de operador NR-11 no DASC Senador Canedo"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/senador-canedo-go/", "Equipamentos em Senador Canedo", "locação de equipamentos em Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura", "Aluguel de Plataforma Tesoura em Senador Canedo", "aluguel de plataforma tesoura para obra no DASC Senador Canedo"),
        ("/senador-canedo-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão em Senador Canedo", "locação de empilhadeira a combustão no Complexo Petroquímico Canedo"),
        ("/senador-canedo-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira em Senador Canedo", "aluguel de transpaleteira elétrica em Senador Canedo GO"),
        ("/senador-canedo-go/curso-de-operador-de-empilhadeira", "Curso de Operador de Empilhadeira em Senador Canedo", "habilitação NR-11 para operador de empilhadeira em Senador Canedo"),
        ("/senador-canedo-go/curso-de-operador-de-empilhadeira", "treinamento para operadores", "treinamento NR-11 para operadores no DASC Senador Canedo"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/senador-canedo-go/", "Equipamentos em Senador Canedo", "locação de equipamentos em Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada", "Aluguel de Plataforma Articulada em Senador Canedo", "locação de plataforma articulada para fachada no DASC Senador Canedo"),
        ("/senador-canedo-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão em Senador Canedo", "aluguel de empilhadeira a combustão no Complexo Petroquímico Canedo"),
        ("/senador-canedo-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira em Senador Canedo", "locação de transpaleteira elétrica em Senador Canedo GO"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/senador-canedo-go/", "Equipamentos em Senador Canedo", "locação de equipamentos em Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão em Senador Canedo", "aluguel de empilhadeira a combustão no DASC Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura", "Aluguel de Plataforma Tesoura em Senador Canedo", "locação de plataforma tesoura para obra em Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada", "Aluguel de Plataforma Articulada em Senador Canedo", "aluguel de plataforma articulada no Complexo Petroquímico Canedo"),
        ("/senador-canedo-go/curso-de-operador-de-empilhadeira", "Curso de Operador de Empilhadeira em Senador Canedo", "habilitação NR-11 para operador de empilhadeira em Senador Canedo"),
        ("/senador-canedo-go/curso-de-operador-de-empilhadeira", "curso de operador", "curso de operador de empilhadeira no DASC Senador Canedo"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/senador-canedo-go/", "Senador Canedo", "locação de equipamentos em Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no DASC Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Senador Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Senador Canedo", "locação de plataforma articulada no Complexo Petroquímico Canedo GO"),
        ("/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Senador Canedo GO", "aluguel de plataforma tesoura para obra no DASC Senador Canedo"),
    ],
}

BRASILIA = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/brasilia-df/", "Equipamentos em Brasília", "locação de equipamentos em Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Brasília", "aluguel de plataforma tesoura no SIA Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Brasília", "locação de plataforma articulada na Ceilândia Industrial Brasília"),
        ("/brasilia-df/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Brasília", "aluguel de transpaleteira elétrica em Brasília DF"),
        ("/brasilia-df/curso-de-operador-de-empilhadeira", "Curso NR-11 em Brasília", "habilitação NR-11 para operador de empilhadeira em Brasília DF"),
        ("/brasilia-df/curso-de-operador-de-empilhadeira", "curso de operador de empilhadeira", "curso de operador de empilhadeira em Brasília DF"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/brasilia-df/", "Equipamentos em Brasília", "locação de equipamentos em Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Brasília", "aluguel de plataforma tesoura para obra no SIA Brasília DF"),
        ("/brasilia-df/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Brasília", "locação de empilhadeira a combustão no SIA Brasília DF"),
        ("/brasilia-df/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Brasília", "aluguel de transpaleteira elétrica em Brasília DF"),
        ("/brasilia-df/curso-de-operador-de-empilhadeira", "Curso NR-11 em Brasília", "habilitação NR-11 para operador de empilhadeira em Brasília DF"),
        ("/brasilia-df/curso-de-operador-de-empilhadeira", "capacitação NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura no SIA Brasília DF"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/brasilia-df/", "Equipamentos em Brasília", "locação de equipamentos em Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Brasília", "locação de plataforma articulada no SIA Brasília DF"),
        ("/brasilia-df/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Brasília", "aluguel de empilhadeira a combustão na Ceilândia Industrial Brasília"),
        ("/brasilia-df/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Brasília", "locação de transpaleteira elétrica em Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada no SIA Brasília DF", "locação de plataforma articulada para fachada na Ceilândia Industrial DF"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/brasilia-df/", "Equipamentos em Brasília", "locação de equipamentos em Brasília DF"),
        ("/brasilia-df/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Brasília", "aluguel de empilhadeira a combustão no SIA Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Brasília", "locação de plataforma tesoura para obra em Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Brasília", "aluguel de plataforma articulada na Ceilândia Industrial Brasília"),
        ("/brasilia-df/curso-de-operador-de-empilhadeira", "Curso NR-11 em Brasília", "habilitação NR-11 para operador de empilhadeira em Brasília DF"),
        ("/brasilia-df/curso-de-operador-de-empilhadeira", "curso de operador NR-11", "curso de operador de empilhadeira no SIA Brasília DF"),
        ("/brasilia-df/curso-de-operador-de-empilhadeira", "curso NR-11 para Brasília", "habilitação NR-11 para operadores na Ceilândia Industrial DF"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/brasilia-df/", "Brasília-DF", "locação de equipamentos em Brasília DF"),
        ("/brasilia-df/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Brasília", "aluguel de empilhadeira a combustão no SIA Brasília DF"),
        ("/brasilia-df/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Brasília", "locação de transpaleteira elétrica em Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Brasília", "locação de plataforma articulada no SIA Brasília DF"),
        ("/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Brasília", "aluguel de plataforma tesoura para obra na Ceilândia Industrial DF"),
    ],
}

LUZIANIA = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/luziania-go/", "Equipamentos em Luziânia", "locação de equipamentos em Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Luziânia", "aluguel de plataforma tesoura no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Luziânia", "locação de plataforma articulada no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Luziânia", "aluguel de transpaleteira elétrica em Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Luziânia", "habilitação NR-11 para operador de empilhadeira em Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "curso NR-11 para operadores de empilhadeira", "curso de operador NR-11 no DIAL Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "habilitação NR-11 para empilhadeira em Luziânia GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/luziania-go/", "Equipamentos em Luziânia", "locação de equipamentos em Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Luziania", "aluguel de plataforma tesoura para obra no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustao em Luziania", "locação de empilhadeira a combustão no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-transpaleteira", "Transpaleteira Eletrica em Luziania", "aluguel de transpaleteira elétrica em Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Luziania", "habilitação NR-11 para operador de empilhadeira em Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "capacitacao NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura no DIAL Luziânia GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/luziania-go/", "Equipamentos em Luziânia", "locação de equipamentos em Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Luziânia", "locação de plataforma articulada para fachada no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Luziânia", "aluguel de empilhadeira a combustão no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Luziânia", "locação de transpaleteira elétrica em Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para fachada em Luziânia GO", "locação de plataforma articulada para reforma no DIAL Luziânia GO"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/luziania-go/", "Equipamentos em Luziânia", "locação de equipamentos em Luziânia GO"),
        ("/luziania-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Luziânia", "aluguel de empilhadeira a combustão no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Luziânia", "locação de plataforma tesoura para obra em Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Luziânia", "aluguel de plataforma articulada no DIAL Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Luziânia", "habilitação NR-11 para operador de empilhadeira em Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores", "curso de operador NR-11 no DIAL Luziânia GO"),
        ("/luziania-go/curso-de-operador-de-empilhadeira", "capacitação e reciclagem", "habilitação e reciclagem NR-11 em Luziânia GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/luziania-go/", "Luziânia", "locação de equipamentos em Luziânia GO"),
        ("/luziania-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Luziânia", "locação de plataforma articulada no DIAL Luziânia GO"),
        ("/luziania-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Luziânia GO", "aluguel de plataforma tesoura para obra em Luziânia GO"),
    ],
}

TRINDADE = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/trindade-go/", "Equipamentos em Trindade", "locação de equipamentos em Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Trindade", "aluguel de plataforma tesoura no Polo Industrial de Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Trindade", "locação de plataforma articulada em Trindade GO"),
        ("/trindade-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Trindade", "aluguel de transpaleteira elétrica em Trindade GO"),
        ("/trindade-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Trindade", "habilitação NR-11 para operador de empilhadeira em Trindade GO"),
        ("/trindade-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "curso de operador NR-11 no Polo Industrial de Trindade GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/trindade-go/", "Equipamentos em Trindade", "locação de equipamentos em Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Trindade", "aluguel de plataforma tesoura para obra no Polo Industrial de Trindade"),
        ("/trindade-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Trindade", "locação de empilhadeira a combustão em Trindade GO"),
        ("/trindade-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Trindade", "aluguel de transpaleteira elétrica em Trindade GO"),
        ("/trindade-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Trindade", "habilitação NR-11 para operador de empilhadeira em Trindade GO"),
        ("/trindade-go/curso-de-operador-de-empilhadeira", "capacitação NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura em Trindade GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/trindade-go/", "Equipamentos em Trindade", "locação de equipamentos em Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Trindade", "locação de plataforma articulada para fachada em Trindade GO"),
        ("/trindade-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Trindade", "aluguel de empilhadeira a combustão no Polo Industrial de Trindade GO"),
        ("/trindade-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Trindade", "locação de transpaleteira elétrica em Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para fachada em Trindade GO", "locação de plataforma articulada para reforma no Polo Industrial de Trindade"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/trindade-go/", "Equipamentos em Trindade", "locação de equipamentos em Trindade GO"),
        ("/trindade-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Trindade", "aluguel de empilhadeira a combustão no Polo Industrial de Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Trindade", "locação de plataforma tesoura para obra em Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Trindade", "aluguel de plataforma articulada em Trindade GO"),
        ("/trindade-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Trindade", "habilitação NR-11 para operador de empilhadeira em Trindade GO"),
        ("/trindade-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores", "curso de operador NR-11 no Polo Industrial de Trindade GO"),
        ("/trindade-go/curso-de-operador-de-empilhadeira", "capacitação e reciclagem", "habilitação e reciclagem NR-11 em Trindade GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/trindade-go/", "Trindade", "locação de equipamentos em Trindade GO"),
        ("/trindade-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no Polo Industrial de Trindade GO"),
        ("/trindade-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Trindade GO", "locação de plataforma articulada em Trindade GO"),
        ("/trindade-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Trindade GO", "aluguel de plataforma tesoura para obra em Trindade GO"),
    ],
}

INHUMAS = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/inhumas-go/", "Equipamentos em Inhumas", "locação de equipamentos em Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Inhumas", "aluguel de plataforma tesoura no Distrito Industrial de Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Inhumas", "locação de plataforma articulada em Inhumas GO"),
        ("/inhumas-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Inhumas", "aluguel de transpaleteira elétrica em Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Inhumas", "habilitação NR-11 para operador de empilhadeira em Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "curso NR-11 para operadores de empilhadeira", "curso de operador NR-11 no Distrito Industrial de Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "habilitação NR-11 para empilhadeira em Inhumas GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/inhumas-go/", "Equipamentos em Inhumas", "locação de equipamentos em Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Inhumas", "aluguel de plataforma tesoura para obra no Distrito Industrial de Inhumas"),
        ("/inhumas-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Inhumas", "locação de empilhadeira a combustão em Inhumas GO"),
        ("/inhumas-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Inhumas", "aluguel de transpaleteira elétrica em Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Inhumas", "habilitação NR-11 para operador de empilhadeira em Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "capacitação NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura em Inhumas GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/inhumas-go/", "Equipamentos em Inhumas", "locação de equipamentos em Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Inhumas", "locação de plataforma articulada para fachada em Inhumas GO"),
        ("/inhumas-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Inhumas", "aluguel de empilhadeira a combustão no Distrito Industrial de Inhumas GO"),
        ("/inhumas-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Inhumas", "locação de transpaleteira elétrica em Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para fachada em Inhumas GO", "locação de plataforma articulada para obra no Distrito Industrial de Inhumas"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/inhumas-go/", "Equipamentos em Inhumas", "locação de equipamentos em Inhumas GO"),
        ("/inhumas-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Inhumas", "aluguel de empilhadeira a combustão no Distrito Industrial de Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Inhumas", "locação de plataforma tesoura para obra em Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Inhumas", "aluguel de plataforma articulada em Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Inhumas", "habilitação NR-11 para operador de empilhadeira em Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores", "curso de operador NR-11 no Distrito Industrial de Inhumas GO"),
        ("/inhumas-go/curso-de-operador-de-empilhadeira", "capacitação e reciclagem", "habilitação e reciclagem NR-11 em Inhumas GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/inhumas-go/", "Inhumas", "locação de equipamentos em Inhumas GO"),
        ("/inhumas-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no Distrito Industrial de Inhumas GO"),
        ("/inhumas-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Inhumas GO", "locação de plataforma articulada em Inhumas GO"),
        ("/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Inhumas GO", "aluguel de plataforma tesoura para obra em Inhumas GO"),
    ],
}

ITUMBIARA = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/itumbiara-go/", "Equipamentos em Itumbiara", "locação de equipamentos em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Itumbiara", "aluguel de plataforma tesoura no Polo Sucroalcooleiro de Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Itumbiara", "locação de plataforma articulada em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Itumbiara", "aluguel de transpaleteira elétrica em Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Itumbiara", "habilitação NR-11 para operador de empilhadeira em Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "curso NR-11 para operadores de empilhadeira", "curso de operador NR-11 no Polo Sucroalcooleiro Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "habilitação NR-11 para empilhadeira em Itumbiara GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/itumbiara-go/", "Equipamentos em Itumbiara", "locação de equipamentos em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Itumbiara", "aluguel de plataforma tesoura para obra no Polo Sucroalcooleiro Itumbiara"),
        ("/itumbiara-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustao em Itumbiara", "locação de empilhadeira a combustão em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-transpaleteira", "Transpaleteira Eletrica em Itumbiara", "aluguel de transpaleteira elétrica em Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Itumbiara", "habilitação NR-11 para operador de empilhadeira em Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "capacitacao NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura em Itumbiara GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/itumbiara-go/", "Equipamentos em Itumbiara", "locação de equipamentos em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Itumbiara", "locação de plataforma articulada para fachada em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Itumbiara", "aluguel de empilhadeira a combustão no Polo Sucroalcooleiro Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Itumbiara", "locação de transpaleteira elétrica em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada em Itumbiara GO", "locação de plataforma articulada para obra no Polo Sucroalcooleiro Itumbiara"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/itumbiara-go/", "Equipamentos em Itumbiara", "locação de equipamentos em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Itumbiara", "aluguel de empilhadeira a combustão no Polo Sucroalcooleiro Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Itumbiara", "locação de plataforma tesoura para obra em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Itumbiara", "aluguel de plataforma articulada em Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Itumbiara", "habilitação NR-11 para operador de empilhadeira em Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores", "curso de operador NR-11 no Polo Sucroalcooleiro Itumbiara GO"),
        ("/itumbiara-go/curso-de-operador-de-empilhadeira", "capacitação e reciclagem", "habilitação e reciclagem NR-11 em Itumbiara GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/itumbiara-go/", "Itumbiara", "locação de equipamentos em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no Polo Sucroalcooleiro Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Itumbiara GO", "locação de plataforma articulada em Itumbiara GO"),
        ("/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Itumbiara GO", "aluguel de plataforma tesoura para obra em Itumbiara GO"),
    ],
}

CALDAS_NOVAS = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/caldas-novas-go/", "Equipamentos em Caldas Novas", "locação de equipamentos em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Caldas Novas", "aluguel de plataforma tesoura no Polo Hoteleiro de Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Caldas Novas", "locação de plataforma articulada em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Caldas Novas", "aluguel de transpaleteira elétrica em Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Caldas Novas", "habilitação NR-11 para operador de empilhadeira em Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "curso NR-11 para operadores de empilhadeira", "curso de operador NR-11 no Polo Hoteleiro Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "habilitação NR-11 para empilhadeira em Caldas Novas GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/caldas-novas-go/", "Equipamentos em Caldas Novas", "locação de equipamentos em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Caldas Novas", "aluguel de plataforma tesoura para obra no Polo Hoteleiro Caldas Novas"),
        ("/caldas-novas-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Caldas Novas", "locação de empilhadeira a combustão em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Caldas Novas", "aluguel de transpaleteira elétrica em Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Caldas Novas", "habilitação NR-11 para operador de empilhadeira em Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "capacitação NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura em Caldas Novas GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/caldas-novas-go/", "Equipamentos em Caldas Novas", "locação de equipamentos em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Caldas Novas", "locação de plataforma articulada para fachada em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Caldas Novas", "aluguel de empilhadeira a combustão no Polo Hoteleiro Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Caldas Novas", "locação de transpaleteira elétrica em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada em Caldas Novas GO", "locação de plataforma articulada para obra no Polo Hoteleiro Caldas Novas"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/caldas-novas-go/", "Equipamentos em Caldas Novas", "locação de equipamentos em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Caldas Novas", "aluguel de empilhadeira a combustão no Polo Hoteleiro Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Caldas Novas", "locação de plataforma tesoura para obra em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Caldas Novas", "aluguel de plataforma articulada em Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Caldas Novas", "habilitação NR-11 para operador de empilhadeira em Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores", "curso de operador NR-11 no Polo Hoteleiro Caldas Novas GO"),
        ("/caldas-novas-go/curso-de-operador-de-empilhadeira", "capacitação e reciclagem", "habilitação e reciclagem NR-11 em Caldas Novas GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/caldas-novas-go/", "Caldas Novas", "locação de equipamentos em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no Polo Hoteleiro Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Caldas Novas GO", "locação de plataforma articulada em Caldas Novas GO"),
        ("/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Caldas Novas GO", "aluguel de plataforma tesoura para obra em Caldas Novas GO"),
    ],
}

FORMOSA = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/formosa-go/", "Equipamentos em Formosa", "locação de equipamentos em Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Formosa", "aluguel de plataforma tesoura no Polo Agropecuário de Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Formosa", "locação de plataforma articulada em Formosa GO"),
        ("/formosa-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Formosa", "aluguel de transpaleteira elétrica em Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "Curso NR-11 para Operadores em Formosa", "habilitação NR-11 para operador de empilhadeira em Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "curso NR-11 para operadores de empilhadeira", "curso de operador NR-11 no Polo Agropecuário Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "habilitação NR-11 para empilhadeira em Formosa GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/formosa-go/", "Equipamentos em Formosa", "locação de equipamentos em Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Formosa", "aluguel de plataforma tesoura para obra no Polo Agropecuário Formosa"),
        ("/formosa-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Formosa", "locação de empilhadeira a combustão em Formosa GO"),
        ("/formosa-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Formosa", "aluguel de transpaleteira elétrica em Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Formosa", "habilitação NR-11 para operador de empilhadeira em Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "capacitação NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura em Formosa GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/formosa-go/", "Equipamentos em Formosa", "locação de equipamentos em Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Formosa", "locação de plataforma articulada para fachada em Formosa GO"),
        ("/formosa-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Formosa", "aluguel de empilhadeira a combustão no Polo Agropecuário Formosa GO"),
        ("/formosa-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Formosa", "locação de transpaleteira elétrica em Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada em Formosa GO", "locação de plataforma articulada para obra no Polo Agropecuário Formosa"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/formosa-go/", "Equipamentos em Formosa", "locação de equipamentos em Formosa GO"),
        ("/formosa-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Formosa", "aluguel de empilhadeira a combustão no Polo Agropecuário Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Formosa", "locação de plataforma tesoura para obra em Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Formosa", "aluguel de plataforma articulada em Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Formosa", "habilitação NR-11 para operador de empilhadeira em Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores de transpaleteira", "curso de operador NR-11 no Polo Agropecuário Formosa GO"),
        ("/formosa-go/curso-de-operador-de-empilhadeira", "capacitação dos operadores", "habilitação e reciclagem NR-11 em Formosa GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/formosa-go/", "Formosa", "locação de equipamentos em Formosa GO"),
        ("/formosa-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no Polo Agropecuário Formosa GO"),
        ("/formosa-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Formosa GO", "locação de plataforma articulada em Formosa GO"),
        ("/formosa-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Formosa GO", "aluguel de plataforma tesoura para obra em Formosa GO"),
    ],
}

URUACU = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/uruacu-go/", "Equipamentos em Uruaçu", "locação de equipamentos em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Uruaçu", "aluguel de plataforma tesoura no Polo Agropecuário Norte de Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Uruaçu", "locação de plataforma articulada em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Uruaçu", "aluguel de transpaleteira elétrica em Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Uruaçu", "habilitação NR-11 para operador de empilhadeira em Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "curso NR-11 para operadores de empilhadeira", "curso de operador NR-11 no Polo Agropecuário Norte Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "habilitação NR-11 para empilhadeira em Uruaçu GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/uruacu-go/", "Equipamentos em Uruaçu", "locação de equipamentos em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Uruaçu", "aluguel de plataforma tesoura para obra no Polo Agropecuário Norte Uruaçu"),
        ("/uruacu-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Uruaçu", "locação de empilhadeira a combustão em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Uruaçu", "aluguel de transpaleteira elétrica em Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Uruaçu", "habilitação NR-11 para operador de empilhadeira em Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "capacitação NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura em Uruaçu GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/uruacu-go/", "Equipamentos em Uruaçu", "locação de equipamentos em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Uruaçu", "locação de plataforma articulada para fachada em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Uruaçu", "aluguel de empilhadeira a combustão no Polo Agropecuário Norte Uruaçu GO"),
        ("/uruacu-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Uruaçu", "locação de transpaleteira elétrica em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada em Uruaçu GO", "locação de plataforma articulada para obra no Polo Agropecuário Norte Uruaçu"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/uruacu-go/", "Equipamentos em Uruaçu", "locação de equipamentos em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Uruaçu", "aluguel de empilhadeira a combustão no Polo Agropecuário Norte Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Uruaçu", "locação de plataforma tesoura para obra em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Uruaçu", "aluguel de plataforma articulada em Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Uruaçu", "habilitação NR-11 para operador de empilhadeira em Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores", "curso de operador NR-11 no Polo Agropecuário Norte Uruaçu GO"),
        ("/uruacu-go/curso-de-operador-de-empilhadeira", "certificação e reciclagem periódica", "habilitação e reciclagem NR-11 em Uruaçu GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/uruacu-go/", "Uruaçu", "locação de equipamentos em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no Polo Agropecuário Norte Uruaçu GO"),
        ("/uruacu-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Uruaçu GO", "locação de plataforma articulada em Uruaçu GO"),
        ("/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Uruaçu GO", "aluguel de plataforma tesoura para obra em Uruaçu GO"),
    ],
}

VALPARAISO = {
    "aluguel-de-empilhadeira-combustao/index.html": [
        ("/valparaiso-de-goias-go/", "Equipamentos em Valparaíso de Goiás", "locação de equipamentos em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Valparaíso de Goiás", "aluguel de plataforma tesoura no Polo Moveleiro de Valparaíso GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Valparaíso de Goiás", "locação de plataforma articulada em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Valparaíso de Goiás", "aluguel de transpaleteira elétrica em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Valparaíso de Goiás", "habilitação NR-11 para operador de empilhadeira em Valparaíso GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "curso NR-11 para operadores de empilhadeira", "curso de operador NR-11 no Polo Moveleiro Valparaíso GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "curso NR-11 de operador de empilhadeira", "habilitação NR-11 para empilhadeira em Valparaíso de Goiás GO"),
    ],
    "aluguel-de-plataforma-elevatoria-articulada/index.html": [
        ("/valparaiso-de-goias-go/", "Equipamentos em Valparaíso de Goiás", "locação de equipamentos em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Valparaíso de Goiás", "aluguel de plataforma tesoura para obra no Polo Moveleiro Valparaíso"),
        ("/valparaiso-de-goias-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Valparaíso de Goiás", "locação de empilhadeira a combustão em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Valparaíso de Goiás", "aluguel de transpaleteira elétrica em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Valparaíso de Goiás", "habilitação NR-11 para operador de empilhadeira em Valparaíso GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "capacitação NR-18/NR-35 para operadores", "habilitação NR-35 para trabalho em altura em Valparaíso de Goiás GO"),
    ],
    "aluguel-de-plataforma-elevatoria-tesoura/index.html": [
        ("/valparaiso-de-goias-go/", "Equipamentos em Valparaíso de Goiás", "locação de equipamentos em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Valparaíso de Goiás", "locação de plataforma articulada para fachada em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Valparaíso de Goiás", "aluguel de empilhadeira a combustão no Polo Moveleiro Valparaíso GO"),
        ("/valparaiso-de-goias-go/aluguel-de-transpaleteira", "Transpaleteira Elétrica em Valparaíso de Goiás", "locação de transpaleteira elétrica em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada em Valparaíso de Goiás", "locação de plataforma articulada para obra no Polo Moveleiro Valparaíso"),
    ],
    "aluguel-de-transpaleteira/index.html": [
        ("/valparaiso-de-goias-go/", "Equipamentos em Valparaíso de Goiás", "locação de equipamentos em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-empilhadeira-combustao", "Empilhadeira a Combustão em Valparaíso de Goiás", "aluguel de empilhadeira a combustão no Polo Moveleiro Valparaíso GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-tesoura", "Plataforma Tesoura em Valparaíso de Goiás", "locação de plataforma tesoura para obra em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-articulada", "Plataforma Articulada em Valparaíso de Goiás", "aluguel de plataforma articulada em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "Curso NR-11 em Valparaíso de Goiás", "habilitação NR-11 para operador de empilhadeira em Valparaíso GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "capacitação NR-11 para operadores", "curso de operador NR-11 no Polo Moveleiro Valparaíso GO"),
        ("/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira", "certificação e reciclagem", "habilitação e reciclagem NR-11 em Valparaíso de Goiás GO"),
    ],
    "curso-de-operador-de-empilhadeira/index.html": [
        ("/valparaiso-de-goias-go/", "Valparaíso de Goiás", "locação de equipamentos em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-empilhadeira-combustao", "Aluguel de Empilhadeira a Combustão", "aluguel de empilhadeira a combustão no Polo Moveleiro Valparaíso GO"),
        ("/valparaiso-de-goias-go/aluguel-de-transpaleteira", "Aluguel de Transpaleteira", "locação de transpaleteira elétrica em Valparaíso de Goiás GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-articulada", "locação de plataforma articulada para obra em Valparaíso GO", "locação de plataforma articulada no Polo Moveleiro Valparaíso GO"),
        ("/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-tesoura", "aluguel de plataforma tesoura em Valparaíso de Goiás GO", "aluguel de plataforma tesoura para obra em Valparaíso de Goiás GO"),
    ],
}

CITY_MAP = {
    "aparecida-de-goiania-go": APARECIDA,
    "anapolis-go": ANAPOLIS,
    "senador-canedo-go": SENADOR_CANEDO,
    "brasilia-df": BRASILIA,
    "luziania-go": LUZIANIA,
    "trindade-go": TRINDADE,
    "inhumas-go": INHUMAS,
    "itumbiara-go": ITUMBIARA,
    "caldas-novas-go": CALDAS_NOVAS,
    "formosa-go": FORMOSA,
    "uruacu-go": URUACU,
    "valparaiso-de-goias-go": VALPARAISO,
}

# =============================================================================
# EXECUÇÃO
# =============================================================================

DRY_RUN = "--dry-run" in sys.argv

print("=" * 70)
print("ANCHOR UPDATE v2 — LPs das 12 cidades (breadcrumbs + irmãos body)")
print("Textos extraídos do HTML real em 2026-04-20")
print("=" * 70)

grand_applied = 0
grand_not_found = 0

for city_slug, city_data in CITY_MAP.items():
    print(f"\n{'='*50}")
    print(f"CIDADE: {city_slug}")
    print("=" * 50)
    city_applied = 0
    city_not_found = 0

    for file_key, changes in city_data.items():
        filepath = os.path.join(BASE, city_slug, file_key)
        svc_label = file_key.replace("/index.html", "")
        print(f"\n  [{svc_label}]")
        a, nf = apply_changes(filepath, changes, dry_run=DRY_RUN)
        city_applied += a
        city_not_found += nf

    print(f"\n  SUBTOTAL {city_slug}: {city_applied} aplicadas | {city_not_found} nao encontradas")
    grand_applied += city_applied
    grand_not_found += city_not_found

print(f"\nGRAND TOTAL: {grand_applied} aplicadas | {grand_not_found} nao encontradas")
if DRY_RUN:
    print("(DRY RUN — nenhum arquivo foi modificado)")
