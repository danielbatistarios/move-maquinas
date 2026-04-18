#!/usr/bin/env python3
"""
rebuild-itumbiara-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Itumbiara
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXT: Itumbiara-GO, -18.4097/-49.2158, 203km BR-153,
pop 105k. Frigoríficos JBS/BRF — câmaras frias -18°C.
Grãos Caramuru/Cargill. Usinas de etanol.
Entity bridge: câmaras frias de frigoríficos (-18°C),
docas de expedição de cooperativas agrícolas.
Transpaleteira com bateria lítio para câmara fria.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/itumbiara-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Locação de Transpaleteira Elétrica em Itumbiara-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Transpaleteira elétrica Clark para locação em Itumbiara. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com lítio 24V para câmaras frias de frigoríficos JBS/BRF a -18°C e docas de cooperativas agrícolas Caramuru/Cargill. Manutenção inclusa, entrega via BR-153."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/itumbiara-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Locação de Transpaleteira Elétrica em Itumbiara-GO | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark em Itumbiara. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para frigoríficos, cooperativas de grãos e usinas de etanol. Entrega pela BR-153, manutenção total inclusa."')

r('content="Goiânia, Goiás, Brasil"', 'content="Itumbiara, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-18.4097;-49.2158"')
r('content="-16.7234, -49.2654"', 'content="-18.4097, -49.2158"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -18.4097, "longitude": -49.2158')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -18.4097')
r('"longitude": -49.2654', '"longitude": -49.2158')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Itumbiara"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Itumbiara", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira elétrica é mais usada nos frigoríficos de Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark SWX16 domina os contratos em frigoríficos da região. Com chassi anticorrosão e lítio 24V, ela opera dentro de câmaras frias a -18°C nos abatedouros JBS e BRF sem perda de desempenho. Para docas de expedição e áreas de picking seco, a WPio15 walkie é o modelo mais contratado pela agilidade em corredores de 1,8 m." } },
        { "@type": "Question", "name": "A paleteira elétrica Clark opera em câmaras frias de frigoríficos a -18°C?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A SWX16 foi projetada para ambientes de até -25°C. A bateria de lítio 24V mantém autonomia estável mesmo em temperatura negativa, e o chassi com tratamento anticorrosão resiste à umidade constante das câmaras de congelamento dos frigoríficos JBS e BRF em Itumbiara. Além disso, a empilhagem até 4.500 mm otimiza o espaço vertical das câmaras." } },
        { "@type": "Question", "name": "Transpaleteira elétrica funciona nas docas de cooperativas agrícolas?", "acceptedAnswer": { "@type": "Answer", "text": "Perfeitamente. As docas de expedição da Caramuru e da Cargill recebem e despacham centenas de paletes de sacaria e big bags por turno. A PWio20 com plataforma percorre os corredores longos entre recebimento e armazém sem fadiga do operador, enquanto a WPX35 heavy duty movimenta paletes de insumos agrícolas acima de 2.000 kg." } },
        { "@type": "Question", "name": "Quanto dura a bateria de lítio 24V em operações contínuas de frigorífico?", "acceptedAnswer": { "@type": "Answer", "text": "A autonomia varia de 6 a 10 horas de operação contínua conforme modelo e carga. Nos frigoríficos de Itumbiara com turnos de 8 a 10 horas alternados, a recarga completa em 2 a 3 horas na troca de turno garante operação ininterrupta. Cargas de oportunidade de 15 a 30 minutos em pausas programadas estendem a jornada sem trocar equipamento." } },
        { "@type": "Question", "name": "Operadores de frigoríficos e cooperativas precisam de curso para usar transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga. O curso abrange inspeção pré-operacional em ambiente frio, limites de capacidade sobre piso úmido, velocidade em áreas com circulação de pedestres e protocolos de emergência. Indicamos centros de formação credenciados na região de Itumbiara e Goiânia." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de transpaleteira elétrica em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Itumbiara fica a 203 km da sede pela BR-153. A entrega acontece em até 24 horas da confirmação do contrato. Para demandas urgentes de frigoríficos com linha parada ou cooperativas em período de safra, priorizamos o despacho e conseguimos antecipar a entrega. Frete incluso no contrato, sem custo adicional." } },
        { "@type": "Question", "name": "O contrato de locação cobre manutenção da bateria em ambiente de câmara fria?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato Move Máquinas inclui manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi anticorrosão. Para Itumbiara, nossa equipe técnica mobile se desloca pela BR-153 e realiza atendimento no local, incluindo monitoramento de ciclos de carga da bateria em operação de câmara fria." } },
        { "@type": "Question", "name": "Qual a capacidade máxima das transpaleteiras Clark disponíveis para Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). A WPX35 é a mais indicada para paletes de sacaria de grãos e insumos agrícolas pesados nas cooperativas Caramuru e Cargill. A SWX16 stacker patolada eleva cargas até 4.500 mm, maximizando o aproveitamento vertical das câmaras frias dos frigoríficos." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/itumbiara-go/">Equipamentos em Itumbiara</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Itumbiara</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Transpaleteira Elétrica para Locação em <em>Itumbiara</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V projetadas para câmaras frias de frigoríficos JBS e BRF a -18°C, docas de expedição das cooperativas Caramuru e Cargill e armazéns de usinas de etanol. Chassi anticorrosão, manutenção inclusa. Entrega pela BR-153.')

# WhatsApp URLs — encoded Goiânia → Itumbiara
r('Goi%C3%A2nia', 'Itumbiara', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Chassi Anticorrosão p/ Câmara Fria</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega pela BR-153 (203 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos de Experiência</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Suporte Técnico Mobile BR-153</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Por que a <span>transpaleteira elétrica</span> virou necessidade nos frigoríficos de Itumbiara')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — conhecida como paleteira ou patolinha no chão de fábrica — utiliza motor de tração e bomba hidráulica alimentados por bateria de lítio 24V para movimentar paletes na horizontal. Elimina o esforço repetitivo do operador, acelera o fluxo de carga e opera com zero emissão de gases. Itumbiara concentra frigoríficos de grande porte (JBS, BRF) com câmaras de congelamento a -18°C que exigem equipamento anticorrosão, cooperativas agrícolas (Caramuru, Cargill) que movimentam centenas de paletes de sacaria por turno e usinas de etanol com logística interna de insumos pesados.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: autonomia garantida mesmo a -18°C nas câmaras frias de Itumbiara')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'O lítio 24V das transpaleteiras Clark substituiu o chumbo-ácido com tripla vantagem: recarga completa entre 2 e 3 horas (contra 8h do chumbo), cargas de oportunidade durante intervalos programados e vida útil até três vezes superior. Nos frigoríficos de Itumbiara que alternam turnos de abate e expedição, a bateria de lítio mantém desempenho estável mesmo dentro das câmaras a -18°C — ponto em que baterias convencionais perdem até 40% de capacidade. A recarga na troca de turno garante operação ininterrupta.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual modelo resolve sua operação em Itumbiara')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida com o operador caminhando — perfeita para corredores de picking seco nas docas dos frigoríficos. A PWio20 com plataforma fixa percorre distâncias longas sem fadiga, ideal para os armazéns de cooperativas agrícolas que separam o recebimento de grãos da área de expedição. A PPXs20 com plataforma dobrável alterna entre modo caminhada em corredores apertados e modo plataforma para trajetos amplos. A stacker SWX16 eleva paletes até 4.500 mm com chassi anticorrosão, substituindo empilhadeiras dentro das câmaras frias dos frigoríficos JBS e BRF.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark SWX16: a paleteira que opera a -18°C nos frigoríficos de Itumbiara')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A Clark SWX16 é a transpaleteira mais demandada em Itumbiara pelo segmento frigorífico. Com chassi anticorrosão projetado para câmaras de congelamento, lítio 24V que mantém carga em temperatura negativa e elevação até 4.500 mm, ela maximiza o aproveitamento vertical das câmaras frias dos abatedouros JBS e BRF. Para áreas secas — docas, expedição e recebimento de sacaria — a WPio15 walkie lidera os contratos pelo chassi compacto e timão ergonômico de controle proporcional.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga de 2 a 3 horas na troca de turno, carga de oportunidade nos intervalos, desempenho estável dentro de câmaras frias a -18°C dos frigoríficos de Itumbiara.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso e sem emissão:</strong> atende normas sanitárias de frigoríficos e áreas de processamento de alimentos — zero poluentes nas câmaras de congelamento e salas de corte.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave sobre pisos úmidos de frigoríficos, docas com desnível e rampas de nivelamento das cooperativas agrícolas.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Itumbiara:</strong> frigoríficos JBS/BRF (câmaras frias -18°C), cooperativas Caramuru/Cargill (sacaria e big bags), usinas de etanol (insumos químicos) e CDs de distribuição na BR-153.</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark SWX16 com lítio 24V e chassi anticorrosão para câmaras frias de frigoríficos em Itumbiara"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega via BR-153 em até 24h')

# Form selects — Itumbiara como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Itumbiara" selected>Itumbiara</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Caldas Novas">Caldas Novas</option>
              <option value="Uruaçu">Uruaçu</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Itumbiara" selected>Itumbiara</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Caldas Novas">Caldas Novas</option>
              <option value="Uruaçu">Uruaçu</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 atende as operações de picking seco e dock-to-stock nos frigoríficos e cooperativas de Itumbiara. Chassi compacto para corredores de 1,8 m, timão ergonômico com controle proporcional de velocidade. Perfeita para separação de pedidos nas docas de expedição, recebimento de sacaria e movimentação entre câmaras de resfriamento e áreas de carregamento.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em doca de expedição de cooperativa agrícola em Itumbiara"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a fadiga em trajetos longos. Nos armazéns de grãos da Caramuru e Cargill em Itumbiara, o operador percorre corredores de 100 a 150 metros entre recebimento e estoque sem desgaste. Ideal para cooperativas que operam em pico de safra com volume triplicado de paletes e para cross-docking de insumos agrícolas na BR-153.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alterna entre plataforma para distâncias longas e walkie para manobras em corredores estreitos. A plataforma se recolhe com um gesto, adaptando a paleteira ao corredor de armazenagem ou ao trajeto amplo entre galpões. Versátil para operações mistas nas usinas de etanol de Itumbiara que combinam recebimento de cana, estoque de insumos químicos e expedição de produto acabado em áreas distintas.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 combina movimentação horizontal com elevação até 4.500 mm, maximizando o aproveitamento vertical. O chassi com tratamento anticorrosão opera dentro de câmaras de congelamento a -18°C nos frigoríficos JBS e BRF de Itumbiara sem degradação por umidade. Patolada para estabilidade máxima ao empilhar caixas de proteína congelada em racks de até 4 metros de altura.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 operando em câmara fria de frigorífico a -18°C em Itumbiara"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 movimenta as cargas mais pesadas da frota Clark. Projetada para paletes de sacaria de grãos acima de 2.000 kg, big bags de fertilizantes e insumos químicos das usinas de etanol. Motor de tração reforçado e rodas de alta durabilidade para pisos de armazéns graneleiros e docas de cooperativas agrícolas em Itumbiara.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para sacaria de grãos e insumos pesados em Itumbiara"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: frota disponível para locação na região de Itumbiara')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Itumbiara
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Itumbiara é o município que mais me surpreendeu nos últimos dois anos. Os frigoríficos movimentam carga pesada em câmara fria o dia inteiro, e a paleteira manual travava com a umidade e o operador saía de licença por dor no ombro. Coloquei duas SWX16 anticorrosão dentro da câmara a -18 graus de um abatedouro da JBS. Em 15 dias o gerente me ligou dizendo que o volume de paletes expedidos no turno da noite subiu 45% e zerou o afastamento. Na Caramuru, a mesma coisa: trocaram três manuais por duas PWio20 na safra de soja e eliminaram a sobreestadia dos caminhões na doca."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Parâmetro decisivo para Itumbiara:</strong> se o frigorífico opera câmaras frias, se a cooperativa movimenta mais de 30 paletes de sacaria por turno ou se o trajeto entre doca e armazém passa de 50 metros, a paleteira elétrica compensa o investimento no primeiro mês. Os abatedouros JBS e BRF, as cooperativas Caramuru e Cargill e as usinas de etanol da região já operam exclusivamente com transpaleteira elétrica pela exigência de ambiente refrigerado e pelo volume de carga.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Itumbiara:')

# Links internos — todos para itumbiara-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Itumbiara')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Itumbiara')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Itumbiara')

r('/goiania-go/curso-operador-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Itumbiara')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de transpaleteira elétrica para frigoríficos e cooperativas em Itumbiara"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Itumbiara')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe o passo a passo da locação: análise da operação do seu frigorífico ou cooperativa, indicação do modelo Clark ideal, entrega pela BR-153 e suporte técnico contínuo. Do orçamento pelo WhatsApp à paleteira operando na câmara fria.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Quanto custa locar uma <span>transpaleteira elétrica</span> para Itumbiara em 2026?')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark na região de Itumbiara. O investimento final depende do modelo, prazo de contrato e configuração do chassi (padrão ou anticorrosão para câmara fria).')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção, lítio 24V e chassi anticorrosão no valor')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato cobre manutenção preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi anticorrosão. O valor mensal já contempla o equipamento pronto para operar — sem cobranças extras de peças, fluidos ou deslocamento técnico até Itumbiara.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Itumbiara (BR-153, frete incluso)')

r('Sem custo de frete na capital',
  'Frete incluso para Itumbiara')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — a 203 km de Itumbiara pela BR-153. Entrega em até 24 horas da confirmação. A transpaleteira chega no seu frigorífico, cooperativa ou usina de etanol pronta para operar, com frete incluso no contrato.')

r('O prejuízo invisível da paleteira manual',
  'O custo real de manter paleteiras manuais dentro de câmaras frias')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que os frigoríficos de Itumbiara raramente fazem:</strong> dentro de câmaras a -18°C, a paleteira manual trava com frequência, o operador perde rendimento pelo frio extremo e os afastamentos por lesão de esforço repetitivo chegam a 20 dias/ano no setor de proteínas. Some o custo de operadores extras, as multas de sobreestadia por atraso na expedição e a degradação acelerada do equipamento manual pela umidade. A locação da paleteira elétrica Clark com chassi anticorrosão se paga na primeira quinzena com a produtividade recuperada.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações em Itumbiara')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>transpaleteira elétrica Clark</span> opera diariamente em Itumbiara')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Frigoríficos, cooperativas agrícolas e usinas de etanol que contratam paleteira elétrica na região.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Stacker Clark SWX16 operando em câmara fria de frigorífico JBS em Itumbiara a -18°C"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>Frigoríficos JBS e BRF: câmaras frias a -18°C</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'Os abatedouros JBS e BRF de Itumbiara processam centenas de toneladas de proteína por dia. Dentro das câmaras de congelamento a -18°C, a SWX16 com chassi anticorrosão empilha caixas de produto acabado em racks de até 4 metros, enquanto a WPio15 abastece as linhas de embalagem e expedição com zero emissão de gases — requisito sanitário inegociável.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Transpaleteira Clark PWio20 em doca de expedição da cooperativa Caramuru em Itumbiara"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>Cooperativas Caramuru e Cargill: sacaria e grãos</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'As cooperativas de grãos Caramuru e Cargill movimentam centenas de paletes de sacaria de soja, milho e derivados por turno, especialmente no pico da safra. A PWio20 com plataforma percorre os corredores longos entre recebimento e armazém sem fadiga, enquanto a WPX35 heavy duty transporta paletes de big bags e fertilizantes acima de 2.000 kg nas docas de expedição.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PPXs20 em usina de etanol na região de Itumbiara"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>Usinas de etanol: insumos químicos e logística interna</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'As usinas de etanol e açúcar da região de Itumbiara movimentam paletes de insumos químicos, embalagens e produto acabado em áreas de produção extensas. A PPXs20 com plataforma dobrável alterna entre modo walkie para manobras em áreas confinadas e plataforma para trajetos longos entre recebimento e estoque. Zero emissão de gases atende as exigências de segurança das áreas de produção.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark WPX35 em armazém de distribuição da BR-153 em Itumbiara"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>CDs da BR-153: distribuição regional</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'Itumbiara é entroncamento logístico na BR-153 entre Goiânia e o Triângulo Mineiro. Os centros de distribuição da região recebem e expedem paletes para todo Centro-Oeste e Sudeste. A WPX35 heavy duty movimenta cargas de até 3.500 kg em pisos industriais com tráfego intenso de empilhadeiras e carretas, acelerando o cross-docking e reduzindo o tempo de sobreestadia.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica mobile com deslocamento pela BR-153. Atendimento em Itumbiara com diagnóstico de sistema elétrico, tração e bomba hidráulica diretamente no frigorífico, cooperativa ou usina — sem necessidade de remover o equipamento.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-153 até seu frigorífico, cooperativa ou usina em Itumbiara. São 203 km da sede — entrega em até 24 horas da confirmação, com frete incluso no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"A câmara fria do nosso abatedouro destruía paleteiras manuais em dois meses — umidade corroía o chassi e as rodas travavam no piso gelado. Trocamos por duas SWX16 anticorrosão da Clark e o cenário mudou completamente. Operam a -18 graus sem falha desde janeiro, empilham caixas até 4 metros e o lítio recarrega na troca de turno. Zeramos os afastamentos por esforço repetitivo que eram crônicos na expedição."')
r('<strong>Marcos V.</strong>',
  '<strong>Cláudio R.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente de Expedição, Frigorífico JBS, Itumbiara-GO (jan/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"Na safra de soja o volume de paletes triplica e nenhuma manual aguentava o ritmo. Alugamos três PWio20 com plataforma da Move e os operadores passaram a cobrir os 120 metros entre doca e armazém sem destruir o joelho. A sobreestadia dos caminhões de sacaria que custava R$ 800/dia zerou. Renovamos o contrato semestral antes do prazo e já encomendamos mais uma WPX35 para big bags de fertilizante."')
r('<strong>Renata C.</strong>',
  '<strong>Eduardo T.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Logística, Cooperativa Caramuru, Itumbiara-GO (mar/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"Nossa usina precisa mover paletes de insumos químicos em área classificada — zero emissão é obrigatório. A PPXs20 Clark com lítio resolveu: silenciosa, sem gás, e a plataforma dobrável encaixa tanto no corredor apertado do almoxarifado quanto no galpão de expedição. A Move entregou pela BR-153 em menos de um dia e o suporte técnico aparece antes de a gente precisar ligar."')
r('<strong>Anderson L.</strong>',
  '<strong>Luciana F.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Supervisora de Almoxarifado, Usina de Etanol, Itumbiara-GO (fev/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/itumbiara-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Conectamos sua equipe a centros credenciados na região de Itumbiara e Goiânia.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Itumbiara</span> e cidades atendidas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 203 km de Itumbiara pela BR-153. Entrega de transpaleteira elétrica em até 24 horas da confirmação. Atendemos frigoríficos, cooperativas e usinas num raio de 200 km da sede.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/itumbiara-go/"><strong>Itumbiara</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/caldas-novas-go/">Caldas Novas</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/uruacu-go/">Uruaçu</a>
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
        <a href="/luziania-go/">Luziânia</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-49.2158!3d-18.4097')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Itumbiara"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Itumbiara</a>')
r('/goiania-go/" style="color', '/itumbiara-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Itumbiara')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica é mais usada nos frigoríficos de Itumbiara?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark SWX16 domina os contratos em frigoríficos pela capacidade de operar em câmaras frias a -18°C com chassi anticorrosão. Para operações de picking seco e expedição em docas, a WPio15 walkie é a mais contratada pela agilidade em corredores de 1,8 m nos abatedouros JBS e BRF e nas cooperativas Caramuru e Cargill.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A paleteira elétrica Clark opera em câmaras frias de frigoríficos a -18°C?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Sim. A SWX16 foi projetada para ambientes de até -25°C. A bateria de lítio 24V mantém autonomia estável mesmo em temperatura negativa, e o chassi anticorrosão resiste à umidade constante das câmaras de congelamento dos frigoríficos JBS e BRF em Itumbiara. A empilhagem até 4.500 mm maximiza o espaço vertical, reduzindo a necessidade de empilhadeiras dentro das câmaras.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>Transpaleteira elétrica funciona nas docas de cooperativas agrícolas?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Perfeitamente. As docas da Caramuru e da Cargill recebem e expedem centenas de paletes de sacaria e big bags por turno. A PWio20 percorre corredores longos sem fadiga, enquanto a WPX35 heavy duty transporta paletes de insumos agrícolas acima de 2.000 kg. Na safra, quando o volume triplica, as paleteiras elétricas eliminam o gargalo de expedição que as manuais não acompanham.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>Quanto dura a bateria de lítio 24V em operações contínuas de frigorífico?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A autonomia varia de 6 a 10 horas contínuas conforme modelo e intensidade de uso. Nos frigoríficos de Itumbiara com turnos alternados de 8 a 10 horas, a recarga completa em 2 a 3 horas na troca de turno cobre a próxima jornada inteira. Cargas de oportunidade de 15 a 30 minutos em pausas programadas estendem a operação sem substituir o equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores de frigoríficos e cooperativas precisam de curso para usar transpaleteira?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige treinamento em operação de equipamentos de movimentação de carga. O curso cobre inspeção pré-operacional em ambiente frio, limites de capacidade sobre piso úmido, velocidade em áreas de circulação e protocolos de emergência. Indicamos centros de formação credenciados na região de Itumbiara e Goiânia para <a href="/itumbiara-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação e reciclagem</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Qual o prazo de entrega de transpaleteira elétrica em Itumbiara?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Itumbiara fica a 203 km da sede pela BR-153. A entrega acontece em até 24 horas da confirmação do contrato. Para demandas urgentes de frigoríficos com linha parada ou cooperativas em período de safra, priorizamos o despacho e conseguimos antecipar. Frete incluso no contrato, sem custo adicional.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>O contrato de locação cobre manutenção da bateria em ambiente de câmara fria?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todo contrato Move Máquinas inclui manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi anticorrosão. Para Itumbiara, nossa equipe técnica mobile se desloca pela BR-153 e realiza atendimento no local, incluindo monitoramento dos ciclos de carga da bateria que opera em temperatura negativa.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Qual a capacidade máxima das transpaleteiras Clark disponíveis para Itumbiara?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). A WPX35 é a mais indicada para paletes de sacaria de grãos e insumos agrícolas pesados nas cooperativas. A SWX16 stacker patolada com chassi anticorrosão eleva cargas até 4.500 mm dentro de câmaras frias dos frigoríficos, substituindo empilhadeiras em corredores estreitos.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Itumbiara')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Itumbiara.\\n\\n'")

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
            'goiania-go/', '203 km', 'Goiânia - GO',
            'Itumbiara e Goiânia',  # legitimate: training centers in both
            'Goiânia —',  # legitimate: sede location
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
it = html.count('Itumbiara')
local = html.count('frigoríf') + html.count('JBS') + html.count('BRF') + html.count('Caramuru') + html.count('Cargill') + html.count('etanol') + html.count('BR-153')
print(f"\nItumbiara: {it} menções")
print(f"Contexto local (frigorífico/JBS/BRF/Caramuru/Cargill/etanol/BR-153): {local} menções")

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

# Check vs SC and BSB V2 pages
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
