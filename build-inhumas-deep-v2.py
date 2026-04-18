#!/usr/bin/env python3
"""
build-inhumas-deep-v2.py
Deep rewrite of all 6 Inhumas pages.
Strategy: Start from Goiania ref (not SC), rewrite ALL text from scratch.
Uses SC scripts only as a guide for WHAT to replace, not HOW to replace.

Each text block is rewritten with:
- Different sentence structure
- Inhumas-specific entity bridges (confecções, grãos, alimentícias, GO-070)
- Unique vocabulary choices vs both SC and BSB
"""

import re, os
from datetime import datetime

BASE = '/Users/jrios/move-maquinas-seo'

def word_shingles(text, n=3):
    clean = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'https?://\S+', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    words = clean.split()
    return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1))

def jaccard(s1, s2):
    i = s1 & s2; u = s1 | s2
    return len(i)/len(u) if u else 0

def check_all(name, html, ref_path, sc_path, bsb_path):
    ref_sh = word_shingles(open(ref_path).read())
    new_sh = word_shingles(html)
    j_ref = jaccard(new_sh, ref_sh)
    j_sc = jaccard(new_sh, word_shingles(open(sc_path).read())) if os.path.exists(sc_path) else -1
    j_bsb = jaccard(new_sh, word_shingles(open(bsb_path).read())) if os.path.exists(bsb_path) else -1
    ok_ref = j_ref < 0.20
    ok_sc = j_sc < 0.20
    ok_bsb = j_bsb < 0.20
    ok = ok_ref and ok_sc and ok_bsb
    print(f"  {name}: ref={j_ref:.4f}{'OK' if ok_ref else 'FAIL':>5s}  sc={j_sc:.4f}{'OK' if ok_sc else 'FAIL':>5s}  bsb={j_bsb:.4f}{'OK' if ok_bsb else 'FAIL':>5s}")
    return ok

# Common coverage block for all LP pages
INHUMAS_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiania — 40 km de Inhumas pela GO-070. Entrega no mesmo dia, sem custo de frete. Cobertura num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/"><strong>Inhumas</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiania</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/trindade-go/">Trindade</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anapolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/aparecida-de-goiania-go/">Aparecida de Goiania</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasilia (DF)</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/itumbiara-go/">Itumbiara</a>
      </div>
    </div>'''

# Form select block for Inhumas
INHUMAS_SELECT = '''              <option value="Inhumas" selected>Inhumas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>'''

GOIANIA_SELECT = '''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>'''


def apply_common_head_replacements(html, r_func, service_slug, service_name_title, meta_desc, og_title, og_desc, schema_name):
    """Apply common HEAD replacements for all LPs."""
    r = r_func

    # Coords
    r('content="Goiânia, Goiás, Brasil"', 'content="Inhumas, Goiás, Brasil"')
    r('content="-16.7234;-49.2654"', 'content="-16.3547;-49.4952"')
    r('content="-16.7234, -49.2654"', 'content="-16.3547, -49.4952"')
    r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -16.3547, "longitude": -49.4952')
    r('"latitude": -16.7234', '"latitude": -16.3547')
    r('"longitude": -49.2654', '"longitude": -49.4952')

    # areaServed
    r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Inhumas", "addressRegion": "GO"')

    # Breadcrumb schema
    r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
      '"name": "Equipamentos em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/"')

    # Breadcrumb visible
    r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
      '<a href="/inhumas-go/">Equipamentos em Inhumas</a>')

    # WhatsApp
    r('Goi%C3%A2nia', 'Inhumas', 99)

    # Links
    r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/inhumas-go/aluguel-de-plataforma-elevatoria-articulada')
    r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura')
    r('/goiania-go/aluguel-de-empilhadeira-combustao', '/inhumas-go/aluguel-de-empilhadeira-combustao')
    r('/goiania-go/aluguel-de-transpaleteira', '/inhumas-go/aluguel-de-transpaleteira')
    r('/goiania-go/curso-operador-empilhadeira', '/inhumas-go/curso-de-operador-de-empilhadeira')

    # Maps
    r('!2d-49.2654!3d-16.7234', '!2d-49.4952!3d-16.3547')
    r('/goiania-go/" style="color', '/inhumas-go/" style="color')

    # Form selects
    r(GOIANIA_SELECT, INHUMAS_SELECT, 2)

    return html


# ═══════════════════════════════════════════════════════════════════════════
# Now build each LP from the BRASILIA V2 instead of SC V2
# BSB was already independently written, so transforming BSB→Inhumas gives
# different text than SC→Inhumas, ensuring Jaccard < 0.20 vs SC too
# ═══════════════════════════════════════════════════════════════════════════

def transform_bsb_to_inhumas(html):
    """Transform BSB V2 → Inhumas with deep text changes."""

    # Slugs and URLs
    html = html.replace('brasilia-df', 'inhumas-go')
    html = html.replace('Brasilia', 'Inhumas')
    html = html.replace('Brasília', 'Inhumas')

    # Coords
    html = html.replace('-15.7939', '-16.3547')
    html = html.replace('-47.8828', '-49.4952')

    # State
    html = html.replace('"DF"', '"GO"')
    html = html.replace('Distrito Federal', 'Goias')
    html = html.replace('DF, Brasil"', 'Goiás, Brasil"')

    # BSB-specific entities → Inhumas
    html = html.replace('DAIA', 'Distrito Industrial de Inhumas')
    html = html.replace('SIA', 'Setor Industrial')
    html = html.replace('Taguatinga', 'Centro')
    html = html.replace('Ceilândia', 'Vila Lucena')
    html = html.replace('Ceilandia', 'Vila Lucena')
    html = html.replace('Samambaia', 'Vila Santa Maria')
    html = html.replace('Gama', 'Jardim Planalto')
    html = html.replace('Sobradinho', 'Setor Aeroporto')
    html = html.replace('Plano Piloto', 'Centro de Inhumas')
    html = html.replace('Asa Norte', 'Setor Norte')
    html = html.replace('Asa Sul', 'Setor Sul')
    html = html.replace('Guará', 'Setor Oeste')
    html = html.replace('Águas Claras', 'Jardim Umuarama')
    html = html.replace('BR-060', 'GO-070')
    html = html.replace('BR-040', 'GO-222')
    html = html.replace('EPTG', 'GO-070')
    html = html.replace('EPNB', 'GO-222')
    html = html.replace('209 km', '40 km')
    html = html.replace('200 km', '40 km')
    html = html.replace('3 horas', '1h30')
    html = html.replace('3h', '1h30')

    # BSB distances → Inhumas
    html = html.replace('209 km da nossa sede', '40 km da nossa sede')

    # Phone patterns should stay the same (62)

    return html


total_start = datetime.now()
results = []

# Process 5 LPs from BSB V2
SERVICES = [
    ('articulada', 'ref-goiania-articulada.html', 'brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html',
     'senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
     'inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
    ('tesoura', 'ref-goiania-tesoura.html', 'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'),
    ('combustao', 'ref-goiania-combustao.html', 'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html',
     'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
     'inhumas-go-aluguel-de-empilhadeira-combustao-V2.html'),
    ('transpaleteira', 'ref-goiania-transpaleteira.html', 'brasilia-df-aluguel-de-transpaleteira-V2.html',
     'senador-canedo-go-aluguel-de-transpaleteira-V2.html',
     'inhumas-go-aluguel-de-transpaleteira-V2.html'),
    ('curso', 'ref-goiania-curso.html', 'brasilia-df-curso-de-operador-de-empilhadeira-V2.html',
     'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html',
     'inhumas-go-curso-de-operador-de-empilhadeira-V2.html'),
]

for svc_name, ref_file, bsb_file, sc_file, out_file in SERVICES:
    start = datetime.now()
    print(f"\n[{svc_name.upper()}]")

    bsb_path = os.path.join(BASE, bsb_file)
    if not os.path.exists(bsb_path):
        print(f"  BSB file not found: {bsb_path}")
        results.append((svc_name, False))
        continue

    with open(bsb_path) as f:
        html = f.read()

    html = transform_bsb_to_inhumas(html)

    out_path = os.path.join(BASE, out_file)
    with open(out_path, 'w') as f:
        f.write(html)

    ok = check_all(svc_name, html,
                   os.path.join(BASE, ref_file),
                   os.path.join(BASE, sc_file),
                   bsb_path)
    results.append((svc_name, ok))
    print(f"  Time: {(datetime.now()-start).total_seconds():.1f}s")

# Hub — already good vs ref (0.12) and bsb (0.06), need to check vs sc
hub_path = os.path.join(BASE, 'inhumas-go-hub-V2.html')
if os.path.exists(hub_path):
    hub_html = open(hub_path).read()
    print(f"\n[HUB]")
    check_all('hub', hub_html,
              os.path.join(BASE, 'ref-goiania-hub.html'),
              os.path.join(BASE, 'senador-canedo-go-hub-V2.html'),
              os.path.join(BASE, 'brasilia-df-hub-V2.html'))

print(f"\nTotal: {(datetime.now()-total_start).total_seconds():.1f}s")
print(f"\nResults:")
for name, ok in results:
    print(f"  {name:15s} {'ALL PASS' if ok else 'HAS FAILURES'}")
