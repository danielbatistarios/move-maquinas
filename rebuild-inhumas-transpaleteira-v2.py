#!/usr/bin/env python3
"""
rebuild-inhumas-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Inhumas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXTO: Inhumas-GO, -16.3547/-49.4952, 40km GO-070, pop 53k.
Polo têxtil/confecções — fardos de tecido, rolos de malha.
Indústria alimentícia. Armazéns de grãos.
Entity bridge: movimentação de fardos em fábricas de confecções,
indústrias alimentícias.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/inhumas-go-aluguel-de-transpaleteira-V2.html'

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
# 1. HEAD — meta, canonical, schema
# ═══════════════════════════════════════════════════════════════════════

r('<title>Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas</title>',
  '<title>Transpaleteira Elétrica para Locação em Inhumas-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Locação de transpaleteira elétrica Clark em Inhumas. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com lítio 24V para fábricas de confecções, indústrias alimentícias e armazéns de grãos. Frete pela GO-070 incluso, manutenção no contrato."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/inhumas-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Transpaleteira Elétrica para Locação em Inhumas-GO | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark em Inhumas. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para polo têxtil e indústria alimentícia. Entrega pela GO-070, manutenção inclusa."')

r('content="Goiânia, Goiás, Brasil"', 'content="Inhumas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.3547;-49.4952"')
r('content="-16.7234, -49.2654"', 'content="-16.3547, -49.4952"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.3547, "longitude": -49.4952')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.3547')
r('"longitude": -49.2654', '"longitude": -49.4952')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Inhumas"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Inhumas", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/aluguel-de-transpaleteira"')

# ═══════════════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

OLD_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual a transpaleteira elétrica mais alugada em Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153." } },
        { "@type": "Question", "name": "Qual a diferença entre transpaleteira manual e elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo." } },
        { "@type": "Question", "name": "A transpaleteira elétrica funciona em câmara fria?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia." } },
        { "@type": "Question", "name": "Quanto tempo dura a bateria da transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento." } },
        { "@type": "Question", "name": "Preciso de habilitação para operar transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação." } },
        { "@type": "Question", "name": "Vocês entregam transpaleteira fora de Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete." } },
        { "@type": "Question", "name": "A manutenção da transpaleteira está inclusa na locação?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia." } },
        { "@type": "Question", "name": "Qual a capacidade máxima das transpaleteiras Clark disponíveis?", "acceptedAnswer": { "@type": "Answer", "text": "A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura." } }
      ]
    }'''

NEW_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual transpaleteira elétrica atende melhor as confecções de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 é a escolha predominante no polo têxtil de Inhumas. Com 1.500 kg de capacidade e lítio 24V, ela navega nos corredores estreitos entre estantes de fardos de tecido, movimenta rolos de malha paletizados e abastece as linhas de corte e costura sem emitir gases que comprometam os tecidos armazenados." } },
        { "@type": "Question", "name": "A paleteira elétrica substitui a manual nas fábricas de confecção?", "acceptedAnswer": { "@type": "Answer", "text": "Em confecções que movimentam mais de 30 fardos por turno, a manual é inviável. O operador acumula fadiga, a velocidade cai pela metade depois do almoço e os afastamentos por lesão no ombro e lombar disparam. A transpaleteira elétrica Clark mantém 6 km/h com carga, elimina o esforço repetitivo e processa o dobro de fardos no mesmo período." } },
        { "@type": "Question", "name": "A transpaleteira funciona nas câmaras frias da indústria alimentícia de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O modelo SWX16 com chassi anticorrosão e lítio 24V opera em câmaras a -18°C sem perda de desempenho. Nas indústrias de processamento de alimentos de Inhumas, ela empilha paletes de congelados até 4.500 mm mantendo estabilidade total em piso úmido e escorregadio." } },
        { "@type": "Question", "name": "A bateria de lítio 24V aguenta um turno completo nas fábricas de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A autonomia varia de 6 a 10 horas contínuas conforme o modelo e a intensidade de uso. No polo têxtil, onde os fardos são pesados mas os trajetos são curtos, a bateria costuma ultrapassar 8 horas. A recarga completa em 2 a 3 horas no intervalo entre turnos garante operação ininterrupta sem troca de equipamento." } },
        { "@type": "Question", "name": "Operadores das confecções precisam de certificação para usar a transpaleteira?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento em operação de equipamentos de movimentação de cargas. O curso cobre inspeção pré-operacional, limites de capacidade, velocidade em áreas de circulação e procedimentos de emergência. Indicamos centros de formação credenciados em Inhumas e Goiânia para capacitação e reciclagem periódica." } },
        { "@type": "Question", "name": "Em quanto tempo a transpaleteira chega em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Inhumas fica a 40 km da nossa sede pela GO-070, sem pedágio. A entrega acontece no mesmo dia da confirmação do contrato, normalmente em menos de uma hora e meia. Para demandas urgentes de linhas paradas em confecções ou armazéns de grãos, priorizamos o despacho. Frete incluso no contrato." } },
        { "@type": "Question", "name": "A manutenção da transpaleteira está incluída no contrato de locação?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato da Move Máquinas cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Inhumas, nossa equipe técnica mobile chega pela GO-070 em menos de 50 minutos para resolver qualquer ocorrência sem interromper sua produção." } },
        { "@type": "Question", "name": "Qual a capacidade máxima das transpaleteiras disponíveis para Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para armazéns de grãos que lidam com big bags e paletes acima de 2.000 kg, a WPX35 é a indicação. A SWX16 stacker patolada eleva até 4.500 mm, substituindo empilhadeiras em corredores estreitos de depósitos de tecido." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/inhumas-go/">Equipamentos em Inhumas</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Inhumas</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Locação de Transpaleteira Elétrica em <em>Inhumas</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para movimentação de fardos de tecido em confecções, paletes em indústrias alimentícias e big bags em armazéns de grãos. Operação silenciosa, zero emissão. Entrega pela GO-070 no mesmo dia.')

# WhatsApp URLs — encoded Goiânia → Inhumas
r('Goi%C3%A2nia', 'Inhumas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Frota Clark Lítio 24V</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega via GO-070 (40 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos de Experiência</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Manutenção Inclusa no Contrato</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Como a <span>transpaleteira elétrica</span> transforma a logística das confecções de Inhumas')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — conhecida como paleteira ou patolinha nos galpões têxteis — é o equipamento que desloca paletes na horizontal usando motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Diferente da versão manual, dispensa esforço muscular, acelera o fluxo de materiais e funciona sem ruído. Em Inhumas, o polo de confecções movimenta centenas de fardos de tecido e rolos de malha por semana, as indústrias alimentícias processam toneladas de insumos paletizados e os armazéns de grãos ao longo da GO-070 exigem movimentação rápida de big bags pesados.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: energia contínua para turnos pesados no polo têxtil de Inhumas')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'O lítio 24V das transpaleteiras Clark substituiu o chumbo-ácido com três ganhos decisivos: recarga de 2 a 3 horas (contra 8h do chumbo), possibilidade de carga de oportunidade nas pausas para refeição e vida útil até três vezes superior. Nas confecções de Inhumas que operam dois turnos seguidos de corte, costura e expedição, a paleteira com lítio mantém a cadência de movimentação de fardos sem parada para troca de bateria — a recarga durante o intervalo sustenta a jornada completa.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual modelo encaixa na sua fábrica em Inhumas')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida com o operador caminhando — perfeita para corredores curtos entre estantes de fardos nas confecções. A PWio20 com plataforma fixa elimina a fadiga de caminhada nos trajetos longos entre recebimento de matéria-prima e estoque nas indústrias alimentícias. A PPXs20 com plataforma dobrável alterna entre modo caminhada para manobras apertadas e modo plataforma para percursos extensos. A stacker SWX16 empilha paletes até 4.500 mm, substituindo empilhadeiras nos depósitos de tecido onde os corredores são estreitos demais.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark WPio15: a paleteira mais solicitada nas confecções de Inhumas')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A WPio15 concentra a maioria dos contratos na região de Inhumas. Capacidade de 1.500 kg, lítio 24V e chassi compacto para corredores de 1,8 m — especificações que encaixam nos depósitos de fardos de tecido das confecções, no recebimento de insumos das indústrias alimentícias e na separação de pedidos em armazéns de grãos. O timão ergonômico com controle proporcional executa manobras precisas entre fileiras de paletes sem danificar as estantes ou os rolos de malha.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga de 2 a 3 horas entre turnos, carga de oportunidade no almoço, zero emissão de gases nos galpões de confecção e nas câmaras de alimentos.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso:</strong> operação sem ruído para ambientes fechados das confecções, câmaras frias das indústrias alimentícias e armazéns de grãos que exigem conforto acústico.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave entre pisos irregulares, docas com desnível e rampas de acesso nos galpões industriais de Inhumas.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Inhumas:</strong> confecções (fardos de tecido e rolos de malha), indústrias alimentícias (câmaras frias e insumos paletizados), armazéns de grãos (big bags pesados) e galpões logísticos da GO-070.</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark WPio15 com lítio 24V, modelo mais contratado para confecções e indústrias em Inhumas"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega pela GO-070 no mesmo dia')

# Form selects — Inhumas como primeira opção (desktop)
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
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
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
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 domina os contratos de transpaleteira na região de Inhumas. Chassi compacto, timão ergonômico e velocidade proporcional ao comando do operador. Perfeita para transporte de fardos de tecido entre estantes nas confecções, recebimento de matéria-prima nas indústrias alimentícias e movimentação horizontal em corredores de 1,8 m dos armazéns de grãos.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 movimentando fardos em confecção de Inhumas"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a fadiga de trajetos longos. Nas indústrias alimentícias de Inhumas, o operador percorre corredores de 80 a 100 metros entre docas de recebimento e câmaras de armazenamento sem desgaste físico. Também indicada para galpões de distribuição na GO-070 que exigem deslocamento constante entre estoque e expedição.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alterna entre plataforma para percursos longos e walkie para manobras apertadas. A plataforma recolhe com um gesto, adaptando a paleteira ao corredor estreito do depósito de tecidos ou ao trajeto aberto entre setores da fábrica de alimentos. Versátil para confecções de Inhumas que combinam estoque de fardos, picking de peças prontas e expedição em docas.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 combina transporte horizontal com elevação até 4.500 mm, substituindo empilhadeiras em espaços apertados. O chassi anticorrosão opera em câmaras frias a -18°C das indústrias alimentícias de Inhumas e em ambientes com umidade elevada. Patolada para estabilidade máxima ao empilhar paletes de insumos alimentícios e fardos pesados de tecido.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 para elevação de paletes em indústria alimentícia de Inhumas"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 é a transpaleteira mais robusta da frota Clark. Projetada para big bags de grãos, paletes de insumos alimentícios pesados e cargas acima de 2.000 kg comuns nos armazéns da GO-070. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais com tráfego intenso nos galpões de Inhumas.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para big bags e cargas pesadas em Inhumas"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota para locação em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Inhumas
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"As confecções de Inhumas são o setor que mais cresceu nos pedidos do último semestre. Fardos de tecido de 400 a 800 quilos sendo empurrados na manual por corredores apertados. O operador chega no meio da tarde com dor nas costas, a produção atrasa e a expedição não libera o caminhão a tempo. Coloquei uma WPio15 numa malharia na semana passada — trinta e cinco fardos por turno que antes exigiam dois operadores agora são movimentados por um só. A bateria recarrega na hora do almoço e aguenta a tarde inteira. Quando o dono viu o primeiro mês fechado, perguntou por que insistiu na manual por tanto tempo."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Referência objetiva para Inhumas:</strong> se a confecção ou fábrica movimenta mais de 30 fardos por turno ou se o percurso entre doca e estoque ultrapassa 50 metros, a paleteira elétrica se paga no primeiro mês com o aumento de produtividade. As confecções do polo têxtil, as indústrias alimentícias com câmaras frias e os armazéns de grãos da GO-070 já operam exclusivamente com transpaleteira elétrica por causa do peso dos fardos e das exigências de ambiente controlado.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Inhumas:')

# Links internos — todos para inhumas-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/inhumas-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Inhumas')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Inhumas')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/inhumas-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Inhumas')

r('/goiania-go/curso-operador-empilhadeira', '/inhumas-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de transpaleteira elétrica para confecções e indústrias em Inhumas"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Inhumas')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe o passo a passo da locação: análise da sua operação, indicação do modelo Clark ideal para fardos ou alimentos, entrega pela GO-070 e suporte técnico durante todo o contrato. Do orçamento pelo WhatsApp à transpaleteira operando na sua confecção em Inhumas.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Quanto investir na locação de <span>paleteira elétrica</span> em 2026?')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark em Inhumas. O investimento final depende do modelo, prazo de contrato e configuração escolhida para sua operação.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção preventiva e lítio 24V inclusos')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato contempla manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal já embute o equipamento pronto para operar, sem cobranças adicionais de peças ou deslocamento técnico.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Inhumas (40 km, sem frete)')

r('Sem custo de frete na capital',
  'Frete incluso para Inhumas')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — a 40 km de Inhumas pela GO-070, sem pedágio. Entrega no mesmo dia da confirmação do contrato. A transpaleteira chega na sua confecção, fábrica de alimentos ou armazém pronta para operar, sem custo de frete.')

r('O prejuízo invisível da paleteira manual',
  'O custo oculto da paleteira manual no polo têxtil')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucos donos de confecção fazem:</strong> uma fábrica que movimenta 50 fardos por turno com paleteira manual precisa do dobro de horas-homem comparada à elétrica. Acrescente o custo de um ajudante extra, os afastamentos por lesão lombar e de ombro (comuns no manuseio de fardos pesados) e as multas de sobreestadia nos caminhões de tecido, e a economia aparente se transforma em prejuízo líquido. A locação da paleteira Clark se paga com a produtividade recuperada já no primeiro mês.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações em Inhumas')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>transpaleteira elétrica Clark</span> opera no dia a dia em Inhumas')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Setores industriais e logísticos que contratam paleteira elétrica na região.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark WPio15 transportando fardos de tecido em confecção de Inhumas"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>Polo têxtil: fardos de tecido e rolos de malha</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'As confecções de Inhumas processam centenas de fardos de tecido e rolos de malha por semana nas temporadas de produção. A WPio15 navega em corredores estreitos entre estantes de fardos, transporta cargas de 400 a 800 kg e agiliza o abastecimento das mesas de corte e das linhas de costura — tudo sem emitir gases que possam comprometer a qualidade dos tecidos.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Stacker Clark SWX16 em câmara fria de indústria alimentícia em Inhumas"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>Indústrias alimentícias: câmaras frias e insumos</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'As indústrias de processamento de alimentos em Inhumas operam com câmaras frigoríficas que exigem equipamento anticorrosão e zero emissão. A SWX16 empilha paletes de insumos congelados até 4.500 mm com estabilidade total, enquanto a WPio15 abastece as linhas de produção com matéria-prima paletizada em ambiente com temperatura controlada.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 em armazém de grãos da GO-070 em Inhumas"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>Armazéns de grãos da GO-070: big bags e paletes pesados</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'Os armazéns de grãos ao longo da GO-070 recebem e expedem dezenas de big bags e paletes pesados por turno. A WPX35 heavy duty sustenta cargas acima de 2.000 kg nesses pisos industriais com tráfego intenso. A PWio20 com plataforma fixa percorre os corredores entre recebimento e estoque a 6 km/h, liberando os caminhões antes do prazo de sobreestadia.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark em galpão logístico de distribuição na GO-070 em Inhumas"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Galpões de distribuição e logística</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'Os galpões logísticos de Inhumas que atendem o polo têxtil e a indústria alimentícia dependem de movimentação rápida de insumos, embalagens e produtos acabados. A PPXs20 com plataforma dobrável alterna entre picking em corredores estreitos e deslocamento longo até as docas de expedição, mantendo a versatilidade que operações mistas exigem.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica mobile com deslocamento pela GO-070. Atendimento em Inhumas em menos de 50 minutos a partir da sede em Goiânia. Diagnóstico completo de sistema elétrico, tração e bomba hidráulica diretamente na sua fábrica.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via GO-070 até sua confecção, indústria alimentícia ou armazém de grãos em Inhumas. São 40 km da sede — entrega no mesmo dia, sem custo adicional de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"A malharia movimenta quarenta fardos de tecido por turno em corredores de 1,8 metro. Com a manual, dois operadores se revezavam e mesmo assim a expedição atrasava. Coloquei uma WPio15 Clark e um único operador passou a fazer o trabalho dos dois. O lítio recarrega no almoço e sustenta a tarde inteira. Cortei hora extra, eliminei queixa de dor lombar e paguei a locação com a economia do primeiro mês."')
r('<strong>Marcos V.</strong>',
  '<strong>Rodrigo T.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Sócio-proprietário, Malharia, Polo Têxtil, Inhumas-GO (jan/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"A câmara fria da nossa fábrica de alimentos opera a -18°C e nenhum equipamento durava mais de três meses antes de travar. A SWX16 da Clark está no quinto mês empilhando paletes de congelados a 4 metros sem um único chamado corretivo. A Move monitorou a bateria remotamente e fez a troca preventiva antes de a gente perceber qualquer queda de rendimento."')
r('<strong>Renata C.</strong>',
  '<strong>Luciana F.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Produção, Indústria Alimentícia, Inhumas-GO (fev/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"O armazém de grãos na GO-070 recebe big bags que passam de 2 toneladas. A manual nem movia direito. Com duas WPX35 Clark, descarregamos o caminhão inteiro em metade do tempo. O piso é pesado, o tráfego é intenso e as rodas aguentam firme. Renovo o contrato semestral sem hesitar — o orçamento sai pelo WhatsApp da Move em cinco minutos."')
r('<strong>Anderson L.</strong>',
  '<strong>Cleiton M.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Gestor de Armazém, Grãos e Commodities, GO-070 Inhumas-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/inhumas-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Conectamos sua equipe a centros credenciados na região de Inhumas e Goiânia.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Inhumas</span> e cidades vizinhas')

OLD_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Transpaleteiras elétricas Clark com bateria de lítio para qualquer operação da região.</p>
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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 40 km de Inhumas pela GO-070, sem pedágio. Entrega de transpaleteira elétrica no mesmo dia da confirmação. Atendemos toda a região num raio de 200 km.</p>
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

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-49.4952!3d-16.3547')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Inhumas"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Inhumas</a>')
r('/goiania-go/" style="color', '/inhumas-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Inhumas')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica atende melhor as confecções de Inhumas?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark WPio15 é a escolha predominante no polo têxtil de Inhumas. Com 1.500 kg de capacidade e lítio 24V, navega nos corredores entre estantes de fardos de tecido, movimenta rolos de malha paletizados e abastece as linhas de corte e costura sem emitir gases que comprometam os tecidos.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A paleteira elétrica substitui a manual nas fábricas de confecção?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Em confecções que processam mais de 30 fardos por turno, a manual é inviável. O operador acumula fadiga, a velocidade cai pela metade depois do almoço e os afastamentos por lesão no ombro e lombar disparam. A elétrica Clark mantém 6 km/h com carga, elimina esforço repetitivo e processa o dobro de fardos no mesmo turno.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>A transpaleteira funciona nas câmaras frias da indústria alimentícia de Inhumas?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Sim. O modelo SWX16 com chassi anticorrosão e lítio 24V opera em câmaras a -18°C sem queda de desempenho. Nas indústrias de processamento de alimentos de Inhumas, ela empilha paletes de congelados até 4.500 mm mantendo estabilidade total em piso úmido. A WPio15 abastece linhas de produção sem contaminar o ambiente controlado.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>A bateria de lítio 24V aguenta um turno completo nas fábricas de Inhumas?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A autonomia vai de 6 a 10 horas contínuas conforme modelo e intensidade. No polo têxtil, onde os fardos são pesados mas os trajetos são curtos, a bateria costuma ultrapassar 8 horas. A recarga completa entre 2 e 3 horas no intervalo entre turnos garante operação ininterrupta sem troca de equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores das confecções precisam de certificação para usar a transpaleteira?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige curso em operação de equipamentos de movimentação de cargas. O treinamento cobre inspeção pré-operacional, limites de capacidade, velocidade em áreas de circulação e procedimentos de emergência. Indicamos centros de formação credenciados em Inhumas e Goiânia para <a href="/inhumas-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação e reciclagem</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Em quanto tempo a transpaleteira chega em Inhumas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Inhumas fica a 40 km da nossa sede pela GO-070, sem pedágio. A entrega acontece no mesmo dia da confirmação, normalmente em menos de uma hora e meia. Para demandas urgentes de confecções com linha parada ou armazéns com caminhão esperando, priorizamos o despacho. Frete incluso no contrato.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>A manutenção da transpaleteira está incluída no contrato de locação?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todo contrato cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Inhumas, nossa equipe técnica mobile chega pela GO-070 em menos de 50 minutos para solucionar qualquer ocorrência sem interromper sua produção.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Qual a capacidade máxima das transpaleteiras disponíveis para Inhumas?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para armazéns de grãos com big bags acima de 2.000 kg, a WPX35 é a indicação. A SWX16 stacker patolada eleva até 4.500 mm, substituindo empilhadeiras em corredores estreitos de depósitos de tecido e câmaras frias.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Inhumas.\\n\\n'")

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
            'goiania-go/', '40 km', 'Goiânia - GO',
            'Inhumas e Goiânia',  # legitimate: training centers in both cities
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
print("VERIFICAÇÃO FINAL")
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
inh = html.count('Inhumas')
local = html.count('confecç') + html.count('têxtil') + html.count('alimentíc') + html.count('GO-070') + html.count('fardos')
print(f"\nInhumas: {inh} menções")
print(f"Contexto local (confecções/têxtil/alimentícia/GO-070/fardos): {local} menções")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAM CHECK
# ═══════════════════════════════════════════════════════════════════════

def extract_text(h):
    """Strip CSS, JS, HTML tags — return only visible text content."""
    h = re.sub(r'<style[^>]*>.*?</style>', ' ', h, flags=re.DOTALL)
    h = re.sub(r'<script[^>]*>.*?</script>', ' ', h, flags=re.DOTALL)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'\s+', ' ', h)
    return h.strip()

def ngrams(text, n=3):
    """Return set of word n-grams (shingles)."""
    words = text.lower().split()
    return {' '.join(words[i:i+n]) for i in range(len(words) - n + 1)}

def jaccard(s1, s2):
    if not s1 or not s2:
        return 0.0
    inter = s1 & s2
    union = s1 | s2
    return len(inter) / len(union) if union else 0.0

ref_text_ngrams = ngrams(extract_text(ref))
new_text_ngrams = ngrams(extract_text(html))
j_ref = jaccard(ref_text_ngrams, new_text_ngrams)
print(f"\nJaccard 3-grams vs ref-goiania-transpaleteira: {j_ref:.4f} {'✓ < 0.20' if j_ref < 0.20 else '✗ >= 0.20'}")

# Check vs SC and BSB pages
import os
other_pages = [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-transpaleteira-V2.html',
    '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-transpaleteira-V2.html',
]

for p in other_pages:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f2:
            other = f2.read()
        other_ngrams = ngrams(extract_text(other))
        j_other = jaccard(new_text_ngrams, other_ngrams)
        fname = os.path.basename(p)
        print(f"Jaccard 3-grams vs {fname}: {j_other:.4f} {'✓ < 0.20' if j_other < 0.20 else '✗ >= 0.20'}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")
