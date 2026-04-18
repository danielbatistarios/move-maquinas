#!/usr/bin/env python3
"""
fix-uruacu-goiania-sweep.py
Sweep all 4 remaining LP files and replace ALL Goiânia/goiania-go mentions
(except legitimate ones like addressLocality, Av. Eurico Viana, CNPJ, option values).
"""
import re, os, time, boto3

START = time.time()
BASE = '/Users/jrios/move-maquinas-seo'

r2 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto')

def text_only(h):
    h2 = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h2 = re.sub(r'<script[^>]*>.*?</script>', '', h2, flags=re.DOTALL)
    h2 = re.sub(r'<select[^>]*>.*?</select>', '', h2, flags=re.DOTALL)
    h2 = re.sub(r'<[^>]+>', ' ', h2)
    return re.sub(r'\s+', ' ', h2).strip().lower()

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(a, b):
    if not a or not b: return 0
    return len(a & b) / len(a | b)

# Lines that should keep "Goiânia" as-is
KEEP_PATTERNS = [
    'addressLocality',
    'Parque das Flores',
    'Eurico Viana',
    'CNPJ',
    '<option value=',
    'goiania-go/',       # internal links TO goiania (legitimate)
    'Aparecida de Goiânia',  # city name in coverage
    'Goiânia</a>',       # link text for Goiania hub
    'Goiânia)',           # in coverage list e.g. "Goiânia (280 km)"
    'sede',              # "sede em Goiânia"
]

files_config = [
    {
        'v2': 'uruacu-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
        'ref': 'ref-goiania-tesoura.html',
        'r2_key': 'uruacu-go/aluguel-de-plataforma-elevatoria-tesoura/index.html',
        'label': 'TESOURA',
    },
    {
        'v2': 'uruacu-go-aluguel-de-empilhadeira-combustao-V2.html',
        'ref': 'ref-goiania-combustao.html',
        'r2_key': 'uruacu-go/aluguel-de-empilhadeira-combustao/index.html',
        'label': 'COMBUSTAO',
    },
    {
        'v2': 'uruacu-go-aluguel-de-transpaleteira-V2.html',
        'ref': 'ref-goiania-transpaleteira.html',
        'r2_key': 'uruacu-go/aluguel-de-transpaleteira/index.html',
        'label': 'TRANSPALETEIRA',
    },
    {
        'v2': 'uruacu-go-curso-de-operador-de-empilhadeira-V2.html',
        'ref': 'ref-goiania-curso.html',
        'r2_key': 'uruacu-go/curso-de-operador-de-empilhadeira/index.html',
        'label': 'CURSO',
    },
]

results = []

for cfg in files_config:
    v2_path = os.path.join(BASE, cfg['v2'])
    ref_path = os.path.join(BASE, cfg['ref'])

    with open(v2_path, 'r', encoding='utf-8') as f:
        html = f.read()

    lines = html.split('\n')
    new_lines = []
    changes = 0

    for i, line in enumerate(lines):
        if 'Goiânia' in line or 'Goiania' in line or 'goiânia' in line:
            # Check if this line should be kept
            should_keep = any(p in line for p in KEEP_PATTERNS)
            if not should_keep:
                # Replace Goiânia → Uruaçu
                orig = line
                line = line.replace('Goiânia', 'Uruaçu')
                line = line.replace('Goiania', 'Uruaçu')  # without accent
                line = line.replace('goiânia', 'uruaçu')
                if line != orig:
                    changes += 1
        new_lines.append(line)

    html = '\n'.join(new_lines)

    # Also fix remaining goiania-go slugs that are NOT internal links
    # (canonical, schema breadcrumb items pointing to this page's own URL)
    # Keep: href="/goiania-go/" (link to Goiania hub — legitimate)
    # Fix: movemaquinas.com.br/goiania-go/aluguel-de-... → uruacu-go/...
    html = html.replace('movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura',
                        'movemaquinas.com.br/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura')
    html = html.replace('movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao',
                        'movemaquinas.com.br/uruacu-go/aluguel-de-empilhadeira-combustao')
    html = html.replace('movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira',
                        'movemaquinas.com.br/uruacu-go/aluguel-de-transpaleteira')
    html = html.replace('movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira',
                        'movemaquinas.com.br/uruacu-go/curso-de-operador-de-empilhadeira')
    html = html.replace('movemaquinas.com.br/goiania-go/curso-operador-empilhadeira',
                        'movemaquinas.com.br/uruacu-go/curso-de-operador-de-empilhadeira')

    # Verify remaining issues
    lines2 = html.split('\n')
    remaining = []
    for i, line in enumerate(lines2):
        if ('Goiânia' in line or 'Goiania' in line) and not any(p in line for p in KEEP_PATTERNS):
            remaining.append((i+1, line.strip()[:120]))

    # Jaccard
    ref_html = open(ref_path).read()
    ng_ref = ngrams(text_only(ref_html))
    ng_new = ngrams(text_only(html))
    j_ref = jaccard(ng_ref, ng_new)

    # vs SC/BSB
    sc_file = cfg['v2'].replace('uruacu-go', 'senador-canedo-go')
    bsb_file = cfg['v2'].replace('uruacu-go', 'brasilia-df')
    j_sc = j_bsb = '-'
    for lbl, comp_file in [('SC', sc_file), ('BSB', bsb_file)]:
        comp_path = os.path.join(BASE, comp_file)
        if os.path.exists(comp_path):
            ng_c = ngrams(text_only(open(comp_path).read()))
            j = jaccard(ng_c, ng_new)
            if lbl == 'SC': j_sc = j
            else: j_bsb = j

    print(f"\n{'='*60}")
    print(f"{cfg['label']} URUACU")
    print(f"{'='*60}")
    print(f"Linhas alteradas neste sweep: {changes}")
    print(f"Referências residuais: {len(remaining)}")
    for ln, txt in remaining[:3]:
        print(f"  L{ln}: {txt}")
    print(f"JACCARD vs REF: {j_ref:.4f}")
    if isinstance(j_sc, float): print(f"JACCARD vs SC: {j_sc:.4f}")
    if isinstance(j_bsb, float): print(f"JACCARD vs BSB: {j_bsb:.4f}")

    # Count local mentions
    uru_count = html.count('Uruaçu') + html.count('Uruacu')
    local_count = html.count('Distrito Agroindustrial') + html.count('BR-153') + html.count('frigor') + html.count('armazén')
    print(f"Uruaçu mentions: {uru_count} | Local context: {local_count}")

    # Save
    with open(v2_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Upload
    r2.put_object(Bucket='pages', Key=cfg['r2_key'], Body=html.encode('utf-8'),
                  ContentType='text/html; charset=utf-8')
    url = f"https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{cfg['r2_key']}"
    print(f"Salvo + Upload: {url}")

    results.append({
        'page': cfg['label'],
        'j_ref': j_ref,
        'j_sc': j_sc,
        'j_bsb': j_bsb,
        'url': url,
        'uru_count': uru_count,
    })

elapsed = time.time() - START
print("\n\n" + "="*80)
print("RESUMO SWEEP — 4 LPs corrigidas")
print("="*80)
print(f"{'Pagina':<25} {'J_REF':>8} {'J_SC':>8} {'J_BSB':>8} {'Uruaçu':>8}")
print("-"*65)
for r in results:
    j_sc = f"{r['j_sc']:.4f}" if isinstance(r['j_sc'], float) else '-'
    j_bsb = f"{r['j_bsb']:.4f}" if isinstance(r['j_bsb'], float) else '-'
    print(f"{r['page']:<25} {r['j_ref']:>8.4f} {j_sc:>8} {j_bsb:>8} {r['uru_count']:>8}")

print(f"\nTEMPO: {elapsed:.1f}s")
print("\nURLs:")
for r in results:
    print(f"  {r['url']}")
