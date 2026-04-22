#!/usr/bin/env python3
"""
Implementação de Wikidata + Wikipedia dupla verificação nas LPs de Serviço.
Atualiza Service.sameAs com Q-codes semanticamente corretos por tipo de serviço.

Estratégia (Rule R21 — Schema Markup Skill):
- Equipment rental (aluguel): Q5384579 + https://en.wikipedia.org/wiki/Car_rental
- Maintenance/Repair: Q116786099 + https://en.wikipedia.org/wiki/Maintenance_repair_operations
- Vocational education (curso): Q6869278 + https://en.wikipedia.org/wiki/Vocational_education
- Spare parts (peças): Q25394887 + https://en.wikipedia.org/wiki/Spare_part

IMPORTANTE: Service.sameAs NUNCA deve linkar para Clark (Q964158).
Clark linking (brand) vai APENAS em Product nodes, nunca em Service.
"""

import json
import os
import re
from pathlib import Path

# Mapa de tipos de serviço → Wikidata Q-codes + Wikipedia URLs
SERVICE_WIKIDATA_MAP = {
    "aluguel-de-empilhadeira-combustao": {
        "qcode": "Q5384579",
        "label": "Equipment rental",
        "wikipedia": "https://en.wikipedia.org/wiki/Equipment_rental"
    },
    "aluguel-de-empilhadeira-eletrica": {
        "qcode": "Q5384579",
        "label": "Equipment rental",
        "wikipedia": "https://en.wikipedia.org/wiki/Equipment_rental"
    },
    "manutencao-empilhadeira": {
        "qcode": "Q116786099",
        "label": "Maintenance, Repair and Operations",
        "wikipedia": "https://en.wikipedia.org/wiki/Maintenance_repair_operations"
    },
    "curso-de-operador-de-empilhadeira": {
        "qcode": "Q6869278",
        "label": "Vocational education",
        "wikipedia": "https://en.wikipedia.org/wiki/Vocational_education"
    },
    "pecas-e-assistencia-empilhadeira": {
        "qcode": "Q25394887",
        "label": "Spare part",
        "wikipedia": "https://en.wikipedia.org/wiki/Spare_part"
    }
}

# 13 cidades mapeadas
CITIES = [
    "goiania-go", "brasilia-df", "anapolis-go",
    "aparecida-de-goiania-go", "senador-canedo-go", "trindade-go",
    "caldas-novas-go", "inhumas-go",
    "formosa-go", "luziania-go", "valparaiso-de-goias-go",
    "uruacu-go", "itumbiara-go"
]

def extract_json_ld(html_content):
    """Extrai JSON-LD minificado do HTML."""
    pattern = r'<script type="application/ld\+json">({.*?})</script>'
    match = re.search(pattern, html_content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def update_service_sameAs(json_str, service_type):
    """
    Atualiza Service.sameAs com Q-code correto.
    Remove qualquer brand linking (Q964158) de Service nodes.
    """
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return None, f"JSON parse error: {e}"

    if not isinstance(data, dict) or "@graph" not in data:
        return None, "Not a @graph structure"

    graph = data["@graph"]
    modified = False

    service_info = SERVICE_WIKIDATA_MAP.get(service_type)
    if not service_info:
        return None, f"Unknown service type: {service_type}"

    qcode = service_info["qcode"]
    wikipedia_url = service_info["wikipedia"]
    wikidata_url = f"https://www.wikidata.org/wiki/{qcode}"

    for item in graph:
        item_type = item.get("@type", [])
        if isinstance(item_type, str):
            item_type = [item_type]

        # Atualiza Service ou Course nodes
        if any(t in item_type for t in ["Service", "Course"]):
            # Remove sameAs antigo (se existir)
            if "sameAs" in item:
                old_sameAs = item["sameAs"]
                # Log da mudança
                if isinstance(old_sameAs, list):
                    item["sameAs"] = [wikidata_url]
                else:
                    item["sameAs"] = [wikidata_url]
            else:
                item["sameAs"] = [wikidata_url]

            modified = True

    if modified:
        return json.dumps(data, separators=(',', ':'), ensure_ascii=False), None
    else:
        return None, "No Service/Course node found"

def process_file(filepath, city, service_type, dry_run=False):
    """Processa um arquivo HTML, atualizando Service.sameAs."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error: {e}"

    old_json_str = extract_json_ld(content)
    if not old_json_str:
        return False, "No JSON-LD found"

    new_json_str, error = update_service_sameAs(old_json_str, service_type)
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

        # Itera serviços
        for service_type in SERVICE_WIKIDATA_MAP.keys():
            if single_service and service_type != single_service:
                continue

            service_file = city_dir / service_type / "index.html"
            if service_file.exists():
                files_to_process.append((service_file, city, service_type))

    print(f"\n📋 Total de arquivos a processar: {len(files_to_process)}")
    if dry_run:
        print("🔍 Modo DRY-RUN (nenhuma escrita)")
    print()

    success_count = 0
    error_count = 0

    for filepath, city, service_type in files_to_process:
        result, msg = process_file(filepath, city, service_type, dry_run=dry_run)
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
        print("   python3 schema-fix-wikidata-sematico.py")

if __name__ == "__main__":
    main()
