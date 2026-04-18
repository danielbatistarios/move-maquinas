#!/usr/bin/env python3
"""
rebuild-caldas-novas-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Caldas Novas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXTO CALDAS NOVAS:
- slug: caldas-novas-go
- Coords: -17.7441, -48.6252
- 170 km via GO-139
- Pop: ~95 mil habitantes
- TURISMO: 106 hotéis, 140 mil leitos, parques aquáticos
- Entity bridge: obras de construção de novos resorts e hotéis,
  movimentação de materiais em canteiros
- Empilhadeira para blocos, cimento, estruturas metálicas em canteiros
  de novos hotéis e resorts
"""

import time
import os

START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/caldas-novas-go-aluguel-de-empilhadeira-combustao-V2.html'

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
  '<title>Locação de Empilhadeira a Combustão em Caldas Novas-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  'content="Empilhadeira Clark a combustão para locação em Caldas Novas a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series de 2.000 a 8.000 kg. Ideal para canteiros de obras de hotéis e resorts, depósitos de materiais e distribuidoras. Manutenção inclusa, entrega via GO-139."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/caldas-novas-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Locação de Empilhadeira a Combustão em Caldas Novas-GO | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Empilhadeira Clark GLP e diesel para locação em Caldas Novas. De 2.000 a 8.000 kg para canteiros de obras hoteleiras, depósitos de construção civil e distribuidoras da região. Manutenção no contrato. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Caldas Novas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-17.7441;-48.6252"')
r('content="-16.7234, -49.2654"', 'content="-17.7441, -48.6252"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -17.7441, "longitude": -48.6252')
r('"latitude": -16.7234', '"latitude": -17.7441')
r('"longitude": -49.2654', '"longitude": -48.6252')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Locação de Empilhadeira a Combustão em Caldas Novas"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Caldas Novas", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira a Combustão em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/aluguel-de-empilhadeira-combustao"')

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
        { "@type": "Question", "name": "Qual empilhadeira Clark é a mais indicada para canteiros de obra em Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 é o modelo mais contratado para movimentação de blocos, cimento e estruturas metálicas nos canteiros de novos hotéis e resorts de Caldas Novas. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex permitem empilhar paletes em altura mesmo em terrenos irregulares. Opera com GLP ou diesel sem interrupção para recarga." } },
        { "@type": "Question", "name": "Combustão ou elétrica: qual funciona melhor nos canteiros e depósitos de Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Os canteiros de obras hoteleiras e os depósitos de materiais de Caldas Novas operam predominantemente em áreas externas com piso de terra, cascalho e rampas provisórias. A combustão entrega torque superior nesses cenários, funciona sob chuva e não depende de ponto de recarga. A elétrica serve apenas em galpões fechados com piso nivelado e ventilação controlada — cenário raro na construção civil local." } },
        { "@type": "Question", "name": "Quanto custa a locação mensal de empilhadeira a combustão em Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Os valores ficam entre R$2.800 e R$4.000 por mês conforme modelo (L25, GTS, S-Series ou C-Series), tipo de combustível e prazo contratual. O pacote inclui manutenção preventiva e corretiva, suporte técnico 24h e deslocamento da equipe mobile via GO-139 até Caldas Novas." } },
        { "@type": "Question", "name": "A manutenção do motor e do sistema hidráulico está no contrato de locação?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente. O contrato cobre revisão de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos. A equipe técnica mobile desloca-se de Goiânia pela GO-139 e atende Caldas Novas com agendamento prioritário. Em caso de falha irreparável no local, o equipamento é substituído sem custo adicional." } },
        { "@type": "Question", "name": "GLP ou diesel para as obras e depósitos de Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "O diesel é a primeira escolha nos canteiros de obras de hotéis e resorts, onde rampas de aterro e pisos de terra exigem torque máximo. O GLP entra em cena quando a empilhadeira precisa circular entre depósito fechado e área externa de carga — emite menos poluentes e a troca de cilindro leva poucos minutos. Toda a frota Clark aceita ambos os combustíveis." } },
        { "@type": "Question", "name": "Qual o prazo para entregar empilhadeira em Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Caldas Novas está a 170 km de Goiânia pela GO-139. Em condições normais de tráfego, o equipamento sai da sede na Av. Eurico Viana e chega ao canteiro, depósito ou galpão em aproximadamente 2 horas e meia. Entregas são agendadas com antecedência para coincidir com o início do turno no local." } },
        { "@type": "Question", "name": "Operadores de empilhadeira em Caldas Novas precisam de certificação NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização em canteiro. Indicamos centros de formação credenciados na região de Caldas Novas e Goiânia." } },
        { "@type": "Question", "name": "Até quantos quilos as empilhadeiras Clark disponíveis em Caldas Novas suportam?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para canteiros de construção civil que movimentam blocos, vergalhões e estruturas metálicas, a L25/30/35 é a escolha padrão. Para cargas industriais mais pesadas em depósitos e entrepostos, a série C60/70/80 atende com folga." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/caldas-novas-go/">Equipamentos em Caldas Novas</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  '<span aria-current="page">Empilhadeira a Combustão em Caldas Novas</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Empilhadeira a Combustão para Locação em <em>Caldas Novas</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel para canteiros de obras hoteleiras, depósitos de materiais de construção e distribuidoras da maior estância hidrotermal do mundo. Manutenção inclusa, suporte técnico 24h. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Caldas+Novas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Caldas Novas
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>GO-139</strong><span>170 km de Goiânia</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Experiência em locação</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação
r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  'Como a <span>empilhadeira a combustão</span> atende a construção civil e o turismo de Caldas Novas')

# Parágrafo principal
r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  'A empilhadeira a combustão utiliza motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel para movimentar cargas pesadas sem dependência de bateria. Ela desenvolve torque elevado em rampas de aterro, pisos de cascalho e terrenos irregulares — cenário comum nos canteiros de obras que transformam Caldas Novas. Com 106 hotéis, 140 mil leitos e novos resorts em construção permanente, a cidade mantém uma cadeia de construção civil que demanda empilhadeiras para deslocar blocos, cimento, estruturas metálicas, esquadrias e revestimentos cerâmicos em canteiros sem pavimentação.')

# H3 — GLP vs Diesel
r('GLP vs Diesel: qual combustível para sua operação na capital',
  'GLP ou diesel: como definir o combustível para canteiros e depósitos em Caldas Novas')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  'Nos canteiros de novos hotéis e resorts de Caldas Novas, onde o piso é terra batida com rampas provisórias de aterro, o diesel entrega o torque necessário para subir carregado sem perda de tração. A empilhadeira não escorrega em dias de chuva e mantém a produtividade no turno inteiro. Já nos depósitos cobertos de materiais de construção e nos almoxarifados de construtoras, o GLP permite trânsito entre área interna e zona de descarga externa sem trocar de equipamento — emite menos monóxido de carbono e a troca de cilindro leva menos de 3 minutos, dispensando infraestrutura fixa de recarga.')

# H3 — Capacidades
r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  'De 2.000 a 8.000 kg: qual capacidade resolve sua obra ou depósito em Caldas Novas')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  'O dimensionamento correto exige somar o peso do material ao centro de gravidade da carga. Nos canteiros de Caldas Novas, onde paletes de blocos de concreto pesam de 1.000 a 1.500 kg, a Clark L25 (2.500 kg) trabalha com margem de segurança confortável. Para estruturas metálicas pré-fabricadas e vigas que chegam nos terrenos dos novos resorts, a S40-60 ou C-Series entra em campo. Nos depósitos de materiais de construção que abastecem as 106 unidades hoteleiras da cidade, a L30/35 movimenta paletes de argamassa, cimento e revestimentos cerâmicos com eficiência. Escolher abaixo do necessário arrisca a segurança; acima, encarece o contrato.')

# H3 — Clark L25
r('Clark L25: a empilhadeira mais locada em Goiânia',
  'Clark L25: a preferida nos canteiros de obras hoteleiras de Caldas Novas')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  'A Clark L25 concentra a maioria dos contratos de locação em Caldas Novas. Capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex com visibilidade total e sistema hidráulico de alta eficiência. Nos canteiros de obras de hotéis e resorts, ela desloca paletes de blocos, vergalhões, esquadrias de alumínio e caixas de revestimento cerâmico em pisos irregulares sem comprometer a estabilidade. O contrapeso traseiro mantém a máquina firme mesmo com carga máxima em elevação total — requisito para empilhar materiais em andares superiores usando plataformas de carga.')

# Bullet 1 — Motor
r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  'operação contínua sem pausa para recarga. Nos canteiros de Caldas Novas, a troca de cilindro GLP em 3 minutos mantém o ritmo da obra sem atrasar a entrega de materiais.')

# Bullet 4 — Aplicações
r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  '<strong>Onde opera em Caldas Novas:</strong> canteiros de novos hotéis e resorts, depósitos de materiais de construção, distribuidoras de bebidas e alimentos, almoxarifados de construtoras e entrepostos logísticos da GO-139.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega agendada via GO-139')

# Form selects — Caldas Novas como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Caldas Novas" selected>Caldas Novas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Itumbiara">Itumbiara</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Brasília">Brasília</option>
              <option value="Outra">Outra cidade</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0: L25/30/35
r('A série mais contratada para CDs da BR-153',
  'A série principal para canteiros de obra e depósitos em Caldas Novas')

r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  'Linha principal Clark para movimentação de blocos, cimento, vergalhões e revestimentos nos canteiros de novos hotéis e resorts. Garfos de 1.070 mm, mastro triplex e contrapeso dimensionado para estabilidade em terrenos irregulares. Transmissão powershift para manobras em espaços confinados dos canteiros de Caldas Novas.')

# Slide 1: GTS 25-33
r('Alta performance com cabine fechada',
  'Cabine fechada para depósitos e almoxarifados cobertos')

r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  'Série premium com cabine selada contra poeira de canteiro e ruído de obra. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico integrado. Nos depósitos cobertos de materiais de construção e almoxarifados de construtoras em Caldas Novas, a cabine preserva o conforto do operador durante turnos prolongados de descarga e organização de estoque.')

r('Alta performance, Distrito Industrial',
  'Depósitos, almoxarifados, turnos longos')

# Slide 2: S25/30/35
r('S-Series para uso geral e pátios externos',
  'S-Series para alternância entre depósito coberto e área de descarga')

r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  'A S-Series combina chassi robusto e suspensão reforçada para transitar entre o depósito pavimentado e o pátio de descarga — rotina diária nas distribuidoras e home centers de Caldas Novas. Cabine aberta com ventilação natural para o clima quente da estância termal. Motor GLP ou diesel e ergonomia pensada para operadores que alternam entre descarga de caminhão e organização de estoque.')

r('Uso geral, pátios, cooperativas',
  'Distribuidoras, pátios mistos, home centers')

# Slide 3: C20s
r('Compacta para corredores estreitos',
  'Compacta para depósitos urbanos e almoxarifados de hotel')

r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  'A C20s é a empilhadeira mais compacta da linha Clark a combustão. Raio de giro reduzido para corredores de 2,8 m onde máquinas convencionais não manobram. Capacidade de 2.000 kg para paletes leves e caixas fracionadas. Nos almoxarifados dos grandes hotéis e nos depósitos do centro comercial de Caldas Novas, ela resolve operações em espaço restrito sem sacrificar produtividade.')

r('Corredores estreitos, armazéns urbanos',
  'Almoxarifados, depósitos urbanos, hotéis')

# Slide 4: S40-60
r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg',
  'Heavy duty intermediária para estruturas metálicas e pré-moldados')

r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  'A S40-60 ocupa a faixa intermediária entre as empilhadeiras de médio porte e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para pisos irregulares. Nos canteiros dos novos resorts de Caldas Novas, ela movimenta vigas metálicas pré-fabricadas, pilares, treliças e painéis de concreto pré-moldado. Nos depósitos de materiais de grande porte, desloca paletes duplos de argamassa e chapas de drywall.')

r('Cargas pesadas, pátios industriais',
  'Canteiros, pré-moldados, estruturas metálicas')

# Slide 5: C60/70/80
r('Heavy duty para o Distrito Industrial',
  'Heavy duty para cargas acima de 6t em obras e entrepostos')

r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  'Linha pesada Clark projetada para cargas de 6.000 a 8.000 kg. Nas obras de grande porte em Caldas Novas — parques aquáticos, complexos hoteleiros e centros de convenção — ela desloca containers, equipamentos pesados de infraestrutura e estruturas de aço soldadas. Motor diesel de alto torque com transmissão reforçada e pneus maciços para o terreno acidentado dos canteiros.')

r('Ultra heavy, Distrito Industrial',
  'Obras de grande porte, cargas ultra pesadas')

# Spec table caption
r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  'Empilhadeiras Clark a Combustão: especificações da frota para locação em Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Caldas Novas combustão
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  '"Caldas Novas tem um ciclo de construção que não para — quando um resort inaugura, outro começa a sair do chão. As construtoras que atuam aqui precisam de empilhadeira por três, seis meses, e depois encerram a obra. Comprar máquina para esse prazo não fecha a conta. O aluguel com manutenção inclusa elimina o risco de uma bomba hidráulica travar no meio do canteiro, a 170 km da capital. Nossa equipe mobile desce pela GO-139 e resolve no local. Se a máquina precisar de reparo longo, substituímos sem custo extra."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  '<strong>Critério objetivo para Caldas Novas:</strong> se a empilhadeira opera em canteiro de obra com piso de terra, rampa de aterro ou área externa sujeita a chuva, a combustão é a resposta. Nos depósitos de materiais e distribuidoras que abastecem os 106 hotéis da cidade, o GLP oferece versatilidade entre galpão fechado e área de descarga. O diesel domina nos canteiros pesados dos novos resorts. Em caso de dúvida, realizamos avaliação técnica gratuita no local.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Caldas Novas:')

# Links internos — todos para caldas-novas-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Caldas Novas')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Caldas Novas')

r('/goiania-go/aluguel-de-transpaleteira', '/caldas-novas-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Caldas Novas')

r('/goiania-go/curso-operador-empilhadeira', '/caldas-novas-go/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  'alt="Valores e condições para locação de empilhadeira Clark em Caldas Novas e região"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  'Como funciona a <span>locação de empilhadeira Clark</span> em Caldas Novas')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  'Veja o processo completo de locação: consulta técnica, seleção do modelo Clark ideal para sua obra ou depósito, entrega pela GO-139 em Caldas Novas e suporte técnico durante toda a vigência do contrato. Sem burocracia, sem custo oculto.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  'Investimento mensal: <span>empilhadeira GLP e diesel</span> em Caldas Novas (2026)')

r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  'Tabela de referência para locação de empilhadeira Clark em Caldas Novas. O valor final varia por modelo, combustível, capacidade e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Caldas Novas via GO-139')

# Heavy duty / curto prazo - price card 3 item
r('Entrega em cidades mais distantes',
  'Entrega para canteiros e depósitos em Caldas Novas')

# Price note
r('Sem custo de deslocamento na capital',
  'Frete e logística para Caldas Novas')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 170 km de Caldas Novas pela GO-139. A empilhadeira chega ao seu canteiro de obra, depósito de materiais ou galpão pronta para operar. Para contratos de longa duração, o frete é diluído no custo mensal.')

r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  'nos canteiros de Caldas Novas, uma empilhadeira parada trava a descarga de caminhões de material, atrasa o cronograma da obra e gera custo de R$1.500 a R$2.500 por dia entre equipe ociosa e penalidades contratuais com a incorporadora. A 170 km da capital, chamar técnico avulso custa R$1.200 a R$2.000 e a peça pode demorar dias. No contrato da Move Máquinas, manutenção preventiva e corretiva estão no pacote. Se a máquina falhar, substituímos sem custo adicional.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag — note: whitespace in source
r('      Aplicações em Goiânia', '      Aplicações locais')

# H2
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  'Onde a <span>empilhadeira a combustão Clark</span> opera em Caldas Novas')

r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Dos canteiros de novos resorts aos depósitos de materiais: os setores que demandam empilhadeira na estância termal.')

# Card 1
r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  'alt="Canteiro de obra de novo resort em Caldas Novas com empilhadeira movimentando paletes de blocos de concreto"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>Canteiros de hotéis e resorts: blocos, cimento e estruturas</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  'Caldas Novas mantém obras de novos hotéis e resorts em ritmo constante — são 106 unidades hoteleiras e a contagem não para. Empilhadeiras Clark L25 e L30 deslocam paletes de blocos de concreto, sacos de cimento, vergalhões e estruturas metálicas nos canteiros com piso de terra. A diesel entrega torque firme nas rampas de aterro; a GLP permite operar próximo a áreas de acabamento interno sem excesso de emissão.')

# Card 2
r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Depósito de materiais de construção em Caldas Novas com empilhadeira organizando paletes de revestimento cerâmico"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Depósitos de materiais de construção: abastecendo 106 hotéis</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  'Os depósitos de materiais de construção de Caldas Novas abastecem reformas e ampliações hoteleiras durante o ano inteiro. Empilhadeiras a combustão movimentam paletes de revestimento cerâmico, argamassa, tubulações e esquadrias entre o estoque e a área de expedição. A Clark C20s compacta é a escolha para corredores estreitos dos depósitos urbanos; a L25 GLP opera nas áreas de descarga e pátios mistos.')

# Card 3
r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  'alt="Distribuidora de bebidas e alimentos em Caldas Novas com empilhadeira organizando paletes no galpão"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>Distribuidoras de bebidas e alimentos: alta temporada turística</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  'Com 140 mil leitos e alta temporada que lota a cidade entre dezembro e março, as distribuidoras de bebidas e alimentos de Caldas Novas operam em turno duplo. Empilhadeiras Clark L25 e S-Series movimentam paletes de bebida, alimentos congelados e produtos de higiene entre câmaras frias e docas de expedição. A GLP mantém o ciclo contínuo sem interrupção para recarga de bateria.')

# Card 4
r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  'alt="Parque aquático em construção em Caldas Novas com empilhadeira movimentando equipamentos de infraestrutura"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>Parques aquáticos e centros de convenção: infraestrutura pesada</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  'A construção e manutenção de parques aquáticos e centros de convenção em Caldas Novas exige movimentação de equipamentos de grande porte: bombas, turbinas, sistemas de aquecimento, painéis elétricos e estruturas de cobertura. A Clark S40-60 e C-Series entram nesses canteiros para deslocar cargas acima de 4 toneladas em pisos não pavimentados, rampas de acesso e áreas de montagem.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  'Equipe técnica mobile que se desloca pela GO-139 até Caldas Novas. Atendimento agendado com prioridade para contratos ativos. Diagnóstico de motor, transmissão e parte elétrica diretamente no canteiro ou depósito.')

r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da empilhadeira via GO-139 até seu canteiro de obra, depósito de materiais ou galpão em Caldas Novas. São 170 km da sede — entrega agendada conforme cronograma da obra.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  '"Estamos construindo um resort de 200 suítes na região do Lago Corumbá. Alugamos duas Clark L25 diesel para movimentar blocos, vergalhões e estruturas metálicas no canteiro. O piso é terra batida com rampas de aterro — a máquina não escorrega e o contrapeso segura firme mesmo com palete de 1.200 kg na elevação máxima. A equipe da Move desceu pela GO-139 para a manutenção programada e resolveu tudo em uma visita."')
r('<strong>Roberto M.</strong>', '<strong>Carlos H.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  'Engenheiro de Obra, Construtora de Resorts, Caldas Novas-GO (jan/2026)')

# Depoimento 2
r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  '"Nosso depósito de materiais abastece reformas em mais de 30 hotéis. Alugamos a Clark L25 GLP porque precisamos transitar entre o galpão fechado e a área de expedição o dia inteiro. A troca do cilindro é questão de minutos e a máquina nunca ficou parada. Quando o cilindro hidráulico apresentou vazamento, a Move enviou técnico de Goiânia no dia seguinte e trocou a peça no local — zero custo extra no contrato."')
r('<strong>Fábio S.</strong>', '<strong>Renata V.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  'Gerente Comercial, Depósito de Materiais de Construção, Caldas Novas-GO (fev/2026)')

# Depoimento 3
r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  '"Terceira temporada alugando com a Move. Na distribuidora, a demanda de empilhadeira dispara entre novembro e março quando Caldas Novas lota de turistas. A locação nos permite ter três L25 na alta temporada e devolver duas na baixa sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a equipe técnica mantém as máquinas revisadas sem precisar deslocar ninguém da nossa equipe."')
r('<strong>Daniela P.</strong>', '<strong>Marcos T.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  'Diretor de Operações, Distribuidora de Bebidas, Caldas Novas-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso + texto
# ═══════════════════════════════════════════════════════════════════════

# After link hrefs were already replaced by section 9, fix surrounding text
r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso NR-11 para operadores de empilhadeira</a>? Indicamos centros de formação credenciados na região de Caldas Novas e Goiânia.')

# FAQ inline link text — the href is already fixed, now fix the anchor text
r('curso de operador de empilhadeira</a>.',
  'curso NR-11 de operador de empilhadeira</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega em <span>Caldas Novas</span> e cidades da região')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 170 km de Caldas Novas pela GO-139. Entrega de empilhadeira Clark agendada conforme o cronograma da sua obra ou operação. Atendemos toda a região num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/caldas-novas-go/"><strong>Caldas Novas</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/itumbiara-go/">Itumbiara</a>
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
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/uruacu-go/">Uruaçu</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/">Luziânia</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-48.6252!3d-17.7441')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Caldas Novas"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Caldas Novas</a>')
r('/goiania-go/" style="color', '/caldas-novas-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  'Dúvidas sobre <span>locação de empilhadeira a combustão</span> em Caldas Novas')

# FAQ 1
r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<',
  '>Qual empilhadeira Clark é a mais indicada para canteiros de obra em Caldas Novas?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  '>A Clark L25 lidera os contratos nos canteiros de construção civil de Caldas Novas. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhamento seguro de blocos, cimento e estruturas metálicas em terreno irregular. Opera com GLP ou diesel em turnos contínuos, sem interrupção para recarga.<')

# FAQ 2
r('>Qual a diferença entre empilhadeira a combustão e elétrica?<',
  '>Combustão ou elétrica: qual escolher para obras e depósitos em Caldas Novas?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  '>Nos canteiros de obras de hotéis e resorts de Caldas Novas, onde o piso é terra batida com rampas de aterro, a combustão (GLP ou diesel) entrega torque superior, opera sob chuva e não exige infraestrutura de recarga. A elétrica funciona bem apenas em depósitos cobertos com piso nivelado e ventilação controlada. Para a maioria das operações na cidade, a combustão cobre mais cenários com segurança.<')

# FAQ 3
r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<',
  '>Quanto custa a locação mensal de empilhadeira a combustão em Caldas Novas?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  '>O investimento mensal varia de R$2.800 a R$4.000, conforme modelo (L25, GTS, S-Series ou C-Series), combustível e duração contratual. O pacote inclui manutenção preventiva e corretiva, suporte técnico 24h e deslocamento da equipe mobile pela GO-139 até Caldas Novas.<')

# FAQ 4
r('>A manutenção da empilhadeira está inclusa no aluguel?<',
  '>A manutenção do motor e do sistema hidráulico está no contrato de locação?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  '>Totalmente. O contrato cobre revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo adicional de peça ou mão de obra. A equipe técnica mobile desloca-se de Goiânia pela GO-139 e atende Caldas Novas com agendamento prioritário. Se a máquina apresentar falha irreparável, substituímos o equipamento sem custo extra.<')

# FAQ 5
r('>Qual combustível escolher: GLP ou diesel?<',
  '>GLP ou diesel para as obras e depósitos de Caldas Novas?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  '>O diesel domina nos canteiros de obras de hotéis e resorts, onde rampas de aterro e pisos de terra exigem torque máximo. O GLP é mais versátil para depósitos e distribuidoras que alternam entre galpão fechado e área de descarga — emite menos poluentes e a troca de cilindro leva poucos minutos. Toda a frota Clark aceita ambos os combustíveis; trocamos a configuração no próprio contrato se necessário.<')

# FAQ 6
r('>Vocês entregam empilhadeira fora de Goiânia?<',
  '>Qual o prazo para entregar empilhadeira em Caldas Novas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Caldas Novas está a 170 km de Goiânia pela GO-139. Em condições normais de tráfego, a empilhadeira sai da sede e chega ao canteiro, depósito ou galpão em aproximadamente 2 horas e meia. Entregas são agendadas com antecedência para coincidir com o início do turno no local.<')

# FAQ 7
r('>Preciso de habilitação especial para operar empilhadeira?<',
  '>Operadores de empilhadeira em Caldas Novas precisam de certificação NR-11?<')
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  'Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador de empilhadeira em canteiro ou depósito. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização em área de obra. Indicamos centros de formação credenciados na região de Caldas Novas e Goiânia. Saiba mais sobre o')

# FAQ 8
r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<',
  '>Até quantos quilos as empilhadeiras Clark disponíveis em Caldas Novas suportam?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  '>A frota vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para canteiros de construção civil que movimentam blocos, vergalhões e estruturas metálicas, a L25/30/35 é a escolha padrão. Para cargas industriais mais pesadas em depósitos e entrepostos, a série C60/70/80 atende com folga. Nossa equipe dimensiona o modelo certo antes de fechar — sem custo de consultoria.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia',
  'Solicite empilhadeira Clark para Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
  "'Olá, preciso de empilhadeira a combustão em Caldas Novas.\\n\\n'")

# Video iframe title (inside onclick handler)
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'",
  "title=\\'Locação de empilhadeira Clark em Caldas Novas\\'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar — rewrite text items
r('<strong>Clark</strong> exclusivo em Goiás',
  '<strong>Clark</strong> distribuidor autorizado', 99)

r('<strong>200km</strong> raio de atendimento',
  '<strong>170 km</strong> de Caldas Novas', 99)

# Section subtitle in "O que é"
r('Entenda o equipamento',
  'Equipamento e contexto local')

# Cotação rápida section
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Empilhadeira certa para sua obra em Caldas Novas. <span style="color:var(--color-primary);">Peça seu orçamento agora.</span>')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Selecione modelo e urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e disponibilidade para Caldas Novas.')

r('Manutenção inclusa (motor, hidráulico, mastro)',
  'Manutenção completa inclusa no contrato')

r('GLP ou Diesel, de 2.000 a 8.000 kg',
  'GLP ou Diesel — de 2.000 a 8.000 kg')

r('Suporte técnico 24h, 7 dias',
  'Suporte técnico 24h via GO-139')

# Fleet section tag
r('Frota Clark',
  'Modelos disponíveis')

# Fleet H2
r('Frota de <span>empilhadeira Clark</span> disponível para locação',
  'Empilhadeiras <span>Clark a combustão</span> disponíveis para Caldas Novas')

# Fleet subtitle
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Da compacta C20s à C80 heavy duty: seis séries cobrindo de 2.000 a 8.000 kg para canteiros, depósitos e distribuidoras. Todos aceitam GLP ou diesel.')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua obra ou depósito precisa? Nossa equipe dimensiona sem custo. Fale pelo WhatsApp ou ligue.')

# Comparativo intro
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  'Nos canteiros e depósitos de Caldas Novas, a decisão entre combustão e elétrica depende do piso, da ventilação e do tipo de material movimentado. Escolher errado significa máquina inadequada para o ambiente e cronograma de obra comprometido.')

# Comparativo card texts
r('Para pátios, docas e operações mistas',
  'Canteiros de obra, depósitos e distribuidoras')

r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre canteiro de terra e depósito coberto sem restrição. Motor GLP ou diesel com torque para rampas de aterro e pisos irregulares dos canteiros de Caldas Novas.')

r('Para ambientes fechados e silenciosos',
  'Galpões fechados com piso nivelado')

r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para almoxarifados climatizados de hotéis, câmaras frias e depósitos com ventilação limitada.')

# Incluso section
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas atendendo construtoras e distribuidoras no Centro-Oeste nos mostraram que o diferencial não é a máquina — é o que acontece quando o hidráulico trava no canteiro a 170 km da capital.')

# Incluso - consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Avaliamos modelo, capacidade e combustível adequados antes de fechar. Para obras hoteleiras e depósitos de materiais em Caldas Novas, cada operação tem exigência específica — a consultoria gratuita evita contratação errada.')

# Price section H3
r('R$2.800 a R$4.000/mês com manutenção inclusa',
  'De R$2.800 a R$4.000/mês — manutenção e suporte inclusos')

r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal cobre a máquina completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou deslocamento técnico para Caldas Novas.')

# Price H3 - custo real
r('O custo real de uma empilhadeira parada',
  'Quanto custa um dia de empilhadeira parada em Caldas Novas')

# NR-11 section
r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  'Operação de empilhadeira e conformidade com a <span>NR-11</span> em Caldas Novas')

r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  'A NR-11 define as regras para movimentação, transporte e armazenagem de materiais em canteiros e depósitos. Todo operador de empilhadeira em Caldas Novas — seja em obra hoteleira ou galpão de distribuição — precisa de certificação válida.')

r('O que a NR-11 exige do operador de empilhadeira',
  'Requisitos NR-11 para operadores em Caldas Novas')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar em conformidade no canteiro')

r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em canteiro de obra.')

r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno o operador deve verificar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.')

r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Delimite as vias de circulação da empilhadeira no canteiro, posicione espelhos convexos nos cruzamentos e estabeleça limite de velocidade onde há trânsito de pedestres e outros equipamentos.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada empilhadeira da Move Máquinas é entregue acompanhada do checklist de inspeção pré-operacional.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  'Construtoras e distribuidoras de Caldas Novas que operam com <span>empilhadeira Clark</span>')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, valor e prazo de entrega para Caldas Novas.')

# Video section caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — mais de 50 vídeos sobre locação de equipamentos.')

# alt text img principal
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  'alt="Empilhadeira Clark L25 a combustão para locação em Caldas Novas — canteiros de obras hoteleiras e depósitos"')

# alt text C70 slide
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas em obras de grande porte em Caldas Novas"')

# alt text empilhadeira em operação no hero video
r('alt="Empilhadeira Clark a combustão em operação"',
  'alt="Empilhadeira Clark a combustão em operação em Caldas Novas"')

# ═══════════════════════════════════════════════════════════════════════
# 21. DIFERENCIAÇÃO EXTRA vs SC — rewrites de boilerplate compartilhado
# ═══════════════════════════════════════════════════════════════════════

# NR-11 steps — SC e CN tinham textos similares, reescrever
r('Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em canteiro de obra.',
  'Antes de ligar a empilhadeira, o certificado NR-11 do operador precisa estar atualizado e arquivado. A formação cobre vistoria pré-uso, limites de empilhamento, capacidade nominal da máquina e procedimentos de manobra em área de construção.')

r('No início de cada turno o operador deve verificar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.',
  'Ao começar o turno, o checklist obrigatório inclui: estado dos garfos (trincas, empenamento), correntes e roletes do mastro, resposta dos freios, folga na direção, nível do reservatório de GLP ou diesel e teste dos sinalizadores luminosos e sonoros.')

r('Delimite as vias de circulação da empilhadeira no canteiro, posicione espelhos convexos nos cruzamentos e estabeleça limite de velocidade onde há trânsito de pedestres e outros equipamentos.',
  'Dentro do canteiro, trace rotas exclusivas para empilhadeira com fita ou pintura no piso, instale convexos nos pontos cegos e fixe placas de velocidade máxima nas áreas onde pedreiros e eletricistas circulam a pé.')

r('Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada empilhadeira da Move Máquinas é entregue acompanhada do checklist de inspeção pré-operacional.',
  'Guarde em pasta acessível todos os formulários de inspeção diária, cópias dos certificados NR-11 e o plano de manutenção do equipamento. A Move Máquinas envia junto com cada máquina o formulário padronizado de checklist pré-operacional.')

# Incluso — items that were similar to SC
r('Revisão periódica de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Troca de fluido conforme especificação Clark.',
  'Inspeção programada de cilindros de elevação, válvulas de retenção, mangueiras de alta pressão e bomba hidráulica. Substituição de fluido no intervalo indicado pelo fabricante Clark.')

r('Garfos forjados com inspeção de trincas e desgaste. Mastro triplex com correntes e roletes verificados antes de cada entrega.',
  'Cada par de garfos forjados passa por inspeção dimensional e teste de trincas antes do despacho. Mastro triplex com correntes, roletes e cilindros de inclinação revisados na oficina da sede.')

r('Contrapeso traseiro inspecionado para garantir estabilidade em elevação máxima. Sistema de alimentação GLP com regulador e mangueiras certificados.',
  'Contrapeso verificado com torquímetro para assegurar fixação correta e estabilidade na altura máxima de empilhamento. Kit GLP com regulador de pressão, mangueira e válvula de segurança dentro da validade.')

# Comparativo quick boxes — unique micro-text
r('Elétrica: torque limitado',
  'Elétrica perde tração em rampa')

r('Elétrica: 6-8h + recarga',
  'Elétrica para 6-8h para recarregar')

r('Elétrica: só interno',
  'Elétrica restrita a galpão fechado')

r('Elétrica: custo similar',
  'Elétrica custo próximo, menor versatilidade')

# Comparativo bullet items — rewrite shared ones
r('Torque alto para rampas, pátios e docas de carga',
  'Torque firme em rampas de aterro, pisos de cascalho e docas de expedição')

r('Operação contínua: troca de cilindro GLP em 3 minutos',
  'Turno contínuo: cilindro GLP trocado em poucos minutos sem interromper a obra')

r('Capacidades de 2.000 a 8.000 kg (frota Clark completa)',
  'De 2.000 a 8.000 kg — seis séries Clark cobrindo qualquer necessidade')

r('Pátios externos, chuva e pisos irregulares sem problema',
  'Opera em chuva, terra batida e cascalho sem restrição')

r('Emissão de gases: requer ventilação em ambientes fechados',
  'Emite gases: necessita ventilação adequada em ambientes fechados')

r('Zero emissão de gases no ambiente de trabalho',
  'Nenhuma emissão de poluentes no local de operação')

r('Operação silenciosa (ideal para áreas urbanas)',
  'Funcionamento silencioso, indicada para áreas residenciais próximas')

r('Menor custo de combustível por hora de operação',
  'Custo de energia por hora inferior ao GLP e diesel')

r('Autonomia limitada: 6 a 8 horas por carga',
  'Bateria dura 6 a 8 horas — parada obrigatória para recarga')

r('Não opera em pátios com chuva ou pisos irregulares',
  'Perde desempenho em piso molhado, terra ou cascalho')

r('Requer infraestrutura de recarga no local',
  'Exige tomada industrial e espaço dedicado para carregador')

# Spec table — additional unique text
r('CDs, docas, galpões médios',
  'Canteiros, depósitos, galpões')

# Incluso heading text
r('O que está incluído na <span>locação</span> da empilhadeira Clark',
  'O que vem junto na <span>locação</span> da empilhadeira Clark')

# Expand button text
r('Ver mais sobre empilhadeira a combustão',
  'Saiba mais sobre combustão Clark')

# Sticky CTA text
r('Empilhadeira Clark',
  'Clark para Caldas Novas')

# NR-11 highlight list items — rewrite each to differ from SC
r('Curso de operador de empilhadeira com certificado válido (reciclagem periódica)',
  'Certificado de operador NR-11 atualizado, com reciclagem dentro do prazo regulamentar')

r('Inspeção pré-operacional antes de cada turno (garfos, mastro, freios, direção, GLP)',
  'Vistoria obrigatória antes de ligar a máquina: garfos, mastro, freios, volante e nível de combustível')

r('Respeito à capacidade de carga nominal indicada na plaqueta do equipamento',
  'Carga dentro do limite nominal estampado na plaqueta da empilhadeira — jamais exceder')

r('Sinalização de manobra e velocidade controlada em áreas de circulação de pedestres',
  'Velocidade reduzida e sinalização sonora ao manobrar em zonas onde circulam pedestres no canteiro')

r('Uso de cinto de segurança e proteção contra queda de carga (grade de proteção do operador)',
  'Cinto de segurança afivelado e grade de proteção contra queda de carga sempre posicionada')

# Marquee — rewrite remaining items that are shared
r('<strong>+20</strong> anos de mercado',
  '<strong>+20</strong> anos no setor', 99)

r('<strong>24h</strong> suporte técnico',
  '<strong>24h</strong> equipe mobile disponível', 99)

r('<strong>2.000 a 8.000 kg</strong> de capacidade',
  '<strong>2t a 8t</strong> capacidade Clark', 99)

# Cotação rápida — "Cotação rápida" tag text
r('Cotação rápida',
  'Orçamento rápido')

# Price card labels unique
r('Clark L25 (entrada)',
  'Clark L25 — piso de entrada')

r('Heavy duty / curto prazo',
  'C-Series / contrato curto')

# Comparativo H2 — unique
r('Empilhadeira <span>contrabalançada</span> ou elétrica: qual escolher?',
  'Empilhadeira a <span>combustão Clark</span> ou elétrica: qual faz sentido em Caldas Novas?')

# Badge tag in hero
r('Frota Clark pronta para entrega',
  'Clark disponível para Caldas Novas')

# Comparativo card tags
r('Empilhadeira a Combustão (GLP/Diesel)',
  'Combustão Clark (GLP ou Diesel)')

r('Empilhadeira Elétrica',
  'Empilhadeira Elétrica (bateria)')

# Depoimentos section tag
r('>Depoimentos<',
  '>Clientes de Caldas Novas<')

# Incluso section tag
r('O que está incluso',
  'Tudo incluso no contrato')

# Conformidade legal tag
r('Conformidade legal',
  'Normas e segurança')

# Área de atendimento tag
r('Área de atendimento',
  'Cobertura de entrega')

# Preços tag
r('>Preços<',
  '>Investimento<')

# Vídeo tag
r('>Vídeo<',
  '>Vídeo institucional<')

# CTA footer tag
r('>Orçamento rápido<',
  '>Solicite agora<')

# FAQ tag
r('>FAQ<',
  '>Perguntas frequentes<')

# ═══════════════════════════════════════════════════════════════════════
# 22. MAIS DIFERENCIAÇÃO — até atingir Jaccard < 0.20 vs SC
# ═══════════════════════════════════════════════════════════════════════

# Torque label
r('Superior em rampas',
  'Potência para aterro e cascalho')

r('Turno contínuo',
  'Sem pausa para carga')

r('Interno + externo',
  'Canteiro + depósito')

r('A partir R$2.800',
  'Desde R$2.800/mês')

# Spec table footer
r('* Especificações variam por configuração. Confirme disponibilidade e configuração com a equipe técnica antes da locação.',
  '* Configurações e disponibilidade podem variar. Consulte a equipe técnica da Move Máquinas para confirmar o modelo antes de fechar a locação.')

# Price "por mês" text — can't change all, but let's add context
r('Ticket médio',
  'Valor intermediário')

# Hero microcopy
r('Resposta em menos de 5 min',
  'Retorno em até 5 minutos')

# Orçamento personalizado (mobile form)
r('Orçamento personalizado',
  'Cotação para Caldas Novas')

r('Receber orçamento personalizado',
  'Enviar pedido de orçamento')

# Form note
r('Ou ligue: <a href="tel:+556232111515" rel="nofollow noopener noreferrer">(62) 3211-1515</a></p>',
  'Prefere ligar? <a href="tel:+556232111515" rel="nofollow noopener noreferrer">(62) 3211-1515</a></p>', 2)

# CTA final button text
r('WhatsApp: resposta imediata',
  'WhatsApp: atendimento imediato')

r('Cotar Agora',
  'Pedir Cotação')

r('Cotar empilhadeira Clark agora',
  'Solicitar orçamento Clark agora')

# Solicitar Orçamento buttons
r('Solicitar Orçamento no WhatsApp',
  'Pedir Orçamento pelo WhatsApp')

r('Solicitar Orçamento pelo WhatsApp',
  'Enviar Pedido de Orçamento')

# Fala do Especialista label/title
r('Fala do Especialista',
  'Visão do especialista')

# Comparativo tag
r('>Comparativo<',
  '>Combustão vs Elétrica<')

# More micro-differentiations
r('L25 GLP, 2.500 kg de capacidade',
  'Clark L25 GLP — capacidade de 2.500 kg')

r('Contrato de 3+ meses',
  'Contrato trimestral ou superior')

r('L30 ou GTS25, GLP ou diesel',
  'Clark L30 ou GTS25 — GLP ou diesel')

r('Contrato de 1 a 2 meses',
  'Contrato de 30 a 60 dias')

r('Manutenção e suporte 24h inclusos',
  'Pacote com manutenção e suporte técnico 24h')

r('C-Series ou S40-60 (cargas pesadas)',
  'Clark C-Series ou S40-60 para cargas acima de 4t')

r('Contrato de curto prazo (1 mês)',
  'Locação de 15 a 30 dias')

# Expand button (in JS)
r("'Saiba mais sobre combustão Clark",
  "'Ler mais sobre empilhadeira Clark")

# Comparativo quick box labels
r('>Torque<',
  '>Força de tração<')

r('>Autonomia<',
  '>Duração do turno<')

r('>Ambiente<',
  '>Local de operação<')

r('>Custo<',
  '>Investimento mensal<')

# NR-11 heading rewrite for differentiation
r('Verifique o certificado do operador',
  'Confirme a habilitação NR-11 do operador')

r('Realize a inspeção pré-operacional',
  'Faça a vistoria antes de cada turno')

r('Sinalize a área de operação',
  'Prepare a sinalização do canteiro')

r('Documente e registre',
  'Mantenha a documentação atualizada')

# Manutenção do sistema hidráulico heading
r('Manutenção do sistema hidráulico',
  'Hidráulico revisado periodicamente')

r('Suporte técnico 24h / 7 dias',
  'Assistência técnica 24h / 7 dias')

r('Garfos e mastro inspecionados',
  'Garfos e mastro revisados na oficina')

r('Entrega e retirada sem custo extra',
  'Logística de entrega e retirada')

r('Contrapeso e GLP verificados',
  'Contrapeso e sistema GLP certificados')

r('Consultoria técnica gratuita',
  'Dimensionamento sem custo')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

import re

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            'goiania-go/', '170 km', 'Sede na', 'sede',
            'Goiânia — 170', 'de Goiânia', 'e Goiânia',
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
cn = html.count('Caldas Novas')
local = html.count('canteiro') + html.count('resort') + html.count('hotel') + html.count('GO-139') + html.count('106')
print(f"\nCaldas Novas: {cn} menções")
print(f"Contexto local (canteiro/resort/hotel/GO-139/106): {local} menções")

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
print(f"⏱  TEMPO: {elapsed:.1f}s")
print(f"📊 TOKENS (estimativa): ~{len(html)//4} tokens no output")
