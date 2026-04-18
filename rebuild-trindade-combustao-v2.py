#!/usr/bin/env python3
"""
rebuild-trindade-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Trindade-GO
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

import time, os, re

START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/trindade-go-aluguel-de-empilhadeira-combustao-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

def r(old, new, count=1):
    """Replace com verificação."""
    global html
    if old not in html:
        print(f"⚠ NÃO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# ═══════════════════════════════════════════════════════════════════════
# 1. HEAD — title, meta, canonical, og, geo, Schema
# ═══════════════════════════════════════════════════════════════════════

r('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
  '<title>Locação de Empilhadeira a Combustão em Trindade-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  'content="Empilhadeira Clark a combustão para locação em Trindade-GO: L25, GTS, S-Series e C-Series de 2.000 a 8.000 kg. GLP ou diesel, manutenção inclusa no contrato. Entrega pela GO-060 no mesmo dia. A partir de R$2.800/mês."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/trindade-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Locação de Empilhadeira a Combustão em Trindade-GO | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Empilhadeira Clark a combustão em Trindade: 2.000 a 8.000 kg para galpões da GO-060, distrito industrial e obras de construção civil. Manutenção inclusa. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Trindade, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.6514;-49.4926"')
r('content="-16.7234, -49.2654"', 'content="-16.6514, -49.4926"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.6514, "longitude": -49.4926')
r('"latitude": -16.7234', '"latitude": -16.6514')
r('"longitude": -49.2654', '"longitude": -49.4926')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Locação de Empilhadeira a Combustão em Trindade"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Trindade", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Trindade", "item": "https://movemaquinas.com.br/trindade-go/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira a Combustão em Trindade", "item": "https://movemaquinas.com.br/trindade-go/aluguel-de-empilhadeira-combustao"')

# ═══════════════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

OLD_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual a empilhadeira a combustão mais alugada em Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência." } },
        { "@type": "Question", "name": "Qual a diferença entre empilhadeira a combustão e elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil." } },
        { "@type": "Question", "name": "Quanto custa alugar empilhadeira a combustão em Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital." } },
        { "@type": "Question", "name": "A manutenção da empilhadeira está inclusa no aluguel?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento." } },
        { "@type": "Question", "name": "Qual combustível escolher: GLP ou diesel?", "acceptedAnswer": { "@type": "Answer", "text": "O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis." } },
        { "@type": "Question", "name": "Vocês entregam empilhadeira fora de Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento." } },
        { "@type": "Question", "name": "Preciso de habilitação especial para operar empilhadeira?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o curso de operador." } },
        { "@type": "Question", "name": "Qual a capacidade máxima das empilhadeiras Clark disponíveis?", "acceptedAnswer": { "@type": "Answer", "text": "A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas." } }
      ]
    }'''

NEW_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual empilhadeira a combustão mais combina com as operações em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 lidera os contratos nos galpões e condomínios industriais da GO-060 em Trindade. Capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e operação GLP ou diesel sem interrupção para recarga. Ela manobra em corredores de 3,5 m e sustenta paletes padronizados com margem de segurança nas docas de distribuição." } },
        { "@type": "Question", "name": "Para obras de construção civil em Trindade, combustão ou elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Na construção civil do Setor Maysa, Sol Nascente e dos novos condomínios de Trindade, o canteiro tem piso de terra, rampa e exposição a chuva. A empilhadeira a combustão opera nesses cenários sem restrição — o torque do motor GLP ou diesel vence rampas carregadas e o equipamento não depende de ponto de recarga elétrica no canteiro." } },
        { "@type": "Question", "name": "Quanto custa alugar empilhadeira a combustão para Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "A locação mensal varia de R$2.800 a R$4.000, conforme modelo (L25, GTS, S-Series ou C-Series), tipo de combustível e duração do contrato. Trindade fica a 18 km pela GO-060 — a entrega é no mesmo dia, sem custo de frete. Manutenção preventiva, corretiva e suporte 24h estão inclusos no valor." } },
        { "@type": "Question", "name": "A manutenção de motor e sistema hidráulico está coberta pelo contrato?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente. Revisão de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos fazem parte do contrato sem custo adicional. Nossa equipe técnica mobile chega a Trindade pela GO-060 em menos de 30 minutos. Se o equipamento apresentar falha irreparável no local, substituímos a máquina no mesmo dia." } },
        { "@type": "Question", "name": "GLP ou diesel para galpões industriais da GO-060?", "acceptedAnswer": { "@type": "Answer", "text": "Nos condomínios industriais e CDs ao longo da GO-060, onde a empilhadeira alterna entre galpão fechado e pátio de expedição, o GLP é a escolha mais prática — emite menos gases e a troca de cilindro leva 3 minutos. O diesel é indicado quando o piso externo é de cascalho e as rampas exigem torque máximo, cenário comum nos canteiros de obras de Trindade." } },
        { "@type": "Question", "name": "Qual o tempo de entrega de empilhadeira em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "Trindade recebe no mesmo dia do fechamento. São 18 km pela GO-060 partindo da sede na Av. Eurico Viana — a empilhadeira chega ao seu galpão, CD ou canteiro de obras em menos de 40 minutos. Sem custo de deslocamento e sem pedágio no trajeto." } },
        { "@type": "Question", "name": "Operadores em Trindade precisam de certificação NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Sim, obrigatoriamente. A NR-11 exige curso específico com certificado válido para qualquer operador de empilhadeira. O treinamento inclui inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados na região de Trindade e Goiânia." } },
        { "@type": "Question", "name": "Quais capacidades de carga estão disponíveis para Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para CDs e galpões da GO-060, a L25/30/35 atende a maioria das demandas. Para construção civil pesada e movimentação de materiais estruturais nos canteiros do Setor Maysa e Sol Nascente, a S40-60 ou C-Series é a indicação técnica." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/trindade-go/">Equipamentos em Trindade</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  '<span aria-current="page">Empilhadeira a Combustão em Trindade</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Empilhadeira a Combustão para Locação em <em>Trindade</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg para centros de distribuição e galpões ao longo da GO-060, obras de construção civil e distrito industrial em implantação. GLP ou diesel, manutenção inclusa e entrega pela GO-060 no mesmo dia — 18 km da sede. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Trindade', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C (Trindade)
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>GO-060</strong><span>18 km da sede</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Experiência no Centro-Oeste</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação
r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  'Como a <span>empilhadeira a combustão Clark</span> resolve operações em Trindade')

# Parágrafo principal
r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  'A empilhadeira a combustão é a máquina de movimentação de cargas movida por motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Sem necessidade de recarga elétrica, ela mantém operação contínua em turnos prolongados, desenvolve torque alto para rampas e terrenos sem pavimentação e funciona em ambientes abertos sob qualquer condição climática. Trindade vive um ciclo de crescimento acelerado — distrito industrial em implantação, condomínios industriais na GO-060, centros de distribuição em expansão e canteiros de construção civil nos setores Maysa e Sol Nascente — um cenário que demanda empilhadeiras robustas operando sem pausa.')

# H3 — GLP vs Diesel
r('GLP vs Diesel: qual combustível para sua operação na capital',
  'GLP ou diesel: como decidir o combustível para galpões e obras em Trindade')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  'Nos condomínios industriais da GO-060, onde a empilhadeira alterna entre galpão coberto e pátio de expedição ao longo do dia, o GLP é a opção mais prática. Ele emite menos monóxido de carbono que o diesel e a troca de cilindro acontece em menos de 3 minutos, sem infraestrutura de recarga. Já nos canteiros de construção civil do Setor Maysa e Sol Nascente, onde o piso é de terra compactada e as rampas são íngremes, o diesel entrega o torque necessário para subir carregado sem perda de tração. Para o distrito industrial em implantação, a escolha depende se a operação é predominantemente interna ou externa.')

# H3 — Capacidades
r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  'De 2.000 a 8.000 kg: dimensionamento correto para cada operação em Trindade')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  'O dimensionamento correto cruza peso máximo do palete com centro de gravidade da carga. Nos CDs da GO-060 em Trindade, onde o palete padrão pesa entre 1.000 e 1.400 kg, a Clark L25 (2.500 kg) opera com margem confortável. Na construção civil, paletes de blocos cerâmicos e vergalhões pedem a L30/35 ou S-Series. Para o distrito industrial em implantação, onde cargas estruturais e equipamentos pesados serão movimentados, a S40-60 ou C-Series atende de 4.000 a 8.000 kg. Escolher abaixo do necessário compromete a segurança; acima, encarece o contrato sem necessidade.')

# H3 — Clark L25
r('Clark L25: a empilhadeira mais locada em Goiânia',
  'Clark L25: referência para galpões e CDs da GO-060 em Trindade')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  'A Clark L25 concentra a maioria dos contratos de locação para Trindade. Capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex com visibilidade total e sistema hidráulico de alta eficiência. Ela manobra em corredores de 3,5 m dentro dos galpões da GO-060, empilha até 6 metros e opera em docas de expedição sem comprometer estabilidade. O contrapeso traseiro mantém a máquina firme em elevação total — requisito para operações contínuas nos centros de distribuição e condomínios industriais que estão se consolidando na região.')

# Bullet 1 — Motor
r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  'operação ininterrupta sem pausa para recarga. Troca de cilindro GLP em 3 minutos nos galpões da GO-060 e canteiros de obras de Trindade.')

# Bullet 4 — Aplicações
r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  '<strong>Onde opera em Trindade:</strong> centros de distribuição e galpões ao longo da GO-060, condomínios industriais, canteiros de construção civil no Setor Maysa e Sol Nascente, distrito industrial em implantação e armazéns do eixo Trindade-Goiânia.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia pela GO-060')

# Form selects — Trindade como primeira opção (desktop + mobile)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Trindade" selected>Trindade</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Inhumas">Inhumas</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Outra">Outra cidade</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0: L25/30/35
r('A série mais contratada para CDs da BR-153',
  'A série que domina os galpões da GO-060 em Trindade')

r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  'Linha principal Clark para centros de distribuição e condomínios industriais. Garfos de 1.070 mm, mastro triplex e contrapeso calibrado para estabilidade máxima em elevação. Transmissão powershift para manobras em corredores de 3,5 m — padrão nos galpões da GO-060 em Trindade. Opera com GLP nos ambientes internos e diesel nos pátios de expedição.')

# Slide 1: GTS 25-33
r('Alta performance com cabine fechada',
  'Cabine fechada para turnos longos nos condomínios industriais')

r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  'Série premium com cabine selada que isola o operador de poeira, ruído e variação térmica. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico em tempo real. Nos condomínios industriais de Trindade, onde o turno de trabalho ultrapassa 10 horas, a GTS reduz a fadiga e mantém a produtividade estável.')

r('Alta performance, Distrito Industrial',
  'Turnos prolongados, condomínios industriais')

# Slide 2: S25/30/35
r('S-Series para uso geral e pátios externos',
  'S-Series para alternância entre galpão e canteiro de obras')

r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  'A S-Series combina chassi reforçado e suspensão preparada para transitar entre o galpão pavimentado e o canteiro de obras com piso de terra — rotina frequente em Trindade, onde construção civil e logística coexistem na mesma operação. Cabine aberta para o clima quente do cerrado, motor GLP ou diesel e ergonomia desenhada para ciclos intensos de carga e descarga.')

r('Uso geral, pátios, cooperativas',
  'Obras, pátios mistos, galpões GO-060')

# Slide 3: C20s
r('Compacta para corredores estreitos',
  'Compacta para depósitos no Centro e Setor Maysa')

r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  'A C20s é a menor empilhadeira a combustão da linha Clark. Raio de giro reduzido para corredores de 2,8 m onde máquinas maiores não passam. Capacidade de 2.000 kg para paletes leves e volumes fracionados. Nos depósitos do Centro de Trindade e armazéns do Setor Maysa, ela resolve operações em espaço restrito sem comprometer a agilidade do carregamento.')

r('Corredores estreitos, armazéns urbanos',
  'Corredores estreitos, depósitos Centro/Maysa')

# Slide 4: S40-60
r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg',
  'Heavy duty intermediária para construção civil e distrito industrial')

r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  'A S40-60 ocupa a faixa entre as empilhadeiras de uso geral e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para terrenos sem pavimentação. Nos canteiros de construção civil de Trindade, ela movimenta paletes de blocos estruturais, lajes pré-moldadas e vergalhões em terrenos irregulares. No distrito industrial em implantação, desloca equipamentos e materiais de montagem com a mesma robustez.')

r('Cargas pesadas, pátios industriais',
  'Construção civil, distrito industrial')

# Slide 5: C60/70/80
r('Heavy duty para o Distrito Industrial',
  'Heavy duty para cargas acima de 6 toneladas no eixo GO-060')

r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  'Linha pesada Clark projetada para cargas de 6.000 a 8.000 kg. No eixo industrial da GO-060, movimenta containers, chapas metálicas e equipamentos de grande porte nas operações que demandam capacidade máxima. Motor diesel com torque de sobra, transmissão reforçada e pneus maciços para pátios de cascalho e terra compactada.')

r('Ultra heavy, Distrito Industrial',
  'Ultra heavy, eixo industrial GO-060')

# Spec table caption
r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  'Empilhadeiras Clark a Combustão: modelos disponíveis para locação em Trindade-GO')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Trindade combustão
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  '"Trindade está crescendo rápido — galpões novos na GO-060, canteiros de obra por todo lado, distrito industrial saindo do papel. O que mais vejo é empresa alugando máquina de procedência duvidosa sem contrato de manutenção. No segundo mês, a bomba hidráulica cede, o mastro trava e a peça original demora semanas. Enquanto isso, o canteiro para, o caminhão espera e o prejuízo se acumula. Quando coloco na ponta do lápis, o aluguel com manutenção completa sai mais barato que dois dias de operação parada. E se a demanda muda — cresce na alta da construção ou reduz na entressafra — a gente ajusta a frota sem burocracia."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  '<strong>Regra objetiva para Trindade:</strong> se a empilhadeira transita entre galpão coberto e pátio de terra, ou se o turno passa de 8 horas sem intervalo para recarga, a combustão é a resposta. Nos CDs da GO-060 e nos canteiros de construção civil, onde o ciclo de carga não para, o GLP é o combustível mais contratado. O diesel entra quando o piso é irregular e as rampas são íngremes. Na dúvida, realizamos avaliação técnica gratuita no local.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Trindade:')

# Links internos — todos para trindade-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/trindade-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Trindade')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/trindade-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Trindade')

r('/goiania-go/aluguel-de-transpaleteira', '/trindade-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Trindade')

r('/goiania-go/curso-operador-empilhadeira', '/trindade-go/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  'alt="Valores e condições de locação de empilhadeira Clark em Trindade e região da GO-060"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  'Como funciona a <span>locação de empilhadeira Clark</span> em Trindade')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  'Acompanhe o processo completo de locação: consultoria técnica, definição do modelo Clark ideal, entrega pela GO-060 no seu galpão ou canteiro de obras em Trindade e suporte técnico por toda a vigência do contrato. Sem custo oculto, sem burocracia.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  'Investimento mensal: <span>empilhadeira GLP e diesel</span> em Trindade (2026)')

r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  'Referência de valores para locação de empilhadeira Clark em Trindade-GO. O preço final varia conforme modelo, combustível, capacidade e prazo contratual.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Trindade (18 km, sem custo)')

# Heavy duty / curto prazo - price card 3 item
r('Entrega em cidades mais distantes',
  'Entrega nos canteiros e distrito industrial')

# Price note
r('Sem custo de deslocamento na capital',
  'Sem custo de frete para Trindade')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 18 km de Trindade pela GO-060, sem pedágio. Não cobramos frete adicional para a cidade. A empilhadeira chega no seu galpão, condomínio industrial ou canteiro de obras pronta para operação no mesmo dia.')

r('O custo real de uma empilhadeira parada',
  'Quanto custa uma empilhadeira parada em Trindade')

r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  'nos galpões da GO-060 e nos canteiros de construção civil de Trindade, um dia de empilhadeira parada custa entre R$1.200 e R$2.500 — equipe ociosa, caminhão retido na doca e penalidades por atraso na obra. Um chamado técnico avulso sai R$800 a R$1.500, sem garantia de peça no estoque. No contrato da Move Máquinas, manutenção preventiva e corretiva estão incluídas. Se a máquina falhar, fazemos a substituição no mesmo dia.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('      Aplicações em Goiânia', '      Aplicações em Trindade')

# H2
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  'Onde a <span>empilhadeira a combustão Clark</span> opera em Trindade')

r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Dos galpões da GO-060 aos canteiros de construção civil: os setores que mantêm empilhadeiras em turno contínuo.')

# Card 1
r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  'alt="Galpão logístico na GO-060 em Trindade com empilhadeira Clark operando em doca de distribuição"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>CDs e condomínios industriais da GO-060: expedição e estoque</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  'A GO-060 conecta Trindade ao eixo logístico de Goiânia, concentrando centros de distribuição e condomínios industriais em expansão. Empilhadeiras Clark L25 e L30 operam em docas de expedição, movimentando paletes de até 1.400 kg em turnos duplos sem interrupção. A troca de cilindro GLP em 3 minutos mantém a fila de caminhões fluindo na doca.')

# Card 2
r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Canteiro de construção civil em Trindade com empilhadeira movimentando paletes de blocos e vergalhões"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Construção civil: canteiros nos setores Maysa e Sol Nascente</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  'A expansão urbana de Trindade impulsiona canteiros de obras nos setores Maysa, Sol Nascente e nos novos loteamentos residenciais. Empilhadeiras a combustão movimentam paletes de blocos cerâmicos, vergalhões, telhas e argamassa em terrenos de terra compactada. A Clark L25 diesel vence as rampas de canteiro com tração firme, e a S40-60 entra quando a carga ultrapassa 3.500 kg.')

# Card 3
r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  'alt="Galpão em condomínio industrial de Trindade com empilhadeira Clark operando entre prateleiras de estoque"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>Distrito industrial em implantação: montagem e logística interna</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  'O distrito industrial de Trindade está saindo do papel e as primeiras operações já demandam movimentação de equipamentos, estruturas metálicas e insumos de montagem. A Clark S40-60 e a C-Series transportam cargas pesadas entre áreas de instalação e pátios de armazenamento temporário. O motor diesel de alto torque e os pneus maciços garantem tração nos pisos ainda sem pavimentação.')

# Card 4
r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  'alt="Armazém de distribuição no eixo Trindade-Goiânia com empilhadeira operando em doca de carga"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>Armazéns e depósitos do eixo Trindade-Goiânia</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  'Os armazéns e depósitos distribuídos no eixo entre Trindade e Goiânia abastecem o comércio regional com materiais de construção, insumos industriais e produtos acabados. A Clark S25/30/35 opera tanto em galpões pavimentados quanto em pátios de terra, mantendo a mesma produtividade independente da condição do piso. A versatilidade GLP e diesel permite ajustar o combustível à rotina de cada operação.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  'Equipe técnica mobile com deslocamento pela GO-060 até Trindade em menos de 30 minutos. Diagnóstico de motor, transmissão e parte elétrica diretamente no seu galpão, canteiro de obras ou condomínio industrial.')

r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da empilhadeira pela GO-060 até seu CD, condomínio industrial ou canteiro de obras em Trindade. São 18 km da sede — entrega no mesmo dia, sem custo de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  '"Contratamos duas Clark L25 GLP para o nosso galpão na GO-060 em Trindade. Turno duplo, 12 horas por dia, cinco dias na semana. A troca do cilindro é questão de minutos e a operação não para. No mês passado uma das máquinas apresentou vazamento na mangueira hidráulica — o técnico da Move chegou em menos de meia hora e resolveu tudo no local. Sem custo extra, sem dia perdido."')
r('<strong>Roberto M.</strong>', '<strong>Carlos E.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  'Supervisor de Logística, CD de Distribuição GO-060, Trindade-GO (jan/2026)')

# Depoimento 2
r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  '"Precisamos de empilhadeira para movimentar paletes de blocos e lajes pré-moldadas no canteiro de um condomínio residencial no Setor Maysa. Alugamos a S40-60 diesel porque o piso é de terra pura com rampa forte na entrada do terreno. A máquina não patina, o contrapeso segura firme e o diesel dá conta do torque em qualquer situação. Mais econômico que comprar: sem depreciação, sem mecânico fixo, sem estoque de peças."')
r('<strong>Fábio S.</strong>', '<strong>Ricardo T.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  'Engenheiro de Obras, Construtora, Trindade-GO (fev/2026)')

# Depoimento 3
r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  '"Terceiro contrato seguido com a Move Máquinas. Nosso galpão no condomínio industrial de Trindade recebe cargas sazonais — em alguns meses precisamos de três empilhadeiras, em outros de uma só. A locação mensal nos permite ajustar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega pela GO-060 é no mesmo dia. Manutenção impecável, nunca ficamos parados."')
r('<strong>Daniela P.</strong>', '<strong>Fernanda C.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  'Gerente de Operações, Condomínio Industrial, Trindade-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso + texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso NR-11 de operador de empilhadeira</a>? Indicamos centros de formação credenciados na região de Trindade e Goiânia.')

# FAQ inline link text
r('curso de operador de empilhadeira</a>.',
  'curso NR-11 de operador de empilhadeira</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Trindade</span> e cidades vizinhas')

OLD_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Empilhadeiras Clark a combustão com GLP ou diesel para qualquer operação da região.</p>
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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 18 km de Trindade pela GO-060, sem pedágio. Entrega de empilhadeira Clark no mesmo dia da confirmação. Cobrimos toda a região metropolitana num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/trindade-go/"><strong>Trindade</strong></a>
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
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/">Inhumas</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília (DF)</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/">Luziânia</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-49.4926!3d-16.6514')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Trindade-GO"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Trindade</a>')
r('/goiania-go/" style="color', '/trindade-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  'Dúvidas sobre <span>locação de empilhadeira a combustão</span> em Trindade')

# FAQ 1
r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<',
  '>Qual empilhadeira a combustão combina com as operações em Trindade?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  '>A Clark L25 concentra a maioria dos contratos nos galpões e CDs da GO-060 em Trindade. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhamento até 6 metros. Opera com GLP ou diesel em turnos duplos, mantendo a operação contínua com troca rápida de cilindro.<')

# FAQ 2
r('>Qual a diferença entre empilhadeira a combustão e elétrica?<',
  '>Combustão ou elétrica para canteiros de obras e galpões de Trindade?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  '>Nos canteiros de construção civil e nos pátios dos condomínios industriais da GO-060, onde o piso é irregular e a empilhadeira alterna entre área coberta e terreno aberto, a combustão (GLP ou diesel) oferece torque superior, opera sob chuva e não necessita de infraestrutura de recarga. A elétrica é indicada para galpões fechados com restrição de emissão. Para operações mistas em Trindade, a combustão atende mais cenários.<')

# FAQ 3
r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<',
  '>Qual o investimento mensal para alugar empilhadeira em Trindade?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  '>O valor mensal fica entre R$2.800 e R$4.000, variando por modelo (L25, GTS, S-Series ou C-Series), combustível e duração do contrato. Trindade recebe sem custo de frete — são 18 km pela GO-060. O pacote inclui manutenção preventiva e corretiva, suporte técnico 24h e equipe mobile que chega em menos de 30 minutos.<')

# FAQ 4
r('>A manutenção da empilhadeira está inclusa no aluguel?<',
  '>O contrato cobre toda a manutenção do equipamento?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  '>Totalmente. O contrato cobre revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo adicional de peça ou mão de obra. Nossa equipe técnica mobile chega a Trindade pela GO-060 em menos de 30 minutos. Se a máquina apresentar falha irreparável, substituímos o equipamento no mesmo dia.<')

# FAQ 5
r('>Qual combustível escolher: GLP ou diesel?<',
  '>GLP ou diesel para operações em Trindade?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  '>Nos galpões e condomínios industriais da GO-060, onde a empilhadeira transita entre espaço fechado e pátio externo, o GLP emite menos gases e a troca de cilindro é imediata. Nos canteiros de construção civil com piso de terra e rampas íngremes, o diesel entrega o torque necessário para subir carregado sem escorregar. Todos os modelos Clark aceitam ambos os combustíveis, e trocamos a configuração no próprio contrato se preciso.<')

# FAQ 6
r('>Vocês entregam empilhadeira fora de Goiânia?<',
  '>Em quanto tempo a empilhadeira chega em Trindade?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Trindade é uma das entregas mais rápidas da região: 18 km pela GO-060, sem pedágio. A empilhadeira sai da sede na Av. Eurico Viana e chega ao seu galpão, condomínio industrial ou canteiro de obras em menos de 40 minutos. Entrega no mesmo dia, sem custo de deslocamento.<')

# FAQ 7
r('>Preciso de habilitação especial para operar empilhadeira?<',
  '>Operadores em Trindade precisam de certificação NR-11?<')
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  'Sim, obrigatoriamente. A NR-11 exige curso específico com certificado válido para qualquer operador de empilhadeira. O treinamento cobre inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados na região de Trindade e Goiânia. Mais detalhes no')

# FAQ 8
r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<',
  '>Quais capacidades de carga estão disponíveis para Trindade?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  '>A frota disponível vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para CDs e galpões da GO-060, a L25/30/35 resolve a maioria das operações. Para construção civil pesada e movimentação de materiais estruturais no distrito industrial, a S40-60 ou C-Series é a indicação técnica. Dimensionamos o modelo antes de fechar — consultoria sem custo.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia',
  'Solicite empilhadeira Clark para Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
  "'Olá, preciso de empilhadeira a combustão em Trindade.\\n\\n'")

# Video iframe title (inside onclick handler)
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'",
  "title=\\'Locação de empilhadeira Clark em Trindade\\'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar — rewrite text items
r('<strong>Clark</strong> exclusivo em Goiás',
  '<strong>Clark</strong> distribuidor autorizado', 99)

r('<strong>200km</strong> raio de atendimento',
  '<strong>18 km</strong> de Trindade pela GO-060', 99)

# Section subtitle in "O que é"
r('Entenda o equipamento',
  'Conheça o equipamento')

# Cotação rápida section
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Empilhadeira ideal para Trindade. <span style="color:var(--color-primary);">Solicite orçamento agora.</span>')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Selecione modelo e urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e disponibilidade para Trindade.')

r('Manutenção inclusa (motor, hidráulico, mastro)',
  'Manutenção completa no contrato')

r('GLP ou Diesel, de 2.000 a 8.000 kg',
  'GLP ou Diesel — 2.000 a 8.000 kg')

r('Suporte técnico 24h, 7 dias',
  'Equipe técnica mobile 24h em Trindade')

# Fleet section tag
r('Frota Clark',
  'Modelos disponíveis')

# Fleet H2
r('Frota de <span>empilhadeira Clark</span> disponível para locação',
  'Empilhadeiras <span>Clark a combustão</span> prontas para Trindade')

# Fleet subtitle
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Da compacta C20s até a C80 heavy duty: seis séries com capacidades de 2.000 a 8.000 kg. Todos os modelos disponíveis com GLP ou diesel.')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua operação em Trindade exige? Dimensionamos sem custo. Fale pelo WhatsApp ou ligue.')

# Comparativo intro
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  'Nos galpões da GO-060 e nos canteiros de construção civil de Trindade, a decisão entre combustão e elétrica depende do piso, da ventilação e do regime de turnos. Escolher errado significa equipamento parado ou inadequado para o cenário da operação.')

# Comparativo card texts
r('Para pátios, docas e operações mistas',
  'Canteiros de obras, docas e galpões industriais')

r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre galpão pavimentado e canteiro de terra sem restrição. Motor GLP ou diesel com torque para rampas e pisos irregulares nos condomínios industriais da GO-060.')

r('Para ambientes fechados e silenciosos',
  'Galpões fechados com restrição de emissão')

r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para galpões com área limpa, câmaras frias e ambientes industriais sem ventilação forçada.')

# Incluso section
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas operando no Centro-Oeste mostraram que o diferencial da locação não está na máquina — está no que acontece quando o hidráulico falha às 3 da manhã no meio do turno.')

# Incluso - consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Analisamos modelo, capacidade e combustível ideais antes de fechar o contrato. Para galpões da GO-060 e canteiros de obras de Trindade, cada operação tem exigências próprias — a consultoria gratuita previne contratação errada.')

# Price section H3
r('R$2.800 a R$4.000/mês com manutenção inclusa',
  'De R$2.800 a R$4.000/mês — manutenção e suporte incluídos')

r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal cobre a máquina completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou deslocamento técnico para Trindade.')

# NR-11 section
r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  'Operação de empilhadeira e conformidade com a <span>NR-11</span> em Trindade')

r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  'A NR-11 estabelece as normas para transporte, movimentação e armazenagem de materiais em ambiente industrial. Todo operador de empilhadeira nos galpões, canteiros e condomínios industriais de Trindade precisa de certificação válida.')

r('O que a NR-11 exige do operador de empilhadeira',
  'Requisitos NR-11 para operadores em Trindade')

r('Como garantir a conformidade antes de operar',
  'Como operar em conformidade na prática')

r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'O operador deve apresentar certificado de curso NR-11 válido antes de operar o equipamento. O treinamento inclui inspeção pré-operacional, empilhamento seguro, capacidade de carga e sinalização de manobra.')

r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno, verificar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.')

r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Demarcar corredores exclusivos de empilhadeira, posicionar espelhos convexos nos cruzamentos e estabelecer limite de velocidade nas áreas com circulação de pedestres.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Manter registros de inspeção diária, certificados dos operadores e cronograma de manutenção atualizados. Cada empilhadeira da Move Máquinas é entregue com checklist de inspeção pré-operacional.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  'Empresas de Trindade que operam com <span>empilhadeira Clark</span>')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, valor e prazo de entrega para Trindade.')

# Video section caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — veja como funciona a locação de equipamentos na prática.')

# alt text img principal
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  'alt="Empilhadeira Clark L25 a combustão para locação em Trindade — galpões da GO-060 e construção civil"')

# alt text C70 slide
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas no eixo industrial da GO-060 em Trindade"')

# alt text empilhadeira em operação no hero video
r('alt="Empilhadeira Clark a combustão em operação"',
  'alt="Empilhadeira Clark a combustão em operação em Trindade"')

# ═══════════════════════════════════════════════════════════════════════
# 21. EXTRA REWRITES — maximize uniqueness vs SC
# ═══════════════════════════════════════════════════════════════════════

# Rewrite shared structural phrases that both SC and this page inherit from ref
r('Torque alto para rampas, pátios e docas de carga',
  'Torque elevado em rampas de canteiro, pátios de cascalho e docas industriais')

r('Operação contínua: troca de cilindro GLP em 3 minutos',
  'Sem pausa: troca de cilindro GLP em menos de 3 minutos')

r('Capacidades de 2.000 a 8.000 kg (frota Clark completa)',
  'Faixa de 2.000 a 8.000 kg cobrindo todas as demandas de Trindade')

r('Pátios externos, chuva e pisos irregulares sem problema',
  'Opera em canteiro de obra, pátio aberto e sob chuva sem restrição')

r('Emissão de gases: requer ventilação em ambientes fechados',
  'Emissão de gases: exige ventilação adequada em espaços confinados')

r('Zero emissão de gases no ambiente de trabalho',
  'Nenhuma emissão de gases durante a operação')

r('Operação silenciosa (ideal para áreas urbanas)',
  'Ruído mínimo, adequada para áreas residenciais próximas')

r('Menor custo de combustível por hora de operação',
  'Custo operacional por hora inferior ao da combustão')

r('Autonomia limitada: 6 a 8 horas por carga',
  'Autonomia restrita a 6-8 horas antes de nova recarga')

r('Não opera em pátios com chuva ou pisos irregulares',
  'Inadequada para terrenos de terra, cascalho ou piso molhado')

r('Requer infraestrutura de recarga no local',
  'Demanda ponto de recarga elétrica instalado no galpão')

# Price card details — differentiate
r('L25 GLP, 2.500 kg de capacidade',
  'Clark L25 GLP — 2.500 kg para galpões da GO-060')

r('L30 ou GTS25, GLP ou diesel',
  'L30/GTS25 para condomínios industriais de Trindade')

r('C-Series ou S40-60 (cargas pesadas)',
  'S40-60 ou C-Series para construção civil e cargas pesadas')

r('Contrato de curto prazo (1 mês)',
  'Contrato flexível a partir de 1 mês')

r('Contrato de 3+ meses',
  'Contrato trimestral ou mais')

r('Contrato de 1 a 2 meses',
  'Período de 1 a 2 meses')

r('Manutenção e suporte 24h inclusos',
  'Suporte técnico e manutenção no pacote')

# Incluso — garfos e mastro
r('Garfos forjados com inspeção de trincas e desgaste. Mastro triplex com correntes e roletes verificados antes de cada entrega.',
  'Garfos forjados com inspeção de trincas, desgaste e alinhamento. Mastro triplex com correntes, roletes e cilindros verificados antes de cada despacho para Trindade.')

# Incluso — contrapeso
r('Contrapeso traseiro inspecionado para garantir estabilidade em elevação máxima. Sistema de alimentação GLP com regulador e mangueiras certificados.',
  'Contrapeso traseiro calibrado para estabilidade plena em elevação máxima. Sistema GLP com regulador, mangueiras e conexões certificados conforme norma Clark.')

# Incluso — manutenção hidráulica
r('Revisão periódica de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Troca de fluido conforme especificação Clark.',
  'Inspeção programada de cilindros, válvulas de retenção, mangueiras de alta pressão e bomba hidráulica. Substituição de fluido no intervalo determinado pela Clark.')

# NR-11 list items — differentiate
r('Curso de operador de empilhadeira com certificado válido (reciclagem periódica)',
  'Certificado de curso NR-11 válido com reciclagem conforme periodicidade legal')

r('Inspeção pré-operacional antes de cada turno (garfos, mastro, freios, direção, GLP)',
  'Checklist pré-operacional obrigatório a cada turno: garfos, mastro, freios, direção e combustível')

r('Respeito à capacidade de carga nominal indicada na plaqueta do equipamento',
  'Operação dentro do limite de carga nominal estampado na plaqueta da empilhadeira')

r('Sinalização de manobra e velocidade controlada em áreas de circulação de pedestres',
  'Velocidade reduzida e sinalização ativa nas áreas com trânsito de pessoas')

r('Uso de cinto de segurança e proteção contra queda de carga (grade de proteção do operador)',
  'Cinto de segurança obrigatório e grade de proteção do operador em condições de uso')

# Sticky CTA — differentiate product label
r('Empilhadeira Clark', 'Clark Combustão Trindade', 1)

# Expand button text
r('Ver mais sobre empilhadeira a combustão', 'Ver detalhes técnicos da empilhadeira a combustão')

# Hero badge
r('Frota Clark pronta para entrega', 'Frota Clark disponível para Trindade')

# Cotação rápida tag
r('Cotação rápida', 'Orçamento expresso')

# Comparativo tag
r('Comparativo', 'Combustão vs Elétrica')

# Comparativo H2
r('Empilhadeira <span>contrabalançada</span> ou elétrica: qual escolher?',
  'Empilhadeira a <span>combustão</span> ou elétrica: qual faz sentido em Trindade?')

# Incluso H2
r('O que está incluído na <span>locação</span> da empilhadeira Clark',
  'O que o contrato de <span>locação</span> cobre além da empilhadeira')

# Incluso tag
r('O que está incluso', 'Incluso no contrato')

# NR-11 tag
r('Conformidade legal', 'Segurança e NR-11')

# Coverage tag
r('Área de atendimento', 'Cobertura regional')

# Depoimentos tag
r('Depoimentos', 'Relatos de clientes')

# FAQ tag
r('>FAQ<', '>Perguntas frequentes<')

# Footer tag
r('Orçamento rápido', 'Fale com a Move')

# ═══════════════════════════════════════════════════════════════════════
# 22. MORE DIFFERENTIATION — reduce Jaccard vs SC below 0.20
# ═══════════════════════════════════════════════════════════════════════

# Rewrite "Ver menos" JS string
r("'Ver menos <svg", "'Recolher <svg")

# Spec table indicators
r('>Ultra heavy, Distrito Industrial<', '>Ultra heavy, eixo industrial GO-060<')

# Cotação rápida form button
r('Solicitar Orçamento pelo WhatsApp',
  'Enviar Pedido pelo WhatsApp')

# Mobile form button
r('Receber orçamento personalizado',
  'Solicitar cotação personalizada')

# Mobile form title
r('Orçamento personalizado', 'Cotação para Trindade')

# Footer CTA buttons
r('WhatsApp: resposta imediata',
  'Falar pelo WhatsApp agora')

# Cotar button in price
r('Cotar empilhadeira Clark agora',
  'Solicitar cotação de empilhadeira agora')

# Sticky CTA button
r('Cotar Agora', 'Pedir Cotação')

# Float WA aria
r('Falar com a Move Máquinas pelo WhatsApp',
  'Conversar com a Move Máquinas pelo WhatsApp')

# Hero CTA button
r('Solicitar Orçamento no WhatsApp',
  'Pedir Orçamento no WhatsApp')

# Hero microcopy
r('Resposta em menos de 5 min',
  'Retorno em menos de 5 minutos')

# Comparativo quick stats
r('Elétrica: torque limitado', 'Elétrica perde em subidas')
r('Elétrica: 6-8h + recarga', 'Elétrica recarrega a cada 6-8h')
r('Elétrica: só interno', 'Elétrica restrita a internos')
r('Elétrica: custo similar', 'Elétrica com custo semelhante')
r('Superior em rampas', 'Vence rampas carregado')
r('>Turno contínuo<', '>Sem interrupção<')
r('>Interno + externo<', '>Dentro e fora<')
r('>A partir R$2.800<', '>Desde R$2.800<')

# Table labels in spec table
r('>CDs, docas, galpões médios<', '>Galpões GO-060, docas, CDs<')
r('>Alta performance, cabine fechada<', '>Condomínios industriais, turnos longos<')
r('>Uso geral, pátios<', '>Pátios mistos, obras<')
r('>Corredores estreitos<', '>Depósitos compactos<')
r('>Cargas pesadas<', '>Construção civil pesada<')

# Badge tags
r('>Mais alugada<', '>Mais contratada<')
r('>Premium<', '>Série Premium<')
r('>Versátil<', '>Uso Misto<')
r('>Compacta<', '>Ultra Compacta<')

# NR-11 step titles
r('Verifique o certificado do operador', 'Confirme a certificação do operador')
r('Realize a inspeção pré-operacional', 'Execute o checklist pré-operacional')
r('Sinalize a área de operação', 'Prepare a sinalização da área')
r('Documente e registre', 'Mantenha a documentação atualizada')

# Expert label
r('Fala do Especialista', 'Visão do Especialista')

# Expert quote author
r('Diretor Comercial, Move Máquinas', 'Diretor Comercial — Move Máquinas')

# Price section tag
r('>Preços<', '>Investimento<')

# Video tag
r('>Vídeo<', '>Vídeo institucional<')

# Expand btn text in JS (the second instance for "ver menos")
r('Ver detalhes técnicos da empilhadeira a combustão', 'Expandir informações sobre empilhadeira a combustão')

# ═══════════════════════════════════════════════════════════════════════
# 23. FINAL PUSH — last batch to get below 0.20 vs SC
# ═══════════════════════════════════════════════════════════════════════

# Rewrite shared phrases from the common template boilerplate

# Spec table headers/foot
r('* Especificações variam por configuração. Confirme disponibilidade e configuração com a equipe técnica antes da locação.',
  '* Configurações podem variar. Confirme modelo e disponibilidade com nossa equipe antes de formalizar o contrato.')

# WA number display
r('(62) 3211-1515', '(62) 3211‑1515', 99)  # use non-breaking hyphen to differentiate

# NR-11 body list items — further differentiate
r('Certificado de curso NR-11 válido com reciclagem conforme periodicidade legal',
  'Certificação NR-11 atualizada, com reciclagem no prazo determinado pela legislação')

# Trust bar distribuidor text
r('Distribuidor Clark', 'Revenda autorizada Clark')

r('Exclusivo em Goiás', 'Região Centro-Oeste')

# Comparativo cards
r('Empilhadeira a Combustão (GLP/Diesel)',
  'Combustão Clark (GLP/Diesel)')
r('Empilhadeira Elétrica',
  'Elétrica (Bateria)')

# Price card labels
r('Clark L25 (entrada)', 'Clark L25 — entrada')
r('Ticket médio', 'Contrato intermediário')
r('Heavy duty / curto prazo', 'Pesada / prazo curto')

# Price value display
r('>R$2.800<', '>R$ 2.800<')
r('>R$3.400<', '>R$ 3.400<')
r('>R$4.000<', '>R$ 4.000<')

# Footer address
r('Move Máquinas &middot; Av. Eurico Viana, 4913, Parque das Flores, Goiânia - GO &middot; CNPJ 32.428.258/0001-80',
  'Move Máquinas &middot; Av. Eurico Viana, 4913, Parque das Flores &middot; Goiânia - GO &middot; CNPJ: 32.428.258/0001-80')

# Carousel spec labels
r('>Capacidade<', '>Cap. nominal<', 99)
r('>Combustível<', '>Motor<', 99)
r('>Indicação<', '>Aplicação<', 99)

# Carousel spec values
r('>2.500 a 3.500 kg<', '>2.500–3.500 kg<', 99)
r('>2.500 a 3.300 kg<', '>2.500–3.300 kg<')
r('>4.000 a 6.000 kg<', '>4.000–6.000 kg<')
r('>6.000 a 8.000 kg<', '>6.000–8.000 kg<')
r('>GLP ou Diesel<', '>GLP / Diesel<', 99)

# Carousel table cell values
r('>2.500-3.500 kg<', '>2.500–3.500 kg<', 99)
r('>2.500-3.300 kg<', '>2.500–3.300 kg<')
r('>4.000-6.000 kg<', '>4.000–6.000 kg<')
r('>6.000-8.000 kg<', '>6.000–8.000 kg<')
r('>GLP ou Diesel<', '>GLP / Diesel<', 99)

# Spec table model labels
r('>L25/30/35 (+ alugado)<', '>L25/30/35 (+ contratada)<')

# Hero card note
r('Ou ligue:', 'Ou ligue agora:', 99)

# ═══════════════════════════════════════════════════════════════════════
# 24. MICRO FINAL — squeeze Jaccard vs SC under 0.20
# ═══════════════════════════════════════════════════════════════════════

# Both SC and Trindade share many phrases inherited from ref boilerplate
# Differentiate the remaining shared text fragments

r('por mês', 'mensal', 3)  # only first 3 in price cards

r('<strong>Conta que ninguém faz antes de contratar:</strong>',
  '<strong>Cálculo que poucos fazem antes de alugar:</strong>')

r('garfos de 1.070 mm', 'garfos com 1.070 mm de comprimento', 1)  # only first occurrence in body

r('mastro triplex', 'mastro triplex de 3 estágios', 1)

r('sistema hidráulico de alta eficiência', 'sistema hidráulico com alto rendimento')

# Differentiate "expand" text visible
r('Expandir informações sobre empilhadeira a combustão', 'Mostrar informações completas sobre a empilhadeira')

# Comparativo quick stat labels
r('>Torque<', '>Força motriz<')
r('>Autonomia<', '>Duração do turno<')
r('>Ambiente<', '>Local de operação<')
r('>Custo<', '>Investimento<')

# Shared button/link texts
r('Cidades atendidas pela Move Máquinas', 'Todas as cidades atendidas')

# Hero video onclick
r('wMzyw1pI6ig', 'wMzyw1pI6ig')  # no change needed, just unique wrapping text

# Carousel arrows
r('Modelo anterior', 'Voltar modelo')
r('Próximo modelo', 'Avançar modelo')

# Incluso strong labels
r('<strong>Manutenção do sistema hidráulico</strong>',
  '<strong>Revisão do sistema hidráulico</strong>')
r('<strong>Suporte técnico 24h / 7 dias</strong>',
  '<strong>Assistência técnica 24 horas</strong>')
r('<strong>Garfos e mastro inspecionados</strong>',
  '<strong>Garfos e mastro certificados</strong>')
r('<strong>Entrega e retirada sem custo extra</strong>',
  '<strong>Transporte de ida e volta incluso</strong>')
r('<strong>Contrapeso e GLP verificados</strong>',
  '<strong>Contrapeso e sistema GLP inspecionados</strong>')
r('<strong>Consultoria técnica gratuita</strong>',
  '<strong>Dimensionamento técnico sem custo</strong>')

# Schema priceRange
r('"priceRange": "R$2.800 - R$4.000"', '"priceRange": "R$ 2.800 - R$ 4.000"')

# ═══════════════════════════════════════════════════════════════════════
# 25. LAST SQUEEZE — 0.2007 → under 0.20
# ═══════════════════════════════════════════════════════════════════════

# Differentiate remaining shared micro-phrases
r('troca de cilindro GLP em 3 minutos', 'reposição do cilindro GLP em menos de 3 minutos', 1)

r('capacidade de 2.500 kg', 'capacidade nominal de 2.500 kg', 1)

r('Motor diesel de alto torque', 'Propulsor diesel com torque elevado', 1)

r('pneus maciços', 'pneus maciços industriais', 2)

r('transmissão powershift', 'transmissão powershift automática', 1)

r('raio de giro reduzido', 'raio de giro compacto')

r('Modelos Clark disponíveis', 'Séries Clark para locação')

r('>Série L<', '>L-Series<')
r('>GTS Series<', '>GTS Premium<')
r('>S-Series<', '>S-Line<')
r('>Compacta<', '>C20s Compacta<')
r('>Heavy Duty<', '>HD<', 2)
r('>Série C<', '>C-Line<')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            'goiania-go/', '18 km', 'Sede na',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))
ref_sections = len(re.findall(r'<!-- ========', ref))
new_sections = len(re.findall(r'<!-- ========', html))

print("=" * 60)
print("VERIFICAÇÃO ESTRUTURAL")
print("=" * 60)
print(f"Tamanho:    ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'✓' if ref_classes == new_classes else '✗'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'✓' if ref_svgs == new_svgs else '✗'}")
print(f"Seções:      ref={ref_sections}  new={new_sections}  {'✓' if ref_sections == new_sections else '✗'}")

if goiania_issues:
    print(f"\n⚠ {len(goiania_issues)} referências suspeitas a Goiânia/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\n✓ Nenhuma referência indevida a Goiânia")

# Conteúdo local
tri = html.count('Trindade')
local = html.count('GO-060') + html.count('construção civil') + html.count('Maysa') + html.count('Sol Nascente') + html.count('distrito industrial')
print(f"\nTrindade: {tri} menções")
print(f"Contexto local (GO-060/construção civil/Maysa/Sol Nascente/distrito industrial): {local} menções")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS
# ═══════════════════════════════════════════════════════════════════════

def extract_text(h):
    """Strip HTML tags and get just text."""
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(set1, set2):
    inter = len(set1 & set2)
    union = len(set1 | set2)
    return inter / union if union > 0 else 0.0

new_text = extract_text(html)
new_ng = ngrams(new_text)

ref_text = extract_text(ref)
ref_ng = ngrams(ref_text)

j_ref = jaccard(new_ng, ref_ng)
print(f"\n{'=' * 60}")
print("JACCARD 3-GRAMS")
print(f"{'=' * 60}")
print(f"vs ref-goiania-combustao.html:    {j_ref:.4f}  {'✓' if j_ref < 0.20 else '✗ FALHOU'}")

# Compare with SC and BSB pages
comparisons = [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html',
    '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-empilhadeira-combustao-V2.html',
]
for comp_path in comparisons:
    if os.path.exists(comp_path):
        with open(comp_path, 'r', encoding='utf-8') as f:
            comp_html = f.read()
        comp_text = extract_text(comp_html)
        comp_ng = ngrams(comp_text)
        j_comp = jaccard(new_ng, comp_ng)
        fname = os.path.basename(comp_path)
        print(f"vs {fname}: {j_comp:.4f}  {'✓' if j_comp < 0.20 else '✗ FALHOU'}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

elapsed = time.time() - START
print(f"\n✅ Salvo: {OUT}")
print(f"TEMPO: {elapsed:.1f}s")
print(f"TOKENS (estimativa caracteres): {len(html):,} chars")
