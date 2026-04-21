#!/usr/bin/env python3
"""
Fase 2 — Schema @graph unification
1. venda-de-maquinas-clark/index.html — 2 blocks → 1 @graph
2. cidades-atendidas/index.html — 1 partial block → @graph with ItemList
3. blog/*/index.html — N isolated blocks → 1 @graph per article
"""
import json, re, os

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"
WEBSITE_ID = "https://movemaquinas.com.br/#website"
PERSON_ID = "https://movemaquinas.com.br/#person-marcio"

# Blog article metadata — real distinct dates + descriptions/keywords
BLOG_META = {
    "alugar-ou-comprar": {
        "datePublished": "2026-03-12",
        "dateModified": "2026-04-09",
        "headline": "Alugar ou Comprar Empilhadeira: Quando Vale Cada Opção",
        "description": "Alugar ou comprar empilhadeira? Comparativo imparcial com dados reais: TCO de 24 meses, custos ocultos, cenários onde cada opção vence.",
        "keywords": ["alugar empilhadeira", "comprar empilhadeira", "locação vs compra", "TCO empilhadeira", "custo empilhadeira"],
        "articleSection": "Locação",
        "wordCount": 3400,
    },
    "andaime-vs-plataforma-custo-real": {
        "datePublished": "2026-03-20",
        "dateModified": "2026-04-10",
        "headline": "Andaime vs Plataforma Elevatória: Custo Real por Dia de Uso",
        "description": "Andaime ou plataforma elevatória? Análise do custo real por dia, produtividade, NR-18 e NR-35. Dados de obra em Goiânia.",
        "keywords": ["andaime vs plataforma elevatória", "custo plataforma elevatória", "NR-18", "NR-35", "trabalho em altura"],
        "articleSection": "Plataformas Elevatórias",
        "wordCount": 2800,
    },
    "plataforma-nr35-responsabilidade": {
        "datePublished": "2026-04-01",
        "dateModified": "2026-04-11",
        "headline": "NR-35 e Plataformas Elevatórias: Quem é Responsável na Locação",
        "description": "Quem responde pela NR-35 na locação de plataforma elevatória? Locatário, locador ou operador? Guia jurídico e técnico com a divisão exata de responsabilidades.",
        "keywords": ["NR-35", "responsabilidade locação plataforma", "plataforma elevatória", "trabalho em altura", "segurança trabalho"],
        "articleSection": "Segurança e Normas",
        "wordCount": 2600,
    },
    "andaime-vilao-cronograma-obra": {
        "datePublished": "2026-04-08",
        "dateModified": "2026-04-12",
        "headline": "Andaime: O Vilão Oculto do Cronograma de Obra",
        "description": "Andaimes travam obras por montagem lenta, risco de queda e área bloqueada. Veja como plataformas elevatórias reduzem prazo em até 40%.",
        "keywords": ["andaime", "atraso de obra", "plataforma elevatória", "produtividade obra", "cronograma construção"],
        "articleSection": "Plataformas Elevatórias",
        "wordCount": 2500,
    },
}

# 13 cities with Wikidata IDs (same as home)
CITIES_HUBS = [
    {"name": "Goiânia", "slug": "goiania-go", "state": "GO", "lat": -16.6869, "lon": -49.2648,
     "wikidata": "https://www.wikidata.org/wiki/Q131426"},
    {"name": "Aparecida de Goiânia", "slug": "aparecida-de-goiania-go", "state": "GO", "lat": -16.8236, "lon": -49.2442,
     "wikidata": "https://www.wikidata.org/wiki/Q1041394"},
    {"name": "Anápolis", "slug": "anapolis-go", "state": "GO", "lat": -16.3281, "lon": -48.9530,
     "wikidata": "https://www.wikidata.org/wiki/Q187770"},
    {"name": "Senador Canedo", "slug": "senador-canedo-go", "state": "GO", "lat": -16.7072, "lon": -49.0931,
     "wikidata": "https://www.wikidata.org/wiki/Q1199698"},
    {"name": "Trindade", "slug": "trindade-go", "state": "GO", "lat": -16.6533, "lon": -49.4922,
     "wikidata": "https://www.wikidata.org/wiki/Q973765"},
    {"name": "Inhumas", "slug": "inhumas-go", "state": "GO", "lat": -16.3586, "lon": -49.4944,
     "wikidata": "https://www.wikidata.org/wiki/Q1004098"},
    {"name": "Itumbiara", "slug": "itumbiara-go", "state": "GO", "lat": -18.4158, "lon": -49.2158,
     "wikidata": "https://www.wikidata.org/wiki/Q734543"},
    {"name": "Caldas Novas", "slug": "caldas-novas-go", "state": "GO", "lat": -17.7444, "lon": -48.6247,
     "wikidata": "https://www.wikidata.org/wiki/Q951050"},
    {"name": "Formosa", "slug": "formosa-go", "state": "GO", "lat": -15.5353, "lon": -47.3336,
     "wikidata": "https://www.wikidata.org/wiki/Q779375"},
    {"name": "Luziânia", "slug": "luziania-go", "state": "GO", "lat": -16.2525, "lon": -47.9503,
     "wikidata": "https://www.wikidata.org/wiki/Q1009813"},
    {"name": "Valparaíso de Goiás", "slug": "valparaiso-de-goias-go", "state": "GO", "lat": -16.0781, "lon": -47.9942,
     "wikidata": "https://www.wikidata.org/wiki/Q1016614"},
    {"name": "Brasília", "slug": "brasilia-df", "state": "DF", "lat": -15.7801, "lon": -47.9292,
     "wikidata": "https://www.wikidata.org/wiki/Q2455"},
    {"name": "Uruaçu", "slug": "uruacu-go", "state": "GO", "lat": -14.5236, "lon": -49.1411,
     "wikidata": "https://www.wikidata.org/wiki/Q1195268"},
]


# ──────────────────────────────────────────────────────────────────────────────
# 1. VENDA-DE-MAQUINAS-CLARK
# ──────────────────────────────────────────────────────────────────────────────

def fix_venda_clark():
    path = os.path.join(BASE, "venda-de-maquinas-clark/index.html")
    with open(path) as f:
        html = f.read()

    if '"@graph"' in html and html.count('application/ld+json') == 1:
        print("  SKIP venda-clark (already @graph)")
        return

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    faq_block = json.loads(blocks[0])    # FAQPage
    coll_block = json.loads(blocks[1])   # CollectionPage

    base_url = "https://movemaquinas.com.br/venda-de-maquinas-clark/"
    webpage_id = "https://movemaquinas.com.br/venda-de-maquinas-clark/#webpage"
    breadcrumb_id = "https://movemaquinas.com.br/venda-de-maquinas-clark/#breadcrumb"
    faq_id = "https://movemaquinas.com.br/venda-de-maquinas-clark/#faqpage"
    itemlist_id = "https://movemaquinas.com.br/venda-de-maquinas-clark/#itemlist"

    # Fix product offers — add businessFunction Sell + proper seller @id
    item_list = coll_block["mainEntity"]
    item_list["@id"] = itemlist_id
    item_list["isPartOf"] = {"@id": webpage_id}
    item_list["about"] = {"@id": ORG_ID}
    for li in item_list.get("itemListElement", []):
        product = li.get("item", {})
        offer = product.get("offers", {})
        if isinstance(offer, dict):
            offer["businessFunction"] = "https://purl.org/goodrelations/v1#Sell"
            offer["seller"] = {"@id": ORG_ID}
            if "@type" not in offer:
                offer["@type"] = "Offer"

    # Build @graph
    graph = [
        {
            "@type": "CollectionPage",
            "@id": webpage_id,
            "url": base_url,
            "name": coll_block["name"],
            "description": coll_block["description"],
            "datePublished": coll_block.get("datePublished", "2026-03-25"),
            "dateModified": coll_block.get("dateModified", "2026-04-09"),
            "isPartOf": {"@id": WEBSITE_ID},
            "publisher": {"@id": ORG_ID},
            "speakableSpecification": {
                "@type": "SpeakableSpecification",
                "cssSelector": ["h1", "h2", ".faq__answer"]
            },
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "breadcrumb": {"@id": breadcrumb_id},
            "mainEntity": {"@id": itemlist_id},
        },
        item_list,
        {
            "@type": "BreadcrumbList",
            "@id": breadcrumb_id,
            "isPartOf": {"@id": webpage_id},
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://movemaquinas.com.br/"},
                {"@type": "ListItem", "position": 2, "name": "Venda Clark", "item": base_url}
            ]
        },
        {
            "@type": "FAQPage",
            "@id": faq_id,
            "about": {"@id": ORG_ID},
            "isPartOf": {"@id": webpage_id},
            "mainEntity": faq_block["mainEntity"]
        }
    ]

    new_schema = {"@context": "https://schema.org", "@graph": graph}
    schema_json = json.dumps(new_schema, ensure_ascii=False, separators=(",", ":"))
    new_block = f'<script type="application/ld+json">{schema_json}</script>\n'

    # Remove all existing ld+json blocks and inject single @graph
    html_clean = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', html, flags=re.DOTALL)
    html_out = html_clean.replace("</head>", new_block + "</head>", 1)

    with open(path, "w") as f:
        f.write(html_out)
    print("  OK: venda-de-maquinas-clark")


# ──────────────────────────────────────────────────────────────────────────────
# 2. CIDADES-ATENDIDAS
# ──────────────────────────────────────────────────────────────────────────────

def fix_cidades_atendidas():
    path = os.path.join(BASE, "cidades-atendidas/index.html")
    with open(path) as f:
        html = f.read()

    if '"@graph"' in html:
        print("  SKIP cidades-atendidas (already @graph)")
        return

    base_url = "https://movemaquinas.com.br/cidades-atendidas/"
    webpage_id = "https://movemaquinas.com.br/cidades-atendidas/#webpage"
    breadcrumb_id = "https://movemaquinas.com.br/cidades-atendidas/#breadcrumb"
    itemlist_id = "https://movemaquinas.com.br/cidades-atendidas/#itemlist"

    item_list_elements = []
    for i, city in enumerate(CITIES_HUBS, 1):
        item_list_elements.append({
            "@type": "ListItem",
            "position": i,
            "item": {
                "@type": "City",
                "name": city["name"],
                "sameAs": city["wikidata"],
                "url": f"https://movemaquinas.com.br/{city['slug']}/",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": city["lat"],
                    "longitude": city["lon"]
                }
            }
        })

    graph = [
        {
            "@type": "WebPage",
            "@id": webpage_id,
            "url": base_url,
            "name": "Cidades Atendidas pela Movemáquinas em GO, DF, TO e MT",
            "description": "Veja todas as cidades atendidas pela Movemáquinas. Locação de empilhadeiras, plataformas e transpaleteiras em mais de 60 cidades de GO, DF, TO e MT.",
            "isPartOf": {"@id": WEBSITE_ID},
            "publisher": {"@id": ORG_ID},
            "about": {"@id": ORG_ID},
            "speakableSpecification": {
                "@type": "SpeakableSpecification",
                "cssSelector": ["h1", "h2", ".cidades__lista"]
            },
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "breadcrumb": {"@id": breadcrumb_id},
            "mainEntity": {"@id": itemlist_id},
        },
        {
            "@type": "ItemList",
            "@id": itemlist_id,
            "name": "Cidades Atendidas pela Movemáquinas",
            "numberOfItems": len(CITIES_HUBS),
            "isPartOf": {"@id": WEBSITE_ID},
            "about": {"@id": ORG_ID},
            "itemListElement": item_list_elements
        },
        {
            "@type": "BreadcrumbList",
            "@id": breadcrumb_id,
            "isPartOf": {"@id": webpage_id},
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://movemaquinas.com.br/"},
                {"@type": "ListItem", "position": 2, "name": "Cidades Atendidas", "item": base_url}
            ]
        }
    ]

    new_schema = {"@context": "https://schema.org", "@graph": graph}
    schema_json = json.dumps(new_schema, ensure_ascii=False, separators=(",", ":"))
    new_block = f'<script type="application/ld+json">{schema_json}</script>\n'

    html_clean = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', html, flags=re.DOTALL)
    html_out = html_clean.replace("</head>", new_block + "</head>", 1)

    with open(path, "w") as f:
        f.write(html_out)
    print("  OK: cidades-atendidas")


# ──────────────────────────────────────────────────────────────────────────────
# 3. BLOG ARTIGOS — unify N isolated blocks into @graph
# ──────────────────────────────────────────────────────────────────────────────

def fix_blog_article(slug):
    path = os.path.join(BASE, f"blog/{slug}/index.html")
    if not os.path.exists(path):
        print(f"  SKIP {slug} (not found)")
        return

    with open(path) as f:
        html = f.read()

    if '"@graph"' in html:
        print(f"  SKIP {slug} (already @graph)")
        return

    meta = BLOG_META[slug]
    base_url = f"https://movemaquinas.com.br/blog/{slug}/"
    article_id = f"https://movemaquinas.com.br/blog/{slug}/#article"
    webpage_id = f"https://movemaquinas.com.br/blog/{slug}/#webpage"
    breadcrumb_id = f"https://movemaquinas.com.br/blog/{slug}/#breadcrumb"
    faq_id = f"https://movemaquinas.com.br/blog/{slug}/#faqpage"

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    parsed = [json.loads(b) for b in blocks]

    # Extract existing nodes
    breadcrumb_node = next((p for p in parsed if p.get("@type") == "BreadcrumbList"), None)
    faq_node = next((p for p in parsed if p.get("@type") == "FAQPage"), None)
    article_node = next((p for p in parsed if p.get("@type") in ("Article", "BlogPosting")), None)

    # Extract og:image if exists in html
    og_img_match = re.search(r'og:image.*?content="([^"]+)"', html)
    image_url = og_img_match.group(1) if og_img_match else "https://movemaquinas.com.br/assets/og-move-maquinas.jpg"

    # Build unified @graph nodes

    # WebPage node
    webpage = {
        "@type": "WebPage",
        "@id": webpage_id,
        "url": base_url,
        "name": meta["headline"],
        "description": meta["description"],
        "isPartOf": {"@id": WEBSITE_ID},
        "publisher": {"@id": ORG_ID},
        "datePublished": meta["datePublished"],
        "dateModified": meta["dateModified"],
        "speakableSpecification": {
            "@type": "SpeakableSpecification",
            "cssSelector": ["h1", "h2", ".intro", ".faq__answer"]
        },
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "breadcrumb": {"@id": breadcrumb_id},
        "mainEntity": {"@id": article_id},
    }

    # Article/BlogPosting node
    article = {
        "@type": "BlogPosting",
        "@id": article_id,
        "headline": meta["headline"],
        "description": meta["description"],
        "keywords": meta["keywords"],
        "articleSection": meta["articleSection"],
        "wordCount": meta["wordCount"],
        "datePublished": meta["datePublished"],
        "dateModified": meta["dateModified"],
        "url": base_url,
        "mainEntityOfPage": {"@id": webpage_id},
        "image": {
            "@type": "ImageObject",
            "url": image_url,
            "width": 1200,
            "height": 630
        },
        "author": {"@id": PERSON_ID},
        "publisher": {"@id": ORG_ID},
        "isPartOf": {"@id": f"https://movemaquinas.com.br/blog/#blog"},
    }

    # Person node (compact reference)
    person = {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": "Márcio Rocha",
        "givenName": "Márcio",
        "familyName": "Rocha",
        "jobTitle": "Diretor Comercial",
        "worksFor": {"@id": ORG_ID},
        "knowsAbout": [
            {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q187959", "name": "Empilhadeira"},
            {"@type": "DefinedTerm", "@id": "https://www.wikidata.org/wiki/Q1142888", "name": "Plataforma Elevatória"},
        ]
    }

    # BreadcrumbList
    if breadcrumb_node:
        breadcrumb_node["@id"] = breadcrumb_id
        breadcrumb_node["isPartOf"] = {"@id": webpage_id}
    else:
        breadcrumb_node = {
            "@type": "BreadcrumbList",
            "@id": breadcrumb_id,
            "isPartOf": {"@id": webpage_id},
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://movemaquinas.com.br/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://movemaquinas.com.br/blog/"},
                {"@type": "ListItem", "position": 3, "name": meta["headline"], "item": base_url}
            ]
        }

    # FAQPage
    if faq_node:
        faq_node["@id"] = faq_id
        faq_node["isPartOf"] = {"@id": webpage_id}
        faq_node["about"] = {"@id": ORG_ID}
    else:
        faq_node = None

    graph = [webpage, article, person, breadcrumb_node]
    if faq_node:
        graph.append(faq_node)

    new_schema = {"@context": "https://schema.org", "@graph": graph}
    schema_json = json.dumps(new_schema, ensure_ascii=False, separators=(",", ":"))
    new_block = f'<script type="application/ld+json">{schema_json}</script>\n'

    # Fix canonical to absolute if relative
    html = re.sub(
        r'(<link rel="canonical" href=")(/blog/' + slug + r'/?)(")',
        r'\1https://movemaquinas.com.br/blog/' + slug + r'/\3',
        html
    )

    # Add og:image if missing
    if 'og:image' not in html:
        og_block = f'<meta property="og:image" content="{image_url}">\n'
        html = html.replace("</head>", og_block + "</head>", 1)

    html_clean = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', html, flags=re.DOTALL)
    html_out = html_clean.replace("</head>", new_block + "</head>", 1)

    with open(path, "w") as f:
        f.write(html_out)
    print(f"  OK: blog/{slug}")


# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Schema Fase 2 — Move Máquinas ===\n")

    print("1. Venda Clark:")
    fix_venda_clark()

    print("\n2. Cidades Atendidas:")
    fix_cidades_atendidas()

    print("\n3. Blog Artigos:")
    for slug in BLOG_META:
        fix_blog_article(slug)

    print("\nFase 2 concluída.")
