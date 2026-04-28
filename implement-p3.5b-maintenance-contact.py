#!/usr/bin/env python3
"""
Move Máquinas — P3.5b: Adiciona Service.maintenanceContact em páginas de manutenção
Contato técnico: Márcio Lima (suporte)
Escopo: 13 páginas (manutenção-empilhadeira em 13 cidades)
"""

import json
import re
from pathlib import Path

# Technical maintenance contact
MAINTENANCE_CONTACT = {
    "@type": "Person",
    "@id": "https://movemaquinas.com.br/#marcio-lima-maintenance",
    "name": "Márcio Lima",
    "jobTitle": "Technical Support",
    "telephone": "+55-62-98434-3800",
    "url": "https://movemaquinas.com.br/quem-somos/"
}

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando maintenanceContact em Service nodes de manutenção"""
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

        # Encontra Service nodes de manutenção e adiciona maintenanceContact
        changes_made = 0

        for node in nodes:
            if node.get('@type') == 'Service':
                # Verifica se é página de manutenção
                if 'manutencao' in filepath.lower():
                    if 'maintenanceContact' not in node:
                        node['maintenanceContact'] = MAINTENANCE_CONTACT
                        changes_made += 1

        if changes_made == 0:
            return False, "No Service found or all already have maintenanceContact"

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

        return True, f"Added maintenance contact (Márcio Lima) to {changes_made} Service(s)"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra páginas de manutenção
    html_files = base_path.glob('**/manutencao-empilhadeira/index.html')
    html_files = sorted([f for f in html_files if f.exists()])

    print(f"📊 Encontradas {len(html_files)} páginas de manutenção\n")

    success_count = 0
    skipped_count = 0
    error_count = 0
    total_contacts = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            # Extrai número de contacts
            import re as re_module
            match = re_module.search(r'(\d+)', msg)
            if match:
                total_contacts += int(match.group(1))
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "already" in msg.lower():
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.5b:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  📞 Total maintenanceContact adicionados: {total_contacts}")
    print(f"  ⏭️  Páginas já com contato: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas de manutenção: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +1.5pp conformidade, suporte técnico estruturado")

if __name__ == '__main__':
    main()
