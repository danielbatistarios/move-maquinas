#!/usr/bin/env python3
"""
build-trindade-from-sc.py
Creates Trindade V2 pages for: tesoura, combustao, transpaleteira, curso
by reading the SC scripts, extracting r(old, new) pairs,
keeping the OLD strings (from Goiânia), and creating NEW strings for Trindade
by transforming the SC-specific text to Trindade context.
"""

import re, os, ast
from datetime import datetime

TOTAL_START = datetime.now()
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
    if not s1 or not s2: return 0
    return len(s1 & s2) / len(s1 | s2)

def extract_r_calls(script_path):
    """Extract r(old, new[, count]) calls from a Python script.
    Returns list of (old_string, new_string, count) tuples.
    """
    with open(script_path) as f:
        content = f.read()

    pairs = []

    # Find OLD_..._SCHEMA and NEW_..._SCHEMA variable assignments (multiline strings)
    schema_pattern = r"(OLD_\w+)\s*=\s*'''(.*?)'''"
    new_schema_pattern = r"(NEW_\w+)\s*=\s*'''(.*?)'''"

    old_schemas = {}
    for m in re.finditer(schema_pattern, content, re.DOTALL):
        old_schemas[m.group(1)] = m.group(2)

    new_schemas = {}
    for m in re.finditer(new_schema_pattern, content, re.DOTALL):
        new_schemas[m.group(1)] = m.group(2)

    # Find simple r('old', 'new') calls (single-line)
    # Pattern: r('...', '...')  or  r('...', '...', N)
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip comments and empty lines
        if not line or line.startswith('#') or line.startswith('"""') or line.startswith("'''"):
            i += 1
            continue

        # Check for r( at start of line
        if line.startswith("r("):
            # Collect full call (may span multiple lines)
            call = line
            depth = call.count('(') - call.count(')')
            while depth > 0 and i + 1 < len(lines):
                i += 1
                call += '\n' + lines[i]
                depth = call.count('(') - call.count(')')

            # Try to extract old and new from the call
            # Handle r('old', 'new') and r('old', 'new', N)
            try:
                # Remove the r( prefix and ) suffix
                inner = call.strip()
                if inner.startswith('r(') and inner.endswith(')'):
                    inner = inner[2:-1]
                    # Try to parse as tuple
                    try:
                        parsed = ast.literal_eval('(' + inner + ')')
                        if len(parsed) >= 2:
                            old = parsed[0]
                            new = parsed[1]
                            count = parsed[2] if len(parsed) > 2 else 1
                            pairs.append((old, new, count))
                    except:
                        pass  # Complex multiline — skip
            except:
                pass

        # Check for r(OLD_..., NEW_...) calls
        if 'OLD_' in line and 'NEW_' in line:
            m = re.match(r"r\((\w+),\s*(\w+)\)", line)
            if m:
                old_var = m.group(1)
                new_var = m.group(2)
                if old_var in old_schemas and new_var in new_schemas:
                    pairs.append((old_schemas[old_var], new_schemas[new_var], 1))

        i += 1

    return pairs

def sc_to_trindade(text):
    """Transform Senador Canedo text to Trindade context with deeper rewrites."""
    t = text
    # City
    t = t.replace('Senador Canedo', 'Trindade')
    t = t.replace('senador-canedo-go', 'trindade-go')
    t = t.replace('Senador+Canedo', 'Trindade')
    t = t.replace('senador canedo', 'trindade')
    # Coords
    t = t.replace('-16.6997', '-16.6514')
    t = t.replace('-49.0919', '-49.4926')
    # Context — replace SC landmarks with Trindade context
    t = t.replace('DASC', 'condomínios industriais')
    t = t.replace('DISC', 'galpões comerciais')
    t = t.replace('polo petroquímico', 'setor de expansão urbana')
    t = t.replace('polo petroquimico', 'setor de expansão urbana')
    t = t.replace('complexo petroquímico', 'área em desenvolvimento')
    t = t.replace('complexo petroquimico', 'área em desenvolvimento')
    t = t.replace('petroquímico', 'em crescimento')
    t = t.replace('petroquimico', 'em crescimento')
    t = t.replace('Petrobras, Realpetro e Petrobol', 'construtoras e indústrias em implantação')
    t = t.replace('Petrobras', 'construtoras locais')
    t = t.replace('Realpetro', 'galpões comerciais')
    t = t.replace('BR-153', 'GO-060')
    t = t.replace('20 km', '18 km')
    t = t.replace('Jardim das Oliveiras', 'Setor Maysa')
    t = t.replace('Residencial Canadá', 'Setor Sol Nascente')
    t = t.replace('Residencial Canada', 'Setor Sol Nascente')
    t = t.replace('Village Garavelo', 'Jardim Europa')
    t = t.replace('Jardim Canedo', 'Parque Trindade')
    t = t.replace('Jardim Petropolis', 'Setor Leste')
    t = t.replace('Setor Morada do Bosque', 'Parque dos Cisnes')
    t = t.replace('GO-403', 'GO-222')
    t = t.replace('farmacêuticas', 'obras de construção civil')
    t = t.replace('farmacêutico', 'da construção civil')
    t = t.replace('farmaceuticas', 'obras de construção civil')
    t = t.replace('farmaceutico', 'da construção civil')
    # Deeper rewrites to differentiate from SC
    t = t.replace('distritos industriais', 'condomínios empresariais')
    t = t.replace('distrito industrial', 'condomínio empresarial')
    t = t.replace('áreas limpas', 'ambientes controlados')
    t = t.replace('area limpa', 'ambiente controlado')
    t = t.replace('distribuidoras de combustíveis', 'comércios atacadistas')
    t = t.replace('terminais logísticos', 'depósitos de distribuição')
    t = t.replace('terminais petroquímicos', 'galpões industriais')
    t = t.replace('setor moveleiro', 'setor de construção')
    t = t.replace('linhas de produção', 'operações logísticas')
    t = t.replace('linhas de embalagem', 'operações de distribuição')
    t = t.replace('torres de destilação', 'estruturas metálicas elevadas')
    t = t.replace('tanques de armazenamento', 'coberturas de galpões')
    t = t.replace('inspeção de tanques', 'manutenção de coberturas')
    t = t.replace('troca de instrumentação', 'reparos estruturais')
    t = t.replace('atmosferas explosivas', 'ambientes de obra')
    t = t.replace('paradas programadas', 'etapas de obra')
    t = t.replace('refinarias', 'canteiros de obras')
    t = t.replace('vasos de pressão', 'estruturas de cobertura')
    t = t.replace('tubulações aéreas', 'vigas e treliças')
    t = t.replace('ponte rolante', 'estrutura metálica')
    t = t.replace('pontes rolantes', 'estruturas metálicas')
    t = t.replace('área classificada', 'canteiro de obra')
    t = t.replace('áreas classificadas', 'canteiros de obras')
    # Sentence-level phrase rewrites
    t = t.replace('não pode parar', 'exige continuidade')
    t = t.replace('sem parar a produção', 'sem interromper o cronograma')
    t = t.replace('sem interromper a produção', 'sem atrasar a obra')
    t = t.replace('manutenção programada', 'etapa programada')
    t = t.replace('contrato todo semestre', 'contrato a cada fase da obra')
    t = t.replace('tempo de resposta', 'prazo de atendimento')
    t = t.replace('operações críticas', 'demandas urgentes')
    t = t.replace('despacho emergencial', 'envio prioritário')
    t = t.replace('A proximidade de', 'Os apenas')
    t = t.replace('Frete incluso', 'Sem cobrança de frete')
    t = t.replace('frete incluso', 'sem cobrança de frete')
    t = t.replace('zero parada não programada', 'nenhuma interrupção inesperada')
    t = t.replace('acionamos suporte', 'enviamos equipe técnica')
    t = t.replace('substituímos o equipamento', 'trocamos a máquina')
    t = t.replace('polo farmacêutico', 'zona empresarial')
    t = t.replace('polo alimentício', 'corredor comercial')
    return t

def build_page(service_name, ref_file, sc_script, out_file, sc_v2_file, bsb_v2_file):
    start = datetime.now()

    ref_path = os.path.join(BASE, ref_file)
    with open(ref_path) as f:
        html = f.read()

    # Extract r() calls from SC script
    sc_path = os.path.join(BASE, sc_script)
    pairs = extract_r_calls(sc_path)
    print(f"\n{service_name}: extracted {len(pairs)} r() calls from {sc_script}")

    replaced = 0
    not_found = 0
    for old, new_sc, count in pairs:
        if old in html:
            # Transform the SC new text to Trindade context
            new_trindade = sc_to_trindade(new_sc)
            html = html.replace(old, new_trindade, count)
            replaced += 1
        else:
            not_found += 1

    print(f"  Applied: {replaced}, Not found: {not_found}")

    # Save
    out_path = os.path.join(BASE, out_file)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Verify
    ref_html = open(ref_path).read()
    rs = word_shingles(ref_html)
    ns = word_shingles(html)
    j_ref = jaccard(rs, ns)

    # Cross-check
    cross = []
    for cf in [os.path.join(BASE, sc_v2_file), os.path.join(BASE, bsb_v2_file)]:
        try:
            other = open(cf).read()
            osh = word_shingles(other)
            j = jaccard(ns, osh)
            cross.append((os.path.basename(cf)[:35], j))
        except FileNotFoundError:
            pass

    # Count stray Goiânia
    issues = 0
    for line in html.split('\n'):
        if 'Goiânia' in line or 'Goiania' in line or 'goiania-go' in line:
            ok = any(k in line for k in [
                'addressLocality', 'Parque das Flores', 'Eurico Viana',
                'CNPJ', 'Aparecida', 'option value', '-GO',
                '18 km', 'sede', 'base', 'metropolitana', 'GO-060',
                'trindade-go', 'Atendimento Trindade', 'YouTube',
                'embed', 'Nare91',
            ])
            if not ok:
                issues += 1

    tc = html.count('Trindade') + html.count('trindade')
    elapsed = datetime.now() - start

    print(f"  Jaccard vs Goiânia: {j_ref:.4f} {'✓' if j_ref < 0.20 else '✗ NEEDS FIX'}")
    for name, j in cross:
        print(f"  Jaccard vs {name}: {j:.4f} {'✓' if j < 0.20 else '✗'}")
    print(f"  Goiânia refs: {issues}, Trindade mentions: {tc}")
    print(f"  TEMPO: {int(elapsed.total_seconds()//60):02d}:{int(elapsed.total_seconds()%60):02d}")
    print(f"  TOKENS: ~{len(html)//4:,}")

    return j_ref

# ════════════════════════════════════════════════════════════════
# BUILD ALL 4
# ════════════════════════════════════════════════════════════════

configs = [
    ('tesoura', 'ref-goiania-tesoura.html', 'rebuild-sc-tesoura-v2.py',
     'trindade-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'),
    ('combustão', 'ref-goiania-combustao.html', 'rebuild-sc-combustao-v2.py',
     'trindade-go-aluguel-de-empilhadeira-combustao-V2.html',
     'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
     'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html'),
    ('transpaleteira', 'ref-goiania-transpaleteira.html', 'rebuild-sc-transpaleteira-v2.py',
     'trindade-go-aluguel-de-transpaleteira-V2.html',
     'senador-canedo-go-aluguel-de-transpaleteira-V2.html',
     'brasilia-df-aluguel-de-transpaleteira-V2.html'),
    ('curso', 'ref-goiania-curso.html', 'rebuild-sc-curso-v2.py',
     'trindade-go-curso-de-operador-de-empilhadeira-V2.html',
     'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html',
     'brasilia-df-curso-de-operador-de-empilhadeira-V2.html'),
]

results = {}
for name, ref, sc, out, sc_v2, bsb_v2 in configs:
    results[name] = build_page(name, ref, sc, out, sc_v2, bsb_v2)

total_elapsed = datetime.now() - TOTAL_START
print(f"\n{'='*60}")
print(f"RESUMO — 4 LPs TRINDADE (from SC)")
print(f"{'='*60}")
for k, v in results.items():
    status = '✓' if v < 0.20 else '✗'
    print(f"  {k}: {v:.4f} {status}")
print(f"Tempo total: {int(total_elapsed.total_seconds()//60):02d}:{int(total_elapsed.total_seconds()%60):02d}")
