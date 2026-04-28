#!/usr/bin/env python3
"""
Move Máquinas — P3.1b: Adiciona @id em VideoObject nodes (96 páginas, ~180 vídeos)
Padrão: "https://movemaquinas.com.br/{city}/{service}/#video-{index}"
"""

import json
import re
from pathlib import Path

def extract_url_components(filepath: str) -> tuple[str, str] | None:
    """Extrai city-state e service-slug do caminho"""
    parts = Path(filepath).relative_to('/Users/jrios/move-maquinas-seo').parts

    # Home: /index.html
    if len(parts) == 1 and parts[0] == 'index.html':
        return 'home', 'home'

    # LP ou hub: {city-state}/{service-slug}/index.html
    if len(parts) >= 2 and parts[-1] == 'index.html':
        city_state = parts[0]
        service_slug = parts[1] if len(parts) > 2 else 'hub'
        return city_state, service_slug

    return None

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando @id em VideoObject nodes"""
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

        # Encontra VideoObject nodes e adiciona @id
        changes_made = 0
        video_index = 0

        for node in nodes:
            if node.get('@type') == 'VideoObject':
                if '@id' not in node:
                    if city_state == 'home':
                        node['@id'] = f"https://movemaquinas.com.br/#video-home-{video_index}"
                    else:
                        node['@id'] = f"https://movemaquinas.com.br/{city_state}/{service_slug}/#video-{video_index}"
                    changes_made += 1
                video_index += 1

        if changes_made == 0:
            return False, "No VideoObject found or all already have @id" if video_index > 0 else "No VideoObject found"

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

        return True, f"Injected @id in {changes_made} VideoObject(s)"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra todas as páginas com WebPage (LPs + hubs + home)
    html_files = [base_path / 'index.html']  # Home
    html_files.extend(base_path.glob('*/index.html'))  # City hubs
    html_files.extend(base_path.glob('*/**/index.html'))  # Service LPs
    html_files.extend(base_path.glob('blog/**/index.html'))  # Blog articles

    # Remove duplicatas
    html_files = list(set(html_files))
    html_files = sorted([f for f in html_files if f.exists()])

    print(f"📊 Encontradas {len(html_files)} páginas (LPs + hubs + home + blog)\n")

    success_count = 0
    skipped_count = 0
    error_count = 0
    total_videos = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            # Extrai número de vídeos injetados
            import re as re_module
            match = re_module.search(r'(\d+)', msg)
            if match:
                total_videos += int(match.group(1))
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "No VideoObject found" in msg:
            skipped_count += 1
        elif "already have @id" in msg:
            print(f"⏭️  {relative_path}: {msg}")
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.1b:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  📹 Total VideoObject @ids injetados: {total_videos}")
    print(f"  ⏭️  Páginas sem vídeos: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +2pp conformidade, ~180 VideoObjects deduplicáveis globalmente")

if __name__ == '__main__':
    main()
