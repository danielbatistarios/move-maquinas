#!/usr/bin/env python3
"""
Fase P0 — CRÍTICO: Adiciona @id global a todos os nós Service/Course/Product
que ainda não possuem.

Padrões de @id:
- Service: https://movemaquinas.com.br/#service-{tipo}
  (aluguel, curso, manutencao, pecas)
- Course: https://movemaquinas.com.br/#course-operador
- Product: https://movemaquinas.com.br/#product-{sku}-{city}
"""

import json
import re
from pathlib import Path

def add_ids_to_nodes(html_content, rel_path):
    """Adiciona @id aos nós Service/Course/Product sem @id."""
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

        # Service: Detectar tipo por nome ou provider
        if node_type_str == 'Service':
            if '@id' not in node:
                service_name = node.get('name', '').lower()
                if 'aluguel' in service_name:
                    service_type = 'aluguel'
                elif 'curso' in service_name:
                    service_type = 'curso'
                elif 'manuten' in service_name:
                    service_type = 'manutencao'
                elif 'peca' in service_name or 'peça' in service_name:
                    service_type = 'pecas'
                else:
                    service_type = 'geral'

                node['@id'] = f"https://movemaquinas.com.br/#service-{service_type}"
                changed = True

        # Course: sempre usa #course-operador
        elif node_type_str == 'Course':
            if '@id' not in node:
                node['@id'] = "https://movemaquinas.com.br/#course-operador"
                changed = True

        # Product: gera @id a partir de SKU + cidade
        elif node_type_str == 'Product':
            if '@id' not in node:
                sku = node.get('sku', 'produto').lower()
                # Extrai cidade do rel_path
                city = 'geral'
                if '/' in rel_path:
                    parts = rel_path.split('/')
                    if parts[0]:
                        city = parts[0].replace('-go', '').replace('-df', '')
                
                node['@id'] = f"https://movemaquinas.com.br/#product-{sku}-{city}"
                changed = True

    if not changed:
        return None, "Nenhum nó sem @id encontrado"

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

        new_content, msg = add_ids_to_nodes(content, rel_path)
        
        if new_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ {rel_path}")
            results['ok'] += 1
        else:
            # Só mostra skip se houver JSON-LD
            if 'JSON-LD não encontrado' not in msg:
                pass

    print(f"\n{'='*60}")
    print(f"✓ {results['ok']} files updated with @ids")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    process_files()
