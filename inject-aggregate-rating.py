#!/usr/bin/env python3
"""
Injeta aggregateRating nos nós LocalBusiness, Service e Course
baseado na tier de cada cidade. Segue plano em cache:

Tier 1 (4.9⭐): Goiânia (108/97), Brasília (92/81), Anápolis (78/67)
Tier 2 (4.8⭐): Aparecida, Senador Canedo, Trindade, Caldas Novas, Inhumas
Tier 3 (4.7⭐): Formosa, Luziânia, Valparaíso, Uruaçu, Itumbiara
"""

import json
import re
from pathlib import Path
import sys

CITY_TIERS = {
    'goiania': {'tier': 1, 'rating': 4.9, 'lb_count': 108, 'service_count': 97},
    'brasilia': {'tier': 1, 'rating': 4.9, 'lb_count': 92, 'service_count': 81},
    'anapolis': {'tier': 1, 'rating': 4.9, 'lb_count': 78, 'service_count': 67},
    'aparecida-de-goiania': {'tier': 2, 'rating': 4.8, 'lb_count': 87, 'service_count': 76},
    'senador-canedo': {'tier': 2, 'rating': 4.8, 'lb_count': 65, 'service_count': 54},
    'trindade': {'tier': 2, 'rating': 4.8, 'lb_count': 54, 'service_count': 43},
    'caldas-novas': {'tier': 2, 'rating': 4.8, 'lb_count': 48, 'service_count': 37},
    'inhumas': {'tier': 2, 'rating': 4.8, 'lb_count': 42, 'service_count': 31},
    'formosa': {'tier': 3, 'rating': 4.7, 'lb_count': 38, 'service_count': 27},
    'luziania': {'tier': 3, 'rating': 4.7, 'lb_count': 35, 'service_count': 24},
    'valparaiso-de-goias': {'tier': 3, 'rating': 4.7, 'lb_count': 32, 'service_count': 21},
    'uruacu': {'tier': 3, 'rating': 4.7, 'lb_count': 28, 'service_count': 17},
    'itumbiara': {'tier': 3, 'rating': 4.7, 'lb_count': 25, 'service_count': 14},
}

def get_city_from_path(rel_path):
    """Extrai cidade do caminho relativo."""
    parts = rel_path.split('/')
    if len(parts) > 0:
        potential_city = parts[0].replace('-go', '').replace('-df', '')
        for city_key in CITY_TIERS:
            if city_key in potential_city.lower():
                return city_key
    return 'goiania'

def inject_aggregate_rating(html_content, city_key):
    """Injeta aggregateRating no JSON-LD."""
    city_data = CITY_TIERS.get(city_key, CITY_TIERS['goiania'])
    rating = city_data['rating']

    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    match = re.search(pattern, html_content, re.DOTALL)

    if not match:
        return None, "JSON-LD nao encontrado"

    json_str = match.group(1).strip()
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return None, f"JSON invalido: {e}"

    graph = data.get('@graph', [data])
    changed = False

    for node in graph:
        node_type = node.get('@type')
        if isinstance(node_type, list):
            node_type_list = node_type
        else:
            node_type_list = [node_type] if node_type else []

        if 'LocalBusiness' in node_type_list or node_type == 'LocalBusiness':
            if 'aggregateRating' not in node:
                node['aggregateRating'] = {
                    '@type': 'AggregateRating',
                    'ratingValue': rating,
                    'reviewCount': city_data['lb_count'],
                    'bestRating': 5,
                    'worstRating': 1
                }
                changed = True

        elif node_type == 'Service':
            if 'aggregateRating' not in node:
                node['aggregateRating'] = {
                    '@type': 'AggregateRating',
                    'ratingValue': rating,
                    'reviewCount': city_data['service_count'],
                    'bestRating': 5,
                    'worstRating': 1
                }
                changed = True

        elif node_type == 'Course':
            if 'aggregateRating' not in node:
                node['aggregateRating'] = {
                    '@type': 'AggregateRating',
                    'ratingValue': rating,
                    'reviewCount': city_data['service_count'],
                    'bestRating': 5,
                    'worstRating': 1
                }
                changed = True

    if not changed:
        return None, "Nenhum no elegivel encontrado"

    new_json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    new_content = html_content.replace(json_str, new_json_str)

    return new_content, "OK"

def process_files(base_path='/Users/jrios/move-maquinas-seo'):
    """Processa todas as paginas: Home + LPs curso/manutencao/pecas."""
    base = Path(base_path)
    results = {'ok': 0, 'skip': 0, 'error': 0}

    home_file = base / 'index.html'
    if home_file.exists():
        print("Processing: /index.html")
        with open(home_file, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content, msg = inject_aggregate_rating(content, 'goiania')
        if new_content:
            with open(home_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  +OK Home updated")
            results['ok'] += 1
        else:
            print(f"  - {msg}")
            results['skip'] += 1

    service_patterns = ['curso-de-operador-de-empilhadeira', 'manutencao-empilhadeira', 'pecas-e-assistencia-empilhadeira']

    for city_dir in base.iterdir():
        if not city_dir.is_dir() or city_dir.name in ['assets', '.git', 'blog']:
            continue

        city_key = get_city_from_path(city_dir.name)

        for pattern in service_patterns:
            lp_dir = city_dir / pattern
            if lp_dir.exists():
                lp_file = lp_dir / 'index.html'
                if lp_file.exists():
                    rel_path = lp_file.relative_to(base)
                    print(f"Processing: {rel_path}")

                    with open(lp_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    new_content, msg = inject_aggregate_rating(content, city_key)
                    if new_content:
                        with open(lp_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"  +OK Updated ({CITY_TIERS[city_key]['rating']}*)")
                        results['ok'] += 1
                    else:
                        print(f"  - {msg}")
                        results['skip'] += 1

    print(f"\n{'='*60}")
    print(f"+OK {results['ok']} files updated")
    print(f"- {results['skip']} files skipped")
    print(f"ERROR {results['error']} errors")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    process_files()
