#!/usr/bin/env python3
"""
generate-inhumas-from-sc.py
Reads SC rebuild scripts and generates Inhumas versions by:
1. Keeping all OLD strings (from ref-goiania) unchanged
2. Replacing SC NEW text with Inhumas-specific text

This generates: tesoura, transpaleteira, curso, hub scripts
"""

import re

BASE = '/Users/jrios/move-maquinas-seo'

# Services to generate (articulada and combustao already done)
services = ['tesoura', 'transpaleteira', 'curso', 'hub']

for svc in services:
    sc_path = f'{BASE}/rebuild-sc-{svc}-v2.py'
    inh_path = f'{BASE}/rebuild-inhumas-{svc}-v2.py'

    with open(sc_path) as f:
        code = f.read()

    # ═══════════════════════════════════════════════════════════════
    # STEP 1: Replace OUTPUT file path
    # ═══════════════════════════════════════════════════════════════
    code = code.replace(
        "OUT = '/Users/jrios/move-maquinas-seo/senador-canedo-go-",
        "OUT = '/Users/jrios/move-maquinas-seo/inhumas-go-"
    )

    # ═══════════════════════════════════════════════════════════════
    # STEP 2: Replace all NEW strings (second arg of r() calls)
    # Strategy: Replace SC-specific terms with Inhumas equivalents
    # The OLD strings (first arg) stay the same since they're from ref-goiania
    # ═══════════════════════════════════════════════════════════════

    # Structural: city name, slug, coords
    replacements = [
        # City name in NEW text
        ("'Senador Canedo'", "'Inhumas'"),
        ('"Senador Canedo"', '"Inhumas"'),
        ('Senador Canedo', 'Inhumas'),
        ('Senador+Canedo', 'Inhumas'),
        ('senador-canedo-go', 'inhumas-go'),
        ('senador-canedo', 'inhumas'),

        # Coords
        ('-16.6997', '-16.3547'),
        ('-49.0919', '-49.4952'),

        # Distance/road (in NEW text only)
        ('20 km', '40 km'),
        ('BR-153', 'GO-070'),
        ('pela GO-070', 'pela GO-070'),  # No-op, just for safety

        # SC industrial context → Inhumas textile context
        ('polo petroquímico', 'Distrito Industrial'),
        ('polo petroquimico', 'Distrito Industrial'),
        ('complexo petroquímico', 'polo têxtil'),
        ('complexo petroquimico', 'polo têxtil'),
        ('Petrobras, Realpetro e Petrobol', 'confecções, tecelagens e beneficiadoras'),
        ('Petrobras, Realpetro', 'confecções e tecelagens'),
        ('Petrobol', 'indústrias alimentícias'),
        ('DASC e DISC', 'polo de confecção e Distrito Industrial'),
        ('DASC', 'polo de confecções'),
        ('DISC', 'indústria alimentícia'),
        ('polo de confecções e indústria alimentícia', 'polo de confecção e indústria alimentícia'),
        ('farmacêutic', 'de confecção e alimentíci'),
        ('tanques de armazenamento', 'barracões de costura'),
        ('torres de destilação', 'galpões de tecelagem'),
        ('vasos de pressão', 'esteiras de produção'),
        ('tubulações aéreas', 'linhas de exaustão'),
        ('Jardim das Oliveiras', 'Centro'),
        ('Residencial Canadá', 'Setor Industrial'),
        ('130 mil habitantes', '53 mil habitantes'),
        ('GO-403', 'GO-070'),
        ('tambores de 200 litros', 'fardos de tecido'),
        ('IBC de 1.000 kg', 'paletes de confecção'),
        ('tambores', 'fardos'),
        ('insumos químicos', 'aviamentos e tecidos'),
    ]

    for old, new in replacements:
        code = code.replace(old, new)

    # ═══════════════════════════════════════════════════════════════
    # STEP 3: Fix script metadata
    # ═══════════════════════════════════════════════════════════════
    code = code.replace(f'rebuild-sc-{svc}-v2.py', f'rebuild-inhumas-{svc}-v2.py')
    code = code.replace('para Inhumas Canedo', 'para Inhumas')
    code = code.replace('Gera LP de', 'Gera LP de')
    code = code.replace('Gera Hub de Cidade para Inhumas',
                        'Gera Hub de Cidade para Inhumas')

    # Fix Jaccard comparison references
    code = code.replace("sc = html.count('Inhumas')",
                        "sc = html.count('Inhumas')")
    code = code.replace("f\"\\nInhumas: {sc} menções\"",
                        "f\"\\nInhumas: {sc} menções\"")

    # Fix the local keyword counting for Inhumas context
    code = code.replace(
        "local = html.count('polo de confecções') + html.count('Distrito Industrial') + html.count('indústria alimentícia') + html.count('GO-070')",
        "local = html.count('confecç') + html.count('têxtil') + html.count('grão') + html.count('GO-070') + html.count('Distrito Industrial')"
    )

    # ═══════════════════════════════════════════════════════════════
    # STEP 4: Fix verification section — look for Inhumas not SC
    # ═══════════════════════════════════════════════════════════════
    code = code.replace("'Inhumas': {sc}", "'Inhumas': {sc}")

    with open(inh_path, 'w') as f:
        f.write(code)

    print(f"✅ Generated: {inh_path} ({len(code):,} chars)")

print("\nDone. Now run each script to build the HTML files.")
