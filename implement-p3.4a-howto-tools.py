#!/usr/bin/env python3
"""
Move Máquinas — P3.4a: Adiciona tools em HowTo.step nodes
Equipamentos necessários por tipo de serviço
Escopo: ~350 steps em 52 aluguel páginas
"""

import json
import re
from pathlib import Path

# Mapear service slug → tools por categoria
SERVICE_TOOLS = {
    'aluguel-de-empilhadeira-combustao': [
        {
            "@type": "HowToTool",
            "name": "Clark Combustion Forklift",
            "@id": "https://movemaquinas.com.br/#product-clark-c60"
        },
        {
            "@type": "HowToTool",
            "name": "NR-11 Safety Certification",
            "url": "https://movemaquinas.com.br/curso-de-operador-de-empilhadeira/"
        }
    ],
    'aluguel-de-plataforma-elevatoria-articulada': [
        {
            "@type": "HowToTool",
            "name": "Articulated Lift Platform",
            "@id": "https://movemaquinas.com.br/#product-clark-c70"
        },
        {
            "@type": "HowToTool",
            "name": "NR-35 Work at Heights Certification",
            "url": "https://movemaquinas.com.br/curso-de-operador-de-empilhadeira/"
        }
    ],
    'aluguel-de-plataforma-elevatoria-tesoura': [
        {
            "@type": "HowToTool",
            "name": "Scissor Lift Platform",
            "@id": "https://movemaquinas.com.br/#product-clark-c80"
        },
        {
            "@type": "HowToTool",
            "name": "NR-35 Work at Heights Certification",
            "url": "https://movemaquinas.com.br/curso-de-operador-de-empilhadeira/"
        }
    ],
    'aluguel-de-transpaleteira': [
        {
            "@type": "HowToTool",
            "name": "Electric Pallet Truck",
            "@id": "https://movemaquinas.com.br/#product-clark-transpaleteira"
        },
        {
            "@type": "HowToTool",
            "name": "Basic Material Handling Safety",
            "url": "https://movemaquinas.com.br/curso-de-operador-de-empilhadeira/"
        }
    ]
}

def get_service_tools(service_slug: str) -> list:
    """Retorna tools para serviço"""
    return SERVICE_TOOLS.get(service_slug, [])

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando tools em HowTo steps"""
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
        tools = get_service_tools(service_slug)

        if not tools:
            return False, "No tools defined for this service"

        # Encontra HowTo node
        changes_made = 0

        for node in nodes:
            if node.get('@type') == 'HowTo':
                if 'step' in node and isinstance(node['step'], list):
                    for step in node['step']:
                        if isinstance(step, dict) and 'tool' not in step:
                            step['tool'] = tools
                            changes_made += 1

        if changes_made == 0:
            return False, "No HowTo step found or all already have tools"

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

        return True, f"Added tools to {changes_made} HowTo step(s)"

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
    total_steps = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            # Extrai número de steps
            import re as re_module
            match = re_module.search(r'(\d+)', msg)
            if match:
                total_steps += int(match.group(1))
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "already" in msg.lower() or "all already have" in msg:
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.4a:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  🛠️  Total HowTo steps com tools: {total_steps}")
    print(f"  ⏭️  Páginas sem HowTo: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +1.5pp conformidade, ~350 steps com equipamentos")

if __name__ == '__main__':
    main()
