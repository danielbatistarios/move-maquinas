#!/usr/bin/env python3
"""
Move Máquinas — P1: Reorganiza @graph nodes por camada semântica
Hierarquia: L0 (Organization/LocalBusiness) → L1 (WebPage, Person, BreadcrumbList, SiteNavigation)
            → L2 (Service, VideoObject, HowTo, Course) → L3 (FAQPage, Product)
"""

import json
import re
import os
from pathlib import Path
from typing import Dict, List, Any

# Hierarquia semântica de tipos de nó
SEMANTIC_LAYERS = {
    # L0 — Entidade principal
    0: ['Organization', 'LocalBusiness', 'Company'],

    # L1 — Documento + estrutura
    1: ['WebSite', 'WebPage', 'Person', 'BreadcrumbList', 'SiteNavigationElement', 'ProfilePage'],

    # L2 — Conteúdo/Serviço
    2: ['Service', 'VideoObject', 'Video', 'HowTo', 'Course', 'TrainingEvent'],

    # L3 — Detalhes/Produtos
    3: ['FAQPage', 'Product', 'AggregateOffer', 'Offer', 'Question', 'Answer']
}

# Dentro de cada camada, ordem específica
INTRA_LAYER_ORDER = {
    0: ['Organization', 'LocalBusiness', 'Company'],
    1: ['WebSite', 'WebPage', 'Person', 'BreadcrumbList', 'SiteNavigationElement', 'ProfilePage'],
    2: ['Service', 'VideoObject', 'Video', 'HowTo', 'Course', 'TrainingEvent'],
    3: ['FAQPage', 'Product', 'AggregateOffer', 'Offer', 'Question', 'Answer']
}

def get_node_layer(node: Dict[str, Any]) -> int:
    """Retorna a camada semântica do nó (0-3)"""
    node_type = node.get('@type', '')

    # Converte array para string (pega o primeiro elemento)
    if isinstance(node_type, list):
        node_type = node_type[0] if node_type else ''

    for layer, types in SEMANTIC_LAYERS.items():
        if node_type in types:
            return layer

    return 3  # Padrão: L3 para tipos desconhecidos

def get_intra_layer_priority(node: Dict[str, Any], layer: int) -> int:
    """Retorna prioridade dentro da camada (menor = antes)"""
    node_type = node.get('@type', '')

    # Converte array para string (pega o primeiro elemento)
    if isinstance(node_type, list):
        node_type = node_type[0] if node_type else ''

    if layer in INTRA_LAYER_ORDER:
        try:
            return INTRA_LAYER_ORDER[layer].index(node_type)
        except ValueError:
            return 999

    return 999

def sort_nodes(nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Ordena nós por camada semântica, depois por prioridade intra-layer"""
    return sorted(
        nodes,
        key=lambda n: (get_node_layer(n), get_intra_layer_priority(n, get_node_layer(n)))
    )

def extract_json_ld(html_content: str) -> tuple[str, List[Dict[str, Any]] | None, int, int]:
    """Extrai o script JSON-LD do HTML"""
    pattern = r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>'
    match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)

    if not match:
        return None, None, 0, 0

    json_str = match.group(1).strip()
    start_pos = match.start()
    end_pos = match.end()

    try:
        data = json.loads(json_str)

        # Handle both @graph and direct object
        if isinstance(data, dict):
            if '@graph' in data:
                nodes = data['@graph']
            else:
                nodes = [data]
        else:
            nodes = data

        return json_str, nodes, start_pos, end_pos
    except json.JSONDecodeError as e:
        print(f"❌ JSON Parse Error: {e}")
        return json_str, None, start_pos, end_pos

def reconstruct_json_ld(nodes: List[Dict[str, Any]]) -> str:
    """Reconstrói JSON-LD minificado com ordenação correta"""
    if len(nodes) == 1:
        # Sem @graph
        return json.dumps(nodes[0], separators=(',', ':'), ensure_ascii=False)
    else:
        # Com @graph
        graph_structure = {
            '@context': 'https://schema.org',
            '@graph': nodes
        }
        return json.dumps(graph_structure, separators=(',', ':'), ensure_ascii=False)

def process_file(filepath: str) -> tuple[bool, str]:
    """Processa um arquivo HTML individual"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()

        original_json_str, nodes, start_pos, end_pos = extract_json_ld(html_content)

        if nodes is None:
            return False, f"No JSON-LD found"

        # Verifica se já está ordenado
        sorted_nodes = sort_nodes(nodes)
        if nodes == sorted_nodes:
            return False, f"Already sorted"

        # Reconstrói JSON-LD
        new_json_str = reconstruct_json_ld(sorted_nodes)

        # Substitui no HTML
        new_html = html_content[:start_pos] + f'<script type="application/ld+json">{new_json_str}</script>' + html_content[end_pos:]

        # Escreve de volta
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)

        return True, f"Reordered {len(nodes)} nodes"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra todos os index.html files (84 páginas)
    html_files = list(base_path.glob('**/index.html'))
    print(f"📊 Encontrados {len(html_files)} arquivos HTML\n")

    # Filtra para LPs de serviço (exclui root index.html se necessário para teste)
    service_pages = [f for f in html_files if len(f.relative_to(base_path).parts) >= 3]

    success_count = 0
    skipped_count = 0
    error_count = 0

    for filepath in sorted(service_pages):
        relative_path = filepath.relative_to(base_path)
        success, msg = process_file(str(filepath))

        if success:
            print(f"✅ {relative_path}: {msg}")
            success_count += 1
        elif "Already sorted" in msg:
            print(f"⏭️  {relative_path}: {msg}")
            skipped_count += 1
        else:
            print(f"❌ {relative_path}: {msg}")
            error_count += 1

    print(f"\n📈 Resumo:")
    print(f"  ✅ Processadas: {success_count}")
    print(f"  ⏭️  Já ordenadas: {skipped_count}")
    print(f"  ❌ Erros: {error_count}")
    print(f"  📊 Total: {len(service_pages)}")

if __name__ == '__main__':
    main()
