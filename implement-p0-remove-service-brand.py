#!/usr/bin/env python3
"""
Fase P0 — Issue #2: Remove 'brand' de nós Service
(Service nodes não devem ter brand, apenas Provider)
"""

import json
import re
from pathlib import Path

def remove_brand_from_services(html_content):
    """Remove brand property de nós Service."""
    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    match = re.search(pattern, html_content, re.DOTALL)

    if not match:
        return None, "JSON-LD não encontrado"

    json_str = match.group(1).strip()
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return None, f"JSON inválido: {e}"

    graph = data.get('@graph', [data])
    changed = False

    for node in graph:
        node_type = node.get('@type')
        if isinstance(node_type, list):
            node_type_str = node_type[0] if node_type else None
        else:
            node_type_str = node_type

        if node_type_str == 'Service' and 'brand' in node:
            del node['brand']
            changed = True

    if not changed:
        return None, "Nenhum Service com brand encontrado"

    new_json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    new_content = html_content.replace(json_str, new_json_str)

    return new_content, "OK"

def process_files(base_path='/Users/jrios/move-maquinas-seo'):
    """Processa todas as páginas."""
    base = Path(base_path)
    results = {'ok': 0, 'skip': 0}

    for html_file in base.rglob('index.html'):
        if html_file.parent.name == 'assets' or '.git' in html_file.parts:
            continue

        rel_path = str(html_file.relative_to(base))
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, msg = remove_brand_from_services(content)
        
        if new_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ {rel_path}")
            results['ok'] += 1

    print(f"\n{'='*60}")
    print(f"✓ {results['ok']} files cleaned (brand removed from Service)")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    process_files()
