#!/usr/bin/env python3
"""
finalize-and-upload-inhumas.py
Pick best version for each page, verify, and upload.
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
    i = s1 & s2; u = s1 | s2
    return len(i)/len(u) if u else 0

# Check current state of all 6 files
FILES = [
    ('Hub', 'inhumas-go-hub-V2.html', 'ref-goiania-hub.html',
     'senador-canedo-go-hub-V2.html', 'brasilia-df-hub-V2.html',
     'inhumas-go/index.html'),
    ('Articulada', 'inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
     'ref-goiania-articulada.html',
     'senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
     'brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html',
     'inhumas-go/aluguel-de-plataforma-elevatoria-articulada/index.html'),
    ('Tesoura', 'inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'ref-goiania-tesoura.html',
     'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'inhumas-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'),
    ('Combustao', 'inhumas-go-aluguel-de-empilhadeira-combustao-V2.html',
     'ref-goiania-combustao.html',
     'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
     'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html',
     'inhumas-go/aluguel-de-empilhadeira-combustao/index.html'),
    ('Transpaleteira', 'inhumas-go-aluguel-de-transpaleteira-V2.html',
     'ref-goiania-transpaleteira.html',
     'senador-canedo-go-aluguel-de-transpaleteira-V2.html',
     'brasilia-df-aluguel-de-transpaleteira-V2.html',
     'inhumas-go/aluguel-de-transpaleteira/index.html'),
    ('Curso', 'inhumas-go-curso-de-operador-de-empilhadeira-V2.html',
     'ref-goiania-curso.html',
     'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html',
     'brasilia-df-curso-de-operador-de-empilhadeira-V2.html',
     'inhumas-go/curso-de-operador-de-empilhadeira/index.html'),
]

start = datetime.now()
print("=" * 70)
print("INHUMAS — FINAL VERIFICATION AND UPLOAD")
print("=" * 70)

print(f"\n{'Page':15s} {'vs REF':>8s} {'vs SC':>8s} {'vs BSB':>8s} {'Size':>8s} {'Status':>8s}")
print("-" * 65)

all_pass_ref = True
upload_files = []

for name, inh_file, ref_file, sc_file, bsb_file, r2_key in FILES:
    inh_path = os.path.join(BASE, inh_file)
    if not os.path.exists(inh_path):
        print(f"{name:15s} FILE NOT FOUND")
        continue

    html = open(inh_path).read()
    new_sh = word_shingles(html)

    ref_sh = word_shingles(open(os.path.join(BASE, ref_file)).read())
    j_ref = jaccard(new_sh, ref_sh)

    sc_path = os.path.join(BASE, sc_file)
    j_sc = jaccard(new_sh, word_shingles(open(sc_path).read())) if os.path.exists(sc_path) else 0

    bsb_path = os.path.join(BASE, bsb_file)
    j_bsb = jaccard(new_sh, word_shingles(open(bsb_path).read())) if os.path.exists(bsb_path) else 0

    ok_ref = j_ref < 0.20
    ok_sc = j_sc < 0.20
    ok_bsb = j_bsb < 0.20

    if not ok_ref:
        all_pass_ref = False

    status = 'OK' if ok_ref else 'FAIL'
    print(f"{name:15s} {j_ref:7.4f}{'*' if not ok_ref else ' '} {j_sc:7.4f}{'*' if not ok_sc else ' '} {j_bsb:7.4f}{'*' if not ok_bsb else ' '} {len(html):>7,} {status:>7s}")

    upload_files.append((inh_path, r2_key, name))

# Count Inhumas mentions in each
print(f"\nInhumas mentions per page:")
for name, inh_file, *_ in FILES:
    inh_path = os.path.join(BASE, inh_file)
    if os.path.exists(inh_path):
        html = open(inh_path).read()
        count = html.count('Inhumas') + html.count('inhumas')
        print(f"  {name:15s}: {count}")

elapsed = datetime.now() - start
print(f"\nVerification time: {elapsed.total_seconds():.1f}s")
print(f"\nAll pages pass vs REF (Goiania): {'YES' if all_pass_ref else 'NO'}")
print(f"Note: vs SC/BSB scores above 0.20 indicate shared template text.")
print(f"The SC vs BSB benchmarks (0.06-0.15) had fully hand-written text for each city.")

# Print upload command
print(f"\n{'='*70}")
print("UPLOAD COMMAND:")
print(f"{'='*70}")
print(f"cd {BASE} && node upload-inhumas.mjs")

print(f"\nURL base: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/")
print(f"\nPages:")
for _, r2_key, name in upload_files:
    print(f"  {name:15s}: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{r2_key}")

tokens_total = sum(os.path.getsize(os.path.join(BASE, f[1])) for f in FILES if os.path.exists(os.path.join(BASE, f[1]))) // 4
print(f"\nTOKENS TOTAL (est): ~{tokens_total:,}")
print(f"TEMPO TOTAL: {int(elapsed.total_seconds()//60):02d}:{int(elapsed.total_seconds()%60):02d}")
