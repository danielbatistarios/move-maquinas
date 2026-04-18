#!/usr/bin/env python3
"""
rebuild-inhumas-generic.py
Generic builder for all 6 Inhumas pages.
Reads ref-goiania-{service}.html, applies common replacements,
then applies service-specific text replacements.

Usage: python3 rebuild-inhumas-generic.py [articulada|combustao|tesoura|transpaleteira|curso|hub|all]
"""

import sys, time, re, os

BASE = '/Users/jrios/move-maquinas-seo'

# Inhumas context
CITY = 'Inhumas'
SLUG = 'inhumas-go'
LAT = '-16.3547'
LON = '-49.4952'
DIST = '40 km'
ROAD = 'GO-070'
POP = '53.000'

# Service configs
SERVICES = {
    'articulada': {
        'ref': 'ref-goiania-articulada.html',
        'out': f'{SLUG}-aluguel-de-plataforma-elevatoria-articulada-V2.html',
        'slug': 'aluguel-de-plataforma-elevatoria-articulada',
        'name_goi': 'Aluguel de Plataforma Elevatória Articulada em Goiânia',
        'name_inh': 'Locação de Plataforma Articulada em Inhumas',
        'bc_name_goi': 'Plataforma Articulada em Goiânia',
        'bc_name_inh': 'Plataforma Articulada em Inhumas',
        'script': 'rebuild-inhumas-articulada-v2.py',  # Has its own dedicated script
    },
    'combustao': {
        'ref': 'ref-goiania-combustao.html',
        'out': f'{SLUG}-aluguel-de-empilhadeira-combustao-V2.html',
        'slug': 'aluguel-de-empilhadeira-combustao',
        'name_goi': 'Aluguel de Empilhadeira a Combustão em Goiânia',
        'name_inh': 'Locação de Empilhadeira a Combustão em Inhumas',
        'bc_name_goi': 'Empilhadeira a Combustão em Goiânia',
        'bc_name_inh': 'Empilhadeira a Combustão em Inhumas',
        'script': 'rebuild-inhumas-combustao-v2.py',
    },
    'tesoura': {
        'ref': 'ref-goiania-tesoura.html',
        'out': f'{SLUG}-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
        'slug': 'aluguel-de-plataforma-elevatoria-tesoura',
        'name_goi': 'Aluguel de Plataforma Elevatória Tesoura em Goiânia',
        'name_inh': 'Locação de Plataforma Tesoura em Inhumas',
        'bc_name_goi': 'Plataforma Tesoura em Goiânia',
        'bc_name_inh': 'Plataforma Tesoura em Inhumas',
        'script': 'rebuild-inhumas-tesoura-v2.py',
    },
    'transpaleteira': {
        'ref': 'ref-goiania-transpaleteira.html',
        'out': f'{SLUG}-aluguel-de-transpaleteira-V2.html',
        'slug': 'aluguel-de-transpaleteira',
        'name_goi': 'Aluguel de Transpaleteira Elétrica em Goiânia',
        'name_inh': 'Locação de Transpaleteira Elétrica em Inhumas',
        'bc_name_goi': 'Transpaleteira Elétrica em Goiânia',
        'bc_name_inh': 'Transpaleteira Elétrica em Inhumas',
        'script': 'rebuild-inhumas-transpaleteira-v2.py',
    },
    'curso': {
        'ref': 'ref-goiania-curso.html',
        'out': f'{SLUG}-curso-de-operador-de-empilhadeira-V2.html',
        'slug': 'curso-de-operador-de-empilhadeira',
        'name_goi': 'Curso de Operador de Empilhadeira NR-11 em Goiânia',
        'name_inh': 'Treinamento NR-11 para Operadores de Empilhadeira em Inhumas',
        'bc_name_goi': 'Curso de Operador de Empilhadeira',
        'bc_name_inh': 'Curso NR-11 Empilhadeira',
        'script': 'rebuild-inhumas-curso-v2.py',
    },
    'hub': {
        'ref': 'ref-goiania-hub.html',
        'out': f'{SLUG}-hub-V2.html',
        'slug': '',
        'name_goi': '',
        'name_inh': '',
        'bc_name_goi': 'Goiania — GO',
        'bc_name_inh': 'Inhumas — GO',
        'script': 'rebuild-inhumas-hub-v2.py',
    },
}


def run_dedicated_script(svc_name):
    """Run the dedicated per-service script if it exists."""
    cfg = SERVICES[svc_name]
    script_path = os.path.join(BASE, cfg['script'])
    if os.path.exists(script_path):
        import subprocess
        t0 = time.time()
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True, text=True, cwd=BASE
        )
        elapsed = time.time() - t0
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr[:300])
        return elapsed
    else:
        print(f"⚠ Script not found: {script_path}")
        return 0


def verify_and_jaccard(svc_name):
    """Run Jaccard check for a built page."""
    cfg = SERVICES[svc_name]
    out_path = os.path.join(BASE, cfg['out'])
    if not os.path.exists(out_path):
        print(f"  FILE NOT FOUND: {out_path}")
        return False

    def extract_text(h):
        t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
        t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
        t = re.sub(r'<[^>]+>', ' ', t)
        return re.sub(r'\s+', ' ', t).strip().lower()

    def ngrams(text, n=3):
        words = text.split()
        return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

    def jaccard_sim(s1, s2):
        inter = len(s1 & s2); union = len(s1 | s2)
        return inter / union if union > 0 else 0.0

    with open(out_path) as f:
        new_ng = ngrams(extract_text(f.read()))

    all_pass = True
    ref_path = os.path.join(BASE, cfg['ref'])
    sc_slug_map = {
        'articulada': 'senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
        'combustao': 'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
        'tesoura': 'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
        'transpaleteira': 'senador-canedo-go-aluguel-de-transpaleteira-V2.html',
        'curso': 'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html',
        'hub': 'senador-canedo-go-hub-V2.html',
    }
    bsb_slug_map = {
        'articulada': 'brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html',
        'combustao': 'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html',
        'tesoura': 'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
        'transpaleteira': 'brasilia-df-aluguel-de-transpaleteira-V2.html',
        'curso': 'brasilia-df-curso-de-operador-de-empilhadeira-V2.html',
        'hub': 'brasilia-df-hub-V2.html',
    }

    comparisons = [
        ('ref-goiania', ref_path),
        ('senador-canedo', os.path.join(BASE, sc_slug_map.get(svc_name, ''))),
        ('brasilia-df', os.path.join(BASE, bsb_slug_map.get(svc_name, ''))),
    ]

    for label, comp_path in comparisons:
        if os.path.exists(comp_path):
            with open(comp_path) as f:
                comp_ng = ngrams(extract_text(f.read()))
            j = jaccard_sim(new_ng, comp_ng)
            status = '✓' if j < 0.20 else '✗ FALHOU'
            if j >= 0.20:
                all_pass = False
            print(f"  vs {label:20s}: {j:.4f}  {status}")
        else:
            print(f"  vs {label:20s}: FILE NOT FOUND")

    return all_pass


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 rebuild-inhumas-generic.py [articulada|combustao|tesoura|transpaleteira|curso|hub|all]")
        sys.exit(1)

    target = sys.argv[1]
    if target == 'all':
        targets = list(SERVICES.keys())
    else:
        targets = [target]

    total_start = time.time()
    results = {}

    for svc in targets:
        print(f"\n{'='*60}")
        print(f"BUILDING: {svc}")
        print(f"{'='*60}")

        elapsed = run_dedicated_script(svc)
        results[svc] = elapsed

    print(f"\n\n{'='*60}")
    print("JACCARD MATRIX — ALL BUILT PAGES")
    print(f"{'='*60}")

    all_pass = True
    for svc in targets:
        print(f"\n--- {svc} ---")
        if not verify_and_jaccard(svc):
            all_pass = False

    print(f"\n{'='*60}")
    for svc, elapsed in results.items():
        print(f"  {svc:20s}: {elapsed:.1f}s")
    print(f"  Total: {time.time()-total_start:.1f}s")
    print(f"\n{'✓ ALL PASS' if all_pass else '✗ FAILURES DETECTED'}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
