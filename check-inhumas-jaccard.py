#!/usr/bin/env python3
"""Check Jaccard for all 6 Inhumas pages vs ref, SC, BSB"""
import re, os

def extract_text(h):
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t).strip().lower()

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(s1, s2):
    i = len(s1 & s2); u = len(s1 | s2)
    return i/u if u else 0

services = [
    ('articulada', 'aluguel-de-plataforma-elevatoria-articulada'),
    ('combustao', 'aluguel-de-empilhadeira-combustao'),
    ('tesoura', 'aluguel-de-plataforma-elevatoria-tesoura'),
    ('transpaleteira', 'aluguel-de-transpaleteira'),
    ('curso', 'curso-de-operador-de-empilhadeira'),
    ('hub', 'hub'),
]

print('SERVICE          | vs REF-GOI | vs SC      | vs BSB     |')
print('-'*65)
fails = 0
for name, slug in services:
    inh = f'inhumas-go-{slug}-V2.html'
    ref = f'ref-goiania-{"hub" if slug=="hub" else name}.html'
    sc = f'senador-canedo-go-{slug}-V2.html'
    bsb = f'brasilia-df-{slug}-V2.html'

    if not os.path.exists(inh):
        print(f'{name:17s}| NOT FOUND')
        fails += 1
        continue

    inh_ng = ngrams(extract_text(open(inh).read()))
    row = f'{name:17s}|'
    for label, comp in [('REF', ref), ('SC', sc), ('BSB', bsb)]:
        if os.path.exists(comp):
            j = jaccard(inh_ng, ngrams(extract_text(open(comp).read())))
            ok = j < 0.20
            if not ok: fails += 1
            row += f' {j:.4f} {"P" if ok else "F"} |'
        else:
            row += f' N/A        |'
    print(row)

print(f'\nFAILURES: {fails}')
