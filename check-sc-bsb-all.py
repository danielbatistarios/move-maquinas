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
    p1, p2 = os.path.join(BASE, f1), os.path.join(BASE, f2)
    if not os.path.exists(p1) or not os.path.exists(p2): return -1
    s1, s2 = ws(open(p1).read()), ws(open(p2).read())
    inter = s1 & s2; union = s1 | s2
    return len(inter)/len(union) if union else 0

pairs = [
    ('hub', 'senador-canedo-go-hub-V2.html', 'brasilia-df-hub-V2.html'),
    ('articulada', 'senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
    ('tesoura', 'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'),
    ('combustao', 'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html', 'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html'),
    ('transpaleteira', 'senador-canedo-go-aluguel-de-transpaleteira-V2.html', 'brasilia-df-aluguel-de-transpaleteira-V2.html'),
    ('curso', 'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html', 'brasilia-df-curso-de-operador-de-empilhadeira-V2.html'),
]

for name, sc, bsb in pairs:
    score = j(sc, bsb)
    print(f"SC vs BSB {name:15s}: {score:.4f} {'OK' if score < 0.20 else 'OVER'}")
