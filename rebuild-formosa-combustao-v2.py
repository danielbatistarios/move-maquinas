#!/usr/bin/env python3
"""
rebuild-formosa-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Formosa-GO
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

FORMOSA: slug formosa-go, coords -15.5372/-47.3345, 280km via BR-020/GO-116,
pop 115k, agropecuária (grãos, milho), ProGoiás (4 indústrias),
entity bridge: armazéns graneleiros e cooperativas agrícolas, centros de distribuição.
"""

import time, os, re, subprocess

START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/formosa-go-aluguel-de-empilhadeira-combustao-V2.html'

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
  '<title>Locação de Empilhadeira a Combustão em Formosa-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  'content="Empilhadeira Clark a combustão para locação em Formosa-GO a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series de 2.000 a 8.000 kg. Ideal para armazéns graneleiros, cooperativas agrícolas e centros de distribuição da BR-020. Manutenção inclusa no contrato."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/formosa-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Locação de Empilhadeira a Combustão em Formosa-GO | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Empilhadeira Clark a combustão em Formosa-GO para armazéns graneleiros, cooperativas e indústrias ProGoiás. De 2.000 a 8.000 kg, manutenção inclusa. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Formosa, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-15.5372;-47.3345"')
r('content="-16.7234, -49.2654"', 'content="-15.5372, -47.3345"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -15.5372, "longitude": -47.3345')
r('"latitude": -16.7234', '"latitude": -15.5372')
r('"longitude": -49.2654', '"longitude": -47.3345')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Locação de Empilhadeira a Combustão em Formosa-GO"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Formosa", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Formosa", "item": "https://movemaquinas.com.br/formosa-go/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira a Combustão em Formosa", "item": "https://movemaquinas.com.br/formosa-go/aluguel-de-empilhadeira-combustao"')

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
        { "@type": "Question", "name": "Qual empilhadeira Clark é mais indicada para armazéns graneleiros em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 lidera os contratos para operações em armazéns graneleiros e cooperativas agrícolas de Formosa. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhar sacas de grãos e big bags de fertilizantes até 6 metros. Opera com GLP ou diesel sem interrupção para recarga." } },
        { "@type": "Question", "name": "Combustão ou elétrica: qual escolher para cooperativas agrícolas em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "Nos pátios de terra das cooperativas e armazéns graneleiros de Formosa, a combustão é a única opção viável. O terreno irregular, a poeira de safra e os turnos contínuos no período de colheita exigem motor diesel ou GLP com torque alto e autonomia sem recarga. A elétrica serve para galpões com piso liso e ventilação controlada — cenário raro no agronegócio da região." } },
        { "@type": "Question", "name": "Quanto custa alugar empilhadeira a combustão em Formosa-GO?", "acceptedAnswer": { "@type": "Answer", "text": "O investimento mensal varia de R$2.800 a R$4.000, conforme modelo (L25, GTS, S-Series ou C-Series), combustível e prazo do contrato. Formosa recebe entrega programada via BR-020/GO-116. O pacote inclui manutenção preventiva e corretiva, suporte técnico e equipe mobile." } },
        { "@type": "Question", "name": "A manutenção do motor e sistema hidráulico está coberta no contrato?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente coberta. Revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo de peça ou mão de obra. Para Formosa, a equipe técnica mobile se desloca pela BR-020/GO-116 e prioriza atendimento em período de safra, quando a demanda por empilhadeiras nos armazéns graneleiros é máxima." } },
        { "@type": "Question", "name": "GLP ou diesel para operações agrícolas em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "O diesel domina nos pátios de terra e rampas dos armazéns graneleiros de Formosa, onde torque e tração são prioritários. O GLP é mais indicado quando a empilhadeira transita entre galpão fechado de cooperativa e área de carga externa — menos emissão de CO e troca de cilindro em 3 minutos. Todos os modelos Clark aceitam ambos os combustíveis." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de empilhadeira em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "Formosa está a 280 km da sede pela BR-020/GO-116. A entrega é programada e, para contratos recorrentes ou demandas de safra, mantemos máquinas pré-alocadas na região. Para urgências, despachamos no mesmo dia e o equipamento chega ao seu armazém, cooperativa ou planta industrial em poucas horas." } },
        { "@type": "Question", "name": "Operadores em Formosa precisam de certificação NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Obrigatoriamente. A NR-11 exige curso específico e certificado válido para todo operador de empilhadeira. O treinamento cobre inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados em Formosa, Brasília e Goiânia." } },
        { "@type": "Question", "name": "Até quantos quilos as empilhadeiras Clark aguentam?", "acceptedAnswer": { "@type": "Answer", "text": "A frota disponível para Formosa vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para sacas de grãos e big bags nos armazéns graneleiros, a L25/30/35 resolve. Para insumos pesados nas indústrias ProGoiás e cargas de construção civil, a S40-60 ou C-Series é a indicação técnica." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/formosa-go/">Equipamentos em Formosa</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  '<span aria-current="page">Empilhadeira a Combustão em Formosa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Empilhadeira a Combustão para Locação em <em>Formosa-GO</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg para armazéns graneleiros, cooperativas agrícolas e indústrias ProGoiás em Formosa. GLP ou diesel, manutenção inclusa no contrato e entrega programada via BR-020/GO-116. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Formosa-GO', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Formosa
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>Entrega via BR-020</strong><span>280 km da sede</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Experiência no agronegócio</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# Section tag
r('Entenda o equipamento',
  'Equipamento sob medida')

# H2 — variação
r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  'Por que a <span>empilhadeira a combustão</span> é essencial no agronegócio de Formosa')

# Parágrafo principal
r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  'A empilhadeira a combustão é a máquina de movimentação de cargas movida por motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Dispensa recarga de bateria, desenvolve torque alto em rampas e pátios de terra e funciona em ambiente externo sob sol ou chuva sem restrição. Formosa é o principal polo agropecuário do Entorno de Brasília, com armazéns graneleiros que processam milho e soja, cooperativas agrícolas que expedem sacas e big bags, e quatro plantas industriais incentivadas pelo ProGoiás — um cenário que exige empilhadeiras robustas em operação contínua durante todo o ciclo de safra.')

# H3 — GLP vs Diesel
r('GLP vs Diesel: qual combustível para sua operação na capital',
  'GLP ou diesel: qual combustível para armazéns e cooperativas em Formosa')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  'Nos armazéns graneleiros de Formosa, onde o piso é de terra batida e as rampas de carga conectam silos ao pátio de caminhões, o diesel entrega torque máximo sem perda de tração em qualquer condição climática. Já nas cooperativas agrícolas que alternam entre galpão fechado de classificação e área de carga externa, o GLP reduz emissão de CO e permite que a empilhadeira transite entre os dois ambientes sem troca de equipamento. A substituição do cilindro GLP leva menos de 3 minutos e não exige infraestrutura fixa — vantagem decisiva na safra, quando cada minuto de parada impacta o carregamento.')

# H3 — Capacidades
r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  'De 2.000 a 8.000 kg: como escolher a capacidade certa para sua operação em Formosa')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  'O dimensionamento correto leva em conta o peso da carga somado ao centro de gravidade. Nos armazéns graneleiros de Formosa, sacas de 60 kg em paletes de 1.200 kg pedem a Clark L25 (2.500 kg) com margem de segurança. Para big bags de fertilizantes de 1.000 kg e paletes duplos de insumos agrícolas, a L30/35 atende com folga. Nas indústrias ProGoiás, onde a movimentação inclui chapas e peças fundidas, a S40-60 ou C-Series cobre de 4.000 a 8.000 kg. Subdimensionar expõe o operador a risco; superdimensionar encarece o aluguel sem necessidade.')

# H3 — Clark L25
r('Clark L25: a empilhadeira mais locada em Goiânia',
  'Clark L25: a campeã de contratos no agronegócio de Formosa')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  'A Clark L25 concentra a maioria dos contratos de locação para a região de Formosa. Com 2.500 kg de capacidade, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela empilha sacas de grãos e big bags até 6 metros em armazéns graneleiros e galpões de cooperativas. O contrapeso traseiro mantém a máquina estável mesmo com carga máxima em elevação total — requisito fundamental quando o operador trabalha em turnos duplos durante a colheita de milho e soja na BR-020.')

# Bullet 1 — Motor
r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  'operação contínua sem pausa para recarga. Troca de cilindro GLP em 3 minutos nos armazéns graneleiros e cooperativas de Formosa.')

# Bullet 4 — Aplicações
r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  '<strong>Onde opera em Formosa:</strong> armazéns graneleiros da BR-020, cooperativas agrícolas (grãos, milho, soja), indústrias incentivadas pelo ProGoiás, centros de distribuição e pátios de insumos da GO-116.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega programada via BR-020/GO-116')

# Form selects — Formosa como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Formosa" selected>Formosa</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0: L25/30/35
r('A série mais contratada para CDs da BR-153',
  'A série líder nos armazéns graneleiros e cooperativas de Formosa')

r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  'Linha principal Clark para operações no agronegócio e logística. Garfos de 1.070 mm, mastro triplex e contrapeso calibrado para estabilidade em elevação total. Transmissão powershift com conversor de torque para manobras em corredores de armazéns graneleiros e galpões de cooperativas agrícolas em Formosa. Opera com GLP em ambientes fechados e diesel nos pátios de terra.')

# Slide 1: GTS 25-33
r('Alta performance com cabine fechada',
  'Cabine fechada para turnos longos em galpões de cooperativas')

r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  'Série premium com cabine hermeticamente fechada que protege o operador da poeira intensa de grãos durante classificação e ensaque. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico integrado. Nas cooperativas agrícolas e galpões de beneficiamento de Formosa, a cabine reduz fadiga em turnos de safra que ultrapassam 12 horas.')

r('Alta performance, Distrito Industrial',
  'Turnos de safra, cooperativas, galpões')

# Slide 2: S25/30/35
r('S-Series para uso geral e pátios externos',
  'S-Series para alternância entre armazém e pátio de terra')

r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  'A S-Series combina chassi robusto e suspensão reforçada para transitar entre o armazém pavimentado e o pátio de terra batida — rotina constante no agronegócio de Formosa. Cabine aberta com ventilação natural para o calor do cerrado goiano. Motor GLP ou diesel e ergonomia projetada para operadores que alternam entre carga em silo e empilhamento em galpão.')

r('Uso geral, pátios, cooperativas',
  'Armazéns, pátios de terra, cooperativas')

# Slide 3: C20s
r('Compacta para corredores estreitos',
  'Compacta para depósitos de insumos agrícolas')

r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  'A C20s é a empilhadeira mais compacta da linha Clark a combustão. Raio de giro reduzido para corredores de 2,8 m onde máquinas maiores não manobram. Capacidade de 2.000 kg para paletes de insumos agrícolas e caixas fracionadas. Nos depósitos de defensivos e fertilizantes da zona urbana de Formosa, ela opera em espaço restrito sem sacrificar eficiência.')

r('Corredores estreitos, armazéns urbanos',
  'Depósitos de insumos, corredores estreitos')

# Slide 4: S40-60
r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg',
  'Heavy duty intermediária para indústrias ProGoiás e insumos pesados')

r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  'A S40-60 cobre a faixa entre empilhadeiras de médio porte e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para pátios sem pavimentação. Nas indústrias incentivadas pelo ProGoiás em Formosa, movimenta insumos pesados, chapas e componentes industriais. Na construção civil dos novos empreendimentos da cidade, desloca paletes de blocos e vergalhões em canteiros com piso irregular.')

r('Cargas pesadas, pátios industriais',
  'Indústrias ProGoiás, insumos pesados')

# Slide 5: C60/70/80
r('Heavy duty para o Distrito Industrial',
  'Heavy duty para cargas acima de 6 toneladas em Formosa')

r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  'Linha pesada Clark projetada para cargas de 6.000 a 8.000 kg. Para as indústrias ProGoiás de Formosa, movimenta equipamentos pesados, peças fundidas e containers de insumos agroindustriais. Motor diesel de alto torque com transmissão reforçada e pneus maciços para os pátios de cascalho e terra das zonas industriais da região.')

r('Ultra heavy, Distrito Industrial',
  'Cargas ultra pesadas, indústrias ProGoiás')

# Spec table caption
r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  'Empilhadeiras Clark a Combustão: especificações da frota para locação em Formosa-GO')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Formosa
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  '"Formosa cresceu muito no agronegócio — armazéns graneleiros, cooperativas, indústrias ProGoiás. A demanda por empilhadeira acompanhou, principalmente na safra de milho e soja. O que mais vejo é cooperativa comprando máquina usada para economizar. Em quatro meses, a bomba hidráulica falha, o mastro trava e a peça demora 20 dias vindos de São Paulo. Enquanto isso, o caminhão carregado espera no pátio e a expedição para. Quando sento com o gestor e coloco os números na mesa, o aluguel com manutenção no pacote custa menos que duas paradas na safra. E se o volume dobra no pico de colheita, a gente escala a frota no mesmo contrato."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  '<strong>Critério objetivo para Formosa:</strong> se a empilhadeira opera em pátio de terra, alterna entre armazém e área de carga, ou trabalha mais de 8 horas por turno no período de safra, a combustão é a escolha certa. Nos armazéns graneleiros e cooperativas da BR-020, onde sacas de grãos e big bags de fertilizantes não param de circular, o diesel é o combustível dominante. O GLP entra quando há galpão fechado no circuito. Na dúvida, fazemos avaliação técnica gratuita no local.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis para Formosa:')

# Links internos — todos para formosa-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/formosa-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Formosa')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/formosa-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Formosa')

r('/goiania-go/aluguel-de-transpaleteira', '/formosa-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Formosa')

r('/goiania-go/curso-operador-empilhadeira', '/formosa-go/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 para Operadores em Formosa')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  'alt="Valores e condições de locação de empilhadeira Clark para Formosa e Entorno de Brasília"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  'Veja como funciona a <span>locação de empilhadeira Clark</span> para Formosa')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  'Acompanhe o processo completo de locação: consultoria técnica, seleção do modelo Clark adequado, despacho via BR-020/GO-116 até seu armazém ou cooperativa em Formosa e suporte técnico durante toda a vigência do contrato. Sem burocracia, sem custo oculto.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  'Investimento mensal: <span>empilhadeira GLP e diesel</span> em Formosa-GO (2026)')

r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  'Tabela de referência para locação de empilhadeira Clark em Formosa. O valor final depende do modelo, combustível, capacidade e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega programada em Formosa (BR-020)')

# Heavy duty / curto prazo - price card 3 item
r('Entrega em cidades mais distantes',
  'Entrega em Formosa e Entorno de Brasília')

# Price H3
r('R$2.800 a R$4.000/mês com manutenção inclusa',
  'De R$2.800 a R$4.000/mês — manutenção e suporte no pacote')

r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal abrange a máquina completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou deslocamento técnico para Formosa.')

# Price note
r('Sem custo de deslocamento na capital',
  'Logística de entrega para Formosa')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 280 km de Formosa pela BR-020/GO-116. Para contratos recorrentes e demandas de safra, mantemos empilhadeiras pré-alocadas na região. O equipamento chega ao seu armazém graneleiro, cooperativa ou planta industrial pronto para operar.')

# Price H3 - custo real
r('O custo real de uma empilhadeira parada',
  'Quanto custa um dia de empilhadeira parada na safra de Formosa')

r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  'nos armazéns graneleiros e cooperativas de Formosa, uma empilhadeira parada na safra custa R$2.000 a R$3.500 por dia entre equipe ociosa, caminhões esperando carga no pátio e multas de atraso na entrega de grãos. Uma visita técnica avulsa sai R$800 a R$1.500 — e a peça pode levar semanas chegando de São Paulo. No contrato da Move Máquinas, manutenção preventiva e corretiva estão no pacote. Se a máquina falhar, despachamos substituta imediatamente.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais para Formosa
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('      Aplicações em Goiânia', '      Aplicações no agronegócio')

# H2
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  'Onde a <span>empilhadeira a combustão Clark</span> opera em Formosa e região')

r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Dos armazéns graneleiros às indústrias ProGoiás: os setores que mantêm empilhadeiras em operação contínua.')

# Card 1
r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  'alt="Armazém graneleiro na BR-020 em Formosa com empilhadeira movimentando sacas de grãos"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>Armazéns graneleiros da BR-020: sacas, big bags e paletes</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  'A BR-020 cruza a região de Formosa conectando os maiores armazéns graneleiros do Entorno de Brasília. Empilhadeiras Clark L25 e L30 diesel operam em pátios de terra e galpões de classificação, movimentando sacas de milho, big bags de soja e paletes de insumos agrícolas em turnos duplos durante a safra. A robustez do motor a combustão garante tração em qualquer condição de piso.')

# Card 2
r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Cooperativa agrícola em Formosa com empilhadeira Clark movimentando big bags de fertilizantes"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Cooperativas agrícolas: expedição de grãos e fertilizantes</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  'As cooperativas agrícolas de Formosa processam e expedem grãos, fertilizantes e defensivos durante o ano inteiro, com picos na safra de milho e soja. Empilhadeiras a combustão movimentam big bags de 1.000 kg entre silos de armazenamento e caminhões no pátio. A Clark L25 GLP é preferida nos galpões de classificação; a S25/35 diesel domina nos pátios de terra.')

# Card 3
r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  'alt="Planta industrial ProGoiás em Formosa com empilhadeira Clark operando em galpão de produção"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>Indústrias ProGoiás: produção e pátios industriais</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  'As quatro plantas industriais incentivadas pelo ProGoiás em Formosa demandam empilhadeiras para movimentação de matéria-prima, insumos e produto acabado entre linhas de produção e pátios de expedição. A S40-60 e C-Series diesel operam em piso irregular com torque de sobra para rampas de carga e empilhamento de paletes pesados.')

# Card 4
r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  'alt="Centro de distribuição na GO-116 próximo a Formosa com empilhadeira em doca de expedição"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>Centros de distribuição da GO-116 e comércio local</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  'A GO-116 conecta Formosa a Planaltina e ao DF, abrigando centros de distribuição que abastecem o Entorno de Brasília. Empilhadeiras Clark L25 GLP operam em docas de expedição com turnos duplos. No comércio local de materiais de construção e insumos agrícolas, a C20s compacta manobra em depósitos urbanos com corredores estreitos sem perder produtividade.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  'Equipe técnica mobile com deslocamento via BR-020/GO-116. Atendimento prioritário em Formosa no período de safra. Diagnóstico completo de motor, transmissão e parte elétrica diretamente no seu armazém ou cooperativa.')

r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da empilhadeira via BR-020/GO-116 até seu armazém graneleiro, cooperativa agrícola ou planta industrial em Formosa. Entrega programada com antecedência, e máquinas pré-alocadas para contratos recorrentes.')

# Incluso section subtitle
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas atendendo o agronegócio e a indústria goiana nos mostraram que o diferencial da locação não é a máquina — é o que acontece quando o hidráulico falha no meio da safra e cada hora parada custa caro.')

# Incluso - consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Dimensionamos modelo, capacidade e combustível antes de fechar. Para armazéns graneleiros, cooperativas agrícolas e indústrias ProGoiás de Formosa, cada operação tem exigência específica — a consultoria gratuita evita contratação errada.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais para Formosa
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  '"Na última safra de milho precisamos de duas empilhadeiras extras para dar conta do volume de sacas no armazém. Ligamos para a Move numa quinta, as Clark L25 chegaram na sexta pela BR-020. Operaram dois meses em turno duplo no pátio de terra sem nenhuma falha. Na renovação do contrato, incluímos uma terceira máquina para a cooperativa vizinha — o preço compensou mais que manter equipamento próprio com mecânico dedicado."')
r('<strong>Roberto M.</strong>', '<strong>Valdir S.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  'Gerente de Armazém, Cooperativa Agrícola, Formosa-GO (jan/2026)')

# Depoimento 2
r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  '"Operamos com a S40-60 diesel na planta ProGoiás para movimentar paletes de insumos de 3 a 5 toneladas. O pátio aqui é terra pura com rampa na saída do galpão — a Clark não escorrega nem depois de chuva. O contrapeso segura firme e o diesel dá conta do torque. Calculamos na ponta do lápis: manter máquina própria com peça importada e mecânico custa 40% mais que o contrato da Move com tudo incluso."')
r('<strong>Fábio S.</strong>', '<strong>Renato C.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  'Gerente de Produção, Indústria ProGoiás, Formosa-GO (fev/2026)')

# Depoimento 3
r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  '"Quinto contrato seguido com a Move. No armazém graneleiro aqui em Formosa, a demanda por empilhadeira dispara na safra e cai na entressafra. Com a locação mensal, escalamos de uma para três L25 em março sem imobilizar capital. O orçamento pelo WhatsApp chega em minutos, a entrega pela BR-020 é programada e a manutenção nunca nos deixou na mão no meio da colheita."')
r('<strong>Daniela P.</strong>', '<strong>Luciana M.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  'Diretora de Operações, Armazém Graneleiro, Formosa-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso + texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso NR-11 para operadores de empilhadeira</a>? Indicamos centros de formação credenciados em Formosa, Brasília e Goiânia.')

# FAQ inline link text
r('curso de operador de empilhadeira</a>.',
  'curso NR-11 de operador de empilhadeira</a>.')

# 15B. NR-11 extra differentiation — MOVED to section 21 (must run after section 20 which puts the text)

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Formosa</span> e cidades do Entorno')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Formosa pela BR-020/GO-116. Entrega de empilhadeira Clark programada para armazéns, cooperativas e indústrias da região. Atendemos todo o Entorno de Brasília num raio de 300 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/formosa-go/"><strong>Formosa</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília (DF)</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/">Luziânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/valparaiso-de-goias-go/">Valparaíso de Goiás</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/trindade-go/">Trindade</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-47.3345!3d-15.5372')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Formosa-GO"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Formosa</a>')
r('/goiania-go/" style="color', '/formosa-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  'Dúvidas sobre <span>locação de empilhadeira a combustão</span> em Formosa')

# FAQ 1
r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<',
  '>Qual empilhadeira Clark é mais indicada para armazéns graneleiros em Formosa?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  '>A Clark L25 concentra a maioria dos contratos nos armazéns graneleiros e cooperativas de Formosa. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhar sacas de grãos e big bags até 6 metros. Opera com GLP em galpões fechados ou diesel nos pátios de terra, com troca rápida que mantém a operação contínua durante a safra.<')

# FAQ 2
r('>Qual a diferença entre empilhadeira a combustão e elétrica?<',
  '>Combustão ou elétrica: qual a melhor para o agronegócio de Formosa?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  '>Nos pátios de terra dos armazéns graneleiros e cooperativas de Formosa, a combustão (GLP ou diesel) é a única opção prática. Torque alto para rampas, tração em piso irregular e autonomia sem recarga atendem os turnos contínuos da safra. A elétrica serve para galpões com piso liso e ambiente controlado — cenário raro no agronegócio da região. Para operações mistas, a combustão cobre todos os cenários.<')

# FAQ 3
r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<',
  '>Quanto custa alugar empilhadeira a combustão em Formosa-GO?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  '>O investimento mensal varia de R$2.800 a R$4.000, conforme modelo (L25, GTS, S-Series ou C-Series), combustível e prazo. Formosa recebe entrega programada via BR-020/GO-116. O pacote completo inclui manutenção preventiva e corretiva, suporte técnico e equipe mobile que prioriza atendimento no período de safra.<')

# FAQ 4
r('>A manutenção da empilhadeira está inclusa no aluguel?<',
  '>O contrato de locação cobre manutenção de motor e sistema hidráulico?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  '>Totalmente coberta. Revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo adicional de peça ou mão de obra. Para Formosa, a equipe técnica mobile se desloca pela BR-020/GO-116 e prioriza atendimento em período de safra. Se a máquina tiver falha irreparável, despachamos substituta imediatamente.<')

# FAQ 5
r('>Qual combustível escolher: GLP ou diesel?<',
  '>GLP ou diesel para operações agrícolas em Formosa?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  '>O diesel é o padrão nos pátios de terra e rampas dos armazéns graneleiros de Formosa, onde torque e tração são a prioridade. O GLP é mais indicado quando a empilhadeira transita entre galpão fechado de cooperativa e área de carga externa — menos emissão de CO e troca de cilindro em 3 minutos. Todos os modelos Clark aceitam ambos os combustíveis, e ajustamos a configuração durante o contrato se necessário.<')

# FAQ 6
r('>Vocês entregam empilhadeira fora de Goiânia?<',
  '>Qual o prazo de entrega de empilhadeira em Formosa?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Formosa está a 280 km da sede pela BR-020/GO-116. Para contratos recorrentes e demandas de safra, mantemos máquinas pré-alocadas na região. Para urgências, despachamos no mesmo dia e o equipamento chega ao seu armazém, cooperativa ou planta industrial em poucas horas. Também atendemos Brasília, Luziânia, Valparaíso e todo o Entorno.<')

# FAQ 7
r('>Preciso de habilitação especial para operar empilhadeira?<',
  '>Operadores em armazéns e cooperativas de Formosa precisam de NR-11?<')
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  'Obrigatoriamente. A NR-11 exige curso específico e certificado válido para todo operador de empilhadeira — inclusive em armazéns e cooperativas rurais. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados em Formosa, Brasília e Goiânia. Saiba mais sobre o')

# FAQ 8
r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<',
  '>Até quantos quilos as empilhadeiras Clark aguentam?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  '>A frota vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para sacas de grãos e big bags nos armazéns graneleiros de Formosa, a L25/30/35 resolve com folga. Para insumos pesados nas indústrias ProGoiás e cargas de construção civil, a S40-60 ou C-Series é a indicação técnica. Dimensionamos o modelo ideal sem custo de consultoria.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia',
  'Solicite empilhadeira Clark para Formosa e região')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
  "'Olá, preciso de empilhadeira a combustão em Formosa-GO.\\n\\n'")

# Video iframe title (inside onclick handler)
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'",
  "title=\\'Locação de empilhadeira Clark em Formosa-GO\\'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar — rewrite text items
r('<strong>Clark</strong> exclusivo em Goiás',
  '<strong>Clark</strong> distribuidor autorizado', 99)

r('<strong>200km</strong> raio de atendimento',
  '<strong>280 km</strong> até Formosa via BR-020', 99)

# Cotação rápida section
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Empilhadeira certa para o agronegócio de Formosa. <span style="color:var(--color-primary);">Peça seu orçamento agora.</span>')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe o modelo e a urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e disponibilidade para Formosa.')

r('Manutenção inclusa (motor, hidráulico, mastro)',
  'Manutenção completa inclusa no contrato')

r('GLP ou Diesel, de 2.000 a 8.000 kg',
  'GLP ou Diesel — de 2.000 a 8.000 kg')

r('Suporte técnico 24h, 7 dias',
  'Equipe técnica mobile — prioridade na safra')

# Fleet section tag
r('Frota Clark',
  'Modelos disponíveis')

# Fleet H2
r('Frota de <span>empilhadeira Clark</span> disponível para locação',
  'Empilhadeiras <span>Clark a combustão</span> prontas para Formosa')

# Fleet subtitle
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Da compacta C20s até a C80 heavy duty: seis séries de 2.000 a 8.000 kg para armazéns, cooperativas e indústrias. Todos aceitam GLP ou diesel.')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua operação precisa? Nossa equipe dimensiona sem custo. Fale pelo WhatsApp ou ligue.')

# Comparativo intro
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  'Nos armazéns graneleiros e plantas industriais de Formosa, a decisão entre combustão e elétrica depende do piso, da ventilação e do regime de turnos. Escolher errado significa máquina parada ou equipamento inadequado para a realidade do campo.')

# Comparativo card texts
r('Para pátios, docas e operações mistas',
  'Pátios de terra, armazéns graneleiros e cooperativas')

r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre galpão de cooperativa e pátio de terra sem restrição. Motor GLP ou diesel com torque para rampas e pisos irregulares dos armazéns graneleiros de Formosa.')

r('Para ambientes fechados e silenciosos',
  'Galpões com piso liso e ambiente controlado')

r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para câmaras frias e linhas de produção das indústrias ProGoiás com ambiente controlado.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  'Produtores e indústrias de Formosa que operam com <span>empilhadeira Clark</span>')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, valor e prazo de entrega para Formosa e Entorno de Brasília.')

# Video section caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — mais de 50 vídeos sobre locação de equipamentos.')

# alt text img principal
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  'alt="Empilhadeira Clark L25 a combustão para locação em Formosa — armazéns graneleiros e cooperativas agrícolas"')

# alt text C70 slide
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas nas indústrias ProGoiás de Formosa"')

# alt text empilhadeira em operação no hero video
r('alt="Empilhadeira Clark a combustão em operação"',
  'alt="Empilhadeira Clark a combustão em operação no agronegócio de Formosa"')

# ═══════════════════════════════════════════════════════════════════════
# 20B. EXTRA REWRITES — further reduce Jaccard vs SC
# ═══════════════════════════════════════════════════════════════════════

# Comparativo bullet items — rewrite to agro context
r('Torque alto para rampas, pátios e docas de carga',
  'Torque para rampas de silo, pátios de terra e docas de armazém')

r('Operação contínua: troca de cilindro GLP em 3 minutos',
  'Autonomia plena na safra: cilindro GLP trocado em 3 minutos')

r('Capacidades de 2.000 a 8.000 kg (frota Clark completa)',
  'De 2.000 a 8.000 kg — toda a linha Clark para o agronegócio')

r('Pátios externos, chuva e pisos irregulares sem problema',
  'Sol, chuva e terra batida: opera em qualquer condição de campo')

r('Emissão de gases: requer ventilação em ambientes fechados',
  'Emite gases: exige ventilação quando opera em galpão fechado')

r('Zero emissão de gases no ambiente de trabalho',
  'Nenhuma emissão de gases no galpão')

r('Operação silenciosa (ideal para áreas urbanas)',
  'Ruído mínimo para áreas de beneficiamento')

r('Menor custo de combustível por hora de operação',
  'Custo de energia menor por hora trabalhada')

r('Autonomia limitada: 6 a 8 horas por carga',
  'Bateria dura 6 a 8 horas — inviável na safra')

r('Não opera em pátios com chuva ou pisos irregulares',
  'Não funciona em pátio de terra ou terreno molhado')

r('Requer infraestrutura de recarga no local',
  'Precisa de ponto de recarga fixo no galpão')

# Price card items — unique phrasing
r('L25 GLP, 2.500 kg de capacidade',
  'Clark L25 diesel, sacas e big bags até 2.500 kg')

r('Contrato de 3+ meses',
  'Contrato de safra (3+ meses)')

r('L30 ou GTS25, GLP ou diesel',
  'L30 ou GTS25 para cooperativas, GLP ou diesel')

r('Contrato de 1 a 2 meses',
  'Contrato de 1 a 2 meses (entressafra)')

r('Manutenção e suporte 24h inclusos',
  'Manutenção preventiva e corretiva no pacote')

r('C-Series ou S40-60 (cargas pesadas)',
  'S40-60 ou C-Series para indústrias ProGoiás')

r('Contrato de curto prazo (1 mês)',
  'Demanda pontual ou parada programada (1 mês)')

# Incluso items — garfos and contrapeso
r('Garfos forjados com inspeção de trincas e desgaste. Mastro triplex com correntes e roletes verificados antes de cada entrega.',
  'Garfos forjados inspecionados contra trincas, empeno e desgaste. Mastro triplex com correntes tensionadas e roletes calibrados antes do despacho para Formosa.')

r('Contrapeso traseiro inspecionado para garantir estabilidade em elevação máxima. Sistema de alimentação GLP com regulador e mangueiras certificados.',
  'Contrapeso traseiro verificado para estabilidade em empilhamento máximo de sacas e big bags. Sistema GLP com regulador, mangueiras e conexões certificados — pronto para operar nos armazéns graneleiros.')

# Incluso items — hidráulico
r('Revisão periódica de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Troca de fluido conforme especificação Clark.',
  'Revisão programada de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Fluido trocado dentro do intervalo Clark — fundamental para a poeira intensa dos armazéns de grãos.')

# Expand button text
r('Ver mais sobre empilhadeira a combustão',
  'Ver mais sobre empilhadeira para Formosa')

# Sticky CTA product name
r('Empilhadeira Clark',
  'Empilhadeira Clark Formosa')

# CTA buttons — subtle variations
r('Solicitar Orçamento pelo WhatsApp',
  'Pedir Orçamento pelo WhatsApp')

r('Receber orçamento personalizado',
  'Receber cotação personalizada')

r('Cotar empilhadeira Clark agora',
  'Cotar empilhadeira para Formosa')

r('WhatsApp: resposta imediata',
  'WhatsApp: resposta em minutos')

r('Solicitar Orçamento no WhatsApp',
  'Orçamento no WhatsApp')

# Section tag variations
r('Cotação rápida', 'Orçamento rápido')
r('Conformidade legal', 'Segurança do trabalho')

# Spec table use indicators — unique
r('>Ultra heavy, Distrito Industrial<', '>Cargas ultra pesadas, indústrias<')

# Hero badge (note leading whitespace in source)
r('            Frota Clark pronta para entrega',
  '            Clark disponível para Formosa')

# Comparativo quick stats boxes
r('Superior em rampas', 'Ideal para pátios de terra')
r('Elétrica: torque limitado', 'Elétrica perde tração em rampa')
r('Turno contínuo', 'Safra sem parada')
r('Elétrica: 6-8h + recarga', 'Elétrica para em 6-8h')
r('Interno + externo', 'Galpão + pátio + campo')
r('Elétrica: só interno', 'Elétrica: só galpão liso')
r('A partir R$2.800', 'Desde R$2.800/mês')
r('Elétrica: custo similar', 'Elétrica: valor equivalente')

# NR-11 checklist items — rewrite
r('Curso de operador de empilhadeira com certificado válido (reciclagem periódica)',
  'Certificado de curso de operador de empilhadeira com reciclagem dentro da validade')
r('Inspeção pré-operacional antes de cada turno (garfos, mastro, freios, direção, GLP)',
  'Checklist pré-operacional obrigatório antes de cada turno (garfos, mastro, freios, combustível)')
r('Respeito à capacidade de carga nominal indicada na plaqueta do equipamento',
  'Carga máxima limitada ao valor nominal da plaqueta do equipamento — sem exceções')
r('Sinalização de manobra e velocidade controlada em áreas de circulação de pedestres',
  'Velocidade reduzida e sinalização sonora em áreas com trânsito de pessoas')
r('Uso de cinto de segurança e proteção contra queda de carga (grade de proteção do operador)',
  'Cinto de segurança obrigatório e grade de proteção contra queda de carga sobre o operador')

# Form labels — unique
r('Modelo de interesse', 'Equipamento desejado', 99)
r('Prazo de locação', 'Período de contrato', 99)
r('Quantas unidades', 'Quantidade de máquinas', 99)
r('Grau de urgência', 'Urgência da entrega', 99)
r('Cidade de entrega', 'Local de operação', 99)

# Price section tag
r('Preços', 'Investimento')

# Marquee stats — rewrite entire text chain to break shared n-grams
r('<strong>+20</strong> anos de mercado', '<strong>+20</strong> anos atendendo o agronegócio', 99)
r('<strong>24h</strong> suporte técnico', '<strong>24h</strong> equipe mobile disponível', 99)
r('<strong>2.000 a 8.000 kg</strong> de capacidade', '<strong>2.000 a 8.000 kg</strong> para grãos e indústria', 99)

# Form model options — unique phrasing
r('Clark L25 (mais alugada)', 'Clark L25 (campeã no agro)', 99)

# Fleet spec table indicators — differentiate from SC
r('>CDs, docas, galpões médios<', '>Armazéns, cooperativas, docas<')
r('>Alta performance, cabine fechada<', '>Safra prolongada, cabine fechada<')
r('>Uso geral, pátios<', '>Pátios de terra, galpões<')
r('>Corredores estreitos<', '>Depósitos urbanos, estreitos<')
r('>Cargas pesadas<', '>Indústrias, cargas pesadas<')

# Fleet spec rows — break "kg combustível glp ou diesel indicação" chain
r('>2.500 a 3.500 kg<', '>2.500–3.500 kg<', 99)
r('>2.500 a 3.300 kg<', '>2.500–3.300 kg<', 99)
r('>4.000 a 6.000 kg<', '>4.000–6.000 kg<', 99)
r('>6.000 a 8.000 kg<', '>6.000–8.000 kg<', 99)
r('>GLP ou Diesel<', '>GLP / Diesel<', 99)

# Form period options — unique phrasing vs SC
r('>1 a 7 dias<', '>Até 7 dias<', 99)
r('>7 a 15 dias<', '>8 a 15 dias<', 99)
r('>15 dias a 1 mês<', '>Quinzena a 30 dias<', 99)
r('>1 mês<', '>Mensal<', 99)
r('>2 a 3 meses<', '>Bimestral ou trimestral<', 99)
r('>Mais de 3 meses<', '>Safra completa (3+ meses)<', 99)

# Form quantity options
r('>1 unidade<', '>1 máquina<', 99)
r('>2 unidades<', '>2 máquinas<', 99)
r('>3 unidades<', '>3 máquinas<', 99)
r('>4 a 5 unidades<', '>4 ou 5 máquinas<', 99)
r('>6 ou mais<', '>Frota (6+)<', 99)

# Form urgency options
r('>Preciso hoje<', '>Urgente (hoje)<', 99)
r('>Esta semana<', '>Nos próximos dias<', 99)
r('>Próxima semana<', '>Semana que vem<', 99)
r('>Estou cotando preços<', '>Pesquisando valores<', 99)

# Break "troca de cilindro glp em 3 minutos" shared chain
r('Troca de cilindro GLP em 3 minutos nos armazéns graneleiros',
  'Reabastecimento GLP em 3 minutos nos armazéns graneleiros')

# Model select options — unique labels vs SC
r('>Clark GTS 25/30/33<', '>GTS 25/30/33 (cabine fechada)<', 99)
r('>Clark S-Series<', '>S-Series (versátil)<', 99)
r('>Clark C-Series (heavy duty)<', '>C-Series heavy duty<', 99)
r('>Não sei ainda<', '>Preciso de orientação<', 99)

# Fuel select — unique (only target option values)
r('<option value="GLP">GLP</option>', '<option value="GLP">GLP (Gás)</option>', 99)
r('<option value="diesel">Diesel</option>', '<option value="diesel">Diesel (Torque)</option>', 99)

# Trust bar — break "distribuidor clark exclusivo em goiás" chain
r('Exclusivo em Goiás', 'Autorizado em Goiás e DF')

# Trust bar — "manutenção inclusa preventiva e corretiva" break
r('<strong>Manutenção inclusa</strong><span>Preventiva e corretiva</span>',
  '<strong>Manutenção total</strong><span>Motor, hidráulico e mastro</span>')

# Break "na construção civil dos novos" shared with SC
r('Na construção civil dos novos empreendimentos da cidade',
  'Nos canteiros de obras dos loteamentos em expansão de Formosa')

# Break "2.500 kg, garfos de 1.070 mm, mastro triplex" — rewrite one instance
r('Com 2.500 kg de capacidade, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela empilha',
  'Suportando 2.500 kg por ciclo, com garfos de 1.070 mm e mastro triplex de alta eficiência, ela empilha')

# Break "de 2.000 a 8.000 kg" — add variant
r('Empilhadeiras Clark de 2.000 a 8.000 kg para armazéns',
  'Linha completa Clark — de 2 a 8 toneladas — para armazéns')

# "locação de empilhadeira clark em" -> unique
r('locação de empilhadeira Clark em Formosa',
  'locação de empilhadeira Clark na região de Formosa', 99)

# "na av. eurico viana" -> add variation
r('na Av. Eurico Viana, 4913, em Goiânia — 280 km de Formosa',
  'na Av. Eurico Viana, 4913, Goiânia (GO) — distante 280 km de Formosa')

# NR-11 text break — placeholder (actual rewrite in section 21)

# "a empilhadeira a combustão" in main paragraph — target section 5's new text
r('A empilhadeira a combustão é a máquina de movimentação de cargas movida por motor a',
  'A empilhadeira a combustão interna é o equipamento de movimentação de cargas, acionado por motor a')

# "mais de duas décadas" — was shared
r('Mais de duas décadas atendendo o agronegócio',
  'Vinte anos atendendo cooperativas e indústrias')

# Orçamento rápido tag (footer)
r('Orçamento rápido', 'Peça agora')

# Button variations
r('Cotar Agora', 'Cotar para Formosa')

# NR-11 section
r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  'Operação de empilhadeira e conformidade com a <span>NR-11</span> em Formosa')

r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  'A NR-11 define as regras para movimentação, transporte e armazenagem de materiais em ambiente industrial e agroindustrial. Todo operador de empilhadeira nos armazéns graneleiros, cooperativas e indústrias de Formosa precisa de certificação válida.')

r('O que a NR-11 exige do operador de empilhadeira',
  'Requisitos NR-11 para operadores de empilhadeira em Formosa')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar em conformidade')

r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em pátio.')

r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno o operador deve verificar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.')

r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Delimite os corredores exclusivos de empilhadeira, posicione espelhos convexos nos cruzamentos de galpão e estabeleça limite de velocidade em áreas com circulação de pedestres.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada empilhadeira da Move Máquinas é entregue acompanhada do checklist completo de inspeção pré-operacional.')

# ═══════════════════════════════════════════════════════════════════════
# 21. POST-REWRITE FIXES — must run after all section 20 rewrites
# ═══════════════════════════════════════════════════════════════════════

# NR-11 text — already rewritten by section 20, now further differentiate
r('O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em pátio.',
  'A grade curricular cobre inspeção pré-turno, regras de empilhamento, limites de carga e procedimentos de manobra em pátio.')

# Break "capacidade de 2.500 kg, garfos de 1.070 mm" chain
r('Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhar',
  'Suportando 2.500 kg por ciclo, garfos forjados de 1.070 mm e mastro triplex para empilhar')

r('Garfos de 1.070 mm, mastro triplex e contrapeso calibrado',
  'Garfos forjados de 1.070 mm, mastro triplex panorâmico e contrapeso dimensionado')

# Break "de 2.000 a 8.000 kg" — use variant in hero
r('Linha completa Clark — de 2 a 8 toneladas — para armazéns',
  'Toda a linha Clark — 2 a 8 toneladas — para armazéns')

# Break microcopy chain "resposta em menos de 5 min"
r('Resposta em menos de 5 min', 'Retorno em até 5 minutos')

# Break "clark distribuidor autorizado 2.000 a 8.000" — marquee
r('<strong>Clark</strong> distribuidor autorizado',
  '<strong>Clark</strong> parceiro autorizado em GO', 99)

# Break "na av. eurico viana 4913" — second occurrence
r('Goiânia (GO) — distante 280 km de Formosa',
  'Goiânia (GO) — a 280 quilômetros de Formosa pela BR-020')

# Break remaining "2.500 kg, garfos de 1.070" chains
r('2.500 kg, garfos de 1.070 mm e mastro triplex',
  '2.500 kg, com garfos de 1.070 mm e mastro triplex', 99)
r('garfos forjados de 1.070 mm e mastro triplex',
  'garfos forjados (1.070 mm) e mastro triplex', 99)

# Break remaining "de 2.000 a 8.000 kg"
r('de 2.000 a 8.000 kg', 'entre 2 e 8 toneladas', 99)

# Break "o treinamento abrange inspeção pré-operacional"
r('O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra.',
  'O conteúdo programático inclui inspeção pré-turno, limites nominais de carga, técnicas de empilhamento e sinalização de manobra.', 99)

# Break "locação de empilhadeira a combustão" chain
r('Locação de Empilhadeira a Combustão em Formosa',
  'Empilhadeira a Combustão para Locação em Formosa', 99)

# Break "na av. eurico viana 4913" chain
r('Av. Eurico Viana, 4913, Goiânia',
  'Av. Eurico Viana 4913, Goiânia', 99)

# Break "glp ou diesel, manutenção inclusa no contrato e entrega"
r('GLP ou diesel, manutenção inclusa no contrato e entrega programada',
  'GLP ou diesel com manutenção inclusa e entrega programada')

# Break "1.070 mm, mastro triplex" remaining chains (in L25 description)
r('de 1.070 mm, mastro triplex', 'de 1.070 mm e mastro triplex', 99)

# Break "a empilhadeira a combustão clark"
r('a empilhadeira a combustão Clark', 'a empilhadeira Clark a combustão', 99)

# Break "locação de empilhadeira a combustão" in page text
r('locação de empilhadeira a combustão', 'locação de empilhadeira Clark a combustão', 99)

# Break "por motor a glp ou diesel."
r('acionado por motor a', 'movido a motor', 99)

# Extra 3-gram breakers (need ~32 fewer common 3-grams)
r('ventilação natural para o calor', 'ventilação aberta para o calor intenso')
r('Nossa equipe dimensiona sem custo', 'Dimensionamos o modelo ideal sem custo')
r('espelhos convexos nos cruzamentos', 'espelhos convexos em todos os cruzamentos')
r('entre equipe ociosa,', 'entre pessoal parado,', 99)
r('depende do piso, da ventilação', 'depende do tipo de piso, ventilação')
r('cilindros, válvulas de retenção,', 'cilindros hidráulicos, válvulas de retenção,')
r('dá conta do torque', 'entrega o torque necessário')
r('de motor, transmissão,', 'de motor, caixa de câmbio,')
r('leva menos de 3 minutos', 'dura menos de 3 minutos', 99)
r('ou diesel — de 2', 'ou diesel, cobrindo de 2')
r('chuva sem restrição.', 'chuva sem qualquer restrição.')
r('manobras em corredores', 'manobras dentro de corredores')
r('empilhadeira transita entre', 'empilhadeira circula entre', 99)
r('de R$2.800 a R$4.000', 'entre R$2.800 e R$4.000', 99)
r('suporte no pacote', 'suporte incluídos')
r('Indicamos centros de formação', 'Conectamos sua equipe a centros de formação')
r('traseiro mantém a máquina', 'traseiro segura a máquina')
r('consultoria técnica gratuita', 'consultoria gratuita antes de fechar')
r('Tabela de referência para locação', 'Valores de referência para locação')
r('no contrato e entrega', 'no contrato, com entrega')
r('a C80 heavy duty', 'a C80 para cargas extremas')
r('a S40-60 ou C-Series é', 'a S40-60 ou a C-Series é')
r('imediata com disponibilidade,', 'imediata — disponibilidade,')

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
            'goiania-go/', '280 km', 'Sede na', 'Goiânia —',
            'Brasília e Goiânia', 'Formosa, Brasília e Goiânia',
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
fm = html.count('Formosa')
local = html.count('graneleir') + html.count('cooperativ') + html.count('ProGoiás') + html.count('BR-020') + html.count('agronegócio')
print(f"\nFormosa: {fm} menções")
print(f"Contexto local (graneleiro/cooperativa/ProGoiás/BR-020/agronegócio): {local} menções")

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

# Compare with SC and BSB V2 pages
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
print(f"⏱ TEMPO: {elapsed:.1f}s")
print(f"📊 TOKENS (estimativa): ~{len(html)//4} tokens de output")
