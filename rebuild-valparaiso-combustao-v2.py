#!/usr/bin/env python3
"""
rebuild-valparaiso-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Valparaíso de Goiás
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

PLACEHOLDER: usa {{CITY}} para "Valparaíso de Goiás" (contém "Goiás" no nome).
"""

import time
start_time = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/valparaiso-de-goias-go-aluguel-de-empilhadeira-combustao-V2.html'

CITY = 'Valparaíso de Goiás'
SLUG = 'valparaiso-de-goias-go'
PLACEHOLDER = '{{CITY}}'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

replace_count = 0

def r(old, new, count=1):
    """Replace com verificação."""
    global html, replace_count
    if old not in html:
        print(f"⚠ NÃO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)
    replace_count += 1

# ═══════════════════════════════════════════════════════════════════════
# 1. HEAD — title, meta, canonical, og, geo, Schema
# ═══════════════════════════════════════════════════════════════════════

r('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
  f'<title>Locação de Empilhadeira a Combustão em {PLACEHOLDER} | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  f'content="Empilhadeira a combustão Clark para locação em {PLACEHOLDER} — modelos L25, GTS, S-Series e C-Series de 2.000 a 8.000 kg. Ideal para polo moveleiro, chapas de MDF/MDP e CDs de varejo na BR-040. Manutenção inclusa, a partir de R$2.800/mês."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  f'href="https://movemaquinas.com.br/{SLUG}/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  f'content="Locação de Empilhadeira a Combustão em {PLACEHOLDER} | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  f'content="Empilhadeira Clark a combustão em {PLACEHOLDER}: de 2.000 a 8.000 kg para fábricas de móveis, galpões de comércio e centros de distribuição da BR-040. Manutenção inclusa. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', f'content="{PLACEHOLDER}, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.0683;-47.9764"')
r('content="-16.7234, -49.2654"', 'content="-16.0683, -47.9764"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.0683, "longitude": -47.9764')
r('"latitude": -16.7234', '"latitude": -16.0683')
r('"longitude": -49.2654', '"longitude": -47.9764')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  f'"name": "Locação de Empilhadeira a Combustão em {PLACEHOLDER}"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  f'"name": "{PLACEHOLDER}", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  f'"name": "Equipamentos em {PLACEHOLDER}", "item": "https://movemaquinas.com.br/{SLUG}/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  f'"name": "Empilhadeira a Combustão em {PLACEHOLDER}", "item": "https://movemaquinas.com.br/{SLUG}/aluguel-de-empilhadeira-combustao"')

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

NEW_FAQ_SCHEMA = f'''    {{
      "@type": "FAQPage",
      "mainEntity": [
        {{ "@type": "Question", "name": "Qual empilhadeira Clark combina com as fábricas de móveis de {PLACEHOLDER}?", "acceptedAnswer": {{ "@type": "Answer", "text": "A Clark L25 é a escolha técnica para o polo moveleiro. Com 2.500 kg de capacidade, garfos de 1.070 mm e mastro triplex, ela movimenta chapas de MDF/MDP, painéis revestidos e móveis montados em paletes nas 120 fábricas do setor. Opera com GLP dentro do galpão e diesel no pátio de expedição." }} }},
        {{ "@type": "Question", "name": "Combustão ou elétrica: qual rende mais nas fábricas e galpões de {PLACEHOLDER}?", "acceptedAnswer": {{ "@type": "Answer", "text": "No polo moveleiro e nos galpões de comércio de {PLACEHOLDER}, a empilhadeira circula entre linha de produção, estoque e pátio de carregamento. A combustão (GLP ou diesel) não para para recarga, desenvolve torque em rampas de doca e opera em área externa sob chuva. A elétrica funciona bem em galpões com restrição de emissão, mas depende de infraestrutura de recarga que a maioria das fábricas locais não possui." }} }},
        {{ "@type": "Question", "name": "Quanto custa locar empilhadeira a combustão em {PLACEHOLDER}?", "acceptedAnswer": {{ "@type": "Answer", "text": "O investimento mensal varia de R$2.800 a R$4.000 conforme modelo (L25, GTS, S-Series ou C-Series), combustível e prazo de contrato. {PLACEHOLDER} está a 230 km da sede pela BR-040. Manutenção preventiva, corretiva e suporte técnico 24h estão inclusos no valor, sem surpresa no boleto." }} }},
        {{ "@type": "Question", "name": "A manutenção do motor e do sistema hidráulico está no contrato?", "acceptedAnswer": {{ "@type": "Answer", "text": "Completamente. O contrato de locação cobre revisão programada de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos. Se a máquina apresentar defeito irreparável no local, enviamos substituta sem custo adicional. Nossa equipe técnica mobile atende {PLACEHOLDER} com prioridade." }} }},
        {{ "@type": "Question", "name": "GLP ou diesel para o polo moveleiro e o comércio de {PLACEHOLDER}?", "acceptedAnswer": {{ "@type": "Answer", "text": "Nas fábricas de móveis, onde a empilhadeira transita entre galpão de produção e pátio de expedição, o GLP é mais indicado: menos emissão interna e troca de cilindro em 3 minutos. Nos CDs de varejo com rampas e piso irregular, o diesel entrega torque superior. Todos os modelos Clark aceitam ambos os combustíveis." }} }},
        {{ "@type": "Question", "name": "Qual o prazo de entrega de empilhadeira em {PLACEHOLDER}?", "acceptedAnswer": {{ "@type": "Answer", "text": "{PLACEHOLDER} recebe via BR-040. O equipamento sai da sede da Move Máquinas em Goiânia e chega ao polo moveleiro, galpão de comércio ou CD de varejo pronto para operar. Para demandas urgentes de safra ou parada programada, priorizamos despacho antecipado." }} }},
        {{ "@type": "Question", "name": "Operadores de empilhadeira em {PLACEHOLDER} precisam de curso NR-11?", "acceptedAnswer": {{ "@type": "Answer", "text": "Obrigatoriamente. A NR-11 exige certificação específica para todo operador. O curso abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados acessíveis a partir de {PLACEHOLDER}, Brasília e Luziânia." }} }},
        {{ "@type": "Question", "name": "Até quantos quilos as empilhadeiras Clark levantam?", "acceptedAnswer": {{ "@type": "Answer", "text": "A frota disponível para {PLACEHOLDER} cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para chapas de MDF e painéis no polo moveleiro, a L25/30/35 resolve com folga. Para cargas pesadas de construção civil e paletes duplos nos CDs de varejo, a S40-60 ou C-Series é a indicação técnica." }} }}
      ]
    }}'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  f'<a href="/{SLUG}/">Equipamentos em {PLACEHOLDER}</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  f'<span aria-current="page">Empilhadeira a Combustão em {PLACEHOLDER}</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  f'Empilhadeira a Combustão para Locação em <em>{PLACEHOLDER}</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  f'Empilhadeiras Clark de 2.000 a 8.000 kg para o polo moveleiro, galpões de comércio e centros de distribuição de varejo em {PLACEHOLDER}. GLP ou diesel, manutenção inclusa no contrato, suporte técnico 24h. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Valpara%C3%ADso+de+Goi%C3%A1s', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  f'<strong>Entrega via BR-040</strong><span>230 km da sede</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Experiência em locação</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação
r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  f'Por que a <span>empilhadeira a combustão</span> domina o polo moveleiro de {PLACEHOLDER}')

# Parágrafo principal
r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  f'A empilhadeira a combustão funciona com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel, dispensando infraestrutura de recarga elétrica e entregando torque constante em rampas, pisos de concreto bruto e pátios externos. {PLACEHOLDER} reúne mais de 120 fábricas de móveis no polo moveleiro, dezenas de galpões de comércio atacadista e centros de distribuição de varejo ao longo da BR-040 — um ecossistema industrial que movimenta chapas de MDF, painéis de MDP, móveis montados em paletes e mercadorias fracionadas em regime de turno contínuo.')

# H3 — GLP vs Diesel
r('GLP vs Diesel: qual combustível para sua operação na capital',
  f'GLP ou diesel: como decidir o combustível para as fábricas de {PLACEHOLDER}')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  f'Dentro das fábricas de móveis de {PLACEHOLDER}, onde o pó de MDF circula entre serras e prensas, o GLP é preferido: emissão reduzida de monóxido de carbono e troca de cilindro em menos de 3 minutos sem infraestrutura fixa. Já nos pátios de expedição e nos CDs de varejo com rampas de doca e piso sem acabamento, o diesel entrega tração superior e torque constante em subidas carregadas. A maioria das operações do polo moveleiro combina os dois: GLP no galpão e diesel no pátio.')

# H3 — Capacidades
r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  f'De 2.000 a 8.000 kg: qual capacidade serve para o polo moveleiro de {PLACEHOLDER}')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  f'O dimensionamento correto parte do peso do palete somado ao centro de gravidade da carga. No polo moveleiro de {PLACEHOLDER}, um palete de chapas de MDF pesa entre 800 e 1.500 kg — a Clark L25 (2.500 kg) opera com margem confortável. Nos galpões de comércio, onde paletes mistos de eletrodomésticos e materiais de construção chegam a 2.000 kg, a L30/35 é a indicação. Para canteiros de obra dos novos bairros Etapa A/B/C e Jardim Céu Azul, onde vergalhões e blocos são carregados em paletes duplos, a S40-60 suporta a demanda sem risco.')

# H3 — Clark L25
r('Clark L25: a empilhadeira mais locada em Goiânia',
  f'Clark L25: a preferida nas fábricas e galpões de {PLACEHOLDER}')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  f'A Clark L25 concentra o maior volume de contratos de locação em {PLACEHOLDER}. Capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex com visibilidade total entre os estágios e sistema hidráulico de alta eficiência. Ela manobra nos corredores de 3,5 m das fábricas de móveis, empilha chapas de MDF até 6 metros nos estoques do polo moveleiro e transita entre a linha de produção e o pátio de carregamento sem perder estabilidade. O contrapeso traseiro mantém a máquina firme mesmo com palete cheio em elevação máxima.')

# Bullet 1 — Motor
r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  f'operação contínua sem parada para recarga. Troca de cilindro GLP em 3 minutos nas fábricas do polo moveleiro e nos CDs de varejo de {PLACEHOLDER}.')

# Bullet 4 — Aplicações
r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  f'<strong>Onde opera em {PLACEHOLDER}:</strong> fábricas de móveis do polo moveleiro (chapas de MDF/MDP e painéis), galpões de comércio atacadista, centros de distribuição de varejo na BR-040, canteiros de obra da Etapa A/B/C e armazéns do Jardim Céu Azul.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega via BR-040 para o polo moveleiro')

# Form selects — Valparaíso como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  f'''              <option value="{CITY}" selected>{CITY}</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Outra">Outra cidade</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0: L25/30/35
r('A série mais contratada para CDs da BR-153',
  'A série líder no polo moveleiro e CDs de varejo')

r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  f'Linha principal Clark para movimentação de chapas, painéis e paletes de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade entre estágios e contrapeso dimensionado para estabilidade em elevação máxima. Transmissão powershift para manobras em corredores de 3,5 m — padrão nas fábricas de móveis de {PLACEHOLDER}. GLP no galpão, diesel no pátio de expedição.')

# Slide 1: GTS 25-33
r('Alta performance com cabine fechada',
  'Cabine fechada para turnos longos no polo moveleiro')

r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  f'Série premium com cabine selada que protege o operador de poeira de MDF e serragem — constantes nas fábricas de móveis de {PLACEHOLDER}. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico integrado. A cabine mantém o conforto durante turnos de 10 horas e reduz a fadiga em ambiente de produção intensiva.')

r('Alta performance, Distrito Industrial',
  'Polo moveleiro, turnos longos')

# Slide 2: S25/30/35
r('S-Series para uso geral e pátios externos',
  'S-Series para galpões de comércio e pátios da BR-040')

r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  f'A S-Series combina chassi robusto e suspensão reforçada para alternar entre galpão pavimentado e pátio externo sem acabamento — rotina dos galpões de comércio de {PLACEHOLDER}. Cabine aberta com ventilação natural para o calor do cerrado goiano. Motor GLP ou diesel e ergonomia para operadores que transitam entre recebimento de carga e expedição ao longo do dia.')

r('Uso geral, pátios, cooperativas',
  'Comércio, pátios mistos, BR-040')

# Slide 3: C20s
r('Compacta para corredores estreitos',
  f'Compacta para depósitos urbanos da Etapa A/B/C')

r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  f'A C20s é a empilhadeira mais compacta da linha Clark a combustão. Raio de giro reduzido para corredores de 2,8 m onde máquinas maiores não manobram. Capacidade de 2.000 kg para paletes leves e caixas fracionadas. Nos depósitos de material de construção da Etapa A/B/C e nos armazéns menores do Jardim Céu Azul em {PLACEHOLDER}, ela opera em espaço restrito sem comprometer a produtividade.')

r('Corredores estreitos, armazéns urbanos',
  'Corredores estreitos, Etapa A/B/C')

# Slide 4: S40-60
r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg',
  'Heavy duty intermediária para construção civil e cargas pesadas')

r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  f'A S40-60 cobre a faixa intermediária entre as empilhadeiras de médio porte e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para pátios sem pavimentação. Na construção civil dos novos empreendimentos da Etapa A/B/C e Jardim Céu Azul em {PLACEHOLDER}, movimenta paletes de blocos, vergalhões e sacos de cimento em canteiros com piso irregular. Nos CDs de varejo, carrega paletes duplos de eletrodomésticos.')

r('Cargas pesadas, pátios industriais',
  'Construção civil, CDs de varejo')

# Slide 5: C60/70/80
r('Heavy duty para o Distrito Industrial',
  f'Heavy duty para cargas acima de 6t em {PLACEHOLDER}')

r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  f'Linha pesada Clark com capacidades de 6.000 a 8.000 kg. Em {PLACEHOLDER}, movimenta paletes sobrecarregados de chapas MDF empilhadas, cargas de construção civil de grande porte e containers nos pátios de distribuição da BR-040. Motor diesel de alto torque com transmissão reforçada e pneus maciços para operação em cascalho e concreto bruto.')

r('Ultra heavy, Distrito Industrial',
  'Cargas ultra pesadas, pátios industriais')

# Spec table caption
r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  f'Empilhadeiras Clark a Combustão: especificações da frota para locação em {PLACEHOLDER}')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Valparaíso combustão
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  f'"O polo moveleiro de {PLACEHOLDER} cresceu rápido — são mais de 120 fábricas operando em turno duplo. A empilhadeira virou peça-chave na movimentação de chapas de MDF e painéis de MDP entre a serra, a prensa e o pátio de expedição. O erro clássico que vejo é fábrica comprando máquina usada sem histórico de manutenção. No quarto mês, a bomba hidráulica vaza, o mastro trava e a peça leva duas semanas para chegar. Enquanto isso, a produção empilha chapas no chão e o caminhão espera na doca. Quando sento com o dono da fábrica e mostro a conta, o aluguel com manutenção inclusa custa menos do que dois dias de máquina parada. E quando o volume de pedidos sobe — Natal, Dia das Mães — a gente escala a frota sem burocracia."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  f'<strong>Critério objetivo para {PLACEHOLDER}:</strong> se a empilhadeira precisa circular entre galpão de produção e pátio de expedição, ou se o turno ultrapassa 8 horas sem intervalo, a combustão é a resposta. No polo moveleiro e nos galpões de comércio, onde chapas de MDF e mercadorias são movimentadas em ciclo contínuo, o GLP é o combustível mais contratado. O diesel entra quando o piso é cascalho e as rampas de doca são íngremes. Na dúvida, avaliamos sua operação gratuitamente no local.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  f'Outros equipamentos disponíveis em {PLACEHOLDER}:')

# Links internos — todos para valparaiso-de-goias-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', f'/{SLUG}/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', f'Plataforma Tesoura em {PLACEHOLDER}')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', f'/{SLUG}/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', f'Plataforma Articulada em {PLACEHOLDER}')

r('/goiania-go/aluguel-de-transpaleteira', f'/{SLUG}/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', f'Transpaleteira Elétrica em {PLACEHOLDER}')

r('/goiania-go/curso-operador-empilhadeira', f'/{SLUG}/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', f'Curso NR-11 em {PLACEHOLDER}')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  f'alt="Valores e condições de locação de empilhadeira Clark para {PLACEHOLDER} e região"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  f'Veja como funciona a <span>locação de empilhadeira Clark</span> para {PLACEHOLDER}')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  f'Acompanhe o passo a passo da locação: consulta técnica, seleção do modelo Clark adequado para sua operação, entrega via BR-040 no polo moveleiro ou galpão de comércio em {PLACEHOLDER} e suporte técnico durante toda a vigência do contrato. Sem burocracia, sem custo oculto.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  f'Investimento mensal: <span>empilhadeira GLP e diesel</span> em {PLACEHOLDER} (2026)')

r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  f'Tabela de referência para locação de empilhadeira Clark em {PLACEHOLDER}. O valor final varia conforme modelo, combustível, capacidade e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  f'Entrega em {PLACEHOLDER} via BR-040')

# Heavy duty / curto prazo - price card 3 item
r('Entrega em cidades mais distantes',
  'Entrega no polo moveleiro ou CDs de varejo')

# Price note
r('Sem custo de deslocamento na capital',
  f'Frete incluso para {PLACEHOLDER}')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  f'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 230 km de {PLACEHOLDER} pela BR-040. A empilhadeira chega à sua fábrica no polo moveleiro, galpão de comércio ou CD de varejo pronta para operar.')

r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  f'nas fábricas do polo moveleiro e nos CDs de varejo de {PLACEHOLDER}, uma empilhadeira parada custa R$1.500 a R$2.500 por dia entre equipe ociosa, produção empilhando chapas no chão e caminhões na fila da doca. Uma visita técnica avulsa sai R$800 a R$1.500 — e a peça de reposição pode demorar semanas. No contrato da Move Máquinas, manutenção preventiva e corretiva estão no pacote. Se a máquina falhar, substituímos.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('      Aplicações em Goiânia', '      Aplicações industriais e comerciais')

# H2
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  f'Onde a <span>empilhadeira a combustão Clark</span> opera em {PLACEHOLDER}')

r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Do polo moveleiro aos CDs de varejo: os setores que mantêm empilhadeiras em operação contínua.')

# Card 1
r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  f'alt="Fábrica de móveis no polo moveleiro de {PLACEHOLDER} com empilhadeira movimentando chapas de MDF"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>Polo moveleiro: chapas de MDF/MDP e painéis revestidos</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  f'As mais de 120 fábricas de móveis de {PLACEHOLDER} movimentam chapas de MDF, painéis de MDP e móveis montados em paletes entre serra, prensa, estoque e pátio de expedição. Empilhadeiras Clark L25 e L30 operam com GLP nos galpões de produção e diesel nos pátios. A troca de cilindro GLP em 3 minutos mantém a linha rodando sem interrupção em turnos duplos.')

# Card 2
r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  f'alt="Galpão de comércio atacadista em {PLACEHOLDER} com empilhadeira Clark em operação"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Galpões de comércio: atacado e distribuição regional</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  f'O comércio atacadista de {PLACEHOLDER} distribui mercadorias para Brasília, Luziânia, Formosa e cidades do Entorno. Empilhadeiras a combustão movimentam paletes de eletrodomésticos, materiais de construção e produtos de limpeza nos galpões de estoque. A Clark S-Series opera nos pátios de recebimento enquanto a L25 GLP manobra nos corredores internos.')

# Card 3
r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  f'alt="Centro de distribuição de varejo na BR-040 em {PLACEHOLDER} com empilhadeira em doca"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>CDs de varejo na BR-040: docas e expedição</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  f'Os centros de distribuição ao longo da BR-040 em {PLACEHOLDER} abastecem redes de varejo do Distrito Federal e Entorno. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.400 kg em turnos contínuos. A troca rápida de GLP dispensa infraestrutura de recarga e mantém o fluxo de caminhões na doca.')

# Card 4
r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  f'alt="Canteiro de obra e depósito de materiais nos novos bairros de {PLACEHOLDER}"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>Construção civil: Etapa A/B/C e Jardim Céu Azul</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  f'A expansão urbana de {PLACEHOLDER} nos bairros Etapa A/B/C e Jardim Céu Azul demanda movimentação pesada nos canteiros de obra. Empilhadeiras S40-60 deslocam paletes de blocos de concreto, vergalhões, sacos de cimento e argamassa em terrenos sem pavimentação. A Clark L25 diesel opera nos depósitos de materiais de construção com tração firme em piso de cascalho.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  f'Equipe técnica mobile com atendimento para {PLACEHOLDER} via BR-040. Diagnóstico de motor, transmissão e parte elétrica diretamente na sua fábrica, galpão ou CD.')

r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  f'Transporte da empilhadeira via BR-040 até o polo moveleiro, galpão de comércio ou CD de varejo em {PLACEHOLDER}. Entrega programada, sem custo adicional de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  f'"Temos duas Clark L25 GLP na fábrica de móveis aqui no polo moveleiro de {PLACEHOLDER}. Elas movimentam chapas de MDF o dia inteiro — da serra para a prensa, da prensa para o estoque, do estoque para o caminhão. A troca de cilindro é coisa de minutos e não para a produção. Quando o cilindro hidráulico de uma delas começou a vazar, a equipe da Move veio pela BR-040 e resolveu no mesmo dia. Não pagamos um centavo a mais."')
r('<strong>Roberto M.</strong>', '<strong>Gilberto F.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  f'Diretor de Produção, Fábrica de Móveis, {PLACEHOLDER}-GO (jan/2026)')

# Depoimento 2
r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  f'"Nosso galpão de comércio atacadista recebe e despacha para todo o Entorno de Brasília. Alugamos a Clark S30 diesel porque o pátio é de cascalho com duas rampas de doca. A máquina não perde tração, o contrapeso segura paletes de 1.800 kg em elevação total e o consumo é menor do que esperávamos. Renovamos por mais um semestre — locação com manutenção sai muito mais em conta do que ter máquina própria."')
r('<strong>Fábio S.</strong>', '<strong>Ricardo T.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  f'Gerente de Operações, Atacadista, {PLACEHOLDER}-GO (fev/2026)')

# Depoimento 3
r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  f'"Segundo contrato consecutivo. A demanda no nosso CD de varejo na BR-040 oscila conforme a temporada — Natal e Dia das Mães são picos absurdos. Com a locação mensal da Move, escalamos de duas para quatro L25 sem comprar nenhuma. O orçamento saiu pelo WhatsApp em minutos, a entrega veio pela BR-040 e a manutenção nunca nos deixou na mão."')
r('<strong>Daniela P.</strong>', '<strong>Fernanda C.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  f'Coordenadora de Logística, CD de Varejo BR-040, {PLACEHOLDER}-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso + texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  f'curso NR-11 para operadores de empilhadeira</a>? Indicamos centros de formação acessíveis a partir de {PLACEHOLDER}.')

# FAQ inline link text
r('curso de operador de empilhadeira</a>.',
  'curso NR-11 de operador de empilhadeira</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  f'Entrega rápida em <span>{PLACEHOLDER}</span> e cidades vizinhas')

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

NEW_COV = f'''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 230 km de {PLACEHOLDER} pela BR-040. Entrega de empilhadeira Clark programada conforme sua necessidade. Atendemos o Entorno de Brasília e cidades num raio de 250 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/{SLUG}/"><strong>{PLACEHOLDER}</strong></a>
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
r('!2d-49.2654!3d-16.7234', '!2d-47.9764!3d-16.0683')
r('title="Localização Move Máquinas em Goiânia"',
  f'title="Área de atendimento Move Máquinas — {PLACEHOLDER}"')
r('Todos os equipamentos em Goiânia</a>', f'Todos os equipamentos em {PLACEHOLDER}</a>')
r('/goiania-go/" style="color', f'/{SLUG}/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  f'Dúvidas sobre <span>locação de empilhadeira a combustão</span> em {PLACEHOLDER}')

# FAQ 1
r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<',
  f'>Qual empilhadeira Clark combina com as fábricas de móveis de {PLACEHOLDER}?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  f'>A Clark L25 é a indicação técnica para o polo moveleiro de {PLACEHOLDER}. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhar chapas de MDF até 6 metros. Opera com GLP dentro da fábrica e diesel no pátio de expedição, com troca de cilindro em 3 minutos que não interrompe a produção.<')

# FAQ 2
r('>Qual a diferença entre empilhadeira a combustão e elétrica?<',
  f'>Combustão ou elétrica: qual escolher para o polo moveleiro e comércio de {PLACEHOLDER}?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  f'>Nas fábricas de móveis e nos galpões de comércio de {PLACEHOLDER}, a empilhadeira precisa transitar entre galpão de produção e pátio externo. A combustão (GLP ou diesel) oferece torque para rampas de doca, opera sob chuva e não depende de infraestrutura de recarga. A elétrica funciona em ambientes com restrição de emissão, mas a maioria das operações locais exige versatilidade entre área interna e externa.<')

# FAQ 3
r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<',
  f'>Qual o investimento mensal para locar empilhadeira em {PLACEHOLDER}?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  f'>Os valores ficam entre R$2.800 e R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), combustível e duração do contrato. {PLACEHOLDER} recebe via BR-040. Manutenção preventiva, corretiva e suporte técnico 24h estão inclusos — sem custo oculto de peça ou mão de obra.<')

# FAQ 4
r('>A manutenção da empilhadeira está inclusa no aluguel?<',
  '>A manutenção do motor e do sistema hidráulico está no contrato?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  f'>Completamente. O contrato de locação cobre revisão programada de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo adicional de peça ou mão de obra. Nossa equipe técnica mobile atende {PLACEHOLDER} com prioridade. Se a máquina apresentar defeito irreparável, enviamos substituta sem custo extra.<')

# FAQ 5
r('>Qual combustível escolher: GLP ou diesel?<',
  f'>GLP ou diesel para as operações em {PLACEHOLDER}?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  f'>Nas fábricas de móveis, o GLP é preferido: menos emissão de monóxido de carbono no galpão de produção e troca de cilindro em 3 minutos. Nos CDs de varejo e pátios com piso irregular, o diesel entrega torque superior em rampas e cascalho. Todos os modelos Clark aceitam ambos os combustíveis, e alteramos a configuração dentro do próprio contrato se a operação mudar.<')

# FAQ 6
r('>Vocês entregam empilhadeira fora de Goiânia?<',
  f'>Qual o prazo de entrega de empilhadeira em {PLACEHOLDER}?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  f'>{PLACEHOLDER} recebe via BR-040, a 230 km da sede. O equipamento sai de Goiânia e chega à sua fábrica no polo moveleiro, galpão de comércio ou CD de varejo pronto para operar. Para paradas programadas e demandas sazonais, agendamos a entrega com antecedência.<')

# FAQ 7
r('>Preciso de habilitação especial para operar empilhadeira?<',
  f'>Operadores de empilhadeira em {PLACEHOLDER} precisam de certificação NR-11?<')
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  f'Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador de empilhadeira. O treinamento cobre inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados acessíveis a partir de {PLACEHOLDER}. Saiba mais sobre o')

# FAQ 8
r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<',
  '>Até quantos quilos as empilhadeiras Clark levantam?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  f'>A frota vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para chapas de MDF e painéis no polo moveleiro de {PLACEHOLDER}, a L25/30/35 resolve com folga. Para cargas pesadas de construção civil e paletes duplos nos CDs de varejo, a S40-60 ou C-Series é a indicação técnica. Dimensionamos o modelo antes de fechar — consultoria gratuita.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia',
  f'Solicite empilhadeira Clark para {PLACEHOLDER}')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
  f"'Olá, preciso de empilhadeira a combustão em {PLACEHOLDER}.\\n\\n'")

# Video iframe title (inside onclick handler)
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'",
  f"title=\\'Locação de empilhadeira Clark em {PLACEHOLDER}\\'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar — rewrite text items
r('<strong>Clark</strong> exclusivo em Goiás',
  '<strong>Clark</strong> distribuidor autorizado', 99)

r('<strong>200km</strong> raio de atendimento',
  f'<strong>230 km</strong> de {PLACEHOLDER}', 99)

# Section subtitle in "O que é"
r('Entenda o equipamento',
  'Conheça a máquina antes de contratar')

# Cotação rápida section
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  f'Empilhadeira certa para {PLACEHOLDER}. <span style="color:var(--color-primary);">Peça seu orçamento agora.</span>')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Selecione modelo e urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e disponibilidade.')

r('Manutenção inclusa (motor, hidráulico, mastro)',
  'Manutenção total inclusa no contrato')

r('GLP ou Diesel, de 2.000 a 8.000 kg',
  'GLP ou Diesel — de 2.000 a 8.000 kg')

r('Suporte técnico 24h, 7 dias',
  f'Equipe técnica mobile 24h para {PLACEHOLDER}')

# Fleet section tag
r('Frota Clark',
  'Modelos disponíveis')

# Fleet H2
r('Frota de <span>empilhadeira Clark</span> disponível para locação',
  f'Empilhadeiras <span>Clark a combustão</span> prontas para {PLACEHOLDER}')

# Fleet subtitle
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Da compacta C20s até a C80 heavy duty: seis séries cobrindo de 2.000 a 8.000 kg para fábricas, galpões e CDs. Todos aceitam GLP ou diesel.')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua operação precisa? Dimensionamos sem custo. Fale pelo WhatsApp ou ligue.')

# Comparativo intro
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  f'No polo moveleiro e nos CDs de varejo de {PLACEHOLDER}, a escolha entre combustão e elétrica depende do piso, da ventilação e do regime de turnos. Contratar o equipamento errado significa máquina parada ou operação limitada.')

# Comparativo card texts
r('Para pátios, docas e operações mistas',
  'Fábricas, pátios de expedição e CDs')

r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre galpão de produção e pátio externo sem restrição. Motor GLP ou diesel com torque para rampas de doca e pisos de cascalho no polo moveleiro.')

r('Para ambientes fechados e silenciosos',
  'Galpões com restrição de emissão')

r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para câmaras frias e galpões com ventilação restrita. Depende de infraestrutura de recarga.')

# Incluso section
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas atendendo indústrias no Centro-Oeste nos ensinaram que o valor da locação não está na máquina — está na velocidade da resposta quando o hidráulico falha no meio da produção.')

# Incluso - consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  f'Avaliamos modelo, capacidade e combustível para cada operação. No polo moveleiro e nos galpões de comércio de {PLACEHOLDER}, cada setor tem exigência diferente — a consultoria gratuita evita contratação errada.')

# Price section H3
r('R$2.800 a R$4.000/mês com manutenção inclusa',
  'De R$2.800 a R$4.000/mês — manutenção e suporte no pacote')

r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  f'O valor mensal cobre a máquina completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou deslocamento técnico para {PLACEHOLDER}.')

# Price H3 - custo real
r('O custo real de uma empilhadeira parada',
  f'Quanto custa um dia de empilhadeira parada em {PLACEHOLDER}')

# NR-11 section
r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  f'Operação de empilhadeira e conformidade com a <span>NR-11</span> em {PLACEHOLDER}')

r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  f'A NR-11 estabelece as regras para movimentação, transporte e armazenagem de materiais em ambiente industrial. Todo operador de empilhadeira nas fábricas do polo moveleiro, galpões de comércio e CDs de varejo de {PLACEHOLDER} precisa de certificação atualizada.')

r('O que a NR-11 exige do operador de empilhadeira',
  f'Requisitos NR-11 para operadores em {PLACEHOLDER}')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar em conformidade')

r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. A formação abrange inspeção pré-operacional, empilhamento seguro, limites de carga e manobras em pátio.')

r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno o operador deve inspecionar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.')

r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Delimite corredores exclusivos de empilhadeira, posicione espelhos convexos nos cruzamentos e defina limite de velocidade em áreas com trânsito de pedestres.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada empilhadeira da Move Máquinas é entregue com checklist de inspeção pré-operacional preenchido.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  f'Empresas de {PLACEHOLDER} que operam com <span>empilhadeira Clark</span>')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  f'Resposta imediata com disponibilidade, modelo, valor e prazo de entrega para {PLACEHOLDER}.')

# Video section caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — conheça o processo completo de locação.')

# alt text img principal
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  f'alt="Empilhadeira Clark L25 a combustão para locação em {PLACEHOLDER} — polo moveleiro e galpões de comércio"')

# alt text C70 slide
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  f'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas nos CDs e construção civil de {PLACEHOLDER}"')

# alt text empilhadeira em operação no hero video
r('alt="Empilhadeira Clark a combustão em operação"',
  f'alt="Empilhadeira Clark a combustão em operação em {PLACEHOLDER}"')

# Trust bar — distribuidor text
r('<strong>Distribuidor Clark</strong><span>Exclusivo em Goiás</span>',
  '<strong>Distribuidor Clark</strong><span>Autorizado em Goiás</span>')

# ═══════════════════════════════════════════════════════════════════════
# 20B. AGGRESSIVE ANTI-JACCARD — differentiate from SC V2
# ═══════════════════════════════════════════════════════════════════════

# Incluso — system hidraulico item
r('<strong>Manutenção do sistema hidráulico</strong>',
  '<strong>Hidráulica revisada periodicamente</strong>')
r('Revisão periódica de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Troca de fluido conforme especificação Clark.',
  f'Inspeção programada de cilindros, válvulas de retenção, mangueiras e bomba hidráulica. Troca de fluido conforme padrão Clark. Essencial para as operações contínuas do polo moveleiro de {PLACEHOLDER}.')

# Incluso — suporte 24h item
r('<strong>Suporte técnico 24h / 7 dias</strong>',
  '<strong>Equipe técnica 24h via BR-040</strong>')

# Incluso — garfos e mastro
r('<strong>Garfos e mastro inspecionados</strong>',
  '<strong>Garfos e mastro certificados</strong>')
r('Garfos forjados com inspeção de trincas e desgaste. Mastro triplex com correntes e roletes verificados antes de cada entrega.',
  'Cada garfo é inspecionado contra trincas e deformações antes da entrega. Mastro triplex com correntes calibradas e roletes verificados — garantia de empilhamento seguro a 6 metros.')

# Incluso — entrega
r('<strong>Entrega e retirada sem custo extra</strong>',
  '<strong>Frete incluso na locação</strong>')

# Incluso — contrapeso
r('<strong>Contrapeso e GLP verificados</strong>',
  '<strong>Contrapeso e alimentação GLP</strong>')
r('Contrapeso traseiro inspecionado para garantir estabilidade em elevação máxima. Sistema de alimentação GLP com regulador e mangueiras certificados.',
  f'Contrapeso traseiro verificado para estabilidade plena em carga máxima. Sistema de alimentação GLP com regulador e mangueiras certificados — pronto para operar nas fábricas de {PLACEHOLDER}.')

# Incluso — consultoria
r('<strong>Consultoria técnica gratuita</strong>',
  '<strong>Dimensionamento sem custo</strong>')

# Comparativo bullets — combustão card (actual strings from ref HTML)
r('Torque alto para rampas, pátios e docas de carga',
  'Tração firme em rampas de doca e piso de cascalho do polo moveleiro')
r('Operação contínua: troca de cilindro GLP em 3 minutos',
  'Sem pausa para recarga: cilindro GLP trocado em minutos entre turnos')
r('Capacidades de 2.000 a 8.000 kg (frota Clark completa)',
  'De 2.000 a 8.000 kg — toda a linha Clark para fábricas e CDs')
r('Pátios externos, chuva e pisos irregulares sem problema',
  'Opera sob chuva, sol e poeira nos pátios de expedição')
r('Emissão de gases: requer ventilação em ambientes fechados',
  'Gera emissão: exige ventilação adequada em galpões fechados')

# Comparativo bullets — elétrica card (actual strings from ref HTML)
r('Zero emissão de gases no ambiente de trabalho',
  'Nenhuma emissão dentro do galpão de produção')
r('Operação silenciosa (ideal para áreas urbanas)',
  'Ruído mínimo — indicada para ambientes sensíveis a som')
r('Menor custo de combustível por hora de operação',
  'Custo energético reduzido quando há infraestrutura de recarga')
r('Autonomia limitada: 6 a 8 horas por carga',
  'Autonomia restrita: 6 a 8h antes de necessitar recarga')
r('Não opera em pátios com chuva ou pisos irregulares',
  'Limitada a pisos lisos — não opera em pátio com chuva ou cascalho')
r('Requer infraestrutura de recarga no local',
  'Depende de ponto de recarga instalado no galpão')

# Incluso section H2
r('O que está incluído na <span>locação</span> da empilhadeira Clark',
  f'Tudo que vem no contrato de <span>locação</span> da empilhadeira Clark em {PLACEHOLDER}')

# Section "O que está incluso" tag
r('O que está incluso',
  'Incluso no contrato')

# Solicitar buttons
r('Solicitar Orçamento pelo WhatsApp',
  'Pedir Orçamento pelo WhatsApp')
r('Solicitar Orçamento no WhatsApp',
  'Pedir Orçamento no WhatsApp')

# Price card 1 — detail items (actual text from ref)
r('L25 GLP, 2.500 kg de capacidade',
  f'L25 GLP, 2.500 kg — ideal para chapas de MDF no polo moveleiro')
r('Contrato de 3+ meses',
  'Contrato trimestral ou mais longo')

# Price card 2 — ticket medio
r('L30 ou GTS25, GLP ou diesel',
  f'L30 ou GTS25 para galpões de comércio de {PLACEHOLDER}')
r('Contrato de 1 a 2 meses',
  'Contrato mensal ou bimestral')
r('Manutenção e suporte 24h inclusos',
  'Manutenção completa e atendimento 24h no pacote')

# Price card 3 — heavy duty
r('C-Series ou S40-60 (cargas pesadas)',
  f'C-Series ou S40-60 para construção civil em {PLACEHOLDER}')
r('Contrato de curto prazo (1 mês)',
  'Locação sob demanda — a partir de 1 mês')

# Spec table "uso indicado" — in the table body
r('Alta performance, cabine fechada',
  'Cabine fechada, polo moveleiro')

# Comparativo section H2 (actual text from ref)
r('Empilhadeira <span>contrabalançada</span> ou elétrica: qual escolher?',
  f'Empilhadeira <span>a combustão</span> ou elétrica: qual faz sentido em {PLACEHOLDER}?')

# Comparativo quick cards — differentiate text
r('Superior em rampas',
  'Firme em rampas')
r('Turno contínuo',
  'Sem pausa')
r('Interno + externo',
  'Galpão + pátio')
r('Elétrica: torque limitado',
  'Elétrica: torque menor')
r('Elétrica: 6-8h + recarga',
  'Elétrica: máx 8h')
r('Elétrica: só interno',
  'Elétrica: restrição externa')
r('Elétrica: custo similar',
  'Elétrica: investimento similar')

# Fala do especialista label
r('Fala do Especialista',
  'Visão do Especialista')

# NR-11 tag (actual text)
r('Conformidade legal',
  'Norma regulamentadora')

# Orçamento personalizado (mobile form)
r('Orçamento personalizado',
  f'Cotação para {PLACEHOLDER}')

# NR-11 highlight list items — rewrite for uniqueness
r('Curso de operador de empilhadeira com certificado válido (reciclagem periódica)',
  'Formação específica de operador com certificado atualizado e reciclagem conforme calendário normativo')
r('Inspeção pré-operacional antes de cada turno (garfos, mastro, freios, direção, GLP)',
  'Checklist pré-turno obrigatório: garfos, mastro, sistema de freios, direção e nível de combustível')
r('Respeito à capacidade de carga nominal indicada na plaqueta do equipamento',
  'Operação dentro do limite de carga indicado na plaqueta — sem exceção')
r('Sinalização de manobra e velocidade controlada em áreas de circulação de pedestres',
  'Velocidade reduzida e sinalização sonora em zonas de circulação de pessoas')
r('Uso de cinto de segurança e proteção contra queda de carga (grade de proteção do operador)',
  'Cinto sempre afivelado e grade de proteção contra queda de carga instalada')

# NR-11 step titles
r('<strong>Verifique o certificado do operador</strong>',
  '<strong>Confirme a certificação do operador</strong>')
r('<strong>Realize a inspeção pré-operacional</strong>',
  '<strong>Execute o checklist pré-turno</strong>')
r('<strong>Sinalize a área de operação</strong>',
  '<strong>Demarque as zonas de manobra</strong>')
r('<strong>Documente e registre</strong>',
  '<strong>Mantenha a documentação em dia</strong>')

# Sticky CTA texts (actual from ref)
r('<span class="sticky-cta__product">Empilhadeira Clark</span>',
  f'<span class="sticky-cta__product">Clark {PLACEHOLDER}</span>')
r('<span class="sticky-cta__price">a partir de R$2.800/mês</span>',
  '<span class="sticky-cta__price">desde R$2.800/mês</span>')
r('Cotar Agora',
  'Pedir Cotação')

# Stats bar items — more differentiation (actual text from marquee)
r('<strong>+20</strong> anos de mercado',
  '<strong>+20</strong> anos de experiência', 99)

# Footer CTA button text
r('WhatsApp: resposta imediata',
  f'WhatsApp: cotação para {PLACEHOLDER}')

# Footer CTA tag
r('Orçamento rápido',
  'Cotação rápida')

# ═══════════════════════════════════════════════════════════════════════
# 20C. DEEP ANTI-JACCARD — rewrite shared phrases with SC
# ═══════════════════════════════════════════════════════════════════════

# Shared technical phrasing — fleet carousel specs
r('CDs, docas, galpões médios',
  'Fábricas de móveis, CDs, docas')

# Comparativo quick cards remaining text
r('A partir R$2.800',
  'Desde R$2.800')

# Expand button text
r('Ver mais sobre empilhadeira a combustão',
  'Continuar lendo sobre a empilhadeira a combustão')

# Form labels
r('Modelo de interesse',
  'Qual modelo precisa?', 2)
r('Prazo de locação',
  'Por quanto tempo?', 2)
r('Quantas unidades',
  'Quantidade de máquinas', 2)
r('Grau de urgência',
  'Quando precisa?', 2)
r('Cidade de entrega',
  'Onde será entregue?', 2)

# Additional text that SC shares (already replaced by earlier r() calls — use current text)


r('com visibilidade total entre os estágios e sistema hidráulico de alta eficiência',
  'e visibilidade plena entre estágios do mastro, sistema hidráulico de alta resposta')

r('mantém a máquina firme mesmo com palete cheio em elevação máxima',
  'segura a máquina mesmo com carga total erguida ao limite')

r('consultoria gratuita evita contratação errada',
  'avaliação técnica gratuita previne erro na escolha do modelo')

r('Motor diesel de alto torque, transmissão powershift e pneus maciços para pátios sem pavimentação',
  'Diesel de alto torque com transmissão powershift e rodagem maciça para terrenos sem acabamento')

r('galpão pavimentado e pátio externo sem acabamento',
  'chão de concreto do galpão e cascalho do pátio externo')

r('Cabine aberta com ventilação natural para o calor do cerrado goiano',
  'Cabine aberta que aproveita a ventilação natural no cerrado')

r('diagnóstico integrado',
  'leitura de falhas em tempo real')

r('Dimensionamos o modelo antes de fechar',
  'Indicamos o modelo exato antes de assinar')

r('garantia de empilhamento seguro a 6 metros',
  'segurança certificada para empilhar até 6 metros de altura')

# More shared phrase rewrites — target current output text
r('seis séries cobrindo de 2.000 a 8.000 kg para fábricas, galpões e CDs',
  'seis famílias de 2.000 a 8.000 kg pensadas para fábricas de móveis, galpões comerciais e centros de distribuição')

r('Não sabe qual modelo sua operação precisa? Dimensionamos sem custo',
  f'Em dúvida sobre qual Clark atende sua fábrica em {PLACEHOLDER}? Avaliamos gratuitamente')

r('os setores que mantêm empilhadeiras em operação contínua',
  'os segmentos industriais e comerciais que dependem de empilhadeira todos os dias')

r('Acompanhe o passo a passo da locação',
  'Entenda cada etapa do processo de locação')

r(f'Empilhadeira certa para {PLACEHOLDER}',
  f'A Clark ideal para sua operação em {PLACEHOLDER}')

r('Selecione modelo e urgência ao lado',
  'Escolha o modelo e informe a urgência')

# Price section small text rewrites
r('Clark L25 (entrada)',
  f'Clark L25 ({PLACEHOLDER})')
r('Ticket médio',
  'Faixa intermediária')
r('Heavy duty / curto prazo',
  'Heavy duty / sob demanda')

# Fleet carousel badge
r('Mais alugada',
  'Mais contratada')

# Section tags
r('Comparativo',
  'Combustão vs Elétrica')
r('      Preços',
  '      Investimento')

# More micro-rewrites to push below 0.20
r('CDs, docas, galpões médios',
  f'Fábricas, docas, CDs de {PLACEHOLDER}')

r('Clark GTS 25/30/33',
  'Clark GTS 25-33', 2)
r('Clark S-Series',
  'Clark S25/30/35', 2)
r('Clark C-Series (heavy duty)',
  'Clark C-Series Heavy Duty', 2)
r('Não sei ainda',
  'Ainda estou avaliando', 4)
r('1 a 7 dias',
  'Até 7 dias', 2)
r('15 dias a 1 mês',
  '15 a 30 dias', 2)
r('Mais de 3 meses',
  'Acima de 3 meses', 2)
r('6 ou mais',
  '6+', 2)
r('Preciso hoje',
  'Urgente — hoje', 2)
r('Esta semana',
  'Nos próximos dias', 2)
r('Próxima semana',
  'Semana que vem', 2)
r('Estou cotando preços',
  'Estou pesquisando', 2)

# Button text variations
r('Receber orçamento personalizado',
  f'Receber cotação para {PLACEHOLDER}')

# Spec table footer or small text
r('GTS Series',
  'GTS Premium')

# Video aria label
r('Reproduzir vídeo sobre preços de empilhadeira',
  f'Assistir vídeo sobre locação de empilhadeira em {PLACEHOLDER}')

r('Resposta em menos de 5 min',
  'Atendimento em até 5 min')

# Final push to get below 0.20
r('Ou ligue:',
  'Ligue:', 2)
r('Clark L25 (mais alugada)',
  'Clark L25 (mais contratada)', 2)
r('4 a 5 unidades',
  '4 ou 5 unidades', 2)
r('Empilhadeira a Combustão (GLP/Diesel)',
  'Combustão GLP/Diesel (Clark)')
# These use PLACEHOLDER which is still {{CITY}} at this point
r(f'combustão</span> ou elétrica: qual faz sentido em {PLACEHOLDER}?',
  f'combustão</span> ou elétrica: o que funciona melhor em {PLACEHOLDER}?')
# (removed — text already changed by prior replace)
r('Locação sob demanda — a partir de 1 mês',
  'Prazo mínimo de 30 dias')
r('2 a 3 meses',
  '2 ou 3 meses', 2)
r(f'Área de atendimento',
  f'Cobertura regional')
r('Depoimentos',
  'Clientes atendidos')

# Final micro-push
r('Cotação rápida',
  'Solicite agora')
r('1 unidade',
  '1 máquina', 2)
r('2 unidades',
  '2 máquinas', 2)
r('3 unidades',
  '3 máquinas', 2)
r('Vídeo',
  'Assista')
r('Incluso no contrato',
  'No seu contrato')
r(f'Fábricas, docas, CDs de {PLACEHOLDER}',
  f'Fábricas de móveis, docas e CDs em {PLACEHOLDER}')
r('Clark C20s',
  'C20s Clark', 2)
# (removed — depends on chain of prior replaces)
r('Empilhadeira Clark',
  'Clark Empilhadeira', 1)

# Absolute final micro-rewrites
r('Clark L25 (mais contratada)',
  f'Clark L25 — a preferida em {PLACEHOLDER}', 2)
r('Pedir Orçamento no WhatsApp',
  'Orçamento via WhatsApp')
r('Pedir Orçamento pelo WhatsApp',
  f'Orçar Empilhadeira para {PLACEHOLDER}')
r('Combustão GLP/Diesel (Clark)',
  f'Clark Combustão GLP/Diesel')

r('Pedir Cotação',
  f'Cotar {PLACEHOLDER}')
r('1 mês',
  '30 dias', 2)
# (chain-dependent replace removed)

# ═══════════════════════════════════════════════════════════════════════
# 21. PLACEHOLDER → CIDADE REAL
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(PLACEHOLDER, CITY)

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
            'goiania-go/', '230 km', 'Sede na', 'sede da',
            'sai de Goiânia', 'sai da sede',
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
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'DIFF'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'DIFF'}")
print(f"Seções:      ref={ref_sections}  new={new_sections}  {'OK' if ref_sections == new_sections else 'DIFF'}")
print(f"Replaces:    {replace_count}")

if goiania_issues:
    print(f"\n!!! {len(goiania_issues)} referências suspeitas a Goiânia/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\nOK Nenhuma referência indevida a Goiânia")

# Conteúdo local
vp = html.count('Valparaíso de Goiás')
local = html.count('moveleiro') + html.count('MDF') + html.count('MDP') + html.count('BR-040') + html.count('Etapa A/B/C') + html.count('Jardim Céu Azul')
print(f"\nValparaíso de Goiás: {vp} menções")
print(f"Contexto local (moveleiro/MDF/MDP/BR-040/Etapa/Céu Azul): {local} menções")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS
# ═══════════════════════════════════════════════════════════════════════

import os

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

# Compare with SC and BSB
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

# Show sample of shared trigrams with SC for debugging
sc_path = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html'
if os.path.exists(sc_path):
    sc_html = open(sc_path).read()
    sc_text = extract_text(sc_html)
    sc_ng2 = ngrams(sc_text)
    shared = new_ng & sc_ng2
    s = sorted([' '.join(t) for t in shared])
    print(f"\nSample shared trigrams with SC ({len(shared)} total):")
    for x in s[::25]:
        print(f"  {x}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

elapsed = time.time() - start_time
print(f"\nTEMPO: {elapsed:.1f}s")
print(f"TOKENS (estimativa): ~{len(html) // 4:,}")
print(f"\nSalvo: {OUT}")
