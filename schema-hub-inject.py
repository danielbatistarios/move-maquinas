#!/usr/bin/env python3
"""
Injeta schema JSON-LD @graph nos 13 hubs de cidade + og:description + og:image.
Fase 1 da auditoria de schema markup — Move Máquinas.
"""
import json
import re
import os

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"

CITIES = [
    {
        "slug": "goiania-go",
        "name": "Goiânia",
        "state": "GO",
        "uf": "go",
        "lat": -16.6869,
        "lon": -49.2648,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-empilhadeira-eletrica","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","manutencao-empilhadeira","pecas-e-assistencia-empilhadeira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "aparecida-de-goiania-go",
        "name": "Aparecida de Goiânia",
        "state": "GO",
        "uf": "go",
        "lat": -16.8236,
        "lon": -49.2442,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "anapolis-go",
        "name": "Anápolis",
        "state": "GO",
        "uf": "go",
        "lat": -16.3281,
        "lon": -48.9530,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "senador-canedo-go",
        "name": "Senador Canedo",
        "state": "GO",
        "uf": "go",
        "lat": -16.7072,
        "lon": -49.0931,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "trindade-go",
        "name": "Trindade",
        "state": "GO",
        "uf": "go",
        "lat": -16.6533,
        "lon": -49.4922,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "inhumas-go",
        "name": "Inhumas",
        "state": "GO",
        "uf": "go",
        "lat": -16.3586,
        "lon": -49.4944,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "itumbiara-go",
        "name": "Itumbiara",
        "state": "GO",
        "uf": "go",
        "lat": -18.4158,
        "lon": -49.2158,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "caldas-novas-go",
        "name": "Caldas Novas",
        "state": "GO",
        "uf": "go",
        "lat": -17.7444,
        "lon": -48.6247,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "formosa-go",
        "name": "Formosa",
        "state": "GO",
        "uf": "go",
        "lat": -15.5353,
        "lon": -47.3336,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "luziania-go",
        "name": "Luziânia",
        "state": "GO",
        "uf": "go",
        "lat": -16.2525,
        "lon": -47.9503,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "valparaiso-de-goias-go",
        "name": "Valparaíso de Goiás",
        "state": "GO",
        "uf": "go",
        "lat": -16.0781,
        "lon": -47.9942,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "brasilia-df",
        "name": "Brasília",
        "state": "DF",
        "uf": "df",
        "lat": -15.7801,
        "lon": -47.9292,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
    {
        "slug": "uruacu-go",
        "name": "Uruaçu",
        "state": "GO",
        "uf": "go",
        "lat": -14.5236,
        "lon": -49.1411,
        "services": ["aluguel-de-empilhadeira-combustao","aluguel-de-plataforma-elevatoria-tesoura","aluguel-de-plataforma-elevatoria-articulada","aluguel-de-transpaleteira","curso-de-operador-de-empilhadeira"],
    },
]

SERVICE_NAMES = {
    "aluguel-de-empilhadeira-combustao": "Aluguel de Empilhadeira a Combustão",
    "aluguel-de-empilhadeira-eletrica": "Aluguel de Empilhadeira Elétrica",
    "aluguel-de-plataforma-elevatoria-tesoura": "Aluguel de Plataforma Elevatória Tesoura",
    "aluguel-de-plataforma-elevatoria-articulada": "Aluguel de Plataforma Elevatória Articulada",
    "aluguel-de-transpaleteira": "Aluguel de Transpaleteira Elétrica",
    "manutencao-empilhadeira": "Manutenção de Empilhadeira",
    "pecas-e-assistencia-empilhadeira": "Peças e Assistência para Empilhadeira",
    "curso-de-operador-de-empilhadeira": "Curso NR-11 Operador de Empilhadeira",
}

FAQ_TEMPLATE = [
    {
        "@type": "Question",
        "name": "A Movemáquinas atende em {city}?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sim. A Movemáquinas atende {city}, {state} com frota própria Clark, manutenção inclusa e entrega em até 24 horas."
        }
    },
    {
        "@type": "Question",
        "name": "Quais equipamentos estão disponíveis para locação em {city}?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Empilhadeiras a combustão e elétricas Clark, transpaleteiras elétricas e plataformas elevatórias tesoura e articuladas. Todos com manutenção preventiva e corretiva inclusa."
        }
    },
    {
        "@type": "Question",
        "name": "Como solicitar orçamento para {city}?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pelo WhatsApp (62) 98263-7300 ou pelo formulário do site. Resposta em horário comercial, segunda a sexta das 8h às 18h."
        }
    },
]

OG_IMAGE = "https://movemaquinas.com.br/assets/og-move-maquinas.jpg"


def build_schema(city):
    slug = city["slug"]
    name = city["name"]
    state = city["state"]
    base_url = f"https://movemaquinas.com.br/{slug}/"
    local_id = f"https://movemaquinas.com.br/{slug}/#localbusiness"
    webpage_id = f"https://movemaquinas.com.br/{slug}/#webpage"

    offer_catalog_items = []
    for svc_slug in city["services"]:
        svc_url = f"https://movemaquinas.com.br/{slug}/{svc_slug}/"
        svc_name = SERVICE_NAMES.get(svc_slug, svc_slug)
        offer_catalog_items.append({
            "@type": "Offer",
            "name": f"{svc_name} em {name}",
            "url": svc_url,
            "seller": {"@id": ORG_ID}
        })

    faq = []
    for q in FAQ_TEMPLATE:
        faq.append({
            "@type": "Question",
            "name": q["name"].replace("{city}", name).replace("{state}", state),
            "acceptedAnswer": {
                "@type": "Answer",
                "text": q["acceptedAnswer"]["text"].replace("{city}", name).replace("{state}", state)
            }
        })

    graph = [
        {
            "@type": ["LocalBusiness", "AutomotiveBusiness"],
            "@id": local_id,
            "name": f"Movemáquinas - {name}",
            "url": base_url,
            "telephone": ["+55-62-98263-7300", "+55-62-98175-3350"],
            "address": {
                "@type": "PostalAddress",
                "addressLocality": name,
                "addressRegion": state,
                "addressCountry": "BR"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": city["lat"],
                "longitude": city["lon"]
            },
            "areaServed": {
                "@type": "City",
                "name": name
            },
            "parentOrganization": {"@id": ORG_ID},
            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": f"Locação de Equipamentos em {name}",
                "itemListElement": offer_catalog_items
            }
        },
        {
            "@type": "WebPage",
            "@id": webpage_id,
            "url": base_url,
            "name": f"Aluguel de Equipamentos em {name} | Movemáquinas",
            "description": f"Locação de empilhadeiras, plataformas elevatórias e transpaleteiras em {name}, {state}. Frota Clark, manutenção inclusa.",
            "breadcrumb": {"@id": f"https://movemaquinas.com.br/{slug}/#breadcrumb"},
            "publisher": {"@id": ORG_ID}
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"https://movemaquinas.com.br/{slug}/#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://movemaquinas.com.br/"},
                {"@type": "ListItem", "position": 2, "name": name, "item": base_url}
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": faq
        }
    ]

    return {"@context": "https://schema.org", "@graph": graph}


def inject_schema_and_og(city):
    slug = city["slug"]
    filepath = os.path.join(BASE, slug, "index.html")
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Skip if JSON-LD already exists
    if 'application/ld+json' in html:
        print(f"  SKIP (JSON-LD already exists): {slug}")
        return

    schema = build_schema(city)
    schema_json = json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
    schema_block = f'<script type="application/ld+json">{schema_json}</script>\n'

    # Inject og:description and og:image if missing
    og_desc = city["name"]
    og_block = ""
    if 'og:description' not in html:
        og_block += f'<meta property="og:description" content="Locação de empilhadeiras, plataformas elevatórias e transpaleteiras em {city["name"]}, {city["state"]}. Frota Clark, manutenção inclusa. Movemáquinas.">\n'
    if 'og:image' not in html:
        og_block += f'<meta property="og:image" content="{OG_IMAGE}">\n'
    if 'og:type' not in html:
        og_block += f'<meta property="og:type" content="website">\n'

    # Inject before </head>
    inject = og_block + schema_block
    html = html.replace("</head>", inject + "</head>", 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  OK: {slug}")


if __name__ == "__main__":
    print("=== Schema Hub Inject — Move Máquinas ===")
    for city in CITIES:
        inject_schema_and_og(city)
    print("\nConcluído.")
