#!/usr/bin/env python3
"""
rebuild-inhumas-smart.py
Smart builder that generates Inhumas pages by:
1. Reading ref-goiania-{service}.html
2. Applying GENERIC structural replacements (coords, URLs, city refs)
3. Rewriting ALL major text paragraphs with Inhumas-specific content

This handles the common 80% of replacements automatically.
The remaining service-specific text is in per-service functions.

Usage: python3 rebuild-inhumas-smart.py [service|all]
"""
import sys, time, re, os

BASE = '/Users/jrios/move-maquinas-seo'
CITY = 'Inhumas'
SLUG = 'inhumas-go'
LAT, LON = '-16.3547', '-49.4952'
ROAD = 'GO-070'
DIST = '40 km'

# Service mapping
SVC_MAP = {
    'articulada': ('ref-goiania-articulada.html', f'{SLUG}-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'aluguel-de-plataforma-elevatoria-articulada'),
    'combustao': ('ref-goiania-combustao.html', f'{SLUG}-aluguel-de-empilhadeira-combustao-V2.html', 'aluguel-de-empilhadeira-combustao'),
    'tesoura': ('ref-goiania-tesoura.html', f'{SLUG}-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'aluguel-de-plataforma-elevatoria-tesoura'),
    'transpaleteira': ('ref-goiania-transpaleteira.html', f'{SLUG}-aluguel-de-transpaleteira-V2.html', 'aluguel-de-transpaleteira'),
    'curso': ('ref-goiania-curso.html', f'{SLUG}-curso-de-operador-de-empilhadeira-V2.html', 'curso-de-operador-de-empilhadeira'),
    'hub': ('ref-goiania-hub.html', f'{SLUG}-hub-V2.html', ''),
}

warn_count = 0

def r(html, old, new, count=1):
    global warn_count
    if old not in html:
        warn_count += 1
        if warn_count <= 5:
            print(f"  ⚠ NÃO ENCONTRADO: {old[:70]}...")
        return html
    return html.replace(old, new, count)


def apply_generic_replacements(html, svc_name):
    """Apply structural replacements common to all service pages."""
    ref_file, out_file, svc_slug = SVC_MAP[svc_name]

    # Geo coords
    html = r(html, 'content="Goiânia, Goiás, Brasil"', f'content="{CITY}, Goiás, Brasil"')
    html = r(html, 'content="-16.7234;-49.2654"', f'content="{LAT};{LON}"')
    html = r(html, 'content="-16.7234, -49.2654"', f'content="{LAT}, {LON}"')
    html = r(html, '"latitude": -16.7234, "longitude": -49.2654', f'"latitude": {LAT}, "longitude": {LON}')
    html = r(html, '"latitude": -16.7234', f'"latitude": {LAT}')
    html = r(html, '"longitude": -49.2654', f'"longitude": {LON}')

    # Schema areaServed
    html = r(html, '"name": "Goiânia", "addressRegion": "GO"', f'"name": "{CITY}", "addressRegion": "GO"')

    # Breadcrumb schema
    html = r(html, '"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
             f'"name": "Equipamentos em {CITY}", "item": "https://movemaquinas.com.br/{SLUG}/"')

    # Breadcrumb visual
    html = r(html, '<a href="/goiania-go/">Equipamentos em Goiânia</a>',
             f'<a href="/{SLUG}/">Equipamentos em {CITY}</a>')

    # WhatsApp encoded URLs — bulk
    html = r(html, 'Goi%C3%A2nia', CITY, 99)

    # Internal links — goiania-go -> inhumas-go
    for slug_part in ['aluguel-de-plataforma-elevatoria-tesoura', 'aluguel-de-plataforma-elevatoria-articulada',
                      'aluguel-de-empilhadeira-combustao', 'aluguel-de-transpaleteira',
                      'curso-operador-empilhadeira', 'curso-de-operador-de-empilhadeira']:
        html = r(html, f'/goiania-go/{slug_part}', f'/{SLUG}/{slug_part}', 99)

    # Map embed coords
    html = r(html, '!2d-49.2654!3d-16.7234', f'!2d{LON}!3d{LAT}')
    html = r(html, 'title="Localização Move Máquinas em Goiânia"',
             f'title="Área de atendimento Move Máquinas — {CITY}"')

    # Coverage hub link
    html = r(html, 'Todos os equipamentos em Goiânia</a>', f'Todos os equipamentos em {CITY}</a>')
    html = r(html, '/goiania-go/" style="color', f'/{SLUG}/" style="color')

    # Generic text replacements
    html = r(html, 'Entrega rápida em <span>Goiânia</span> e região metropolitana',
             f'Entrega rápida em <span>{CITY}</span> e cidades vizinhas')
    html = r(html, 'Entrega no mesmo dia em Goiânia', f'Entrega no mesmo dia via {ROAD}')
    html = r(html, f'Outros equipamentos disponíveis para locação em Goiânia:',
             f'Outros equipamentos disponíveis em {CITY}:')

    # Link anchor texts
    html = r(html, 'Aluguel de Plataforma Tesoura em Goiânia', f'Plataforma Tesoura em {CITY}')
    html = r(html, 'Aluguel de Plataforma Articulada em Goiânia', f'Plataforma Articulada em {CITY}')
    html = r(html, 'Aluguel de Empilhadeira a Combustão em Goiânia', f'Empilhadeira a Combustão em {CITY}')
    html = r(html, 'Aluguel de Transpaleteira em Goiânia', f'Transpaleteira Elétrica em {CITY}')
    html = r(html, 'Curso de Operador de Empilhadeira em Goiânia', f'Curso NR-11 em {CITY}')

    # Form selects — put Inhumas first
    html = r(html, '''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
             f'''              <option value="{CITY}" selected>{CITY}</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''', 2)

    # Marquee stats
    html = r(html, '<strong>200km</strong> raio de atendimento', f'<strong>{DIST}</strong> de {CITY}', 99)
    html = r(html, '<strong>+20</strong> anos de mercado', '<strong>+20</strong> anos atendendo GO', 99)
    html = r(html, '<strong>Clark</strong> exclusivo em Goiás', '<strong>Clark</strong> distribuidor autorizado', 99)

    # Generic section texts
    html = r(html, 'Entenda o equipamento', 'Conheça o equipamento')
    html = r(html, 'Publicado no canal oficial da Move Máquinas no YouTube.',
             'Canal oficial Move Máquinas no YouTube — mais de 50 vídeos sobre locação.')
    html = r(html, 'Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
             f'Informe modelo e prazo ao lado — retornamos pelo WhatsApp em até 2 horas com valor e disponibilidade para {CITY}.')

    return html


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


def check_jaccard(svc_name, html):
    ref_file = SVC_MAP[svc_name][0]
    ref_path = os.path.join(BASE, ref_file)

    new_ng = ngrams(extract_text(html))

    all_pass = True
    for label, path in [
        ('ref-goiania', ref_path),
        ('senador-canedo', os.path.join(BASE, f'senador-canedo-go-{SVC_MAP[svc_name][2]}-V2.html')),
        ('brasilia-df', os.path.join(BASE, f'brasilia-df-{SVC_MAP[svc_name][2]}-V2.html')),
    ]:
        if os.path.exists(path):
            with open(path) as f:
                comp_ng = ngrams(extract_text(f.read()))
            j = jaccard_sim(new_ng, comp_ng)
            status = '✓' if j < 0.20 else '✗ FALHOU'
            if j >= 0.20:
                all_pass = False
            print(f"  vs {label:20s}: {j:.4f}  {status}")
    return all_pass


def build_service(svc_name):
    """Build one service page using dedicated script if available, otherwise generic."""
    global warn_count
    warn_count = 0

    cfg = SVC_MAP[svc_name]
    script_path = os.path.join(BASE, f'rebuild-{SLUG.replace("-go","")}-{svc_name}-v2.py')
    # Check dedicated script
    dedicated = os.path.join(BASE, SERVICES_SCRIPTS.get(svc_name, ''))

    ref_path = os.path.join(BASE, cfg[0])
    out_path = os.path.join(BASE, cfg[1])

    # For articulada and combustao, we have dedicated scripts
    if svc_name in ('articulada', 'combustao') and os.path.exists(os.path.join(BASE, f'rebuild-inhumas-{svc_name}-v2.py')):
        import subprocess
        print(f"  Using dedicated script: rebuild-inhumas-{svc_name}-v2.py")
        result = subprocess.run(
            [sys.executable, os.path.join(BASE, f'rebuild-inhumas-{svc_name}-v2.py')],
            capture_output=True, text=True, cwd=BASE
        )
        print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
        return

    # Otherwise, apply generic replacements
    print(f"  Applying generic replacements to {cfg[0]}...")
    with open(ref_path) as f:
        html = f.read()

    html = apply_generic_replacements(html, svc_name)

    # Save
    with open(out_path, 'w') as f:
        f.write(html)

    print(f"  Warnings: {warn_count}")
    print(f"  Saved: {out_path}")
    print(f"  Size: {len(html):,}")


SERVICES_SCRIPTS = {
    'articulada': 'rebuild-inhumas-articulada-v2.py',
    'combustao': 'rebuild-inhumas-combustao-v2.py',
    'tesoura': 'rebuild-inhumas-tesoura-v2.py',
    'transpaleteira': 'rebuild-inhumas-transpaleteira-v2.py',
    'curso': 'rebuild-inhumas-curso-v2.py',
    'hub': 'rebuild-inhumas-hub-v2.py',
}


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    targets = list(SVC_MAP.keys()) if target == 'all' else [target]

    total_start = time.time()

    for svc in targets:
        print(f"\n{'='*60}")
        print(f"SERVICE: {svc}")
        print(f"{'='*60}")

        t0 = time.time()

        # Try dedicated script first
        script = os.path.join(BASE, f'rebuild-inhumas-{svc}-v2.py')
        if os.path.exists(script):
            import subprocess
            result = subprocess.run([sys.executable, script], capture_output=True, text=True, cwd=BASE)
            # Show last 15 lines
            lines = result.stdout.strip().split('\n')
            for line in lines[-15:]:
                print(f"  {line}")
        else:
            print(f"  ⚠ No dedicated script found: rebuild-inhumas-{svc}-v2.py")
            build_service(svc)

        elapsed = time.time() - t0
        print(f"  Elapsed: {elapsed:.1f}s")

    # Final Jaccard check
    print(f"\n\n{'='*60}")
    print("FINAL JACCARD CHECK")
    print(f"{'='*60}")

    all_pass = True
    for svc in targets:
        out_path = os.path.join(BASE, SVC_MAP[svc][1])
        if os.path.exists(out_path):
            with open(out_path) as f:
                html = f.read()
            print(f"\n--- {svc} ---")
            if not check_jaccard(svc, html):
                all_pass = False
        else:
            print(f"\n--- {svc} --- FILE NOT FOUND")
            all_pass = False

    total = time.time() - total_start
    print(f"\n{'='*60}")
    print(f"TOTAL TIME: {total:.1f}s")
    print(f"RESULT: {'✓ ALL PASS' if all_pass else '✗ FAILURES'}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
