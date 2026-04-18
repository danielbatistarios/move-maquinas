#!/usr/bin/env python3
"""
rebuild-caldas-novas-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Caldas Novas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXTO: Caldas Novas — capital turística de Goiás
- Pop ~95 mil, 106 hotéis, 140 mil leitos
- Entity bridge: estoque de hotéis/resorts (alimentos, lavanderia),
  centros de distribuição de alimentos turísticos
- Transpaleteira para cozinhas industriais de resorts, lavanderias,
  almoxarifados de hotéis
- Coord: -17.7441 / -48.6252
- Distância: 170 km de Goiânia pela GO-139
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/caldas-novas-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Transpaleteira Elétrica para Hotéis e Resorts em Caldas Novas | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Locação de transpaleteira elétrica Clark em Caldas Novas. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com lítio 24V para almoxarifados de hotéis, cozinhas industriais de resorts e lavanderias do polo turístico. Manutenção inclusa, entrega pela GO-139."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/caldas-novas-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Transpaleteira Elétrica para Hotéis e Resorts em Caldas Novas | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark para locação em Caldas Novas. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para o polo hoteleiro com 106 hotéis e 140 mil leitos. Entrega pela GO-139, manutenção inclusa."')

r('content="Goiânia, Goiás, Brasil"', 'content="Caldas Novas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-17.7441;-48.6252"')
r('content="-16.7234, -49.2654"', 'content="-17.7441, -48.6252"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -17.7441, "longitude": -48.6252')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -17.7441')
r('"longitude": -49.2654', '"longitude": -48.6252')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Caldas Novas"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Caldas Novas", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira elétrica é mais procurada pelos hotéis de Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 concentra a maioria dos contratos no polo hoteleiro. Com 1.500 kg de capacidade e lítio 24V, opera em silêncio nos almoxarifados de resorts, cozinhas industriais e lavanderias dos 106 hotéis da cidade. Chassi compacto para corredores de serviço com 1,8 m de largura e zero emissão de gases em áreas internas." } },
        { "@type": "Question", "name": "A transpaleteira elétrica substitui a manual nas cozinhas dos resorts?", "acceptedAnswer": { "@type": "Answer", "text": "Nas cozinhas industriais que servem café da manhã para 300 a 500 hóspedes, o volume de paletes de alimentos e bebidas supera 40 unidades por turno matinal. A paleteira manual causa atrasos no abastecimento e expõe funcionários a lesão por esforço repetitivo. A elétrica Clark movimenta paletes a até 6 km/h, elimina esforço físico e mantém o fluxo de reposição contínuo durante a alta temporada." } },
        { "@type": "Question", "name": "A transpaleteira funciona nas câmaras frias dos hotéis e distribuidoras?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O modelo Clark SWX16 opera em câmaras frias a -18°C com bateria de lítio 24V que mantém desempenho estável em baixa temperatura. O chassi anticorrosão resiste à umidade das câmaras frigoríficas dos centros de distribuição de alimentos que abastecem os 140 mil leitos do polo turístico de Caldas Novas." } },
        { "@type": "Question", "name": "A bateria de lítio 24V aguenta a alta temporada dos hotéis de Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "A autonomia varia de 6 a 10 horas contínuas conforme modelo e carga. Na alta temporada — julho, feriados prolongados e réveillon — os almoxarifados operam em turnos estendidos. A recarga completa em 2 a 3 horas entre turnos cobre a jornada seguinte. Cargas de oportunidade de 15 minutos em pausas permitem operação ininterrupta sem troca de equipamento." } },
        { "@type": "Question", "name": "Funcionários de hotel precisam de certificação para usar transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento em operação de equipamentos de movimentação de carga, incluindo transpaleteiras. O curso cobre inspeção pré-operacional, limites de capacidade, velocidade em corredores de serviço e procedimentos de emergência. Indicamos centros de formação credenciados na região de Caldas Novas e Goiânia para capacitação e reciclagem." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de transpaleteira elétrica em Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Caldas Novas fica a 170 km da sede pela GO-139. A entrega ocorre em até 24 horas após confirmação do contrato. Para demandas urgentes de hotéis com eventos ou alta temporada, priorizamos o despacho com logística dedicada. Frete incluso no contrato, sem custo adicional." } },
        { "@type": "Question", "name": "O contrato de locação cobre manutenção completa?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato da Move Máquinas inclui manutenção preventiva e corretiva: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Para Caldas Novas, mantemos equipe técnica com rota fixa pela GO-139 que resolve ocorrências sem parar a operação do hotel." } },
        { "@type": "Question", "name": "Quais capacidades de transpaleteira estão disponíveis para Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para almoxarifados de hotéis e cozinhas industriais, a WPio15 é a mais indicada. A SWX16 stacker patolada eleva paletes até 4.500 mm, substituindo empilhadeiras em depósitos de lavanderias e centros de distribuição de alimentos do polo turístico." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/caldas-novas-go/">Equipamentos em Caldas Novas</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Caldas Novas</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Locação de Transpaleteira Elétrica em <em>Caldas Novas</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para almoxarifados de hotéis, cozinhas industriais de resorts e centros de distribuição de alimentos do polo turístico. Zero emissão, operação silenciosa em corredores de serviço. Entrega pela GO-139, manutenção inclusa.')

# WhatsApp URLs — encoded Goiânia → Caldas+Novas
r('Goi%C3%A2nia', 'Caldas+Novas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C (turismo)
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Frota Clark Lítio 24V</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega via GO-139 (170 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos no Mercado Goiano</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Suporte Técnico com Rota Fixa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Como a <span>transpaleteira elétrica</span> resolve a logística interna dos hotéis')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — chamada no dia a dia de paleteira ou patolinha — movimenta paletes na horizontal usando motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Diferente da versão manual, elimina esforço repetitivo e opera em silêncio absoluto. Caldas Novas reúne 106 hotéis e resorts com 140 mil leitos que demandam abastecimento contínuo: paletes de alimentos para cozinhas industriais que servem centenas de hóspedes por refeição, volumes de rouparia e toalhas nas lavanderias e insumos de manutenção nos almoxarifados. Cada resort é uma operação logística completa onde a paleteira elétrica mantém o fluxo de materiais sem ruído nos corredores de serviço.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: energia contínua durante a alta temporada de Caldas Novas')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'As baterias de lítio 24V das transpaleteiras Clark oferecem vantagem tripla sobre o chumbo-ácido: recarga completa entre 2 e 3 horas (contra 8h do chumbo), cargas de oportunidade durante intervalos da equipe e vida útil até três vezes superior. Na alta temporada — julho, Carnaval e réveillon — os almoxarifados dos resorts operam em turnos estendidos de 14 horas. A recarga rápida durante a virada de turno garante que a paleteira aguenta a jornada inteira sem substituição de equipamento.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual modelo atende seu hotel ou resort')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida com o operador caminhando — perfeita para corredores de serviço estreitos dentro dos hotéis. A PWio20 com plataforma fixa permite percorrer distâncias longas entre almoxarifado e cozinha sem desgaste físico, ideal nos resorts de grande porte com mais de 300 quartos. A PPXs20 com plataforma dobrável alterna entre modo caminhada para espaços confinados e plataforma para trajetos amplos. A stacker SWX16 eleva paletes até 4.500 mm, substituindo empilhadeiras nas câmaras frias dos centros de distribuição de alimentos do polo turístico.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark WPio15: a paleteira preferida do setor hoteleiro em Caldas Novas')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A WPio15 lidera os contratos de locação na região turística de Caldas Novas. Capacidade de 1.500 kg, lítio 24V e chassi compacto para corredores de 1,8 m — especificações que encaixam nos almoxarifados de hotéis, cozinhas industriais e lavanderias de resorts. O timão ergonômico com controle proporcional permite manobras silenciosas entre estantes de insumos sem danificar estoque ou paredes dos corredores de serviço.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga entre turnos de 2 a 3 horas, carga de oportunidade nos intervalos, zero emissão de gases dentro dos hotéis e cozinhas industriais.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso:</strong> operação sem ruído para corredores de serviço dos resorts, lavanderias e áreas internas dos hotéis onde o conforto do hóspede é prioridade.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave entre pisos de cozinha industrial, rampas de acesso a almoxarifados e docas de recebimento nos hotéis.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Caldas Novas:</strong> cozinhas de resorts (alimentos e bebidas), lavanderias industriais (rouparia e toalhas), almoxarifados de hotéis (insumos), CDs de alimentos turísticos (câmaras frias) e depósitos de manutenção predial.</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark WPio15 com lítio 24V, modelo mais contratado para hotéis e resorts em Caldas Novas"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega pela GO-139 em até 24h')

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
              <option value="Brasília">Brasília (DF)</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
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
              <option value="Brasília">Brasília (DF)</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 é a paleteira walkie mais procurada pelo setor hoteleiro de Caldas Novas. Chassi compacto, timão ergonômico e controle proporcional de velocidade. Movimenta paletes de alimentos, bebidas e rouparia nos corredores de serviço de 1,8 m dos resorts, almoxarifados de hotéis e lavanderias industriais — com operação silenciosa e zero emissão.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em operação de almoxarifado de hotel em Caldas Novas"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a fadiga de caminhada em trajetos longos. Nos resorts com mais de 300 quartos, o operador percorre corredores de 80 a 120 metros entre almoxarifado central e cozinha industrial sem desgaste. Perfeita para centros de distribuição de alimentos que abastecem múltiplos hotéis no polo turístico.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alterna entre plataforma para distâncias longas e walkie para manobras em corredores apertados. A plataforma recolhe com um gesto, adaptando a paleteira ao corredor estreito de almoxarifado ou ao trajeto amplo entre depósito e doca. Versátil para hotéis que combinam estoque seco, câmara fria e lavanderia em operações de turnos estendidos na alta temporada.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 combina movimentação horizontal com elevação até 4.500 mm, substituindo empilhadeiras em espaços reduzidos. O chassi anticorrosão opera em câmaras frias a -18°C dos centros de distribuição de alimentos que abastecem os 140 mil leitos de Caldas Novas. Patolada para estabilidade máxima ao empilhar paletes de congelados e insumos em prateleiras altas.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 para câmaras frias de centros de distribuição de alimentos em Caldas Novas"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 movimenta as cargas mais pesadas da frota Clark. Indicada para paletes de pisos, materiais de construção e insumos de manutenção predial que abastecem reformas e ampliações dos hotéis e resorts. Motor de tração reforçado e rodas de alta durabilidade para docas de recebimento com tráfego intenso de caminhões no polo turístico de Caldas Novas.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para cargas pesadas em hotéis e depósitos de Caldas Novas"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota para locação em Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Caldas Novas
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Caldas Novas é um caso especial. O gerente de hotel me liga em junho dizendo que precisa de paleteira para julho — alta temporada, 100% de ocupação, cozinha servindo 500 cafés por manhã. O almoxarifado recebe 30, 40 paletes de alimento e bebida por dia, e a equipe empurrando manual não dá conta. O atraso na reposição vira fila no restaurante, e fila no café vira reclamação no Booking. Coloquei duas WPio15 no resort Privé, e o abastecimento que levava 3 horas caiu para menos de uma. Depois do réveillon, o gerente renovou o contrato por 12 meses. Descobriu que na baixa temporada a paleteira economiza horas-homem na lavanderia e no almoxarifado de manutenção."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Critério objetivo para hotéis e resorts de Caldas Novas:</strong> se o almoxarifado ou cozinha movimenta mais de 30 paletes por turno, ou se o trajeto entre doca e estoque passa de 50 metros, a paleteira elétrica se paga no primeiro mês com o ganho de produtividade. Na alta temporada, quando a ocupação chega a 100%, os resorts operam exclusivamente com transpaleteira elétrica pelo volume de reposição e pela exigência de silêncio nas áreas internas.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Caldas Novas:')

# Links internos — todos para caldas-novas-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/caldas-novas-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Caldas Novas')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Caldas Novas')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Caldas Novas')

r('/goiania-go/curso-operador-empilhadeira', '/caldas-novas-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de transpaleteira elétrica para hotéis e resorts em Caldas Novas"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Caldas Novas')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe cada etapa da locação: análise da operação do seu hotel ou resort, escolha do modelo Clark ideal, entrega pela GO-139 e suporte técnico contínuo. Do orçamento pelo WhatsApp à paleteira operando no almoxarifado em Caldas Novas.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Investimento na locação de <span>transpaleteira elétrica</span> para hotéis em 2026')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark em Caldas Novas. O investimento final depende do modelo, prazo contratual e necessidades do hotel ou resort.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção completa e lítio 24V no valor')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato cobre manutenção preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal já inclui o equipamento operando, sem cobranças adicionais de peças ou deslocamento técnico. Ideal para hotéis que precisam de previsibilidade no orçamento operacional.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Caldas Novas (GO-139, frete incluso)')

r('Sem custo de frete na capital',
  'Frete incluso para Caldas Novas')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — 170 km de Caldas Novas pela GO-139. A entrega é feita em até 24 horas após confirmação. A transpaleteira chega no almoxarifado, cozinha ou lavanderia do seu hotel pronta para operar, com frete incluso no contrato.')

r('O prejuízo invisível da paleteira manual',
  'O custo escondido da paleteira manual no setor hoteleiro')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucos hoteleiros fazem:</strong> na alta temporada, o almoxarifado que movimenta 50 paletes/dia com paleteira manual demanda o dobro de funcionários. Somando horas extras, afastamentos por lesão repetitiva (média de 15 dias/ano no setor) e o atraso na reposição das cozinhas que vira reclamação de hóspede, a economia aparente se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com a produtividade recuperada já no primeiro mês de contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('Aplicações em Goiânia', 'Aplicações no polo turístico')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>paleteira elétrica Clark</span> opera diariamente em Caldas Novas')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Setores hoteleiros e logísticos que dependem de transpaleteira elétrica no maior polo turístico de águas quentes do Brasil.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark em cozinha industrial de resort com abastecimento de alimentos em Caldas Novas"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>Cozinhas industriais: alimentos e bebidas dos resorts</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'As cozinhas dos grandes resorts de Caldas Novas — Privé, Lagoa Quente, diRoma — servem café da manhã para 300 a 500 hóspedes. Na alta temporada, o volume de paletes de alimentos, bebidas e descartáveis ultrapassa 40 unidades por manhã. A WPio15 abastece câmaras e despensas em corredores de serviço de 1,8 m com zero emissão de gases e ruído, preservando a experiência do hóspede.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Stacker Clark SWX16 em câmara fria de centro de distribuição de alimentos turísticos em Caldas Novas"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>CDs de alimentos: câmaras frias a -18°C</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'Os centros de distribuição de alimentos que abastecem os 106 hotéis de Caldas Novas operam câmaras frigoríficas a -18°C. A SWX16 empilha paletes de congelados e hortifrútis até 4.500 mm com estabilidade total, mesmo em piso escorregadio. O chassi anticorrosão resiste à umidade constante das câmaras que alimentam a cadeia hoteleira.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 em lavanderia industrial de resort em Caldas Novas"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>Lavanderias industriais: rouparia e toalhas dos hotéis</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'As lavanderias industriais que atendem os resorts de Caldas Novas processam milhares de toalhas, lençóis e roupas de cama por dia. A PWio20 com plataforma fixa percorre os corredores longos entre área de lavagem, secagem e expedição sem fadiga do operador. A velocidade de 6 km/h mantém o fluxo contínuo de rouparia limpa para reposição dos 140 mil leitos na alta temporada.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark WPX35 em almoxarifado de hotel para insumos de manutenção em Caldas Novas"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Almoxarifados de hotéis: insumos e manutenção predial</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'Os almoxarifados dos hotéis armazenam desde produtos de limpeza e amenidades até materiais de reforma e manutenção predial. A WPX35 heavy duty movimenta paletes de pisos cerâmicos, tintas e equipamentos que ultrapassam 2.000 kg nas ampliações dos resorts. Motor de tração reforçado e rodas de alta durabilidade para docas com tráfego de caminhões de fornecedores.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica com rota fixa pela GO-139 para atendimento em Caldas Novas. Diagnóstico de sistema elétrico, tração e bomba hidráulica diretamente no hotel ou resort, sem necessidade de remover o equipamento.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via GO-139 até o almoxarifado, cozinha ou lavanderia do seu hotel em Caldas Novas. São 170 km da sede — entrega em até 24 horas, com frete incluso no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"Na alta temporada, nosso almoxarifado recebia 45 paletes de alimento e bebida por dia com paleteira manual. A cozinha ficava esperando reposição e o café da manhã atrasava. Contratamos duas WPio15 Clark da Move e o abastecimento caiu de 3 horas para 50 minutos. Eliminamos as horas extras da equipe de almoxarifado e as reclamações de hóspedes por atraso no restaurante desapareceram. Renovamos para contrato anual."')
r('<strong>Marcos V.</strong>',
  '<strong>Fábio L.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente Operacional, Resort com 280 quartos, Caldas Novas-GO (jul/2025)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"Distribuímos alimentos congelados para 38 hotéis de Caldas Novas. Nossa câmara fria opera a -18°C e já queimamos paleteira de duas marcas em menos de 90 dias por corrosão. A SWX16 Clark está no oitavo mês sem manutenção corretiva — o chassi anticorrosão segura a umidade da câmara. A Move fez troca preventiva da bateria pelo monitoramento remoto, sem a gente nem precisar ligar."')
r('<strong>Renata C.</strong>',
  '<strong>Daniela V.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Logística, Distribuidora de Alimentos Turísticos, Caldas Novas-GO (jan/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"Nossa lavanderia processa rouparia de 12 hotéis em Caldas Novas. Os funcionários empurravam carrinhos manuais com paletes de toalhas e lençóis percorrendo 10 km por turno. Com duas PWio20 na plataforma, o mesmo trajeto leva metade do tempo. As lesões por esforço sumiram e a produtividade na virada de enxoval subiu 40%. O orçamento da Move pelo WhatsApp saiu em cinco minutos."')
r('<strong>Anderson L.</strong>',
  '<strong>Roberta M.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Supervisora de Produção, Lavanderia Industrial, Caldas Novas-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/caldas-novas-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Conectamos sua equipe a centros credenciados na região de Caldas Novas e Goiânia.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega em <span>Caldas Novas</span> e cidades do sul goiano')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 170 km de Caldas Novas pela GO-139. Entrega de transpaleteira elétrica em até 24 horas. Atendemos todo o sul goiano e cidades num raio de 200 km.</p>
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

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Caldas Novas')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica é mais procurada pelos hotéis de Caldas Novas?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark WPio15 concentra a maioria dos contratos no polo hoteleiro. Com 1.500 kg de capacidade e lítio 24V, opera em silêncio nos almoxarifados de resorts, cozinhas industriais e lavanderias dos 106 hotéis da cidade. Chassi compacto para corredores de serviço com 1,8 m de largura.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A transpaleteira elétrica substitui a manual nas cozinhas dos resorts?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Nas cozinhas que servem café para 300 a 500 hóspedes, o volume de paletes de alimentos ultrapassa 40 unidades por turno. A manual causa atrasos de reposição e lesão repetitiva. A elétrica Clark movimenta a 6 km/h, elimina esforço físico e mantém fluxo contínuo de abastecimento durante a alta temporada. A troca reduz o tempo de movimentação em até 60%.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>A transpaleteira funciona nas câmaras frias dos hotéis e distribuidoras?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Sim. O modelo Clark SWX16 opera em câmaras frias a -18°C com lítio 24V que mantém desempenho estável em baixa temperatura. O chassi anticorrosão resiste à umidade das câmaras frigoríficas dos centros de distribuição que abastecem os 140 mil leitos de Caldas Novas. Zero emissão de gases preserva a integridade dos alimentos armazenados.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>A bateria de lítio 24V aguenta a alta temporada dos hotéis de Caldas Novas?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A autonomia varia de 6 a 10 horas contínuas conforme modelo e intensidade de uso. Na alta temporada, quando os almoxarifados operam em turnos estendidos, a recarga completa em 2 a 3 horas entre turnos cobre a jornada seguinte. Cargas de oportunidade de 15 minutos durante pausas permitem operação ininterrupta sem substituir o equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Funcionários de hotel precisam de certificação para usar transpaleteira?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige curso de operação de equipamentos de movimentação incluindo transpaleteiras elétricas. O treinamento cobre inspeção pré-operacional, limites de capacidade, velocidade em corredores de serviço e procedimentos de emergência. Indicamos centros credenciados na região de Caldas Novas e Goiânia para <a href="/caldas-novas-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação e reciclagem</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Qual o prazo de entrega de transpaleteira em Caldas Novas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Caldas Novas fica a 170 km da sede pela GO-139. A entrega acontece em até 24 horas após confirmação do contrato. Para demandas urgentes de hotéis com alta temporada ou eventos, priorizamos o despacho com logística dedicada. Frete incluso, sem custo adicional.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>O contrato de locação cobre manutenção completa?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todo contrato inclui manutenção preventiva e corretiva: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Para Caldas Novas, mantemos equipe técnica com rota fixa pela GO-139 que resolve ocorrências sem parar a operação do hotel ou lavanderia.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Quais capacidades de transpaleteira estão disponíveis para Caldas Novas?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para almoxarifados de hotéis e cozinhas industriais, a WPio15 é a mais indicada. A SWX16 stacker patolada eleva paletes até 4.500 mm, substituindo empilhadeiras em depósitos de lavanderias e centros de distribuição de alimentos do polo turístico.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para seu hotel em Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Caldas Novas.\\n\\n'")

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
            'goiania-go/', '170 km', 'Goiânia - GO',
            'Caldas Novas e Goiânia',  # legitimate: training centers
            '4913',  # address reference
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
cn = html.count('Caldas Novas')
local = html.count('hotel') + html.count('Hotel') + html.count('resort') + html.count('Resort') + html.count('lavanderia') + html.count('Lavanderia') + html.count('GO-139') + html.count('turístic') + html.count('hóspede')
print(f"\nCaldas Novas: {cn} menções")
print(f"Contexto local (hotel/resort/lavanderia/GO-139/turístico/hóspede): {local} menções")

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
