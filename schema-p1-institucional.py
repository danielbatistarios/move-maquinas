#!/usr/bin/env python3
"""
Script 5: P1 enhancements for 6 institutional pages
1. Convert schema solo → @graph wrapper
2. Add @id, inLanguage, dateModified, isPartOf, publisher to WebPage/AboutPage
3. Add/fix BreadcrumbList with @id and isPartOf
"""
import json, re, os
from datetime import datetime

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"
WEBSITE_ID = "https://movemaquinas.com.br/#website"

PAGES = {
    "sobre": {
        "type": "AboutPage",
        "name": "Sobre a Move Máquinas",
        "description": "Conheça a história, missão e valores da Move Máquinas, distribuidora oficial de equipamentos Clark.",
    },
    "contato": {
        "type": "ContactPage",
        "name": "Entre em Contato",
        "description": "Fale conosco sobre locação, manutenção ou dúvidas sobre equipamentos Clark.",
    },
    "politica-de-privacidade": {
        "type": "WebPage",
        "name": "Política de Privacidade",
        "description": "Conheça como a Move Máquinas protege seus dados pessoais.",
    },
    "termos-de-uso": {
        "type": "WebPage",
        "name": "Termos de Uso",
        "description": "Leia os termos e condições de uso do site da Move Máquinas.",
    },
    "cookies": {
        "type": "WebPage",
        "name": "Política de Cookies",
        "description": "Informações sobre o uso de cookies no site da Move Máquinas.",
    },
    "trabalhe-conosco": {
        "type": "WebPage",
        "name": "Trabalhe Conosco",
        "description": "Oportunidades de trabalho na Move Máquinas.",
    },
}

def fix_institucional(slug, page_meta):
    path = os.path.join(BASE, slug, "index.html")
    if not os.path.exists(path):
        return False

    with open(path, encoding="utf-8") as f:
        html = f.read()

    # Check if schema already has @graph
    has_graph = '"@graph"' in html

    # Extract existing schema blocks
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)

    if not blocks:
        # No schema at all - create from scratch
        page_url = f"https://movemaquinas.com.br/{slug}/"
        webpage_id = f"https://movemaquinas.com.br/{slug}/#webpage"
        breadcrumb_id = f"https://movemaquinas.com.br/{slug}/#breadcrumb"

        data = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": page_meta["type"],
                    "@id": webpage_id,
                    "url": page_url,
                    "name": page_meta["name"],
                    "description": page_meta["description"],
                    "inLanguage": "pt-BR",
                    "dateModified": datetime.now().isoformat(),
                    "publisher": {"@id": ORG_ID},
                    "isPartOf": {"@id": WEBSITE_ID},
                    "breadcrumb": {"@id": breadcrumb_id},
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": breadcrumb_id,
                    "isPartOf": {"@id": webpage_id},
                    "itemListElement": [
                        {
                            "@type": "ListItem",
                            "position": 1,
                            "name": "Início",
                            "item": "https://movemaquinas.com.br/"
                        },
                        {
                            "@type": "ListItem",
                            "position": 2,
                            "name": page_meta["name"],
                            "item": page_url
                        }
                    ]
                }
            ]
        }
        new_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        new_block = f'<script type="application/ld+json">{new_json}</script>'
        # Find first occurrence of any JSON-LD block or insert before </head>
        old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
        if old_match:
            html_out = html[:old_match.start()] + new_block + html[old_match.end():]
        else:
            # No existing block - insert before </head>
            html_out = html.replace("</head>", f"{new_block}\n</head>", 1)
    else:
        # Has schema - wrap in @graph if not already
        if has_graph:
            # Already @graph - just update fields
            data = json.loads(blocks[0])
            graph = data.get("@graph", [])
        else:
            # Single schema - convert to @graph
            try:
                existing = json.loads(blocks[0])
                data = {
                    "@context": "https://schema.org",
                    "@graph": [existing]
                }
                graph = data["@graph"]
            except json.JSONDecodeError:
                return "invalid"

        page_url = f"https://movemaquinas.com.br/{slug}/"
        webpage_id = f"https://movemaquinas.com.br/{slug}/#webpage"
        breadcrumb_id = f"https://movemaquinas.com.br/{slug}/#breadcrumb"

        for node in graph:
            t = node.get("@type", "")
            types = t if isinstance(t, list) else [t]

            if any(tp in types for tp in ["WebPage", "AboutPage", "ContactPage"]):
                if "@id" not in node:
                    node["@id"] = webpage_id
                if "url" not in node:
                    node["url"] = page_url
                if "inLanguage" not in node:
                    node["inLanguage"] = "pt-BR"
                if "dateModified" not in node:
                    node["dateModified"] = datetime.now().isoformat()
                if "publisher" not in node:
                    node["publisher"] = {"@id": ORG_ID}
                if "isPartOf" not in node:
                    node["isPartOf"] = {"@id": WEBSITE_ID}
                if "breadcrumb" not in node:
                    node["breadcrumb"] = {"@id": breadcrumb_id}

            elif "BreadcrumbList" in types:
                if "@id" not in node:
                    node["@id"] = breadcrumb_id
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
    print("=== Schema P1 — Institutional Pages (6 páginas) ===")
    ok = fail = 0
    for slug, meta in PAGES.items():
        path = os.path.join(BASE, slug, "index.html")
        if not os.path.exists(path):
            fail += 1
            print(f"  SKIP: {slug}")
            continue
        result = fix_institucional(slug, meta)
        if result is True:
            ok += 1
            print(f"  OK: {slug}")
        elif result == "invalid":
            fail += 1
            print(f"  INVALID JSON: {slug}")
        else:
            fail += 1
            print(f"  FAIL: {slug}")

    print(f"\nOK: {ok} | FAIL: {fail}")
