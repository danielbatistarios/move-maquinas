#!/usr/bin/env python3
"""
Move Máquinas — P3.2a: Adiciona seller reference em Offer nodes
Padrão: "seller": {"@id": "https://movemaquinas.com.br/#organization"}
Escopo: ~200+ offers em 91 páginas (aluguel + curso + manutenção + peças)
"""

import json
import re
from pathlib import Path

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa arquivo HTML, adicionando seller em Offer nodes"""
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

        # Encontra Offer nodes e adiciona seller
        changes_made = 0

        def add_seller_to_node(node):
            nonlocal changes_made
            if node.get('@type') == 'Offer' and 'seller' not in node:
                node['seller'] = {
                    "@id": "https://movemaquinas.com.br/#organization"
                }
                changes_made += 1
            # Verifica offers dentro de Service
            if 'offers' in node and isinstance(node['offers'], list):
                for offer in node['offers']:
                    if isinstance(offer, dict) and offer.get('@type') == 'Offer' and 'seller' not in offer:
                        offer['seller'] = {
                            "@id": "https://movemaquinas.com.br/#organization"
                        }
                        changes_made += 1

        for node in nodes:
            add_seller_to_node(node)

        if changes_made == 0:
            return False, "No Offer found or all already have seller"

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

        return True, f"Injected seller in {changes_made} Offer(s)"

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
    total_offers = 0

    for filepath in sorted(html_files):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            # Extrai número de offers
            import re as re_module
            match = re_module.search(r'(\d+)', msg)
            if match:
                total_offers += int(match.group(1))
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "already" in msg.lower():
            print(f"⏭️  {relative_path}: {msg}")
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo P3.2a:")
    print(f"  ✅ Páginas processadas: {success_count}")
    print(f"  💰 Total Offer sellers injetados: {total_offers}")
    print(f"  ⏭️  Páginas sem offers: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total páginas: {len(html_files)}")
    print(f"\n🎯 Impacto esperado: +1.5pp conformidade, todos os offers conectados ao vendedor global")

if __name__ == '__main__':
    main()
