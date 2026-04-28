#!/usr/bin/env python3
"""
Move Máquinas — P3.3b: Adiciona @id em Question nodes (FAQPage)
Padrão: "https://movemaquinas.com.br/{city}/{service}/#q-{position}"
Escopo: ~200 questions em 26 páginas (curso + peças)
"""

import json
import re
from pathlib import Path

def extract_url_components(filepath: str) -> tuple[str, str] | None:
    """Extrai city-state e service-slug do caminho"""
    parts = Path(filepath).relative_to('/Users/jrios/move-maquinas-seo').parts

    # Formato: {city-state}/{service-slug}/index.html
    if len(parts) == 3 and parts[2] == 'index.html':
        city_state = parts[0]
        service_slug = parts[1]
        return city_state, service_slug

    return None

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando @id em Question nodes"""
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

        # Extrai componentes da URL
        url_components = extract_url_components(filepath)
        if not url_components:
            return False, "Cannot extract URL components"

        city_state, service_slug = url_components

        # Encontra FAQPage node e adiciona @id em Questions
        changes_made = 0

        for node in nodes:
            if node.get('@type') == 'FAQPage':
                if 'mainEntity' in node and isinstance(node['mainEntity'], list):
                    for position, question in enumerate(node['mainEntity']):
                        if isinstance(question, dict) and question.get('@type') == 'Question':
                            if '@id' not in question:
                                question['@id'] = f"https://movemaquinas.com.br/{city_state}/{service_slug}/#q-{position}"
                                changes_made += 1

        if changes_made == 0:
            return False, "No Question found or all already have @id"

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

        return True, f"Injected @id in {changes_made} Question(s)"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra páginas de curso e peças
    html_files = []
    for pattern in ['**/curso-de-operador-de-empilhadeira/index.html',
                    '**/pecas-e-assistencia-empilhadeira/index.html']:
        html_files.extend(base_path.glob(pattern))

    # Remove duplicatas
    html_files = list(set(html_files))
    html_files = sorted([f for f in html_files if f.exists()])

    print(f"📊 Encontradas {len(html_files)} páginas (curso + peças)\n")

    success_count = 0
    skipped_count = 0
    error_count = 0
    total_questions = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            # Extrai número de questions
            import re as re_module
            match = re_module.search(r'(\d+)', msg)
            if match:
                total_questions += int(match.group(1))
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "already" in msg.lower():
            print(f"⏭️  {relative_path}: {msg}")
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.3b:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  ❓ Total Question @ids injetados: {total_questions}")
    print(f"  ⏭️  Páginas já conformes: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +1.5pp conformidade, ~200 Questions deduplicáveis")

if __name__ == '__main__':
    main()
