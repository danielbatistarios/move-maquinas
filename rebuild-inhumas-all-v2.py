#!/usr/bin/env python3
"""
rebuild-inhumas-all-v2.py
Master script that runs all 6 Inhumas rebuild scripts,
checks Jaccard, and uploads to R2.

Runs: articulada, combustao, tesoura, transpaleteira, curso, hub
"""

import subprocess, sys, time, os, re

BASE = '/Users/jrios/move-maquinas-seo'

scripts = [
    'rebuild-inhumas-articulada-v2.py',
    'rebuild-inhumas-combustao-v2.py',
    'rebuild-inhumas-tesoura-v2.py',
    'rebuild-inhumas-transpaleteira-v2.py',
    'rebuild-inhumas-curso-v2.py',
    'rebuild-inhumas-hub-v2.py',
]

total_start = time.time()
results = []

for script in scripts:
    path = os.path.join(BASE, script)
    if not os.path.exists(path):
        print(f"❌ MISSING: {script}")
        results.append((script, 'MISSING', 0))
        continue

    print(f"\n{'='*60}")
    print(f"RUNNING: {script}")
    print(f"{'='*60}")

    t0 = time.time()
    result = subprocess.run(
        [sys.executable, path],
        capture_output=True, text=True, cwd=BASE
    )
    elapsed = time.time() - t0

    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr[:500])

    results.append((script, 'OK' if result.returncode == 0 else 'ERROR', elapsed))

print(f"\n\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
for script, status, elapsed in results:
    print(f"  {status:7s} {elapsed:5.1f}s  {script}")
print(f"\nTotal: {time.time()-total_start:.1f}s")

# ═══════════════════════════════════════════════════════════════════════
# COMPREHENSIVE JACCARD CHECK
# ═══════════════════════════════════════════════════════════════════════

def extract_text(h):
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t).strip().lower()

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard_sim(s1, s2):
    inter = len(s1 & s2)
    union = len(s1 | s2)
    return inter / union if union > 0 else 0.0

services = [
    ('articulada', 'aluguel-de-plataforma-elevatoria-articulada'),
    ('combustao', 'aluguel-de-empilhadeira-combustao'),
    ('tesoura', 'aluguel-de-plataforma-elevatoria-tesoura'),
    ('transpaleteira', 'aluguel-de-transpaleteira'),
    ('curso', 'curso-de-operador-de-empilhadeira'),
]

print(f"\n{'='*60}")
print("JACCARD MATRIX — ALL SERVICES")
print(f"{'='*60}")

all_pass = True
for svc_name, svc_slug in services:
    inhumas_file = os.path.join(BASE, f'inhumas-go-{svc_slug}-V2.html')
    if not os.path.exists(inhumas_file):
        print(f"\n{svc_name}: FILE NOT FOUND")
        all_pass = False
        continue

    with open(inhumas_file) as f:
        inh_ng = ngrams(extract_text(f.read()))

    ref_file = os.path.join(BASE, f'ref-goiania-{svc_name}.html')
    sc_file = os.path.join(BASE, f'senador-canedo-go-{svc_slug}-V2.html')
    bsb_file = os.path.join(BASE, f'brasilia-df-{svc_slug}-V2.html')

    print(f"\n--- {svc_name} ---")
    for label, comp_file in [('ref-goiania', ref_file), ('senador-canedo', sc_file), ('brasilia-df', bsb_file)]:
        if os.path.exists(comp_file):
            with open(comp_file) as f:
                comp_ng = ngrams(extract_text(f.read()))
            j = jaccard_sim(inh_ng, comp_ng)
            status = '✓' if j < 0.20 else '✗ FALHOU'
            if j >= 0.20:
                all_pass = False
            print(f"  vs {label:20s}: {j:.4f}  {status}")
        else:
            print(f"  vs {label:20s}: FILE NOT FOUND")

# Hub check
hub_file = os.path.join(BASE, 'inhumas-go-hub-V2.html')
if os.path.exists(hub_file):
    with open(hub_file) as f:
        hub_ng = ngrams(extract_text(f.read()))
    ref_hub = os.path.join(BASE, 'ref-goiania-hub.html')
    sc_hub = os.path.join(BASE, 'senador-canedo-go-hub-V2.html')
    bsb_hub = os.path.join(BASE, 'brasilia-df-hub-V2.html')
    print(f"\n--- hub ---")
    for label, comp_file in [('ref-goiania', ref_hub), ('senador-canedo', sc_hub), ('brasilia-df', bsb_hub)]:
        if os.path.exists(comp_file):
            with open(comp_file) as f:
                comp_ng = ngrams(extract_text(f.read()))
            j = jaccard_sim(hub_ng, comp_ng)
            status = '✓' if j < 0.20 else '✗ FALHOU'
            if j >= 0.20:
                all_pass = False
            print(f"  vs {label:20s}: {j:.4f}  {status}")

print(f"\n{'='*60}")
print(f"RESULTADO FINAL: {'✓ TODOS PASSARAM' if all_pass else '✗ FALHAS DETECTADAS'}")
print(f"{'='*60}")
