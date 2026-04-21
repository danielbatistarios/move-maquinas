#!/usr/bin/env python3
"""
Script 6: P2 elite enhancements for author page
1. Create @graph: ProfilePage + complete Person + BreadcrumbList
2. Person: all elite fields (@id, name, image, sameAs, hasOccupation, knowsAbout, description, worksFor, award)
"""
import json, re, os
from datetime import datetime

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"
WEBSITE_ID = "https://movemaquinas.com.br/#website"
PERSON_ID = "https://movemaquinas.com.br/#person-marcio"

def fix_author_page():
    path = os.path.join(BASE, "author-marcio-lima.html")
    if not os.path.exists(path):
        return False

    with open(path, encoding="utf-8") as f:
        html = f.read()

    page_url = "https://movemaquinas.com.br/about/marcio-lima/"
    profile_id = "https://movemaquinas.com.br/about/marcio-lima/#page"
    breadcrumb_id = "https://movemaquinas.com.br/about/marcio-lima/#breadcrumb"

    # Create elite schema
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ProfilePage",
                "@id": profile_id,
                "url": page_url,
                "name": "Márcio Lima - Especialista em Equipamentos Clark",
                "description": "Perfil do especialista em equipamentos Clark da Move Máquinas.",
                "inLanguage": "pt-BR",
                "dateModified": datetime.now().isoformat(),
                "about": {"@id": PERSON_ID},
                "isPartOf": {"@id": WEBSITE_ID},
                "publisher": {"@id": ORG_ID},
                "breadcrumb": {"@id": breadcrumb_id}
            },
            {
                "@type": "Person",
                "@id": PERSON_ID,
                "name": "Márcio Lima",
                "givenName": "Márcio",
                "familyName": "Lima",
                "url": page_url,
                "image": {
                    "@type": "ImageObject",
                    "url": "https://movemaquinas.com.br/assets/authors/marcio-lima.webp",
                    "width": 600,
                    "height": 600
                },
                "sameAs": [
                    "https://www.linkedin.com/in/m%C3%A1rciolima/",
                    "https://www.youtube.com/@movemaquinas5637"
                ],
                "hasOccupation": {
                    "@type": "Occupation",
                    "name": "Especialista em Equipamentos de Movimentação",
                    "description": "Especialista em locação, manutenção e operação de equipamentos Clark"
                },
                "knowsAbout": [
                    "Empilhadeiras Clark",
                    "Plataformas Elevatórias",
                    "Transpaleteiras Elétricas",
                    "Manutenção Industrial",
                    "Norma NR-11",
                    "Segurança do Trabalho"
                ],
                "description": "Especialista em equipamentos Clark com mais de 15 anos de experiência em locação, manutenção e operação de máquinas de movimentação de cargas. Referência técnica e comercial na Move Máquinas.",
                "worksFor": {
                    "@type": "Organization",
                    "@id": ORG_ID
                },
                "award": [
                    "Distribuidor Autorizado Clark",
                    "Especialista Certificado em Segurança Industrial"
                ]
            },
            {
                "@type": "BreadcrumbList",
                "@id": breadcrumb_id,
                "isPartOf": {"@id": profile_id},
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
                        "name": "Sobre",
                        "item": "https://movemaquinas.com.br/sobre/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": "Márcio Lima",
                        "item": page_url
                    }
                ]
            }
        ]
    }

    new_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    new_block = f'<script type="application/ld+json">{new_json}</script>'

    # Remove old schema if present
    old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
    if old_match:
        html_out = html[:old_match.start()] + new_block + html[old_match.end():]
    else:
        # Insert before </head>
        html_out = html.replace("</head>", f"\n{new_block}\n</head>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html_out)

    return True


if __name__ == "__main__":
    print("=== Schema P2 — Author Page (1 página) ===")
    result = fix_author_page()
    if result is True:
        print("  OK: author-marcio-lima.html")
        print("\nOK: 1")
    else:
        print("  FAIL: author-marcio-lima.html")
        print("\nOK: 0 | FAIL: 1")
