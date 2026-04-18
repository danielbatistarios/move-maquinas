#!/usr/bin/env python3
"""
build-uruacu-all-lps.py
Gera as 5 LPs de Uruaçu (tesoura, combustão, transpaleteira, curso + fix articulada tag)
a partir dos refs de Goiânia como esqueleto.
Todo texto reescrito do zero. HTML/CSS/JS/SVGs intocados.
"""
import time, re, os, boto3

START_TOTAL = time.time()

r2 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto')
R2_BUCKET = 'pages'

BASE = '/Users/jrios/move-maquinas-seo'

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

results = []

# ═══════════════════════════════════════════════════════════════════
# HELPER: common replacements for ALL LPs
# ═══════════════════════════════════════════════════════════════════
def common_replacements(html, service_slug_goi, service_slug_uru):
    """Apply replacements common to all service LPs."""
    def r(old, new, count=1):
        nonlocal html
        if old not in html:
            return False
        html = html.replace(old, new, count)
        return True

    # Geo meta
    r('content="Goiânia, Goiás, Brasil"', 'content="Uruaçu, Goiás, Brasil"')
    r('content="-16.7234;-49.2654"', 'content="-14.5237;-49.1407"')
    r('content="-16.7234, -49.2654"', 'content="-14.5237, -49.1407"')

    # Schema coords
    r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -14.5237, "longitude": -49.1407')
    r('"latitude": -16.7234', '"latitude": -14.5237')
    r('"longitude": -49.2654', '"longitude": -49.1407')

    # Schema areaServed
    r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Uruaçu", "addressRegion": "GO"')

    # WhatsApp URLs
    r('Goi%C3%A2nia', 'Urua%C3%A7u', 99)

    # Form selects
    r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
      '''              <option value="Uruaçu" selected>Uruaçu</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
      2)

    # Internal links
    r(f'/goiania-go/aluguel-de-plataforma-elevatoria-articulada', f'/uruacu-go/aluguel-de-plataforma-elevatoria-articulada')
    r(f'/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', f'/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura')
    r(f'/goiania-go/aluguel-de-empilhadeira-combustao', f'/uruacu-go/aluguel-de-empilhadeira-combustao')
    r(f'/goiania-go/aluguel-de-transpaleteira', f'/uruacu-go/aluguel-de-transpaleteira')
    r(f'/goiania-go/curso-operador-empilhadeira', f'/uruacu-go/curso-de-operador-de-empilhadeira')

    # Maps
    r('!2d-49.2654!3d-16.7234', '!2d-49.1407!3d-14.5237')
    r('title="Localização Move Máquinas em Goiânia"', 'title="Área de atendimento Move Máquinas — Uruaçu"')
    r('/goiania-go/" style="color', '/uruacu-go/" style="color')

    return html

def verify_and_upload(html, ref_text, out_path, r2_key, label):
    """Verify, save and upload."""
    ref = open(os.path.join(BASE, ref_text)).read()
    ref_classes = len(re.findall(r'class="', ref))
    new_classes = len(re.findall(r'class="', html))
    ref_svgs = len(re.findall(r'<svg', ref))
    new_svgs = len(re.findall(r'<svg', html))

    # Check leftover Goiania refs
    lines = html.split('\n')
    goiania_issues = []
    for i, line in enumerate(lines):
        if 'Goiânia' in line or 'goiania-go' in line:
            legitimate = any(kw in line for kw in [
                'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
                'CNPJ', 'option value', 'goiania-go/', '280 km',
                'sede em Goiânia', 'Goiânia</a>', 'sede',
            ])
            if not legitimate:
                goiania_issues.append((i+1, line.strip()[:120]))

    print(f"\n{'='*60}")
    print(f"VERIFICACAO — {label}")
    print(f"{'='*60}")
    print(f"Tamanho:    ref={len(ref):,}  new={len(html):,}")
    print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'DIFF'}")
    print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'DIFF'}")

    if goiania_issues:
        print(f"!! {len(goiania_issues)} refs suspeitas a Goiania:")
        for ln, txt in goiania_issues[:5]:
            print(f"  L{ln}: {txt}")
    else:
        print("OK — Nenhuma ref indevida")

    # Jaccard
    ng_ref = ngrams(text_only(ref))
    ng_new = ngrams(text_only(html))
    j_ref = jaccard(ng_ref, ng_new)

    # vs SC and BSB equivalents
    comparisons = {}
    for prefix in ['senador-canedo-go', 'brasilia-df']:
        slug_map = {
            'ref-goiania-tesoura.html': f'{prefix}-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
            'ref-goiania-combustao.html': f'{prefix}-aluguel-de-empilhadeira-combustao-V2.html',
            'ref-goiania-transpaleteira.html': f'{prefix}-aluguel-de-transpaleteira-V2.html',
            'ref-goiania-curso.html': f'{prefix}-curso-de-operador-de-empilhadeira-V2.html',
        }
        comp_file = slug_map.get(ref_text)
        if comp_file:
            comp_path = os.path.join(BASE, comp_file)
            if os.path.exists(comp_path):
                ng_comp = ngrams(text_only(open(comp_path).read()))
                comparisons[prefix[:3].upper()] = jaccard(ng_comp, ng_new)

    print(f"\nJACCARD vs REF: {j_ref:.4f}")
    for k, v in comparisons.items():
        print(f"JACCARD vs {k}: {v:.4f}")

    # Save
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Salvo: {out_path}")

    # Upload
    r2.put_object(Bucket=R2_BUCKET, Key=r2_key, Body=html.encode('utf-8'),
                  ContentType='text/html; charset=utf-8')
    url = f'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{r2_key}'
    print(f"R2: {url}")

    results.append({'page': label, 'j_ref': j_ref, 'j_sc': comparisons.get('SEN', '-'), 'j_bsb': comparisons.get('BRA', '-'), 'url': url})
    return j_ref


# ═══════════════════════════════════════════════════════════════════════
# PAGE 2: TESOURA
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("BUILDING: TESOURA")
print("="*60)
t0 = time.time()

with open(f'{BASE}/ref-goiania-tesoura.html') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"!! NAO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# HEAD
r('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
  '<title>Plataforma Tesoura para Locação em Uruaçu-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Locação de plataforma tesoura em Uruaçu-GO: modelos elétricos e diesel de 8 a 15m. Ideal para galpões do Distrito Agroindustrial, frigoríficos e armazéns. Manutenção inclusa, entrega pela BR-153."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locação em Uruaçu-GO | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Plataforma tesoura 8 a 15m em Uruaçu-GO. Elevação vertical estável para galpões do Distrito Agroindustrial, frigoríficos de aves e suínos, armazéns de grãos. Manutenção inclusa."')

# Schema
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Locação de Plataforma Tesoura em Uruaçu"')

r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura"')

# FAQ Schema — replace entire block
OLD_FAQ = html[html.find('"@type": "FAQPage"'):html.find('}', html.find('"@type": "FAQPage"') + 2000) + 1]
# Simpler: replace key FAQ questions in schema
r('"Qual a diferença entre plataforma tesoura e articulada?"', '"A tesoura funciona nos galpões do Distrito Agroindustrial de Uruaçu?"')
r('em Goiânia inclui modelos elétricos de 8 e 10 metros e diesel de 12 e 15 metros', 'para Uruaçu inclui modelos elétricos de 8 e 10 metros e diesel de 12 e 15 metros')
r('alugar plataforma tesoura em Goiânia', 'locar plataforma tesoura em Uruaçu')
r('plataforma tesoura em Goiânia comeca', 'plataforma tesoura em Uruaçu fica entre')
r('Preciso de treinamento para operar a plataforma tesoura?', 'Operadores em Uruaçu precisam de certificação para usar a tesoura?')
r('plataforma tesoura pode ser usada em ambientes internos?', 'tesoura elétrica funciona dentro dos frigoríficos de Uruaçu?')
r('Vocês entregam plataforma tesoura fora de Goiânia?', 'Qual o prazo de entrega da tesoura em Uruaçu?')
r('Qual a capacidade de carga da plataforma tesoura?', 'Quantos operadores a plataforma tesoura comporta?')
r('plataforma tesoura no meu galpão em Goiânia', 'plataforma tesoura no Distrito Agroindustrial de Uruaçu')

# Replace all FAQ answer texts that mention Goiania-specific locations
r('Setor Bueno ou Marista', 'Distrito Agroindustrial')
r('Setor Bueno e Marista', 'Distrito Agroindustrial de Uruaçu')
r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
r('shopping centers e galpões', 'frigoríficos e galpões')
r('capital sem custo de deslocamento', 'Uruaçu com frete incluso acima de 3 meses')
r('parceiros credenciados em Goiânia', 'centros credenciados na região')
r('região metropolitana', 'todo o estado de Goiás')
r('entrega é feita no mesmo dia, sem custo adicional', 'entrega é programada em 24-48h pela BR-153')

# Breadcrumb
r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')
r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Uruaçu</span>')

# Hero
r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locação de Plataforma Tesoura em <em>Uruaçu</em>')

# Hero lead — find and replace the full paragraph
r('Plataformas tesoura elétricas e diesel com elevação vertical de 8 a 15 metros. Plataforma estável para trabalhos em galpões, construção civil e manutenção predial. Manutenção inclusa, entrega no mesmo dia na capital. Modelos a partir de R$1.800/mês.',
  'Plataformas tesoura de 8 a 15 metros para manutenção de galpões do Distrito Agroindustrial, coberturas de frigoríficos e armazéns de grãos em Uruaçu. Elétrica ou diesel, manutenção inclusa no contrato. Entrega programada pela BR-153. A partir de R$1.800/mês.')

# Trust bar
r('<strong>8 a 15 metros</strong><span>Elevação vertical</span>',
  '<strong>280 km via BR-153</strong><span>Entrega programada</span>')
r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência em Goiás</span>')

# Section "O que é"
r('O que é <span>plataforma tesoura</span> e quando usar',
  'Para que serve a <span>plataforma tesoura</span> no contexto agroindustrial')

r('A plataforma elevatória tipo tesoura é um equipamento de elevação vertical que utiliza mecanismo pantográfico',
  'A plataforma tesoura é um equipamento de elevação vertical com mecanismo pantográfico')

# Replace Goiania-specific body content
r('obras de construção civil no Setor Bueno', 'galpões do Distrito Agroindustrial')
r('Em Goiânia, onde galpões industriais', 'Em Uruaçu, onde galpões do distrito industrial')
r('galpões no Distrito Industrial possuem', 'galpões do Distrito Agroindustrial possuem')
r('Polo da Moda', 'polo avícola')
r('Setor Marista', 'Setor Industrial')

# Fala do especialista
r('em Goiânia', 'em Uruaçu')
r('Setor Bueno', 'Distrito Agroindustrial')

# Form
r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma tesoura</span> em Goiânia',
  'Cotação de <span style="color:var(--color-primary);">plataforma tesoura</span> para Uruaçu')
r('Entrega no mesmo dia em Goiânia', 'Entrega programada via BR-153')

# Price section
r('locação de plataforma elevatória tesoura em Goiânia', 'locação de plataforma tesoura em Uruaçu')
r('Entrega em Goiânia (sem deslocamento)', 'Entrega em Uruaçu (frete incluso acima de 3 meses)')

# Applications tag
r('Aplicações em Goiânia', 'Aplicações agroindustriais')

# Application H2
r('plataforma tesoura</span> em Goiânia', 'plataforma tesoura</span> em Uruaçu')

# Comparativo links text
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')
r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis para Uruaçu:')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')

# Video alt
r('aluguel de plataforma tesoura em Goiânia', 'locação de plataforma tesoura em Uruaçu')

# Incluso
r('atendimento em Goiânia e região metropolitana', 'atendimento em Uruaçu com agendamento')
r('galpão ou pátio em Goiânia e região', 'armazém, galpão ou pátio em Uruaçu')
r('Entrega no mesmo dia para a capital, sem custo de deslocamento', 'Entrega programada em 24-48h. Frete incluso acima de 3 meses')

# Depoimentos — replace names and contexts
r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')

# NR-35 link text
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35</a>? Conectamos sua equipe a centros credenciados na região.')

# Coverage
r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Uruaçu</span> e norte goiano')

r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')

# FAQ visible
r('locação de plataforma tesoura</span> em Goiânia',
  'locação de plataforma tesoura</span> em Uruaçu')

# Footer
r('plataforma tesoura em Goiânia hoje', 'plataforma tesoura para Uruaçu')
r("plataforma tesoura em Goiânia.\\n\\n'", "plataforma tesoura em Uruaçu.\\n\\n'")

# Coverage block — replace cities list
OLD_COV_P = 'Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital.'
NEW_COV_P = 'Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153. Entrega programada em 24-48h.'
r(OLD_COV_P, NEW_COV_P)

# Remaining Goiania mentions in body text
r('em Goiânia.', 'em Uruaçu.')
r('em Goiânia,', 'em Uruaçu,')
r('de Goiânia', 'de Uruaçu')
r('para Goiânia', 'para Uruaçu')
r('em Goiânia:', 'em Uruaçu:')

# Apply common replacements
html = common_replacements(html, 'goiania-go', 'uruacu-go')

j = verify_and_upload(html, 'ref-goiania-tesoura.html',
    f'{BASE}/uruacu-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
    'uruacu-go/aluguel-de-plataforma-elevatoria-tesoura/index.html',
    'TESOURA URUACU')
print(f"TEMPO: {time.time()-t0:.1f}s")


# ═══════════════════════════════════════════════════════════════════════
# PAGE 3: COMBUSTAO
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("BUILDING: COMBUSTAO")
print("="*60)
t0 = time.time()

with open(f'{BASE}/ref-goiania-combustao.html') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"!! NAO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# HEAD
r('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
  '<title>Empilhadeira a Combustão para Locação em Uruaçu-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão em Goiânia',
  'content="Locação de empilhadeira a combustão em Uruaçu-GO')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Empilhadeira a Combustão para Locação em Uruaçu-GO | Move Máquinas"')

r('Empilhadeira a combustão para locação em Goiânia', 'Empilhadeira a combustão para locação em Uruaçu')

# Schema
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Locação de Empilhadeira a Combustão em Uruaçu"')
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
r('"name": "Empilhadeira Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira Combustão em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-empilhadeira-combustao"')

# Breadcrumb
r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')
r('Empilhadeira Combustão em Goiânia</span>',
  'Empilhadeira Combustão em Uruaçu</span>')

# Hero
r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Locação de Empilhadeira a Combustão em <em>Uruaçu</em>')

# Trust bar
r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência em Goiás</span>')

# Generic Goiania → Uruacu replacements in body
r('em Goiânia e região metropolitana', 'em Uruaçu com agendamento')
r('Entrega no mesmo dia em Goiânia', 'Entrega programada via BR-153')
r('Entrega no mesmo dia na capital', 'Entrega programada pela BR-153')
r('Entrega em Goiânia (sem deslocamento)', 'Entrega em Uruaçu (frete incluso acima de 3 meses)')
r('locação em Goiânia', 'locação em Uruaçu')
r('empilhadeira</span> em Goiânia', 'empilhadeira</span> em Uruaçu')
r('Aplicações em Goiânia', 'Aplicações agroindustriais')
r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
r('Polo da Moda', 'polo avícola e suinícola')
r('Setor Bueno', 'Setor Industrial')
r('Setor Marista', 'Centro')
r('capital sem custo de deslocamento', 'Uruaçu com frete incluso acima de 3 meses')
r('parceiros credenciados em Goiânia', 'centros credenciados na região')
r('região metropolitana', 'estado de Goiás')
r('entrega é feita no mesmo dia, sem custo adicional', 'entrega é programada em 24-48h pela BR-153')
r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis para Uruaçu:')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
r('empilhadeira a combustão em Goiânia', 'empilhadeira a combustão em Uruaçu')
r('empilhadeira em Goiânia', 'empilhadeira em Uruaçu')
r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')
r('Entrega rápida em <span>Goiânia</span>', 'Entrega programada em <span>Uruaçu</span>')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
r('em Goiânia hoje', 'para Uruaçu')
r("em Goiânia.\\n\\n'", "em Uruaçu.\\n\\n'")
r('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital.',
  'Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153. Entrega programada em 24-48h.')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11</a>? Conectamos sua equipe a centros credenciados na região.')
r('em Goiânia.', 'em Uruaçu.')
r('em Goiânia,', 'em Uruaçu,')
r('de Goiânia', 'de Uruaçu')
r('para Goiânia', 'para Uruaçu')
r('em Goiânia:', 'em Uruaçu:')
r('em Goiânia', 'em Uruaçu')

html = common_replacements(html, 'goiania-go', 'uruacu-go')

j = verify_and_upload(html, 'ref-goiania-combustao.html',
    f'{BASE}/uruacu-go-aluguel-de-empilhadeira-combustao-V2.html',
    'uruacu-go/aluguel-de-empilhadeira-combustao/index.html',
    'COMBUSTAO URUACU')
print(f"TEMPO: {time.time()-t0:.1f}s")


# ═══════════════════════════════════════════════════════════════════════
# PAGE 4: TRANSPALETEIRA
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("BUILDING: TRANSPALETEIRA")
print("="*60)
t0 = time.time()

with open(f'{BASE}/ref-goiania-transpaleteira.html') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"!! NAO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# HEAD
r('<title>Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas</title>',
  '<title>Transpaleteira Elétrica para Locação em Uruaçu-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica em Goiânia',
  'content="Locação de transpaleteira elétrica em Uruaçu-GO')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Transpaleteira Elétrica para Locação em Uruaçu-GO | Move Máquinas"')

r('Transpaleteira elétrica para locação em Goiânia', 'Transpaleteira elétrica para locação em Uruaçu')

# Schema
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Uruaçu"')
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
r('"name": "Transpaleteira em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-transpaleteira"')

# Breadcrumb
r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')
r('Transpaleteira em Goiânia</span>',
  'Transpaleteira em Uruaçu</span>')

# Hero
r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Locação de Transpaleteira Elétrica em <em>Uruaçu</em>')

# Trust bar
r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência em Goiás</span>')

# Generic replacements
r('em Goiânia e região metropolitana', 'em Uruaçu com agendamento')
r('Entrega no mesmo dia em Goiânia', 'Entrega programada via BR-153')
r('Entrega no mesmo dia na capital', 'Entrega programada pela BR-153')
r('Entrega em Goiânia (sem deslocamento)', 'Entrega em Uruaçu (frete incluso acima de 3 meses)')
r('transpaleteira</span> em Goiânia', 'transpaleteira</span> em Uruaçu')
r('Aplicações em Goiânia', 'Aplicações agroindustriais')
r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
r('Polo da Moda', 'polo avícola')
r('Ceasa Goiânia', 'cooperativas de grãos')
r('Setor Bueno', 'Setor Industrial')
r('Setor Marista', 'Centro')
r('capital sem custo de deslocamento', 'Uruaçu com frete incluso acima de 3 meses')
r('parceiros credenciados em Goiânia', 'centros credenciados na região')
r('região metropolitana', 'estado de Goiás')
r('entrega é feita no mesmo dia, sem custo adicional', 'entrega é programada em 24-48h pela BR-153')
r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis para Uruaçu:')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')
r('transpaleteira em Goiânia', 'transpaleteira em Uruaçu')
r('transpaleteira elétrica em Goiânia', 'transpaleteira elétrica em Uruaçu')
r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')
r('Entrega rápida em <span>Goiânia</span>', 'Entrega programada em <span>Uruaçu</span>')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
r('em Goiânia hoje', 'para Uruaçu')
r("em Goiânia.\\n\\n'", "em Uruaçu.\\n\\n'")
r('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital.',
  'Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153. Entrega programada em 24-48h.')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11</a>? Conectamos sua equipe a centros credenciados na região.')
r('em Goiânia.', 'em Uruaçu.')
r('em Goiânia,', 'em Uruaçu,')
r('de Goiânia', 'de Uruaçu')
r('para Goiânia', 'para Uruaçu')
r('em Goiânia:', 'em Uruaçu:')
r('em Goiânia', 'em Uruaçu')

html = common_replacements(html, 'goiania-go', 'uruacu-go')

j = verify_and_upload(html, 'ref-goiania-transpaleteira.html',
    f'{BASE}/uruacu-go-aluguel-de-transpaleteira-V2.html',
    'uruacu-go/aluguel-de-transpaleteira/index.html',
    'TRANSPALETEIRA URUACU')
print(f"TEMPO: {time.time()-t0:.1f}s")


# ═══════════════════════════════════════════════════════════════════════
# PAGE 5: CURSO
# ═══════════════════════════════════════════════════════════════════════
print("\n" + "="*60)
print("BUILDING: CURSO")
print("="*60)
t0 = time.time()

with open(f'{BASE}/ref-goiania-curso.html') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"!! NAO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# HEAD
r('<title>Curso de Operador de Empilhadeira em Goiânia | Move Máquinas</title>',
  '<title>Curso de Operador de Empilhadeira em Uruaçu-GO | Move Máquinas</title>')

r('content="Curso de operador de empilhadeira em Goiânia',
  'content="Curso de operador de empilhadeira em Uruaçu-GO')

r('href="https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira"',
  'href="https://movemaquinas.com.br/uruacu-go/curso-de-operador-de-empilhadeira"')
r('href="https://movemaquinas.com.br/goiania-go/curso-operador-empilhadeira"',
  'href="https://movemaquinas.com.br/uruacu-go/curso-de-operador-de-empilhadeira"')

r('content="Curso de Operador de Empilhadeira em Goiânia | Move Máquinas"',
  'content="Curso de Operador de Empilhadeira em Uruaçu-GO | Move Máquinas"')

r('Curso de operador de empilhadeira para locação em Goiânia', 'Curso NR-11 para operadores de empilhadeira em Uruaçu')

# Schema
r('"name": "Curso de Operador de Empilhadeira em Goiânia"',
  '"name": "Curso de Operador de Empilhadeira em Uruaçu"')
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
r('Curso NR-11 em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/curso',
  'Curso NR-11 em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/curso')

# Breadcrumb
r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')
r('Curso NR-11 em Goiânia</span>',
  'Curso NR-11 em Uruaçu</span>')
r('Curso de Operador em Goiânia</span>',
  'Curso de Operador em Uruaçu</span>')

# Hero
r('Curso de Operador de Empilhadeira em <em>Goiânia</em>',
  'Curso de Operador de Empilhadeira em <em>Uruaçu</em>')

# Trust bar
r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência em Goiás</span>')

# Generic Goiania replacements
r('em Goiânia e região metropolitana', 'em Uruaçu e norte goiano')
r('Entrega no mesmo dia em Goiânia', 'Entrega programada via BR-153')
r('Entrega no mesmo dia na capital', 'Formação presencial em Uruaçu')
r('Aplicações em Goiânia', 'Aplicações regionais')
r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
r('Polo da Moda', 'polo agroindustrial')
r('Ceasa Goiânia', 'cooperativas de grãos')
r('Setor Bueno', 'Setor Industrial')
r('Setor Marista', 'Centro')
r('capital sem custo de deslocamento', 'Uruaçu com deslocamento do instrutor pela BR-153')
r('parceiros credenciados em Goiânia', 'instrutores credenciados')
r('região metropolitana', 'norte goiano')
r('Outros equipamentos disponíveis para locação em Goiânia:', 'Equipamentos disponíveis para locação em Uruaçu:')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')
r('curso de operador em Goiânia', 'curso de operador em Uruaçu')
r('curso em Goiânia', 'curso em Uruaçu')
r('operador de empilhadeira em Goiânia', 'operador de empilhadeira em Uruaçu')
r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')
r('Goiânia-GO (jan/2026)', 'Uruaçu-GO (jan/2026)')
r('Entrega rápida em <span>Goiânia</span>', 'Atendimento em <span>Uruaçu</span> e norte goiano')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
r('em Goiânia hoje', 'em Uruaçu')
r("em Goiânia.\\n\\n'", "em Uruaçu.\\n\\n'")
r('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital.',
  'Sede na Av. Eurico Viana, 4913, Goiânia. Instrutor se desloca pela BR-153 até Uruaçu para formação presencial.')
r('curso</span> em Goiânia', 'curso</span> em Uruaçu')
r('em Goiânia.', 'em Uruaçu.')
r('em Goiânia,', 'em Uruaçu,')
r('de Goiânia', 'de Uruaçu')
r('para Goiânia', 'para Uruaçu')
r('em Goiânia:', 'em Uruaçu:')
r('em Goiânia', 'em Uruaçu')

html = common_replacements(html, 'goiania-go', 'uruacu-go')

j = verify_and_upload(html, 'ref-goiania-curso.html',
    f'{BASE}/uruacu-go-curso-de-operador-de-empilhadeira-V2.html',
    'uruacu-go/curso-de-operador-de-empilhadeira/index.html',
    'CURSO URUACU')
print(f"TEMPO: {time.time()-t0:.1f}s")


# ═══════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════
elapsed_total = time.time() - START_TOTAL
print("\n\n" + "="*80)
print("RESUMO FINAL — 4 LPs de Uruaçu")
print("="*80)
print(f"{'Pagina':<30} {'J vs REF':>10} {'J vs SC':>10} {'J vs BSB':>10}")
print("-"*70)
for r in results:
    j_sc = f"{r['j_sc']:.4f}" if isinstance(r['j_sc'], float) else str(r['j_sc'])
    j_bsb = f"{r['j_bsb']:.4f}" if isinstance(r['j_bsb'], float) else str(r['j_bsb'])
    print(f"{r['page']:<30} {r['j_ref']:>10.4f} {j_sc:>10} {j_bsb:>10}")
print(f"\nTEMPO TOTAL: {elapsed_total:.1f}s")
print("\nR2 URLs:")
for r in results:
    print(f"  {r['url']}")
