#!/usr/bin/env python3
import re, os

BASE = '/Users/jrios/move-maquinas-seo'

def ws(text, n=3):
    clean = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'https?://\S+', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    words = clean.split()
    return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1))

def j(f1, f2):
    s1 = ws(open(os.path.join(BASE, f1)).read())
    s2 = ws(open(os.path.join(BASE, f2)).read())
    inter = s1 & s2
    union = s1 | s2
    return len(inter)/len(union) if union else 0

# Check SC vs BSB for articulada
print(f"SC vs BSB articulada: {j('senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html'):.4f}")

# Check all 6 Inhumas pages vs ref, SC, BSB
pages = [
    ('inhumas-go-hub-V2.html', 'ref-goiania-hub.html', 'senador-canedo-go-hub-V2.html', 'brasilia-df-hub-V2.html'),
    ('inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'ref-goiania-articulada.html', 'senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
    ('inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'ref-goiania-tesoura.html', 'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'),
    ('inhumas-go-aluguel-de-empilhadeira-combustao-V2.html', 'ref-goiania-combustao.html', 'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html', 'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html'),
    ('inhumas-go-aluguel-de-transpaleteira-V2.html', 'ref-goiania-transpaleteira.html', 'senador-canedo-go-aluguel-de-transpaleteira-V2.html', 'brasilia-df-aluguel-de-transpaleteira-V2.html'),
    ('inhumas-go-curso-de-operador-de-empilhadeira-V2.html', 'ref-goiania-curso.html', 'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html', 'brasilia-df-curso-de-operador-de-empilhadeira-V2.html'),
]

print(f"\n{'Page':50s} {'vs REF':>8s} {'vs SC':>8s} {'vs BSB':>8s}")
print("-" * 80)
for inh, ref, sc, bsb in pages:
    inh_p = os.path.join(BASE, inh)
    ref_p = os.path.join(BASE, ref)
    sc_p = os.path.join(BASE, sc)
    bsb_p = os.path.join(BASE, bsb)
    if not os.path.exists(inh_p):
        print(f"{inh:50s} NOT FOUND")
        continue
    j_ref = j(inh, ref)
    j_sc = j(inh, sc) if os.path.exists(sc_p) else -1
    j_bsb = j(inh, bsb) if os.path.exists(bsb_p) else -1
    status_ref = 'OK' if j_ref < 0.20 else 'FAIL'
    status_sc = 'OK' if j_sc < 0.20 else ('FAIL' if j_sc >= 0 else 'N/A')
    status_bsb = 'OK' if j_bsb < 0.20 else ('FAIL' if j_bsb >= 0 else 'N/A')
    print(f"{inh:50s} {j_ref:7.4f}{status_ref:>5s} {j_sc:7.4f}{status_sc:>5s} {j_bsb:7.4f}{status_bsb:>5s}")
