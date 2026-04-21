#!/usr/bin/env python3
"""
Round 2 — Batch fix para todos os LPs de serviço (91 páginas):
1. @type: AutomotiveBusiness → ["LocalBusiness","ProfessionalService"]
2. Service: add @id + potentialAction RentAction (ou LearnAction em cursos)
3. Service: add sameAs Wikidata em areaServed.City
4. Service: add businessFunction (LeaseOut ou Teach)
5. BreadcrumbList: add @id + isPartOf → #webpage
6. BreadcrumbList pos.3: fix trailing slash na URL
7. LocalBusiness: fix telephone string → remover (já está na home via #org ref)
8. LocalBusiness: fix taxID → sem formatação
9. LocalBusiness: add parentOrganization + sameAs → #organization
"""
import json, re, os

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"

CITY_DATA = {
    "goiania-go":              {"name": "Goiânia",              "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q128387"},
    "aparecida-de-goiania-go": {"name": "Aparecida de Goiânia", "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1034461"},
    "anapolis-go":             {"name": "Anápolis",              "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q582601"},
    "senador-canedo-go":       {"name": "Senador Canedo",        "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1023869"},
    "trindade-go":             {"name": "Trindade",              "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1006009"},
    "inhumas-go":              {"name": "Inhumas",               "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1521813"},
    "itumbiara-go":            {"name": "Itumbiara",             "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q974395"},
    "caldas-novas-go":         {"name": "Caldas Novas",          "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q875474"},
    "formosa-go":              {"name": "Formosa",               "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q623042"},
    "luziania-go":             {"name": "Luziânia",              "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q729963"},
    "valparaiso-de-goias-go":  {"name": "Valparaíso de Goiás",  "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1042820"},
    "brasilia-df":             {"name": "Brasília",              "uf": "DF", "wikidata": "https://www.wikidata.org/wiki/Q2966"},
    "uruacu-go":               {"name": "Uruaçu",               "uf": "GO", "wikidata": "https://www.wikidata.org/wiki/Q1064382"},
}

SERVICE_META = {
    "aluguel-de-empilhadeira-combustao": {
        "label": "Aluguel de Empilhadeira a Combustão",
        "serviceType": "Locação de Empilhadeira a Combustão",
        "businessFunction": "https://purl.org/goodrelations/v1#LeaseOut",
        "rentAction": True,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q187959", "name": "Empilhadeira"},
    },
    "aluguel-de-empilhadeira-eletrica": {
        "label": "Aluguel de Empilhadeira Elétrica",
        "serviceType": "Locação de Empilhadeira Elétrica",
        "businessFunction": "https://purl.org/goodrelations/v1#LeaseOut",
        "rentAction": True,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q187959", "name": "Empilhadeira"},
    },
    "aluguel-de-plataforma-elevatoria-tesoura": {
        "label": "Aluguel de Plataforma Elevatória Tesoura",
        "serviceType": "Locação de Plataforma Elevatória Tesoura",
        "businessFunction": "https://purl.org/goodrelations/v1#LeaseOut",
        "rentAction": True,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q1142888", "name": "Plataforma Elevatória"},
    },
    "aluguel-de-plataforma-elevatoria-articulada": {
        "label": "Aluguel de Plataforma Elevatória Articulada",
        "serviceType": "Locação de Plataforma Elevatória Articulada",
        "businessFunction": "https://purl.org/goodrelations/v1#LeaseOut",
        "rentAction": True,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q1142888", "name": "Plataforma Elevatória"},
    },
    "aluguel-de-transpaleteira": {
        "label": "Aluguel de Transpaleteira Elétrica",
        "serviceType": "Locação de Transpaleteira Elétrica",
        "businessFunction": "https://purl.org/goodrelations/v1#LeaseOut",
        "rentAction": True,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q1860965", "name": "Transpaleteira"},
    },
    "manutencao-empilhadeira": {
        "label": "Manutenção de Empilhadeira",
        "serviceType": "Manutenção de Empilhadeira Clark",
        "businessFunction": "https://purl.org/goodrelations/v1#Maintain",
        "rentAction": False,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q187959", "name": "Empilhadeira"},
    },
    "pecas-e-assistencia-empilhadeira": {
        "label": "Peças e Assistência para Empilhadeira",
        "serviceType": "Peças e Assistência Técnica para Empilhadeira Clark",
        "businessFunction": "https://purl.org/goodrelations/v1#Sell",
        "rentAction": False,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q187959", "name": "Empilhadeira"},
    },
    "curso-de-operador-de-empilhadeira": {
        "label": "Curso NR-11 Operador de Empilhadeira",
        "serviceType": "Curso NR-11 para Operadores de Empilhadeira",
        "businessFunction": "https://purl.org/goodrelations/v1#Sell",
        "rentAction": False,
        "learnAction": True,
        "subject": {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q187959", "name": "Empilhadeira"},
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
    except json.JSONDecodeError as e:
        print(f"    JSON INVALID: {e}")
        return "invalid"
    graph = data.get("@graph", [])

    city = CITY_DATA[city_slug]
    svc  = SERVICE_META[svc_slug]
    page_url  = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/"
    webpage_id = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/#webpage"
    breadcrumb_id = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/#breadcrumb"
    service_id = f"https://movemaquinas.com.br/{city_slug}/{svc_slug}/#service"

    for node in graph:
        t = node.get("@type", "")
        types = t if isinstance(t, list) else [t]

        # ── LocalBusiness node ───────────────────────────────────────────────
        if "LocalBusiness" in types or "AutomotiveBusiness" in types:
            node["@type"] = ["LocalBusiness", "ProfessionalService"]
            # Fix taxID formatting
            if "taxID" in node:
                node["taxID"] = re.sub(r"[.\-/]", "", node["taxID"])
            # Remove bare telephone string (already in home org)
            node.pop("telephone", None)
            # Add parentOrganization + sameAs to #organization
            node["parentOrganization"] = {"@id": ORG_ID}
            if "sameAs" not in node:
                node["sameAs"] = [ORG_ID]

        # ── Service node ─────────────────────────────────────────────────────
        elif "Service" in types:
            node["@id"] = service_id
            node["serviceType"] = svc["serviceType"]
            node["subject"] = svc["subject"]
            # Fix areaServed City — add sameAs Wikidata
            if "areaServed" in node and isinstance(node["areaServed"], dict):
                node["areaServed"]["@type"] = "City"
                node["areaServed"]["name"] = city["name"]
                node["areaServed"]["sameAs"] = city["wikidata"]
            # businessFunction
            node["businessFunction"] = svc["businessFunction"]
            # potentialAction
            if svc.get("rentAction"):
                node["potentialAction"] = {
                    "@type": "RentAction",
                    "target": page_url,
                    "object": {"@type": "Service", "name": svc["label"]}
                }
            elif svc.get("learnAction"):
                node["potentialAction"] = {
                    "@type": "LearnAction",
                    "target": page_url
                }

        # ── BreadcrumbList node ───────────────────────────────────────────────
        elif "BreadcrumbList" in types:
            node["@id"] = breadcrumb_id
            node["isPartOf"] = {"@id": webpage_id}
            # Fix trailing slash on last item
            items = node.get("itemListElement", [])
            for item in items:
                if "item" in item and isinstance(item["item"], str):
                    if not item["item"].endswith("/"):
                        item["item"] = item["item"] + "/"

        # ── FAQPage node ──────────────────────────────────────────────────────
        elif "FAQPage" in types:
            node["about"] = {"@id": ORG_ID}
            node["isPartOf"] = {"@id": webpage_id}

    # Add WebPage node if not present
    has_webpage = any("WebPage" in (n.get("@type","") if isinstance(n.get("@type",""), str) else " ".join(n.get("@type",[]))) for n in graph)
    if not has_webpage:
        graph.insert(1, {
            "@type": "WebPage",
            "@id": webpage_id,
            "url": page_url,
            "name": f"{svc['label']} em {city['name']} | Movemáquinas",
            "breadcrumb": {"@id": breadcrumb_id},
            "publisher": {"@id": ORG_ID}
        })

    new_json  = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    new_block = f'<script type="application/ld+json">{new_json}</script>'
    old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
    html_out  = html[:old_match.start()] + new_block + html[old_match.end():]

    with open(path, "w", encoding="utf-8") as f:
        f.write(html_out)

    return True


if __name__ == "__main__":
    print("=== Schema Fix P0 — LPs de Serviço ===")
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
