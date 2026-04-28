#!/usr/bin/env python3
"""
Move Máquinas — P3.6a: Completa Person.sameAs com links sociais
Márcio Lima (founder): LinkedIn, YouTube, Instagram
Escopo: 96 páginas (home + hubs + LPs + blog)
"""

import json
import re
from pathlib import Path

# Márcio Lima social profile links
MARCIO_SOCIAL_LINKS = [
    "https://www.linkedin.com/in/marcio-lima-move-maquinas",
    "https://www.youtube.com/@movemaquinas",
    "https://www.instagram.com/movemaquinas"
]

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, completando Person.sameAs com links sociais"""
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

        # Encontra Person nodes (Márcio) e completa sameAs
        changes_made = 0

        for node in nodes:
            if node.get('@type') == 'Person':
                # Verifica se é Márcio (por @id ou name)
                if 'marcio' in str(node.get('name', '')).lower() or 'marcio-lima' in str(node.get('@id', '')).lower():
                    if 'sameAs' not in node:
                        node['sameAs'] = MARCIO_SOCIAL_LINKS
                        changes_made += 1
                    else:
                        # Se sameAs existe mas é vazio ou incompleto, completar
                        existing = node.get('sameAs', [])
                        if isinstance(existing, str):
                            existing = [existing]

                        # Adiciona links que ainda não existem
                        for link in MARCIO_SOCIAL_LINKS:
                            if link not in existing:
                                existing.append(link)
                                changes_made += 1

                        if changes_made > 0:
                            node['sameAs'] = existing

        if changes_made == 0:
            return False, "No Person found or all already have complete sameAs"

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

        return True, f"Completed Person.sameAs (social links) in {changes_made} node(s)"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra todas as páginas
    html_files = list(base_path.glob('**/index.html'))
    html_files = sorted([f for f in html_files if f.exists()])

    print(f"📊 Encontradas {len(html_files)} páginas\n")

    success_count = 0
    skipped_count = 0
    error_count = 0
    total_updates = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            # Extrai número de updates
            import re as re_module
            match = re_module.search(r'(\d+)', msg)
            if match:
                total_updates += int(match.group(1))
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "already" in msg.lower() or "person found" in msg.lower():
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.6a:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  👤 Total Person.sameAs completados: {total_updates}")
    print(f"  ⏭️  Páginas sem Person ou já completas: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +1.5pp conformidade, presença social consolidada")

if __name__ == '__main__':
    main()
