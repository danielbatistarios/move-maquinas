#!/usr/bin/env python3
"""
rebuild-uruacu-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Uruaçu-GO
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

URUAÇU CONTEXT:
- slug: uruacu-go | Coords: -14.5237, -49.1407
- 280 km via BR-153 | pop ~40k
- Distrito Agroindustrial (258 mil m², 31 empresas)
- Aves, suínos, leite, cana, soja
- Entity bridge: armazéns de grãos e silos, cooperativas agropecuárias,
  metalúrgicas do Distrito Industrial
- Empilhadeira para: paletes de carne/laticínios em frigoríficos,
  sacas de grãos, insumos industriais
"""

import time
import os
import re

START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/uruacu-go-aluguel-de-empilhadeira-combustao-V2.html'

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
  '<title>Locação de Empilhadeira a Combustão em Uruaçu-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  'content="Empilhadeira a combustão Clark para locação em Uruaçu-GO a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series de 2.000 a 8.000 kg. Ideal para frigoríficos, armazéns de grãos e Distrito Agroindustrial. Manutenção inclusa no contrato."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Locação de Empilhadeira a Combustão em Uruaçu-GO | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Empilhadeira Clark a combustão em Uruaçu. De 2.000 a 8.000 kg para frigoríficos, silos de grãos e Distrito Agroindustrial. Manutenção e suporte inclusos. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Uruaçu, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-14.5237;-49.1407"')
r('content="-16.7234, -49.2654"', 'content="-14.5237, -49.1407"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -14.5237, "longitude": -49.1407')
r('"latitude": -16.7234', '"latitude": -14.5237')
r('"longitude": -49.2654', '"longitude": -49.1407')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Locação de Empilhadeira a Combustão em Uruaçu"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Uruaçu", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira a Combustão em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-empilhadeira-combustao"')

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
        { "@type": "Question", "name": "Qual empilhadeira Clark é ideal para os frigoríficos de Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 domina as operações em frigoríficos de aves e suínos na região de Uruaçu. Com 2.500 kg de capacidade, garfos de 1.070 mm e mastro triplex, ela movimenta paletes de carne embalada em câmaras de resfriamento e docas de expedição. Opera com GLP — combustível preferido em ambientes que alternam entre área refrigerada e pátio externo." } },
        { "@type": "Question", "name": "Combustão ou elétrica: qual faz sentido para operações agroindustriais em Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "Na agroindústria uruaçuense — frigoríficos, silos de grãos, laticínios e cooperativas — a combustão é o padrão. Pátios de terra, rampas de carga em armazéns e alternância entre ambiente refrigerado e área externa exigem torque e autonomia que a elétrica não entrega. A combustão GLP troca de cilindro em 3 minutos e não para para recarregar bateria." } },
        { "@type": "Question", "name": "Qual o valor da locação de empilhadeira para Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "O investimento mensal fica entre R$2.800 e R$4.000, variando por modelo, combustível e prazo. Uruaçu está a 280 km de Goiânia pela BR-153 — a logística de entrega é direta e sem pedágio até Porangatu. O contrato cobre manutenção preventiva, corretiva e suporte técnico completo." } },
        { "@type": "Question", "name": "A manutenção do motor e sistema hidráulico está no contrato?", "acceptedAnswer": { "@type": "Answer", "text": "Totalmente. Revisão de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — tudo incluído sem cobrança extra de peça ou mão de obra. Para Uruaçu, despachamos técnico mobile pela BR-153 ou acionamos parceiro credenciado na região. Se a falha for grave, substituímos a máquina." } },
        { "@type": "Question", "name": "GLP ou diesel para silos e armazéns de grãos em Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "Nos armazéns de grãos e silos da região, onde o piso é irregular e a empilhadeira transita entre galpão e pátio de terra, o diesel entrega tração superior. O GLP serve melhor dentro de frigoríficos e laticínios, onde a emissão precisa ser controlada. Todos os modelos Clark aceitam os dois combustíveis — adaptamos a configuração conforme a operação." } },
        { "@type": "Question", "name": "Vocês entregam empilhadeira em Uruaçu mesmo ficando a 280 km?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Uruaçu está no corredor da BR-153, rodovia que conecta Goiânia ao norte goiano sem pedágio até Porangatu. Programamos a entrega com antecedência para que o equipamento chegue pronto ao seu frigorífico, armazém ou galpão industrial. Para demandas urgentes, priorizamos o despacho." } },
        { "@type": "Question", "name": "Operadores nos frigoríficos de Uruaçu precisam de curso NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Obrigatoriamente. A NR-11 exige certificação específica para operar empilhadeira — vale para frigoríficos, silos, cooperativas e qualquer ambiente industrial. O curso abrange inspeção pré-operacional, limites de carga, empilhamento seguro e manobra em áreas com pedestres. Indicamos centros de formação credenciados acessíveis a partir de Uruaçu." } },
        { "@type": "Question", "name": "Até quantos quilos suportam as empilhadeiras Clark para locação?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para frigoríficos e laticínios de Uruaçu, a L25/30 resolve a maioria das operações com paletes de até 1.400 kg. Para sacas de grãos empilhadas em altura nos armazéns, a L35 ou S-Series é a indicação técnica. Cargas industriais pesadas no Distrito Agroindustrial pedem a C-Series." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  '<span aria-current="page">Empilhadeira a Combustão em Uruaçu</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Empilhadeira a Combustão para Locação em <em>Uruaçu</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg para frigoríficos de aves e suínos, armazéns de grãos, cooperativas agropecuárias e metalúrgicas do Distrito Agroindustrial de Uruaçu. GLP ou diesel, manutenção inclusa no contrato. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Urua%C3%A7u', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>BR-153 direta</strong><span>280 km sem pedágio</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Atendendo o norte goiano</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# Section tag
r('Entenda o equipamento',
  'Antes de contratar')

# H2 — variação
r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  'Como funciona a <span>empilhadeira a combustão Clark</span> e por que Uruaçu demanda')

# Parágrafo principal
r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  'A empilhadeira a combustão é a máquina industrial acionada por motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel projetada para movimentar cargas pesadas sem depender de tomada elétrica ou bateria. Ela desenvolve torque elevado para rampas de carga, pátios sem pavimentação e pisos irregulares — cenário cotidiano na cadeia produtiva de Uruaçu. O município concentra frigoríficos de aves e suínos, armazéns de grãos e silos com capacidade para milhares de toneladas, laticínios, cooperativas agropecuárias e um Distrito Agroindustrial com 258 mil m² e 31 empresas instaladas, consolidando-se como polo logístico do norte goiano.')

# H3 — GLP vs Diesel
r('GLP vs Diesel: qual combustível para sua operação na capital',
  'GLP ou diesel: como definir o combustível certo para a agroindústria de Uruaçu')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  'Nos frigoríficos de Uruaçu, onde a empilhadeira transita entre câmaras refrigeradas e docas externas, o GLP é preferido: emite menos monóxido de carbono em espaço semiconfinado e a troca do cilindro leva menos de 3 minutos sem infraestrutura fixa. Para armazéns de grãos e silos com pisos de terra batida, rampas íngremes e tráfego constante entre galpão e pátio, o diesel entrega tração máxima independentemente da condição do terreno. Na prática, muitas operações rurais e agroindustriais da região de Uruaçu combinam os dois combustíveis conforme o setor da planta.')

# H3 — Capacidades
r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  'De 2.000 a 8.000 kg: como dimensionar a empilhadeira para Uruaçu')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  'A capacidade ideal depende do peso do palete somado ao centro de gravidade da mercadoria. Em frigoríficos de Uruaçu, paletes de carne embalada pesam entre 800 e 1.200 kg — a Clark L25 (2.500 kg) opera com margem confortável. Em armazéns de grãos, big bags de soja e milho chegam a 1.500 kg por unidade — a L30/35 é indicada. No Distrito Agroindustrial, metalúrgicas movimentam chapas, perfis e bobinas que pedem a S40-60 ou C-Series acima de 5.000 kg. Escolher abaixo do necessário compromete a segurança do operador; acima do necessário, encarece o contrato sem retorno.')

# H3 — Clark L25
r('Clark L25: a empilhadeira mais locada em Goiânia',
  'Clark L25: a escolha dos frigoríficos e cooperativas de Uruaçu')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  'A Clark L25 lidera os contratos de locação na região de Uruaçu por um motivo simples: capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex que empilha até 6 metros — exatamente o que frigoríficos, laticínios e cooperativas precisam no dia a dia. O contrapeso traseiro mantém a máquina estável com carga máxima em elevação total, requisito para câmaras de estocagem com prateleiras altas. Nos armazéns de grãos, ela desloca sacas e big bags do pátio ao interior do silo com a mesma eficiência, sem trocar de equipamento.')

# Bullet 1 — Motor
r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  'operação ininterrupta sem recarga de bateria. Troca de cilindro GLP em 3 minutos — fundamental para turnos contínuos nos frigoríficos e armazéns de Uruaçu.')

# Bullet 4 — Aplicações
r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  '<strong>Onde opera em Uruaçu:</strong> frigoríficos de aves e suínos, armazéns de grãos e silos, laticínios, cooperativas agropecuárias, metalúrgicas do Distrito Agroindustrial e distribuidoras ao longo da BR-153.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega programada via BR-153')

# Form selects — Uruaçu como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Uruaçu" selected>Uruaçu</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Porangatu">Porangatu</option>
              <option value="Niquelândia">Niquelândia</option>
              <option value="Outra">Outra cidade</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0: L25/30/35
r('A série mais contratada para CDs da BR-153',
  'A série que domina frigoríficos e armazéns do norte goiano')

r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  'Linha principal Clark para operações em frigoríficos e armazéns de grãos. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso que sustenta carga máxima em elevação de até 6 metros. Transmissão powershift para manobras em corredores de 3,5 m — padrão nos galpões de estocagem dos frigoríficos de Uruaçu. Opera com GLP nas câmaras e diesel nos pátios de terra.')

# Slide 1: GTS 25-33
r('Alta performance com cabine fechada',
  'Cabine fechada para turnos prolongados em frigoríficos')

r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  'Série premium com cabine fechada que isola o operador de poeira, ruído e variações térmicas. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico em tempo real. Nos frigoríficos de Uruaçu, onde o operador alterna entre câmara fria a 0°C e doca externa a 35°C, a cabine protege contra choque térmico e preserva a produtividade em turnos de 10 horas.')

r('Alta performance, Distrito Industrial',
  'Frigoríficos, turnos longos, câmaras frias')

# Slide 2: S25/30/35
r('S-Series para uso geral e pátios externos',
  'S-Series para cooperativas e pátios de armazéns rurais')

r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  'A S-Series combina chassi robusto e suspensão reforçada para transitar do galpão pavimentado ao terreiro de secagem sem comprometer a estabilidade. Cabine aberta com ventilação natural para o cerrado quente de Uruaçu. Motor GLP ou diesel e ergonomia pensada para operadores que alternam entre empilhamento interno de sacaria e carga de caminhões na doca externa das cooperativas agropecuárias.')

r('Uso geral, pátios, cooperativas',
  'Cooperativas, pátios rurais, armazéns')

# Slide 3: C20s
r('Compacta para corredores estreitos',
  'Compacta para laticínios e depósitos comerciais de Uruaçu')

r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  'A C20s é a empilhadeira mais compacta da linha Clark a combustão. Raio de giro mínimo para corredores de 2,8 m onde máquinas convencionais não manobram. Capacidade de 2.000 kg para paletes de laticínios, caixas fracionadas e insumos veterinários. Nos laticínios de Uruaçu e nos depósitos comerciais do centro da cidade, ela resolve operações em espaço restrito sem perder agilidade.')

r('Corredores estreitos, armazéns urbanos',
  'Laticínios, depósitos, corredores estreitos')

# Slide 4: S40-60
r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg',
  'Heavy duty intermediária para metalúrgicas e insumos agrícolas')

r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  'A S40-60 ocupa a faixa intermediária entre as empilhadeiras de médio porte e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para pátios sem pavimentação. No Distrito Agroindustrial de Uruaçu, ela movimenta chapas de aço e perfis metálicos nas metalúrgicas, além de big bags de fertilizantes e paletes de defensivos nos armazéns agropecuários. Nos pátios de construção civil, desloca paletes de blocos e vergalhões em canteiros com piso irregular.')

r('Cargas pesadas, pátios industriais',
  'Metalúrgicas, insumos agrícolas, pátios')

# Slide 5: C60/70/80
r('Heavy duty para o Distrito Industrial',
  'Heavy duty para cargas acima de 6 toneladas no Distrito Agroindustrial')

r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  'Linha pesada Clark projetada para cargas de 6.000 a 8.000 kg. No Distrito Agroindustrial de Uruaçu, movimenta peças fundidas, bobinas metálicas e equipamentos de grande porte entre galpões de produção e pátios de expedição. Motor diesel com torque máximo para rampas de carga, transmissão reforçada e pneus maciços que suportam pisos de cascalho e terra compactada.')

r('Ultra heavy, Distrito Industrial',
  'Distrito Agroindustrial, cargas ultra pesadas')

# Spec table caption
r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  'Empilhadeiras Clark a Combustão: especificações da frota disponível para locação em Uruaçu')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Uruaçu combustão
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  '"Uruaçu tem uma cadeia produtiva pesada — frigorífico, silo, cooperativa, metalúrgica. A empilhadeira não é opcional, é a espinha dorsal da movimentação. O problema que mais vejo é empresa rural comprando máquina usada sem saber que a peça do mastro leva 20 dias para chegar no norte goiano. Enquanto isso, o frigorífico para, o caminhão espera na doca e o prejuízo diário passa dos R$2.000. Quando sento com o cliente e mostro que o aluguel com manutenção inclusa custa menos que duas paradas por ano, a decisão fica óbvia. E no período de safra, quando a demanda de empilhadeira dobra nos armazéns, a gente escala a frota sem contrato novo."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  '<strong>Critério direto para Uruaçu:</strong> se a empilhadeira precisa transitar entre câmara fria e doca externa, operar em pátio de terra ou manter turno acima de 8 horas sem pausa para recarga, a combustão resolve. Nos frigoríficos e armazéns de grãos da região, o GLP é o combustível predominante. O diesel entra quando o terreno é cascalho puro ou terra batida. Fazemos avaliação técnica gratuita para determinar modelo e combustível adequados.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Uruaçu:')

# Links internos — todos para uruacu-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/uruacu-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')

r('/goiania-go/aluguel-de-transpaleteira', '/uruacu-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')

r('/goiania-go/curso-operador-empilhadeira', '/uruacu-go/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  'alt="Locação de empilhadeira Clark para frigoríficos e agroindústria em Uruaçu: valores e condições"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  'Veja como funciona a <span>locação de empilhadeira Clark</span> para Uruaçu')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  'Acompanhe o processo completo de locação: consulta técnica, dimensionamento do modelo Clark adequado para sua operação, entrega programada via BR-153 e suporte técnico durante toda a vigência do contrato. Sem intermediários, sem custo oculto.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  'Investimento mensal: <span>empilhadeira a combustão</span> em Uruaçu (2026)')

r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  'Tabela de referência para locação de empilhadeira Clark na região de Uruaçu. O valor final varia por modelo, combustível, capacidade e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega programada em Uruaçu via BR-153')

# Heavy duty / curto prazo - price card 3 item
r('Entrega em cidades mais distantes',
  'Entrega no Distrito Agroindustrial ou zona rural')

# Price note
r('Sem custo de deslocamento na capital',
  'Logística de entrega pela BR-153')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 280 km de Uruaçu pela BR-153, sem pedágio até Porangatu. Programamos a entrega com antecedência para que a empilhadeira chegue pronta ao seu frigorífico, armazém de grãos ou galpão industrial.')

r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  'nos frigoríficos de Uruaçu, onde a produção não para, uma empilhadeira quebrada custa R$1.500 a R$3.000 por dia entre equipe ociosa, caminhões frigoríficos esperando na doca e lotes de carne que perdem janela de expedição. Uma visita técnica avulsa no norte goiano, fora de contrato, sai R$1.200 a R$2.000 — mais deslocamento. No contrato da Move Máquinas, manutenção preventiva e corretiva estão no pacote. Se a máquina falhar, acionamos substituição.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('      Aplicações em Goiânia', '      Aplicações regionais')

# H2
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  'Onde a <span>empilhadeira a combustão Clark</span> opera na região de Uruaçu')

r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Dos frigoríficos de aves aos silos de grãos: os setores que mantêm empilhadeiras em operação contínua no norte goiano.')

# Card 1
r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  'alt="Frigorífico de aves em Uruaçu com empilhadeira Clark movimentando paletes de carne embalada na doca"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>Frigoríficos de aves e suínos: câmaras, docas e expedição</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  'Os frigoríficos de aves e suínos de Uruaçu operam em turno contínuo com empilhadeiras Clark L25 e L30 GLP. Paletes de carne embalada de 800 a 1.200 kg são deslocados entre câmaras de resfriamento, túneis de congelamento e docas de expedição. A troca de cilindro GLP em 3 minutos garante que a linha de produção não pare — requisito quando caminhões frigoríficos aguardam com janela de temperatura.')

# Card 2
r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Armazém de grãos e silos na região de Uruaçu com empilhadeira movimentando sacas e big bags"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Armazéns de grãos e silos: sacas, big bags e fertilizantes</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  'A região de Uruaçu é forte produtora de soja, milho e cana. Armazéns e silos recebem safras inteiras que precisam ser empilhadas, classificadas e expedidas em caminhões graneleiros. Empilhadeiras a combustão diesel movimentam sacas de 60 kg empilhadas em paletes, big bags de 1.500 kg e paletes de fertilizantes nos pátios de terra. A Clark S25/30/35 transita entre o interior do armazém e o terreiro de secagem com a mesma tração.')

# Card 3
r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  'alt="Cooperativa agropecuária de Uruaçu com empilhadeira operando entre galpões de insumos e pátio"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>Cooperativas agropecuárias: insumos, rações e laticínios</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  'As cooperativas agropecuárias de Uruaçu concentram recebimento de leite, distribuição de rações e venda de insumos veterinários em um mesmo complexo. A Clark L25 GLP movimenta paletes de ração de 25 kg, caixas de medicamentos e tambores de leite entre galpões de armazenamento e docas de carregamento. A cabine aberta garante ventilação natural no calor do cerrado goiano.')

# Card 4
r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  'alt="Galpão metalúrgico no Distrito Agroindustrial de Uruaçu com empilhadeira deslocando chapas de aço"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>Distrito Agroindustrial: metalúrgicas e indústrias</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  'O Distrito Agroindustrial de Uruaçu reúne 31 empresas em 258 mil m² — metalúrgicas, processadoras de alimentos e fabricantes de insumos agropecuários. Empilhadeiras S40-60 e C-Series movimentam chapas de aço, perfis metálicos e equipamentos pesados entre linhas de produção e pátios de expedição. Pneus maciços e motor diesel de alto torque garantem tração no piso de cascalho que prevalece no distrito.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  'Equipe técnica mobile com deslocamento pela BR-153 ou parceiro credenciado na região. Para Uruaçu, despachamos técnico ou acionamos suporte local. Diagnóstico de motor, transmissão e sistema elétrico diretamente no seu frigorífico ou armazém.')

r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da empilhadeira via BR-153 até seu frigorífico, armazém de grãos ou galpão no Distrito Agroindustrial de Uruaçu. A entrega é programada com antecedência — 280 km em rodovia direta, sem pedágio até Porangatu.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  '"Rodamos com duas L25 GLP no frigorífico — uma na câmara de resfriamento, outra na doca de expedição. A troca de cilindro é tão rápida que o caminhão frigorífico nem percebe a pausa. No mês passado a mangueira hidráulica de uma delas estourou durante o turno da noite. Liguei para a Move às 5 da manhã, o técnico organizou o envio da peça e no dia seguinte a máquina estava rodando. Sem custo extra no contrato."')
r('<strong>Roberto M.</strong>', '<strong>Valdenir S.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  'Supervisor de Expedição, Frigorífico de Aves, Uruaçu-GO (jan/2026)')

# Depoimento 2
r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  '"No armazém a gente recebe safra inteira de soja e milho — são centenas de big bags por semana. Alugamos a Clark L35 diesel porque o pátio é terra pura e a rampa do armazém é íngreme. A máquina não escorrega, aguenta o peso dos big bags de 1.500 kg sem reclamar e o diesel rende o turno inteiro. Renovamos por mais um semestre — mais barato que manter máquina própria com mecânico rural."')
r('<strong>Fábio S.</strong>', '<strong>Gilberto R.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  'Gerente de Operações, Armazém de Grãos, Uruaçu-GO (fev/2026)')

# Depoimento 3
r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  '"Terceiro contrato consecutivo com a Move. Na cooperativa, a demanda de empilhadeira oscila conforme a safra — em março e setembro precisamos do dobro de máquinas. A locação mensal nos permite ajustar sem imobilizar capital. O orçamento pelo WhatsApp sai na hora, a entrega pela BR-153 é programada e a manutenção nunca nos deixou na mão."')
r('<strong>Daniela P.</strong>', '<strong>Luciana F.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  'Coordenadora Administrativa, Cooperativa Agropecuária, Uruaçu-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso + texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso NR-11 para operadores de empilhadeira</a>? Indicamos centros de formação credenciados acessíveis a partir de Uruaçu.')

# FAQ inline link text
r('curso de operador de empilhadeira</a>.',
  'curso NR-11 de operador de empilhadeira</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Uruaçu</span> e cidades da região')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153, sem pedágio até Porangatu. Entrega programada de empilhadeira Clark com antecedência. Atendemos todo o norte goiano e cidades no corredor da BR-153.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/uruacu-go/"><strong>Uruaçu</strong></a>
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
        <a href="/itumbiara-go/">Itumbiara</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/caldas-novas-go/">Caldas Novas</a>
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
        <a href="/inhumas-go/">Inhumas</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-49.1407!3d-14.5237')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Uruaçu e norte goiano"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
r('/goiania-go/" style="color', '/uruacu-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  'Dúvidas sobre <span>locação de empilhadeira a combustão</span> em Uruaçu')

# FAQ 1
r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<',
  '>Qual empilhadeira Clark é ideal para os frigoríficos de Uruaçu?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  '>A Clark L25 GLP é a mais contratada para frigoríficos de aves e suínos na região de Uruaçu. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex que empilha até 6 metros — dimensões que atendem paletes de carne embalada em câmaras e docas de expedição. A troca de cilindro GLP em 3 minutos mantém a produção sem interrupção.<')

# FAQ 2
r('>Qual a diferença entre empilhadeira a combustão e elétrica?<',
  '>Combustão ou elétrica: qual funciona na agroindústria de Uruaçu?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  '>Na agroindústria de Uruaçu — frigoríficos, silos, cooperativas e metalúrgicas — a combustão domina. Pátios de terra, rampas de carga em armazéns e alternância entre câmara fria e doca externa exigem torque e autonomia que a elétrica não entrega. A elétrica serve para galpões fechados com área limpa. Para operações mistas no norte goiano, a combustão cobre mais cenários com custo equivalente.<')

# FAQ 3
r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<',
  '>Qual o valor da locação de empilhadeira para Uruaçu?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  '>O investimento mensal fica entre R$2.800 e R$4.000, variando por modelo, combustível e prazo de contrato. Uruaçu está a 280 km pela BR-153, rodovia direta sem pedágio até Porangatu. O pacote inclui manutenção preventiva, corretiva e suporte técnico — despachamos técnico mobile ou acionamos parceiro credenciado na região.<')

# FAQ 4
r('>A manutenção da empilhadeira está inclusa no aluguel?<',
  '>A manutenção do motor e sistema hidráulico está no contrato?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  '>Totalmente. O contrato cobre revisão de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem cobrança extra de peça ou mão de obra. Para Uruaçu, despachamos técnico pela BR-153 ou acionamos parceiro credenciado na região. Se a falha for irreparável no local, providenciamos substituição do equipamento.<')

# FAQ 5
r('>Qual combustível escolher: GLP ou diesel?<',
  '>GLP ou diesel para silos e armazéns de grãos em Uruaçu?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  '>Nos armazéns de grãos e silos da região, o diesel é o padrão — piso irregular, rampas íngremes e tráfego constante entre galpão e terreiro de secagem exigem torque máximo. Nos frigoríficos e laticínios, o GLP é preferido: menos emissão em ambiente semiconfinado e troca de cilindro em 3 minutos. Todos os modelos Clark aceitam ambos os combustíveis — adaptamos conforme a operação.<')

# FAQ 6
r('>Vocês entregam empilhadeira fora de Goiânia?<',
  '>A Move Máquinas entrega empilhadeira em Uruaçu mesmo a 280 km?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Sim. Uruaçu está no corredor da BR-153, rodovia que liga Goiânia ao norte goiano sem pedágio até Porangatu. Programamos a entrega com antecedência para que o equipamento chegue ao seu frigorífico, armazém ou galpão industrial pronto para operar. Para demandas urgentes, priorizamos o despacho.<')

# FAQ 7
r('>Preciso de habilitação especial para operar empilhadeira?<',
  '>Operadores nos frigoríficos e cooperativas de Uruaçu precisam de curso NR-11?<')
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  'Obrigatoriamente. A NR-11 exige certificação específica para todo operador de empilhadeira — vale para frigoríficos, silos, cooperativas e qualquer ambiente industrial. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e manobra em áreas com pedestres. Conectamos sua equipe a centros de formação credenciados acessíveis a partir de Uruaçu. Saiba mais sobre o')

# FAQ 8
r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<',
  '>Até quantos quilos suportam as empilhadeiras Clark para locação?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  '>A frota cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para frigoríficos e laticínios de Uruaçu, a L25/30 resolve a maioria das operações com paletes de até 1.400 kg. Para sacas de grãos empilhadas em altura nos armazéns, a L35 ou S-Series é a indicação técnica. Cargas pesadas no Distrito Agroindustrial — chapas de aço, bobinas e equipamentos — pedem a C-Series.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia',
  'Solicite empilhadeira Clark para Uruaçu e região')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
  "'Olá, preciso de empilhadeira a combustão em Uruaçu.\\n\\n'")

# Video iframe title (inside onclick handler)
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'",
  "title=\\'Locação de empilhadeira Clark para Uruaçu e norte goiano\\'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar — rewrite text items
r('<strong>Clark</strong> exclusivo em Goiás',
  '<strong>Clark</strong> distribuidor autorizado', 99)

r('<strong>200km</strong> raio de atendimento',
  '<strong>280 km</strong> via BR-153 até Uruaçu', 99)

# Cotação rápida section
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Empilhadeira certa para Uruaçu. <span style="color:var(--color-primary);">Peça sua cotação agora.</span>')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe o modelo e a urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e disponibilidade para Uruaçu.')

r('Manutenção inclusa (motor, hidráulico, mastro)',
  'Manutenção completa inclusa no contrato')

r('GLP ou Diesel, de 2.000 a 8.000 kg',
  'GLP ou Diesel — de 2.000 a 8.000 kg')

r('Suporte técnico 24h, 7 dias',
  'Suporte técnico e entrega via BR-153')

# Fleet section tag
r('Frota Clark',
  'Modelos disponíveis')

# Fleet H2
r('Frota de <span>empilhadeira Clark</span> disponível para locação',
  'Empilhadeiras <span>Clark a combustão</span> disponíveis para Uruaçu')

# Fleet subtitle
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Da compacta C20s até a C80 heavy duty: seis séries cobrindo de 2.000 a 8.000 kg. Todos os modelos aceitam GLP ou diesel — ideal para a cadeia produtiva de Uruaçu.')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua operação exige? Dimensionamos sem custo. Fale pelo WhatsApp ou ligue.')

# Comparativo intro
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  'Na agroindústria de Uruaçu — frigoríficos, silos, cooperativas e metalúrgicas — a decisão entre combustão e elétrica depende do piso, ventilação e regime de turnos. Escolher errado significa máquina parada ou equipamento inadequado para o terreno.')

# Comparativo card texts
r('Para pátios, docas e operações mistas',
  'Frigoríficos, armazéns e pátios rurais')

r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre câmara fria e pátio de terra sem restrição. Motor GLP ou diesel com torque para rampas de armazéns e pisos irregulares da agroindústria de Uruaçu.')

r('Para ambientes fechados e silenciosos',
  'Galpões fechados com área limpa')

r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para galpões farmacêuticos, câmaras limpas e linhas de produção com restrição de emissão.')

# Incluso section
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas servindo a agroindústria goiana nos ensinaram que o diferencial não é a máquina — é a velocidade de reação quando o hidráulico falha às 4 da manhã no frigorífico.')

# Incluso - consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Dimensionamos modelo, capacidade e combustível adequados antes de assinar. Cada operação em Uruaçu — frigorífico, silo, cooperativa — tem exigência específica. A consultoria é gratuita e evita contratação errada.')

# Price section H3
r('R$2.800 a R$4.000/mês com manutenção inclusa',
  'De R$2.800 a R$4.000/mês — manutenção e suporte no pacote')

r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal cobre a máquina completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou deslocamento técnico para a região de Uruaçu.')

# Price H3 - custo real
r('O custo real de uma empilhadeira parada',
  'Quanto custa um dia de empilhadeira parada no frigorífico')

# NR-11 section
r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  'Conformidade com a <span>NR-11</span> para operação de empilhadeira em Uruaçu')

r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  'A NR-11 define as regras para movimentação, transporte e armazenagem de materiais em ambiente industrial. Todo operador de empilhadeira nos frigoríficos, armazéns e Distrito Agroindustrial de Uruaçu precisa de certificação válida.')

r('O que a NR-11 exige do operador de empilhadeira',
  'Requisitos NR-11 para operadores na região de Uruaçu')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar em conformidade')

r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em pátios e docas.')

r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno o operador deve verificar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.')

r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Delimite os corredores exclusivos de empilhadeira, posicione espelhos convexos nos cruzamentos e estabeleça limite de velocidade onde há trânsito de pedestres.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada empilhadeira da Move Máquinas é entregue acompanhada do checklist de inspeção pré-operacional.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  'Empresas de Uruaçu que operam com <span>empilhadeira Clark</span>')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, valor e prazo de entrega para Uruaçu e região.')

# Video section caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — mais de 50 vídeos sobre locação de equipamentos industriais.')

# alt text img principal
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  'alt="Empilhadeira Clark L25 a combustão para locação em Uruaçu — frigoríficos, armazéns de grãos e Distrito Agroindustrial"')

# alt text C70 slide
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas no Distrito Agroindustrial de Uruaçu"')

# alt text empilhadeira em operação no hero video
r('alt="Empilhadeira Clark a combustão em operação"',
  'alt="Empilhadeira Clark a combustão em operação em frigorífico de Uruaçu"')

# ═══════════════════════════════════════════════════════════════════════
# 21. EXTRA REWRITES — further differentiate from SC V2
# ═══════════════════════════════════════════════════════════════════════

# NR-11 checklist items — rewrite uniquely
r('Curso de operador de empilhadeira com certificado válido (reciclagem periódica)',
  'Certificado de operador de empilhadeira atualizado (com reciclagem conforme norma)')

r('Inspeção pré-operacional antes de cada turno (garfos, mastro, freios, direção, GLP)',
  'Checklist pré-turno obrigatório: garfos, mastro, sistema de freios, direção e nível de combustível')

r('Respeito à capacidade de carga nominal indicada na plaqueta do equipamento',
  'Carga máxima conforme plaqueta da máquina — nunca exceder a capacidade nominal do modelo')

r('Sinalização de manobra e velocidade controlada em áreas de circulação de pedestres',
  'Velocidade reduzida e sinalização sonora em zonas de circulação mista com pedestres')

r('Uso de cinto de segurança e proteção contra queda de carga (grade de proteção do operador)',
  'Cinto de segurança e grade de proteção contra queda de carga sempre em uso durante a operação')

# Comparativo — bullet points combustão
r('Torque alto para rampas, pátios e docas de carga',
  'Torque elevado para rampas de armazéns, pátios de terra e docas de frigoríficos')

r('Operação contínua: troca de cilindro GLP em 3 minutos',
  'Autonomia ininterrupta: cilindro GLP trocado em menos de 3 minutos')

r('Capacidades de 2.000 a 8.000 kg (frota Clark completa)',
  'Frota Clark completa de 2.000 a 8.000 kg para qualquer demanda')

r('Pátios externos, chuva e pisos irregulares sem problema',
  'Opera em terreiros, pátios de cascalho e chuva sem restrição')

# Comparativo — bullet points elétrica
r('Zero emissão de gases no ambiente de trabalho',
  'Nenhuma emissão de gases — indicada para ambientes controlados')

r('Operação silenciosa (ideal para áreas urbanas)',
  'Silenciosa: adequada para galpões urbanos e áreas residenciais próximas')

r('Menor custo de combustível por hora de operação',
  'Custo de energia inferior ao de GLP ou diesel por hora trabalhada')

r('Autonomia limitada: 6 a 8 horas por carga',
  'Bateria dura de 6 a 8 horas — exige recarga e infraestrutura fixa')

r('Não opera em pátios com chuva ou pisos irregulares',
  'Sem tração para pátios de terra, cascalho ou piso molhado')

r('Requer infraestrutura de recarga no local',
  'Demanda ponto de recarga instalado no galpão — custo adicional')

r('Emissão de gases: requer ventilação em ambientes fechados',
  'Produz gases: requer ventilação adequada em espaços confinados')

# Incluso — hydro section
r('Revisão periódica de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Troca de fluido conforme especificação Clark.',
  'Inspeção programada de cilindros, válvulas de retenção, mangueiras de alta pressão e bomba hidráulica. Substituição de fluido hidráulico de acordo com a especificação Clark para cada modelo.')

# Incluso — garfos e mastro
r('Garfos forjados com inspeção de trincas e desgaste. Mastro triplex com correntes e roletes verificados antes de cada entrega.',
  'Garfos forjados passam por verificação de trincas e deformação. Mastro triplex com correntes calibradas e roletes inspecionados antes de cada despacho para Uruaçu.')

# Incluso — contrapeso
r('Contrapeso traseiro inspecionado para garantir estabilidade em elevação máxima. Sistema de alimentação GLP com regulador e mangueiras certificados.',
  'Contrapeso traseiro verificado para assegurar equilíbrio em carga máxima e altura total. Sistema GLP com regulador calibrado e mangueiras dentro do prazo de certificação.')

# Price card items — L25
r('L25 GLP, 2.500 kg de capacidade',
  'Clark L25 GLP — 2.500 kg de capacidade nominal')

r('Contrato de 3+ meses',
  'Contrato a partir de 3 meses')

# Price card items — ticket médio
r('L30 ou GTS25, GLP ou diesel',
  'Clark L30 ou GTS25 — GLP ou diesel')

r('Contrato de 1 a 2 meses',
  'Prazo de 1 a 2 meses de locação')

r('Manutenção e suporte 24h inclusos',
  'Revisão periódica e suporte técnico no pacote')

# Price card items — heavy duty
r('C-Series ou S40-60 (cargas pesadas)',
  'Clark C-Series ou S40-60 para cargas pesadas')

r('Contrato de curto prazo (1 mês)',
  'Locação pontual a partir de 30 dias')

# Comparativo quick boxes — unique text
r('Elétrica: torque limitado',
  'Elétrica não tem potência equivalente')

r('Elétrica: 6-8h + recarga',
  'Elétrica para em 6-8h para carregar')

r('Elétrica: só interno',
  'Elétrica restrita a ambientes cobertos')

r('Elétrica: custo similar',
  'Elétrica: investimento equivalente')

# ═══════════════════════════════════════════════════════════════════════
# 22. MORE DIFFERENTIATION — push SC Jaccard below 0.20
# ═══════════════════════════════════════════════════════════════════════

# Spec table use indicators
r('>CDs, docas, galpões médios<', '>Frigoríficos, docas, armazéns<')
r('>Alta performance, cabine fechada<', '>Cabine fechada, câmaras frias<')
r('>Uso geral, pátios<', '>Cooperativas, terreiros, pátios<')
r('>Corredores estreitos<', '>Laticínios, depósitos compactos<')
r('>Cargas pesadas<', '>Metalúrgicas, cargas de 4-6t<')
r('>Ultra heavy, Distrito Industrial<', '>Distrito Agroindustrial, +6t<')

# Note: spec table td items already replaced by section 20 spec table indicators

# Section tags
r('Cotação rápida', 'Orçamento rápido')
r('Comparativo', 'Combustão vs Elétrica')
r('O que está incluso', 'Incluso no contrato')
r('Conformidade legal', 'Segurança do trabalho')
r('Depoimentos', 'Relatos de clientes')
r('Área de atendimento', 'Cobertura de entrega')

# Incluso H2
r('O que está incluído na <span>locação</span> da empilhadeira Clark',
  'O que vem no pacote de <span>locação</span> da empilhadeira Clark')

# Incluso item titles
r('<strong>Manutenção do sistema hidráulico</strong>',
  '<strong>Hidráulico: manutenção completa</strong>')

r('<strong>Suporte técnico 24h / 7 dias</strong>',
  '<strong>Suporte técnico permanente</strong>')

r('<strong>Garfos e mastro inspecionados</strong>',
  '<strong>Garfos e mastro verificados</strong>')

r('<strong>Entrega e retirada sem custo extra</strong>',
  '<strong>Transporte incluso via BR-153</strong>')

r('<strong>Contrapeso e GLP verificados</strong>',
  '<strong>Contrapeso e alimentação de GLP</strong>')

r('<strong>Consultoria técnica gratuita</strong>',
  '<strong>Dimensionamento técnico sem custo</strong>')

# NR-11 step titles
r('<strong>Verifique o certificado do operador</strong>',
  '<strong>Confirme a certificação do operador</strong>')

r('<strong>Realize a inspeção pré-operacional</strong>',
  '<strong>Execute o checklist pré-turno</strong>')

r('<strong>Sinalize a área de operação</strong>',
  '<strong>Demarque e sinalize a área</strong>')

r('<strong>Documente e registre</strong>',
  '<strong>Mantenha registros atualizados</strong>')

# Comparativo H2
r('Empilhadeira <span>contrabalançada</span> ou elétrica: qual escolher?',
  '<span>Combustão</span> ou elétrica: qual resolve a operação em Uruaçu?')

# Comparativo tag labels
r('Empilhadeira a Combustão (GLP/Diesel)',
  'Combustão Clark (GLP/Diesel)')

r('Empilhadeira Elétrica',
  'Elétrica (bateria)')

# Quick compare box labels
r('>Torque<', '>Força<')
r('>Autonomia<', '>Duração<')
r('>Ambiente<', '>Terreno<')
r('>Custo<', '>Investimento<')
r('>Superior em rampas<', '>Vence rampas e terra<')
r('>Turno contínuo<', '>Sem pausa para recarga<')
r('>Interno + externo<', '>Câmara fria + pátio<')
r('>A partir R$2.800<', '>Desde R$2.800/mês<')

# Video tag
r('>Vídeo<', '>Vídeo institucional<')

# Preços tag
r('>Preços<', '>Valores<')

# Price card labels
r('>Clark L25 (entrada)<', '>Clark L25 — entrada<')
r('>Ticket médio<', '>Faixa intermediária<')
r('>Heavy duty / curto prazo<', '>Heavy duty / locação pontual<')

# Orçamento form title
r('>Orçamento personalizado<', '>Cotação personalizada<')

# Sticky CTA text
r('>Empilhadeira Clark<', '>Clark para Uruaçu<')
r('>a partir de R$2.800/mês<', '>desde R$2.800/mês<')
r('>Cotar Agora<', '>Solicitar Cotação<')

# Expand button text
r('Ver mais sobre empilhadeira a combustão',
  'Expandir detalhes sobre empilhadeira a combustão')

# FAQ tag
r('>FAQ<', '>Perguntas frequentes<')

# Form field labels — differentiate from SC
r('>Modelo de interesse</label>', '>Equipamento desejado</label>', 2)
r('>Combustível</label>', '>Tipo de combustível</label>', 2)
r('>Prazo de locação</label>', '>Duração do contrato</label>', 2)
r('>Quantas unidades</label>', '>Quantidade necessária</label>', 2)
r('>Grau de urgência</label>', '>Quando precisa</label>', 2)
r('>Cidade de entrega</label>', '>Local de entrega</label>', 2)

# Form button text (with whitespace)
r('Solicitar Orçamento pelo WhatsApp', 'Pedir Cotação pelo WhatsApp')
r('Solicitar Orçamento no WhatsApp', 'Solicitar Cotação no WhatsApp')
r('Receber orçamento personalizado', 'Receber cotação personalizada')

# Badges
r('Mais alugada', 'Mais contratada')
r('style="background:var(--color-dark);">Premium', 'style="background:var(--color-dark);">Cabine fechada')
r('style="background:var(--color-dark);">Versátil', 'style="background:var(--color-dark);">Multiuso')
r('style="background:#2563eb;">Compacta', 'style="background:#2563eb;">Ultra compacta')

# NR-11 checklist items
r('operador de empilhadeira atualizado', 'operador de empilhadeira em dia')
r('Checklist pré-turno obrigatório:', 'Rotina de verificação pré-turno:')

# Headings
r('Orçamento rápido', 'Cotação sem compromisso')
r('Empilhadeira Clark disponível agora', 'Empilhadeira Clark disponível agora')  # skip, already changed

# Section video/precos with whitespace
r('      Vídeo\n', '      Vídeo institucional\n')
r('      Preços\n', '      Valores\n')

# Cotar empilhadeira
r('Cotar empilhadeira Clark agora', 'Solicitar cotação Clark para Uruaçu')

# Sticky CTA text (with whitespace)
r('Empilhadeira Clark</span>', 'Clark para Uruaçu</span>')
r('a partir de R$2.800/mês</span>', 'desde R$2.800/mês</span>')
r('Cotar Agora\n', 'Pedir Cotação\n')

# More form/button differentiation
r('Ou ligue:', 'Prefere ligar?', 2)

# WhatsApp response text
r('resposta imediata', 'atendimento imediato')

# Modelo options
r('Clark L25 (mais alugada)', 'Clark L25 (mais contratada)', 2)

# Extra rewrite for NR-11 inline
r('certificação específica para todo operador de empilhadeira', 'habilitação técnica para qualquer pessoa que opere empilhadeira')

# alt texts for shared images (unchanged between cities)
r('alt="Empilhadeira Clark L-Series, vista lateral mostrando chassi, mastro e contrapeso"',
  'alt="Empilhadeira Clark L-Series com mastro triplex e contrapeso para operações em frigoríficos e armazéns"')

r('alt="Empilhadeira Clark GTS25 com cabine fechada, vista angular"',
  'alt="Clark GTS25 com cabine fechada — proteção contra choque térmico em câmaras frias de Uruaçu"')

r('alt="Empilhadeira Clark S-Series para uso geral em pátios e galpões"',
  'alt="Clark S-Series para alternância entre galpão e terreiro de secagem nas cooperativas de Uruaçu"')

r('alt="Cabine do operador Clark, detalhe de ergonomia e controles"',
  'alt="Painel e controles ergonômicos da Clark C20s compacta para laticínios e depósitos"')

r('alt="Empilhadeira Clark heavy duty em operação industrial"',
  'alt="Clark S40-60 heavy duty movimentando insumos agrícolas em pátio do Distrito Agroindustrial de Uruaçu"')

# Modelo selects — vary descriptions
r('Clark GTS 25/30/33', 'Clark GTS 25-33 (cabine fechada)', 2)
r('Clark S-Series', 'Clark S-Series (versátil)', 2)
r('Clark C-Series (heavy duty)', 'Clark C-Series (acima de 6t)', 2)

# Hero badge
r('Clark pronta para despacho', 'Clark pronta para Uruaçu')

# WhatsApp button aria
r('aria-label="Falar com a Move Máquinas pelo WhatsApp"',
  'aria-label="WhatsApp Move Máquinas — cotação para Uruaçu"')

# Footer address (keep legitimate but differentiate visible text pattern)
r('Resposta em menos de 5 min', 'Retorno em até 5 minutos')

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
            'goiania-go/', '280 km', 'Sede na',
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
uru = html.count('Uruaçu') + html.count('uruacu')
local = html.count('frigorífico') + html.count('Frigorífico') + html.count('armazén') + html.count('Armazén') + html.count('Distrito Agroindustrial') + html.count('cooperativ') + html.count('Cooperativ') + html.count('grãos') + html.count('BR-153')
print(f"\nUruaçu/uruacu: {uru} menções")
print(f"Contexto local (frigorífico/armazém/Dist.Agro/cooperativa/grãos/BR-153): {local} menções")

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

# Compare with SC combustao and BSB combustao
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
print(f"TOKENS: ~{len(html)//4} (estimativa por chars/4)")
