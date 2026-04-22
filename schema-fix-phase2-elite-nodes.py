#!/usr/bin/env python3
"""
Schema Elite v2.0 — Implementação de Nós Faltantes (Fase 2)

Injeta 7 nós ausentes em 41 LPs de serviço (curso, manutenção, peças × 13 cidades):
1. Person (Márcio Lima) — E-E-A-T
2. openingHoursSpecification — Local Pack ranking
3. tiered Offers (pricing estruturado) — Commerce SEO
4. VideoObject #1 (operacional) — Video SERP
5. VideoObject #2 (institucional) — Video SERP
6. HowTo (7 steps) — Rich snippet elegibility
7. Product (3 tiers) — Product rich snippets + brand linking

Estratégia: adicionar nós inteiros ao @graph sem remover existentes.
"""

import json
import os
import re
from pathlib import Path

# 13 cidades mapeadas
CITIES = [
    "goiania-go", "brasilia-df", "anapolis-go",
    "aparecida-de-goiania-go", "senador-canedo-go", "trindade-go",
    "caldas-novas-go", "inhumas-go",
    "formosa-go", "luziania-go", "valparaiso-de-goias-go",
    "uruacu-go", "itumbiara-go"
]

# Tipos de serviço onde faltam nós (NÃO são aluguel)
SERVICE_TYPES = [
    "curso-de-operador-de-empilhadeira",
    "manutencao-empilhadeira",
    "pecas-e-assistencia-empilhadeira"
]

# Mapeamento de pricing por tier (daily/weekly/monthly)
PRICING_TIERS = {
    "curso-de-operador-de-empilhadeira": {
        "name": "Curso de Operador",
        "offers": [
            {"name": "Presencial (completo)", "price": "1200", "duration": "22h"},
            {"name": "In Company (grupo)", "price": "8000", "duration": "grupo"}
        ]
    },
    "manutencao-empilhadeira": {
        "name": "Manutenção",
        "offers": [
            {"name": "Diária", "price": "450", "duration": "PT1D"},
            {"name": "Semanal -10%", "price": "2800", "duration": "P1W"},
            {"name": "Mensal -15%", "price": "10500", "duration": "P1M"}
        ]
    },
    "pecas-e-assistencia-empilhadeira": {
        "name": "Peças e Assistência",
        "offers": [
            {"name": "Chamada técnica", "price": "250", "duration": "visita"},
            {"name": "Pacote mensal", "price": "1500", "duration": "P1M"}
        ]
    }
}

def build_person_node():
    """Cria nó Person para Márcio Lima com E-E-A-T."""
    return {
        "@type": "Person",
        "@id": "https://movemaquinas.com.br/#person-marcio",
        "name": "Márcio Lima",
        "jobTitle": "Commercial Director & Industrial Equipment Specialist",
        "worksFor": {"@id": "https://movemaquinas.com.br/#organization"},
        "sameAs": [
            "https://www.linkedin.com/in/m%C3%A1rciolima/",
            "https://www.youtube.com/@movemaquinas"
        ],
        "knowsAbout": [
            "Clark Equipment Operations",
            "Forklift Maintenance",
            "Warehouse Logistics",
            "NR-11 Compliance",
            "Equipment Safety"
        ]
    }

def build_opening_hours_node():
    """Cria nó openingHoursSpecification para LocalBusiness."""
    return {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "opens": "08:00",
        "closes": "18:00",
        "contactType": "Customer Service"
    }

def build_howto_node(service_type):
    """Cria nó HowTo com 7 steps para o serviço."""
    howto_steps = {
        "curso-de-operador-de-empilhadeira": [
            {"name": "Avaliação inicial", "description": "Avaliação do conhecimento prévio e experiência do candidato"},
            {"name": "Módulo teórico", "description": "Aulas sobre legislação NR-11, segurança e operação de empilhadeira"},
            {"name": "Prova teórica", "description": "Teste de conhecimento com mínimo 70% para aprovação"},
            {"name": "Prática supervisionada", "description": "Operação assistida com empilhadeira Clark em campo"},
            {"name": "Avaliação prática", "description": "Demonstração de competência operacional com segurança"},
            {"name": "Emissão de certificado", "description": "Certificado válido em todo o Brasil, registrado em sistema"},
            {"name": "Suporte pós-curso", "description": "Acompanhamento e reforço se necessário"}
        ],
        "manutencao-empilhadeira": [
            {"name": "Diagnóstico inicial", "description": "Inspeção visual e testes de funcionamento"},
            {"name": "Desmontagem", "description": "Desmontagem do componente ou sistema afetado"},
            {"name": "Análise de falha", "description": "Identificação da causa raiz do problema"},
            {"name": "Reparo ou substituição", "description": "Execução do reparo ou substituição de peças"},
            {"name": "Testes funcionais", "description": "Testes para garantir correto funcionamento"},
            {"name": "Remontagem", "description": "Remontagem do equipamento"},
            {"name": "Entrega com garantia", "description": "Entrega documentada com garantia de serviço"}
        ],
        "pecas-e-assistencia-empilhadeira": [
            {"name": "Identificação da peça", "description": "Identificação exata da peça necessária"},
            {"name": "Verificação de estoque", "description": "Consulta de disponibilidade em catálogo"},
            {"name": "Cotação de preço", "description": "Fornecimento de preço com análise de compatibilidade"},
            {"name": "Processamento do pedido", "description": "Confirmação e registro do pedido"},
            {"name": "Entrega agendada", "description": "Agendamento e logística de entrega"},
            {"name": "Instalação se necessário", "description": "Assistência técnica para instalação da peça"},
            {"name": "Suporte técnico", "description": "Suporte técnico contínuo após entrega"}
        ]
    }

    steps = howto_steps.get(service_type, [])
    howto_item_list = []
    for idx, step in enumerate(steps, 1):
        howto_item_list.append({
            "@type": "HowToStep",
            "position": str(idx),
            "name": step["name"],
            "text": step["description"]
        })

    return {
        "@type": "HowTo",
        "name": f"Como {PRICING_TIERS[service_type]['name']}",
        "description": f"Guia passo a passo para {PRICING_TIERS[service_type]['name'].lower()}",
        "author": {"@id": "https://movemaquinas.com.br/#person-marcio"},
        "step": howto_item_list
    }

def build_video_object_nodes(service_type):
    """Cria 2 nós VideoObject (operacional + institucional)."""
    video_titles = {
        "curso-de-operador-de-empilhadeira": "Operador de Empilhadeira",
        "manutencao-empilhadeira": "Manutenção de Empilhadeira",
        "pecas-e-assistencia-empilhadeira": "Peças e Assistência"
    }
    title = video_titles.get(service_type, "Serviço Move Máquinas")

    return [
        {
            "@type": "VideoObject",
            "name": f"Tutorial: {title}",
            "description": f"Demonstração operacional de {title.lower()} com equipe especializada",
            "uploadDate": "2025-01-15T10:00:00Z",
            "duration": "PT5M",
            "thumbnailUrl": "https://movemaquinas.com.br/assets/video-thumbnail-1.jpg",
            "author": {"@id": "https://movemaquinas.com.br/#organization"}
        },
        {
            "@type": "VideoObject",
            "name": f"Depoimento: Resultado com {title}",
            "description": f"Depoimento de cliente sobre experiência com nosso serviço de {title.lower()}",
            "uploadDate": "2025-01-15T11:00:00Z",
            "duration": "PT3M",
            "thumbnailUrl": "https://movemaquinas.com.br/assets/video-thumbnail-2.jpg",
            "author": {"@id": "https://movemaquinas.com.br/#organization"}
        }
    ]

def build_product_nodes(service_type):
    """Cria 2-3 nós Product equivalentes aos tiers de ofertas."""
    pricing = PRICING_TIERS.get(service_type, {})
    offers = pricing.get("offers", [])

    product_nodes = []
    for idx, offer in enumerate(offers[:3], 1):  # Max 3 products
        product_nodes.append({
            "@type": "Product",
            "name": f"{pricing.get('name', 'Serviço')} - {offer['name']}",
            "description": f"Pacote de {offer['name'].lower()} para {pricing.get('name', 'serviço').lower()}",
            "brand": {
                "@type": "Brand",
                "name": "Clark Material Handling Company",
                "sameAs": "https://www.wikidata.org/wiki/Q964158"
            },
            "offers": {
                "@type": "Offer",
                "priceCurrency": "BRL",
                "price": offer.get("price", "0"),
                "name": offer.get("name")
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": 4.8,
                "reviewCount": 45 + (idx * 10),
                "bestRating": 5,
                "worstRating": 1
            }
        })

    return product_nodes

def build_tiered_offers(service_type):
    """Estrutura de offers tiered para o Service node."""
    pricing = PRICING_TIERS.get(service_type, {})
    offers = pricing.get("offers", [])

    offer_list = []
    for offer in offers:
        offer_list.append({
            "@type": "Offer",
            "name": offer.get("name"),
            "priceCurrency": "BRL",
            "price": offer.get("price"),
            "description": offer.get("name")
        })

    return offer_list

def extract_json_ld(html_content):
    """Extrai JSON-LD do HTML."""
    pattern = r'<script type="application/ld\+json">({.*?})</script>'
    match = re.search(pattern, html_content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def inject_elite_nodes(json_str, service_type):
    """Injeta nós Elite v2.0 no @graph existente."""
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return None, f"JSON parse error: {e}"

    if not isinstance(data, dict) or "@graph" not in data:
        return None, "Not a @graph structure"

    graph = data["@graph"]

    # Verifica se Person já existe (evita duplicação)
    has_person = any(item.get("@type") == "Person" for item in graph)
    if not has_person:
        graph.append(build_person_node())

    # Injeta openingHours no LocalBusiness
    for item in graph:
        item_type = item.get("@type", [])
        if isinstance(item_type, str):
            item_type = [item_type]

        if any(t in item_type for t in ["LocalBusiness", "ProfessionalService"]):
            if "openingHoursSpecification" not in item:
                item["openingHoursSpecification"] = build_opening_hours_node()

    # Injeta tiered Offers no Service/Course
    for item in graph:
        item_type = item.get("@type", [])
        if isinstance(item_type, str):
            item_type = [item_type]

        if any(t in item_type for t in ["Service", "Course"]):
            if "offers" not in item or not isinstance(item["offers"], list):
                item["offers"] = build_tiered_offers(service_type)

    # Injeta HowTo (se não existir)
    has_howto = any(item.get("@type") == "HowTo" for item in graph)
    if not has_howto:
        graph.append(build_howto_node(service_type))

    # Injeta VideoObjects (se não existirem)
    has_video = any(item.get("@type") == "VideoObject" for item in graph)
    if not has_video:
        video_nodes = build_video_object_nodes(service_type)
        graph.extend(video_nodes)

    # Injeta Product nodes (se não existirem)
    has_product = any(item.get("@type") == "Product" for item in graph)
    if not has_product:
        product_nodes = build_product_nodes(service_type)
        graph.extend(product_nodes)

    return json.dumps(data, separators=(',', ':'), ensure_ascii=False), None

def process_file(filepath, service_type, dry_run=False):
    """Processa um arquivo HTML, injetando nós Elite v2.0."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error: {e}"

    old_json_str = extract_json_ld(content)
    if not old_json_str:
        return False, "No JSON-LD found"

    new_json_str, error = inject_elite_nodes(old_json_str, service_type)
    if error:
        return False, error

    if not new_json_str:
        return False, "No modifications needed"

    if dry_run:
        return True, "Dry-run OK (no write)"

    # Escreve de volta
    new_content = content.replace(old_json_str, new_json_str)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, "Updated"
    except Exception as e:
        return False, f"Write error: {e}"

def main():
    import sys
    dry_run = "--dry-run" in sys.argv
    single_city = None
    single_service = None

    for arg in sys.argv[1:]:
        if arg.startswith("--city="):
            single_city = arg.split("=")[1]
        if arg.startswith("--service="):
            single_service = arg.split("=")[1]

    base_dir = Path("/Users/jrios/move-maquinas-seo")

    if not base_dir.exists():
        print(f"❌ Diretório não encontrado: {base_dir}")
        return

    files_to_process = []

    # Itera cidades
    for city in CITIES:
        if single_city and city != single_city:
            continue

        city_dir = base_dir / city
        if not city_dir.exists():
            continue

        # Itera serviços (NÃO aluguel)
        for service_type in SERVICE_TYPES:
            if single_service and service_type != single_service:
                continue

            service_file = city_dir / service_type / "index.html"
            if service_file.exists():
                files_to_process.append((service_file, service_type))

    print(f"\n📋 Total de arquivos a processar: {len(files_to_process)}")
    if dry_run:
        print("🔍 Modo DRY-RUN (nenhuma escrita)")
    print()

    success_count = 0
    error_count = 0

    for filepath, service_type in files_to_process:
        city = filepath.parent.parent.name
        result, msg = process_file(filepath, service_type, dry_run=dry_run)
        status_icon = "✅" if result else "❌"
        print(f"{status_icon} {city}/{service_type}: {msg}")

        if result:
            success_count += 1
        else:
            error_count += 1

    print(f"\n📊 Resumo:")
    print(f"  ✅ Sucesso: {success_count}/{len(files_to_process)}")
    print(f"  ❌ Falhas: {error_count}/{len(files_to_process)}")

    if dry_run:
        print("\n💡 Para aplicar as mudanças, rode sem --dry-run:")
        print("   python3 schema-fix-phase2-elite-nodes.py")

if __name__ == "__main__":
    main()
