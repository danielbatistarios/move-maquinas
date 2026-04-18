#!/usr/bin/env python3
"""
template-builder.py — Gera LPs a partir dos HTML de referência de Goiânia.
Mantém layout/CSS/JS/SVGs intactos, substitui apenas conteúdo textual por seção.

Uso:
  python3 template-builder.py senador-canedo-go articulada
  python3 template-builder.py senador-canedo-go --all
  python3 template-builder.py --batch          # todas as pendentes
"""

import os, sys, re, json, urllib.parse, time, datetime
from bs4 import BeautifulSoup, NavigableString, Comment
from importlib.machinery import SourceFileLoader

DIR = os.path.dirname(os.path.abspath(__file__))

# ── Import lp-builder content functions + city loader ──
lb = SourceFileLoader('lp_builder', os.path.join(DIR, 'lp-builder.py')).load_module()
load_city = lb.load_city
SLUGS = lb.SLUGS
WA_NUM = lb.WA_NUM
TEL = lb.TEL
TEL_LINK = lb.TEL_LINK

CONTENT_FUNCS = {
    'articulada': lb.content_articulada,
    'tesoura': lb.content_tesoura,
    'combustao': lb.content_combustao,
    'transpaleteira': lb.content_transpaleteira,
    'curso': lb.content_curso,
}

REFS = {
    'articulada': os.path.join(DIR, 'ref-goiania-articulada.html'),
    'tesoura': os.path.expanduser('~/ref-goiania-tesoura.html'),
    'combustao': os.path.expanduser('~/ref-goiania-combustao.html'),
    'transpaleteira': os.path.expanduser('~/ref-goiania-transpaleteira.html'),
    'curso': os.path.expanduser('~/ref-goiania-curso.html'),
}

BASE_URL = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'
SITE_URL = 'https://movemaquinas.com.br'

# Cidades da cobertura (para seção de cobertura/cross-links)
COVERAGE_CITIES = [
    ('goiania-go', 'Goiânia'),
    ('aparecida-de-goiania-go', 'Aparecida de Goiânia'),
    ('senador-canedo-go', 'Senador Canedo'),
    ('trindade-go', 'Trindade'),
    ('anapolis-go', 'Anápolis'),
    ('inhumas-go', 'Inhumas'),
    ('brasilia-df', 'Brasília'),
    ('formosa-go', 'Formosa'),
    ('luziania-go', 'Luziânia'),
    ('itumbiara-go', 'Itumbiara'),
    ('caldas-novas-go', 'Caldas Novas'),
    ('uruacu-go', 'Uruaçu'),
    ('valparaiso-de-goias-go', 'Valparaíso de Goiás'),
]


def wa_url(city_name, service_text):
    """Build WhatsApp URL with proper encoding."""
    msg = f'Olá, quero orçamento de {service_text} em {city_name}'
    return f'https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}'


def state_name(state_code):
    return {'GO': 'Goiás', 'DF': 'Distrito Federal', 'TO': 'Tocantins', 'MT': 'Mato Grosso'}.get(state_code, state_code)


# ═══════════════════════════════════════════════════════════════
# SECTION REPLACERS
# Each function modifies the soup in-place for a specific section
# ═══════════════════════════════════════════════════════════════

def set_inner_html(element, html_str):
    """Clear an element and set its inner HTML, preserving <br>, <em>, <span> etc."""
    element.clear()
    wrapper = BeautifulSoup(f'<div>{html_str}</div>', 'html.parser').div
    for child in list(wrapper.children):
        element.append(child.extract())


def replace_head(soup, c, content, svc_slug):
    """Replace <head> meta tags and schema JSON-LD."""
    # Title
    soup.title.string = content['title']

    # Meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        meta_desc['content'] = content['desc']

    # Canonical
    link_can = soup.find('link', rel='canonical')
    if link_can:
        link_can['href'] = f'{SITE_URL}/{c["slug"]}/{svc_slug}'

    # OG tags
    for prop, val in [('og:title', content['title']),
                      ('og:description', content.get('og', content['desc']))]:
        tag = soup.find('meta', property=prop)
        if tag:
            tag['content'] = val

    # Geo tags
    geo_region = soup.find('meta', attrs={'name': 'geo.region'})
    if geo_region:
        geo_region['content'] = f'BR-{c["state"]}'

    geo_place = soup.find('meta', attrs={'name': 'geo.placename'})
    if geo_place:
        geo_place['content'] = f'{c["name"]}, {state_name(c["state"])}, Brasil'

    geo_pos = soup.find('meta', attrs={'name': 'geo.position'})
    if geo_pos:
        geo_pos['content'] = f'{c["lat"]};{c["lng"]}'

    icbm = soup.find('meta', attrs={'name': 'ICBM'})
    if icbm:
        icbm['content'] = f'{c["lat"]}, {c["lng"]}'

    # Schema JSON-LD — rebuild entirely
    schema_tag = soup.find('script', type='application/ld+json')
    if schema_tag:
        schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": ["LocalBusiness", "AutomotiveBusiness"],
                    "@id": f"{SITE_URL}/#organization",
                    "name": "Move Máquinas",
                    "url": SITE_URL,
                    "telephone": "+55-62-3211-1515",
                    "taxID": "32.428.258/0001-80",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "Av. Eurico Viana, 4913 - Qd 5 B Lt 04",
                        "addressLocality": "Goiânia",
                        "addressRegion": "GO",
                        "postalCode": "74593-590",
                        "addressCountry": "BR"
                    },
                    "geo": {"@type": "GeoCoordinates", "latitude": float(c['lat']), "longitude": float(c['lng'])},
                    "hasMap": "https://share.google/08G0ATrziYm9nDlKf",
                    "serviceArea": {
                        "@type": "GeoCircle",
                        "geoMidpoint": {"@type": "GeoCoordinates", "latitude": float(c['lat']), "longitude": float(c['lng'])},
                        "geoRadius": "200000"
                    },
                    "areaServed": [
                        {"@type": "State", "name": "Goiás"},
                        {"@type": "State", "name": "Distrito Federal"},
                        {"@type": "State", "name": "Tocantins"},
                        {"@type": "State", "name": "Mato Grosso"}
                    ],
                    "sameAs": [
                        "https://www.instagram.com/move.maquinas/",
                        "https://www.linkedin.com/company/move-maquinas-oficial/",
                        "https://www.youtube.com/@movemaquinas/featured"
                    ]
                },
                {
                    "@type": "Service",
                    "name": content['title'].replace(' | Move Máquinas', ''),
                    "serviceType": content['service_type'],
                    "provider": {"@id": f"{SITE_URL}/#organization"},
                    "areaServed": {"@type": "City", "name": c['name'], "addressRegion": c['state']},
                    "offers": {
                        "@type": "Offer",
                        "priceRange": content['price_range'],
                        "priceCurrency": "BRL",
                        "availability": "https://schema.org/InStock"
                    }
                },
                {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Move Máquinas", "item": SITE_URL},
                        {"@type": "ListItem", "position": 2, "name": f"Equipamentos em {c['name']}", "item": f"{SITE_URL}/{c['slug']}/"},
                        {"@type": "ListItem", "position": 3, "name": content['breadcrumb'], "item": f"{SITE_URL}/{c['slug']}/{svc_slug}"}
                    ]
                },
                {
                    "@type": "FAQPage",
                    "mainEntity": [
                        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                        for q, a in content['faqs']
                    ]
                }
            ]
        }
        schema_tag.string = '\n' + json.dumps(schema, ensure_ascii=False, indent=2) + '\n'


def replace_breadcrumb(soup, c, content):
    """Replace breadcrumb links and text."""
    bc = soup.find('header', class_='breadcrumb')
    if not bc:
        return
    links = bc.find_all('a')
    for a in links:
        href = a.get('href', '')
        if '/goiania-go/' in href or (href.endswith('/') and 'goiania' in href):
            a['href'] = f'/{c["slug"]}/'
            a.string = f'Equipamentos em {c["name"]}'
    # Last li (current page)
    span = bc.find('span', attrs={'aria-current': 'page'})
    if span:
        span.string = content['breadcrumb']


def replace_hero(soup, c, content, svc_slug):
    """Replace hero section: h1, lead, badge, WhatsApp URL."""
    hero = soup.find('section', class_='hero')
    if not hero:
        return

    # H1
    h1 = hero.find('h1')
    if h1:
        set_inner_html(h1, content['h1'])

    # Hero lead
    lead = hero.find('p', class_='hero__lead')
    if lead:
        lead.string = content['hero_sub']

    # WhatsApp links
    wa = wa_url(c['name'], content['wa_subject'])
    for a in hero.find_all('a', class_='btn--wa'):
        a['href'] = wa
    for a in hero.find_all('a', class_='btn--outline-white'):
        if 'tel:' in a.get('href', ''):
            a['href'] = 'tel:+556232111515'


def replace_trust_bar(soup, c, content):
    """Replace trust bar badge text."""
    trust = soup.find('div', class_='trust-bar')
    if not trust:
        return
    badges = content.get('trust_badges', None)
    if not badges:
        return
    badge_els = trust.find_all('div', class_='trust-badge')
    for i, badge_el in enumerate(badge_els):
        if i < len(badges):
            text_div = badge_el.find('div', class_='trust-badge__text')
            if text_div and isinstance(badges[i], dict):
                strong = text_div.find('strong')
                span = text_div.find('span')
                if strong:
                    strong.string = badges[i].get('strong', '')
                if span:
                    span.string = badges[i].get('span', '')


def replace_stats_bar(soup, c):
    """Replace marquee stats bar."""
    stats = soup.find('div', class_='stats-bar')
    if not stats:
        return
    # Keep the existing structure — just update city reference in span text
    for span in stats.find_all('span'):
        text = span.get_text()
        if 'Goiânia' in text:
            span.string = text.replace('Goiânia', c['name'])


def replace_oque(soup, c, content):
    """Replace 'O que é' section: h2, paragraphs, h3s, checklist."""
    section = soup.find('section', attrs={'aria-labelledby': 'oque-h2'})
    if not section:
        return

    # H2
    h2 = section.find('h2', id='oque-h2')
    if h2:
        set_inner_html(h2, content['h2s'][0])

    # Main paragraph (first <p> after h2, before expandable)
    first_p = h2.find_next_sibling('p') if h2 else None
    if first_p:
        first_p.string = content['oque']

    # Expandable content: h3s and their paragraphs
    expandable = section.find('div', class_='expandable')
    if expandable and content.get('h3s'):
        h3_els = expandable.find_all('h3')
        for i, h3_el in enumerate(h3_els):
            if i < len(content['h3s']):
                h3_el.string = content['h3s'][i][0]
                # Next sibling <p>
                p = h3_el.find_next_sibling('p')
                if p:
                    p.string = content['h3s'][i][1]

    # Checklist items
    if content.get('checklist'):
        items = section.find_all('li', class_='whatitis__list-item')
        for i, li in enumerate(items):
            if i < len(content['checklist']):
                div = li.find('div')
                if div:
                    set_inner_html(div, content['checklist'][i])

    # Expand button text
    btn = section.find('button', class_='expand-btn')
    if btn:
        # Keep the SVG, replace text
        svg = btn.find('svg')
        btn.clear()
        btn.append(NavigableString(f'Ver mais sobre {content.get("equip_short", "o equipamento")} '))
        if svg:
            btn.append(svg)


def replace_expert(soup, c, content):
    """Replace expert quote text."""
    section = soup.find('section', class_='expert-quote')
    if not section:
        return
    quote = section.find('blockquote', class_='expert-quote__text')
    if quote and content.get('expert'):
        quote.string = f'"{content["expert"]}"'


def replace_compare(soup, c, content, svc_slug):
    """Replace comparison section."""
    section = soup.find('section', attrs={'aria-labelledby': 'compare-h2'})
    if not section:
        return
    comp = content.get('compare')
    if not comp:
        return

    # H2
    h2 = section.find('h2', id='compare-h2')
    if h2 and len(content['h2s']) > 4:
        set_inner_html(h2, content['h2s'][4])

    # Intro paragraph
    intro = section.find('p', class_='compare__intro')
    if intro:
        intro.string = comp.get('intro', '')

    # Compare cards
    cards = section.find_all('div', class_='compare__card')
    if len(cards) >= 2:
        # Main equipment card
        h3_main = cards[0].find('h3')
        if h3_main:
            h3_main.string = comp.get('equip_desc', h3_main.get_text())
        p_main = cards[0].find('p')
        if p_main:
            p_main.string = comp.get('equip_desc', '')
        # Pros/cons
        lis_main = cards[0].find_all('li')
        all_items = comp.get('equip_pros', []) + comp.get('equip_cons', [])
        for i, li in enumerate(lis_main):
            if i < len(all_items):
                # Keep the SVG icon
                svg = li.find('svg')
                li.clear()
                if svg:
                    li.append(svg)
                li.append(NavigableString(f' {all_items[i]}'))

        # Alt equipment card
        h3_alt = cards[1].find('h3')
        if h3_alt:
            h3_alt.string = comp.get('alt_desc', h3_alt.get_text())
        p_alt = cards[1].find('p')
        if p_alt:
            p_alt.string = comp.get('alt_desc', '')
        lis_alt = cards[1].find_all('li')
        alt_items = comp.get('alt_pros', []) + comp.get('alt_cons', [])
        for i, li in enumerate(lis_alt):
            if i < len(alt_items):
                svg = li.find('svg')
                li.clear()
                if svg:
                    li.append(svg)
                li.append(NavigableString(f' {alt_items[i]}'))

    # Verdict
    verdict = section.find('div', class_='compare__verdict')
    if verdict and comp.get('verdict'):
        p_verdict = verdict.find('p')
        if p_verdict:
            set_inner_html(p_verdict, f'<strong>Regra prática para {c["name"]}:</strong> {comp["verdict"]}')

    # Cross-links and "Outros equipamentos" text
    if verdict:
        for p_tag in verdict.find_all('p'):
            text = p_tag.get_text()
            if 'Outros equipamentos' in text and 'Goiânia' in text:
                p_tag.string = text.replace('Goiânia', c['name'])
        for a in verdict.find_all('a'):
            href = a.get('href', '')
            if '/goiania-go/' in href:
                new_href = href.replace('/goiania-go/', f'/{c["slug"]}/')
                a['href'] = new_href
                text = a.get_text()
                if 'Goiânia' in text:
                    a.string = text.replace('Goiânia', c['name'])


def replace_price(soup, c, content):
    """Replace pricing section."""
    section = soup.find('section', attrs={'aria-labelledby': 'preco-h2'})
    if not section:
        return
    price = content.get('price')
    if not price:
        return

    # H2
    h2 = section.find('h2', id='preco-h2')
    if h2:
        # Find the H2 for pricing in content h2s (usually index 5 or 6)
        for h2_text in content['h2s']:
            if 'custa' in h2_text.lower() or 'preço' in h2_text.lower() or 'valor' in h2_text.lower():
                set_inner_html(h2, h2_text)
                break

    # Subtitle
    subtitle = section.find('p', class_='section-subtitle')
    if subtitle:
        subtitle.string = f'Valores de referência para locação em {c["name"]}. O preço final depende do modelo, prazo e condições do contrato.'

    # Price cards
    cards_data = price.get('cards', [])
    card_els = section.find_all('div', class_='price__card')
    for i, card_el in enumerate(card_els):
        if i >= len(cards_data):
            break
        cd = cards_data[i]
        label = card_el.find('div', class_='price__card-label')
        if label:
            label.string = cd.get('name', '') + (f' ({cd.get("sub", "")})' if cd.get('sub') else '')
        value = card_el.find('div', class_='price__card-value')
        if value:
            value.string = f'R${cd.get("price", "")}'
        items = card_el.find_all('li')
        cd_items = cd.get('items', [])
        for j, li in enumerate(items):
            if j < len(cd_items):
                svg = li.find('svg')
                li.clear()
                if svg:
                    li.append(svg)
                li.append(NavigableString(f' {cd_items[j]}'))

    # Price note
    note = section.find('div', class_='price__note')
    if note and price.get('note'):
        note.string = price['note']

    # WhatsApp button
    for a in section.find_all('a', class_='btn--wa'):
        a['href'] = wa_url(c['name'], content['wa_subject'])


def replace_apps(soup, c, content):
    """Replace applications section."""
    section = soup.find('section', attrs={'aria-labelledby': 'apps-h2'})
    if not section:
        return

    # Section tag text
    tag = section.find('span', class_='section-tag')
    if tag:
        svg = tag.find('svg')
        tag.clear()
        if svg:
            tag.append(svg)
        tag.append(NavigableString(f'\n      Aplicações em {c["name"]}\n    '))

    # H2
    h2 = section.find('h2', id='apps-h2')
    if h2:
        for h2_text in content['h2s']:
            if 'aplicaç' in h2_text.lower() or 'onde' in h2_text.lower():
                set_inner_html(h2, h2_text)
                break

    # Subtitle
    subtitle = section.find('p', class_='section-subtitle')
    if subtitle:
        subtitle.string = f'Onde o equipamento opera diariamente em {c["name"]} e região.'

    # App cards
    apps = content.get('apps', [])
    card_els = section.find_all('article', class_='apps__card')
    for i, card_el in enumerate(card_els):
        if i >= len(apps):
            break
        title, text, img_url, img_alt = apps[i]
        h3 = card_el.find('h3')
        if h3:
            h3.string = title
        p = card_el.find('p')
        if p:
            p.string = text
        img = card_el.find('img')
        if img and img_url:
            img['src'] = img_url
            img['alt'] = img_alt


def replace_incluso(soup, c, content):
    """Replace 'what's included' section."""
    section = soup.find('section', attrs={'aria-labelledby': 'incluso-h2'})
    if not section:
        return

    # H2
    h2 = section.find('h2', id='incluso-h2')
    if h2:
        for h2_text in content['h2s']:
            if 'inclus' in h2_text.lower() or 'inclui' in h2_text.lower():
                set_inner_html(h2, h2_text)
                break

    # Subtitle
    subtitle = section.find('p', class_='section-subtitle')
    if subtitle and content.get('incluso_sub'):
        subtitle.string = content['incluso_sub']

    # Incluso items
    items_data = content.get('incluso_items', [])
    item_els = section.find_all('li', class_='incluso__item')
    for i, item_el in enumerate(item_els):
        if i >= len(items_data):
            break
        svg_path, title, desc = items_data[i]
        body = item_el.find('div', class_='incluso__body')
        if body:
            strong = body.find('strong')
            if strong:
                strong.string = title
            p = body.find('p')
            if p:
                p.string = desc


def replace_testimonials(soup, c, content):
    """Replace testimonials section."""
    section = soup.find('section', class_='testimonials')
    if not section:
        return

    # H2
    h2 = section.find('h2', id='depo-h2')
    if h2:
        for h2_text in content['h2s']:
            if 'cliente' in h2_text.lower() or 'depoimento' in h2_text.lower():
                set_inner_html(h2, h2_text)
                break

    # Testimonial cards
    tests = content.get('tests', [])
    cards = section.find_all('article', class_='testimonial')
    for i, card in enumerate(cards):
        if i >= len(tests):
            break
        quote_text, name, role = tests[i]
        p = card.find('p', class_='testimonial__text')
        if p:
            p.string = f'"{quote_text}"'
        author = card.find('div', class_='testimonial__author')
        if author:
            strong = author.find('strong')
            if strong:
                strong.string = name
            # Replace the text node after <strong>
            for child in author.children:
                if isinstance(child, NavigableString) and child.strip():
                    child.replace_with(NavigableString(f'\n          {role}\n        '))
                    break


def replace_nr(soup, c, content, svc_slug):
    """Replace NR section."""
    # Find by id pattern (nr35-h2 or nr11-h2)
    nr_section = None
    for sid in ['nr35-h2', 'nr11-h2']:
        h2 = soup.find('h2', id=sid)
        if h2:
            nr_section = h2.find_parent('section')
            break
    if not nr_section:
        return

    nr = content.get('nr', {})
    norma = nr.get('norma', 'NR-35')

    # H2
    h2_el = nr_section.find('h2')
    if h2_el:
        for h2_text in content['h2s']:
            if 'nr-' in h2_text.lower() or 'norma' in h2_text.lower() or 'conform' in h2_text.lower():
                set_inner_html(h2_el, h2_text)
                break

    # Subtitle
    subtitle = nr_section.find('p', class_='section-subtitle')
    if subtitle and nr.get('intro'):
        subtitle.string = nr['intro']

    # Link to curso
    for a in nr_section.find_all('a'):
        href = a.get('href', '')
        if '/goiania-go/' in href:
            a['href'] = href.replace('/goiania-go/', f'/{c["slug"]}/')
            text = a.get_text()
            if 'Goiânia' in text:
                a.string = text.replace('Goiânia', c['name'])


def replace_cobertura(soup, c, content, svc_slug):
    """Replace coverage section: cities, map, links."""
    section = soup.find('section', attrs={'aria-labelledby': 'cobertura-h2'})
    if not section:
        return

    # H2
    h2 = section.find('h2', id='cobertura-h2')
    if h2:
        set_inner_html(h2, f'Entrega rápida em <span>{c["name"]}</span> e região')

    # Description paragraph
    ps = section.find_all('p', recursive=False)
    for p_tag in section.find_all('p'):
        text = p_tag.get_text()
        if 'Base localizada' in text or 'Entrega' in text and len(text) > 100:
            p_tag.string = f'Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega {c["delivery"]} em {c["name"]} ({c["dist"]}km via {c["rod"]}). Atendemos toda a região e cidades em um raio de até 200 km.'
            break

    # Coverage cities — rebuild
    coverage_div = section.find('div', class_='coverage__cities')
    if coverage_div:
        coverage_div.clear()
        coverage_div['class'] = ['coverage__cities', 'reveal']
        svg_check = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
        for slug, name in COVERAGE_CITIES:
            city_div = soup.new_tag('div', **{'class': 'coverage__city'})
            city_div.append(BeautifulSoup(svg_check, 'html.parser'))
            if slug == c['slug']:
                # Current city — no link, just text
                city_div.append(NavigableString(f'\n        {name}\n      '))
            else:
                a = soup.new_tag('a', href=f'/{slug}/')
                a.string = name
                city_div.append(a)
            coverage_div.append(city_div)

    # Maps embed — update with city coords
    iframe = section.find('iframe')
    if iframe:
        iframe['src'] = f'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3821.8!2d{c["lng"]}!3d{c["lat"]}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2z{c["lat"]}!5e0!3m2!1spt-BR!2sbr!4v1'
        iframe['title'] = f'Localização Move Máquinas - atendimento em {c["name"]}'

    # "Veja também" links — only target links OUTSIDE the coverage__cities div
    coverage_div = section.find('div', class_='coverage__cities')
    for a in section.find_all('a'):
        # Skip links inside the coverage cities div (those are intentional)
        if coverage_div and a.find_parent('div', class_='coverage__cities'):
            continue
        href = a.get('href', '')
        if '/goiania-go/' in href:
            a['href'] = href.replace('/goiania-go/', f'/{c["slug"]}/')
            text = a.get_text()
            if 'Goiânia' in text:
                a.string = text.replace('Goiânia', c['name'])


def replace_faq(soup, c, content):
    """Replace FAQ section with unique questions/answers."""
    section = soup.find('section', id='faq')
    if not section:
        return

    # H2
    h2 = section.find('h2', id='faq-h2')
    if h2:
        faq_h2_text = None
        for h2_text in content['h2s']:
            if 'pergunta' in h2_text.lower() or 'faq' in h2_text.lower() or 'dúvida' in h2_text.lower():
                faq_h2_text = h2_text
                break
        # Fallback: use last h2 or generate one
        if not faq_h2_text:
            equip = content.get('equip_short', 'equipamento')
            faq_h2_text = f'Perguntas frequentes sobre <span>locação de {equip}</span> em {c["name"]}'
        set_inner_html(h2, faq_h2_text)

    # FAQ items
    faqs = content.get('faqs', [])
    faq_list = section.find('div', class_='faq__list')
    if not faq_list:
        return

    # Rebuild FAQ items from scratch using the structure of the first item as template
    details_els = faq_list.find_all('details', class_='faq__item')
    if not details_els:
        return

    # Use first details as template structure
    template_html = str(details_els[0])

    # Clear and rebuild
    faq_list.clear()
    for i, (question, answer) in enumerate(faqs):
        faq_html = f'''<details class="faq__item reveal reveal-stagger" style="--stagger:{i}" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <summary class="faq__trigger">
          <h3 itemprop="name" style="font-size:inherit;font-weight:inherit;margin:0;color:inherit;line-height:inherit;">{question}</h3>
          <svg class="faq__icon" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
        </summary>
        <div class="faq__answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <div itemprop="text">{answer}</div>
        </div>
      </details>'''
        faq_list.append(BeautifulSoup(faq_html, 'html.parser'))


def replace_footer_cta(soup, c, content):
    """Replace footer CTA section."""
    footer = soup.find('footer', class_='cta-final')
    if not footer:
        return
    h3 = footer.find('h3')
    if h3 and content.get('cta'):
        h3.string = content['cta']
    sub = footer.find('p', class_='cta-final__sub')
    if sub:
        sub.string = f'Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega para {c["name"]} em minutos.'
    # WhatsApp
    for a in footer.find_all('a', class_='btn--wa'):
        a['href'] = wa_url(c['name'], content['wa_subject'])
    # Address
    addr = footer.find('address')
    if addr:
        addr.string = f'Move Máquinas · Av. Eurico Viana, 4913, Parque das Flores, Goiânia - GO · CNPJ 32.428.258/0001-80'


def replace_sticky_and_float(soup, c, content):
    """Replace sticky CTA and floating WhatsApp button."""
    # Sticky CTA
    sticky = soup.find('div', class_='sticky-cta')
    if sticky:
        prod = sticky.find('span', class_='sticky-cta__product')
        if prod:
            prod.string = content.get('equip_short', '').title()
        price = sticky.find('span', class_='sticky-cta__price')
        if price:
            price.string = f'a partir de {content["price_range"].split(" - ")[0]}/mês'
        for a in sticky.find_all('a'):
            a['href'] = wa_url(c['name'], content['wa_subject'])

    # Float WA
    float_wa = soup.find('a', class_='float-wa')
    if float_wa:
        float_wa['href'] = wa_url(c['name'], content['wa_subject'])


def replace_forms(soup, c, content):
    """Replace cotação rápida and mobile form sections."""
    # Cotação rápida h3
    cota_h3 = soup.find('h3', id='cota-h2')
    if cota_h3:
        equip = content.get('equip_short', 'equipamento')
        set_inner_html(cota_h3, f'Solicite orçamento de <span style="color:var(--color-primary);">{equip}</span> em {c["name"]}')

    # Update "Entrega no mesmo dia em Goiânia" in form section
    for li in soup.find_all('li'):
        text = li.get_text()
        if 'Entrega no mesmo dia em Goiânia' in text:
            svg = li.find('svg')
            li.clear()
            if svg:
                li.append(svg)
            li.append(NavigableString(f' Entrega {c["delivery"]} em {c["name"]}'))

    # City select: pre-select current city
    for select in soup.find_all('select', {'name': 'cidade'}):
        # Add current city as first option if not present
        options = select.find_all('option')
        city_found = False
        for opt in options:
            if opt.get('value') == c['name']:
                opt['selected'] = ''
                city_found = True
            elif 'selected' in opt.attrs:
                del opt['selected']
        if not city_found:
            new_opt = soup.new_tag('option', value=c['name'], selected='')
            new_opt.string = c['name']
            select.insert(0, new_opt)


def replace_video_section(soup, c):
    """Replace video section alt text."""
    video_section = soup.find('section', attrs={'aria-labelledby': 'video-h2'})
    if not video_section:
        return
    for img in video_section.find_all('img'):
        alt = img.get('alt', '')
        if 'Goiânia' in alt:
            img['alt'] = alt.replace('Goiânia', c['name'])


def replace_js_wa(html_str, c, content):
    """Replace WhatsApp city in JS form handler."""
    html_str = html_str.replace(
        "plataforma articulada em Goiânia",
        f"{content.get('wa_subject', 'equipamento')} em {c['name']}"
    )
    html_str = html_str.replace(
        "plataforma elevatória tesoura em Goiânia",
        f"{content.get('wa_subject', 'equipamento')} em {c['name']}"
    )
    html_str = html_str.replace(
        "empilhadeira a combustão em Goiânia",
        f"{content.get('wa_subject', 'equipamento')} em {c['name']}"
    )
    html_str = html_str.replace(
        "transpaleteira em Goiânia",
        f"{content.get('wa_subject', 'equipamento')} em {c['name']}"
    )
    html_str = html_str.replace(
        "curso de operador em Goiânia",
        f"{content.get('wa_subject', 'equipamento')} em {c['name']}"
    )
    return html_str


def fix_curso_slug(html_str):
    """Fix old curso slug to match SLUGS dict."""
    html_str = html_str.replace(
        '/curso-operador-empilhadeira',
        '/curso-de-operador-de-empilhadeira'
    )
    return html_str


def safe_replace_urls(html_str, c, svc_slug):
    """Final pass: targeted replacements only. Does NOT do blanket goiania-go replace."""
    # Fix curso slug (reference uses old short slug)
    html_str = fix_curso_slug(html_str)

    # Replace encoded Goiânia in WhatsApp URLs only
    html_str = html_str.replace(
        'Goi%C3%A2nia',
        urllib.parse.quote(c['name'])
    )

    return html_str


# ═══════════════════════════════════════════════════════════════
# FLEET CAROUSEL — more complex, keep structure, update text
# ═══════════════════════════════════════════════════════════════

def replace_fleet(soup, c, content):
    """Replace fleet carousel model descriptions (keep SVG illustrations)."""
    section = soup.find('section', attrs={'aria-labelledby': 'specs-h2'})
    if not section:
        return

    # H2
    h2 = section.find('h2', id='specs-h2')
    if h2:
        for h2_text in content['h2s']:
            if 'modelo' in h2_text.lower() or 'frota' in h2_text.lower() or 'equipamento' in h2_text.lower():
                set_inner_html(h2, h2_text)
                break

    # Fleet models — update text in slides
    models = content.get('fleet_models', [])
    slides = section.find_all('div', class_='fleet-slide')
    if not slides:
        # Try alternative class names
        slides = section.find_all('div', class_='fleet__slide')

    # Also try finding by comment markers
    if not slides:
        # Slides might not have a specific class, look for h3s within the carousel
        carousel = section.find('div', class_='fleet-carousel') or section.find('div', class_='fleet__carousel')
        if carousel:
            slide_h3s = carousel.find_all('h3')
            for i, h3 in enumerate(slide_h3s):
                if i < len(models):
                    m = models[i]
                    h3.string = m.get('name', h3.get_text())
                    # Find subtitle and desc near the h3
                    parent = h3.parent
                    if parent:
                        ps = parent.find_all('p')
                        if len(ps) >= 1 and m.get('subtitle'):
                            ps[0].string = m['subtitle']
                        if len(ps) >= 2 and m.get('desc'):
                            ps[1].string = m['desc']


# ═══════════════════════════════════════════════════════════════
# MAIN BUILDER
# ═══════════════════════════════════════════════════════════════

def build_lp(city_slug, service):
    """Build an LP for a city+service by modifying the reference HTML."""
    ref_file = REFS[service]
    if not os.path.exists(ref_file):
        print(f'  [ERRO] Referência não encontrada: {ref_file}')
        return None

    # Load reference HTML
    with open(ref_file, 'r', encoding='utf-8') as f:
        ref_html = f.read()

    # Load city data and generate content
    c = load_city(city_slug)
    content_func = CONTENT_FUNCS[service]
    content = content_func(c)
    svc_slug = SLUGS[service]

    print(f'  Gerando: {c["name"]} × {service}')

    # Parse HTML
    soup = BeautifulSoup(ref_html, 'html.parser')

    # Apply replacements section by section
    replace_head(soup, c, content, svc_slug)
    replace_breadcrumb(soup, c, content)
    replace_hero(soup, c, content, svc_slug)
    replace_trust_bar(soup, c, content)
    replace_stats_bar(soup, c)
    replace_oque(soup, c, content)
    replace_fleet(soup, c, content)
    replace_expert(soup, c, content)
    replace_compare(soup, c, content, svc_slug)
    replace_forms(soup, c, content)
    replace_video_section(soup, c)
    replace_price(soup, c, content)
    replace_apps(soup, c, content)
    replace_incluso(soup, c, content)
    replace_testimonials(soup, c, content)
    replace_nr(soup, c, content, svc_slug)
    replace_cobertura(soup, c, content, svc_slug)
    replace_faq(soup, c, content)
    replace_footer_cta(soup, c, content)
    replace_sticky_and_float(soup, c, content)

    # Convert to string for final text-level passes
    result_html = str(soup)
    result_html = replace_js_wa(result_html, c, content)
    result_html = safe_replace_urls(result_html, c, svc_slug)

    return result_html


def jaccard_check(ref_html, new_html, threshold=0.25):
    """Check Jaccard similarity between reference and new HTML text."""
    import re
    def extract_text(html):
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup(['script', 'style', 'svg']):
            tag.decompose()
        return set(re.findall(r'\b\w{4,}\b', soup.get_text().lower()))

    ref_words = extract_text(ref_html)
    new_words = extract_text(new_html)
    intersection = ref_words & new_words
    union = ref_words | new_words
    jaccard = len(intersection) / len(union) if union else 0
    return jaccard


# ═══════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python3 template-builder.py <city-slug> <service|--all>')
        print('     python3 template-builder.py --batch')
        sys.exit(1)

    if sys.argv[1] == '--batch':
        # Load city database to get all slugs
        with open(os.path.join(DIR, 'city-context-database.json')) as f:
            db = json.load(f)
        cities = [s for s in db.keys() if s != 'goiania-go']
        services = ['articulada', 'tesoura', 'combustao', 'transpaleteira', 'curso']
        total = 0
        for city_slug in cities:
            for svc in services:
                ref_file = REFS[svc]
                if not os.path.exists(ref_file):
                    print(f'  [SKIP] Sem referência para {svc}')
                    continue
                out_file = os.path.join(DIR, f'{city_slug}-{SLUGS[svc]}-TPL.html')
                if os.path.exists(out_file):
                    print(f'  [SKIP] Já existe: {out_file}')
                    continue
                html = build_lp(city_slug, svc)
                if html:
                    with open(out_file, 'w', encoding='utf-8') as f:
                        f.write(html)
                    total += 1
                    # Quick Jaccard check
                    with open(ref_file, 'r', encoding='utf-8') as f:
                        ref_html = f.read()
                    jac = jaccard_check(ref_html, html)
                    status = 'OK' if jac < 0.25 else 'ALTO' if jac < 0.40 else 'DUPLICADO'
                    print(f'    → {out_file} (Jaccard: {jac:.2f} {status})')
        print(f'\nTotal gerado: {total}')

    else:
        city_slug = sys.argv[1]
        services_arg = sys.argv[2] if len(sys.argv) > 2 else '--all'

        if services_arg == '--all':
            services = ['articulada', 'tesoura', 'combustao', 'transpaleteira', 'curso']
        else:
            services = [services_arg]

        for svc in services:
            ref_file = REFS[svc]
            if not os.path.exists(ref_file):
                print(f'[SKIP] Sem referência para {svc}: {ref_file}')
                continue
            html = build_lp(city_slug, svc)
            if html:
                out_file = os.path.join(DIR, f'{city_slug}-{SLUGS[svc]}-TPL.html')
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(html)
                # Jaccard check
                with open(ref_file, 'r', encoding='utf-8') as f:
                    ref_html = f.read()
                jac = jaccard_check(ref_html, html)
                status = 'OK' if jac < 0.25 else 'ALTO' if jac < 0.40 else 'DUPLICADO'
                print(f'  → {out_file} ({len(html):,} bytes, Jaccard: {jac:.2f} {status})')
