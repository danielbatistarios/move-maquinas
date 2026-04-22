#!/usr/bin/env python3
"""
Move Máquinas — P2: Adiciona @id em FAQPage nodes (24 páginas: curso + peças)
Padrão: https://movemaquinas.com.br/{city-state}/{service-slug}/#faqpage
"""

import json
import re
from pathlib import Path

def extract_url_components(filepath: str) -> tuple[str, str] | None:
    """Extrai city-state e service-slug do caminho"""
    parts = Path(filepath).relative_to('/Users/jrios/move-maquinas-seo').parts

    # Formato: {city-state}/{service-slug}/index.html
    if len(parts) != 3 or parts[2] != 'index.html':
        return None

    city_state = parts[0]
    service_slug = parts[1]

    return city_state, service_slug

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa um arquivo HTML, injetando @id em FAQPage"""
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

        # Encontra FAQPage nodes
        faqpage_nodes = [n for n in nodes if n.get('@type') == 'FAQPage']

        if not faqpage_nodes:
            return False, "No FAQPage found"

        # Extrai componentes da URL
        url_components = extract_url_components(filepath)
        if not url_components:
            return False, "Cannot extract URL components"

        city_state, service_slug = url_components

        # Injeta @id em cada FAQPage node que não tem
        changes_made = 0
        for faq_node in faqpage_nodes:
            if '@id' not in faq_node:
                faq_node['@id'] = f"https://movemaquinas.com.br/{city_state}/{service_slug}/#faqpage"
                changes_made += 1

        if changes_made == 0:
            return False, "FAQPage already has @id"

        # Reconstrói JSON-LD
        new_json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False)

        # Substitui no HTML
        new_html = html_content[:start_pos] + f'<script type="application/ld+json">{new_json_str}</script>' + html_content[end_pos:]

        # Escreve de volta
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)

        return True, f"Injected @id in {changes_made} FAQPage node(s)"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra páginas de curso e peças
    target_patterns = ['**/curso-de-operador-de-empilhadeira/index.html',
                       '**/pecas-e-assistencia-empilhadeira/index.html']

    html_files = []
    for pattern in target_patterns:
        html_files.extend(base_path.glob(pattern))

    print(f"📊 Encontradas {len(html_files)} páginas de curso/peças\n")

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

    print(f"\n📈 Resumo P2:")
    print(f"  ✅ Processadas: {success_count}")
    print(f"  ⏭️  Já tinham @id: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total: {len(html_files)}")

if __name__ == '__main__':
    main()
