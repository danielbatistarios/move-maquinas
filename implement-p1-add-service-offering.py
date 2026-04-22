#!/usr/bin/env python3
"""
Fase P1 — Issue #8: Adiciona serviceOffering a Service nodes
(vincula Service -> array de Product @ids)
"""

import json
import re
from pathlib import Path

def add_service_offering(html_content):
    """Adiciona serviceOffering a nós Service."""
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
    
    # Coleta todos os Product @ids
    product_ids = []
    for node in graph:
        if node.get('@type') == 'Product' and '@id' in node:
            product_ids.append({'@id': node['@id']})
    
    if not product_ids:
        return None, "Nenhum Product com @id encontrado"

    changed = False
    # Adiciona serviceOffering a Service nodes
    for node in graph:
        if node.get('@type') == 'Service' and 'serviceOffering' not in node:
            node['serviceOffering'] = product_ids
            changed = True

    if not changed:
        return None, "Nenhum Service elegível para serviceOffering"

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
        # Skip home e blog
        if rel_path in ['index.html'] or 'blog' in rel_path:
            continue
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, msg = add_service_offering(content)
        
        if new_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ {rel_path}")
            results['ok'] += 1

    print(f"\n{'='*60}")
    print(f"✓ {results['ok']} files updated with serviceOffering")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    process_files()
