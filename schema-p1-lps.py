#!/usr/bin/env python3
"""
Script 2A: P1 enhancements for 78 service LPs (6 service types × 13 cities)
1. WebPage: add description, inLanguage, dateModified, speakableSpecification
2. Service: add image
3. Normalize areaServed with serviceArea.sameAs Wikidata
4. FAQPage: add @id if absent
"""
import json, re, os
from datetime import datetime

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"

CITY_DATA = {
    "goiania-go": {"name": "Goiânia", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q128387"},
    "aparecida-de-goiania-go": {"name": "Aparecida de Goiânia", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1034461"},
    "anapolis-go": {"name": "Anápolis", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q582601"},
    "senador-canedo-go": {"name": "Senador Canedo", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1023869"},
    "trindade-go": {"name": "Trindade", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1006009"},
    "inhumas-go": {"name": "Inhumas", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1521813"},
    "itumbiara-go": {"name": "Itumbiara", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q974395"},
    "caldas-novas-go": {"name": "Caldas Novas", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q875474"},
    "formosa-go": {"name": "Formosa", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q623042"},
    "luziania-go": {"name": "Luziânia", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q729963"},
    "valparaiso-de-goias-go": {"name": "Valparaíso de Goiás", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1042820"},
    "brasilia-df": {"name": "Brasília", "uf": "DF", "wikidata": "https://www.wikidata.org/wiki/Q2966"},
    "uruacu-go": {"name": "Uruaçu", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1064382"},
}

SERVICE_META = {
    "aluguel-de-empilhadeira-combustao": {
        "label": "Aluguel de Empilhadeira a Combustão",
        "description": "Aluguel de empilhadeiras Clark a combustão com entrega rápida em {{CITY}}",
        "image": "https://movemaquinas.com.br/assets/clark/empilhadeira-combustao/c60-70-75-80/studio_lep_frontangle.webp",
    },
    "aluguel-de-empilhadeira-eletrica": {
        "label": "Aluguel de Empilhadeira Elétrica",
        "description": "Aluguel de empilhadeiras Clark elétricas com tecnologia moderna em {{CITY}}",
        "image": "https://movemaquinas.com.br/assets/clark/empilhadeira-eletrica/lep-20-35/studio_lep_frontangle.webp",
    },
    "aluguel-de-plataforma-elevatoria-tesoura": {
        "label": "Aluguel de Plataforma Elevatória Tesoura",
        "description": "Locação de plataformas elevatórias tipo tesoura para trabalhos em altura em {{CITY}}",
        "image": "https://movemaquinas.com.br/assets/clark/empilhadeira-eletrica/lep-20-35/studio_lep_side.webp",
    },
    "aluguel-de-plataforma-elevatoria-articulada": {
        "label": "Aluguel de Plataforma Elevatória Articulada",
        "description": "Locação de plataformas elevatórias articuladas para acesso a espaços restritos em {{CITY}}",
        "image": "https://movemaquinas.com.br/assets/clark/empilhadeira-eletrica/lep-20-35/studio_lep_rearangle.webp",
    },
    "aluguel-de-transpaleteira": {
        "label": "Aluguel de Transpaleteira Elétrica",
        "description": "Aluguel de transpaleteiras Clark elétricas para movimentação de cargas em {{CITY}}",
        "image": "https://movemaquinas.com.br/assets/clark/transpaleteira/wpio20/wpio20_application-2.webp",
    },
    "manutencao-empilhadeira": {
        "label": "Manutenção de Empilhadeira",
        "description": "Serviço de manutenção preventiva e corretiva de empilhadeiras Clark em {{CITY}}",
        "image": "https://movemaquinas.com.br/assets/clark/empilhadeira-combustao/l25-30-35/studio_lep_frontangle.webp",
    },
}

CITY_SLUGS = list(CITY_DATA.keys())
SERVICE_SLUGS = list(SERVICE_META.keys())


def fix_lp(city_slug, svc_slug):
    path = os.path.join(BASE, city_slug, svc_slug, "index.html")
    if not os.path.exists(path):
        return False

    with open(path, encoding="utf-8") as f:
        html = f.read()

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if not blocks:
        return False

    try:
        data = json.loads(blocks[0])
    except json.JSONDecodeError:
        return "invalid"

    graph = data.get("@graph", [])
    city = CITY_DATA[city_slug]
    svc = SERVICE_META[svc_slug]
    page_url = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/"
    webpage_id = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/#webpage"
    service_id = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/#service"
    faq_id = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/#faqpage"

    for node in graph:
        t = node.get("@type", "")
        types = t if isinstance(t, list) else [t]

        # ── WebPage: P1 ────────────────────────────────────────────────────────
        if "WebPage" in types:
            node["@id"] = webpage_id
            if "description" not in node:
                node["description"] = svc["description"].replace("{{CITY}}", city["name"])
            if "inLanguage" not in node:
                node["inLanguage"] = "pt-BR"
            if "dateModified" not in node:
                node["dateModified"] = datetime.now().isoformat()
            if "speakableSpecification" not in node:
                node["speakableSpecification"] = {
                    "@type": "SpeakableSpecification",
                    "cssSelector": ["h1", "h2"]
                }

        # ── Service: P1 ────────────────────────────────────────────────────────
        elif "Service" in types:
            node["@id"] = service_id
            # Add image if not present
            if "image" not in node:
                node["image"] = {
                    "@type": "ImageObject",
                    "url": svc["image"],
                    "width": 600,
                    "height": 400
                }
            # Normalize areaServed with Wikidata sameAs
            if "areaServed" in node:
                if isinstance(node["areaServed"], dict):
                    node["areaServed"]["@type"] = "City"
                    node["areaServed"]["name"] = city["name"]
                    if "sameAs" not in node["areaServed"]:
                        node["areaServed"]["sameAs"] = city["wikidata"]
                elif isinstance(node["areaServed"], list):
                    for area in node["areaServed"]:
                        if isinstance(area, dict) and "City" in str(area.get("@type", "")):
                            if "sameAs" not in area:
                                area["sameAs"] = city["wikidata"]

        # ── FAQPage: P1 ────────────────────────────────────────────────────────
        elif "FAQPage" in types:
            if "@id" not in node:
                node["@id"] = faq_id
            if "isPartOf" not in node:
                node["isPartOf"] = {"@id": webpage_id}

    new_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    new_block = f'<script type="application/ld+json">{new_json}</script>'
    old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
    html_out = html[:old_match.start()] + new_block + html[old_match.end():]

    with open(path, "w", encoding="utf-8") as f:
        f.write(html_out)

    return True


if __name__ == "__main__":
    print("=== Schema P1 — Service LPs (78 páginas) ===")
    ok = fail = skip = 0
    for city_slug in CITY_SLUGS:
        for svc_slug in SERVICE_SLUGS:
            path = os.path.join(BASE, city_slug, svc_slug, "index.html")
            if not os.path.exists(path):
                skip += 1
                continue
            result = fix_lp(city_slug, svc_slug)
            if result is True:
                ok += 1
                print(f"  OK: {city_slug}/{svc_slug}")
            elif result == "invalid":
                fail += 1
                print(f"  INVALID JSON: {city_slug}/{svc_slug}")
            else:
                fail += 1
                print(f"  FAIL: {city_slug}/{svc_slug}")

    print(f"\nOK: {ok} | FAIL: {fail} | SKIP: {skip}")
