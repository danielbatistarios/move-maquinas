#!/usr/bin/env python3
"""
fix_coverage_links.py — Adiciona links internos nas seções de cobertura
de todas as páginas de serviço das cidades Move Máquinas.

Substitui texto puro de cidades conhecidas por <a href="/slug/">Nome</a>
dentro da div.coverage__cities apenas.

Uso:
  python3 fix_coverage_links.py --dry-run   # mostra o que vai mudar
  python3 fix_coverage_links.py             # aplica as mudanças
"""

import re
import sys
import os

# Mapa: texto exato na página → slug da URL
CITY_MAP = {
    # Texto exato (como aparece no HTML) → slug
    'Goiânia':                  'goiania-go',
    'Goiania':                  'goiania-go',
    'Aparecida de Goiânia':     'aparecida-de-goiania-go',
    'Aparecida de Goiania':     'aparecida-de-goiania-go',
    'Anápolis':                 'anapolis-go',
    'Anapolis':                 'anapolis-go',
    'Senador Canedo':           'senador-canedo-go',
    'Brasília (DF)':            'brasilia-df',
    'Brasilia (DF)':            'brasilia-df',
    'Brasília':                 'brasilia-df',
    'Brasilia':                 'brasilia-df',
    'Trindade':                 'trindade-go',
    'Inhumas':                  'inhumas-go',
    'Caldas Novas':             'caldas-novas-go',
    'Luziânia':                 'luziania-go',
    'Luziania':                 'luziania-go',
    'Itumbiara':                'itumbiara-go',
    'Formosa':                  'formosa-go',
    'Valparaíso de Goiás':      'valparaiso-de-goias-go',
    'Valparaiso de Goias':      'valparaiso-de-goias-go',
    'Valparaíso':               'valparaiso-de-goias-go',
    'Uruaçu':                   'uruacu-go',
    'Uruacu':                   'uruacu-go',
}

# Cidades que NÃO têm página própria (não devem ser linkadas)
NO_PAGE = {
    'Goianésia', 'Goianesia',
    'Aparecida de Senador Canedo', 'Aparecida de Anápolis',
    'Taguatinga', 'Ceilândia', 'Santa Maria', 'SIA',
    'Águas Lindas', 'Aguas Lindas',
    'Alexânia', 'Alexania',
    'Cristalina', 'Morrinhos', 'Bela Vista de Goiás',
    'Rio Verde', 'Jataí', 'Mineiros',
}

BASE_DIR = '/Users/jrios/move-maquinas-seo'

CITIES = [
    'anapolis-go', 'aparecida-de-goiania-go', 'brasilia-df',
    'caldas-novas-go', 'formosa-go', 'goiania-go', 'inhumas-go',
    'itumbiara-go', 'luziania-go', 'senador-canedo-go',
    'trindade-go', 'uruacu-go', 'valparaiso-de-goias-go',
]

SERVICES = [
    'aluguel-de-empilhadeira-combustao',
    'aluguel-de-plataforma-elevatoria-articulada',
    'aluguel-de-plataforma-elevatoria-tesoura',
    'aluguel-de-transpaleteira',
    'curso-de-operador-de-empilhadeira',
    'manutencao-empilhadeira',
    'pecas-e-assistencia-empilhadeira',
]

SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'


def make_link(city_name, slug):
    """Gera o HTML do link para uma cidade."""
    return f'<a href="/{slug}/">{city_name}</a>'


def fix_coverage_block(html, current_city_slug, service_slug):
    """
    Substitui texto puro de cidades por links dentro de coverage__cities.
    A cidade atual da página recebe link para seu index (/{city}/),
    as outras recebem link para a mesma página de serviço (/{city}/{service}/).
    Não toca em cidades já linkadas.
    """
    # Localiza o bloco coverage__cities
    start_marker = '<div class="coverage__cities reveal">'
    end_marker = '</div>\n\n    <!-- Google Maps'

    start = html.find(start_marker)
    if start == -1:
        # Tenta variante sem reveal
        start_marker = '<div class="coverage__cities">'
        start = html.find(start_marker)
    if start == -1:
        return html, 0

    end = html.find('<!-- Google Maps', start)
    if end == -1:
        end = html.find('</section>', start)
    if end == -1:
        return html, 0

    block = html[start:end]
    original_block = block

    changes = 0

    # Para cada cidade conhecida, procura o padrão de texto puro dentro de coverage__city
    for city_name, city_slug in CITY_MAP.items():
        if city_name in NO_PAGE:
            continue

        # Padrão: SVG seguido de espaço+texto puro (sem <a>)
        # Captura: texto exato entre SVG e </div>, sem ser já um link
        pattern = (
            r'(<div class="coverage__city">\s*'
            + re.escape(SVG)
            + r'\s*)'
            + r'(?!<a\b)'          # não já linkado
            + r'(?:<strong>)?'
            + re.escape(city_name)
            + r'(?:</strong>)?'
            + r'(\s*</div>)'
        )

        if city_slug == current_city_slug:
            # Cidade atual: link para o hub da cidade
            replacement = r'\g<1>' + make_link(city_name, city_slug) + r'\g<2>'
        else:
            # Outra cidade: link para a mesma página de serviço
            replacement = r'\g<1>' + f'<a href="/{city_slug}/{service_slug}/">{city_name}</a>' + r'\g<2>'

        new_block, n = re.subn(pattern, replacement, block)
        if n > 0:
            block = new_block
            changes += n

    if changes > 0:
        html = html[:start] + block + html[end:]

    return html, changes


def process_file(filepath, city_slug, service_slug, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    fixed, changes = fix_coverage_block(original, city_slug, service_slug)

    if changes == 0:
        return 0

    if dry_run:
        print(f'  [DRY] {changes} link(s) → {filepath.replace(BASE_DIR + "/", "")}')
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f'  ✅ {changes} link(s) → {filepath.replace(BASE_DIR + "/", "")}')

    return changes


def main():
    dry_run = '--dry-run' in sys.argv
    mode = 'DRY RUN' if dry_run else 'APLICANDO'
    print(f'\n🔧 fix_coverage_links.py — {mode}\n')

    total_files = 0
    total_links = 0

    for city in CITIES:
        # Hub da cidade (index.html) — pula por ora (estrutura diferente)
        for service in SERVICES:
            filepath = os.path.join(BASE_DIR, city, service, 'index.html')
            if not os.path.exists(filepath):
                continue
            n = process_file(filepath, city, service, dry_run=dry_run)
            if n > 0:
                total_files += 1
                total_links += n

    print(f'\n─────────────────────────────────────────')
    print(f'{"Simulado" if dry_run else "Concluído"}: {total_links} links em {total_files} arquivos.')
    if dry_run:
        print('Execute sem --dry-run para aplicar.')


if __name__ == '__main__':
    main()
