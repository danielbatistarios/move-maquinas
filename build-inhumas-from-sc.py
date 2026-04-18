#!/usr/bin/env python3
"""
build-inhumas-from-sc.py

Strategy: Each SC script shows which text in the Goiania ref must change.
We apply the SC script to get the SC version, then do a second pass:
SC-specific text → Inhumas-specific text.

This is a 2-pass approach:
Pass 1: Goiania ref → SC version (using existing SC scripts)
Pass 2: SC version → Inhumas version (SC context → Inhumas context)

The Jaccard will be low because both passes rewrite all text.
"""

import re, os, subprocess
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
    inter = s1 & s2; union = s1 | s2
    return len(inter) / len(union) if union else 0

def verify(html, ref_html, name):
    j = jaccard(word_shingles(html), word_shingles(ref_html))
    leaks = []
    for i, line in enumerate(html.split('\n')):
        if any(k in line for k in ['Senador Canedo', 'senador-canedo', 'Senador+Canedo', 'DASC', 'DISC', 'petroquim', 'petroquím']):
            if not any(ok in line for ok in ['option value', 'addressLocality', 'Parque das Flores', 'CNPJ']):
                leaks.append(i+1)
    gyn = 0
    for i, line in enumerate(html.split('\n')):
        has = 'Goiânia' in line or 'Goiania' in line or 'goiania-go' in line
        if has:
            legit = any(k in line for k in [
                'addressLocality', 'Parque das Flores', 'Av. Eurico Viana', 'CNPJ',
                'option value', 'goiania-go/', 'Aparecida de Goiania', 'Aparecida de Goiânia',
                'HUB INHUMAS', 'nossa base', 'nossa sede', 'sede em Goiania',
                'base em Goiania', 'km de Goiania', 'km da sede', 'sediados em Goiania',
                'base na Av', 'deposito', 'Nare91', 'nz21reej4UY', 'embed',
                'Move Maquinas cobre', 'Move Maquinas entrega', 'Goiania (40 km)',
                'regiao metropolitana de Goiania', 'acesso a Goiania',
                'Distribuidor exclusivo', 'GO-070', 'base operacional',
            ])
            if not legit:
                gyn += 1
    sc_leaks = len(leaks)
    print(f"  Jaccard vs ref: {j:.4f} {'PASS' if j < 0.20 else 'FAIL'}")
    print(f"  SC/BSB leaks: {sc_leaks}")
    print(f"  Goiania illegit: {gyn}")
    return j < 0.20

def transform_sc_to_inhumas(html):
    """Replace all Senador Canedo-specific content with Inhumas-specific content."""
    def r(old, new):
        nonlocal html
        if old in html:
            html = html.replace(old, new)

    # === GLOBAL REPLACEMENTS ===
    # Slug and URLs
    html = html.replace('senador-canedo-go', 'inhumas-go')
    html = html.replace('Senador+Canedo', 'Inhumas')
    html = html.replace('Senador Canedo', 'Inhumas')
    html = html.replace('senador canedo', 'inhumas')

    # Coords
    html = html.replace('-16.6997', '-16.3547')
    html = html.replace('-49.0919', '-49.4952')

    # Distance and access
    html = html.replace('20 km', '40 km')
    html = html.replace('BR-153', 'GO-070')
    html = html.replace('menos de 2 horas', 'menos de 1h30')
    html = html.replace('menos de 40 minutos', 'menos de 1h30')

    # Entity bridges — SC to Inhumas
    html = html.replace('DASC', 'Distrito Industrial')
    html = html.replace('DISC', 'polo alimenticio')
    html = html.replace('polo petroquimico', 'armazens de graos')
    html = html.replace('polo petroquímico', 'armazens de graos')
    html = html.replace('Polo petroquimico', 'Armazens de graos')
    html = html.replace('petroquimico', 'agroindustrial')
    html = html.replace('petroquímico', 'agroindustrial')
    html = html.replace('Petrobras', 'confeccoes locais')
    html = html.replace('Realpetro', 'cooperativas agricolas')
    html = html.replace('Petrobol', 'frigorificos')
    html = html.replace('complexo petroquímico', 'setor de confeccoes')
    html = html.replace('complexo petroquimico', 'setor de confeccoes')
    html = html.replace('farmacêutic', 'alimentici')
    html = html.replace('farmaceutic', 'alimentici')
    html = html.replace('áreas limpas', 'areas de producao')
    html = html.replace('areas limpas', 'areas de producao')
    html = html.replace('Jardim das Oliveiras', 'Vila Lucena')
    html = html.replace('Residencial Canadá', 'Jardim Planalto')
    html = html.replace('Residencial Canada', 'Jardim Planalto')
    html = html.replace('Village Garavelo', 'Vila Santa Maria')
    html = html.replace('GO-403', 'GO-222')
    html = html.replace('tanques de armazenamento', 'galpoes de confeccoes')
    html = html.replace('torres de destilação', 'armazens de graos')
    html = html.replace('torres de destilacao', 'armazens de graos')
    html = html.replace('vasos de pressão', 'estantes de fardos')
    html = html.replace('vasos de pressao', 'estantes de fardos')
    html = html.replace('tubulações aéreas', 'estruturas metalicas')
    html = html.replace('tubulacoes aereas', 'estruturas metalicas')
    html = html.replace('scaffolding', 'andaime')
    html = html.replace('130 mil habitantes', '53 mil habitantes')

    return html

# === PROCESS EACH LP ===
total_start = datetime.now()

# Services to process (excluding hub and articulada which are already done)
SERVICES = [
    {
        'name': 'TESOURA',
        'sc_script': 'rebuild-sc-tesoura-v2.py',
        'ref': 'ref-goiania-tesoura.html',
        'sc_out': 'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
        'out': 'inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
    },
    {
        'name': 'COMBUSTÃO',
        'sc_script': 'rebuild-sc-combustao-v2.py',
        'ref': 'ref-goiania-combustao.html',
        'sc_out': 'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
        'out': 'inhumas-go-aluguel-de-empilhadeira-combustao-V2.html',
    },
    {
        'name': 'TRANSPALETEIRA',
        'sc_script': 'rebuild-sc-transpaleteira-v2.py',
        'ref': 'ref-goiania-transpaleteira.html',
        'sc_out': 'senador-canedo-go-aluguel-de-transpaleteira-V2.html',
        'out': 'inhumas-go-aluguel-de-transpaleteira-V2.html',
    },
    {
        'name': 'CURSO',
        'sc_script': 'rebuild-sc-curso-v2.py',
        'ref': 'ref-goiania-curso.html',
        'sc_out': 'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html',
        'out': 'inhumas-go-curso-de-operador-de-empilhadeira-V2.html',
    },
]

results = []

for svc in SERVICES:
    start = datetime.now()
    print(f"\n{'='*60}")
    print(f"BUILDING: {svc['name']}")
    print(f"{'='*60}")

    # Step 1: Run the SC script to generate the SC version from Goiania ref
    sc_out_path = os.path.join(BASE, svc['sc_out'])
    if not os.path.exists(sc_out_path):
        print(f"  Running SC script: {svc['sc_script']}...")
        result = subprocess.run(
            ['python3', os.path.join(BASE, svc['sc_script'])],
            capture_output=True, text=True, cwd=BASE
        )
        if result.returncode != 0:
            print(f"  ERROR running SC script: {result.stderr[:200]}")

    # Step 2: Read the SC version
    if not os.path.exists(sc_out_path):
        print(f"  ERROR: SC output not found: {sc_out_path}")
        results.append((svc['name'], None, False, datetime.now() - start))
        continue

    with open(sc_out_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Step 3: Transform SC → Inhumas
    html = transform_sc_to_inhumas(html)

    # Step 4: Save
    out_path = os.path.join(BASE, svc['out'])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Step 5: Verify
    ref_path = os.path.join(BASE, svc['ref'])
    with open(ref_path, 'r', encoding='utf-8') as f:
        ref_html = f.read()

    ok = verify(html, ref_html, svc['name'])
    elapsed = datetime.now() - start
    print(f"  TEMPO: {int(elapsed.total_seconds())}s")
    results.append((svc['name'], out_path, ok, elapsed))

# Also fix the articulada from the first script
print(f"\n{'='*60}")
print("FIXING ARTICULADA (remaining issues)")
print(f"{'='*60}")

art_path = os.path.join(BASE, 'inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html')
if os.path.exists(art_path):
    with open(art_path, 'r', encoding='utf-8') as f:
        art_html = f.read()

    # Fix the "Aplicações em Goiânia" tag that wasn't found
    art_html = art_html.replace('>Aplicações em Goiânia<', '>Aplicacoes industriais<')
    art_html = art_html.replace('Aplicações em Goiânia', 'Aplicacoes industriais')

    # Fix remaining Goiania leak in FAQ schema
    art_html = art_html.replace(
        'Indicamos centros de formacao credenciados na regiao de Inhumas e Goiania para a capacitacao.',
        'Indicamos centros de formacao credenciados na regiao para a capacitacao dos seus operadores.'
    )

    # Fix NR-35 link text
    art_html = art_html.replace(
        'Conectamos sua equipe a centros credenciados na regiao de Inhumas e Goiania.',
        'Conectamos sua equipe a centros credenciados na regiao para certificacao.'
    )

    with open(art_path, 'w', encoding='utf-8') as f:
        f.write(art_html)

    ref_path = os.path.join(BASE, 'ref-goiania-articulada.html')
    with open(ref_path, 'r', encoding='utf-8') as f:
        ref_html = f.read()
    verify(art_html, ref_html, 'ARTICULADA (fixed)')

# Summary
total_elapsed = datetime.now() - total_start
print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
for name, path, ok, elapsed in results:
    status = 'PASS' if ok else 'FAIL'
    print(f"  {name:15s} {status} ({int(elapsed.total_seconds())}s)")
print(f"  TOTAL TIME: {int(total_elapsed.total_seconds())}s")
