#!/usr/bin/env python3
"""
Fix Itumbiara pages 3-6 (tesoura, combustao, transpaleteira, curso).
Uses SC rebuild scripts as pattern source — extracts OLD strings from them,
then creates Itumbiara-specific NEW strings.
"""

import datetime, re, os, sys

START = datetime.datetime.now()
print(f"INICIO: {START.strftime('%Y-%m-%d %H:%M:%S')}")

BASE = '/Users/jrios/move-maquinas-seo'

def extract_text(h):
    h = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h = re.sub(r'<script[^>]*>.*?</script>', '', h, flags=re.DOTALL)
    h = re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=re.DOTALL)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'https?://\S+', '', h)
    h = re.sub(r'[\d\.\-/]{5,}', '', h)
    h = re.sub(r'\b\d+\b', '', h)
    h = re.sub(r'[·\|—–\-\+\(\)\[\]\{\}\"\'«»\u201c\u201d\u2014]', ' ', h)
    h = re.sub(r'\s+', ' ', h).strip().lower()
    return h

def ngrams(text, n=3):
    words = text.split()
    return set(' '.join(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard_ngram(a, b, n=3):
    sa = ngrams(a, n)
    sb = ngrams(b, n)
    inter = sa & sb
    union = sa | sb
    return len(inter) / len(union) if union else 0

def check_goiania_leaks(html):
    LEGIT = ['Parque das Flores', 'Eurico Viana', 'CNPJ', 'addressLocality',
             'sede em Goiânia', 'base em Goiânia', 'sede em Goiania',
             'Goiânia-GO', 'Goiania-GO', 'Goiás', 'Goias',
             'option value', 'goiania-go/', 'aparecida-de-goiania',
             'Aparecida de Goiânia', 'km da sede', 'km de Goiânia',
             'km de Goiania', 'mercado goiano', 'agronegocio goiano',
             'capital goiana', 'BR-153', 'distribuidor', '203 km']
    issues = []
    for m in re.finditer(r'Goi[aâ]n', html, re.IGNORECASE):
        start = max(0, m.start() - 60)
        end = min(len(html), m.end() + 60)
        ctx = html[start:end].replace('\n', ' ')
        if not any(leg.lower() in ctx.lower() for leg in LEGIT):
            issues.append(ctx.strip()[:120])
    return issues

def verify(ref_path, out_path, comparisons=None):
    with open(ref_path) as f: ref_t = extract_text(f.read())
    with open(out_path) as f: out_t = extract_text(f.read())
    j = jaccard_ngram(ref_t, out_t)
    status = 'PASS' if j < 0.20 else 'FAIL'
    print(f"  Jaccard vs ref: {j:.4f} {status}")
    if comparisons:
        for cp in comparisons:
            if os.path.exists(cp):
                with open(cp) as f: ct = extract_text(f.read())
                jc = jaccard_ngram(out_t, ct)
                print(f"  Jaccard vs {os.path.basename(cp)}: {jc:.4f} {'PASS' if jc < 0.20 else 'FAIL'}")
    with open(out_path) as f: html = f.read()
    leaks = check_goiania_leaks(html)
    if leaks:
        print(f"  Goiania leaks: {len(leaks)}")
        for l in leaks[:3]: print(f"    >>> {l}")
    else:
        print(f"  Goiania leaks: 0 PASS")
    return j < 0.20


# =====================================================================
# Strategy: For each page, read the SC rebuild script to extract
# the OLD strings (which match the Goiania ref), then write new
# Itumbiara-specific content.
# =====================================================================

def read_sc_script(path):
    """Parse SC rebuild script to extract r(old, new) calls."""
    with open(path) as f:
        content = f.read()
    return content

# For each failing page, we'll create it by reading the ref and doing
# targeted replacements based on what we know from the SC scripts.

# =====================================================================
# TESOURA
# =====================================================================
print("\n=== TESOURA ===")

ref = f'{BASE}/ref-goiania-tesoura.html'
out = f'{BASE}/itumbiara-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

with open(ref) as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        return False
    html = html.replace(old, new, count)
    return True

# HEAD
r('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
  '<title>Plataforma Tesoura para Locacao em Itumbiara-GO | Move Maquinas</title>')
r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma tesoura em Itumbiara-GO: modelos eletricos de 8 a 10m para galpoes de frigorificos e armazens do DIAGRI, diesel de 12 a 15m para patios externos e usinas de etanol. Manutencao no contrato, entrega via BR-153. Move Maquinas."')
r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura"')
r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locacao em Itumbiara-GO | Move Maquinas"')
r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Plataforma tesoura eletrica e diesel 8 a 15m em Itumbiara. Ideal para galpoes de frigorificos JBS/BRF, armazens Caramuru/Cargill e usinas do DIAGRI. Manutencao inclusa, entrega agendada."')
r('content="Goiânia, Goiás, Brasil"', 'content="Itumbiara, Goias, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-18.4097;-49.2158"')
r('content="-16.7234, -49.2654"', 'content="-18.4097, -49.2158"')
r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -18.4097, "longitude": -49.2158')
r('"latitude": -16.7234', '"latitude": -18.4097')
r('"longitude": -49.2654', '"longitude": -49.2158')

# Schema names
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Locacao de Plataforma Tesoura em Itumbiara"')
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Itumbiara", "addressRegion": "GO"')

# Schema breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura"')

# FAQ Schema — replace entire block
faq_start = html.find('    {\n      "@type": "FAQPage"')
faq_end_marker = '      ]\n    }'
faq_end = html.find(faq_end_marker, faq_start)
if faq_end > 0:
    faq_end += len(faq_end_marker)
    old_faq = html[faq_start:faq_end]
    new_faq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "A plataforma tesoura serve para galpoes de frigorifico em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A tesoura e ideal para galpoes com acesso vertical livre — tipico de frigorificos JBS/BRF nas areas de expedicao e docas. O mecanismo pantografico eleva a plataforma com estabilidade total para manutencao de coberturas, iluminacao e exaustores." } },
        { "@type": "Question", "name": "Qual a diferenca entre tesoura e articulada para a agroindustria de Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A tesoura sobe na vertical — rapida e com plataforma ampla para equipe com ferramentas. Ideal para galpoes e armazens sem obstaculos aereos. A articulada desvia de tubulacoes e trilhos. Nos frigorificos com redes de amonia, a articulada e melhor. Nos armazens de graos com teto livre, a tesoura e mais produtiva." } },
        { "@type": "Question", "name": "Quanto custa alugar plataforma tesoura em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A partir de R$2.200/mes para modelos eletricos de 8 metros. Diesel de 12 a 15m conforme prazo e motorizacao. Frete via BR-153 (203 km) incluido na proposta. Manutencao preventiva e corretiva cobertas pelo contrato." } },
        { "@type": "Question", "name": "A tesoura diesel funciona nos patios do DIAGRI?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Modelos diesel com tracao 4x4 operam em patios de cascalho, terra e pisos irregulares do DIAGRI e acessos de frigorificos. A eletrica requer piso nivelado — indicada para interiores de galpoes." } },
        { "@type": "Question", "name": "Quantas pessoas cabem na plataforma tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "De 2 a 4 operadores conforme modelo, com capacidade de 350 a 750 kg. Espaco suficiente para equipe com ferramentas, tintas e materiais de reparo — maior que o cesto da articulada." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da tesoura em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Ate 48 horas apos confirmacao do contrato. Rota pela BR-153 leva 2h30. Para paradas programadas, agendamos com antecedencia." } },
        { "@type": "Question", "name": "A tesoura eletrica emite gases?", "acceptedAnswer": { "@type": "Answer", "text": "Zero emissao. Motor eletrico sem gases de combustao — segura para galpoes de processamento de alimentos, armazens fechados e camaras de embalagem. Pneus nao marcantes." } },
        { "@type": "Question", "name": "Preciso de NR-35 para operar tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 exige capacitacao em trabalho em altura e PEMT acima de 2 metros. Indicamos centros credenciados na regiao de Itumbiara e Goiania." } }
      ]
    }'''
    html = html[:faq_start] + new_faq + html[faq_end:]

# Breadcrumb
r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/itumbiara-go/">Equipamentos em Itumbiara</a>')
r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Itumbiara</span>')

# Now do bulk replacements of all remaining Goiania references
# These need to be careful — some strings contain special chars

# WhatsApp encoded
html = html.replace('Goi%C3%A2nia', 'Itumbiara')

# goiania-go/ in links — but preserve legitimate ones
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura')
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada')
html = html.replace('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao')
html = html.replace('/goiania-go/aluguel-de-transpaleteira', '/itumbiara-go/aluguel-de-transpaleteira')
html = html.replace('/goiania-go/curso-operador-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')
# Keep /goiania-go/ as link to hub (legitimate)

# Now replace ALL visible text mentioning Goiânia with Itumbiara-specific content
# Hero
r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locacao de Plataforma Tesoura em <em>Itumbiara</em>')

# Find and replace the hero subtitle (long paragraph about Goiania)
# Read the actual text from the file
r('Plataformas tesoura de 8 a 15 metros com elevação vertical estável. Modelos elétricos para galpões e diesel para canteiros de obra. Manutenção inclusa, entrega no mesmo dia na capital. Ideal para manutenção de coberturas, instalações elétricas e obras civis.',
  'Plataformas tesoura de 8 a 15 metros com elevacao vertical estavel. Eletrica para interiores de frigorificos JBS/BRF e diesel para patios do DIAGRI e usinas de etanol. Manutencao inclusa, entrega via BR-153. Ideal para coberturas de armazens, iluminacao industrial e manutencao de galpoes.')

# Trust bar variations
r('<strong>8 a 15 metros</strong><span>Elevação vertical</span>',
  '<strong>Entrega BR-153</strong><span>203 km da sede</span>')
r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiencia agroindustrial</span>')

# Section "O que e" — the main content paragraphs
# We need to find the exact text in the ref. Let me use broader patterns.

# Replace all "em Goiânia" / "de Goiânia" / "para Goiânia" patterns
# But we need to be careful not to break HTML

# Let's do targeted replacements of known text patterns from the tesoura ref
r('Goiânia concentra o maior parque industrial do Centro-Oeste',
  'Itumbiara concentra o maior polo agroindustrial do sul goiano')
r('edifícios comerciais do Setor Bueno e Marista',
  'galpoes de frigorificos e armazens do DIAGRI')
r('galpões do Distrito Industrial',
  'galpoes de armazens da Caramuru e Cargill')
r('shoppings e centros comerciais no Jardim Goiás',
  'usinas de etanol e cooperativas no eixo da BR-153')
r('condomínios e edifícios na região metropolitana',
  'galpoes e estruturas no DIAGRI e entorno')
r('fábricas da GO-060 e obras civis na região metropolitana',
  'frigorificos, usinas de etanol e armazens do DIAGRI e regiao')

# Now globally replace remaining "Goiânia" (the actual UTF-8 string)
# in visible text, being careful with legitimate refs
lines = html.split('\n')
new_lines = []
for line in lines:
    if 'Goiânia' in line:
        # Check if it's in a legitimate context
        legit = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value="Goiânia"',
            'goiania-go/', '203 km', 'sede em Goiânia',
            'base em Goiânia', '@id',
        ])
        if not legit:
            line = line.replace('Goiânia', 'Itumbiara')
    new_lines.append(line)
html = '\n'.join(new_lines)

# Replace remaining Goiania (without accent) in visible text
lines = html.split('\n')
new_lines = []
for line in lines:
    if 'Goiania' in line and 'goiania-go' not in line.lower():
        legit = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Eurico Viana',
            'CNPJ', 'option value', 'sede em Goiania', 'base em Goiania',
        ])
        if not legit:
            line = line.replace('Goiania', 'Itumbiara')
    new_lines.append(line)
html = '\n'.join(new_lines)

# Fix specific local references
html = html.replace('mercado goiano', 'agronegocio goiano')
html = html.replace('capital goiana', 'polo agroindustrial')
html = html.replace('no Setor Bueno', 'no DIAGRI')
html = html.replace('do Setor Bueno', 'do DIAGRI')
html = html.replace('Setor Bueno', 'DIAGRI')
html = html.replace('Setor Marista', 'Setor Industrial')
html = html.replace('Polo da Moda', 'eixo da BR-153')
html = html.replace('Distrito Industrial de Itumbiara', 'DIAGRI de Itumbiara')
html = html.replace('Distrito Industrial', 'DIAGRI')
html = html.replace('região metropolitana', 'sul goiano')
html = html.replace('entrega no mesmo dia na capital', 'entrega agendada via BR-153')
html = html.replace('entrega no mesmo dia', 'entrega agendada')
html = html.replace('Entrega no mesmo dia', 'Entrega agendada via BR-153')
html = html.replace('shopping centers', 'areas de processamento')
html = html.replace('Shopping', 'Galpao')
html = html.replace('Jardim Goiás', 'Vila Sao Jose')

# Replace coverage block
old_cov = '''Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Itumbiara. Entrega agendada na capital. Atendemos toda a sul goiano e cidades em um raio de até 200 km. Plataformas tesoura elétrica ou diesel para qualquer obra da região.'''
# This might not match exactly due to prior replacements. Let's try the original.

# Coverage cities — replace old city list with Itumbiara list
html = html.replace('<a href="/itumbiara-go/">Itumbiara</a>\n      </div>\n      <div class="coverage__city">',
    '<a href="/itumbiara-go/"><strong>Itumbiara</strong></a>\n      </div>\n      <div class="coverage__city">')

# Depoimentos — replace names and locations
html = html.replace('Goiânia-GO', 'Itumbiara-GO')

# Maps embed
html = html.replace('!2d-49.2654!3d-16.7234', '!2d-49.2158!3d-18.4097')

# JS WhatsApp message
html = html.replace("plataforma tesoura em Itumbiara.\\n\\n'",
    "plataforma tesoura em Itumbiara.\\n\\n'")

with open(out, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"  Salvo: {out}")
verify(ref, out, [
    f'{BASE}/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
    f'{BASE}/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
])


# =====================================================================
# COMBUSTAO
# =====================================================================
print("\n=== COMBUSTAO ===")

ref = f'{BASE}/ref-goiania-combustao.html'
out = f'{BASE}/itumbiara-go-aluguel-de-empilhadeira-combustao-V2.html'

with open(ref) as f:
    html = f.read()

# HEAD
r('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
  '<title>Empilhadeira a Combustao para Locacao em Itumbiara-GO | Move Maquinas</title>')
r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/itumbiara-go/aluguel-de-empilhadeira-combustao"')
r('content="Goiânia, Goiás, Brasil"', 'content="Itumbiara, Goias, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-18.4097;-49.2158"')
r('content="-16.7234, -49.2654"', 'content="-18.4097, -49.2158"')
r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -18.4097, "longitude": -49.2158')
r('"latitude": -16.7234', '"latitude": -18.4097')
r('"longitude": -49.2654', '"longitude": -49.2158')
r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Itumbiara", "addressRegion": "GO"')

# FAQ Schema
faq_start = html.find('    {\n      "@type": "FAQPage"')
faq_end = html.find(faq_end_marker, faq_start)
if faq_end > 0:
    faq_end += len(faq_end_marker)
    old_faq = html[faq_start:faq_end]
    new_faq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual empilhadeira e ideal para frigorificos em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Para docas de expedicao e areas externas, a empilhadeira a combustao GLP ou diesel e a mais indicada. Para camaras frias a -18C, recomendamos modelos eletricos com componentes resistentes ao frio. A frota Clark cobre ambos os cenarios." } },
        { "@type": "Question", "name": "Quanto custa alugar empilhadeira a combustao em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Empilhadeiras Clark a partir de R$2.800/mes com manutencao inclusa. O valor depende da motorizacao (GLP, diesel ou eletrica), capacidade (2 a 8 toneladas) e prazo. Frete pela BR-153 incluido." } },
        { "@type": "Question", "name": "A Move entrega empilhadeira no DIAGRI?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O DIAGRI, frigorificos JBS/BRF, armazens Caramuru/Cargill e usinas estao na rota prioritaria. Entrega em ate 48h via BR-153." } },
        { "@type": "Question", "name": "GLP ou diesel: qual escolher?", "acceptedAnswer": { "@type": "Answer", "text": "GLP gera menos emissao e e preferida em docas semi-cobertas. Diesel tem maior torque para patios externos. Em armazens com poeira de graos, a eletrica e mais segura." } },
        { "@type": "Question", "name": "Preciso de NR-11 para operar?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 obriga capacitacao formal. Oferecemos curso com certificado valido para equipes de Itumbiara." } },
        { "@type": "Question", "name": "Qual a capacidade maxima das empilhadeiras?", "acceptedAnswer": { "@type": "Answer", "text": "De 2.000 a 8.000 kg. Modelos de 2.500 a 3.000 kg sao os mais usados em frigorificos. Modelos maiores atendem armazens e usinas." } },
        { "@type": "Question", "name": "Como funciona a manutencao em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Toda manutencao esta no contrato. Pecas Clark e equipe tecnica via BR-153. Resposta em ate 24h." } },
        { "@type": "Question", "name": "Qual o contrato minimo?", "acceptedAnswer": { "@type": "Answer", "text": "1 mes com renovacao automatica. Para safra ou paradas, contratos sob medida. Maior prazo = melhores condicoes." } }
      ]
    }'''
    html = html[:faq_start] + new_faq + html[faq_end:]

# Schema breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"')

# Links
html = html.replace('Goi%C3%A2nia', 'Itumbiara')
html = html.replace('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao')
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada')
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura')
html = html.replace('/goiania-go/aluguel-de-transpaleteira', '/itumbiara-go/aluguel-de-transpaleteira')
html = html.replace('/goiania-go/curso-operador-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')

# Global text replacements
lines = html.split('\n')
new_lines = []
for line in lines:
    if 'Goiânia' in line:
        legit = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value="Goiânia"',
            'goiania-go/', '203 km', 'sede em Goiânia', 'base em Goiânia', '@id',
        ])
        if not legit:
            line = line.replace('Goiânia', 'Itumbiara')
    new_lines.append(line)
html = '\n'.join(new_lines)

html = html.replace('mercado goiano', 'agronegocio goiano')
html = html.replace('capital goiana', 'polo agroindustrial')
html = html.replace('Setor Bueno', 'DIAGRI')
html = html.replace('Setor Marista', 'Setor Industrial')
html = html.replace('Polo da Moda', 'eixo da BR-153')
html = html.replace('Distrito Industrial de Itumbiara', 'DIAGRI de Itumbiara')
html = html.replace('Distrito Industrial', 'DIAGRI')
html = html.replace('região metropolitana', 'sul goiano')
html = html.replace('entrega no mesmo dia na capital', 'entrega agendada via BR-153')
html = html.replace('entrega no mesmo dia', 'entrega agendada')
html = html.replace('Entrega no mesmo dia', 'Entrega agendada via BR-153')
html = html.replace('Jardim Goiás', 'Vila Sao Jose')
html = html.replace('shopping centers', 'areas de processamento')
html = html.replace('Goiânia-GO', 'Itumbiara-GO')
html = html.replace('!2d-49.2654!3d-16.7234', '!2d-49.2158!3d-18.4097')

with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"  Salvo: {out}")
verify(ref, out, [
    f'{BASE}/senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
    f'{BASE}/brasilia-df-aluguel-de-empilhadeira-combustao-V2.html'
])


# =====================================================================
# TRANSPALETEIRA
# =====================================================================
print("\n=== TRANSPALETEIRA ===")

ref = f'{BASE}/ref-goiania-transpaleteira.html'
out = f'{BASE}/itumbiara-go-aluguel-de-transpaleteira-V2.html'

with open(ref) as f:
    html = f.read()

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/itumbiara-go/aluguel-de-transpaleteira"')
r('content="Goiânia, Goiás, Brasil"', 'content="Itumbiara, Goias, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-18.4097;-49.2158"')
r('content="-16.7234, -49.2654"', 'content="-18.4097, -49.2158"')
r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -18.4097, "longitude": -49.2158')
r('"latitude": -16.7234', '"latitude": -18.4097')
r('"longitude": -49.2654', '"longitude": -49.2158')
r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Itumbiara", "addressRegion": "GO"')

# FAQ Schema
faq_start = html.find('    {\n      "@type": "FAQPage"')
faq_end = html.find(faq_end_marker, faq_start)
if faq_end > 0:
    faq_end += len(faq_end_marker)
    old_faq = html[faq_start:faq_end]
    new_faq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Transpaleteira eletrica funciona em camara fria de frigorifico?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Transpaleteiras Clark com bateria Li-ion operam ate -25C. Nos frigorificos JBS e BRF de Itumbiara, e o equipamento padrao para movimentar paletes em camaras de congelados." } },
        { "@type": "Question", "name": "Quanto custa alugar transpaleteira em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A partir de R$1.500/mes com manutencao inclusa. Valor conforme modelo, capacidade e prazo. Transporte via BR-153 incluido na proposta." } },
        { "@type": "Question", "name": "Qual a capacidade de carga?", "acceptedAnswer": { "@type": "Answer", "text": "De 1.500 a 3.500 kg. Para paletes de frigorifico, modelos de 2.000 kg sao os mais utilizados. Armazens com big bags usam 3.000 a 3.500 kg." } },
        { "@type": "Question", "name": "A bateria de litio aguenta um turno?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Baterias Li-ion 24V suportam 8 a 10 horas de operacao continua. Recarga em 2 horas." } },
        { "@type": "Question", "name": "Preciso de NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. NR-11 obriga capacitacao para qualquer equipamento de movimentacao. Oferecemos curso com certificado para equipes de Itumbiara." } },
        { "@type": "Question", "name": "Entregam no DIAGRI?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. DIAGRI e frigorificos na rota prioritaria. Ate 48h pela BR-153." } },
        { "@type": "Question", "name": "Manutencao inclusa para Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Toda manutencao coberta pelo contrato. Pecas Clark e equipe tecnica via BR-153. Suporte remoto 24h." } },
        { "@type": "Question", "name": "Manual ou eletrica?", "acceptedAnswer": { "@type": "Answer", "text": "A eletrica elimina esforco fisico e triplica a produtividade. Em camaras frias com EPIs pesados, e indispensavel. A manual serve para operacoes curtas e esporadicas." } }
      ]
    }'''
    html = html[:faq_start] + new_faq + html[faq_end:]

r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"')

html = html.replace('Goi%C3%A2nia', 'Itumbiara')
html = html.replace('/goiania-go/aluguel-de-transpaleteira', '/itumbiara-go/aluguel-de-transpaleteira')
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada')
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura')
html = html.replace('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao')
html = html.replace('/goiania-go/curso-operador-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')

lines = html.split('\n')
new_lines = []
for line in lines:
    if 'Goiânia' in line:
        legit = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value="Goiânia"',
            'goiania-go/', '203 km', 'sede em Goiânia', 'base em Goiânia', '@id',
        ])
        if not legit:
            line = line.replace('Goiânia', 'Itumbiara')
    new_lines.append(line)
html = '\n'.join(new_lines)

html = html.replace('mercado goiano', 'agronegocio goiano')
html = html.replace('capital goiana', 'polo agroindustrial')
html = html.replace('Setor Bueno', 'DIAGRI')
html = html.replace('Setor Marista', 'Setor Industrial')
html = html.replace('Polo da Moda', 'eixo da BR-153')
html = html.replace('Distrito Industrial de Itumbiara', 'DIAGRI de Itumbiara')
html = html.replace('Distrito Industrial', 'DIAGRI')
html = html.replace('região metropolitana', 'sul goiano')
html = html.replace('entrega no mesmo dia na capital', 'entrega agendada via BR-153')
html = html.replace('entrega no mesmo dia', 'entrega agendada')
html = html.replace('Entrega no mesmo dia', 'Entrega agendada via BR-153')
html = html.replace('Jardim Goiás', 'Vila Sao Jose')
html = html.replace('Ceasa', 'frigorifico')
html = html.replace('shopping centers', 'areas de processamento')
html = html.replace('Goiânia-GO', 'Itumbiara-GO')
html = html.replace('!2d-49.2654!3d-16.7234', '!2d-49.2158!3d-18.4097')

with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"  Salvo: {out}")
verify(ref, out, [
    f'{BASE}/senador-canedo-go-aluguel-de-transpaleteira-V2.html',
    f'{BASE}/brasilia-df-aluguel-de-transpaleteira-V2.html'
])


# =====================================================================
# CURSO
# =====================================================================
print("\n=== CURSO ===")

ref = f'{BASE}/ref-goiania-curso.html'
out = f'{BASE}/itumbiara-go-curso-de-operador-de-empilhadeira-V2.html'

with open(ref) as f:
    html = f.read()

r('href="https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira"',
  'href="https://movemaquinas.com.br/itumbiara-go/curso-de-operador-de-empilhadeira"')
r('content="Goiânia, Goiás, Brasil"', 'content="Itumbiara, Goias, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-18.4097;-49.2158"')
r('content="-16.7234, -49.2654"', 'content="-18.4097, -49.2158"')
r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -18.4097, "longitude": -49.2158')
r('"latitude": -16.7234', '"latitude": -18.4097')
r('"longitude": -49.2654', '"longitude": -49.2158')

# FAQ Schema
faq_start = html.find('    {\n      "@type": "FAQPage"')
faq_end = html.find(faq_end_marker, faq_start)
if faq_end > 0:
    faq_end += len(faq_end_marker)
    new_faq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "O curso NR-11 e obrigatorio para operadores de frigorifico?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige capacitacao formal para operadores de empilhadeira em qualquer setor. Em frigorificos JBS e BRF de Itumbiara, a certificacao e ainda mais critica por questoes de seguranca e auditoria." } },
        { "@type": "Question", "name": "O curso pode ser feito na empresa em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Realizamos treinamento in company em frigorificos, armazens e usinas. O instrutor se desloca via BR-153 com material didatico completo." } },
        { "@type": "Question", "name": "Quanto custa o curso NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Valor conforme numero de alunos e local. Condicoes especiais para turmas acima de 10 operadores. Solicite orcamento informando a demanda." } },
        { "@type": "Question", "name": "O certificado vale em todo o Brasil?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Certificado com validade nacional, aceito por fiscalizacao do trabalho e auditorias de qualidade." } },
        { "@type": "Question", "name": "Qual a duracao do curso?", "acceptedAnswer": { "@type": "Answer", "text": "16 a 24 horas entre teoria e pratica. Para Itumbiara, concentramos em 2 a 3 dias consecutivos." } },
        { "@type": "Question", "name": "O curso inclui pratica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Pratica com empilhadeira Clark real no ambiente de trabalho do operador — frigorifico, armazem ou usina." } },
        { "@type": "Question", "name": "De quanto em quanto tempo reciclar?", "acceptedAnswer": { "@type": "Answer", "text": "A cada 2 anos ou em caso de mudanca de equipamento ou acidente. Para frigorificos com alta rotatividade, reciclagem semestral." } },
        { "@type": "Question", "name": "Posso combinar curso com locacao?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Pacote empilhadeira Clark + curso NR-11 com entrega e treinamento coordenados." } }
      ]
    }'''
    html = html[:faq_start] + new_faq + html[faq_end:]

r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"')
r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Itumbiara", "addressRegion": "GO"')

html = html.replace('Goi%C3%A2nia', 'Itumbiara')
html = html.replace('/goiania-go/curso-de-operador-de-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')
html = html.replace('/goiania-go/curso-operador-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')
html = html.replace('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao')
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada')
html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura')
html = html.replace('/goiania-go/aluguel-de-transpaleteira', '/itumbiara-go/aluguel-de-transpaleteira')

lines = html.split('\n')
new_lines = []
for line in lines:
    if 'Goiânia' in line:
        legit = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value="Goiânia"',
            'goiania-go/', '203 km', 'sede em Goiânia', 'base em Goiânia', '@id',
        ])
        if not legit:
            line = line.replace('Goiânia', 'Itumbiara')
    new_lines.append(line)
html = '\n'.join(new_lines)

html = html.replace('mercado goiano', 'agronegocio goiano')
html = html.replace('capital goiana', 'polo agroindustrial')
html = html.replace('Setor Bueno', 'DIAGRI')
html = html.replace('Setor Marista', 'Setor Industrial')
html = html.replace('Polo da Moda', 'eixo da BR-153')
html = html.replace('Distrito Industrial de Itumbiara', 'DIAGRI de Itumbiara')
html = html.replace('Distrito Industrial', 'DIAGRI')
html = html.replace('região metropolitana', 'sul goiano')
html = html.replace('entrega no mesmo dia na capital', 'entrega agendada via BR-153')
html = html.replace('entrega no mesmo dia', 'entrega agendada')
html = html.replace('Entrega no mesmo dia', 'Entrega agendada via BR-153')
html = html.replace('Goiânia-GO', 'Itumbiara-GO')
html = html.replace('!2d-49.2654!3d-16.7234', '!2d-49.2158!3d-18.4097')

with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"  Salvo: {out}")
verify(ref, out, [
    f'{BASE}/senador-canedo-go-curso-de-operador-de-empilhadeira-V2.html',
    f'{BASE}/brasilia-df-curso-de-operador-de-empilhadeira-V2.html'
])

END = datetime.datetime.now()
delta = END - START
print(f"\nTEMPO: {int(delta.total_seconds()//60):02d}:{int(delta.total_seconds()%60):02d}")
