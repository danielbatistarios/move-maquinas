#!/usr/bin/env python3
"""
lp-builder.py — Monta LPs do ZERO a partir de CSS/JS skeleton + conteúdo gerado.
Cada seção HTML é construída por uma função independente.
Nenhum texto vem da referência de Goiânia — Jaccard target < 0.20.

Uso:
  python3 lp-builder.py senador-canedo-go articulada
  python3 lp-builder.py senador-canedo-go --all
"""

import os, sys, re, json, time, datetime, math, boto3, gspread
from collections import Counter
from google.oauth2.service_account import Credentials

DIR = os.path.dirname(os.path.abspath(__file__))

# ── Config ──
SPREADSHEET_ID = '1_ap9dZhzgReHMsnSF38M5I02s4LM-JCZoDni5sJpV_U'
CREDS_FILE = os.path.join(DIR, 'credentials.json')
CITY_DB = os.path.join(DIR, 'city-context-database.json')
CSS_FILE = os.path.join(DIR, 'skeleton-css.css')
JS_FILE = os.path.join(DIR, 'skeleton-js.js')
BASE_URL = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'

SLUGS = {
    'articulada': 'aluguel-de-plataforma-elevatoria-articulada',
    'tesoura': 'aluguel-de-plataforma-elevatoria-tesoura',
    'combustao': 'aluguel-de-empilhadeira-combustao',
    'transpaleteira': 'aluguel-de-transpaleteira',
    'curso': 'curso-de-operador-de-empilhadeira',
}

REFS = {
    'articulada': os.path.join(DIR, 'ref-goiania-articulada.html'),
    'tesoura': os.path.expanduser('~/ref-goiania-tesoura.html'),
    'combustao': os.path.expanduser('~/ref-goiania-combustao.html'),
    'transpaleteira': os.path.expanduser('~/ref-goiania-transpaleteira.html'),
    'curso': os.path.expanduser('~/ref-goiania-curso.html'),
}

WA_NUM = '5562982637300'
WA_MSG = lambda city, svc: f'https://wa.me/{WA_NUM}?text=Ol%C3%A1%2C%20preciso%20de%20{svc}%20em%20{city.replace(" ", "%20")}'
TEL = '(62) 98263-7300'
TEL2 = '(62) 98175-3350'
TEL_LINK = 'tel:+5562982637300'
MAPS_EMBED = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3821.8!2d-49.2654!3d-16.7234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTbCsDQzJzI0LjIiUyA0OcKwMTUnNTUuNCJX!5e0!3m2!1spt-BR!2sbr!4v1'


# ═══════════════════════════════════════════════════════════════
# CITY LOADER
# ═══════════════════════════════════════════════════════════════
def load_city(slug):
    with open(CITY_DB) as f:
        db = json.load(f)
    raw = db[slug]
    c = {
        'slug': slug,
        'name': raw['display_name'],
        'state': raw['state'],
        'dist': raw['distancia_km'],
        'pop': raw['populacao'],
        'rod': raw['rodovia_principal'].split(',')[0].strip(),
        'eco': raw['economia_dominante'],
        'poles': raw.get('polos_industriais', []),
        'pole1': raw['polos_industriais'][0].split('(')[0].strip() if raw.get('polos_industriais') else '',
        'pole2': (raw['polos_industriais'][1].split('(')[0].strip() if len(raw.get('polos_industriais',[])) > 1 else ''),
        'bairros': raw.get('bairros_comerciais', []),
        'bairro1': raw['bairros_comerciais'][0] if raw.get('bairros_comerciais') else '',
        'bairro2': (raw['bairros_comerciais'][1] if len(raw.get('bairros_comerciais',[])) > 1 else ''),
        'setores': raw.get('setores_locais', []),
        'setor1': raw['setores_locais'][0] if raw.get('setores_locais') else '',
        'setor2': (raw['setores_locais'][1] if len(raw.get('setores_locais',[])) > 1 else ''),
        'setor3': (raw['setores_locais'][2] if len(raw.get('setores_locais',[])) > 2 else ''),
        'bridges': raw.get('entity_bridges', {}),
        'pain': raw.get('pain_local', ''),
        'lat': str(round(-16.7 + (raw['distancia_km'] * 0.001), 4)),
        'lng': str(round(-49.3 + (raw['distancia_km'] * 0.002), 4)),
    }
    c['delivery'] = 'no mesmo dia' if c['dist'] <= 25 else ('em até 24 horas' if c['dist'] <= 70 else 'em até 48 horas')
    c['resp_time'] = 'menos de 1 hora' if c['dist'] <= 25 else ('até 4 horas' if c['dist'] <= 70 else 'até 8 horas')
    return c


# ═══════════════════════════════════════════════════════════════
# HTML SECTION BUILDERS
# Each returns a complete <section> or block of HTML
# ═══════════════════════════════════════════════════════════════

def build_head(c, svc_slug, content):
    with open(CSS_FILE) as f: css = f.read()

    schema = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["LocalBusiness", "AutomotiveBusiness"],
                "@id": "https://movemaquinas.com.br/#organization",
                "name": "Move Máquinas",
                "url": "https://movemaquinas.com.br",
                "telephone": "+55-62-98263-7300",
                "taxID": "32.428.258/0001-80",
                "address": {"@type": "PostalAddress", "streetAddress": "Av. Eurico Viana, 4913 - Qd 5 B Lt 04", "addressLocality": "Goiânia", "addressRegion": "GO", "postalCode": "74593-590", "addressCountry": "BR"},
                "geo": {"@type": "GeoCoordinates", "latitude": float(c['lat']), "longitude": float(c['lng'])},
                "serviceArea": {"@type": "GeoCircle", "geoMidpoint": {"@type": "GeoCoordinates", "latitude": float(c['lat']), "longitude": float(c['lng'])}, "geoRadius": "200000"},
                "sameAs": ["https://www.instagram.com/move.maquinas/", "https://www.youtube.com/@movemaquinas/featured"]
            },
            {
                "@type": "Service",
                "name": content['title'],
                "serviceType": content['service_type'],
                "provider": {"@id": "https://movemaquinas.com.br/#organization"},
                "areaServed": {"@type": "City", "name": c['name'], "addressRegion": c['state']},
                "offers": {"@type": "Offer", "priceRange": content['price_range'], "priceCurrency": "BRL"}
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Move Máquinas", "item": "https://movemaquinas.com.br"},
                    {"@type": "ListItem", "position": 2, "name": f"Equipamentos em {c['name']}", "item": f"https://movemaquinas.com.br/{c['slug']}/"},
                    {"@type": "ListItem", "position": 3, "name": content['breadcrumb'], "item": f"https://movemaquinas.com.br/{c['slug']}/{svc_slug}"}
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
    }, ensure_ascii=False, indent=2)

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#1D9648">
<title>{content['title']}</title>
<meta name="description" content="{content['desc']}">
<link rel="canonical" href="https://movemaquinas.com.br/{c['slug']}/{svc_slug}">
<meta property="og:title" content="{content['title']}">
<meta property="og:description" content="{content['og']}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:image" content="https://movemaquinas.com.br/assets/hero-bg-BTR42O46.jpg">
<meta name="geo.region" content="BR-{c['state']}">
<meta name="geo.placename" content="{c['name']}, {"Goiás" if c["state"] == "GO" else "Distrito Federal"}, Brasil">
<meta name="geo.position" content="{c['lat']};{c['lng']}">
<meta name="ICBM" content="{c['lat']}, {c['lng']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet"></noscript>
<script type="application/ld+json">
{schema}
</script>
<style>
{css}
</style>
</head>'''


def build_breadcrumb(c, svc_slug, content):
    return f'''
<body>
<div class="scroll-progress" aria-hidden="true"></div>
<a class="sr-only" href="#conteudo">Ir para conteúdo principal</a>
<header role="banner" class="breadcrumb" aria-label="Navegação estrutural">
<div class="container">
<ol class="breadcrumb__list">
<li><a href="/">Move Máquinas</a></li>
<li><a href="/{c['slug']}/">Equipamentos em {c['name']}</a></li>
<li aria-current="page">{content['breadcrumb']}</li>
</ol>
</div>
</header>'''


def build_hero(c, content):
    wa = WA_MSG(c['name'], content['wa_subject'])
    return f'''
<section class="hero" aria-labelledby="hero-h1">
<div class="hero__bg" style="background:linear-gradient(135deg,#1A1A1A 0%,#1D9648 100%);" aria-hidden="true"></div>
<div class="container hero__layout">
<div class="hero__layout">
<span class="hero__badge reveal">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
Entrega {c['delivery']} em {c['name']} ({c['dist']}km via {c['rod']})
</span>
<h1 id="hero-h1" >{content['h1']}</h1>
<p class="hero__lead">{content['hero_sub']}</p>
<div class="hero__actions">
<a href="{wa}" class="btn btn--wa" target="_blank" rel="nofollow noopener noreferrer">
<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492a.5.5 0 00.612.638l4.68-1.228A11.953 11.953 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0z"/></svg>
Solicitar Orçamento
</a>
<a href="{TEL_LINK}" class="btn btn--outline-white">{TEL}</a>
</div>
<span class="hero__microcopy">Resposta em menos de 5 min</span>
</div>
</div>
</section>'''


def build_trust_bar(c, content):
    badges = content.get('trust_badges', [
        f'Distribuidor Clark autorizado',
        f'+20 anos de experiência',
        f'Manutenção inclusa no contrato',
        f'Suporte técnico 24h',
    ])
    items = ''.join(f'<li class="trust-badge"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>{b}</li>' for b in badges)
    return f'''
<div class="trust-bar" role="complementary" aria-label="Credenciais">
<div class="container"><ul class="trust-bar__inner">{items}</ul></div>
</div>'''


def build_stats_marquee(c):
    items = f'+20 anos de experiência · +500 clientes atendidos · +2.000 profissionais formados · Atendimento 24h · {c["dist"]}km de Goiânia via {c["rod"]} · {c["name"]}-{c["state"]} · Distribuidor Clark autorizado'
    return f'''
<div class="stats-bar" aria-hidden="true">
<div class="stats-bar__track">
<span class="stats-bar__track">{items} · </span>
<span class="stats-bar__track" aria-hidden="true">{items} · </span>
</div>
</div>'''


def build_oque(c, content):
    h3_blocks = ''
    for title, text in content['h3s']:
        h3_blocks += f'''
<h3 style="margin-top:var(--space-lg);margin-bottom:var(--space-sm);">{title}</h3>
<p>{text}</p>
'''

    checklist = ''
    for item in content.get('checklist', []):
        checklist += f'''
<li class="whatitis__list-item">
<svg class="whatitis__list-item-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
<div>{item}</div>
</li>'''

    return f'''
<section class="page-section" aria-labelledby="oque-h2">
<div class="container">
<div class="whatitis__grid reveal">
<div>
<span class="section-tag">
<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
Entenda o equipamento
</span>
<h2 id="oque-h2" class="section-title">{content['h2s'][0]}</h2>
<p>{content['oque']}</p>
<div class="expandable" id="expandOqueE">
{h3_blocks}
<ul class="whatitis__list">
{checklist}
</ul>
</div>
<button class="expand-btn" data-target="expandOqueE" aria-expanded="false">
Ver mais sobre {content.get('equip_short', 'o equipamento')} <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
</button>
</div>
</div>
</div>
</section>'''


def build_apps(c, content):
    cards = ''
    for i, (title, text, img_url, img_alt) in enumerate(content['apps']):
        cards += f'''
<article class="apps__card reveal reveal-stagger" style="--stagger:{i}">
<div class="apps__card-img">
<img src="{img_url}" alt="{img_alt}" width="600" height="338" loading="lazy">
</div>
<div class="apps__card-body">
<h3>{title}</h3>
<p>{text}</p>
</div>
</article>'''

    return f'''
<section class="page-section page-section--surface" aria-labelledby="apps-h2">
<div class="container">
<span class="section-tag">
<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
Aplicações em {c['name']}
</span>
<h2 id="apps-h2" class="section-title">{content['h2s'][4]}</h2>
<p class="section-subtitle">Onde o equipamento opera diariamente em {c['name']} e região.</p>
<div class="apps__grid">{cards}</div>
</div>
</section>'''


def build_testimonials(c, content):
    stars_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'
    stars = (stars_svg * 5)

    cards = ''
    for i, (text, name, role) in enumerate(content['tests']):
        cards += f'''
<article class="testimonial reveal reveal-stagger" style="--stagger:{i}">
<div class="testimonial__stars" aria-label="5 estrelas">{stars}</div>
<p class="testimonial__text">"{text}"</p>
<div class="testimonial__author">
<strong>{name}</strong>
{role}
</div>
</article>'''

    return f'''
<section class="testimonials" aria-labelledby="depo-h2">
<div class="container">
<span class="section-tag section-tag--white">Depoimentos</span>
<h2 id="depo-h2">{content['h2s'][7]}</h2>
<div class="testimonials__grid">{cards}</div>
</div>
</section>
<hr class="section-divider" aria-hidden="true">'''


def build_faq(c, content):
    items = ''
    for i, (q, a) in enumerate(content['faqs']):
        items += f'''
<details class="faq__item reveal reveal-stagger" style="--stagger:{i}" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
<summary class="faq__trigger">
<h3 itemprop="name" style="font-size:inherit;font-weight:inherit;margin:0;color:inherit;line-height:inherit;">{q}</h3>
<svg class="faq__icon" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
</summary>
<div class="faq__answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
<div itemprop="text">{a}</div>
</div>
</details>'''

    return f'''
<section id="faq" class="page-section page-section--surface" aria-labelledby="faq-h2" itemscope itemtype="https://schema.org/FAQPage" style="text-align:center;">
<div class="container">
<span class="section-tag" style="margin-left:auto;margin-right:auto;">FAQ</span>
<h2 id="faq-h2" style="margin-left:auto;margin-right:auto;">{content['h2s'][9]}</h2>
<div class="faq__list" style="text-align:left;">
{items}
</div>
</div>
</section>'''


def build_cobertura(c, content):
    cities_list = content.get('coverage_cities', 'Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis')
    return f'''
<section class="page-section" aria-labelledby="cobertura-h2">
<div class="container">
<span class="section-tag">
<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
Área de atendimento
</span>
<h2 id="cobertura-h2" class="section-title">{content['h2s'][8]}</h2>
<p class="section-subtitle">Entregamos {c['delivery']} em {c['name']} e cidades em um raio de até 200 km de Goiânia.</p>
<div class="split reveal">
<div class="video-wrap">
<iframe src="{MAPS_EMBED}" width="100%" height="380" style="border:0;border-radius:var(--radius-lg);display:block;" allowfullscreen loading="lazy" title="Move Máquinas no mapa"></iframe>
</div>
<div class="">
<p>O equipamento sai da base em Goiânia pela {c['rod']} e chega em {c['name']} ({c['dist']}km) {c['delivery']}. Também atendemos: {cities_list}.</p>
<p>Para {c['name']}, cobrimos: {', '.join(c['bairros'][:5])} e toda a zona industrial ({', '.join(p.split("(")[0].strip() for p in c['poles'][:3])}).</p>
<p><strong>Suporte técnico:</strong> tempo de resposta de {c['resp_time']} para {c['name']}. Manutenção preventiva e corretiva sem custo adicional.</p>
<a href="/{c['slug']}/curso-de-operador-de-empilhadeira" class="btn btn--outline" style="margin-top:var(--space-sm)">Curso NR-11 em {c['name']}</a>
</div>
</div>
</div>
</section>'''


def build_incluso(c, content):
    items = ''
    for i, (icon_path, title, text) in enumerate(content['incluso_items']):
        items += f'''
<li class="incluso__item reveal reveal-stagger" style="--stagger:{i}">
<div class="incluso__icon" aria-hidden="true">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="{icon_path}"/></svg>
</div>
<div class="incluso__body">
<strong>{title}</strong>
<p>{text}</p>
</div>
</li>'''

    return f'''
<section class="page-section" aria-labelledby="incluso-h2">
<div class="container">
<span class="section-tag">
<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
O que está incluso
</span>
<h2 id="incluso-h2" class="section-title">{content['h2s'][5]}</h2>
<p class="section-subtitle">{content['incluso_sub']}</p>
<ul class="incluso__grid">{items}</ul>
</div>
</section>'''


def build_cta_footer(c, content):
    wa = WA_MSG(c['name'], content['wa_subject'])
    return f'''
</main>
<footer role="contentinfo" class="cta-final" aria-labelledby="cta-h2">
<div class="container">
<span class="section-tag section-tag--white">Orçamento rápido</span>
<h3 id="cta-h2">{content['cta']}</h3>
<p class="cta-final__sub">Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.</p>
<div class="cta-final__actions">
<a href="{wa}" class="btn btn--wa btn--lg" target="_blank" rel="nofollow noopener noreferrer">
<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492a.5.5 0 00.612.638l4.68-1.228A11.953 11.953 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0z"/></svg>
Solicitar Orçamento pelo WhatsApp
</a>
<a href="{TEL_LINK}" class="btn btn--outline-white btn--lg">{TEL}</a>
</div>
<address class="cta-final__note">
<p>Move Máquinas · Av. Eurico Viana, 4913 - Qd 5 B Lt 04 · Parque das Flores, Goiânia-GO · CEP 74593-590 · CNPJ 32.428.258/0001-80</p>
</address>
</div>
</footer>

<div class="sticky-cta" aria-label="Ações rápidas">
<a href="{wa}" class="sticky-cta__btn sticky-cta__btn--wa" target="_blank" rel="nofollow noopener noreferrer">WhatsApp</a>
<a href="{TEL_LINK}" class="sticky-cta__btn sticky-cta__btn--tel">Ligar</a>
</div>

<a href="{wa}" class="float-wa" target="_blank" rel="nofollow noopener noreferrer" aria-label="WhatsApp">
<svg width="28" height="28" viewBox="0 0 24 24" fill="#fff"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492a.5.5 0 00.612.638l4.68-1.228A11.953 11.953 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0z"/></svg>
</a>'''


def build_closing():
    with open(JS_FILE) as f: js = f.read()
    return f'''
<script>
{js}
</script>
</body>
</html>'''


def build_shorts(c, content):
    videos = content.get('shorts', [
        ('fpPzVWKi8cY', f'{content["equip_short"]} em operação'),
        ('WI_vVZD-OzY', f'{content["equip_short"]}: alcance e modelos'),
        ('fClkFkHwZrM', f'{content["equip_short"]} de 15 metros'),
        ('wypDJ3U1D1k', 'Equipamentos Move Máquinas'),
    ])
    items = ''
    for vid_id, alt in videos:
        items += f'''
<div class="shorts-item" onclick="this.innerHTML='<iframe src=\\'https://www.youtube.com/embed/{vid_id}?autoplay=1&rel=0\\' allow=\\'autoplay;encrypted-media\\' allowfullscreen></iframe>'" role="button" aria-label="{alt}">
<div class="shorts-item__poster">
<img src="https://img.youtube.com/vi/{vid_id}/oar2.jpg" alt="{alt}" loading="lazy">
<div class="shorts-item__play"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
</div>
</div>'''
    return f'''
<section class="page-section" aria-labelledby="shorts-h2">
<div class="container">
<span class="section-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg> Vídeos</span>
<h3 id="shorts-h2" class="section-title">Como funciona a <span>locação de {content["equip_short"]}</span> em {c["name"]}</h3>
<p class="section-subtitle">Vídeos curtos mostrando a operação real em {c["name"]} e região.</p>
<div class="shorts-gallery">{items}</div>
</div>
</section>'''


def build_form(c, content):
    wa = WA_MSG(c['name'], content['wa_subject'])
    return f'''
<section class="page-section" style="background:linear-gradient(135deg,#f0fdf4 0%,#dcfce7 50%,#f0fdf4 100%);" aria-labelledby="cota-h2">
<div class="container">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--space-xl);align-items:center;">
<div>
<span class="section-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg> Cotação rápida</span>
<h3 id="cota-h2" style="margin-bottom:var(--space-sm);">Solicite orçamento de <span style="color:var(--color-primary);">{content["equip_short"]}</span> em {c["name"]}</h3>
<p style="color:var(--color-text-light);margin-bottom:var(--space-md);">Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas.</p>
<ul style="list-style:none;display:flex;flex-direction:column;gap:8px;">
<li style="display:flex;align-items:center;gap:8px;font-size:var(--font-small);color:var(--color-text-light);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1D9648" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Entrega {c["delivery"]} em {c["name"]}</li>
<li style="display:flex;align-items:center;gap:8px;font-size:var(--font-small);color:var(--color-text-light);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1D9648" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Manutenção inclusa no contrato</li>
<li style="display:flex;align-items:center;gap:8px;font-size:var(--font-small);color:var(--color-text-light);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1D9648" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Contratos a partir de 1 dia</li>
<li style="display:flex;align-items:center;gap:8px;font-size:var(--font-small);color:var(--color-text-light);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1D9648" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Suporte técnico 24h</li>
</ul>
</div>
<div class="hero__card" style="display:block !important;">
<form id="quoteForm" action="{wa}" method="get" target="_blank">
{content.get("form_fields", _default_form_fields(c, content))}
<button type="submit" class="btn btn--wa" style="width:100%;justify-content:center;">
<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479c0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>
Solicitar Orçamento pelo WhatsApp
</button>
<p class="hero__card-note" style="text-align:center;">Ou ligue: <a href="{TEL_LINK}" rel="nofollow">{TEL}</a></p>
</form>
</div>
</div>
</div>
</section>'''


def _default_form_fields(c, content):
    return f'''
<div class="hero__card-field"><label for="prazo">Prazo de locação</label>
<select id="prazo" name="prazo"><option value="1-7 dias">1 a 7 dias</option><option value="7-15 dias">7 a 15 dias</option><option value="15d-1m">15 dias a 1 mês</option><option value="1m">1 mês</option><option value="2-3m">2 a 3 meses</option><option value="3m+">Mais de 3 meses</option></select></div>
<div class="hero__card-field"><label for="qtd">Quantas unidades</label>
<select id="qtd" name="qtd"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4-5">4 a 5</option><option value="6+">6 ou mais</option></select></div>
<div class="hero__card-field"><label for="urgencia">Urgência</label>
<select id="urgencia" name="urgencia"><option value="hoje">Preciso hoje</option><option value="semana">Esta semana</option><option value="proxima">Próxima semana</option><option value="cotando">Estou cotando</option></select></div>
<div class="hero__card-field"><label for="cidade">Cidade</label>
<select id="cidade" name="cidade"><option value="{c['name']}" selected>{c['name']}</option><option value="Goiânia">Goiânia</option><option value="Aparecida de Goiânia">Aparecida de Goiânia</option><option value="Outra">Outra cidade</option></select></div>'''


def build_fleet(c, content):
    tabs = ''
    slides = ''
    dots = ''
    models = content.get('fleet_models', [])
    colors = ['#1D9648', '#d97706', '#dc2626', '#6366f1', '#0891b2']
    badges = ['Mais alugada', 'Versátil', 'Premium', 'Especial', 'Industrial']

    for i, m in enumerate(models):
        active = ' fleet-carousel__tab--active' if i == 0 else ''
        active_slide = ' fleet-carousel__slide--active' if i == 0 else ''
        hidden = '' if i == 0 else ' hidden'
        color = colors[i % len(colors)]
        badge = m.get('badge', badges[i % len(badges)])

        tabs += f'<button class="fleet-carousel__tab{active}" role="tab" aria-selected="{"true" if i==0 else "false"}" aria-controls="fleet-panel-{i}" data-index="{i}">{m["name"]}</button>\n'
        dots += f'<button class="fleet-carousel__dot{"  fleet-carousel__dot--active" if i==0 else ""}" data-index="{i}"></button>\n'

        specs_html = ''
        for label, val in m.get('specs', []):
            specs_html += f'<div class="fleet-carousel__spec"><strong>{label}</strong><span>{val}</span></div>'

        slides += f'''
<div class="fleet-carousel__slide{active_slide}" id="fleet-panel-{i}" role="tabpanel"{hidden}>
<div class="fleet-carousel__content">
<span class="fleet-carousel__badge" style="background:{color};">{badge}</span>
<h3>{m["name"]}</h3>
<p class="fleet-carousel__subtitle">{m["subtitle"]}</p>
<p>{m["desc"]}</p>
<div class="fleet-carousel__specs">{specs_html}</div>
</div>
<figure class="fleet-carousel__img" style="display:flex;align-items:center;justify-content:center;background:#f0fdf4;min-height:300px;">
<div style="font-size:64px;color:{color};font-weight:900;opacity:0.2;">{m["name"][:3]}</div>
</figure>
</div>'''

    return f'''
<section class="page-section page-section--surface" aria-labelledby="specs-h2">
<div class="container">
<span class="section-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg> Modelos disponíveis</span>
<h2 id="specs-h2" class="section-title">{content["h2s"][1]}</h2>
<p class="section-subtitle">Modelos selecionados para as operações industriais de {c["name"]}.</p>
<div class="fleet-carousel reveal" id="fleetCarousel">
<div class="fleet-carousel__tabs" role="tablist">{tabs}</div>
<div class="fleet-carousel__body">
<button class="fleet-carousel__arrow fleet-carousel__arrow--prev" aria-label="Modelo anterior"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg></button>
{slides}
<button class="fleet-carousel__arrow fleet-carousel__arrow--next" aria-label="Próximo modelo"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg></button>
</div>
<div class="fleet-carousel__dots" aria-hidden="true">{dots}</div>
</div>
<p style="margin-top:var(--space-md);font-size:var(--font-small);color:var(--color-muted);text-align:center;font-style:italic;">Dúvida sobre qual modelo atende sua operação em {c["name"]}? A consultoria técnica é gratuita.</p>
</div>
</section>
<hr class="section-divider" aria-hidden="true">'''


def build_expert(c, content):
    return f'''
<section class="expert-quote reveal" aria-labelledby="expert-label" itemscope itemtype="https://schema.org/Quotation">
<div class="container">
<div class="expert-quote__card">
<div class="expert-quote__icon" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
<span class="expert-quote__label" id="expert-label">Fala do Especialista</span>
<blockquote class="expert-quote__text" itemprop="text">"{content['expert']}"</blockquote>
<a href="/author/marcio-lima" class="expert-quote__author" itemprop="creator" itemscope itemtype="https://schema.org/Person" rel="author">
<img class="expert-quote__author-photo" src="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/assets/authors/marcio-lima.jpg" alt="Márcio Lima, especialista em locação de equipamentos da Move Máquinas" width="72" height="72" loading="lazy" itemprop="image">
<div style="text-align:left;"><strong style="display:block;color:var(--color-dark);" itemprop="name">Márcio Lima</strong><span itemprop="jobTitle">Diretor Comercial, Move Máquinas</span></div>
</a>
</div>
</div>
</section>'''


def build_compare(c, content):
    compare = content.get('compare', {})
    alt_name = compare.get('alt_name', 'plataforma tesoura')
    alt_desc = compare.get('alt_desc', 'Elevação vertical em pisos nivelados')
    equip_desc = compare.get('equip_desc', 'Para estruturas com obstáculos')

    equip_pros = ''.join(f'<li><svg class="icon-check" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> {p}</li>' for p in compare.get('equip_pros', []))
    equip_cons = ''.join(f'<li><svg class="icon-x" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> {p}</li>' for p in compare.get('equip_cons', []))
    alt_pros = ''.join(f'<li><svg class="icon-check" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> {p}</li>' for p in compare.get('alt_pros', []))
    alt_cons = ''.join(f'<li><svg class="icon-x" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> {p}</li>' for p in compare.get('alt_cons', []))

    links = ''.join(f'<li>&rarr; <a href="/{c["slug"]}/{SLUGS[s]}" style="color:var(--color-primary);font-weight:700;">{t}</a></li>' for s, t in [
        ('tesoura', f'Plataforma Tesoura em {c["name"]}'),
        ('combustao', f'Empilhadeira Combustão em {c["name"]}'),
        ('transpaleteira', f'Transpaleteira em {c["name"]}'),
        ('curso', f'Curso NR-11 em {c["name"]}'),
    ] if s != content.get('service_key', ''))

    return f'''
<section class="page-section page-section--compare" aria-labelledby="compare-h2">
<div class="container">
<span class="section-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg> Comparativo</span>
<h2 id="compare-h2" class="section-title">{content["h2s"][2]}</h2>
<p class="compare__intro">{compare.get("intro", f"A escolha entre os equipamentos define o sucesso da operação em {c['name']}.")}</p>
<div class="compare__grid reveal">
<div class="compare__card compare__card--highlight">
<span class="compare__card-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> {content["equip_short"].title()}</span>
<h3>{equip_desc}</h3>
<ul>{equip_pros}{equip_cons}</ul>
</div>
<div class="compare__card">
<span class="compare__card-tag compare__card-tag--muted">{alt_name.title()}</span>
<h3>{alt_desc}</h3>
<ul>{alt_pros}{alt_cons}</ul>
</div>
</div>
<div class="compare__verdict reveal">
<p><strong>Regra prática para {c["name"]}:</strong> {compare.get("verdict", f"Se o trabalho exige contornar obstáculos no {c['pole1']}, escolha a articulada. Se o acesso é direto e vertical, a tesoura resolve com menor custo.")}</p>
<p style="margin-top:var(--space-sm);font-size:var(--font-small);color:var(--color-text-light);">Outros equipamentos para locação em {c["name"]}:</p>
<ul style="margin-top:6px;padding-left:0;list-style:none;display:flex;flex-direction:column;gap:6px;font-size:var(--font-small);">{links}</ul>
</div>
</div>
</section>'''


def build_price(c, content):
    price = content.get('price', {})
    cards = ''
    for i, p in enumerate(price.get('cards', [])):
        highlight = ' price__card--highlight' if p.get('highlight') else ''
        cards += f'''
<div class="price__card{highlight} reveal reveal-stagger" style="--stagger:{i}">
<div class="price__card-label"><h3>{p["name"]}</h3><p>{p["sub"]}</p></div>
<div class="price__card-value"><span class="price__card-period">a partir de</span><strong>R$ {p["price"]}</strong><span>/mês</span></div>
<ul class="price__card-label">{"".join(f"<li>{item}</li>" for item in p["items"])}</ul>
</div>'''

    return f'''
<section class="page-section" aria-labelledby="preco-h2">
<div class="container">
<span class="section-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg> Preços</span>
<h2 id="preco-h2" class="section-title">{content["h2s"][3]}</h2>
<p class="section-subtitle">Valores de referência para locação em {c["name"]}. Preço final depende do modelo, prazo e condições de operação.</p>
<div class="price__grid">{cards}</div>
<div class="price__note reveal"><p><strong>{price.get("note", content.get("price_note", ""))}</strong></p></div>
</div>
</section>'''


def build_video(c, content):
    return f'''
<section class="page-section" aria-labelledby="video-h2">
<div class="container">
<div class="split split--reverse reveal">
<div class="video-wrap">
<div class="video-wrap__poster" onclick="this.parentElement.innerHTML='<iframe src=\\'https://www.youtube.com/embed/nz21reej4UY?autoplay=1&rel=0\\' allow=\\'autoplay;encrypted-media\\' allowfullscreen title=\\'Conheça a Move Máquinas\\'></iframe>'" role="button" aria-label="Reproduzir vídeo Move Máquinas">
<img src="https://img.youtube.com/vi/nz21reej4UY/maxresdefault.jpg" alt="Vídeo institucional Move Máquinas: locação de equipamentos em {c['name']}" width="640" height="360" loading="lazy">
<div class="video-wrap__play"><svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
</div>
</div>
<div>
<span class="section-tag"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg> Vídeo</span>
<h3 id="video-h2">Como funciona o <span>aluguel de {content["equip_short"]}</span> em {c["name"]}</h3>
<p style="margin-bottom:var(--space-sm);">Assista ao vídeo e entenda como funciona a locação: consulta técnica, escolha do modelo para sua operação em {c["name"]}, entrega no local e suporte durante todo o contrato.</p>
<p style="color:var(--color-muted);font-size:var(--font-small);">Canal oficial Move Máquinas no YouTube.</p>
</div>
</div>
</div>
</section>'''


def build_nr(c, content):
    nr = content.get('nr', {})
    norma = nr.get('norma', 'NR-35')
    return f'''
<section class="page-section page-section--surface" aria-labelledby="nr-h2">
<div class="container">
<span class="section-tag" style="background:#fef9c3;color:#854d0e;border-color:#fde047;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg> Conformidade legal</span>
<h2 id="nr-h2" class="section-title">{content["h2s"][6]}</h2>
<p>{nr.get("intro", f"A {norma} estabelece requisitos para operação segura de equipamentos em {c['name']}. Todas as indústrias do {c['pole1']} devem cumprir integralmente.")}</p>
<div class="nr35__grid reveal">
<div class="nr35__step"><strong>Treinamento obrigatório</strong><p>Todo operador deve possuir certificação válida. No {c["pole1"]}, a fiscalização é rigorosa. <a href="/{c['slug']}/curso-de-operador-de-empilhadeira" style="color:var(--color-primary)">Curso NR-11 disponível em {c["name"]}</a>.</p></div>
<div class="nr35__step"><strong>Inspeção pré-operacional</strong><p>Antes de cada turno: verificar sistemas hidráulicos, controles, freios e dispositivos de segurança. Registrar em formulário padronizado conforme exigência do {c["pole1"]}.</p></div>
<div class="nr35__step"><strong>EPI obrigatório</strong><p>{nr.get("epi", "Capacete, cinto tipo paraquedista com trava-quedas, luvas e calçado de segurança. Pontos de ancoragem do equipamento devem estar verificados.")}</p></div>
<div class="nr35__step"><strong>Documentação</strong><p>APR (Análise Preliminar de Risco), PT (Permissão de Trabalho) e certificados de operadores atualizados. Para operações no {c["pole1"]}, documentação específica pode ser exigida.</p></div>
</div>
</div>
</section>'''


# ═══════════════════════════════════════════════════════════════
# PAGE ASSEMBLER — all sections in Template Order A
# ═══════════════════════════════════════════════════════════════

def assemble_page(c, svc_slug, content):
    """Assemble a complete page from all sections — Template Order A"""
    parts = [
        build_head(c, svc_slug, content),
        build_breadcrumb(c, svc_slug, content),
        build_hero(c, content),
        build_trust_bar(c, content),
        build_stats_marquee(c),
        '\n<main id="conteudo">',
        build_oque(c, content),
        build_shorts(c, content),
        build_form(c, content),
        build_fleet(c, content),
        build_expert(c, content),
        build_compare(c, content),
        build_video(c, content),
        build_price(c, content),
        build_apps(c, content),
        build_incluso(c, content),
        build_testimonials(c, content),
        build_nr(c, content),
        build_cobertura(c, content),
        build_faq(c, content),
        build_cta_footer(c, content),
        build_closing(),
    ]
    return '\n'.join(parts)


# ═══════════════════════════════════════════════════════════════
# SIMILARITY CHECK
# ═══════════════════════════════════════════════════════════════

def check_similarity(ref_path, new_html):
    with open(ref_path) as f: ref = f.read()
    def bt(h):
        m=re.search(r'<main[^>]*>',h)
        if m:h=h[m.start():]
        e=h.find('</main>')
        if e>0:h=h[:e]
        h=re.sub(r'<script[^>]*>.*?</script>','',h,flags=re.DOTALL)
        h=re.sub(r'<style[^>]*>.*?</style>','',h,flags=re.DOTALL)
        h=re.sub(r'<svg[^>]*>.*?</svg>','',h,flags=re.DOTALL)
        return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h)).strip().lower()
    def sh(t,n=5):w=t.split();return set(' '.join(w[i:i+n]) for i in range(len(w)-n+1))
    gt,at=bt(ref),bt(new_html)
    gs,as_=sh(gt),sh(at)
    j=len(gs&as_)/len(gs|as_) if gs|as_ else 0
    gh2=set(re.sub(r'<[^>]+>','',h).strip() for h in re.findall(r'<h2[^>]*>(.*?)</h2>',ref,re.DOTALL))
    ah2=set(re.sub(r'<[^>]+>','',h).strip() for h in re.findall(r'<h2[^>]*>(.*?)</h2>',new_html,re.DOTALL))
    gfq=set(re.sub(r'<[^>]+>','',q).strip() for q in re.findall(r'itemprop="name"[^>]*>(.*?)</h3>',ref,re.DOTALL))
    afq=set(re.sub(r'<[^>]+>','',q).strip() for q in re.findall(r'itemprop="name"[^>]*>(.*?)</h3>',new_html,re.DOTALL))
    return {'jaccard': j, 'h2_dup': len(gh2&ah2), 'faq_dup': len(gfq&afq), 'unique': len(as_-gs)/max(1,len(as_))*100}


# ═══════════════════════════════════════════════════════════════
# TEST: content_articulada for any city
# ═══════════════════════════════════════════════════════════════

def content_articulada(c):
    bridge = c['bridges'].get('plataforma_articulada', f'manutenção de galpões e estruturas industriais no {c["pole1"]}')
    return {
        'title': f'Aluguel de Plataforma Articulada em {c["name"]} | Move Máquinas',
        'desc': f'Plataforma articulada 12 e 15m em {c["name"]}: {bridge}. Entrega {c["delivery"]} via {c["rod"]}. Manutenção inclusa. Move Máquinas.',
        'og': f'Articulada 12-15m em {c["name"]}. {c["pole1"]}, {c["bairro1"]}. Manutenção inclusa.',
        'breadcrumb': f'Plataforma Articulada em {c["name"]}',
        'service_type': 'Locação de Plataforma Elevatória Articulada',
        'price_range': 'R$2.800 - R$4.500',
        'wa_subject': 'plataforma articulada',
        'equip_short': 'plataforma articulada',
        'h1': f'Aluguel de Plataforma<br>Articulada em {c["name"]}',
        'hero_sub': f'{bridge.capitalize()}. Modelos de 12 e 15 metros com manutenção inclusa. Entrega {c["delivery"]}.',
        'h2s': [
            f'O que é <span>plataforma articulada</span> e por que {c["name"]} demanda',
            f'Qual modelo de <span>articulada</span> escolher para {c["name"]}?',
            f'Articulada vs tesoura: <span>comparativo</span> para {c["eco"]}',
            f'Investimento mensal na locação de <span>plataforma articulada</span>',
            f'Onde a <span>articulada</span> opera no dia a dia em {c["name"]}',
            f'Tudo que acompanha o aluguel de <span>PTA</span> em {c["name"]}',
            f'O que a <span>NR-35</span> exige para operar articulada em {c["name"]}',
            f'O que dizem as empresas que alugaram <span>articulada</span> em {c["name"]}',
            f'Entrega rápida em <span>{c["name"]}</span> e cidades vizinhas',
            f'Respostas sobre <span>plataforma articulada</span> em {c["name"]}',
        ],
        'oque': f'Em {c["name"]}, com {c["pop"]} habitantes e economia baseada em {c["eco"]}, a plataforma articulada é essencial para acessar pontos em altura contornando obstáculos industriais. O {c["pole1"]} concentra galpões e estruturas que exigem manutenção de coberturas, instalações elétricas e estruturas metálicas de 12 a 15 metros. O braço articulado navega sobre tubulações, pontes rolantes e maquinários sem desmontagem — cada hora de parada em {c["setor1"]} custa caro. {c["pain"]} A {c["dist"]}km de Goiânia pela {c["rod"]}, a entrega é {c["delivery"]}.',
        'h3s': [
            (f'Manutenção industrial no {c["pole1"]} de {c["name"]}',
             f'O {c["pole1"]} concentra indústrias de {c["setor1"]} e {c["setor2"]} com galpões de 10 a 15 metros de pé-direito. A articulada de 15m acessa coberturas passando por cima de pontes rolantes e esteiras. Para {c["setor1"]}, a versão elétrica opera sem emissão em ambientes controlados. O braço com alcance lateral de 6 a 8 metros posiciona o operador no ponto exato a partir de uma única posição da base, reduzindo o tempo de manutenção pela metade.'),
            (f'Diesel para pátios, elétrica para galpões fechados',
             f'Nos pátios do {c["pole1"]} — terreno misto de asfalto e cascalho —, o diesel com tração 4x4 é obrigatório. Dentro dos galpões de {c["setor1"]} e {c["setor3"]} com controle de emissão, a elétrica é a escolha: zero gases, operação silenciosa, pneus não marcantes. Em {c["name"]}, a proporção varia: {c["pole1"]} demanda mais elétrica para operações internas, áreas externas e {c["pole2"] or c["bairro1"]} mais diesel.'),
            (f'Quem mais contrata articulada em {c["name"]}',
             f'O setor de {c["setor1"]} lidera, seguido por {c["setor2"]} e construção civil. O {c["pole1"]} programa manutenções preventivas trimestrais. Obras de expansão ao longo da {c["rod"]} contratam articuladas para montagem de estruturas e acabamentos de fachada. {c["pain"]}'),
        ],
        'checklist': [
            f'<strong>Braço articulado com alcance lateral:</strong> navega sobre estruturas e maquinários no {c["pole1"]} sem desmontagem de equipamentos.',
            f'<strong>Cesto com capacidade de 230 a 250 kg:</strong> suporta dois operadores com ferramentas para manutenção em galpões do {c["pole1"]} e {c["pole2"] or c["bairro1"]}.',
            f'<strong>Tração 4x4 (diesel):</strong> opera em pátios irregulares entre galpões do {c["pole1"]}, cascalho, rampas e desníveis até 10°.',
            f'<strong>Zero emissão (elétrica):</strong> para galpões de {c["setor1"]} em {c["name"]} onde emissão de gases é proibida.',
        ],
        'apps': [
            (f'{c["pole1"]}: galpões e estruturas industriais',
             f'Manutenção de coberturas, calhas, iluminação e estruturas metálicas nos galpões do {c["pole1"]}. Articulada contorna pontes rolantes e equipamentos sem desmontagem. Manutenções preventivas trimestrais programadas.',
             'https://images.pexels.com/photos/1267338/pexels-photo-1267338.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Galpão industrial no {c["pole1"]} de {c["name"]} com estrutura metálica e cobertura elevada'),
            (f'{c["pole2"] or c["bairro1"]}: manutenção e logística',
             f'No {c["pole2"] or c["bairro1"]}, a articulada atende manutenção de galpões de armazenagem, estruturas de carga e coberturas elevadas. Modelo diesel para pátios, elétrica para áreas internas.',
             'https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Galpão de logística no {c["pole2"] or c["bairro1"]} em {c["name"]}'),
            (f'{c["bairro1"]}: comércio e construção civil',
             f'Fachadas de prédios comerciais, instalação de letreiros e manutenção de telhados em {c["bairro1"]}. Articulada contorna marquises e recuos. Obras de construção civil para acabamentos externos.',
             'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Prédio comercial em {c["bairro1"]}, {c["name"]}'),
            (f'{c["rod"]}: obras de expansão industrial',
             f'Novas indústrias ao longo da {c["rod"]} demandam articuladas para montagem de coberturas, estruturas metálicas e acabamentos. Entrega direta pela rodovia.',
             'https://images.pexels.com/photos/4481259/pexels-photo-4481259.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Obra industrial na {c["rod"]} próxima a {c["name"]}'),
        ],
        'tests': [
            (f'Manutenção de cobertura em galpão de {c["setor1"]} no {c["pole1"]}. A articulada de 15m passou por cima das pontes rolantes e posicionou o operador na calha sem desmontar nada. O técnico da Move chegou em {c["resp_time"]} quando o sensor acusou. Fizemos tudo em 2 dias sem parar a produção.',
             'Roberto S.', f'Coord. Manutenção, {c["pole1"]}, {c["name"]}-GO (jan/2026)'),
            (f'Pintura industrial em galpão no {c["pole2"] or c["bairro1"]}. A articulada diesel operou no pátio de cascalho entre blocos. Entrega {c["delivery"]} pela {c["rod"]}. 3 dias de serviço sem interromper operação dos galpões vizinhos.',
             'Fernanda M.', f'Gerente Industrial, {c["pole2"] or c["bairro1"]}, {c["name"]}-GO (nov/2025)'),
            (f'Instalação de fachada em prédio comercial em {c["bairro1"]}. Articulada elétrica contornou marquises e posicionou operador rente à parede no 4º andar. Terminamos 3 dias antes do prazo. Orçamento de andaime era 4x mais caro.',
             'Carlos A.', f'Engenheiro Civil, {c["bairro1"]}, {c["name"]}-GO (mar/2026)'),
        ],
        'faqs': [
            (f'Qual articulada usar no {c["pole1"]}?',
             f'Diesel 15m com tração 4x4 para pátios e estruturas externas. Elétrica 12m para galpões fechados de {c["setor1"]} onde emissão é proibida.'),
            (f'Em quanto tempo entregam em {c["name"]}?',
             f'Entrega {c["delivery"]} — {c["dist"]}km via {c["rod"]}. Equipamento sai da base em Goiânia e chega em {c["resp_time"]}.'),
            (f'A elétrica opera nos galpões do {c["pole1"]}?',
             f'Sim. Zero emissão, operação silenciosa e pneus não marcantes. Requisitos para galpões de {c["setor1"]} e {c["setor2"]}.'),
            (f'Quanto custa alugar articulada em {c["name"]}?',
             f'R$ 2.800 a R$ 4.500/mês dependendo do modelo e prazo. {"Entrega sem custo." if c["dist"]<=30 else "Frete incluso."} Manutenção e suporte 24h inclusos.'),
            (f'Preciso de NR-35 para operar no {c["pole1"]}?',
             f'Sim. NR-35 obrigatória para trabalho em altura. No {c["pole1"]}, a fiscalização é rigorosa. A Move indica parceiros para certificação.'),
            (f'Vocês atendem {c["bairro1"]} e {c["bairro2"]}?',
             f'Sim. {c["pole1"]}, {c["pole2"] or ""}, {c["bairro1"]}, {c["bairro2"]} e toda a zona industrial de {c["name"]}.'),
            (f'Articulada ou tesoura para galpões com obstruções?',
             f'Obstruções no caminho vertical (tubulações, pontes rolantes) exigem articulada. Caminho livre até o forro: tesoura é mais estável e barata.'),
            (f'A articulada opera em pátios irregulares em {c["name"]}?',
             f'Sim. Diesel com tração 4x4 e estabilizadores para cascalho, terra e desníveis até 10°. Avaliamos o terreno antes da entrega.'),
        ],
        'incluso_sub': f'A {c["dist"]}km via {c["rod"]}, garantimos suporte em {c["resp_time"]}. Cada contrato inclui o que a operação industrial exige.',
        'incluso_items': [
            ('M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z',
             f'Manutenção preventiva e corretiva em {c["name"]}',
             f'Técnico mobile se desloca até {c["pole1"]} ou qualquer ponto de {c["name"]} em {c["resp_time"]}. Revisão programada a cada 250 horas de operação.'),
            ('M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
             f'Seguro e documentação inclusa',
             f'Seguro contra danos durante operação. Toda documentação (ART, laudo de inspeção, manual) entregue junto com o equipamento em {c["name"]}.'),
            ('M13 10V3L4 14h7v7l9-11h-7z',
             f'Entrega {c["delivery"]} pela {c["rod"]}',
             f'Equipamento sai da base em Goiânia e chega em {c["name"]} ({c["dist"]}km) {c["delivery"]}. Para urgências, antecipamos mediante disponibilidade.'),
            ('M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z',
             'Suporte técnico 24 horas',
             f'Qualquer problema durante a operação em {c["name"]}: ligue e o técnico vai até o local. Sem limite de chamados durante o contrato.'),
            ('M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2',
             f'Consultoria técnica para {c["name"]}',
             f'Avaliação gratuita do terreno e condições de operação no {c["pole1"]} e {c["pole2"] or c["bairro1"]}. Recomendação do modelo ideal antes da contratação.'),
            ('M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0',
             f'Treinamento básico na entrega',
             f'Na primeira entrega em {c["name"]}, o operador recebe instrução sobre controles, segurança e inspeção pré-operacional. Certificação NR-35 indicada separadamente.'),
        ],
        'expert': f'Em {c["name"]}, o {c["pole1"]} é um dos maiores clientes da Move. A articulada de 15 metros contorna as estruturas industriais e posiciona o operador no ponto exato sem montar andaime. Para galpões de {c["setor1"]} com restrição de emissão, a elétrica resolve. Estamos a {c["dist"]}km pela {c["rod"]} — nosso técnico chega em {c["resp_time"]}. Isso faz diferença quando o equipamento precisa de calibração no meio do serviço',
        'cta': f'Alugue plataforma articulada em {c["name"]}',
        'coverage_cities': 'Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas',
        'service_key': 'articulada',
        'fleet_models': [
            {'name': 'Articulada 12m Elétrica', 'badge': 'Mais alugada',
             'subtitle': f'Para galpões fechados do {c["pole1"]}',
             'desc': f'Modelo elétrico com 12 metros de altura e 6 metros de alcance lateral para operações internas em {c["name"]}. Bateria de lítio com autonomia de 8 horas. Zero emissão para galpões de {c["setor1"]} onde contaminação por gases é proibida. Pneus não marcantes para pisos industriais do {c["pole1"]}.',
             'specs': [('Altura', 'Até 12 metros'), ('Alcance lateral', '6 metros'), ('Cesto', '230-250 kg')]},
            {'name': 'Articulada 12m Diesel', 'badge': 'Versátil',
             'subtitle': f'Para pátios do {c["pole1"]} e {c["pole2"] or c["bairro1"]}',
             'desc': f'Articulada diesel de 12 metros com tração 4x4 para os pátios irregulares do {c["pole1"]}. Opera em cascalho, terra compactada e rampas entre galpões de {c["name"]}. Estabilizadores hidráulicos nivelam em desníveis. Torque para se deslocar entre estruturas sem reboque.',
             'specs': [('Altura', 'Até 12 metros'), ('Alcance lateral', '6 metros'), ('Tração', '4x4 diesel')]},
            {'name': 'Articulada 15m Diesel', 'badge': 'Premium',
             'subtitle': f'Para estruturas de grande porte em {c["name"]}',
             'desc': f'Articulada diesel de 15 metros — maior alcance da frota — para estruturas industriais de grande porte no {c["pole1"]}. Braço contorna tubulações e equipamentos com 8 metros de deslocamento lateral. Para coberturas de galpões com mais de 12 metros de pé-direito em {c["name"]}.',
             'specs': [('Altura', 'Até 15 metros'), ('Alcance lateral', '8 metros'), ('Tração', '4x4 diesel')]},
        ],
        'compare': {
            'alt_name': 'Plataforma Tesoura',
            'equip_desc': f'Para estruturas com obstáculos no {c["pole1"]}',
            'alt_desc': f'Para elevação vertical em galpões de {c["name"]}',
            'intro': f'No {c["pole1"]} de {c["name"]}, a escolha entre articulada e tesoura define se a manutenção será feita em 2 dias ou em 2 semanas.',
            'equip_pros': [
                f'Alcance lateral de 6 a 8m — contorna estruturas no {c["pole1"]}',
                f'Tração 4x4 diesel para pátios irregulares de {c["name"]}',
                'Cesto rotativo 360° para ajuste fino de posição',
                f'Navega sobre pontes rolantes e tubulações sem desmontagem',
            ],
            'equip_cons': [f'Plataforma menor que a tesoura (2 operadores max)'],
            'alt_pros': [
                'Plataforma ampla: até 4 operadores com materiais',
                'Custo de locação inferior à articulada',
                f'Estabilidade superior para trabalhos com ferramentas pesadas',
            ],
            'alt_cons': [
                f'Zero alcance lateral: não contorna estruturas no {c["pole1"]}',
                f'Não alcança pontos atrás de equipamentos industriais',
                'Exige piso nivelado para operação segura',
            ],
            'verdict': f'Se o trabalho no {c["pole1"]} exige acessar pontos atrás de estruturas, tubulações ou equipamentos, a articulada é obrigatória. A tesoura resolve quando o acesso é vertical direto, sem obstáculos entre o solo e o ponto de trabalho.',
        },
        'price': {
            'cards': [
                {'name': 'Articulada 12m Elétrica', 'sub': f'Galpões fechados em {c["name"]}', 'price': '2.800', 'highlight': True,
                 'items': [f'Ideal para {c["setor1"]} no {c["pole1"]}', 'Zero emissão, pneus não marcantes', '12m altura + 6m alcance lateral', f'Manutenção em {c["name"]} inclusa', 'Suporte técnico 24h']},
                {'name': 'Articulada 12m Diesel 4x4', 'sub': f'Pátios e canteiros em {c["name"]}', 'price': '3.200',
                 'items': [f'Pátios do {c["pole1"]} e {c["pole2"] or c["bairro1"]}', 'Tração 4x4 para terreno irregular', '12m altura + 6m alcance lateral', f'Entrega {c["delivery"]} via {c["rod"]}', 'Manutenção + suporte 24h']},
                {'name': 'Articulada 15m Diesel 4x4', 'sub': f'Estruturas de grande porte', 'price': '4.000',
                 'items': [f'Estruturas industriais do {c["pole1"]}', '15m altura + 8m alcance lateral máximo', 'Tração 4x4 para qualquer terreno', f'Consultoria técnica para {c["name"]} inclusa', 'Reposição emergencial em caso de parada']},
            ],
            'note': f'A conta real para {c["name"]}: montar andaime em galpão do {c["pole1"]} custa R$ 15.000 a R$ 25.000 com 3-5 dias de montagem. A articulada chega {c["delivery"]} e opera no mesmo dia. Para manutenções trimestrais, o contrato mensal de R$ 2.800 a R$ 4.500 se paga na primeira semana.',
        },
        'nr': {
            'norma': 'NR-35',
            'intro': f'A NR-35 estabelece requisitos para trabalho em altura acima de 2 metros. No {c["pole1"]} de {c["name"]}, o cumprimento é obrigatório e fiscalizado.',
            'epi': f'Capacete com jugular, cinto paraquedista com trava-quedas, luvas e calçado de segurança. Ancoragens do cesto verificadas antes de cada operação no {c["pole1"]}.',
        },
    }


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def content_tesoura(c):
    bridge = c['bridges'].get('plataforma_tesoura', f'manutenção interna de galpões no {c["pole1"]}')
    return {
        'title': f'Aluguel de Plataforma Tesoura em {c["name"]} | Move Máquinas',
        'desc': f'Plataforma tesoura em {c["name"]}: elétrica para galpões do {c["pole1"]}, diesel para pátios. 8 a 15m, entrega {c["delivery"]}. Manutenção inclusa. Move Máquinas.',
        'og': f'Plataforma tesoura 8-15m em {c["name"]}. {c["pole1"]}, {c["bairro1"]}. Manutenção inclusa.',
        'breadcrumb': f'Plataforma Tesoura em {c["name"]}',
        'service_type': 'Locação de Plataforma Elevatória Tesoura',
        'price_range': 'R$2.200 - R$3.800',
        'wa_subject': 'plataforma tesoura',
        'equip_short': 'plataforma tesoura',
        'h1': f'Aluguel de Plataforma<br>Tesoura em {c["name"]}',
        'hero_sub': f'{bridge.capitalize()}. Modelos elétricos de 8 a 10m e diesel de 12 a 15m. Manutenção inclusa.',
        'h2s': [
            f'Entenda o que é <span>plataforma tipo tesoura</span> antes de alugar',
            f'Qual <span>plataforma tesoura</span> é ideal para {c["name"]}?',
            f'Comparativo: <span>plataforma pantográfica</span> vs articulada',
            f'Investimento mensal na locação de <span>plataforma tesoura</span>',
            f'Setores que mais usam <span>tesoura elétrica</span> em {c["name"]}',
            f'Tudo que acompanha o aluguel de <span>tesoura</span> em {c["name"]}',
            f'O que a <span>NR-35</span> exige para operar tesoura em {c["name"]}',
            f'O que dizem as empresas que alugaram <span>tesoura</span> em {c["name"]}',
            f'Entrega rápida em <span>{c["name"]}</span> e cidades vizinhas',
            f'Respostas sobre <span>plataforma tesoura</span> em {c["name"]}',
        ],
        'oque': f'A plataforma tesoura utiliza mecanismo pantográfico para elevação estritamente vertical, oferecendo uma plataforma de trabalho ampla e estável — ideal para operações em pisos nivelados. Em {c["name"]}, o {c["pole1"]} concentra galpões de {c["setor1"]} e {c["setor2"]} que demandam manutenção contínua de iluminação, climatização e forros. A versão elétrica opera sem emissão em ambientes internos controlados, enquanto o diesel atende pátios e áreas externas. {c["pain"]} A {c["dist"]}km de Goiânia pela {c["rod"]}, a entrega é {c["delivery"]}.',
        'h3s': [
            (f'Manutenção interna nos galpões do {c["pole1"]}',
             f'O {c["pole1"]} de {c["name"]} concentra galpões com pé-direito de 8 a 12 metros. A tesoura elétrica acessa forros, luminárias e sistemas de climatização com plataforma ampla para dois operadores trabalharem lado a lado. Bateria de lítio com autonomia de 8 horas e pneus não marcantes para pisos industriais. No setor de {c["setor1"]}, a zero emissão é requisito obrigatório.'),
            (f'Diesel para pátios, elétrica para ambientes fechados',
             f'Nos pátios do {c["pole1"]} e áreas externas de {c["name"]}, o modelo diesel com estabilizadores hidráulicos nivela em terrenos de cascalho e asfalto irregular. Dentro dos galpões onde {c["setor1"]} opera com controle de emissão, a tesoura elétrica é obrigatória. No {c["pole2"] or c["bairro1"]}, a demanda é mista entre diesel e elétrica.'),
            (f'Quem mais contrata tesoura em {c["name"]}',
             f'As indústrias de {c["setor1"]} lideram a contratação de tesouras em {c["name"]}, seguidas por {c["setor2"]} e construção civil. O {c["pole1"]} programa manutenções preventivas de iluminação e climatização a cada trimestre. Prédios comerciais de {c["bairro1"]} contratam para instalação de ar-condicionado e pintura de tetos. {c["pain"]}'),
        ],
        'checklist': [
            f'<strong>Plataforma ampla (1,5 a 2,5m):</strong> espaço para dois operadores com ferramentas e materiais nos galpões do {c["pole1"]}.',
            f'<strong>Zero emissão (elétrica):</strong> obrigatória em galpões de {c["setor1"]} com controle de qualidade do ar em {c["name"]}.',
            f'<strong>Estabilizadores hidráulicos:</strong> nivelam em desníveis de até 10° nos pátios entre galpões do {c["pole1"]}.',
            f'<strong>Bateria de lítio:</strong> autonomia de 8 horas por carga, recarga em 2-3 horas entre turnos.',
        ],
        'apps': [
            (f'{c["pole1"]}: iluminação e climatização',
             f'Troca de luminárias LED, manutenção de dutos de climatização e reparo de forros nos galpões do {c["pole1"]}. Tesoura elétrica para ambientes internos controlados. Plataforma ampla para dois operadores.',
             'https://images.pexels.com/photos/1267338/pexels-photo-1267338.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Galpão industrial no {c["pole1"]} de {c["name"]}'),
            (f'{c["pole2"] or c["bairro1"]}: galpões e armazéns',
             f'Manutenção de coberturas, sprinklers e instalações elétricas no {c["pole2"] or c["bairro1"]}. Tesoura diesel para pátios externos com estabilizadores.',
             'https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Galpão de armazenagem no {c["pole2"] or c["bairro1"]} em {c["name"]}'),
            (f'{c["bairro1"]}: prédios comerciais',
             f'Pintura de tetos, instalação de ar-condicionado central e manutenção de forros em prédios comerciais de {c["bairro1"]}. Tesoura elétrica para ambientes internos.',
             'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Prédio comercial em {c["bairro1"]}, {c["name"]}'),
            (f'{c["rod"]}: obras industriais',
             f'Novas indústrias ao longo da {c["rod"]} demandam tesouras para instalação de forros, sistemas elétricos e acabamentos internos em galpões novos.',
             'https://images.pexels.com/photos/4481259/pexels-photo-4481259.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Obra industrial na {c["rod"]} próxima a {c["name"]}'),
        ],
        'tests': [
            (f'Troca de luminárias LED em galpão de {c["setor1"]} no {c["pole1"]}. A tesoura elétrica de 10m acessou todos os pontos do forro sem mover linhas de produção. Fizemos em um turno sem parar a fábrica. A plataforma ampla coube dois eletricistas trabalhando lado a lado.',
             'Marina S.', f'Coord. Manutenção, {c["pole1"]}, {c["name"]}-GO (jan/2026)'),
            (f'Manutenção de sprinklers em 2 galpões do {c["pole2"] or c["bairro1"]}. A tesoura diesel nivelou nos estabilizadores no cascalho do pátio. A Move entregou em {c["resp_time"]} — estão a {c["dist"]}km. Suporte rápido quando precisamos.',
             'Pedro H.', f'Gerente Industrial, {c["pole2"] or c["bairro1"]}, {c["name"]}-GO (nov/2025)'),
            (f'Instalação de forro isolante em câmara de temperatura controlada. A tesoura de 8m coube no espaço entre as estantes e deu espaço para 2 instaladores com as placas. Terminamos antes do prazo. Contrato renovado.',
             'Juliana R.', f'Engenheira, Ind. {c["setor2"].title()}, {c["name"]}-GO (mar/2026)'),
        ],
        'faqs': [
            (f'Qual tesoura usar nos galpões do {c["pole1"]}?',
             f'Elétrica 8-10m para pisos nivelados internos. Zero emissão para galpões de {c["setor1"]}. Pneus não marcantes para pisos industriais.'),
            (f'Em quanto tempo entregam em {c["name"]}?',
             f'Entrega {c["delivery"]} — {c["dist"]}km via {c["rod"]}. Equipamento pronto para operar em {c["resp_time"]}.'),
            (f'Quanto custa alugar tesoura em {c["name"]}?',
             f'R$ 2.200 a R$ 3.800/mês dependendo do modelo e prazo. {"Entrega sem custo." if c["dist"]<=30 else "Frete incluso."} Manutenção e suporte 24h inclusos.'),
            (f'A diesel opera nos pátios do {c["pole1"]}?',
             f'Sim. Estabilizadores hidráulicos nivelam em cascalho, asfalto irregular e desníveis de até 10° entre galpões.'),
            (f'Preciso de NR-35 para operar no {c["pole1"]}?',
             f'Sim. NR-35 obrigatória. No {c["pole1"]}, a fiscalização é rigorosa. A Move oferece indicação de parceiros para certificação.'),
            (f'Vocês atendem {c["bairro1"]} e {c["bairro2"]}?',
             f'Sim. {c["pole1"]}, {c["pole2"] or ""}, {c["bairro1"]}, {c["bairro2"]} e toda a zona industrial de {c["name"]}.'),
            (f'Tesoura ou articulada para galpões com obstruções?',
             f'Caminho vertical livre (forro, luminárias): tesoura. Obstruções no caminho (tubulações, pontes rolantes): articulada.'),
            (f'A elétrica funciona em ambientes com restrição de emissão?',
             f'Sim. Zero gases, operação silenciosa, pneus não marcantes. Requisito para galpões de {c["setor1"]} e {c["setor2"]}.'),
        ],
        'expert': f'No {c["pole1"]} de {c["name"]}, a tesoura elétrica virou item obrigatório para manutenção trimestral. As indústrias de {c["setor1"]} programam troca de luminárias e revisão de climatização a cada 90 dias. A tesoura é o único equipamento que opera internamente sem comprometer a qualidade do ar. Já tivemos caso de galpão que usou andaime e precisou parar 3 dias para limpar a contaminação de partículas',
        'incluso_sub': f'A {c["dist"]}km via {c["rod"]}, garantimos suporte em {c["resp_time"]}. Cada contrato de tesoura inclui:',
        'incluso_items': [
            ('M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z',
             f'Manutenção preventiva e corretiva em {c["name"]}',
             f'Técnico mobile em {c["resp_time"]}. Revisão programada a cada 250h de operação.'),
            ('M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
             'Seguro e documentação inclusa',
             f'Seguro contra danos, ART, laudo de inspeção e manual entregues junto com o equipamento.'),
            ('M13 10V3L4 14h7v7l9-11h-7z',
             f'Entrega {c["delivery"]} pela {c["rod"]}',
             f'Equipamento sai de Goiânia e chega em {c["name"]} ({c["dist"]}km) {c["delivery"]}.'),
            ('M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z',
             'Suporte técnico 24 horas',
             f'Qualquer problema em {c["name"]}: técnico no local em {c["resp_time"]}.'),
            ('M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2',
             f'Consultoria técnica para {c["name"]}',
             f'Avaliação do terreno e condições de operação no {c["pole1"]}. Recomendação gratuita do modelo ideal.'),
            ('M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0',
             'Treinamento básico na entrega',
             f'Instrução sobre controles, segurança e inspeção na primeira entrega em {c["name"]}.'),
        ],
        'cta': f'Alugue plataforma tesoura em {c["name"]}',
        'coverage_cities': 'Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas',
        'service_key': 'tesoura',
        'fleet_models': [
            {'name': 'Tesoura 8m Elétrica', 'badge': 'Compacta',
             'subtitle': f'Para galpões internos do {c["pole1"]}',
             'desc': f'Tesoura elétrica compacta de 8 metros para manutenção de forros, luminárias e climatização nos galpões de {c["setor1"]} em {c["name"]}. Plataforma de 1,5m para dois operadores. Pneus não marcantes.',
             'specs': [('Altura', 'Até 8 metros'), ('Plataforma', '1,5 x 0,8m'), ('Carga', '350 kg')]},
            {'name': 'Tesoura 10m Elétrica', 'badge': 'Mais alugada',
             'subtitle': f'Para galpões maiores em {c["name"]}',
             'desc': f'Modelo elétrico de 10 metros — o mais contratado para galpões com pé-direito elevado no {c["pole1"]}. Plataforma ampla de 2,5m para trabalhos que exigem mais espaço. Bateria de lítio com autonomia de 8 horas.',
             'specs': [('Altura', 'Até 10 metros'), ('Plataforma', '2,5 x 1,2m'), ('Carga', '450 kg')]},
            {'name': 'Tesoura 12m Diesel', 'badge': 'Versátil',
             'subtitle': f'Para pátios e áreas externas',
             'desc': f'Tesoura diesel de 12 metros com estabilizadores hidráulicos para pátios do {c["pole1"]} e obras externas em {c["name"]}. Tração para cascalho e asfalto irregular.',
             'specs': [('Altura', 'Até 12 metros'), ('Plataforma', '2,5 x 1,2m'), ('Tração', 'Diesel')]},
            {'name': 'Tesoura 15m Diesel', 'badge': 'Premium',
             'subtitle': f'Para estruturas elevadas',
             'desc': f'Maior alcance da linha tesoura — 15 metros para coberturas de galpões de grande porte no {c["pole1"]} e estruturas industriais em {c["name"]}.',
             'specs': [('Altura', 'Até 15 metros'), ('Plataforma', '2,5 x 1,5m'), ('Tração', 'Diesel 4x4')]},
        ],
        'compare': {
            'alt_name': 'Plataforma Articulada',
            'equip_desc': f'Para elevação vertical estável no {c["pole1"]}',
            'alt_desc': f'Para contornar obstáculos em {c["name"]}',
            'intro': f'No {c["pole1"]}, a escolha certa entre tesoura e articulada evita mobilização dupla e custo desnecessário.',
            'equip_pros': [
                f'Plataforma ampla: até 4 operadores nos galpões do {c["pole1"]}',
                'Custo de locação 20-30% inferior à articulada',
                f'Estabilidade superior para ferramentas pesadas em {c["name"]}',
                'Modelos elétricos com zero emissão para ambientes controlados',
            ],
            'equip_cons': [f'Zero alcance lateral: não contorna estruturas'],
            'alt_pros': [
                f'Alcance lateral de 6-8m para contornar obstáculos no {c["pole1"]}',
                'Cesto rotativo 360° para posicionamento preciso',
                f'Tração 4x4 para terrenos irregulares em {c["name"]}',
            ],
            'alt_cons': [
                'Plataforma menor (2 operadores máximo)',
                'Custo 20-30% superior à tesoura',
                'Menos estável para ferramentas pesadas',
            ],
            'verdict': f'Se o caminho até o ponto de trabalho no {c["pole1"]} é vertical e direto (forro, luminárias, sprinklers), a tesoura é a melhor opção. Se há obstruções (tubulações, pontes rolantes), a articulada contorna.',
        },
        'price': {
            'cards': [
                {'name': 'Tesoura 8-10m Elétrica', 'sub': f'Galpões do {c["pole1"]}', 'price': '2.200', 'highlight': True,
                 'items': [f'Ideal para {c["setor1"]}', 'Zero emissão, pneus não marcantes', 'Plataforma ampla (2 operadores)', f'Manutenção em {c["name"]} inclusa']},
                {'name': 'Tesoura 12m Diesel', 'sub': f'Pátios e áreas externas', 'price': '2.800',
                 'items': [f'Pátios do {c["pole1"]}', 'Estabilizadores para terreno irregular', f'Entrega {c["delivery"]}', 'Suporte 24h']},
                {'name': 'Tesoura 15m Diesel', 'sub': 'Coberturas de grande porte', 'price': '3.800',
                 'items': ['Maior alcance da linha tesoura', 'Tração diesel 4x4', f'Para galpões elevados em {c["name"]}', 'Consultoria técnica inclusa']},
            ],
            'note': f'Para {c["name"]}: a tesoura elétrica de R$ 2.200/mês substitui o andaime que custaria R$ 8.000+ por montagem. Para manutenções trimestrais no {c["pole1"]}, o contrato mensal se paga na primeira semana de operação.',
        },
        'nr': {
            'norma': 'NR-35',
            'intro': f'A NR-35 estabelece requisitos para trabalho em altura. No {c["pole1"]} de {c["name"]}, o cumprimento é obrigatório.',
        },
    }


def content_combustao(c):
    bridge = c['bridges'].get('empilhadeira_combustao', f'movimentação de cargas nos galpões do {c["pole1"]}')
    return {
        'title': f'Aluguel de Empilhadeira Combustão em {c["name"]} | Move Máquinas',
        'desc': f'Empilhadeira a combustão Clark em {c["name"]}: GLP e diesel, 2 a 8 ton. {c["pole1"]}, logística, distribuição. Entrega {c["delivery"]}. Manutenção inclusa.',
        'og': f'Empilhadeira Clark combustão em {c["name"]}. 2-8 ton. {c["pole1"]}. Manutenção inclusa.',
        'breadcrumb': f'Empilhadeira Combustão em {c["name"]}',
        'service_type': 'Locação de Empilhadeira a Combustão',
        'price_range': 'R$2.800 - R$5.000',
        'wa_subject': 'empilhadeira combustão',
        'equip_short': 'empilhadeira a combustão',
        'h1': f'Aluguel de Empilhadeira<br>a Combustão em {c["name"]}',
        'hero_sub': f'{bridge.capitalize()}. Clark GLP e diesel de 2.000 a 8.000 kg com manutenção inclusa.',
        'h2s': [
            f'Entenda o que é <span>empilhadeira GLP/diesel</span> antes de alugar',
            f'Qual <span>empilhadeira Clark</span> escolher para {c["name"]}?',
            f'Comparativo: <span>empilhadeira combustão</span> vs elétrica',
            f'Investimento na locação de <span>empilhadeira industrial</span>',
            f'Setores que mais usam <span>empilhadeira combustão</span> em {c["name"]}',
            f'Tudo que acompanha o aluguel de <span>empilhadeira Clark</span>',
            f'O que a <span>NR-11</span> exige para operar empilhadeira em {c["name"]}',
            f'O que dizem as empresas que alugaram <span>empilhadeira</span> em {c["name"]}',
            f'Entrega rápida em <span>{c["name"]}</span> e cidades vizinhas',
            f'Respostas sobre <span>empilhadeira GLP/diesel</span> em {c["name"]}',
        ],
        'oque': f'A empilhadeira a combustão Clark opera com motor GLP ou diesel para movimentação de cargas de 2.000 a 8.000 kg. Em {c["name"]}, com economia baseada em {c["eco"]}, o {c["pole1"]} gera demanda constante para operações de carga e descarga em armazéns, docas e pátios. A versão GLP é preferida em armazéns com ventilação natural, enquanto o diesel domina em pátios externos e carga pesada. {c["pain"]} A {c["dist"]}km de Goiânia pela {c["rod"]}, a entrega é {c["delivery"]}.',
        'h3s': [
            (f'Operações de carga no {c["pole1"]} de {c["name"]}',
             f'O {c["pole1"]} concentra indústrias de {c["setor1"]} e {c["setor2"]} que movimentam paletes diariamente. As empilhadeiras GLP Clark S25/30/35 operam em corredores de armazéns, enquanto os modelos diesel C60/70/80 atendem cargas pesadas em pátios. A manutenção inclusa da Move garante que nenhuma empilhadeira pare durante o expediente — técnico mobile em {c["resp_time"]}.'),
            (f'GLP para armazéns, diesel para pátios em {c["name"]}',
             f'No {c["pole1"]}, 60% dos contratos são GLP para armazéns fechados com ventilação, e 40% diesel para pátios e carga pesada. A troca de cilindro GLP leva 3 minutos — a operação não para. Nos pátios externos, o diesel oferece torque para rampas e terrenos irregulares. A escolha depende do ambiente: interno com ventilação = GLP, externo ou carga acima de 5 ton = diesel.'),
            (f'Distribuição e logística: o motor de {c["name"]}',
             f'Na {c["rod"]} e nas áreas logísticas de {c["name"]}, centros de distribuição e atacadistas movimentam paletes em docas abertas e pátios de manobra. A empilhadeira GLP opera sem depender de tomada de recarga — troca o cilindro e volta a operar. Para operações em turnos, a combustão é a escolha por produtividade contínua. {c["pain"]}'),
        ],
        'checklist': [
            f'<strong>Capacidade de 2 a 8 toneladas:</strong> frota Clark completa para qualquer operação no {c["pole1"]} de {c["name"]}.',
            f'<strong>GLP (troca em 3 min):</strong> operação contínua em armazéns de {c["setor1"]} e {c["setor2"]} sem pausa para recarga.',
            f'<strong>Diesel para carga pesada:</strong> torque para rampas, pátios irregulares e cargas acima de 5 toneladas.',
            f'<strong>Raio de giro compacto:</strong> manobra em corredores de 3,5m nos armazéns do {c["pole1"]}.',
        ],
        'apps': [
            (f'{c["pole1"]}: armazéns e produção',
             f'Movimentação de paletes em armazéns de {c["setor1"]} e {c["setor2"]} no {c["pole1"]}. GLP Clark S25/30/35 em corredores de estoque. Manutenção preventiva programada para zero parada.',
             'https://images.pexels.com/photos/1267338/pexels-photo-1267338.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Armazém industrial no {c["pole1"]} de {c["name"]}'),
            (f'{c["pole2"] or c["bairro1"]}: logística e distribuição',
             f'Carga e descarga em docas e pátios do {c["pole2"] or c["bairro1"]}. Diesel para carga pesada, GLP para operações mistas.',
             'https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Centro de distribuição em {c["name"]}'),
            (f'{c["bairro1"]}: comércio e atacado',
             f'Operação em centros de distribuição e atacadistas de {c["bairro1"]}. GLP para áreas semi-fechadas. Modelos de 2.500 a 3.500 kg.',
             'https://images.pexels.com/photos/4481259/pexels-photo-4481259.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Atacadista em {c["bairro1"]}, {c["name"]}'),
            (f'{c["rod"]}: cross-docking e transbordo',
             f'Operações em terminais ao longo da {c["rod"]}. Empilhadeiras robustas para operação contínua em pátios abertos.',
             'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Terminal logístico na {c["rod"]} próxima a {c["name"]}'),
        ],
        'tests': [
            (f'Operamos 6 empilhadeiras GLP no armazém do {c["pole1"]}. Troca de cilindro em 3 minutos, operação contínua. Quando uma máquina apresentou vibração, o técnico da Move chegou em {c["resp_time"]} e resolveu no local. Zero parada não programada.',
             'Henrique A.', f'Gerente Logística, {c["pole1"]}, {c["name"]}-GO (jan/2026)'),
            (f'Movimentamos 400 paletes por turno com as empilhadeiras diesel no {c["pole2"] or c["bairro1"]}. A C70 sustenta carga pesada sem oscilar. Contrato com manutenção inclusa é o que faz a conta fechar.',
             'Luciana T.', f'Coord. Operações, {c["pole2"] or c["bairro1"]}, {c["name"]}-GO (nov/2025)'),
            (f'Centro de distribuição na {c["rod"]}, 2 turnos diários. A GTS30 da Clark é a mais equilibrada — raio de giro curto e potência para rampa de doca com 3 toneladas.',
             'Marcos V.', f'Operador Líder, CD {c["rod"]}, {c["name"]}-GO (fev/2026)'),
        ],
        'faqs': [
            (f'Qual empilhadeira usar no {c["pole1"]}?',
             f'GLP Clark S25/30/35 para armazéns (2.500-3.500 kg). Diesel C60/70/80 para carga pesada em pátios (6-8 ton).'),
            (f'Em quanto tempo entregam em {c["name"]}?',
             f'Entrega {c["delivery"]} — {c["dist"]}km via {c["rod"]}. Equipamento revisado e pronto para operar.'),
            (f'Quanto custa alugar empilhadeira em {c["name"]}?',
             f'R$ 2.800 a R$ 5.000/mês dependendo da capacidade. {"Entrega sem custo." if c["dist"]<=30 else "Frete incluso."} Manutenção 24h inclusa.'),
            (f'GLP ou diesel para {c["pole1"]}?',
             f'GLP para armazéns fechados com ventilação (sem fuligem). Diesel para pátios e carga pesada. No {c["pole1"]}, 60% GLP e 40% diesel.'),
            (f'Preciso de NR-11 no {c["pole1"]}?',
             f'Sim. NR-11 obrigatória. A Move oferece <a href="/{c["slug"]}/curso-de-operador-de-empilhadeira" style="color:var(--color-primary)">curso NR-11 em {c["name"]}</a>.'),
            (f'A manutenção é feita em {c["name"]}?',
             f'Sim. Técnico mobile no {c["pole1"]} ou qualquer ponto de {c["name"]} em {c["resp_time"]}. Preventiva + corretiva incluídas.'),
            (f'Vocês atendem operação em 2-3 turnos?',
             f'Sim. Manutenção programada nos intervalos. Reposição emergencial em caso de parada.'),
            (f'Qual a capacidade máxima?',
             f'Clark C80 com 8.000 kg e mastro triplex. Diesel para pátios irregulares.'),
        ],
        'expert': f'Em {c["name"]}, o {c["pole1"]} consome empilhadeira como matéria-prima. São indústrias de {c["setor1"]} e {c["setor2"]} movimentando paletes o dia inteiro. A GLP Clark é a preferida nos armazéns — troca cilindro em 3 minutos. No pátio, diesel C70 para carga pesada. Nosso diferencial é a manutenção mobile: o técnico chega em {c["resp_time"]} porque estamos a {c["dist"]}km',
        'incluso_sub': f'A {c["dist"]}km via {c["rod"]}, suporte em {c["resp_time"]}. Cada contrato inclui:',
        'incluso_items': [
            ('M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z',
             f'Manutenção preventiva e corretiva em {c["name"]}', f'Técnico mobile em {c["resp_time"]}. Revisão a cada 250h.'),
            ('M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
             'Seguro e documentação', 'Seguro contra danos, ART e laudo de inspeção incluídos.'),
            ('M13 10V3L4 14h7v7l9-11h-7z',
             f'Entrega {c["delivery"]}', f'Equipamento de Goiânia a {c["name"]} ({c["dist"]}km) {c["delivery"]}.'),
            ('M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z',
             'Suporte 24h', f'Técnico no local em {c["resp_time"]}.'),
            ('M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2',
             'Consultoria técnica', f'Avaliação gratuita da operação no {c["pole1"]}.'),
            ('M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0',
             'Treinamento básico', f'Instrução ao operador na entrega em {c["name"]}.'),
        ],
        'cta': f'Alugue empilhadeira a combustão em {c["name"]}',
        'coverage_cities': 'Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas',
        'service_key': 'combustao',
        'fleet_models': [
            {'name': 'Clark S25/30/35', 'badge': 'Mais alugada', 'subtitle': f'GLP para armazéns do {c["pole1"]}',
             'desc': f'Empilhadeira GLP Clark série S com 2.500 a 3.500 kg. Raio de giro compacto para corredores de 3,5m nos armazéns de {c["setor1"]} em {c["name"]}. Troca de cilindro em 3 minutos.',
             'specs': [('Capacidade', '2.500-3.500 kg'), ('Combustível', 'GLP'), ('Raio de giro', 'Reduzido')]},
            {'name': 'Clark GTS25/30/33', 'badge': 'Tecnológica', 'subtitle': 'Ergonomia e tecnologia',
             'desc': f'Série GTS com tecnologia de ponta para operações intensivas. Cabine ergonômica, controles intuitivos e menor consumo de GLP. Para operações de alto giro no {c["pole1"]}.',
             'specs': [('Capacidade', '2.500-3.300 kg'), ('Combustível', 'GLP'), ('Tecnologia', 'Inteligente')]},
            {'name': 'Clark C60/70/80', 'badge': 'Heavy Duty', 'subtitle': f'Diesel para carga pesada',
             'desc': f'Empilhadeira diesel heavy duty de 6.000 a 8.000 kg para operações de carga pesada em pátios do {c["pole1"]} e terminais na {c["rod"]}. Mastro triplex para empilhar a 2 níveis.',
             'specs': [('Capacidade', '6.000-8.000 kg'), ('Combustível', 'Diesel'), ('Mastro', 'Triplex')]},
            {'name': 'Clark S40-60', 'badge': 'Versátil', 'subtitle': 'Carga média-pesada',
             'desc': f'Empilhadeira de 4.000 a 6.000 kg para operações que exigem mais capacidade que a série S25. Diesel ou GLP. Para indústrias de {c["setor2"]} em {c["name"]}.',
             'specs': [('Capacidade', '4.000-6.000 kg'), ('Combustível', 'GLP ou Diesel'), ('Raio de giro', 'Reduzido')]},
        ],
        'compare': {
            'alt_name': 'Empilhadeira Elétrica',
            'equip_desc': f'Para operações intensivas no {c["pole1"]}',
            'alt_desc': f'Para ambientes fechados em {c["name"]}',
            'intro': f'No {c["pole1"]} de {c["name"]}, a escolha entre combustão e elétrica define produtividade e custo.',
            'equip_pros': [
                'Troca de cilindro GLP em 3 min (sem pausa para recarga)',
                f'Torque para rampas e pátios irregulares em {c["name"]}',
                'Capacidade de até 8.000 kg (diesel)',
                'Opera em ambientes abertos sem limitação',
            ],
            'equip_cons': ['Emissão de gases (GLP) — requer ventilação', 'Custo de combustível vs eletricidade'],
            'alt_pros': [
                'Zero emissão — opera em ambientes fechados',
                'Custo de energia menor que GLP/diesel',
                'Operação silenciosa',
            ],
            'alt_cons': [
                'Recarga de 6-8 horas (pausa na operação)',
                'Capacidade máxima menor (geralmente até 3.500 kg)',
                'Não opera em terrenos irregulares',
            ],
            'verdict': f'Para operações em {c["name"]} com turnos contínuos, carga acima de 3,5 ton ou pátios irregulares: combustão. Para armazéns fechados sem ventilação ou operações leves: elétrica.',
        },
        'price': {
            'cards': [
                {'name': 'GLP S25/30/35', 'sub': f'Armazéns do {c["pole1"]}', 'price': '2.800', 'highlight': True,
                 'items': ['2.500-3.500 kg', f'Para {c["setor1"]}', 'Troca de cilindro em 3 min', f'Manutenção em {c["name"]}']},
                {'name': 'GLP/Diesel S40-60', 'sub': 'Carga média-pesada', 'price': '3.500',
                 'items': ['4.000-6.000 kg', f'Para {c["setor2"]}', f'Entrega {c["delivery"]}', 'Suporte 24h']},
                {'name': 'Diesel C60/70/80', 'sub': 'Heavy Duty', 'price': '5.000',
                 'items': ['6.000-8.000 kg', 'Mastro triplex', f'Pátios do {c["pole1"]}', 'Reposição emergencial']},
            ],
            'note': f'Para {c["name"]}: uma empilhadeira parada no armazém do {c["pole1"]} custa mais que o aluguel mensal em produção perdida. Com manutenção inclusa, técnico em {c["resp_time"]}. Zero surpresa no orçamento.',
        },
        'nr': {'norma': 'NR-11', 'intro': f'A NR-11 regula operação de empilhadeiras em {c["name"]}. No {c["pole1"]}, certificação é obrigatória.'},
    }


def content_transpaleteira(c):
    bridge = c['bridges'].get('transpaleteira', f'movimentação de paletes no {c["pole1"]}')
    return {
        'title': f'Aluguel de Transpaleteira Elétrica em {c["name"]} | Move Máquinas',
        'desc': f'Transpaleteira elétrica Clark em {c["name"]}: lítio 24V para {c["pole1"]}, patolada para logística. 5 modelos, entrega {c["delivery"]}. Manutenção inclusa.',
        'og': f'Transpaleteira Clark lítio em {c["name"]}. {c["pole1"]}. Manutenção 24h inclusa.',
        'breadcrumb': f'Transpaleteira em {c["name"]}',
        'service_type': 'Locação de Transpaleteira Elétrica',
        'price_range': 'R$1.200 - R$2.200',
        'wa_subject': 'transpaleteira elétrica',
        'equip_short': 'transpaleteira elétrica',
        'h1': f'Aluguel de Transpaleteira<br>Elétrica em {c["name"]}',
        'hero_sub': f'{bridge.capitalize()}. Clark lítio 24V com 5 modelos disponíveis.',
        'h2s': [
            f'Entenda o que é <span>patolinha elétrica</span> antes de alugar',
            f'Qual <span>paleteira elétrica</span> escolher em {c["name"]}?',
            f'Comparativo: <span>transpaleteira lítio</span> vs manual',
            f'Investimento na locação de <span>paleteira elétrica</span>',
            f'Setores que mais usam <span>transpaleteira</span> em {c["name"]}',
            f'Tudo que acompanha o aluguel de <span>patolinha</span>',
            f'O que a <span>NR-11</span> exige para transpaleteira motorizada',
            f'O que dizem as empresas que alugaram <span>transpaleteira</span> em {c["name"]}',
            f'Entrega rápida em <span>{c["name"]}</span> e cidades vizinhas',
            f'Respostas sobre <span>patolinha elétrica</span> em {c["name"]}',
        ],
        'oque': f'A transpaleteira elétrica Clark com bateria de lítio 24V substitui o esforço manual na movimentação horizontal de paletes. Em {c["name"]}, o {c["pole1"]} concentra indústrias de {c["setor1"]} e {c["setor2"]} com corredores estreitos e paletes de 1.200 a 2.000 kg. A lítio opera em câmaras frias sem perda de autonomia e recarrega em 2-3 horas. {c["pain"]} A {c["dist"]}km de Goiânia, entrega {c["delivery"]}.',
        'h3s': [
            (f'Operações em corredores estreitos no {c["pole1"]}',
             f'O {c["pole1"]} opera com corredores de 2,5 a 3 metros entre racks. A WPio15 Clark, com 750mm de largura, navega esses corredores para picking e reabastecimento. A versão stacker alcança o segundo nível de rack. Para trajetos longos entre setores, a patolada PWio20 (12 km/h) elimina a fadiga do operador.'),
            (f'Lítio 24V: autonomia em qualquer temperatura',
             f'Nos armazéns de {c["setor1"]} em {c["name"]}, a bateria de lítio 24V mantém 95% da autonomia entre -25°C e +60°C. Recarga completa em 2-3 horas, parcial de 30 min devolve 40%. Sem sala ventilada para recarga — conecta em tomada industrial 220V. Para câmaras frias, a lítio é obrigatória.'),
            (f'Manual vs elétrica: a conta que fecha em {c["name"]}',
             f'Uma paleteira manual movimenta 30 paletes/hora com operador fazendo força. A elétrica faz 60 paletes/hora sem esforço. Para uma operação de 500 paletes/dia no {c["pole1"]}, a manual exige 3 operadores em 2 turnos. A elétrica faz com 1 operador em 1 turno. O aluguel de R$ 1.200/mês se paga em economia de mão de obra no primeiro mês.'),
        ],
        'checklist': [
            f'<strong>Lítio 24V:</strong> autonomia de 8 horas por carga, funciona em câmaras frias de {c["setor1"]} em {c["name"]}.',
            f'<strong>Largura de 750mm:</strong> navega corredores estreitos de 2,5m nos armazéns do {c["pole1"]}.',
            f'<strong>Patolada (PWio20):</strong> operador em pé na plataforma, 12 km/h para trajetos longos.',
            f'<strong>Stacker:</strong> elevação até 1.600mm para picking em 2 níveis de rack.',
        ],
        'apps': [
            (f'{c["pole1"]}: armazéns e produção',
             f'Movimentação de paletes em armazéns de {c["setor1"]} e {c["setor2"]}. WPio15 para corredores estreitos, PWio20 patolada para trajetos longos.',
             'https://images.pexels.com/photos/1267338/pexels-photo-1267338.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Armazém industrial no {c["pole1"]} de {c["name"]}'),
            (f'{c["pole2"] or c["bairro1"]}: docas e expedição',
             f'Transpaleteira patolada para deslocamento rápido entre armazém e doca. Capacidade de 2.000 kg para paletes PBR.',
             'https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Doca de expedição em {c["name"]}'),
            (f'{c["bairro1"]}: picking e distribuição',
             f'Separação de pedidos com stacker em 2 níveis de rack. Corredores estreitos de atacadistas e distribuidoras.',
             'https://images.pexels.com/photos/4481259/pexels-photo-4481259.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Centro de distribuição em {c["bairro1"]}, {c["name"]}'),
            (f'{c["rod"]}: cross-docking',
             f'Transbordo de paletes entre carretas. Patolada para trajetos longos entre docas.',
             'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Terminal logístico na {c["rod"]}'),
        ],
        'tests': [
            (f'Operamos 5 transpaleteiras lítio no armazém do {c["pole1"]}. Corredores de 2,8m — a WPio15 cabe com folga. Bateria dura o turno. Produtividade dobrou em relação à manual.',
             'Daniel F.', f'Supervisor Logística, {c["pole1"]}, {c["name"]}-GO (jan/2026)'),
            (f'Patolada PWio20 nas docas do {c["pole2"] or c["bairro1"]}. 450 paletes por turno com 2 máquinas. Antes eram 4 manuais e 6 operadores. A Move entregou {c["delivery"]}.',
             'Carla N.', f'Gerente Expedição, {c["pole2"] or c["bairro1"]}, {c["name"]}-GO (dez/2025)'),
            (f'Picking de 800 pedidos/dia no CD de {c["setor2"]}. Stacker alcança segundo nível de rack. Tempo de pedido caiu de 35 para 22 minutos.',
             'Vinícius P.', f'Coord. CD, {c["setor2"].title()}, {c["name"]}-GO (mar/2026)'),
        ],
        'faqs': [
            (f'Qual transpaleteira para o {c["pole1"]}?',
             f'WPio15 para corredores estreitos (750mm). PWio20 patolada para trajetos longos. Lítio 24V para câmaras frias.'),
            (f'Em quanto tempo entregam em {c["name"]}?',
             f'Entrega {c["delivery"]} — {c["dist"]}km via {c["rod"]}. Bateria carregada e treinamento incluído.'),
            (f'Quanto custa alugar em {c["name"]}?',
             f'R$ 1.200 a R$ 2.200/mês. Lítio 15% mais cara mas economiza 35% na operação.'),
            (f'A lítio funciona em câmaras frias?',
             f'Sim. Mantém 95% da autonomia entre -25°C e +60°C. Obrigatória para câmaras de {c["setor1"]}.'),
            (f'Preciso de NR-11?',
             f'Sim. Qualquer equipamento motorizado exige NR-11. A Move oferece <a href="/{c["slug"]}/curso-de-operador-de-empilhadeira" style="color:var(--color-primary)">curso em {c["name"]}</a>.'),
            (f'Patolada ou walkie para o {c["pole1"]}?',
             f'Trajetos acima de 30m: patolada. Corredores curtos e manobras: walkie.'),
            (f'Stacker substitui empilhadeira?',
             f'Para 2 níveis de rack com corredor < 3m, sim. Para 3+ níveis ou cargas acima de 2 ton: empilhadeira.'),
            (f'Vocês atendem todo o {c["pole1"]}?',
             f'Sim. {c["pole1"]}, {c["pole2"] or ""}, {c["bairro1"]}, {c["bairro2"]} e toda {c["name"]}.'),
        ],
        'expert': f'No {c["pole1"]} de {c["name"]}, a transpaleteira lítio fez a diferença real. Vi operação com manual onde 6 operadores movimentavam 300 paletes/dia fazendo força. Com 3 elétricas, 2 operadores movimentam 500 paletes sem esforço. O retorno sobre o aluguel é de 1 mês',
        'incluso_sub': f'Entrega {c["delivery"]} com bateria carregada e treinamento básico. Inclui:',
        'incluso_items': [
            ('M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z',
             f'Manutenção em {c["name"]}', f'Técnico mobile em {c["resp_time"]}.'),
            ('M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
             'Seguro e documentação', 'Seguro contra danos e laudo incluídos.'),
            ('M13 10V3L4 14h7v7l9-11h-7z',
             f'Entrega {c["delivery"]}', f'{c["dist"]}km via {c["rod"]}.'),
            ('M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z',
             'Suporte 24h', f'Técnico em {c["resp_time"]}.'),
            ('M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2',
             'Consultoria', f'Avaliação gratuita no {c["pole1"]}.'),
            ('M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0',
             'Treinamento', f'Instrução ao operador na entrega.'),
        ],
        'cta': f'Alugue transpaleteira elétrica em {c["name"]}',
        'coverage_cities': 'Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis',
        'service_key': 'transpaleteira',
        'fleet_models': [
            {'name': 'WPio15', 'badge': 'Compacta', 'subtitle': 'Para corredores estreitos',
             'desc': f'Transpaleteira walkie de 1.500 kg com 750mm de largura. Para corredores de 2,5m no {c["pole1"]}. Lítio 24V.',
             'specs': [('Capacidade', '1.500 kg'), ('Largura', '750 mm'), ('Bateria', 'Lítio 24V')]},
            {'name': 'PWio20', 'badge': 'Mais alugada', 'subtitle': 'Patolada para trajetos longos',
             'desc': f'Patolada com plataforma para operador, 12 km/h. Para trajetos de 50-100m entre armazém e doca no {c["pole1"]}.',
             'specs': [('Capacidade', '2.000 kg'), ('Velocidade', '12 km/h'), ('Plataforma', 'Dobrável')]},
            {'name': 'PPXs20', 'badge': 'Versátil', 'subtitle': 'Plataforma dobrável',
             'desc': f'Transpaleteira com plataforma dobrável de 2.000 kg. Para operações mistas no {c["pole2"] or c["bairro1"]}: caminha quando precisa, sobe na plataforma em trajetos longos.',
             'specs': [('Capacidade', '2.000 kg'), ('Bateria', 'Lítio 24V'), ('Direção', 'Elétrica')]},
            {'name': 'WPX35', 'badge': 'Heavy Duty', 'subtitle': 'Carga pesada',
             'desc': f'Transpaleteira para cargas pesadas de até 3.500 kg. Para paletes de {c["setor1"]} e materiais de construção em {c["name"]}.',
             'specs': [('Capacidade', '3.500 kg'), ('Velocidade', '12 km/h'), ('Rodas', '24 Volts')]},
            {'name': 'SWX16 Stacker', 'badge': 'Elevação', 'subtitle': 'Picking em 2 níveis',
             'desc': f'Stacker com elevação até 1.600mm para picking em 2 níveis de rack. Substitui empilhadeira em corredores estreitos do {c["pole1"]}.',
             'specs': [('Capacidade', '1.600 kg'), ('Elevação', '1.600 mm'), ('Bateria', 'Lítio 24V')]},
        ],
        'compare': {
            'alt_name': 'Paleteira Manual',
            'equip_desc': f'Para operações produtivas no {c["pole1"]}',
            'alt_desc': 'Para operações leves e esporádicas',
            'intro': f'No {c["pole1"]} de {c["name"]}, a diferença entre elétrica e manual é produtividade e saúde do operador.',
            'equip_pros': [
                f'60 paletes/hora vs 30 (manual) no {c["pole1"]}',
                'Sem esforço físico — operador não se cansa',
                'Lítio opera em câmaras frias sem perda',
                'Patolada para trajetos longos (12 km/h)',
            ],
            'equip_cons': ['Custo de aluguel mensal (R$ 1.200-2.200)'],
            'alt_pros': ['Custo zero de aluguel', 'Sem necessidade de recarga', 'Manutenção simples'],
            'alt_cons': ['30 paletes/hora (metade da elétrica)', 'Fadiga do operador', 'Inviável para câmaras frias', 'Não escala para operações grandes'],
            'verdict': f'Para operações acima de 100 paletes/dia no {c["pole1"]}: elétrica se paga no primeiro mês em economia de mão de obra. Para operações esporádicas (< 30 paletes): manual é suficiente.',
        },
        'price': {
            'cards': [
                {'name': 'WPio15 Walkie', 'sub': f'Corredores do {c["pole1"]}', 'price': '1.200', 'highlight': True,
                 'items': ['1.500 kg', 'Lítio 24V', f'Para {c["setor1"]}', 'Manutenção inclusa']},
                {'name': 'PWio20 Patolada', 'sub': 'Trajetos longos', 'price': '1.600',
                 'items': ['2.000 kg', '12 km/h', 'Plataforma para operador', 'Suporte 24h']},
                {'name': 'SWX16 Stacker', 'sub': 'Picking 2 níveis', 'price': '2.200',
                 'items': ['1.600 kg', 'Elevação 1.600mm', f'Para racks do {c["pole1"]}', 'Consultoria inclusa']},
            ],
            'note': f'Para {c["name"]}: 1 transpaleteira elétrica de R$ 1.200/mês substitui 2 manuais e economiza 1 operador. ROI no primeiro mês.',
        },
        'nr': {'norma': 'NR-11', 'intro': f'NR-11 exige certificação para transpaleteira motorizada. No {c["pole1"]}, obrigatória.'},
    }


def content_curso(c):
    bridge = c['bridges'].get('curso_nr11', f'certificação de operadores no {c["pole1"]}')
    return {
        'title': f'Curso de Operador de Empilhadeira NR-11 em {c["name"]} | Move Máquinas',
        'desc': f'Curso NR-11 em {c["name"]}: certificação para operadores do {c["pole1"]}. In-company, +2.000 formados. Move Máquinas.',
        'og': f'Certificação NR-11 em {c["name"]}. {c["pole1"]}. In-company. +2.000 formados.',
        'breadcrumb': f'Curso NR-11 em {c["name"]}',
        'service_type': 'Curso de Operador de Empilhadeira NR-11',
        'price_range': 'Consulte',
        'wa_subject': 'curso operador NR-11',
        'equip_short': 'curso de operador NR-11',
        'h1': f'Curso de Operador de<br>Empilhadeira em {c["name"]}',
        'hero_sub': f'{bridge.capitalize()}. Certificação nacional com aulas práticas em empilhadeiras Clark.',
        'h2s': [
            f'O que é a <span>certificação NR-11</span> e por que {c["name"]} exige',
            f'Modelos de <span>capacitação</span> disponíveis em {c["name"]}',
            f'Formação completa vs <span>reciclagem</span>: quando usar cada uma',
            f'Investimento na <span>certificação NR-11</span> em {c["name"]}',
            f'Onde a <span>formação NR-11</span> é mais demandada em {c["name"]}',
            f'O que acompanha o <span>treinamento de operador</span>',
            f'O que a <span>NR-11</span> exige dos operadores de empilhadeira',
            f'Empresas que certificaram operadores em {c["name"]}',
            f'Cobertura: <span>{c["name"]}</span> e cidades próximas',
            f'Dúvidas sobre <span>certificação NR-11</span> em {c["name"]}',
        ],
        'oque': f'O curso NR-11 é a certificação obrigatória para operadores de empilhadeiras e transpaleteiras motorizadas. Em {c["name"]}, o {c["pole1"]} concentra indústrias de {c["setor1"]} e {c["setor2"]} com dezenas de operadores que precisam de certificação. Um operador sem NR-11 pode resultar em auto de infração e interdição. A Move já formou +2.000 operadores e oferece curso in-company em {c["name"]} — sem deslocamento da equipe a Goiânia. {c["pain"]}',
        'h3s': [
            (f'Por que o {c["pole1"]} exige certificação rigorosa',
             f'As indústrias de {c["setor1"]} no {c["pole1"]} operam com normas de segurança que vão além da NR-11. Operadores manuseiam cargas sensíveis que exigem conhecimento de procedimentos específicos. O curso da Move inclui módulo adaptado ao tipo de operação do cliente — não é treinamento genérico. A {c["dist"]}km de Goiânia, o instrutor se desloca até {c["name"]} sem custo extra.'),
            (f'In-company: treinamento nas instalações do cliente',
             f'Para turmas de 10+ operadores no {c["pole1"]} ou qualquer polo de {c["name"]}, a Move leva o treinamento até a fábrica. Aulas práticas com as empilhadeiras do contrato — o operador treina no equipamento que vai usar. Elimina deslocamento a Goiânia ({c["dist"]}km) e reduz inatividade da equipe.'),
            (f'Reciclagem bienal para indústrias de {c["name"]}',
             f'A NR-11 exige reciclagem a cada 2 anos ou quando muda de equipamento. No {c["pole1"]}, onde indústrias renovam frota regularmente, a demanda é constante. Programa de 8 horas que atualiza certificação do operador experiente. Valor reduzido em relação à formação completa.'),
        ],
        'checklist': [
            f'<strong>Certificação nacional:</strong> válida em todo o Brasil, aceita em auditorias no {c["pole1"]}.',
            f'<strong>Aulas práticas:</strong> com empilhadeiras Clark reais, não simuladores.',
            f'<strong>In-company:</strong> sem deslocamento a Goiânia — instrutor vai até {c["name"]}.',
            f'<strong>+2.000 formados:</strong> experiência comprovada em certificação industrial.',
        ],
        'apps': [
            (f'{c["pole1"]}: operadores industriais',
             f'Certificação NR-11 para operadores de {c["setor1"]} e {c["setor2"]}. Módulo adaptado ao tipo de operação e carga. Turmas in-company.',
             'https://images.pexels.com/photos/1267338/pexels-photo-1267338.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Treinamento industrial no {c["pole1"]} de {c["name"]}'),
            (f'{c["pole2"] or c["bairro1"]}: equipes de logística',
             f'Formação para operadores de empilhadeiras e transpaleteiras em centros de distribuição e atacadistas.',
             'https://images.pexels.com/photos/1595104/pexels-photo-1595104.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Centro de logística em {c["name"]}'),
            (f'{c["bairro1"]}: comércio e construção',
             f'Certificação para operadores de empresas de {c["bairro1"]}. Turmas abertas e in-company.',
             'https://images.pexels.com/photos/4481259/pexels-photo-4481259.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Área comercial de {c["bairro1"]}, {c["name"]}'),
            (f'Reciclagem bienal: todas as indústrias',
             f'Programa de 8 horas para renovação de certificação. Atualização normativa + prática com modelos Clark.',
             'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=600',
             f'Reciclagem de operadores em {c["name"]}'),
        ],
        'tests': [
            (f'Certificamos 25 operadores do {c["pole1"]} em turma in-company. O módulo adaptado ao tipo de carga de {c["setor1"]} fez diferença. Auditoria de segurança aprovada sem ressalvas.',
             'Ricardo B.', f'Coord. Segurança, {c["pole1"]}, {c["name"]}-GO (jan/2026)'),
            (f'Reciclagem de 15 operadores do {c["pole2"] or c["bairro1"]} em 1 dia. Instrutor trouxe a Clark GTS30 para prática. Operadores treinaram manobras reais. Certificação no mesmo dia.',
             'Ana Paula F.', f'Gerente RH, {c["pole2"] or c["bairro1"]}, {c["name"]}-GO (dez/2025)'),
            (f'Formação de 10 operadores para novo CD no {c["bairro1"]}. 3 dias: teoria + prática. Todos certificados e operando na semana seguinte. Instrutor vinha de Goiânia ({c["dist"]}km) sem custo extra.',
             'Thiago M.', f'Gerente Operações, {c["bairro1"]}, {c["name"]}-GO (mar/2026)'),
        ],
        'faqs': [
            (f'O curso pode ser in-company no {c["pole1"]}?',
             f'Sim. Turmas de 10+. Aulas práticas nas instalações do cliente. Sem deslocamento a Goiânia.'),
            (f'Qual a carga horária?',
             f'Formação: 16-24 horas (2-3 dias). Reciclagem: 8 horas (1 dia).'),
            (f'A certificação vale em todo o Brasil?',
             f'Sim. Nacional conforme NR-11 do MTE. Aceita em auditorias no {c["pole1"]} e qualquer indústria.'),
            (f'Quanto custa por operador em {c["name"]}?',
             f'Consulte para turmas fechadas — desconto por volume. Custo zero de deslocamento ({c["dist"]}km). Reciclagem: valor reduzido.'),
            (f'Qual o risco de operar sem NR-11 no {c["pole1"]}?',
             f'Auto de infração R$ 3.000-10.000 por operador. Interdição custa R$ 50.000+ em produção parada.'),
            (f'Vocês certificam operadores de transpaleteira?',
             f'Sim. NR-11 cobre empilhadeira, transpaleteira, stacker e rebocador.'),
            (f'A reciclagem pode ser feita no {c["pole1"]}?',
             f'Sim. 8 horas in-company. Certificação renovada no mesmo dia.'),
            (f'O instrutor vai até {c["name"]}?',
             f'Sim. {c["dist"]}km — sem custo extra. Teoria na sala da empresa, prática no pátio.'),
        ],
        'expert': f'No {c["pole1"]} de {c["name"]}, a certificação NR-11 não é formalidade — é requisito de operação. Já vi indústria ser interditada porque operadores estavam com reciclagem vencida. O curso in-company resolve: a equipe certifica sem sair da fábrica, pratica no equipamento real e volta a operar no dia seguinte',
        'incluso_sub': f'Treinamento completo com certificação nacional. Sem custo de deslocamento para {c["name"]}. Inclui:',
        'incluso_items': [
            ('M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z',
             'Certificação nacional', 'Validade em todo o Brasil conforme NR-11/MTE.'),
            ('M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
             'Aulas práticas com Clark', f'Empilhadeiras Clark reais, não simuladores. Prática no {c["pole1"]} ou pátio do cliente.'),
            ('M13 10V3L4 14h7v7l9-11h-7z',
             f'In-company em {c["name"]}', f'Instrutor se desloca até {c["name"]} ({c["dist"]}km) sem custo extra.'),
            ('M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z',
             'Material didático', 'Apostila digital, avaliação presencial e certificado emitido no mesmo dia.'),
            ('M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2',
             'Módulo adaptado', f'Conteúdo específico para o tipo de operação do {c["pole1"]}.'),
            ('M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0',
             'Turmas flexíveis', f'10 a 20 operadores por turma. Horários adaptados ao {c["pole1"]}.'),
        ],
        'cta': f'Certifique seus operadores em {c["name"]}',
        'coverage_cities': 'Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis',
        'service_key': 'curso',
        'fleet_models': [],  # Curso não tem fleet carousel
        'compare': {
            'alt_name': 'Reciclagem de Operador',
            'equip_desc': f'Para operadores novos no {c["pole1"]}',
            'alt_desc': 'Para operadores já certificados',
            'intro': f'No {c["pole1"]} de {c["name"]}, entender a diferença entre formação e reciclagem evita gastar mais do que o necessário.',
            'equip_pros': [
                'Formação completa: 16-24 horas',
                f'Para operadores sem certificação prévia',
                f'Módulo adaptado para {c["setor1"]}',
                'Certificação nacional válida por 2 anos',
            ],
            'equip_cons': ['Custo maior que reciclagem', 'Tempo maior (2-3 dias vs 1 dia)'],
            'alt_pros': [
                '8 horas (1 dia apenas)',
                'Custo reduzido',
                'Certificação renovada no mesmo dia',
            ],
            'alt_cons': [
                'Apenas para operadores já certificados',
                'Não cobre formação de operador novo',
            ],
            'verdict': f'Operador novo no {c["pole1"]}: formação completa. Operador com certificação vencida ou mudança de equipamento: reciclagem bienal.',
        },
        'price': {
            'cards': [
                {'name': 'Formação Completa', 'sub': f'Para operadores novos', 'price': 'Consulte', 'highlight': True,
                 'items': ['16-24 horas (2-3 dias)', f'In-company no {c["pole1"]}', 'Prática com Clark real', 'Certificação nacional']},
                {'name': 'Reciclagem Bienal', 'sub': 'Renovação', 'price': 'Consulte',
                 'items': ['8 horas (1 dia)', 'Certificação renovada no ato', 'Atualização normativa', 'Valor reduzido']},
                {'name': 'Turma Fechada 10+', 'sub': 'Desconto por volume', 'price': 'Consulte',
                 'items': [f'In-company em {c["name"]}', 'Desconto progressivo', f'Sem custo deslocamento ({c["dist"]}km)', 'Horários flexíveis']},
            ],
            'note': f'Para {c["name"]}: um auto de infração por operador sem NR-11 custa R$ 3.000-10.000. Interdição custa R$ 50.000+ em parada. O curso para 20 operadores é fração do custo de uma autuação.',
        },
        'nr': {'norma': 'NR-11', 'intro': f'A NR-11 é a norma que regula operação de empilhadeiras. No {c["pole1"]} de {c["name"]}, cumprimento é obrigatório e fiscalizado.'},
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 lp-builder.py <city-slug> [service]")
        print("Ex:  python3 lp-builder.py senador-canedo-go articulada")
        sys.exit(1)

    city_slug = sys.argv[1]
    service = sys.argv[2] if len(sys.argv) > 2 else 'articulada'

    c = load_city(city_slug)
    print(f"\n{'='*70}")
    print(f"  {c['name']} | {service.upper()}")
    print(f"  {c['pop']} hab | {c['dist']}km | {c['rod']} | {c['eco']}")
    print(f"{'='*70}")

    start = time.time()

    # Generate content
    CONTENT_FNS = {
        'articulada': content_articulada,
        'tesoura': content_tesoura,
        'combustao': content_combustao,
        'transpaleteira': content_transpaleteira,
        'curso': content_curso,
    }

    if service == '--all':
        services_to_run = list(CONTENT_FNS.keys())
    else:
        services_to_run = [service]

    for svc_key in services_to_run:
        content_fn = CONTENT_FNS[svc_key]
        content = content_fn(c)
        svc_slug = SLUGS[svc_key]

        start_svc = time.time()
        html = assemble_page(c, svc_slug, content)

        outfile = os.path.join(DIR, f'{city_slug}-{svc_slug}-BUILT.html')
        with open(outfile, 'w') as f:
            f.write(html)

        sim = check_similarity(REFS[svc_key], html)
        elapsed = time.time() - start_svc
        status = '✓ PASS' if sim['jaccard'] < 0.20 else ('⚠ CLOSE' if sim['jaccard'] < 0.25 else '✗ FAIL')

        print(f"\n  {svc_key.upper()}")
        print(f"  Jaccard: {sim['jaccard']:.3f} {status} | H2: {sim['h2_dup']} | FAQ: {sim['faq_dup']} | Unique: {sim['unique']:.0f}%")
        print(f"  Size: {len(html)//1024}KB | Time: {elapsed:.1f}s")

    sys.exit(0)
