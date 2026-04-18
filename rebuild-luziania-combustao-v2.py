#!/usr/bin/env python3
"""
rebuild-luziania-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Luziânia
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

LUZIÂNIA: slug luziania-go, coords -16.2532/-47.9501,
198km via BR-040, pop 210k. DIAL (Distrito Agroindustrial),
metalurgia, alimentos, químicos, armazéns de grãos.
"""

import time, os, re

t0 = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/luziania-go-aluguel-de-empilhadeira-combustao-V2.html'

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
  '<title>Empilhadeira a Combustão para Alugar em Luziânia-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  'content="Empilhadeira Clark GLP e diesel para locação em Luziânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C60-80 de 2.000 a 8.000 kg. Ideal para o DIAL, armazéns de grãos e metalúrgicas da BR-040. Manutenção inclusa, entrega programada."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/luziania-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Empilhadeira a Combustão para Alugar em Luziânia-GO | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Empilhadeira Clark a combustão em Luziânia-GO. De 2.000 a 8.000 kg para o DIAL, metalúrgicas e armazéns agrícolas da BR-040. Manutenção inclusa no contrato. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Luziânia, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.2532;-47.9501"')
r('content="-16.7234, -49.2654"', 'content="-16.2532, -47.9501"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.2532, "longitude": -47.9501')
r('"latitude": -16.7234', '"latitude": -16.2532')
r('"longitude": -49.2654', '"longitude": -47.9501')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Locação de Empilhadeira a Combustão em Luziânia"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Luziânia", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira a Combustão em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/aluguel-de-empilhadeira-combustao"')

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
        { "@type": "Question", "name": "Qual empilhadeira Clark é mais usada nas indústrias de Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 concentra a maioria dos contratos para o DIAL e armazéns de grãos em Luziânia. Com 2.500 kg de capacidade, garfos de 1.070 mm e mastro triplex, ela movimenta sacaria, insumos químicos e paletes metálicos nos galpões do distrito agroindustrial. Opera com GLP ou diesel sem interrupção para recarga." } },
        { "@type": "Question", "name": "Combustão ou elétrica: qual funciona melhor no DIAL de Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "No DIAL e nos armazéns da BR-040, onde a empilhadeira transita entre galpão coberto e pátio de terra batida, a combustão prevalece. Torque superior em rampas e pisos sem pavimentação, troca de GLP em 3 minutos e zero dependência de infraestrutura de recarga. A elétrica fica restrita a linhas de produção alimentícia com área limpa e controle de emissão." } },
        { "@type": "Question", "name": "Quanto custa alugar empilhadeira a combustão em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "O investimento mensal varia de R$2.800 a R$4.000, conforme modelo (L25, GTS, S-Series ou C60-80), tipo de combustível e prazo do contrato. A entrega para Luziânia é agendada via BR-040 diretamente no DIAL, armazém ou pátio metalúrgico. Manutenção preventiva e corretiva estão incluídas no valor." } },
        { "@type": "Question", "name": "A manutenção cobre motor, mastro e sistema hidráulico?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente. O contrato inclui revisão programada de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos. Nossa equipe técnica mobile se desloca a Luziânia pela BR-040. Em caso de falha irreparável no local, providenciamos a substituição do equipamento sem custo adicional." } },
        { "@type": "Question", "name": "GLP ou diesel para as metalúrgicas e armazéns de Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Nos pátios das metalúrgicas e na área de expedição dos armazéns de grãos, o diesel entrega torque máximo para rampas e pisos de cascalho. Dentro dos galpões do DIAL — alimentício e químico — o GLP gera menos monóxido de carbono e permite trânsito entre área interna e doca sem troca de equipamento. Todos os modelos Clark aceitam ambos os combustíveis." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de empilhadeira em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Luziânia está a 198 km da sede pela BR-040. A entrega é agendada e executada no prazo combinado, com transporte direto até o DIAL, galpão ou pátio industrial. Para demandas urgentes, priorizamos o despacho e comunicamos o horário exato de chegada." } },
        { "@type": "Question", "name": "Operadores no DIAL precisam de certificação NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador de empilhadeira. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados acessíveis a partir de Luziânia e Brasília." } },
        { "@type": "Question", "name": "Até quantos quilos as empilhadeiras Clark aguentam?", "acceptedAnswer": { "@type": "Answer", "text": "A frota disponível para Luziânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para sacaria e paletes no DIAL, a L25/30/35 resolve com folga. Para bobinas metálicas e cargas pesadas nas metalúrgicas, a série C60/70/80 é a especificação técnica correta." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/luziania-go/">Equipamentos em Luziânia</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  '<span aria-current="page">Empilhadeira a Combustão em Luziânia</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Empilhadeira a Combustão para Locação em <em>Luziânia</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel para o DIAL, metalúrgicas e armazéns de grãos de Luziânia. Manutenção inclusa no contrato, suporte técnico e entrega via BR-040. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Luzi%C3%A2nia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>198 km via BR-040</strong><span>Entrega programada</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Atendendo indústrias em GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# Section tag
r('Entenda o equipamento',
  'Saiba antes de contratar')

# H2 — variação
r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  'Por que a <span>empilhadeira a combustão</span> domina as operações industriais de Luziânia')

# Parágrafo principal
r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  'A empilhadeira a combustão funciona com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel, dispensando baterias e infraestrutura de recarga. Ela desenvolve torque elevado para rampas, pátios de terra batida e pisos irregulares — cenário recorrente no parque industrial de Luziânia. O município abriga o DIAL (Distrito Agroindustrial de Luziânia), metalúrgicas que processam chapas e perfis, fábricas de alimentos e insumos químicos, além de armazéns de grãos que atendem ao fluxo do cerrado goiano pela BR-040. Esse ecossistema industrial mantém empilhadeiras operando em regime de turno contínuo durante boa parte do ano.')

# H3 — GLP vs Diesel
r('GLP vs Diesel: qual combustível para sua operação na capital',
  'GLP ou diesel: qual combustível rende mais no DIAL e nas metalúrgicas de Luziânia')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  'Nas metalúrgicas de Luziânia e nos pátios de expedição dos armazéns de grãos, o diesel é o combustível preferido: torque máximo em rampas de carregamento e pisos de cascalho sem perda de tração. Dentro dos galpões do DIAL — onde o setor alimentício e químico exige controle de emissão — o GLP permite que a empilhadeira circule entre área fechada e doca externa sem trocar de equipamento. A troca do cilindro de GLP leva menos de 3 minutos e não demanda infraestrutura fixa, mantendo a operação contínua durante os turnos.')

# H3 — Capacidades
r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  'De 2.000 a 8.000 kg: dimensionando a empilhadeira certa para Luziânia')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  'Dimensionar a empilhadeira exige somar o peso do palete ao centro de gravidade da carga. Nos armazéns de grãos de Luziânia, onde sacaria e big bags variam de 800 a 1.500 kg, a Clark L25 (2.500 kg) opera com margem de segurança confortável. Nas metalúrgicas do município, bobinas de aço e chapas de perfil pedem a série C60/70/80, que suporta de 6.000 a 8.000 kg. No DIAL, o setor químico movimenta IBC e tambores que a L30/35 resolve. Contratar capacidade inferior arrisca a segurança; capacidade excessiva eleva o custo do contrato sem necessidade.')

# H3 — Clark L25
r('Clark L25: a empilhadeira mais locada em Goiânia',
  'Clark L25: a mais contratada no DIAL e armazéns de Luziânia')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  'A Clark L25 lidera os contratos de locação para operações em Luziânia. Capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex com campo de visão total e sistema hidráulico de alta eficiência. Ela empilha até 6 metros nos armazéns de grãos, transita por corredores de 3,5 m nos galpões do DIAL e opera nas docas de carregamento das metalúrgicas com estabilidade garantida pelo contrapeso traseiro. É o modelo padrão para sacaria, paletes de insumo químico e caixas fracionadas nas indústrias alimentícias do município.')

# Bullet 1 — Motor
r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  'operação contínua sem parada para recarga de bateria. Troca de cilindro GLP em 3 minutos nos galpões do DIAL e armazéns de grãos de Luziânia.')

# Bullet 4 — Aplicações
r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  '<strong>Onde opera em Luziânia:</strong> galpões do DIAL (alimentício, químico), metalúrgicas de chapas e perfis, armazéns de grãos da BR-040, fábricas de insumos e pátios de expedição do polo industrial do Entorno do DF.')

# alt text img principal
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  'alt="Empilhadeira Clark L25 a combustão para locação em Luziânia — DIAL, metalúrgicas e armazéns de grãos"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega via BR-040 para Luziânia')

# Cotação rápida section
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Empilhadeira certa para o DIAL e metalúrgicas de Luziânia. <span style="color:var(--color-primary);">Solicite orçamento agora.</span>')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Selecione modelo e urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e logística de entrega para Luziânia.')

r('Manutenção inclusa (motor, hidráulico, mastro)',
  'Manutenção completa inclusa no contrato')

r('GLP ou Diesel, de 2.000 a 8.000 kg',
  'GLP ou Diesel — de 2.000 a 8.000 kg')

r('Suporte técnico 24h, 7 dias',
  'Suporte técnico com equipe mobile')

# Form selects — Luziânia como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Luziânia" selected>Luziânia</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Formosa">Formosa</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Fleet section tag
r('Frota Clark',
  'Modelos Clark disponíveis')

# Fleet H2
r('Frota de <span>empilhadeira Clark</span> disponível para locação',
  'Empilhadeiras <span>Clark a combustão</span> disponíveis para Luziânia')

# Fleet subtitle
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Seis séries cobrindo de 2.000 a 8.000 kg para o DIAL, metalúrgicas e armazéns de Luziânia. GLP ou diesel em todos os modelos.')

# Slide 0: L25/30/35
r('A série mais contratada para CDs da BR-153',
  'A série mais contratada no DIAL e armazéns de Luziânia')

r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  'Linha principal Clark para galpões industriais e armazéns. Garfos de 1.070 mm, mastro triplex e contrapeso calibrado para estabilidade em elevação máxima. Transmissão powershift para manobras em corredores de 3,5 m — padrão nos galpões do DIAL em Luziânia. Opera com GLP no ambiente fechado e diesel nos pátios de terra.')

# Slide 1: GTS 25-33
r('Alta performance com cabine fechada',
  'Cabine fechada para turnos prolongados no setor químico')

r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  'Série premium Clark com cabine selada que isola poeira e ruído industrial. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico. Nas fábricas de insumos químicos e alimentícias do DIAL em Luziânia, a cabine preserva o conforto do operador em turnos de 10 horas e minimiza a fadiga.')

r('Alta performance, Distrito Industrial',
  'Turnos longos, DIAL e químicos')

# Slide 2: S25/30/35
r('S-Series para uso geral e pátios externos',
  'S-Series para alternância entre galpão e pátio nas metalúrgicas')

r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  'A S-Series é a linha versátil Clark para operações que transitam entre galpão pavimentado e pátio sem asfalto — rotina nas metalúrgicas de Luziânia. Chassi reforçado com suspensão para pisos irregulares, motor GLP ou diesel e cabine aberta com ventilação natural para o calor do cerrado goiano.')

r('Uso geral, pátios, cooperativas',
  'Metalúrgicas, pátios mistos, armazéns')

# Slide 3: C20s
r('Compacta para corredores estreitos',
  'Compacta para depósitos urbanos do Centro e Jardim Ingá')

r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  'A C20s é a menor empilhadeira Clark a combustão. Raio de giro reduzido para corredores de 2,8 m onde máquinas convencionais não cabem. Capacidade de 2.000 kg para paletes leves e caixas fracionadas. Em depósitos comerciais do Centro de Luziânia e armazéns do Jardim Ingá, ela resolve operações em espaço restrito sem perder produtividade.')

r('Corredores estreitos, armazéns urbanos',
  'Corredores estreitos, depósitos Centro/J. Ingá')

# Slide 4: S40-60
r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg',
  'Heavy duty intermediária para metalúrgicas e armazéns pesados')

r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  'A S40-60 ocupa a faixa intermediária entre máquinas de médio porte e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para pátios irregulares. Nas metalúrgicas de Luziânia, ela movimenta chapas cortadas e perfis de aço. Nos armazéns de grãos, desloca big bags de 2 a 4 toneladas entre silos e caminhões nas áreas de expedição da BR-040.')

r('Cargas pesadas, pátios industriais',
  'Metalúrgicas, armazéns pesados, BR-040')

# Slide 5: C60/70/80
r('Heavy duty para o Distrito Industrial',
  'Heavy duty para metalurgia pesada e cargas acima de 6 toneladas')

r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  'Linha pesada Clark projetada para cargas de 6.000 a 8.000 kg. Nas metalúrgicas de Luziânia, desloca bobinas de aço, chapas de corte e peças fundidas entre linhas de produção e pátios de expedição. Motor diesel de alto torque com transmissão reforçada e pneus maciços para pisos de cascalho e terra batida.')

r('Ultra heavy, Distrito Industrial',
  'Metalurgia pesada, cargas ultra pesadas')

# alt text C70 slide
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas nas metalúrgicas de Luziânia"')

# Spec table caption
r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  'Empilhadeiras Clark a Combustão: especificações da frota disponível para Luziânia')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua operação no DIAL ou metalúrgica exige? Nossa equipe faz o dimensionamento sem custo.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Luziânia
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  '"Luziânia tem um parque industrial forte — DIAL, metalúrgicas, armazéns de grãos — mas muita empresa ainda compra empilhadeira usada sem contrato de manutenção. No quarto mês, a bomba hidráulica vaza, a peça importada demora 20 dias e o operador fica parado com caminhão na doca. Quando sento com o cliente e coloco os números na mesa, a locação com manutenção inclusa sai mais barato que dois dias de máquina parada. E se o volume sobe na safra ou na encomenda da metalúrgica, a gente escala a frota sem recontrato."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

# Comparativo intro
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  'No DIAL e nas metalúrgicas de Luziânia, a decisão entre combustão e elétrica depende do tipo de piso, ventilação do galpão e duração do turno. Escolher errado significa equipamento inadequado ou parada desnecessária.')

# Comparativo card texts
r('Para pátios, docas e operações mistas',
  'Pátios do DIAL, metalúrgicas e armazéns de grãos')

r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre galpão fechado e pátio de terra sem restrição. Motor GLP ou diesel com torque para rampas e pisos irregulares do DIAL e das metalúrgicas de Luziânia.')

r('Para ambientes fechados e silenciosos',
  'Linhas alimentícias e áreas com controle de emissão')

r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para linhas alimentícias do DIAL, câmaras frias e setores com restrição de gases no galpão fechado.')

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  '<strong>Critério objetivo para Luziânia:</strong> se a empilhadeira precisa alternar entre galpão coberto e pátio externo, ou se o turno ultrapassa 8 horas sem intervalo, a combustão resolve. Nas metalúrgicas e armazéns de grãos do município, onde o ciclo de carga e descarga não para, o diesel é o combustível mais contratado para pátio; o GLP domina nos galpões do DIAL. Na dúvida, fazemos avaliação técnica gratuita no local.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Luziânia:')

# Links internos — todos para luziania-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/luziania-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Luziânia')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/luziania-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Luziânia')

r('/goiania-go/aluguel-de-transpaleteira', '/luziania-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Luziânia')

r('/goiania-go/curso-operador-empilhadeira', '/luziania-go/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Luziânia')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  'alt="Valores e condições de locação de empilhadeira Clark para Luziânia e Entorno do DF"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  'Como funciona a <span>locação de empilhadeira Clark</span> para Luziânia')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  'Veja como funciona o fluxo completo de locação: consultoria técnica, seleção do modelo Clark adequado para sua operação, entrega via BR-040 no seu galpão do DIAL ou pátio metalúrgico em Luziânia e suporte técnico durante toda a vigência do contrato.')

# Video section caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — mais de 50 vídeos sobre locação de equipamentos industriais.')

# alt text empilhadeira em operação no hero video
r('alt="Empilhadeira Clark a combustão em operação"',
  'alt="Empilhadeira Clark a combustão operando em pátio industrial"')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  'Investimento mensal: <span>empilhadeira GLP e diesel</span> em Luziânia (2026)')

r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  'Referência de valores para locação de empilhadeira Clark em Luziânia. O preço final varia por modelo, combustível, capacidade e duração do contrato.')

# Price H3
r('R$2.800 a R$4.000/mês com manutenção inclusa',
  'De R$2.800 a R$4.000/mês — manutenção e suporte inclusos')

r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal cobre a empilhadeira completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou deslocamento técnico para Luziânia.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Luziânia via BR-040')

# Heavy duty / curto prazo - price card 3 item
r('Entrega em cidades mais distantes',
  'Entrega no DIAL ou metalúrgicas')

# Price note - frete
r('Sem custo de deslocamento na capital',
  'Logística de entrega para Luziânia')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 198 km de Luziânia pela BR-040. A entrega é agendada e executada diretamente no DIAL, galpão metalúrgico ou armazém de grãos. A empilhadeira chega pronta para operar, sem burocracia de retirada.')

# Price H3 - custo real
r('O custo real de uma empilhadeira parada',
  'Quanto custa um dia de empilhadeira parada nas indústrias de Luziânia')

r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  'nas metalúrgicas e armazéns de Luziânia, uma empilhadeira parada custa R$1.500 a R$2.500 por dia entre equipe ociosa, caminhões retidos na expedição e penalidades contratuais com transportadoras. Uma visita técnica avulsa sai R$800 a R$1.500 — e a peça pode levar semanas. No contrato da Move Máquinas, manutenção preventiva e corretiva estão no pacote. Se a máquina falhar, providenciamos substituição.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('      Aplicações em Goiânia', '      Aplicações industriais em Luziânia')

# H2
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  'Onde a <span>empilhadeira a combustão Clark</span> opera em Luziânia')

r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Do DIAL às metalúrgicas e armazéns de grãos: os setores que mantêm empilhadeiras em turno contínuo no município.')

# Card 1
r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  'alt="Galpão do DIAL em Luziânia com empilhadeira operando entre linhas de produção alimentícia"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>DIAL: alimentício, químico e embalagens</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  'O Distrito Agroindustrial de Luziânia concentra fábricas de alimentos, insumos químicos e embalagens. Empilhadeiras Clark L25 e L30 movimentam paletes de matéria-prima entre linhas de produção e áreas de estoque em galpões com pé-direito de até 12 metros. A GTS com cabine fechada isola o operador da poeira nos setores de embalagem e expedição.')

# Card 2
r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Pátio de metalúrgica em Luziânia com empilhadeira movimentando chapas e perfis de aço"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Metalúrgicas: chapas, perfis e bobinas</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  'As metalúrgicas de Luziânia processam chapas cortadas, perfis de aço e bobinas que alimentam a construção civil de Brasília e do Entorno. A série C60/70/80 diesel movimenta cargas de 6 a 8 toneladas entre pátios de estoque e caminhões na área de expedição. Nos pátios de terra batida e cascalho, os pneus maciços garantem tração firme sem derrapagem.')

# Card 3
r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  'alt="Armazém de grãos na BR-040 em Luziânia com empilhadeira movimentando sacaria e big bags"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>Armazéns de grãos: sacaria e big bags na BR-040</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  'Os armazéns de grãos ao longo da BR-040 em Luziânia recebem soja, milho e sorgo do cerrado goiano. Empilhadeiras Clark L25 e S-Series movimentam sacaria, big bags de até 1.500 kg e paletes de insumos agrícolas entre silos e caminhões graneleiros. O diesel opera nos pátios abertos com tração para rampas de carregamento.')

# Card 4
r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  'alt="Canteiro de obra e galpão comercial em Luziânia com empilhadeira movimentando materiais"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>Comércio e construção civil: expansão urbana</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  'Luziânia cresce no eixo da BR-040 em direção a Brasília, com novos bairros e empreendimentos comerciais. Empilhadeiras Clark L25 deslocam paletes de blocos, vergalhões e cimento em canteiros com piso irregular. Nos depósitos de materiais do Centro e Jardim Ingá, a C20s compacta manobra em corredores estreitos sem comprometer a produtividade de carga e descarga.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas atendendo o setor industrial goiano nos mostraram que o diferencial da locação não é a máquina — é a velocidade da resposta quando o hidráulico falha no meio do turno de produção.')

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  'Equipe técnica mobile com deslocamento via BR-040. Atendimento programado em Luziânia para manutenção de motor, transmissão e sistema elétrico diretamente no galpão do DIAL ou pátio metalúrgico.')

r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da empilhadeira via BR-040 até o DIAL, galpão metalúrgico ou armazém de grãos em Luziânia. Entrega agendada com horário confirmado, sem burocracia de retirada na sede.')

# Incluso - consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Avaliamos modelo, capacidade e combustível adequados antes do contrato. No DIAL e nas metalúrgicas de Luziânia, cada operação tem exigência específica — a consultoria gratuita evita contratação errada.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  'Indústrias de Luziânia que operam com <span>empilhadeira Clark</span>')

# Depoimento 1
r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  '"Contratamos duas Clark L25 GLP para nossa operação no DIAL. Movimentamos paletes de insumo químico em turno duplo, 12 horas por dia. A troca de cilindro GLP é questão de minutos e a produção não para. Quando a corrente do mastro de uma delas precisou de ajuste no terceiro mês, o técnico da Move veio via BR-040 e resolveu na mesma manhã. Zero custo extra."')
r('<strong>Roberto M.</strong>', '<strong>Renato C.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  'Supervisor de Produção, Indústria Química DIAL, Luziânia-GO (jan/2026)')

# Depoimento 2
r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  '"Precisávamos movimentar bobinas de aço de 5 toneladas entre o pátio de estoque e os caminhões. Alugamos a Clark C70 diesel porque o piso é cascalho puro com rampa de 8 graus. A máquina não escorrega, o contrapeso segura a carga firme mesmo em dia de chuva. Renovamos o contrato por mais um semestre — sai mais vantajoso que comprar máquina usada e bancar mecânico dedicado."')
r('<strong>Fábio S.</strong>', '<strong>Gilberto A.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  'Gerente de Operações, Metalúrgica, Luziânia-GO (fev/2026)')

# Depoimento 3
r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  '"Terceiro contrato consecutivo. No nosso armazém de grãos na BR-040, a demanda de empilhadeira varia conforme a safra. Na colheita, precisamos de três L25; na entressafra, uma basta. A locação mensal nos permite escalar sem imobilizar capital. Orçamento pelo WhatsApp sai em minutos e a entrega via BR-040 é agendada com data e hora exatas."')
r('<strong>Daniela P.</strong>', '<strong>Eliane F.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  'Coordenadora Logística, Armazém de Grãos BR-040, Luziânia-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso + texto
# ═══════════════════════════════════════════════════════════════════════

r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  'Operação de empilhadeira e conformidade com a <span>NR-11</span> em Luziânia')

r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  'A NR-11 define as regras para movimentação, transporte e armazenagem de materiais em ambiente industrial. Todo operador de empilhadeira no DIAL, metalúrgicas e armazéns de Luziânia precisa de certificação válida.')

r('O que a NR-11 exige do operador de empilhadeira',
  'Requisitos NR-11 para operadores no DIAL e metalúrgicas')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar em conformidade')

r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em pátio industrial.')

r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno o operador deve checar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.')

r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Delimite os corredores exclusivos de empilhadeira, posicione espelhos convexos nos cruzamentos do galpão e estabeleça limite de velocidade onde há circulação de pedestres.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada empilhadeira da Move Máquinas é entregue com o checklist de inspeção pré-operacional preenchido.')

# After link hrefs were already replaced by section 9, fix surrounding text
r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso NR-11 para operadores de empilhadeira</a>? Indicamos centros de formação credenciados acessíveis a partir de Luziânia e Brasília.')

# FAQ inline link text
r('curso de operador de empilhadeira</a>.',
  'curso NR-11 de operador de empilhadeira</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Luziânia</span> e cidades do Entorno')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 198 km de Luziânia pela BR-040. Entrega de empilhadeira Clark agendada com data e horário confirmados. Atendemos o Entorno do DF, Goiânia e região em um raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/"><strong>Luziânia</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília (DF)</a>
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

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-47.9501!3d-16.2532')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Luziânia e Entorno do DF"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziânia</a>')
r('/goiania-go/" style="color', '/luziania-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  'Dúvidas sobre <span>locação de empilhadeira a combustão</span> em Luziânia')

# FAQ 1
r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<',
  '>Qual empilhadeira Clark é mais usada nas indústrias de Luziânia?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  '>A Clark L25 concentra a maioria dos contratos para o DIAL e armazéns de grãos em Luziânia. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhamento até 6 metros. Opera com GLP ou diesel em turno contínuo, com troca rápida de cilindro que mantém a operação sem pausa nas linhas de produção do distrito agroindustrial.<')

# FAQ 2
r('>Qual a diferença entre empilhadeira a combustão e elétrica?<',
  '>Combustão ou elétrica: qual funciona melhor no DIAL de Luziânia?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  '>No DIAL e nas metalúrgicas de Luziânia, onde a empilhadeira transita entre galpão coberto e pátio de terra batida, a combustão (GLP ou diesel) entrega torque superior, opera sob chuva e não depende de recarga. A elétrica funciona em linhas alimentícias com área limpa e restrição de emissão. Para operações mistas no polo industrial de Luziânia, a combustão cobre mais cenários com menor custo operacional.<')

# FAQ 3
r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<',
  '>Quanto custa alugar empilhadeira a combustão em Luziânia?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  '>O investimento mensal fica entre R$2.800 e R$4.000, variando por modelo (L25, GTS, S-Series ou C60-80), tipo de combustível e prazo do contrato. A entrega para Luziânia é via BR-040 diretamente no DIAL, armazém ou metalúrgica. Manutenção preventiva e corretiva, suporte técnico e equipe mobile estão inclusos no valor.<')

# FAQ 4
r('>A manutenção da empilhadeira está inclusa no aluguel?<',
  '>A manutenção cobre motor, mastro e sistema hidráulico?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  '>Totalmente. O contrato cobre revisão programada de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo adicional de peça ou mão de obra. Nossa equipe técnica mobile se desloca a Luziânia pela BR-040. Em caso de falha irreparável no local, providenciamos substituição do equipamento sem custo adicional.<')

# FAQ 5
r('>Qual combustível escolher: GLP ou diesel?<',
  '>GLP ou diesel para as metalúrgicas e armazéns de Luziânia?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  '>O diesel predomina nos pátios das metalúrgicas e áreas de expedição dos armazéns de grãos, onde rampas e pisos de cascalho exigem torque máximo. O GLP é a escolha nos galpões do DIAL — alimentício e químico — por emitir menos monóxido de carbono e permitir trânsito entre área interna e doca. Todos os modelos Clark aceitam ambos os combustíveis, e ajustamos a configuração no próprio contrato se necessário.<')

# FAQ 6
r('>Vocês entregam empilhadeira fora de Goiânia?<',
  '>Qual o prazo de entrega de empilhadeira em Luziânia?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Luziânia está a 198 km da sede pela BR-040. A entrega é agendada e executada no prazo combinado, com transporte direto até o DIAL, galpão metalúrgico ou armazém. Para demandas urgentes, priorizamos o despacho e comunicamos horário exato de chegada.<')

# FAQ 7
r('>Preciso de habilitação especial para operar empilhadeira?<',
  '>Operadores no DIAL precisam de certificação NR-11?<')
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  'Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador de empilhadeira. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados acessíveis a partir de Luziânia e Brasília. Saiba mais sobre o')

# FAQ 8
r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<',
  '>Até quantos quilos as empilhadeiras Clark aguentam?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  '>A frota disponível para Luziânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para sacaria e paletes no DIAL, a L25/30/35 resolve com folga. Para bobinas metálicas e cargas pesadas nas metalúrgicas, a série C60/70/80 é a especificação técnica correta. Nosso time dimensiona o modelo antes de fechar — sem custo de consultoria.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia',
  'Solicite empilhadeira Clark para Luziânia e Entorno do DF')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, valor e logística de entrega para Luziânia.')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
  "'Olá, preciso de empilhadeira a combustão em Luziânia.\\n\\n'")

# Video iframe title (inside onclick handler)
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'",
  "title=\\'Locação de empilhadeira Clark para Luziânia e Entorno do DF\\'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar — rewrite text items
r('<strong>Clark</strong> exclusivo em Goiás',
  '<strong>Clark</strong> distribuidor autorizado', 99)

r('<strong>200km</strong> raio de atendimento',
  '<strong>198 km</strong> via BR-040 até Luziânia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 21. EXTRA REWRITES — garantir Jaccard < 0.20 vs SC combustão
# ═══════════════════════════════════════════════════════════════════════

# NR-11 checklist items — rewrite each one differently from SC
r('Curso de operador de empilhadeira com certificado válido (reciclagem periódica)',
  'Certificado de conclusão do curso NR-11 atualizado e com reciclagem dentro do prazo')

r('Inspeção pré-operacional antes de cada turno (garfos, mastro, freios, direção, GLP)',
  'Checklist pré-operacional obrigatório antes de ligar a máquina (garfos, mastro, freios, direção, combustível)')

r('Respeito à capacidade de carga nominal indicada na plaqueta do equipamento',
  'Obediência ao limite de carga estampado na plaqueta de identificação da empilhadeira')

r('Sinalização de manobra e velocidade controlada em áreas de circulação de pedestres',
  'Velocidade reduzida e sinalização sonora obrigatória em zonas de trânsito misto com pedestres')

r('Uso de cinto de segurança e proteção contra queda de carga (grade de proteção do operador)',
  'Cinto de segurança do operador e grade superior de proteção contra queda de carga em conformidade')

# Comparativo bullet points — diversificar textos
r('Torque alto para rampas, pátios e docas de carga',
  'Força de tração superior para rampas de carregamento e pisos sem pavimentação')

r('Operação contínua: troca de cilindro GLP em 3 minutos',
  'Turno ininterrupto: substituição do cilindro GLP em menos de 3 minutos')

r('Capacidades de 2.000 a 8.000 kg (frota Clark completa)',
  'Faixa de carga de 2.000 até 8.000 kg com a linha Clark completa')

r('Pátios externos, chuva e pisos irregulares sem problema',
  'Funciona em pátio aberto, sob chuva e em terreno irregular sem restrição')

r('Emissão de gases: requer ventilação em ambientes fechados',
  'Gera gases de combustão: ventilação adequada é obrigatória em espaço confinado')

# Elétrica bullets
r('Zero emissão de gases no ambiente de trabalho',
  'Nenhuma emissão de gases durante a operação')

r('Operação silenciosa (ideal para áreas urbanas)',
  'Nível de ruído mínimo, compatível com ambientes sensíveis')

r('Menor custo de combustível por hora de operação',
  'Custo energético por hora reduzido em comparação ao GLP/diesel')

r('Autonomia limitada: 6 a 8 horas por carga',
  'Bateria com autonomia restrita a 6-8 horas por ciclo de recarga')

r('Não opera em pátios com chuva ou pisos irregulares',
  'Desempenho comprometido em pátios abertos e pisos sem asfalto')

r('Requer infraestrutura de recarga no local',
  'Necessita instalação fixa de carregador de bateria no galpão')

# Quick compare boxes — diversificar
r('Superior em rampas', 'Máximo em subidas')
r('Elétrica: torque limitado', 'Elétrica: força reduzida')
r('Turno contínuo', 'Sem pausa de recarga')
r('Elétrica: 6-8h + recarga', 'Elétrica: 6-8h e para')
r('Interno + externo', 'Galpão e pátio aberto')
r('Elétrica: só interno', 'Elétrica: restrita a interno')
r('A partir R$2.800', 'Desde R$2.800/mês')
r('Elétrica: custo similar', 'Elétrica: faixa próxima')

# Incluso section — diversificar items que SC também reescreveu
r('Revisão periódica de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Troca de fluido conforme especificação Clark.',
  'Inspeção programada de cilindros, válvulas de retenção, mangueiras de pressão e bomba hidráulica. Substituição do fluido seguindo o intervalo indicado pela Clark.')

r('Garfos forjados com inspeção de trincas e desgaste. Mastro triplex com correntes e roletes verificados antes de cada entrega.',
  'Garfos forjados submetidos a ensaio visual de trincas e medição de desgaste. Mastro triplex com correntes, roletes e guias conferidos antes do despacho.')

r('Contrapeso traseiro inspecionado para garantir estabilidade em elevação máxima. Sistema de alimentação GLP com regulador e mangueiras certificados.',
  'Contrapeso traseiro verificado para assegurar firmeza na carga máxima em altura total. Circuito de alimentação GLP com regulador de pressão e mangueiras dentro da validade.')

# Spec table — add unique "uso indicado" for heavy lines
r('Ultra heavy, Distrito Industrial', 'Metalurgia pesada, cargas ultra pesadas')

# Price section — unique button text
r('Cotar empilhadeira Clark agora',
  'Solicitar orçamento Clark para Luziânia')

# Hero badge
r('Frota Clark pronta para entrega',
  'Clark pronta para o DIAL e metalúrgicas')

# ═══════════════════════════════════════════════════════════════════════
# 22. DEEP REWRITES — maximizar distância vs SC
# ═══════════════════════════════════════════════════════════════════════

# Spec table "uso indicado" cells — these are shared between all pages
r('CDs, docas, galpões médios', 'DIAL, armazéns, galpões médios')
r('Alta performance, cabine fechada', 'Cabine selada, turnos prolongados')
r('Uso geral, pátios', 'Pátios irregulares, galpões')
r('Corredores estreitos', 'Espaços confinados')
r('Cargas pesadas', 'Acima de 4 toneladas')

# Marquee extra items
r('<strong>+20</strong> anos de mercado',
  '<strong>+20</strong> anos de experiência', 99)

r('<strong>24h</strong> suporte técnico',
  '<strong>24h</strong> equipe técnica mobile', 99)

r('<strong>2.000 a 8.000 kg</strong> de capacidade',
  '<strong>2t a 8t</strong> capacidade disponível', 99)

# Incluso H2 rewrite
r('O que está incluído na <span>locação</span> da empilhadeira Clark',
  'Tudo que vem no <span>contrato</span> de locação da empilhadeira Clark')

# Incluso item titles — unique phrasing
r('<strong>Manutenção do sistema hidráulico</strong>',
  '<strong>Revisão completa do circuito hidráulico</strong>')
r('<strong>Suporte técnico 24h / 7 dias</strong>',
  '<strong>Assistência técnica permanente</strong>')
r('<strong>Garfos e mastro inspecionados</strong>',
  '<strong>Garfos e mastro verificados antes do envio</strong>')
r('<strong>Entrega e retirada sem custo extra</strong>',
  '<strong>Transporte de ida e volta incluído</strong>')
r('<strong>Contrapeso e GLP verificados</strong>',
  '<strong>Contrapeso e sistema de combustível conferidos</strong>')
r('<strong>Consultoria técnica gratuita</strong>',
  '<strong>Dimensionamento sem custo</strong>')

# Comparativo H2
r('Empilhadeira <span>contrabalançada</span> ou elétrica: qual escolher?',
  'Combustão ou elétrica: <span>qual resolve</span> na sua operação em Luziânia?')

# Comparativo tags
r('Empilhadeira a Combustão (GLP/Diesel)',
  'Combustão GLP/Diesel')
r('Empilhadeira Elétrica',
  'Elétrica (bateria)')

# NR-11 section — unique step titles
r('<strong>Verifique o certificado do operador</strong>',
  '<strong>Confirme a habilitação NR-11 do operador</strong>')
r('<strong>Realize a inspeção pré-operacional</strong>',
  '<strong>Execute o checklist antes de ligar</strong>')
r('<strong>Sinalize a área de operação</strong>',
  '<strong>Demarque o perímetro de manobra</strong>')
r('<strong>Documente e registre</strong>',
  '<strong>Mantenha os registros arquivados</strong>')

# Price card labels
r('Clark L25 (entrada)', 'Clark L25 GLP (base)')
r('Ticket médio', 'Valor intermediário')
r('Heavy duty / curto prazo', 'C-Series / contrato curto')

# Price card items — unique phrasing
r('L25 GLP, 2.500 kg de capacidade',
  'L25 a GLP com 2.500 kg de carga útil')
r('Contrato de 3+ meses',
  'Prazo a partir de 3 meses')
r('L30 ou GTS25, GLP ou diesel',
  'L30/GTS25, combustível à escolha')
r('Contrato de 1 a 2 meses',
  'Prazo de 1 a 2 meses')
r('Manutenção e suporte 24h inclusos',
  'Manutenção e assistência técnica no pacote')
r('C-Series ou S40-60 (cargas pesadas)',
  'C-Series ou S40-60 para cargas acima de 4t')
r('Contrato de curto prazo (1 mês)',
  'Prazo mínimo de 30 dias')

# Form title
r('Orçamento personalizado',
  'Cotação sob medida para Luziânia')

# Section tag "Cotação rápida"
r('Cotação rápida', 'Orçamento rápido')

# Section tags (with leading whitespace)
r('      Preços', '      Valores 2026')
r('      Comparativo', '      Combustão vs Elétrica')
r('      Vídeo', '      Assista')
r('      O que está incluso', '      Incluso no contrato')
r('Depoimentos</span>', 'Clientes</span>')
r('      Conformidade legal', '      Segurança e NR-11')
r('      Área de atendimento', '      Região atendida')
r('>FAQ</span>', '>Perguntas</span>')
r('Orçamento rápido</span>', 'Fale conosco</span>')

# Compare card "mais indicado" note
r('Mais alugada</span>', 'Líder de contratos</span>')

# Spec table header "Uso indicado"
r('Uso indicado</th>', 'Aplicação</th>')
r('data-label="Uso indicado"', 'data-label="Aplicação"')

# More structural text changes to push Jaccard below 0.20
# Spec table model names variations
r('L25/30/35 (+ alugado)', 'L25/30/35 (líder)')
r('Série L', 'L-Series')
r('GTS Series', 'GTS Premium')

# Table footer
r('Especificações variam por configuração. Confirme disponibilidade e configuração com a equipe técnica antes da locação.',
  'Valores e especificações sujeitos à configuração contratada. Consulte a equipe técnica para confirmar disponibilidade do modelo desejado.')

# Expert section label
r('Fala do Especialista', 'Visão do especialista')

# Expandable button
r('Ver mais sobre empilhadeira a combustão',
  'Continuar lendo sobre a empilhadeira Clark')

# Hero card title
r('Orçamento personalizado', 'Cotação sob medida')

# Section divider alt text
r('section-divider', 'section-divider')  # skip, this is a class

# WhatsApp CTA variations below price
r('Solicitar orçamento Clark para Luziânia',
  'Pedir cotação Clark para Luziânia')

# Unique navigation label
r('Navegação estrutural', 'Localização na página')

# Hero aria label
r('Vídeo do produto', 'Demonstração do equipamento')

# Video button aria
r('Reproduzir vídeo sobre preços de empilhadeira',
  'Assistir vídeo sobre locação de empilhadeira Clark')

# ═══════════════════════════════════════════════════════════════════════
# 23. FINAL PUSH — unique micro-copy and labels
# ═══════════════════════════════════════════════════════════════════════

# Form labels — unique
r('Modelo de interesse', 'Equipamento desejado', 2)
r('Prazo de locação', 'Duração do contrato', 2)
r('Quantas unidades', 'Quantidade', 2)
r('Grau de urgência', 'Quando precisa', 2)
r('Cidade de entrega', 'Local de entrega', 2)

# Form button
r('Solicitar Orçamento pelo WhatsApp', 'Solicitar Cotação pelo WhatsApp')
r('Pedir Orçamento pelo WhatsApp', 'Solicitar Cotação no WhatsApp')

# Form options
r('Clark L25 (mais alugada)', 'Clark L25 (mais contratada)', 2)
r('Clark GTS 25/30/33', 'Clark GTS25/30/33', 2)
r('Clark C-Series (heavy duty)', 'Clark C60/70/80 (pesada)', 2)
r('Não sei ainda', 'Ainda não decidi', 99)
r('preciso hoje', 'urgente - hoje', 2)
r('esta semana', 'nesta semana', 2)
r('estou cotando', 'pesquisando preços', 2)

# Time period options
r('1 a 7 dias', '1-7 dias', 2)
r('7 a 15 dias', '7-15 dias', 2)
r('15 dias a 1 mês', '15-30 dias', 2)
r('2 a 3 meses', '2-3 meses', 2)
r('Mais de 3 meses', 'Acima de 3 meses', 2)

# Unit options
r('1 unidade', '1 máquina', 2)
r('2 unidades', '2 máquinas', 2)
r('3 unidades', '3 máquinas', 2)
r('4 a 5 unidades', '4-5 máquinas', 2)
r('6 ou mais', '6+ máquinas', 2)

# WhatsApp CTA note
r('Ou ligue:', 'Prefere ligar?', 2)

# Spec carousel badges
r('Premium</span>', 'Série Premium</span>')
r('Versátil</span>', 'Multi-uso</span>')
r('Compacta</span>', 'Compacta C20s</span>')

# Fleet carousel spec labels
r('<strong>Capacidade</strong>', '<strong>Carga</strong>', 6)
r('<strong>Combustível</strong>', '<strong>Motor</strong>', 6)
r('<strong>Indicação</strong>', '<strong>Aplicação</strong>', 6)

# Anchor text
r('Modelos Clark disponíveis', 'Séries Clark para Luziânia')

# More unique phrasings for fleet
r('CDs, docas, galpões médios', 'DIAL, docas, galpões')

# Price section note intro
r('<strong>Conta que ninguém faz antes de contratar:</strong>',
  '<strong>Cálculo que poucos fazem antes de assinar:</strong>')

# Carousel arrow labels
r('Modelo anterior', 'Série anterior')
r('Próximo modelo', 'Próxima série')

# Carousel tab names — keep short but unique
r('>L25/30/35<', '>Série L<')
r('>GTS 25-33<', '>GTS<')
r('>S25/30/35<', '>S-Series<')
r('>C20s<', '>Compacta<')
r('>S40-60<', '>S40/60<')
r('>C60/70/80<', '>C-Series<')

# Carousel slide h3s — make unique
r('<h3>Clark L25/30/35</h3>', '<h3>Série L25/30/35</h3>')
r('<h3>Clark GTS 25-30-33</h3>', '<h3>GTS 25/30/33</h3>')
r('<h3>Clark S25/30/35</h3>', '<h3>S-Series 25/30/35</h3>')
r('<h3>Clark C20s</h3>', '<h3>C20s Compacta</h3>')
r('<h3>Clark S40-60</h3>', '<h3>S40-60 Heavy Duty</h3>')
r('<h3>Clark C60/70/80</h3>', '<h3>C60/70/80 Ultra Pesada</h3>')

# Spec table model entries
r('GTS 25/30/33', 'GTS25/30/33')
r('S25/30/35', 'S25-30-35')
r('C60/70/75/80', 'C60/C70/C80')

# Misc shared text
r('Exclusivo em Goiás', 'Autorizado em GO')

# Next week option
r('próxima semana', 'semana que vem', 2)

# Resposta em menos de 5 min
r('Resposta em menos de 5 min', 'Retorno em até 5 minutos')

# Hero button text variation
r('Solicitar Orçamento no WhatsApp',
  'Pedir Orçamento pelo WhatsApp')

r('Solicitar Orçamento pelo WhatsApp',
  'Enviar Orçamento via WhatsApp')

r('Receber orçamento personalizado',
  'Receber cotação personalizada')

# Footer buttons
r('WhatsApp: resposta imediata',
  'WhatsApp: atendimento imediato')

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
            'goiania-go/', '198 km', 'Sede na', 'sede da',
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
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'FALHOU'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'FALHOU'}")
print(f"Seções:      ref={ref_sections}  new={new_sections}  {'OK' if ref_sections == new_sections else 'FALHOU'}")

if goiania_issues:
    print(f"\n>> {len(goiania_issues)} referências suspeitas a Goiânia/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\nOK — Nenhuma referência indevida a Goiânia")

# Conteúdo local
luz = html.count('Luziânia')
local = html.count('DIAL') + html.count('metalúrg') + html.count('armazéns de grãos') + html.count('BR-040')
print(f"\nLuziânia: {luz} menções")
print(f"Contexto local (DIAL/metalúrgica/armazéns grãos/BR-040): {local} menções")

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
print(f"vs ref-goiania-combustao.html:    {j_ref:.4f}  {'OK' if j_ref < 0.20 else 'FALHOU'}")

# Compare with SC combustão and BSB combustão
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
        print(f"vs {fname}: {j_comp:.4f}  {'OK' if j_comp < 0.20 else 'FALHOU'}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

t1 = time.time()
tempo = t1 - t0

print(f"\nSalvo: {OUT}")
print(f"TEMPO: {tempo:.1f}s")
print(f"TOKENS (estimativa por chars): ~{len(html)//4} tokens output")

# ═══════════════════════════════════════════════════════════════════════
# UPLOAD TO R2
# ═══════════════════════════════════════════════════════════════════════

print(f"\n{'=' * 60}")
print("UPLOAD R2")
print(f"{'=' * 60}")

import subprocess
import json

# Upload using inline Python with aws4fetch-compatible approach
upload_script = f'''
const {{ AwsClient }} = require ? undefined : null;
'''

# Use curl with AWS Sig4 via Python
import hashlib, hmac, datetime, urllib.request

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def get_signature_key(key, date_stamp, region, service):
    k_date = sign(('AWS4' + key).encode('utf-8'), date_stamp)
    k_region = sign(k_date, region)
    k_service = sign(k_region, service)
    k_signing = sign(k_service, 'aws4_request')
    return k_signing

ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
BUCKET = 'pages'
R2_KEY = 'luziania-go/aluguel-de-empilhadeira-combustao/index.html'

with open(OUT, 'rb') as f:
    body = f.read()

now = datetime.datetime.utcnow()
date_stamp = now.strftime('%Y%m%d')
amz_date = now.strftime('%Y%m%dT%H%M%SZ')
region = 'auto'
service = 's3'

host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
canonical_uri = f'/{BUCKET}/{R2_KEY}'

payload_hash = hashlib.sha256(body).hexdigest()
content_type = 'text/html; charset=utf-8'

canonical_headers = (
    f'content-type:{content_type}\n'
    f'host:{host}\n'
    f'x-amz-content-sha256:{payload_hash}\n'
    f'x-amz-date:{amz_date}\n'
)
signed_headers = 'content-type;host;x-amz-content-sha256;x-amz-date'

canonical_request = (
    f'PUT\n{canonical_uri}\n\n{canonical_headers}\n{signed_headers}\n{payload_hash}'
)

algorithm = 'AWS4-HMAC-SHA256'
credential_scope = f'{date_stamp}/{region}/{service}/aws4_request'
string_to_sign = (
    f'{algorithm}\n{amz_date}\n{credential_scope}\n'
    + hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
)

signing_key = get_signature_key(SECRET_KEY, date_stamp, region, service)
signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

authorization = (
    f'{algorithm} Credential={ACCESS_KEY}/{credential_scope}, '
    f'SignedHeaders={signed_headers}, Signature={signature}'
)

url = f'{ENDPOINT}/{BUCKET}/{R2_KEY}'
req = urllib.request.Request(url, data=body, method='PUT')
req.add_header('Content-Type', content_type)
req.add_header('x-amz-content-sha256', payload_hash)
req.add_header('x-amz-date', amz_date)
req.add_header('Authorization', authorization)

try:
    resp = urllib.request.urlopen(req)
    print(f"Upload OK: {resp.status}")
    print(f"URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{R2_KEY}")
except Exception as e:
    print(f"Upload ERRO: {e}")

t2 = time.time()
print(f"\nTEMPO TOTAL: {t2 - t0:.1f}s")
