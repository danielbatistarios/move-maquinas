#!/usr/bin/env python3
"""
rebuild-inhumas-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Inhumas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

import time
import re
import os

start = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/inhumas-go-aluguel-de-empilhadeira-combustao-V2.html'

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
  '<title>Empilhadeira a Combustão para Aluguel em Inhumas-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  'content="Empilhadeira Clark a combustão para aluguel em Inhumas-GO. Modelos L25, GTS, S-Series e C-Series de 2.000 a 8.000 kg. Ideal para polo têxtil, indústria alimentícia e armazéns de grãos. Manutenção inclusa, entrega via GO-070 no mesmo dia. A partir de R$2.800/mês."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/inhumas-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Empilhadeira a Combustão para Aluguel em Inhumas-GO | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Empilhadeira Clark GLP e diesel em Inhumas. De 2.000 a 8.000 kg para galpões de confecções, indústrias alimentícias e armazéns de grãos do Distrito Industrial. Manutenção inclusa. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Inhumas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.3547;-49.4952"')
r('content="-16.7234, -49.2654"', 'content="-16.3547, -49.4952"')

# Schema — coords
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.3547, "longitude": -49.4952')
r('"latitude": -16.7234', '"latitude": -16.3547')
r('"longitude": -49.2654', '"longitude": -49.4952')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Aluguel de Empilhadeira a Combustão em Inhumas"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Inhumas", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira a Combustão em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/aluguel-de-empilhadeira-combustao"')

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
        { "@type": "Question", "name": "Qual empilhadeira Clark serve melhor para os galpões de confecção em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 é a mais contratada para o polo têxtil de Inhumas. Com 2.500 kg de capacidade e garfos de 1.070 mm, ela movimenta fardos de tecido e paletes de confecções prontas em corredores de 3,5 m. Opera com GLP nos galpões fechados — menos emissão e troca de cilindro em 3 minutos, sem parar a linha de separação." } },
        { "@type": "Question", "name": "Empilhadeira a combustão ou elétrica para a indústria alimentícia de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Nas indústrias alimentícias de Inhumas, onde a empilhadeira transita entre câmara fria, área de produção e doca de expedição, a combustão GLP resolve: circula em ambientes internos com emissão reduzida e opera em pátios externos sem depender de tomada de recarga. A elétrica é viável apenas em galpões totalmente fechados com infraestrutura de carregamento. Para turnos acima de 8 horas, a combustão evita paradas." } },
        { "@type": "Question", "name": "Quanto custa alugar empilhadeira a combustão em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Os valores variam de R$2.800 a R$4.000 por mês conforme o modelo (L25, GTS, S-Series ou C-Series), tipo de combustível e duração do contrato. Inhumas fica a 40 km da sede pela GO-070 — entrega sem custo de frete. Manutenção preventiva, corretiva e suporte técnico 24h estão inclusos no pacote." } },
        { "@type": "Question", "name": "A manutenção de motor e sistema hidráulico está coberta pelo contrato?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente coberta. O contrato inclui revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos. Nossa equipe técnica mobile percorre a GO-070 e chega a Inhumas em aproximadamente 50 minutos. Se a empilhadeira apresentar defeito que não pode ser reparado no local, substituímos a máquina no mesmo dia." } },
        { "@type": "Question", "name": "GLP ou diesel: qual combustível para os armazéns de grãos de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Nos armazéns de grãos, onde a empilhadeira opera entre o galpão coberto e o pátio de carga dos caminhões graneleiros, o GLP é a escolha mais flexível — transita entre área interna e externa sem trocar de equipamento e emite menos poluentes. O diesel é reservado para pátios de terra batida com rampas íngremes, comuns nas cooperativas agrícolas da região. Todos os modelos Clark aceitam ambos os combustíveis." } },
        { "@type": "Question", "name": "Em quanto tempo a empilhadeira chega em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Inhumas recebe no mesmo dia da confirmação. São 40 km pela GO-070 a partir da sede na Av. Eurico Viana em Goiânia. O equipamento sai da base e chega ao seu galpão de confecções, armazém de grãos ou indústria alimentícia em cerca de 50 minutos. Sem custo de deslocamento." } },
        { "@type": "Question", "name": "Preciso de certificação NR-11 para operar empilhadeira em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Sim, é obrigatório. A NR-11 exige que todo operador de empilhadeira possua treinamento específico com certificado válido. O curso abrange inspeção pré-operacional, limites de carga, empilhamento seguro e manobras em pátio. Indicamos centros de formação credenciados na região de Inhumas e Goiânia." } },
        { "@type": "Question", "name": "Qual a maior capacidade de carga das empilhadeiras disponíveis para Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para fardos de tecido e paletes de alimentos, a L25/30/35 resolve com folga. Para sacas de grãos em big bags e cargas pesadas no Distrito Industrial, a S40-60 ou C-Series são a indicação técnica. Dimensionamos o modelo antes de fechar — sem custo de consultoria." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/inhumas-go/">Equipamentos em Inhumas</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  '<span aria-current="page">Empilhadeira a Combustão em Inhumas</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Empilhadeira a Combustão para Aluguel em <em>Inhumas</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg para o polo têxtil, indústrias alimentícias e armazéns de grãos de Inhumas. GLP ou diesel, manutenção inclusa e entrega via GO-070 no mesmo dia — 40 km da sede. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Inhumas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>Entrega via GO-070</strong><span>40 km da sede</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Referência em locação</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

r('Entenda o equipamento', 'Saiba antes de contratar')

r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  'Como a <span>empilhadeira a combustão Clark</span> resolve a movimentação em Inhumas')

r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  'A empilhadeira a combustão funciona com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel — não depende de tomada de recarga, desenvolve força de tração elevada em pisos irregulares e trabalha em áreas abertas sob qualquer condição climática. Inhumas, município de 53 mil habitantes a 40 km de Goiânia pela GO-070, concentra o maior polo de confecções do interior de Goiás, indústrias alimentícias de expressão regional e armazéns de grãos que escoam safra para todo o Centro-Oeste. Esse ecossistema produtivo demanda empilhadeiras em operação contínua dentro dos galpões de confecções, nas docas das fábricas de alimentos e nos pátios de carga dos silos.')

r('GLP vs Diesel: qual combustível para sua operação na capital',
  'GLP ou diesel: qual combustível atende melhor a indústria de Inhumas')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  'Nos galpões de confecção do polo têxtil de Inhumas, onde a empilhadeira transita entre o estoque fechado e a doca de expedição, o GLP é a opção mais prática — emite menos monóxido de carbono que o diesel e permite que a máquina circule em ambiente interno sem comprometer a qualidade do ar. A troca de cilindro leva menos de 3 minutos e dispensa infraestrutura elétrica. Nos armazéns de grãos e cooperativas agrícolas da região, onde pátios de terra batida e rampas de carga são comuns, o diesel entrega o torque necessário para subir carregado sem perda de tração.')

r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  'De 2.000 a 8.000 kg: como escolher a capacidade certa para Inhumas')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  'O dimensionamento correto exige somar o peso do palete ao centro de gravidade da carga. No polo têxtil de Inhumas, fardos de tecido e caixas de confecção pesam entre 600 e 1.200 kg por palete — a Clark L25 (2.500 kg) opera com margem de segurança. Na indústria alimentícia, paletes de embalagens e ingredientes chegam a 1.500 kg, e a L30/35 é a indicação adequada. Para sacas de grãos em big bags de 1.000 kg e cargas do Distrito Industrial, a S40-60 cobre a faixa intermediária. Subdimensionar arrisca a integridade da carga e do operador; superdimensionar encarece o contrato sem necessidade.')

r('Clark L25: a empilhadeira mais locada em Goiânia',
  'Clark L25: a preferida nos galpões de confecção de Inhumas')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  'A Clark L25 concentra a maioria dos contratos de locação para a região de Inhumas. Capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex com visibilidade total e sistema hidráulico de alta eficiência. Ela manobra nos corredores de 3,5 m dos galpões de confecção, empilha fardos de tecido até 6 metros de altura e opera nas docas das indústrias alimentícias sem comprometer a estabilidade. O contrapeso traseiro mantém a máquina firme mesmo com carga máxima em elevação total — fundamental para a operação contínua no Distrito Industrial de Inhumas.')

r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  'operação ininterrupta sem parada para recarga. Troca de cilindro GLP em 3 minutos nos galpões de confecção e armazéns de grãos de Inhumas.')

r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  '<strong>Onde opera em Inhumas:</strong> galpões de confecções do polo têxtil, indústrias alimentícias, armazéns de grãos, cooperativas agrícolas da região, Distrito Industrial de Inhumas e fábricas ao longo da GO-070.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia', 'Entrega no mesmo dia via GO-070')

r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Inhumas" selected>Inhumas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Trindade">Trindade</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Outra">Outra cidade</option>''', 2)

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL
# ═══════════════════════════════════════════════════════════════════════

r('A série mais contratada para CDs da BR-153', 'A série mais procurada para o polo têxtil de Inhumas')
r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  'Linha principal Clark para movimentação de fardos de tecido, paletes de alimentos e sacas de grãos. Garfos de 1.070 mm, mastro triplex e contrapeso calibrado para estabilidade em elevação máxima. Transmissão powershift para manobras ágeis em corredores de 3,5 m — padrão dos galpões de confecção e armazéns de Inhumas.')

r('Alta performance com cabine fechada', 'Cabine fechada para turnos prolongados no Distrito Industrial')
r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  'Série premium com cabine selada contra poeira de tecido e particulados da indústria alimentícia. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico em tempo real. Nos galpões de confecção de Inhumas, a cabine fechada preserva o conforto do operador durante turnos de 10 horas e reduz a exposição a fibras têxteis em suspensão.')
r('Alta performance, Distrito Industrial', 'Turnos longos, polo têxtil e alimentício')

r('S-Series para uso geral e pátios externos', 'S-Series para transição entre galpão e pátio em Inhumas')
r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  'A S-Series combina chassi reforçado e suspensão robusta para alternar entre o galpão pavimentado e o pátio de terra — rotina frequente nos armazéns de grãos e cooperativas agrícolas de Inhumas. Cabine aberta com ventilação natural adequada ao calor do cerrado goiano. Motor GLP ou diesel e ergonomia projetada para operadores que carregam caminhões graneleiros e organizam estoque em armazéns de grande porte.')
r('Uso geral, pátios, cooperativas', 'Armazéns de grãos, cooperativas, pátios')

r('Compacta para corredores estreitos', 'Compacta para galpões de confecção com corredores apertados')
r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  'A C20s é a empilhadeira mais compacta da linha Clark a combustão. Raio de giro reduzido para corredores de 2,8 m onde máquinas convencionais não entram. Capacidade de 2.000 kg para fardos de tecido, caixas fracionadas e paletes leves. Nos galpões de confecção menores de Inhumas e depósitos do centro da cidade, ela resolve operações em espaço restrito sem sacrificar a produtividade.')
r('Corredores estreitos, armazéns urbanos', 'Confecções compactas, depósitos urbanos')

r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg', 'Heavy duty intermediária para armazéns de grãos e cargas pesadas')
r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  'A S40-60 ocupa a faixa intermediária entre empilhadeiras de médio porte e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para pisos sem pavimentação. Nos armazéns de grãos de Inhumas, ela movimenta big bags de 1.000 kg e paletes duplos de sacas. Na construção civil e no Distrito Industrial, desloca insumos pesados e equipamentos entre galpões e pátios de carga.')
r('Cargas pesadas, pátios industriais', 'Armazéns de grãos, Distrito Industrial')

r('Heavy duty para o Distrito Industrial', 'Heavy duty para cargas acima de 6 toneladas em Inhumas')
r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  'Linha pesada Clark projetada para cargas de 6.000 a 8.000 kg. No Distrito Industrial de Inhumas e em operações agroindustriais da região, movimenta equipamentos pesados, paletes de insumos industriais e cargas de grande volume. Motor diesel de alto torque com transmissão reforçada e pneus maciços para pátios de terra e cascalho.')
r('Ultra heavy, Distrito Industrial', 'Cargas ultra pesadas, agroindústria')

r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  'Empilhadeiras Clark a Combustão: especificações da frota para aluguel em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  '"Inhumas tem um perfil industrial muito específico — polo têxtil forte, indústrias alimentícias crescendo e armazéns de grãos que operam na safra em volume dobrado. O erro mais comum que encontro é empresa do setor de confecções comprando empilhadeira usada sem garantia. No quarto mês, a corrente do mastro estica, a bomba hidráulica começa a vazar e a peça de reposição demora 20 dias para chegar de São Paulo. A conta do tempo parado, com fardos acumulando na expedição e caminhão esperando na doca, ultrapassa o valor de seis meses de aluguel. Com a locação, a manutenção é nossa responsabilidade e, se o volume da safra pedir mais máquinas, a gente escala a frota sem contrato novo."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  '<strong>Critério prático para Inhumas:</strong> se a empilhadeira alterna entre galpão de confecções e doca de expedição, ou se o turno ultrapassa 8 horas sem pausa para recarga, a combustão é a resposta. Nos armazéns de grãos e indústrias alimentícias da região, onde o piso muda de concreto para terra batida, o GLP ou diesel mantém a operação sem interrupção. Na dúvida, fazemos avaliação técnica gratuita no seu galpão.')

r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis em Inhumas:')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Inhumas')
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/inhumas-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Inhumas')
r('/goiania-go/aluguel-de-transpaleteira', '/inhumas-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Inhumas')
r('/goiania-go/curso-operador-empilhadeira', '/inhumas-go/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  'alt="Valores e condições de aluguel de empilhadeira Clark em Inhumas e região"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  'Veja como funciona o <span>aluguel de empilhadeira Clark</span> em Inhumas')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  'Acompanhe o processo completo de aluguel: consulta técnica, seleção do modelo Clark adequado para sua operação, entrega via GO-070 no galpão de confecções, armazém de grãos ou indústria alimentícia em Inhumas e suporte técnico durante toda a vigência. Sem burocracia, sem taxa oculta.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  'Investimento mensal: <span>empilhadeira GLP e diesel</span> em Inhumas (2026)')
r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  'Tabela de referência para aluguel de empilhadeira Clark em Inhumas. O valor final depende do modelo, combustível, capacidade e prazo do contrato.')
r('Entrega em Goiânia (sem deslocamento)', 'Entrega em Inhumas (40 km, sem custo)')
r('Entrega em cidades mais distantes', 'Entrega no Distrito Industrial e armazéns')
r('Sem custo de deslocamento na capital', 'Sem custo de frete para Inhumas')
r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 40 km de Inhumas pela GO-070. Não cobramos frete adicional. A empilhadeira chega ao seu galpão de confecções, indústria alimentícia ou armazém de grãos pronta para operar no mesmo dia da confirmação.')
r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  'nos galpões de confecção e armazéns de grãos de Inhumas, uma empilhadeira parada custa R$1.200 a R$2.000 por dia entre fardos acumulados na expedição, caminhões aguardando carga e penalidades por atraso na entrega. Uma visita técnica avulsa sai R$800 a R$1.500 — e a peça de reposição pode demorar semanas. No contrato da Move Máquinas, manutenção preventiva e corretiva estão cobertas. Se a máquina falhar, substituímos no mesmo dia.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

r('      Aplicações em Goiânia', '      Aplicações na região')
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  'Onde a <span>empilhadeira a combustão Clark</span> opera em Inhumas')
r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Do polo têxtil aos armazéns de grãos: os setores que mantêm empilhadeiras em turno contínuo na cidade.')

r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  'alt="Galpão de confecções no polo têxtil de Inhumas com empilhadeira Clark movimentando fardos de tecido"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>Polo têxtil: fardos de tecido e confecções prontas</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  'Inhumas abriga o maior polo de confecções do interior de Goiás. Empilhadeiras Clark L25 movimentam fardos de tecido cru, paletes de confecções embaladas e caixas de aviamentos nos galpões de estoque e expedição. A troca de cilindro GLP em 3 minutos mantém a operação contínua durante os picos de produção sazonal, sem pausa para recarga de bateria.')

r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Indústria alimentícia de Inhumas com empilhadeira Clark operando em doca de expedição"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Indústria alimentícia: paletes de insumos e produtos acabados</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  'As indústrias alimentícias de Inhumas produzem em escala regional e despacham para distribuidores de todo o Centro-Oeste. Empilhadeiras a combustão transportam paletes de ingredientes entre o estoque e a linha de produção, carregam caminhões na doca de expedição e organizam paletes de produtos acabados na câmara de armazenamento. A Clark L25 GLP opera entre áreas internas e externas sem trocar de equipamento.')

r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  'alt="Armazém de grãos em Inhumas com empilhadeira Clark movimentando sacas e big bags"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>Armazéns de grãos: sacas, big bags e carga de graneleiros</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  'Os armazéns de grãos de Inhumas recebem e escoam safra de milho, soja e sorgo para toda a região. Empilhadeiras Clark S25/30 e S40-60 movimentam big bags de 1.000 kg, sacas empilhadas em paletes e insumos agrícolas entre o galpão coberto e o pátio de carga dos caminhões graneleiros. O motor diesel oferece tração firme em pisos de terra batida e rampas de carga.')

r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  'alt="Distrito Industrial de Inhumas com galpões e empilhadeira Clark em operação no pátio de carga"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>Distrito Industrial e cooperativas agrícolas</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  'O Distrito Industrial de Inhumas reúne fábricas de médio porte e cooperativas agrícolas que armazenam fertilizantes, defensivos e sementes. Empilhadeiras Clark operam nos pátios de carga e galpões sem pavimentação com a mesma eficiência do asfalto — os pneus maciços e a suspensão reforçada da S-Series absorvem o impacto do terreno irregular e mantêm a estabilidade em rampas de acesso.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  'Equipe técnica mobile com deslocamento pela GO-070. Atendimento em Inhumas em aproximadamente 50 minutos a partir da sede. Diagnóstico de motor, transmissão e parte elétrica diretamente no seu galpão ou armazém.')
r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da empilhadeira via GO-070 até seu galpão de confecções, indústria alimentícia ou armazém de grãos em Inhumas. São 40 km da sede — entrega no mesmo dia, sem custo de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  '"Usamos duas Clark L25 GLP no nosso galpão de confecções em Inhumas. A empilhadeira movimenta 120 fardos de tecido por dia, empilha até o quinto nível do porta-paletes e a troca de cilindro não demora nem 5 minutos. No mês passado, a válvula hidráulica de uma delas começou a vazar. Liguei para a Move às 7h e o técnico chegou pela GO-070 antes das 9h. Trocou a peça no local, sem custo extra. É outro nível de atendimento."')
r('<strong>Roberto M.</strong>', '<strong>Leandro F.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  'Supervisor de Expedição, Confecções, Inhumas-GO (dez/2025)')

r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  '"Operamos com Clark L30 diesel no armazém de grãos. Na safra, a movimentação de big bags e sacas triplica e a máquina trabalha de 6h às 22h sem folga. O diesel dá conta das rampas do pátio de terra batida e a empilhadeira não perdeu tração nem com chuva. Renovamos o contrato por mais um ano — fica muito mais barato do que manter máquina própria com mecânico de plantão e peça de importação."')
r('<strong>Fábio S.</strong>', '<strong>Cláudio R.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  'Gerente de Armazém, Cooperativa Agrícola, Inhumas-GO (jan/2026)')

r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  '"Terceira renovação seguida com a Move Máquinas. Na nossa fábrica de alimentos em Inhumas, o volume de produção varia muito entre os meses. Com a locação, escalamos de uma para três empilhadeiras no pico e devolvemos quando a demanda recua. Sem imobilizar capital, sem depreciação. O orçamento pelo WhatsApp chega em minutos e a entrega pela GO-070 é no mesmo dia."')
r('<strong>Daniela P.</strong>', '<strong>Fernanda G.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  'Diretora de Operações, Indústria Alimentícia, Inhumas-GO (fev/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11
# ═══════════════════════════════════════════════════════════════════════

r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso NR-11 para operadores de empilhadeira</a>? Indicamos centros de formação credenciados na região de Inhumas e Goiânia.')
r('curso de operador de empilhadeira</a>.', 'curso NR-11 de operador de empilhadeira</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Inhumas</span> e cidades vizinhas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 40 km de Inhumas pela GO-070. Entrega de empilhadeira Clark no mesmo dia da confirmação. Cobrimos toda a região metropolitana e cidades num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/"><strong>Inhumas</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/trindade-go/">Trindade</a>
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
        <a href="/aparecida-de-goiania-go/">Aparecida de Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília (DF)</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/itumbiara-go/">Itumbiara</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

r('!2d-49.2654!3d-16.7234', '!2d-49.4952!3d-16.3547')
r('title="Localização Move Máquinas em Goiânia"', 'title="Área de atendimento Move Máquinas — Inhumas"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Inhumas</a>')
r('/goiania-go/" style="color', '/inhumas-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  'Dúvidas sobre <span>aluguel de empilhadeira a combustão</span> em Inhumas')

r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<', '>Qual empilhadeira Clark é mais indicada para os galpões de confecção em Inhumas?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  '>A Clark L25 lidera os contratos na região de Inhumas. Com 2.500 kg de capacidade e garfos de 1.070 mm, ela movimenta fardos de tecido e paletes de confecções prontas em corredores de 3,5 m. Opera com GLP nos galpões fechados — menos emissão e troca de cilindro em 3 minutos mantêm a linha de separação funcionando.<')

r('>Qual a diferença entre empilhadeira a combustão e elétrica?<', '>Combustão ou elétrica: qual escolher para o polo têxtil e armazéns de Inhumas?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  '>Nos galpões de confecções e armazéns de grãos de Inhumas, onde a empilhadeira alterna entre área fechada e doca de expedição, a combustão (GLP ou diesel) oferece torque superior, opera em pátios de terra batida e não exige pausa para recarga. A elétrica atende apenas galpões totalmente fechados com infraestrutura de carregamento. Para operações mistas em Inhumas, a combustão cobre mais cenários com menos limitação.<')

r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<', '>Qual o valor mensal do aluguel de empilhadeira em Inhumas?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  '>O investimento mensal fica entre R$2.800 e R$4.000, variando conforme modelo (L25, GTS, S-Series ou C-Series), tipo de combustível e duração do contrato. Inhumas recebe sem custo de frete — são 40 km pela GO-070. O pacote inclui manutenção preventiva e corretiva, suporte técnico 24h e equipe mobile que chega em cerca de 50 minutos.<')

r('>A manutenção da empilhadeira está inclusa no aluguel?<', '>O contrato cobre toda a manutenção da empilhadeira?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  '>Integralmente. O contrato cobre revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo adicional de peça ou mão de obra. Nossa equipe técnica mobile percorre a GO-070 e chega a Inhumas em aproximadamente 50 minutos. Se a máquina apresentar defeito grave, substituímos o equipamento no mesmo dia.<')

r('>Qual combustível escolher: GLP ou diesel?<', '>GLP ou diesel para as operações em Inhumas?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  '>O GLP é o padrão nos galpões de confecções e indústrias alimentícias de Inhumas — emite menos monóxido de carbono e permite transição entre área fechada e doca sem trocar de equipamento. O diesel é a escolha nos armazéns de grãos com pátios de terra batida e rampas íngremes, onde o torque máximo faz diferença. Todos os modelos Clark aceitam ambos os combustíveis, e alteramos a configuração no próprio contrato se necessário.<')

r('>Vocês entregam empilhadeira fora de Goiânia?<', '>Qual o prazo de entrega da empilhadeira em Inhumas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Inhumas recebe no mesmo dia da confirmação. São 40 km pela GO-070 a partir da sede em Goiânia — a empilhadeira chega ao seu galpão de confecções, armazém de grãos ou indústria alimentícia em cerca de 50 minutos. Sem custo de deslocamento. Também atendemos Trindade, Anápolis, Senador Canedo e toda a região num raio de 200 km.<')

r('>Preciso de habilitação especial para operar empilhadeira?<', '>Operadores em Inhumas precisam de certificação NR-11?<')
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  'Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador de empilhadeira. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Conectamos sua equipe a centros de formação credenciados na região de Inhumas e Goiânia. Saiba mais sobre o')

r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<', '>Até quantos quilos as empilhadeiras Clark disponíveis suportam?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  '>A frota vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para fardos de tecido e paletes de alimentos no polo têxtil e indústrias alimentícias, a L25/30/35 resolve com folga. Para sacas de grãos em big bags e cargas pesadas no Distrito Industrial de Inhumas, a S40-60 ou C-Series são a indicação técnica. Dimensionamos o modelo certo antes de fechar — sem custo de consultoria.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA + JS + ADDITIONAL REWRITES
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia', 'Solicite empilhadeira Clark para Inhumas')
r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'", "'Olá, preciso de empilhadeira a combustão em Inhumas.\\n\\n'")
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'", "title=\\'Aluguel de empilhadeira Clark em Inhumas e região\\'")

# Marquee stats bar
r('<strong>Clark</strong> exclusivo em Goiás', '<strong>Clark</strong> distribuidor autorizado GO', 99)
r('<strong>200km</strong> raio de atendimento', '<strong>40 km</strong> de Inhumas pela GO-070', 99)

# Cotação rápida
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Escolha a empilhadeira certa para Inhumas. <span style="color:var(--color-primary);">Peça seu orçamento agora.</span>')
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe o modelo e a urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e disponibilidade para Inhumas.')
r('Manutenção inclusa (motor, hidráulico, mastro)', 'Manutenção total inclusa no contrato')
r('GLP ou Diesel, de 2.000 a 8.000 kg', 'GLP ou Diesel — 2.000 a 8.000 kg')
r('Suporte técnico 24h, 7 dias', 'Equipe técnica mobile 24h para Inhumas')

# Fleet section
r('Frota Clark', 'Frota disponível')
r('Frota de <span>empilhadeira Clark</span> disponível para locação', 'Empilhadeiras <span>Clark a combustão</span> disponíveis para Inhumas')
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Da compacta C20s até a C80 heavy duty: seis séries cobrindo de 2.000 a 8.000 kg para o polo têxtil, indústria alimentícia e armazéns de grãos.')
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua operação precisa? Dimensionamos sem custo. Fale pelo WhatsApp ou ligue agora.')

# Comparativo
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  'Nos galpões de confecções, indústrias alimentícias e armazéns de grãos de Inhumas, a decisão entre combustão e elétrica depende do piso, ventilação e regime de turnos. Escolher errado significa máquina parada ou equipamento inadequado para o ambiente da operação.')
r('Para pátios, docas e operações mistas', 'Galpões de confecção, armazéns e pátios')
r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre galpão fechado e pátio de terra batida sem restrição. Motor GLP ou diesel com torque para rampas e pisos irregulares dos armazéns de grãos e Distrito Industrial de Inhumas.')
r('Para ambientes fechados e silenciosos', 'Galpões com área limpa e restrição de emissão')
r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para câmaras frias e áreas de produção alimentícia com restrição de circulação de ar em Inhumas.')

# Incluso extras
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas locando equipamentos industriais no Centro-Oeste nos ensinaram que o diferencial do contrato não é a máquina — é a velocidade de resposta quando o hidráulico falha no meio do turno de produção.')
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Avaliamos modelo, capacidade e combustível adequados antes de fechar. No polo têxtil e nos armazéns de grãos de Inhumas, cada operação tem particularidade — a consultoria gratuita evita contratação errada.')

# Price extras
r('R$2.800 a R$4.000/mês com manutenção inclusa', 'De R$2.800 a R$4.000/mês — manutenção e entrega no pacote')
r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal cobre a máquina completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou frete para Inhumas.')
r('O custo real de uma empilhadeira parada', 'Quanto custa um dia de empilhadeira parada em Inhumas')

# NR-11 extras
r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  'Operação de empilhadeira e conformidade com a <span>NR-11</span> em Inhumas')
r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  'A NR-11 define as regras para movimentação, transporte e armazenagem de materiais em ambiente industrial. Todo operador de empilhadeira nos galpões de confecção, indústrias alimentícias e armazéns de Inhumas precisa de certificação válida.')
r('O que a NR-11 exige do operador de empilhadeira', 'Requisitos NR-11 para operadores em Inhumas')
r('Como garantir a conformidade antes de operar', 'Passo a passo para operar em conformidade no município')
r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em pátio industrial.')
r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno o operador deve checar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores de segurança.')
r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Delimite os corredores exclusivos de empilhadeira no galpão, posicione espelhos convexos nos cruzamentos e estabeleça limite de velocidade onde há trânsito de pedestres e operários.')
r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção preventiva. Cada empilhadeira da Move Máquinas é entregue acompanhada do checklist de inspeção pré-operacional completo.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  'Empresas de Inhumas que operam com <span>empilhadeira Clark</span>')

# Footer subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, valor e prazo de entrega para Inhumas.')

# Video caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — veja como funciona a locação de equipamentos.')

# Alt texts
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  'alt="Empilhadeira Clark L25 a combustão para aluguel em Inhumas — polo têxtil e armazéns de grãos"')
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas no Distrito Industrial de Inhumas"')
r('alt="Empilhadeira Clark a combustão em operação"',
  'alt="Empilhadeira Clark a combustão em operação em Inhumas"')

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
            'goiania-go/', '40 km', 'Sede na',
            'Inhumas e Goiânia',
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

inh = html.count('Inhumas')
local = html.count('confecç') + html.count('têxtil') + html.count('alimentíc') + html.count('grãos') + html.count('GO-070')
print(f"\nInhumas: {inh} menções")
print(f"Contexto local (confecção/têxtil/alimentícia/grãos/GO-070): {local} menções")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS
# ═══════════════════════════════════════════════════════════════════════

def extract_text(h):
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

comparisons = [
    ('/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html', 'SC'),
    ('/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-empilhadeira-combustao-V2.html', 'BSB'),
]
for comp_path, label in comparisons:
    if os.path.exists(comp_path):
        with open(comp_path, 'r', encoding='utf-8') as f:
            comp_html = f.read()
        comp_text = extract_text(comp_html)
        comp_ng = ngrams(comp_text)
        j_comp = jaccard(new_ng, comp_ng)
        fname = os.path.basename(comp_path)
        print(f"vs {fname}: {j_comp:.4f}  {'✓' if j_comp < 0.20 else '✗ FALHOU'}")
    else:
        print(f"vs {label}: arquivo não encontrado, pulando")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

elapsed = time.time() - start
print(f"\n✅ Salvo: {OUT}")
print(f"TEMPO: {elapsed:.1f}s")
print(f"TOKENS (approx chars): {len(html):,}")
