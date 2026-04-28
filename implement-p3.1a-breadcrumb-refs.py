#!/usr/bin/env python3
"""
Move Máquinas — P3.1a: Adiciona referência de BreadcrumbList em WebPage nodes
Conecta WebPage → BreadcrumbList via @id reference (96 páginas: LPs + hubs + home + blog)
Padrão: "breadcrumb": {"@id": "https://movemaquinas.com.br/#breadcrumbs"}
"""

import json
import re
from pathlib import Path

def extract_url_from_path(filepath: str) -> str:
    """Extrai URL base do caminho do arquivo"""
    parts = Path(filepath).relative_to('/Users/jrios/move-maquinas-seo').parts

    # Home: /index.html → https://movemaquinas.com.br/
    if len(parts) == 1 and parts[0] == 'index.html':
        return 'https://movemaquinas.com.br/'

    # LP ou hub: {city-state}/{service-slug}/index.html → https://movemaquinas.com.br/{city-state}/{service-slug}/
    if len(parts) >= 2 and parts[-1] == 'index.html':
        return f"https://movemaquinas.com.br/{'/'.join(parts[:-1])}/"

    return None

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando breadcrumb reference em WebPage"""
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

        # Encontra WebPage node
        webpage_node = None
        for node in nodes:
            if node.get('@type') == 'WebPage':
                webpage_node = node
                break

        if not webpage_node:
            return False, "No WebPage found"

        # Verifica se já tem breadcrumb reference
        if 'breadcrumb' in webpage_node:
            return False, "WebPage already has breadcrumb reference"

        # Adiciona breadcrumb reference
        webpage_node['breadcrumb'] = {
            "@id": "https://movemaquinas.com.br/#breadcrumbs"
        }

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

        return True, "Injected breadcrumb reference in WebPage"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra todas as páginas: home + city hubs + service LPs + blog
    html_files = [base_path / 'index.html']  # Home
    html_files.extend(base_path.glob('*/index.html'))  # City hubs
    html_files.extend(base_path.glob('**/index.html'))  # All nested pages

    # Remove duplicatas
    html_files = list(set(html_files))
    html_files = sorted([f for f in html_files if f.exists()])

    print(f"📊 Encontradas {len(html_files)} páginas (home + hubs + LPs + blog)\n")

    success_count = 0
    skipped_count = 0
    error_count = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "already" in msg.lower():
            print(f"⏭️  {relative_path}: {msg}")
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.1a:")
    print(f"  ✅ Processadas: {success_count}")
    print(f"  ⏭️  Já tinham breadcrumb ref: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +2pp conformidade, BreadcrumbList conectado no KG")

if __name__ == '__main__':
    main()
