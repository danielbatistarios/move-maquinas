#!/usr/bin/env python3
"""
Script 1: P0 + P1 fixes for 13 city hubs (city-slug/index.html)
1. LocalBusiness.@type: AutomotiveBusiness → ["LocalBusiness","ProfessionalService"]
2. LocalBusiness: add legalName, taxID, foundingDate
3. FAQPage: add @id, about, isPartOf
4. LocalBusiness: add logo, sameAs, openingHoursSpecification, description, priceRange, contactPoint, award
5. WebPage: add inLanguage, dateModified, speakableSpecification, mainEntity
6. BreadcrumbList: add isPartOf
"""
import json, re, os
from datetime import datetime

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"
WEBSITE_ID = "https://movemaquinas.com.br/#website"

CITY_SLUGS = [
    "goiania-go",
    "aparecida-de-goiania-go",
    "anapolis-go",
    "senador-canedo-go",
    "trindade-go",
    "inhumas-go",
    "itumbiara-go",
    "caldas-novas-go",
    "formosa-go",
    "luziania-go",
    "valparaiso-de-goias-go",
    "brasilia-df",
    "uruacu-go",
]

CITY_DATA = {
    "goiania-go": {"name": "Goiânia", "uf": "GO"},
    "aparecida-de-goiania-go": {"name": "Aparecida de Goiânia", "uf": "GO"},
    "anapolis-go": {"name": "Anápolis", "uf": "GO"},
    "senador-canedo-go": {"name": "Senador Canedo", "uf": "GO"},
    "trindade-go": {"name": "Trindade", "uf": "GO"},
    "inhumas-go": {"name": "Inhumas", "uf": "GO"},
    "itumbiara-go": {"name": "Itumbiara", "uf": "GO"},
    "caldas-novas-go": {"name": "Caldas Novas", "uf": "GO"},
    "formosa-go": {"name": "Formosa", "uf": "GO"},
    "luziania-go": {"name": "Luziânia", "uf": "GO"},
    "valparaiso-de-goias-go": {"name": "Valparaíso de Goiás", "uf": "GO"},
    "brasilia-df": {"name": "Brasília", "uf": "DF"},
    "uruacu-go": {"name": "Uruaçu", "uf": "GO"},
}

def fix_hub(city_slug):
    path = os.path.join(BASE, city_slug, "index.html")
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
    hub_url = f"https://movemaquinas.com.br/{city_slug}/"
    webpage_id = f"https://movemaquinas.com.br/{city_slug}/#webpage"
    breadcrumb_id = f"https://movemaquinas.com.br/{city_slug}/#breadcrumb"
    faq_id = f"https://movemaquinas.com.br/{city_slug}/#faqpage"

    for node in graph:
        t = node.get("@type", "")
        types = t if isinstance(t, list) else [t]

        # ── LocalBusiness: P0 + P1 ────────────────────────────────────────────
        if "LocalBusiness" in types or "AutomotiveBusiness" in types:
            # P0: fix @type
            node["@type"] = ["LocalBusiness", "ProfessionalService"]
            # P0: add corporate identity
            node["legalName"] = "Movemaquinas Comercio de Pecas LTDA"
            node["taxID"] = "32428258000180"
            node["foundingDate"] = "2019-01-07"
            # P1: logo
            if "logo" not in node:
                node["logo"] = {
                    "@type": "ImageObject",
                    "url": "https://movemaquinas.com.br/assets/logo-movemaquinas.png",
                    "width": 200,
                    "height": 60
                }
            # P1: sameAs
            if "sameAs" not in node:
                node["sameAs"] = [
                    "https://www.google.com/maps/place/Movemáquinas",
                    "https://www.linkedin.com/company/move-maquinas-oficial/",
                    "https://www.youtube.com/@movemaquinas5637"
                ]
            # P1: openingHoursSpecification (if not present)
            if "openingHoursSpecification" not in node:
                node["openingHoursSpecification"] = [
                    {
                        "@type": "OpeningHoursSpecification",
                        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                        "opens": "08:00",
                        "closes": "18:00"
                    },
                    {
                        "@type": "OpeningHoursSpecification",
                        "dayOfWeek": "Saturday",
                        "opens": "08:00",
                        "closes": "12:00"
                    }
                ]
            # P1: description
            if "description" not in node:
                node["description"] = f"Aluguel e locação de empilhadeiras, plataformas elevatórias e transpaleteiras Clark em {city['name']}. Atendimento 24h, entrega rápida, equipamentos novos e bem mantidos."
            # P1: priceRange
            if "priceRange" not in node:
                node["priceRange"] = "BRL 500..3000"
            # P1: contactPoint (if not present)
            if "contactPoint" not in node:
                node["contactPoint"] = [
                    {
                        "@type": "ContactPoint",
                        "telephone": "+55-62-98263-7300",
                        "contactType": "sales",
                        "areaServed": "BR",
                        "availableLanguage": "Portuguese"
                    }
                ]
            # P1: award
            if "award" not in node:
                node["award"] = "Distribuidor autorizado Clark"

        # ── WebPage: P1 ───────────────────────────────────────────────────────
        elif "WebPage" in types:
            node["@id"] = webpage_id
            if "inLanguage" not in node:
                node["inLanguage"] = "pt-BR"
            if "dateModified" not in node:
                node["dateModified"] = datetime.now().isoformat()
            if "speakableSpecification" not in node:
                node["speakableSpecification"] = {
                    "@type": "SpeakableSpecification",
                    "cssSelector": ["h1", "h2"]
                }
            if "mainEntity" not in node:
                node["mainEntity"] = {"@id": ORG_ID}

        # ── BreadcrumbList: P1 ─────────────────────────────────────────────────
        elif "BreadcrumbList" in types:
            node["@id"] = breadcrumb_id
            if "isPartOf" not in node:
                node["isPartOf"] = {"@id": webpage_id}

        # ── FAQPage: P0 + P1 ───────────────────────────────────────────────────
        elif "FAQPage" in types:
            node["@id"] = faq_id
            if "about" not in node:
                node["about"] = {"@id": ORG_ID}
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
    print("=== Schema P1 — City Hubs (13 páginas) ===")
    ok = fail = 0
    for city_slug in CITY_SLUGS:
        path = os.path.join(BASE, city_slug, "index.html")
        if not os.path.exists(path):
            fail += 1
            print(f"  SKIP: {city_slug} (arquivo não encontrado)")
            continue
        result = fix_hub(city_slug)
        if result is True:
            ok += 1
            print(f"  OK: {city_slug}")
        else:
            fail += 1
            print(f"  FAIL: {city_slug}")

    print(f"\nOK: {ok} | FAIL: {fail}")
