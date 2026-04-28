#!/usr/bin/env python3
"""
Move Máquinas — P3.5a: Adiciona Service.brand (Clark) com sameAs Wikidata
Padrão: Clark Material Handling Company → Wikidata Q63922640
Escopo: 92 páginas (aluguel + curso + manutenção + peças)
"""

import json
import re
from pathlib import Path

# Clark brand reference com Wikidata
CLARK_BRAND = {
    "@type": "Organization",
    "@id": "https://movemaquinas.com.br/#clark-brand",
    "name": "Clark Material Handling Company",
    "sameAs": "https://www.wikidata.org/wiki/Q63922640"
}

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando brand em Service nodes"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Extrai JSON-LD
        pattern = r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>'
        match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)

        if not match:
            return False, "No JSON-LD found"

        json_str = match.group(1).strip()
        start_pos = match.start()
        end_pos = match.end()

        # Parse JSON
        data = json.loads(json_str)
        nodes = data.get('@graph', [data] if isinstance(data, dict) else data)

        # Encontra Service nodes e adiciona brand
        changes_made = 0

        for node in nodes:
            if node.get('@type') == 'Service':
                if 'brand' not in node:
                    node['brand'] = CLARK_BRAND
                    changes_made += 1

        if changes_made == 0:
            return False, "No Service found or all already have brand"

        # Reconstrói JSON-LD
        if len(nodes) == 1:
            new_json_str = json.dumps(nodes[0], separators=(',', ':'), ensure_ascii=False)
        else:
            graph_structure = {
                '@context': 'https://schema.org',
                '@graph': nodes
            }
            new_json_str = json.dumps(graph_structure, separators=(',', ':'), ensure_ascii=False)

        # Substitui no HTML
        new_html = html_content[:start_pos] + f'<script type="application/ld+json">{new_json_str}</script>' + html_content[end_pos:]

        # Escreve de volta
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)

        return True, f"Added Clark brand (Wikidata Q63922640) to {changes_made} Service(s)"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra páginas de aluguel, curso, manutenção e peças
    html_files = []
    for pattern in ['**/aluguel-*/index.html',
                    '**/curso-de-operador-de-empilhadeira/index.html',
                    '**/manutencao-empilhadeira/index.html',
                    '**/pecas-e-assistencia-empilhadeira/index.html']:
        html_files.extend(base_path.glob(pattern))

    # Remove duplicatas
    html_files = list(set(html_files))
    html_files = sorted([f for f in html_files if f.exists()])

    print(f"📊 Encontradas {len(html_files)} páginas (aluguel + curso + manutenção + peças)\n")

    success_count = 0
    skipped_count = 0
    error_count = 0
    total_services = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            # Extrai número de services
            import re as re_module
            match = re_module.search(r'(\d+)', msg)
            if match:
                total_services += int(match.group(1))
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "already" in msg.lower():
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.5a:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  🏭 Total Service brands adicionadas: {total_services}")
    print(f"  ⏭️  Páginas sem Service: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +1.5pp conformidade, 92 Services linkados a Clark Wikidata")

if __name__ == '__main__':
    main()
