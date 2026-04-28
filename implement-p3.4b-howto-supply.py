#!/usr/bin/env python3
"""
Move Máquinas — P3.4b: Adiciona supply em HowTo nodes
Requisitos de segurança (EPI) por tipo de serviço
Escopo: 52 aluguel páginas
"""

import json
import re
from pathlib import Path

# Mapear service slug → safety supplies
SERVICE_SUPPLIES = {
    'aluguel-de-empilhadeira-combustao': "EPI: Safety Helmet, Reflective Vest, Closed-Toe Shoes, Safety Gloves",
    'aluguel-de-plataforma-elevatoria-articulada': "EPI: Safety Helmet, Harness, Reflective Vest, Closed-Toe Shoes",
    'aluguel-de-plataforma-elevatoria-tesoura': "EPI: Safety Helmet, Harness, Reflective Vest, Closed-Toe Shoes",
    'aluguel-de-transpaleteira': "EPI: Reflective Vest, Closed-Toe Shoes, Safety Gloves",
}

def get_service_supply(service_slug: str) -> str | None:
    """Retorna supply requirements para serviço"""
    return SERVICE_SUPPLIES.get(service_slug)

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando supply em HowTo nodes"""
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

        # Extrai service slug do caminho
        parts = Path(filepath).relative_to('/Users/jrios/move-maquinas-seo').parts
        if len(parts) < 3 or parts[-1] != 'index.html':
            return False, "Cannot extract service slug"

        service_slug = parts[1]
        supply_text = get_service_supply(service_slug)

        if not supply_text:
            return False, "No supply defined for this service"

        # Encontra HowTo node
        changes_made = 0

        for node in nodes:
            if node.get('@type') == 'HowTo':
                if 'supply' not in node:
                    node['supply'] = {
                        "@type": "HowToSupply",
                        "name": supply_text
                    }
                    changes_made += 1

        if changes_made == 0:
            return False, "HowTo already has supply or not found"

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

        return True, "Added safety supply requirements to HowTo"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra páginas de aluguel
    html_files = base_path.glob('**/aluguel-*/index.html')
    html_files = sorted([f for f in html_files if f.exists()])

    print(f"📊 Encontradas {len(html_files)} páginas de aluguel\n")

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
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.4b:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  ⏭️  Páginas já com supply: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +1.5pp conformidade, requisitos de segurança estruturados")

if __name__ == '__main__':
    main()
