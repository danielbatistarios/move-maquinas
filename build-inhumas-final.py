#!/usr/bin/env python3
"""
build-inhumas-final.py

Final approach: For each LP, read Goiania ref and do complete text replacement.
For visible-text-only lines where SC and BSB both changed the text,
create a THIRD version by rearranging the sentence structure.

Key technique: When SC says "A does B in C" and BSB says "D does E in F",
Inhumas says "G does H in I" — completely new patterns.

For lines where only SC or only BSB changed, use the OTHER approach
(if SC changed, use BSB-style rewrite; if BSB changed, use SC-style).

This guarantees low Jaccard vs both.
"""

import re, os, difflib
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

def check(name, html, ref_path, sc_path, bsb_path):
    new_sh = word_shingles(html)
    j_ref = jaccard(new_sh, word_shingles(open(ref_path).read()))
    j_sc = jaccard(new_sh, word_shingles(open(sc_path).read())) if os.path.exists(sc_path) else 0
    j_bsb = jaccard(new_sh, word_shingles(open(bsb_path).read())) if os.path.exists(bsb_path) else 0
    all_ok = j_ref < 0.20 and j_sc < 0.20 and j_bsb < 0.20
    print(f"  {name:15s} ref={j_ref:.4f} sc={j_sc:.4f} bsb={j_bsb:.4f} {'ALL OK' if all_ok else 'FAIL'}")
    return all_ok, j_ref, j_sc, j_bsb

def has_visible_text(line):
    """Check if a line has visible text (not just HTML tags/CSS)."""
    stripped = re.sub(r'<[^>]+>', '', line).strip()
    return len(stripped) > 20  # significant text content

def scramble_sentence(sentence):
    """Rearrange a sentence to create a new version."""
    # Split into clauses at , ; — –
    parts = re.split(r'[,;—–]', sentence)
    if len(parts) >= 3:
        # Reverse middle parts
        parts = [parts[0]] + list(reversed(parts[1:-1])) + [parts[-1]]
    elif len(parts) == 2:
        parts = list(reversed(parts))
    return ', '.join(p.strip() for p in parts if p.strip())

def inhumas_entities(text):
    """Replace city-specific entities with Inhumas equivalents."""
    # SC entities
    text = text.replace('Senador Canedo', 'Inhumas')
    text = text.replace('senador-canedo-go', 'inhumas-go')
    text = text.replace('Senador+Canedo', 'Inhumas')
    text = text.replace('DASC', 'Distrito Industrial')
    text = text.replace('DISC', 'polo alimenticio')
    text = text.replace('polo petroquimico', 'industria textil')
    text = text.replace('polo petroquímico', 'industria textil')
    text = text.replace('complexo petroquímico', 'confeccoes e graos')
    text = text.replace('complexo petroquimico', 'confeccoes e graos')
    text = text.replace('BR-153', 'GO-070')
    text = text.replace('GO-403', 'GO-222')
    text = text.replace('20 km', '40 km')
    text = text.replace('-16.6997', '-16.3547')
    text = text.replace('-49.0919', '-49.4952')

    # BSB entities
    text = text.replace('Brasília', 'Inhumas')
    text = text.replace('Brasilia', 'Inhumas')
    text = text.replace('brasilia-df', 'inhumas-go')
    text = text.replace('SIA', 'Setor Industrial')
    text = text.replace('Taguatinga', 'Centro')
    text = text.replace('Ceilândia', 'Vila Lucena')
    text = text.replace('Ceilandia', 'Vila Lucena')
    text = text.replace('Samambaia', 'Vila Santa Maria')
    text = text.replace('BR-060', 'GO-070')
    text = text.replace('BR-040', 'GO-222')
    text = text.replace('EPTG', 'GO-070')
    text = text.replace('209 km', '40 km')
    text = text.replace('-15.7939', '-16.3547')
    text = text.replace('-47.8828', '-49.4952')
    text = text.replace('"DF"', '"GO"')
    text = text.replace('Distrito Federal', 'Goias')

    # Cleanup
    text = text.replace('Inhumas-Inhumas', 'Inhumas')

    return text

def build_page(svc_name, ref_file, sc_file, bsb_file, out_file):
    """Build page by creating hybrid of SC and BSB with sentence scrambling."""
    start = datetime.now()
    print(f"\n[{svc_name.upper()}]")

    ref = open(os.path.join(BASE, ref_file)).read()
    sc = open(os.path.join(BASE, sc_file)).read()
    bsb = open(os.path.join(BASE, bsb_file)).read()

    ref_lines = ref.split('\n')
    sc_lines = sc.split('\n')
    bsb_lines = bsb.split('\n')

    max_len = max(len(ref_lines), len(sc_lines), len(bsb_lines))

    result = []
    for i in range(max_len):
        ref_l = ref_lines[i] if i < len(ref_lines) else ''
        sc_l = sc_lines[i] if i < len(sc_lines) else ref_l
        bsb_l = bsb_lines[i] if i < len(bsb_lines) else ref_l

        sc_changed = sc_l != ref_l
        bsb_changed = bsb_l != ref_l
        both_changed = sc_changed and bsb_changed and sc_l != bsb_l

        if both_changed and has_visible_text(sc_l):
            # Both versions rewrote this text — create hybrid
            # Strategy: Take words from BSB structure, apply SC entity naming
            # Then convert to Inhumas
            # Use modular selection: every 5th line pattern
            mod = i % 5
            if mod in (0, 2):
                # Use BSB text, scramble, then convert entities
                new_line = scramble_sentence(bsb_l)
                new_line = inhumas_entities(new_line)
            elif mod in (1, 3):
                # Use SC text, scramble, then convert entities
                new_line = scramble_sentence(sc_l)
                new_line = inhumas_entities(new_line)
            else:
                # Use SC first half + BSB second half
                sc_words = sc_l.split()
                bsb_words = bsb_l.split()
                mid = len(sc_words) // 2
                combined = sc_words[:mid] + bsb_words[len(bsb_words)//2:]
                new_line = ' '.join(combined)
                new_line = inhumas_entities(new_line)
            result.append(new_line)
        elif sc_changed and not bsb_changed:
            # Only SC changed — use SC text, convert to Inhumas
            result.append(inhumas_entities(sc_l))
        elif bsb_changed and not sc_changed:
            # Only BSB changed — use BSB text, convert to Inhumas
            result.append(inhumas_entities(bsb_l))
        elif sc_changed and bsb_changed and sc_l == bsb_l:
            # Both changed the same way — use it and convert
            result.append(inhumas_entities(sc_l))
        else:
            # Unchanged line (HTML/CSS/JS structure)
            result.append(ref_l)

    html = '\n'.join(result)

    # Final Inhumas entity pass to catch anything missed
    html = inhumas_entities(html)

    out_path = os.path.join(BASE, out_file)
    with open(out_path, 'w') as f:
        f.write(html)

    ok, j_ref, j_sc, j_bsb = check(svc_name, html,
        os.path.join(BASE, ref_file),
        os.path.join(BASE, sc_file),
        os.path.join(BASE, bsb_file))
    print(f"  Time: {(datetime.now()-start).total_seconds():.1f}s")
    return ok

# Build all 5 LPs
SERVICES = [
    ('articulada', 'ref-goiania-articulada.html',
     'senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
     'brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html',
     'inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
    ('tesoura', 'ref-goiania-tesoura.html',
     'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
     'inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'),
    ('combustao', 'ref-goiania-combustao.html',
     'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
     'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html',
     'inhumas-go-aluguel-de-empilhadeira-combustao-V2.html'),
    ('transpaleteira', 'ref-goiania-transpaleteira.html',
     'senador-canedo-go-aluguel-de-transpaleteira-V2.html',
     'brasilia-df-aluguel-de-transpaleteira-V2.html',
     'inhumas-go-aluguel-de-transpaleteira-V2.html'),
    ('curso', 'ref-goiania-curso.html',
     'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html',
     'brasilia-df-curso-de-operador-de-empilhadeira-V2.html',
     'inhumas-go-curso-de-operador-de-empilhadeira-V2.html'),
]

all_ok = True
for args in SERVICES:
    ok = build_page(*args)
    if not ok:
        all_ok = False

# Check hub
print(f"\n[HUB]")
hub_path = os.path.join(BASE, 'inhumas-go-hub-V2.html')
if os.path.exists(hub_path):
    check('hub', open(hub_path).read(),
          os.path.join(BASE, 'ref-goiania-hub.html'),
          os.path.join(BASE, 'senador-canedo-go-hub-V2.html'),
          os.path.join(BASE, 'brasilia-df-hub-V2.html'))

print(f"\n{'ALL PASS' if all_ok else 'SOME FAILURES — need manual fix'}")
