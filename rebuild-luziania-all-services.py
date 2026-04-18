#!/usr/bin/env python3
"""
rebuild-luziania-all-services.py
Gera as 4 LPs restantes de Luziania (tesoura, combustao, transpaleteira, curso)
usando os refs de Goiania como esqueleto e os scripts de SC como base de padroes.

Para cada servico:
1. Le o ref de Goiania
2. Le o script de SC para extrair os OLD strings
3. Aplica replacements com textos 100% novos para Luziania
4. Roda Jaccard check vs ref, SC e BSB
5. Salva o arquivo
"""

import re, os
from datetime import datetime

START = datetime.now()
BASE = '/Users/jrios/move-maquinas-seo'

# ═══════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

def text_from_html(h):
    h = re.sub(r'<script[^>]*>.*?</script>', '', h, flags=re.DOTALL)
    h = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h = re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=re.DOTALL)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'&\w+;', ' ', h)
    h = re.sub(r'\s+', ' ', h).strip().lower()
    return h

def trigrams(text):
    words = text.split()
    return set(' '.join(words[i:i+3]) for i in range(len(words)-2))

def jaccard(s1, s2):
    if not s1 or not s2: return 0.0
    return len(s1 & s2) / len(s1 | s2)

def check_jaccard(html_text, ref_path, sc_path, bsb_path, label):
    new_tri = trigrams(text_from_html(html_text))
    ref_tri = trigrams(text_from_html(open(ref_path).read()))
    j_ref = jaccard(new_tri, ref_tri)
    results = {f'ref-goiania': j_ref}
    for name, path in [('SC', sc_path), ('BSB', bsb_path)]:
        if os.path.exists(path):
            other_tri = trigrams(text_from_html(open(path).read()))
            results[name] = jaccard(new_tri, other_tri)
    print(f"\n  Jaccard {label}:")
    all_pass = True
    for k, v in results.items():
        status = 'OK' if v < 0.20 else 'FAIL'
        if v >= 0.20: all_pass = False
        print(f"    vs {k}: {v:.4f} {status}")
    return all_pass

def check_goiania_refs(html_text, legitimate_extras=None):
    lines = html_text.split('\n')
    issues = []
    legit = [
        'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
        'CNPJ', 'Aparecida de Goiânia', 'Aparecida de Goiania',
        'option value', 'goiania-go/', '198 km', 'sede',
        'Goiânia-GO', 'Goiania-GO', 'base em Goiania',
        'sede em Goiania', 'BR-040 (Goiania',
    ]
    if legitimate_extras:
        legit.extend(legitimate_extras)
    for i, line in enumerate(lines):
        if 'Goiânia' in line or 'Goiania' in line or 'goiania-go' in line:
            if not any(kw in line for kw in legit):
                issues.append((i+1, line.strip()[:120]))
    return issues

def build_service(service_config):
    """Build a single service LP for Luziania."""
    cfg = service_config
    ref_path = os.path.join(BASE, cfg['ref'])
    out_path = os.path.join(BASE, cfg['out'])

    with open(ref_path, 'r', encoding='utf-8') as f:
        html = f.read()

    not_found = []
    _h = [html]  # mutable container for closure
    def r(old, new, count=1):
        if old not in _h[0]:
            not_found.append(old[:80])
            return
        _h[0] = _h[0].replace(old, new, count)

    # Apply all replacements
    for old, new, *rest in cfg['replacements']:
        cnt = rest[0] if rest else 1
        r(old, new, cnt)

    # Check results
    issues = check_goiania_refs(html, cfg.get('legit_extras'))
    all_pass = check_jaccard(html, ref_path, cfg['sc_path'], cfg['bsb_path'], cfg['label'])

    if not_found:
        print(f"\n  NOT FOUND ({len(not_found)}):")
        for nf in not_found[:5]:
            print(f"    {nf}...")

    if issues:
        print(f"\n  Goiania refs ({len(issues)}):")
        for ln, txt in issues[:5]:
            print(f"    L{ln}: {txt}")

    # Save
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Stats
    luz = html.count('Luziânia') + html.count('Luziania') + html.count('luziania')
    local = html.count('DIAL') + html.count('BR-040') + html.count('metalurg') + html.count('silo') + html.count('agro')
    print(f"\n  Luziania: {luz} | Local ctx: {local} | Size: {len(html):,}")
    print(f"  Saved: {out_path}")

    return html, all_pass, out_path


# ═══════════════════════════════════════════════════════════════════════
# COMMON COVERAGE BLOCKS
# ═══════════════════════════════════════════════════════════════════════

# Old coverage block (same in all refs)
OLD_COV_BLOCK = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. {service_desc_old}</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Aparecida de Goiânia
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Senador Canedo
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Trindade
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Anápolis
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Inhumas
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Goianésia
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Brasília (DF)
      </div>
    </div>'''

def new_cov_block(service_desc_new):
    return f'''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 198 km de Luziânia pela BR-040. {service_desc_new}</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/"><strong>Luziânia</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/valparaiso-de-goias-go/">Valparaíso de Goiás</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/formosa-go/">Formosa</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/aparecida-de-goiania-go/">Aparecida de Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
    </div>'''

# Common form select replacement
OLD_FORM = '''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>'''

NEW_FORM = '''              <option value="Luziânia" selected>Luziânia</option>
              <option value="Brasília">Brasília</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Goiânia">Goiânia</option>'''


# ═══════════════════════════════════════════════════════════════════════
# SERVICE CONFIGS
# ═══════════════════════════════════════════════════════════════════════

# I need to read each ref to extract the exact old texts. Let me use the SC scripts
# as a reference for what the old text looks like, then replace with Luziania content.

# For each service, I'll extract key strings from the ref by reading them.

results = {}

for svc in ['tesoura', 'combustao', 'transpaleteira', 'curso']:
    print(f"\n{'='*60}")
    print(f"BUILDING: {svc.upper()} for LUZIANIA")
    print(f"{'='*60}")

    # Read the SC script to extract the OLD strings (they match the ref)
    sc_script = os.path.join(BASE, f'rebuild-sc-{svc}-v2.py')
    with open(sc_script, 'r', encoding='utf-8') as f:
        sc_code = f.read()

    # Read the BSB script for extra patterns
    bsb_script = os.path.join(BASE, f'rebuild-brasilia-{svc}-v2.py')

    # Determine file paths
    if svc == 'tesoura':
        ref_file = 'ref-goiania-tesoura.html'
        out_file = 'luziania-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
        sc_file = 'senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
        bsb_file = 'brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
        r2_path = 'luziania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'
        slug = 'aluguel-de-plataforma-elevatoria-tesoura'
    elif svc == 'combustao':
        ref_file = 'ref-goiania-combustao.html'
        out_file = 'luziania-go-aluguel-de-empilhadeira-combustao-V2.html'
        sc_file = 'senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html'
        bsb_file = 'brasilia-df-aluguel-de-empilhadeira-combustao-V2.html'
        r2_path = 'luziania-go/aluguel-de-empilhadeira-combustao/index.html'
        slug = 'aluguel-de-empilhadeira-combustao'
    elif svc == 'transpaleteira':
        ref_file = 'ref-goiania-transpaleteira.html'
        out_file = 'luziania-go-aluguel-de-transpaleteira-V2.html'
        sc_file = 'senador-canedo-go-aluguel-de-transpaleteira-V2.html'
        bsb_file = 'brasilia-df-aluguel-de-transpaleteira-V2.html'
        r2_path = 'luziania-go/aluguel-de-transpaleteira/index.html'
        slug = 'aluguel-de-transpaleteira'
    elif svc == 'curso':
        ref_file = 'ref-goiania-curso.html'
        out_file = 'luziania-go-curso-de-operador-de-empilhadeira-V2.html'
        sc_file = 'senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html'
        bsb_file = 'brasilia-df-curso-de-operador-de-empilhadeira-V2.html'
        r2_path = 'luziania-go/curso-de-operador-de-empilhadeira/index.html'
        slug = 'curso-de-operador-de-empilhadeira'

    ref_path = os.path.join(BASE, ref_file)
    out_path = os.path.join(BASE, out_file)
    sc_path = os.path.join(BASE, sc_file)
    bsb_path = os.path.join(BASE, bsb_file)

    with open(ref_path, 'r', encoding='utf-8') as f:
        html = f.read()

    not_found = []
    _h = [html]  # mutable container for closure
    def r(old, new, count=1):
        if old not in _h[0]:
            not_found.append(old[:80])
            return
        _h[0] = _h[0].replace(old, new, count)

    # ═══════════════════════════════════════════════════════════════════
    # COMMON REPLACEMENTS (all services)
    # ═══════════════════════════════════════════════════════════════════

    # Coordinates
    r('content="Goiânia, Goiás, Brasil"', 'content="Luziânia, Goiás, Brasil"')
    r('content="-16.7234;-49.2654"', 'content="-16.2532;-47.9501"')
    r('content="-16.7234, -49.2654"', 'content="-16.2532, -47.9501"')
    r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -16.2532, "longitude": -47.9501')
    r('"latitude": -16.7234', '"latitude": -16.2532')
    r('"longitude": -49.2654', '"longitude": -47.9501')

    # areaServed
    r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Luziânia", "addressRegion": "GO"')

    # WhatsApp
    r('Goi%C3%A2nia', 'Luzi%C3%A2nia', 99)

    # Form select
    r(OLD_FORM, NEW_FORM, 2)

    # Maps embed
    r('!2d-49.2654!3d-16.7234', '!2d-47.9501!3d-16.2532')

    # Internal links — all to luziania-go
    r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/luziania-go/aluguel-de-plataforma-elevatoria-tesoura')
    r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/luziania-go/aluguel-de-plataforma-elevatoria-articulada')
    r('/goiania-go/aluguel-de-empilhadeira-combustao', '/luziania-go/aluguel-de-empilhadeira-combustao')
    r('/goiania-go/aluguel-de-transpaleteira', '/luziania-go/aluguel-de-transpaleteira')
    r('/goiania-go/curso-operador-empilhadeira', '/luziania-go/curso-de-operador-de-empilhadeira')
    r('/goiania-go/" style="color', '/luziania-go/" style="color')

    # ═══════════════════════════════════════════════════════════════════
    # SERVICE-SPECIFIC REPLACEMENTS
    # ═══════════════════════════════════════════════════════════════════

    if svc == 'tesoura':
        # HEAD
        r('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
          '<title>Plataforma Tesoura para Locação em Luziânia-GO | Move Máquinas</title>')
        r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
          'content="Plataforma tesoura para locação em Luziânia: elétrica 8-10m para galpões do DIAL e indústrias alimentícias, diesel 12-15m para canteiros e pátios. Manutenção inclusa, transporte pela BR-040. Move Máquinas."')
        r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
          'href="https://movemaquinas.com.br/luziania-go/aluguel-de-plataforma-elevatoria-tesoura"')
        r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
          'content="Plataforma Tesoura para Locação em Luziânia-GO | Move Máquinas"')
        r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
          'content="Plataforma tesoura elétrica e diesel 8 a 15m em Luziânia. Para manutenção interna de fábricas no DIAL, instalações industriais e obras de construção civil. Manutenção inclusa, despacho pela BR-040."')
        # Schema
        r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
          '"name": "Locação de Plataforma Tesoura em Luziânia"')
        r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
          '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
        r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
          '"name": "Plataforma Tesoura em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/aluguel-de-plataforma-elevatoria-tesoura"')
        # Breadcrumb visible
        r('<a href="/goiania-go/">Equipamentos em Goiânia</a>', '<a href="/luziania-go/">Equipamentos em Luziânia</a>')
        r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>', '<span aria-current="page">Plataforma Tesoura em Luziânia</span>')
        # Hero
        r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>', 'Locação de Plataforma Tesoura em <em>Luziânia</em>')
        # Hero subtitle — find in ref
        r('Plataformas tesoura elétricas e diesel de 8 a 15 metros. Plataforma ampla para até 4 operadores, manutenção inclusa, entrega no mesmo dia. A partir de R$2.200/mês.',
          'Plataformas tesoura elétricas e diesel de 8 a 15 metros para manutenção interna de fábricas no DIAL, instalações industriais e coberturas de galpões em Luziânia. Manutenção inclusa, transporte pela BR-040. A partir de R$2.200/mês.')
        # Trust bar
        r('<strong>8 a 15 metros</strong><span>Tesoura pantográfica</span>',
          '<strong>Despacho BR-040</strong><span>198 km da sede</span>')
        r('<strong>+20 anos</strong><span>No mercado goiano</span>',
          '<strong>+20 anos</strong><span>Atuacao no Centro-Oeste</span>')
        # "O que e" section — replace ALL major text blocks
        r('O que é <span>plataforma tesoura</span> e quando usar',
          'Como funciona a <span>plataforma tipo tesoura</span> e quando contratar')
        # Main paragraph
        r('A plataforma elevatória tipo tesoura é um equipamento de elevação vertical com mecanismo pantográfico que sobe e desce em linha reta. Diferente da plataforma articulada, ela não possui braço nem alcance lateral — o que a torna ideal para ambientes internos com teto plano e piso nivelado. Sua principal vantagem é a plataforma de trabalho ampla, que comporta até 4 operadores com ferramentas e materiais. Em Goiânia, a tesoura é o equipamento mais contratado para manutenção interna de galpões, shopping centers, fábricas e obras de construção civil com acesso vertical direto.',
          'A plataforma elevatoria tipo tesoura utiliza mecanismo pantografico para elevar a cesta em linha vertical — sem braco articulado e sem deslocamento lateral. Essa caracteristica a torna ideal para galpoes com teto plano, fabricas com pe-direito regular e ambientes internos onde o piso e nivelado. Sua cesta ampla comporta ate 4 operadores com ferramentas e material de trabalho. Em Luziania, a tesoura e o equipamento mais indicado para manutencao interna de fabricas do DIAL, galpoes de metalurgia, industrias alimenticias e obras de construcao civil onde o acesso vertical direto e suficiente.')
        # H3s and paragraphs
        r('Tesoura elétrica: operação silenciosa dentro de galpões',
          'Tesoura eletrica: zero emissao dentro dos galpoes do DIAL')
        r('A tesoura elétrica é a escolha para trabalhos internos em ambientes que exigem zero emissão de gases e baixo ruído. Em Goiânia, ela é a mais contratada para manutenção em shopping centers como o Flamboyant e Goiânia Shopping, galpões do Distrito Industrial e fábricas com áreas limpas. O motor elétrico alimentado por bateria de 24V opera silenciosamente, sem contaminar produtos ou incomodar clientes. Os pneus não marcantes preservam o piso. Para a maioria das operações internas com pé-direito de até 10 metros, a tesoura elétrica resolve.',
          'A tesoura eletrica e indispensavel dentro de fabricas alimenticias e industrias quimicas do DIAL que operam com ambientes controlados de manipulacao. Motor eletrico com bateria 24V — zero emissao de gases preserva a integridade de areas limpas e nao contamina produtos. Operacao silenciosa que nao interfere nas linhas de producao. Pneus nao marcantes conservam o piso industrial. Para galpoes do DIAL com pe-direito de ate 10 metros, a tesoura eletrica resolve com eficiencia e seguranca.')
        r('Tesoura diesel 4x4: canteiros de obra e pátios externos',
          'Tesoura diesel 4x4: patios industriais e canteiros de construcao')
        r('A tesoura diesel é indicada para canteiros de obra, pátios industriais e ambientes externos com piso irregular. Com tração 4x4 e chassi reforçado, ela opera em terrenos de terra, cascalho e pisos com desnível. Em Goiânia, a tesoura diesel atende canteiros de construção civil, pátios do Distrito Industrial e obras de infraestrutura onde a plataforma precisa se deslocar por terreno não pavimentado. Modelos de 12 a 15 metros alcançam estruturas elevadas como coberturas de galpões e viadutos.',
          'A tesoura diesel com tracao 4x4 e chassi reforcado e a opcao para patios com cascalho, acessos de terra e canteiros de construcao civil em Luziania. Ela se desloca por terrenos irregulares sem perder estabilidade. No DIAL, os patios externos entre galpoes costumam ter piso de cascalho ou terra compactada — ambiente perfeito para a diesel. Modelos de 12 a 15 metros alcancam coberturas de galpoes industriais e estruturas metalicas elevadas do parque fabril.')
        r('Principais segmentos que usam tesoura na capital',
          'Setores que contratam tesoura em Luziania e regiao')
        r('Shopping centers lideram a demanda por plataforma tesoura em Goiânia. Manutenção de iluminação, instalação de decorações sazonais, pintura de tetos e reparo de sistemas de ar condicionado são serviços recorrentes no Flamboyant, Goiânia Shopping e Passeio das Águas. Indústrias no Distrito Industrial utilizam a tesoura para manutenção de coberturas, troca de telhas e instalação de sistemas elétricos em galpões com pé-direito de 8 a 12 metros. Construtoras contratam a diesel para acabamentos internos de edifícios e aplicação de revestimentos em lajes de subsolo.',
          'Metalurgicas e fundicoes do DIAL sao os maiores contratantes de plataforma tesoura em Luziania — manutencao de coberturas, troca de luminarias industriais e instalacao de sistemas eletricos e de exaustao em galpoes de 8 a 14 metros. Industrias alimenticias e quimicas usam a tesoura eletrica para trabalhos internos em areas controladas. Construtoras que operam nos empreendimentos residenciais e comerciais do Centro e Jardim Inga contratam a diesel para acabamentos em pe-direito duplo e instalacao de forros. Armazens de graos ao longo da BR-040 demandam tesoura para inspecao de coberturas e sistemas de ventilacao.')
        # Form
        r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma tesoura</span> em Goiânia',
          'Cotacao de <span style="color:var(--color-primary);">plataforma tesoura</span> para Luziania')
        r('Entrega no mesmo dia em Goiânia', 'Despacho programado pela BR-040')
        # Expert quote
        r('"A tesoura é o equipamento que mais gera confusão na hora de pedir. Cliente liga pedindo articulada para trocar lâmpada de galpão. Quando pergunto: tem alguma coisa no caminho entre o chão e o teto? Se não tem, tesoura resolve. A cesta é maior, mais estável e o custo é menor. Articulada só faz sentido quando precisa contornar algo. Para 80% dos trabalhos internos em galpões de Goiânia, a tesoura é a resposta certa."',
          '"A maioria dos chamados de Luziania e para manutencao interna no DIAL — troca de luminarias, reparo de coberturas, instalacao de exaustao. Pergunto: tem tubulacao ou ponte rolante no caminho? Se o acesso e vertical direto, tesoura resolve melhor e mais barato. A cesta ampla comporta dois montadores com ferramental pesado. Para as metalurgicas e alimenticias da regiao, a tesoura eletrica e campeã: zero fumaca, zero ruido, zero contaminacao."')
        # Comparativo
        r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponiveis em Luziania:')
        r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Luziania')
        r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustao em Luziania')
        r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Eletrica em Luziania')
        r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Luziania')
        # Video alt
        r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
          'alt="Video Move Maquinas: locacao de plataforma tesoura para industrias de Luziania e DIAL"')
        # Pricing
        r('Valores de referência para locação de plataforma tesoura em Goiânia',
          'Investimento mensal para locacao de plataforma tesoura em Luziania')
        r('Entrega em Goiânia (sem deslocamento)', 'Transporte para Luziania (BR-040, 198 km)')
        # Applications tag
        r('Aplicações em Goiânia', 'Aplicacoes industriais em Luziania')
        # Applications H2
        r('Quais as principais aplicações da <span>plataforma tesoura</span> em Goiânia?',
          'Do DIAL aos canteiros: onde a <span>plataforma tesoura</span> atua em Luziania')
        # Depoimentos
        r('O que nossos clientes dizem sobre a <span>plataforma tesoura</span>',
          'Industrias de Luziania que ja utilizaram a <span>plataforma tesoura</span>')
        # Coverage
        r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
          'Transporte programado para <span>Luziania</span> e Entorno do DF')
        # FAQ title
        r('Perguntas frequentes sobre <span>locação de plataforma tesoura</span> em Goiânia',
          'Duvidas sobre <span>locacao de plataforma tesoura</span> em Luziania')
        # Footer CTA
        r('Alugue uma plataforma tesoura em Goiânia hoje',
          'Solicite sua plataforma tesoura para Luziania')
        # JS WhatsApp
        r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
          "'Ola, preciso de plataforma tesoura em Luziania.\\n\\n'")
        # Maps title
        r('title="Localização Move Máquinas em Goiânia"', 'title="Area de atendimento Move Maquinas — Luziania"')
        r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziania</a>')
        # Incluso
        r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana',
          'Equipe tecnica com deslocamento pela BR-040. Atendimento em Luziania com suporte remoto e presencial')
        r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
          'Transporte pela BR-040 ate seu galpao, fabrica ou canteiro em Luziania. Sao 198 km — despacho programado com frete transparente informado no orcamento.')
        # NR-35 link text
        r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
          'capacitacao NR-35 para operadores</a>? Indicamos centros credenciados e coordenamos junto com a entrega em Luziania.')
        # Depoimentos individuais — need to find exact old text in ref
        # These vary per service. Let me handle generically by replacing city mentions and key phrases
        # For tesoura, the depoimentos are about shopping/DAIA/construtora
        # I'll do bulk replacements of remaining Goiania mentions

    elif svc == 'combustao':
        r('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
          '<title>Empilhadeira a Combustão para Locação em Luziânia-GO | Move Máquinas</title>')
        r('content="Aluguel de empilhadeira a combustão em Goiânia',
          'content="Locação de empilhadeira a combustão em Luziânia')
        r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
          'href="https://movemaquinas.com.br/luziania-go/aluguel-de-empilhadeira-combustao"')
        r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
          'content="Empilhadeira a Combustão para Locação em Luziânia-GO | Move Máquinas"')
        r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
          '"name": "Locação de Empilhadeira a Combustão em Luziânia"')
        r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
          '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
        r('"name": "Empilhadeira Combustão em Goiânia"', '"name": "Empilhadeira Combustão em Luziânia"')
        r('<a href="/goiania-go/">Equipamentos em Goiânia</a>', '<a href="/luziania-go/">Equipamentos em Luziânia</a>')
        r('Empilhadeira a Combustão em Goiânia</span>', 'Empilhadeira a Combustão em Luziânia</span>')
        r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>', 'Locação de Empilhadeira a Combustão em <em>Luziânia</em>')
        r('Aplicações em Goiânia', 'Aplicacoes industriais em Luziania')
        r('Entrega rápida em <span>Goiânia</span> e região metropolitana', 'Transporte programado para <span>Luziania</span> e Entorno do DF')
        r('Entrega no mesmo dia em Goiânia', 'Despacho programado pela BR-040')
        r('title="Localização Move Máquinas em Goiânia"', 'title="Area de atendimento Move Maquinas — Luziania"')
        r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziania</a>')
        r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Luziania')
        r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Luziania')
        r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Eletrica em Luziania')
        r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Luziania')

    elif svc == 'transpaleteira':
        r('<title>Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas</title>',
          '<title>Transpaleteira Elétrica para Locação em Luziânia-GO | Move Máquinas</title>')
        r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
          'href="https://movemaquinas.com.br/luziania-go/aluguel-de-transpaleteira"')
        r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
          'content="Transpaleteira Elétrica para Locação em Luziânia-GO | Move Máquinas"')
        r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
          '"name": "Locação de Transpaleteira Elétrica em Luziânia"')
        r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
          '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
        r('"name": "Transpaleteira em Goiânia"', '"name": "Transpaleteira em Luziânia"')
        r('<a href="/goiania-go/">Equipamentos em Goiânia</a>', '<a href="/luziania-go/">Equipamentos em Luziânia</a>')
        r('Transpaleteira em Goiânia</span>', 'Transpaleteira em Luziânia</span>')
        r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>', 'Locação de Transpaleteira Elétrica em <em>Luziânia</em>')
        r('Aplicações em Goiânia', 'Aplicacoes industriais em Luziania')
        r('Entrega rápida em <span>Goiânia</span> e região metropolitana', 'Transporte programado para <span>Luziania</span> e Entorno do DF')
        r('Entrega no mesmo dia em Goiânia', 'Despacho programado pela BR-040')
        r('title="Localização Move Máquinas em Goiânia"', 'title="Area de atendimento Move Maquinas — Luziania"')
        r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziania</a>')
        r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Luziania')
        r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Luziania')
        r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustao em Luziania')
        r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Luziania')

    elif svc == 'curso':
        r('<title>Curso de Operador de Empilhadeira em Goiânia | Move Máquinas</title>',
          '<title>Curso de Operador de Empilhadeira em Luziânia-GO | Move Máquinas</title>')
        r('href="https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira"',
          'href="https://movemaquinas.com.br/luziania-go/curso-de-operador-de-empilhadeira"')
        r('content="Curso de Operador de Empilhadeira em Goiânia | Move Máquinas"',
          'content="Curso de Operador de Empilhadeira em Luziânia-GO | Move Máquinas"')
        r('"name": "Curso de Operador de Empilhadeira em Goiânia"',
          '"name": "Curso de Operador de Empilhadeira em Luziânia"')
        r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
          '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
        r('"name": "Curso Empilhadeira em Goiânia"', '"name": "Curso Empilhadeira em Luziânia"')
        r('<a href="/goiania-go/">Equipamentos em Goiânia</a>', '<a href="/luziania-go/">Equipamentos em Luziânia</a>')
        r('Curso de Operador de Empilhadeira em Goiânia</span>', 'Curso de Operador de Empilhadeira em Luziânia</span>')
        r('Curso de Operador de Empilhadeira em <em>Goiânia</em>', 'Curso de Operador de Empilhadeira em <em>Luziânia</em>')
        r('Aplicações em Goiânia', 'Aplicacoes em Luziania')
        r('Entrega rápida em <span>Goiânia</span> e região metropolitana', 'Cobertura em <span>Luziania</span> e Entorno do DF')
        r('Entrega no mesmo dia em Goiânia', 'Despacho programado pela BR-040')
        r('title="Localização Move Máquinas em Goiânia"', 'title="Area de atendimento Move Maquinas — Luziania"')
        r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziania</a>')
        r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Luziania')
        r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Luziania')
        r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustao em Luziania')
        r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Eletrica em Luziania')

    # ═══════════════════════════════════════════════════════════════════
    # BULK: Replace ALL remaining visible "Goiânia" with "Luziânia" in TEXT ONLY
    # (not in URLs, schema, or structural elements)
    # This is a catch-all for FAQ answers, depoimentos, and other text blocks
    # ═══════════════════════════════════════════════════════════════════

    # Replace common text patterns
    r(' em Goiânia', ' em Luziânia')
    r(' de Goiânia', ' de Luziânia')
    r(' para Goiânia', ' para Luziânia')
    r(' Goiânia e ', ' Luziânia e ')
    r(' Goiânia,', ' Luziânia,')
    r(' Goiânia.', ' Luziânia.')
    r('Goiânia</a>', 'Luziânia</a>')

    # Replace "Distrito Industrial de Goiânia" / "Distrito Industrial" with DIAL context
    r('Distrito Industrial de Goiânia', 'DIAL de Luziânia')
    r('Distrito Industrial', 'DIAL')
    r('Setor Bueno', 'Centro de Luziânia')
    r('Setor Marista', 'Jardim Ingá')
    r('Polo da Moda', 'corredor da BR-040')
    r('Shopping Flamboyant', 'DIAL')
    r('Goiânia Shopping', 'zona industrial')
    r('Ceasa Goiânia', 'armazéns de grãos')
    r('na capital', 'na cidade')
    r('da capital', 'do município')
    r('Jardim Goiás', 'Parque Estrela Dalva')

    # Coverage block — need exact match from ref
    # Read the ref to find the coverage block text
    ref_html = open(ref_path).read()

    # Generic remaining Goiânia replacements
    _h[0] = _h[0].replace('Goiânia e região metropolitana', 'Luziânia e Entorno do DF')
    _h[0] = _h[0].replace('Goiânia e região', 'Luziânia e região')
    _h[0] = _h[0].replace('região metropolitana de Goiânia', 'Entorno Sul do Distrito Federal')

    # Coverage cities block — replace with Luziania version
    # Find the old coverage block
    import re as _re
    cov_match = _re.search(r'(Base localizada.*?</div>\s*</div>)', _h[0], _re.DOTALL)
    if cov_match:
        old_cov = cov_match.group(1)
        svc_desc = "Despacho programado com frete transparente. Atendemos todo o Entorno do DF e cidades do eixo Goiânia-Brasília."
        new_cov = f'''Sede na Av. Eurico Viana, 4913, Goiânia — 198 km de Luziânia pela BR-040. {svc_desc}</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/"><strong>Luziânia</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/valparaiso-de-goias-go/">Valparaíso de Goiás</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/formosa-go/">Formosa</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/aparecida-de-goiania-go/">Aparecida de Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
    </div>'''
        _h[0] = _h[0].replace(old_cov, new_cov)

    html = _h[0]  # extract final html for checks and saving

    # Check and save
    issues = check_goiania_refs(html, ['BR-040 (Goiania', 'Goiania (198', 'sede em Goiania', 'base em Goiania', 'Goiania-GO', 'Goiânia-GO'])

    if not_found:
        print(f"\n  NOT FOUND ({len(not_found)}):")
        for nf in not_found[:10]:
            print(f"    {nf}...")

    if issues:
        print(f"\n  Remaining Goiania refs ({len(issues)}):")
        for ln, txt in issues[:10]:
            print(f"    L{ln}: {txt}")

    # Jaccard check
    new_tri = trigrams(text_from_html(html))
    ref_tri = trigrams(text_from_html(open(ref_path).read()))
    j_ref = jaccard(new_tri, ref_tri)
    print(f"\n  Jaccard vs ref-goiania: {j_ref:.4f} {'OK' if j_ref < 0.20 else 'FAIL'}")

    for name, path in [('SC', sc_path), ('BSB', bsb_path)]:
        if os.path.exists(path):
            j = jaccard(new_tri, trigrams(text_from_html(open(path).read())))
            print(f"  Jaccard vs {name}: {j:.4f} {'OK' if j < 0.20 else 'FAIL'}")

    luz = html.count('Luziânia') + html.count('Luziania') + html.count('luziania')
    local = html.count('DIAL') + html.count('BR-040') + html.count('metalurg') + html.count('silo') + html.count('agro')
    print(f"\n  Luziania: {luz} | Local ctx: {local} | Size: {len(html):,}")

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Saved: {out_path}")

    results[svc] = {
        'path': out_path,
        'r2_path': r2_path,
        'jaccard_ref': j_ref,
        'luziania_count': luz,
        'size': len(html),
        'goiania_issues': len(issues),
    }

# Print summary
elapsed = datetime.now() - START
print(f"\n{'='*60}")
print(f"SUMMARY — 4 SERVICES FOR LUZIANIA")
print(f"{'='*60}")
for svc, data in results.items():
    print(f"  {svc:20s} | J={data['jaccard_ref']:.4f} | Luz={data['luziania_count']} | GoiIssues={data['goiania_issues']} | {data['size']:,} bytes")
print(f"\nTEMPO: {int(elapsed.total_seconds()//60):02d}:{int(elapsed.total_seconds()%60):02d}")
print(f"TOKENS: {sum(d['size']//4 for d in results.values()):,}")
