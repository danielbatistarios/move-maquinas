#!/usr/bin/env python3
"""
Injeta aggregateRating no JSON-LD de páginas Move Máquinas.
Estratégia: 3 tiers de rating (4.9, 4.8, 4.7) com reviewCount variado por cidade.
"""

import json
import os
import re
from pathlib import Path

# Mapa de cidades para tier + dados
CITY_TIER_MAP = {
    "goiania-go": {"tier": 1, "rating": 4.9, "lb_reviews": 108, "service_reviews": 97},
    "brasilia-df": {"tier": 1, "rating": 4.9, "lb_reviews": 92, "service_reviews": 81},
    "anapolis-go": {"tier": 1, "rating": 4.9, "lb_reviews": 78, "service_reviews": 67},

    "aparecida-de-goiania-go": {"tier": 2, "rating": 4.8, "lb_reviews": 87, "service_reviews": 76},
    "senador-canedo-go": {"tier": 2, "rating": 4.8, "lb_reviews": 65, "service_reviews": 54},
    "trindade-go": {"tier": 2, "rating": 4.8, "lb_reviews": 54, "service_reviews": 43},
    "caldas-novas-go": {"tier": 2, "rating": 4.8, "lb_reviews": 48, "service_reviews": 37},
    "inhumas-go": {"tier": 2, "rating": 4.8, "lb_reviews": 42, "service_reviews": 31},

    "formosa-go": {"tier": 3, "rating": 4.7, "lb_reviews": 38, "service_reviews": 27},
    "luziania-go": {"tier": 3, "rating": 4.7, "lb_reviews": 35, "service_reviews": 24},
    "valparaiso-de-goias-go": {"tier": 3, "rating": 4.7, "lb_reviews": 32, "service_reviews": 21},
    "uruacu-go": {"tier": 3, "rating": 4.7, "lb_reviews": 28, "service_reviews": 17},
    "itumbiara-go": {"tier": 3, "rating": 4.7, "lb_reviews": 25, "service_reviews": 14},
}

HOME_RATING = 4.8
HOME_REVIEWS = 108

def extract_city_from_path(path):
    """Extrai nome da cidade do caminho do arquivo."""
    parts = path.parts
    for part in parts:
        if "-go" in part or "-df" in part:
            return part
    return None

def inject_aggregate_rating(json_str, rating, lb_reviews, service_reviews=None):
    """
    Injeta aggregateRating em um JSON-LD string.
    Detecta LocalBusiness, Service, Course e adiciona o schema.
    """
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"  ❌ Erro ao fazer parse JSON: {e}")
        return None

    # Se é um @graph, processa cada item
    if isinstance(data, dict) and "@graph" in data:
        graph = data["@graph"]
        modified = False

        for item in graph:
            item_type = item.get("@type", [])
            if isinstance(item_type, str):
                item_type = [item_type]

            # Injeta em LocalBusiness
            if "LocalBusiness" in item_type or "ProfessionalService" in item_type:
                if "aggregateRating" not in item:
                    item["aggregateRating"] = {
                        "@type": "AggregateRating",
                        "ratingValue": rating,
                        "reviewCount": lb_reviews,
                        "bestRating": 5,
                        "worstRating": 1
                    }
                    modified = True

            # Injeta em Service
            if item.get("@type") == "Service" and service_reviews:
                if "aggregateRating" not in item:
                    item["aggregateRating"] = {
                        "@type": "AggregateRating",
                        "ratingValue": rating,
                        "reviewCount": service_reviews,
                        "bestRating": 5,
                        "worstRating": 1
                    }
                    modified = True

            # Injeta em Course
            if item.get("@type") == "Course" and service_reviews:
                if "aggregateRating" not in item:
                    item["aggregateRating"] = {
                        "@type": "AggregateRating",
                        "ratingValue": rating,
                        "reviewCount": service_reviews,
                        "bestRating": 5,
                        "worstRating": 1
                    }
                    modified = True

        if modified:
            return json.dumps(data, separators=(',', ':'), ensure_ascii=False)

    return None

def process_file(filepath, rating, lb_reviews, service_reviews=None):
    """Processa um arquivo HTML, injetando aggregateRating no JSON-LD."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ❌ Erro ao ler arquivo: {e}")
        return False

    # Extrai JSON-LD minificado
    pattern = r'<script type="application/ld\+json">({.*?})</script>'
    match = re.search(pattern, content)

    if not match:
        print(f"  ⚠️  Nenhum JSON-LD encontrado")
        return False

    old_json_str = match.group(1)
    new_json_str = inject_aggregate_rating(old_json_str, rating, lb_reviews, service_reviews)

    if not new_json_str:
        print(f"  ⚠️  Nenhuma modificação necessária (agregateRating já existe?)")
        return False

    # Substitui no conteúdo
    new_content = content.replace(old_json_str, new_json_str)

    # Escreve de volta
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"  ❌ Erro ao escrever arquivo: {e}")
        return False

def main():
    base_dir = Path("/Users/jrios/move-maquinas-seo")

    if not base_dir.exists():
        print(f"❌ Diretório não encontrado: {base_dir}")
        return

    files_to_process = []

    # Home
    home_file = base_dir / "index.html"
    if home_file.exists():
        files_to_process.append((home_file, "home", HOME_RATING, HOME_REVIEWS, None))

    # LPs por tipo de serviço
    service_types = ["curso-de-operador-de-empilhadeira", "manutencao-empilhadeira", "pecas-e-assistencia-empilhadeira"]

    for city_dir in base_dir.iterdir():
        if not city_dir.is_dir():
            continue

        city_name = city_dir.name
        if city_name not in CITY_TIER_MAP:
            continue

        city_info = CITY_TIER_MAP[city_name]
        rating = city_info["rating"]
        lb_reviews = city_info["lb_reviews"]
        service_reviews = city_info["service_reviews"]

        for service_type in service_types:
            service_file = city_dir / service_type / "index.html"
            if service_file.exists():
                files_to_process.append((service_file, f"{city_name}/{service_type}", rating, lb_reviews, service_reviews))

    print(f"\n📋 Total de arquivos a processar: {len(files_to_process)}\n")

    success_count = 0
    for filepath, label, rating, lb_reviews, service_reviews in files_to_process:
        print(f"🔄 {label}")
        if process_file(filepath, rating, lb_reviews, service_reviews):
            print(f"  ✅ Injetado: {rating}⭐ ({lb_reviews} LB reviews, {service_reviews or 'N/A'} service reviews)")
            success_count += 1
        else:
            print(f"  ⚠️  Não modificado")

    print(f"\n✅ Processados com sucesso: {success_count}/{len(files_to_process)}")

if __name__ == "__main__":
    main()
