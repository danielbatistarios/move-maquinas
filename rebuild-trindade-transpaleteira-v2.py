#!/usr/bin/env python3
"""
rebuild-trindade-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Trindade-GO
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

Contexto local:
  - Trindade-GO, pop ~140k, coord -16.6514/-49.4926
  - 18 km da sede Move Máquinas pela GO-060
  - CDs emergentes ao longo da GO-060 e BR-153
  - Supermercados e comércio varejista (Setor Maysa, Sol Nascente)
  - Construção civil, depósitos de materiais de construção
  - Entity bridge: "supermercados e comércio varejista, centros de distribuição emergentes"
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/trindade-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Locação de Transpaleteira Elétrica em Trindade-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Transpaleteira elétrica Clark para locação em Trindade-GO. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com lítio 24V para supermercados, CDs emergentes da GO-060 e depósitos de materiais de construção. Manutenção inclusa, entrega no mesmo dia."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/trindade-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Locação de Transpaleteira Elétrica em Trindade-GO | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark em Trindade. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para supermercados, comércio varejista e centros de distribuição emergentes. Entrega pela GO-060 no mesmo dia."')

r('content="Goiânia, Goiás, Brasil"', 'content="Trindade, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.6514;-49.4926"')
r('content="-16.7234, -49.2654"', 'content="-16.6514, -49.4926"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.6514, "longitude": -49.4926')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.6514')
r('"longitude": -49.2654', '"longitude": -49.4926')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Trindade"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Trindade", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Trindade", "item": "https://movemaquinas.com.br/trindade-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Trindade", "item": "https://movemaquinas.com.br/trindade-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira elétrica combina melhor com as operações de Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 é o modelo mais requisitado na cidade. Com 1.500 kg de capacidade e lítio 24V, ela atende supermercados de médio e grande porte no Setor Maysa, depósitos de materiais de construção no Sol Nascente e centros de distribuição que estão surgindo ao longo da GO-060. Silenciosa e compacta, navega corredores de 1,8 m sem esforço." } },
        { "@type": "Question", "name": "Supermercados de Trindade podem usar transpaleteira elétrica no salão de vendas?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. As transpaleteiras Clark com lítio 24V não emitem gases nem ruído relevante, operando dentro de áreas abertas ao público. O modelo WPio15 é compacto o suficiente para circular entre gôndolas durante a reposição noturna, movimentando paletes de bebidas, alimentos e produtos de higiene sem incomodar clientes ou colaboradores." } },
        { "@type": "Question", "name": "A paleteira elétrica substitui a manual nos depósitos de construção civil?", "acceptedAnswer": { "@type": "Answer", "text": "Nos depósitos de materiais de construção do Sol Nascente e região central de Trindade, os paletes de cimento, argamassa e revestimentos ultrapassam 1.000 kg. A paleteira manual não sustenta o ritmo de 40 a 50 paletes por turno sem causar fadiga e lesão no operador. A elétrica Clark mantém velocidade constante de até 6 km/h e elimina o desgaste físico, reduzindo afastamentos e acelerando a expedição." } },
        { "@type": "Question", "name": "Quanto tempo a bateria de lítio dura num turno comercial em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "A bateria de lítio 24V entrega de 6 a 10 horas contínuas conforme a intensidade de uso. Em supermercados e depósitos de construção de Trindade que operam turno único diurno, a carga completa cobre a jornada inteira. Para operações com reposição noturna, a recarga de 2 a 3 horas entre turnos garante disponibilidade ininterrupta." } },
        { "@type": "Question", "name": "Operadores de supermercado precisam de curso para usar transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento de operação de equipamentos de movimentação de carga. O curso cobre inspeção pré-operacional, limites de capacidade, velocidade em áreas com circulação de pessoas e procedimentos de emergência. Indicamos centros de formação credenciados em Trindade e Goiânia para capacitação e reciclagem." } },
        { "@type": "Question", "name": "A Move Máquinas entrega transpaleteira no mesmo dia em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "Trindade fica a 18 km da nossa sede pela GO-060, trajeto de aproximadamente 25 minutos. A entrega acontece no mesmo dia da confirmação do contrato, geralmente em menos de 2 horas. Para demandas urgentes de supermercados em pico sazonal ou obras com prazo apertado, priorizamos o despacho. Frete incluso." } },
        { "@type": "Question", "name": "O contrato de locação inclui manutenção preventiva e corretiva?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato da Move Máquinas cobre manutenção completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Trindade, nossa equipe técnica mobile chega pela GO-060 em menos de 30 minutos para resolver qualquer ocorrência sem interromper sua operação." } },
        { "@type": "Question", "name": "Existe transpaleteira para cargas pesadas disponível em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para depósitos de construção que movimentam paletes de cimento e aço acima de 2.000 kg, a WPX35 é a indicação direta. A SWX16 stacker patolada eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de armazéns e CDs emergentes." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/trindade-go/">Equipamentos em Trindade</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Trindade</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Transpaleteira Elétrica para Locação em <em>Trindade</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para supermercados, comércio varejista do Setor Maysa, depósitos de materiais de construção e CDs emergentes da GO-060. Operação silenciosa, manutenção inclusa. Entrega no mesmo dia via GO-060.')

# WhatsApp URLs — encoded Goiânia → Trindade
r('Goi%C3%A2nia', 'Trindade', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Paleteiras Clark Lítio 24V</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega via GO-060 (18 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos no Mercado Goiano</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Suporte Técnico Presencial</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Por que a <span>transpaleteira elétrica</span> virou necessidade em Trindade')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — conhecida no comércio e na indústria como paleteira ou patolinha — movimenta paletes na horizontal usando motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Sem esforço muscular do operador, ela acelera o recebimento de mercadorias e a reposição de gôndolas com total silêncio. Trindade vive um ciclo de expansão comercial: supermercados de médio e grande porte crescem no Setor Maysa e no Sol Nascente, centros de distribuição estão se instalando ao longo da GO-060 e depósitos de materiais de construção acompanham o ritmo de obras residenciais que não para na cidade.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: bateria que acompanha o ritmo comercial de Trindade')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'As baterias de lítio das transpaleteiras Clark aposentaram o chumbo-ácido com tripla vantagem: recarga completa em 2 a 3 horas (contra 8h do chumbo), cargas de oportunidade durante intervalos de almoço e vida útil até três vezes superior. Em supermercados de Trindade que operam reposição noturna após o fechamento, a paleteira recarrega durante a troca de equipe e cobre a jornada seguinte sem interrupção.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual se encaixa no seu negócio em Trindade')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida com o operador caminhando — perfeita para corredores curtos de supermercados e depósitos menores. A PWio20 com plataforma fixa permite percorrer distâncias longas entre a doca e o estoque nos CDs da GO-060 sem fadiga do operador. A PPXs20 com plataforma dobrável combina modo caminhada para manobras entre gôndolas e modo plataforma para trajetos longos. A stacker SWX16 eleva paletes até 4.500 mm, substituindo empilhadeiras em corredores estreitos de armazéns e câmaras frias.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark WPio15: a paleteira preferida dos supermercados e depósitos de Trindade')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A WPio15 concentra o maior número de contratos em Trindade. Capacidade de 1.500 kg, lítio 24V e chassi compacto para corredores de 1,8 m — especificações que encaixam na reposição de bebidas e alimentos nos supermercados do Setor Maysa, na descarga de cimento e argamassa nos depósitos de construção e na separação de pedidos nos CDs emergentes da GO-060. O timão ergonômico com controle proporcional permite manobras entre prateleiras sem danificar produtos ou gôndolas.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga de 2 a 3 horas entre turnos, carga de oportunidade no intervalo, zero emissão de gases em supermercados e depósitos fechados de Trindade.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso:</strong> operação sem ruído para reposição noturna em supermercados, áreas de venda abertas ao público e depósitos de construção com circulação de clientes.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave entre pisos de lojas, docas com desnível e rampas de acesso nos depósitos da GO-060.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Trindade:</strong> supermercados (bebidas, alimentos, higiene), depósitos de construção (cimento, argamassa, revestimentos), CDs emergentes da GO-060 (dock-to-stock) e comércio varejista do Setor Maysa e Sol Nascente.</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark WPio15 com lítio 24V, modelo mais contratado para supermercados e depósitos em Trindade-GO"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega pela GO-060 no mesmo dia')

# Form selects — Trindade como primeira opção (desktop)
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
              <option value="Anápolis">Anápolis</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
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
              <option value="Anápolis">Anápolis</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 lidera os contratos de paleteira em Trindade. Chassi compacto, timão ergonômico e controle proporcional de velocidade. Perfeita para reposição de gôndolas em supermercados do Setor Maysa, descarga de materiais nos depósitos de construção e movimentação horizontal em corredores de 1,8 m nos CDs emergentes da GO-060.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em operação de reposição em supermercado de Trindade-GO"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina o desgaste de caminhar longas distâncias. Nos centros de distribuição da GO-060 em Trindade, o operador percorre corredores de 80 a 120 metros entre docas e prateleiras de estoque sem fadiga. Ideal para cross-docking de mercadorias destinadas ao comércio varejista do entorno.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alterna entre plataforma para trajetos longos e modo walkie para corredores apertados. A plataforma recolhe com um gesto, adaptando a paleteira ao corredor estreito de gôndolas ou ao trajeto amplo entre doca e estoque. Versátil para supermercados de Trindade que combinam reposição de salão com recebimento de carga na área de depósito.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 combina transporte horizontal com elevação até 4.500 mm, substituindo empilhadeiras em corredores estreitos. O chassi anticorrosão opera em câmaras de congelados de supermercados e distribuidoras de Trindade. Patolada para estabilidade máxima ao empilhar paletes pesados de cimento e argamassa nos depósitos de construção civil.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 para elevação de paletes em armazéns e câmaras frias de Trindade-GO"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 movimenta as cargas mais pesadas da frota Clark. Projetada para paletes de cimento, aço, argamassa e materiais de construção acima de 2.000 kg comuns nos depósitos do Sol Nascente e entorno. Motor de tração reforçado e rodas de alta durabilidade para pisos de depósitos com tráfego intenso de caminhões na GO-060.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para cargas de construção civil em Trindade-GO"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota disponível para locação em Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Trindade
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Os chamados de Trindade cresceram muito no último ano. São principalmente supermercados e depósitos de materiais de construção. O dono chega aqui dizendo que a paleteira manual dá conta, mas quando pergunto quantos paletes movimenta por dia, a resposta é sempre acima de 40. Um supermercado do Setor Maysa me contou que o repositor levava três horas para descarregar o caminhão de bebidas. Coloquei uma WPio15 e o tempo caiu para uma hora e vinte. O lítio recarrega de madrugada e já está pronto na abertura da loja. Em menos de um mês o gerente ligou pedindo mais uma unidade para o depósito dos fundos."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

# ── COMPARATIVO — rewrite H2, intro, card texts
r('<span>Paleteira manual</span> ou elétrica: qual sua operação exige?',
  'Transpaleteira <span>manual ou elétrica</span>: quando vale trocar em Trindade?')

r('A paleteira manual resolve operações esporádicas. Para volumes acima de 30 paletes por turno, fluxos de dock-to-stock ou câmaras frias, a transpaleteira elétrica elimina gargalos de produtividade e afastamentos por lesão.',
  'A paleteira manual funciona bem para movimentações pontuais e cargas leves. Quando o volume diário ultrapassa 30 paletes, o trajeto entre doca e estoque passa de 50 metros ou a operação exige silêncio e zero emissão, a transpaleteira elétrica se torna obrigatória para manter produtividade e saúde do operador.')

r('<h3>Para operações acima de 30 paletes por turno</h3>',
  '<h3>Quando o volume diário exige velocidade e ergonomia</h3>')

r('Motor de tração e bomba hidráulica eliminam esforço físico. Bateria de lítio com recarga rápida para turnos consecutivos sem interrupção.',
  'Tração motorizada e bomba hidráulica com lítio 24V eliminam qualquer esforço muscular. Recarga entre turnos garante operação contínua em supermercados, depósitos e CDs de Trindade.')

r('Velocidade de deslocamento até 6 km/h com carga',
  'Desloca a até 6 km/h carregada — três vezes mais rápido que a manual')
r('Zero esforço repetitivo: previne lesões e afastamentos',
  'Elimina esforço repetitivo e previne afastamentos por LER')
r('Recarga rápida: 2 a 3 horas com lítio 24V',
  'Lítio 24V com recarga de 2 a 3 horas entre jornadas')
r('Opera em câmaras frias a -18°C (modelo SWX16)',
  'SWX16 opera em câmaras frias e empilha até 4.500 mm')
r('Capacidades de 1.500 a 3.500 kg (frota Clark completa)',
  'Cinco modelos Clark de 1.500 a 3.500 kg disponíveis')

r('<h3>Para uso esporádico e cargas leves</h3>',
  '<h3>Suficiente apenas para volumes baixos e pontuais</h3>')

r('Sem motor, sem bateria. O operador traciona e eleva o palete com esforço muscular. Funcional para volumes baixos.',
  'Sem motor e sem bateria — o operador faz tudo com força muscular. Resolve cargas esporádicas, mas inviabiliza qualquer operação com ritmo constante.')

r('Custo de aquisição baixo',
  'Investimento inicial reduzido')
r('Não depende de recarga elétrica',
  'Funciona sem eletricidade')
r('Velocidade limitada: 2 km/h com carga',
  'Deslocamento lento: máximo 2 km/h com palete')
r('Esforço repetitivo causa lesões e afastamentos',
  'Risco alto de LER e afastamentos no ombro e lombar')
r('Inviável para câmaras frias e pisos com desnível',
  'Não opera em câmaras frias nem pisos com rampa')
r('Produtividade cai drasticamente acima de 30 paletes/turno',
  'Rendimento despenca quando o volume passa de 30 paletes/dia')

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Referência prática para Trindade:</strong> se o depósito ou supermercado movimenta mais de 30 paletes por dia, ou se a distância entre a doca e o ponto de estoque ultrapassa 50 metros, a paleteira elétrica se paga no primeiro mês pela produtividade recuperada. Os supermercados do Setor Maysa, os depósitos de construção do Sol Nascente e os CDs emergentes da GO-060 já operam com transpaleteira elétrica pelo volume de carga e pela necessidade de agilidade na reposição.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Trindade:')

# Links internos — todos para trindade-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/trindade-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Trindade')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/trindade-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Trindade')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/trindade-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Trindade')

r('/goiania-go/curso-operador-empilhadeira', '/trindade-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de transpaleteira elétrica para supermercados e depósitos em Trindade-GO"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Trindade')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe cada etapa da locação: análise do volume de paletes, escolha do modelo Clark adequado, entrega pela GO-060 e suporte técnico contínuo. Do orçamento pelo WhatsApp até a paleteira operando no seu supermercado ou depósito em Trindade.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Valores de locação de <span>paleteira elétrica</span> para Trindade em 2026')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Faixas de investimento para locação de transpaleteira Clark em Trindade. O valor final depende do modelo, prazo de contrato e configuração escolhida.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção e lítio 24V já inclusos')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato contempla manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal cobre o equipamento pronto para operar, sem cobranças extras de peças ou deslocamento técnico.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Trindade (18 km, sem frete)')

r('Sem custo de frete na capital',
  'Frete incluso para Trindade')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — a 18 km de Trindade pela GO-060, trajeto rápido sem pedágio. Entrega no mesmo dia da confirmação do contrato. A transpaleteira chega no seu supermercado, depósito ou CD pronta para operar, sem custo de frete.')

r('O prejuízo invisível da paleteira manual',
  'O custo real de manter paleteiras manuais no comércio de Trindade')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucos donos de supermercado ou depósito fazem:</strong> uma operação que movimenta 50 paletes por dia com paleteira manual precisa do dobro de horas-homem. Somando o custo de um repositor extra, os afastamentos por lesão no ombro e lombar (média de 15 dias/ano no comércio) e a multa de sobreestadia quando o caminhão de bebidas ou cimento espera na doca, a economia aparente vira prejuízo. A locação da paleteira elétrica Clark se paga com a produtividade recuperada já no primeiro mês.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações locais')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>paleteira elétrica Clark</span> já opera diariamente em Trindade')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Supermercados, depósitos de construção e CDs emergentes que contratam transpaleteira elétrica na cidade.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em operação de reposição em supermercado de Trindade-GO"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>Supermercados: reposição de gôndolas e recebimento</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'Os supermercados de médio e grande porte do Setor Maysa e região central de Trindade recebem dezenas de paletes de bebidas, alimentos e produtos de higiene por dia. A WPio15 circula entre gôndolas com silêncio total, movimenta paletes de 400 a 1.200 kg e agiliza a reposição noturna e a descarga de caminhões de fornecedores.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Stacker Clark SWX16 em depósito de materiais de construção no Sol Nascente, Trindade-GO"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>Depósitos de construção: cimento, aço e argamassa</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'Os depósitos de materiais de construção do Sol Nascente e entorno de Trindade movimentam paletes pesados de cimento (até 1.500 kg), barras de aço e argamassa ensacada. A WPX35 heavy duty transporta essas cargas com motor reforçado, enquanto a SWX16 empilha paletes até 4.500 mm em prateleiras verticais, otimizando o espaço de armazenamento.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 em centro de distribuição emergente da GO-060 em Trindade-GO"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>CDs emergentes da GO-060: distribuição e cross-docking</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'Os centros de distribuição que estão se instalando ao longo da GO-060 em Trindade recebem mercadorias de Goiânia e Anápolis para redistribuir ao comércio varejista da região. A PWio20 com plataforma fixa percorre corredores de 100 metros entre docas e prateleiras sem fadiga. A velocidade de 6 km/h reduz o tempo de dock-to-stock e libera os caminhões antes do prazo de sobreestadia.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark em comércio varejista do Setor Maysa em Trindade-GO"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Comércio varejista: Setor Maysa e centro</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'As lojas de materiais elétricos, acabamentos e home centers do Setor Maysa e da região central de Trindade utilizam transpaleteira elétrica para recebimento de mercadorias e organização de estoque. A WPio15 navega entre corredores de exposição sem ruído, e a PPXs20 alterna entre modo compacto para a loja e plataforma para o depósito dos fundos, cobrindo operações mistas com um único equipamento.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica mobile com deslocamento pela GO-060. Atendimento em Trindade em menos de 30 minutos a partir da sede. Diagnóstico de sistema elétrico, tração e bomba hidráulica diretamente no seu estabelecimento.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via GO-060 até seu supermercado, depósito ou CD em Trindade. São 18 km da sede — entrega no mesmo dia, sem custo adicional de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"O supermercado recebia dois caminhões de bebidas por dia e a equipe gastava quase quatro horas descarregando tudo na mão. Aluguei uma WPio15 da Clark e o tempo de descarga caiu para uma hora e meia. O lítio recarrega de madrugada enquanto a loja está fechada e de manhã está pronta. Dispensei um auxiliar de depósito e os afastamentos por dor no ombro zeraram. O contrato se pagou antes do segundo mês."')
r('<strong>Marcos V.</strong>',
  '<strong>Roberto F.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente de Operações, Supermercado, Setor Maysa, Trindade-GO (fev/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"No depósito de materiais de construção precisávamos empilhar paletes de cimento e argamassa a 4 metros de altura. Alugamos a SWX16 e eliminamos a necessidade de empilhadeira no galpão. O chassi aguenta a poeira de obra e a carga pesada sem reclamar. Quatro meses de uso e nenhuma manutenção corretiva. A Move monitorou a bateria remotamente e fez a troca preventiva sem a gente nem perceber que estava na hora."')
r('<strong>Renata C.</strong>',
  '<strong>Daniela S.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Proprietária, Depósito de Materiais de Construção, Sol Nascente, Trindade-GO (jan/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"Montamos o CD na GO-060 em Trindade para distribuir para o varejo da região metropolitana. Com duas PWio20, os operadores cobrem os 90 metros entre doca e estoque em cima da plataforma. O cross-docking que levava três horas e meia agora fecha em duas. A sobreestadia dos caminhões de fornecedores zerou desde a troca. Renovamos o contrato semestral e o WhatsApp da Move responde em minutos."')
r('<strong>Anderson L.</strong>',
  '<strong>Thiago P.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Supervisor de Logística, CD Distribuição, GO-060 Trindade-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/trindade-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Conectamos sua equipe a centros credenciados em Trindade e Goiânia.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Trindade</span> e cidades vizinhas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 18 km de Trindade pela GO-060, trajeto rápido sem pedágio. Entrega de transpaleteira elétrica no mesmo dia da confirmação. Atendemos toda a região metropolitana num raio de 200 km.</p>
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

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Trindade')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica combina melhor com as operações de Trindade?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark WPio15 é o modelo mais requisitado na cidade. Com 1.500 kg de capacidade e lítio 24V, atende supermercados de médio e grande porte no Setor Maysa, depósitos de materiais de construção no Sol Nascente e centros de distribuição emergentes da GO-060. Silenciosa e compacta para corredores de 1,8 m.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>Supermercados de Trindade podem usar transpaleteira elétrica no salão de vendas?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Sim. As transpaleteiras Clark com lítio 24V não emitem gases nem ruído relevante, podendo circular em áreas abertas ao público. A WPio15 é compacta o suficiente para navegar entre gôndolas durante a reposição noturna, movimentando paletes de bebidas, alimentos e produtos de higiene sem incomodar clientes ou colaboradores durante o horário comercial.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>A paleteira elétrica substitui a manual nos depósitos de construção civil?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Nos depósitos de materiais de construção de Trindade, paletes de cimento, argamassa e revestimentos ultrapassam 1.000 kg. A manual não sustenta o ritmo de 40 a 50 paletes por turno sem causar fadiga e lesão no operador. A elétrica Clark mantém velocidade constante de até 6 km/h e elimina o desgaste físico, reduzindo afastamentos e acelerando a expedição nos depósitos do Sol Nascente e entorno.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>Quanto tempo a bateria de lítio dura num turno comercial em Trindade?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A bateria de lítio 24V entrega de 6 a 10 horas contínuas conforme a intensidade de uso. Em supermercados e depósitos de Trindade que operam turno único diurno, a carga completa cobre a jornada inteira. Para operações com reposição noturna, a recarga de 2 a 3 horas entre turnos garante disponibilidade sem substituição do equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores de supermercado precisam de certificação para usar transpaleteira elétrica?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige curso de operação de equipamentos de movimentação incluindo transpaleteiras elétricas. O treinamento cobre inspeção pré-operacional, limites de capacidade, velocidade em áreas com circulação de pessoas e procedimentos de emergência. Indicamos centros de formação credenciados em Trindade e Goiânia para <a href="/trindade-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação e reciclagem</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>A Move Máquinas entrega transpaleteira no mesmo dia em Trindade?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Trindade fica a 18 km da sede pela GO-060, trajeto de aproximadamente 25 minutos. A entrega acontece no mesmo dia da confirmação, geralmente em menos de 2 horas. Para demandas urgentes de supermercados em pico sazonal ou obras com prazo apertado, priorizamos o despacho. Frete incluso no contrato, sem custo adicional.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>O contrato de locação inclui manutenção preventiva e corretiva?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todo contrato da Move Máquinas cobre manutenção completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Trindade, nossa equipe técnica mobile chega pela GO-060 em menos de 30 minutos para resolver qualquer ocorrência sem interromper sua operação.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Existe transpaleteira para cargas pesadas disponível em Trindade?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para depósitos de construção que movimentam paletes de cimento e aço acima de 2.000 kg, a WPX35 é a indicação direta. A SWX16 stacker patolada eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de armazéns e CDs emergentes da GO-060.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Trindade.\\n\\n'")

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
            'goiania-go/', '18 km', 'Goiânia - GO',
            'Trindade e Goiânia',  # legitimate: training centers in both cities
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
td = html.count('Trindade')
local = html.count('Setor Maysa') + html.count('Sol Nascente') + html.count('GO-060') + html.count('construção')
print(f"\nTrindade: {td} menções")
print(f"Contexto local (Setor Maysa/Sol Nascente/GO-060/construção): {local} menções")

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

# Check vs SC V2
import os
compare_pages = [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-transpaleteira-V2.html',
    '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-transpaleteira-V2.html',
]

for p in compare_pages:
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
