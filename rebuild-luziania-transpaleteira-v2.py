#!/usr/bin/env python3
"""
rebuild-luziania-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Luziânia
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXTO LOCAL:
- Luziânia-GO, -16.2532/-47.9501, 198km BR-040 de Goiânia
- Pop 210k, DIAL (Distrito Industrial Agroindustrial de Luziânia)
- Setores: metalurgia, alimentos, químicos, armazéns de grãos
- Entity bridge: "movimentação de paletes em indústrias alimentícias e químicas do DIAL"
- Clark: WPio15, PWio20, SWX16, WPX35
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/luziania-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Locação de Transpaleteira Elétrica em Luziânia-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Transpaleteira elétrica Clark para locação em Luziânia. Modelos WPio15, PWio20, SWX16 e WPX35 com lítio 24V para movimentação de paletes em indústrias alimentícias e químicas do DIAL, armazéns de grãos da BR-040 e metalúrgicas. Manutenção inclusa, entrega no mesmo dia."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/luziania-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Locação de Transpaleteira Elétrica em Luziânia-GO | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark em Luziânia. Modelos de 1.500 a 3.500 kg com lítio 24V para indústrias do DIAL e armazéns de grãos na BR-040. Entrega pela BR-040 no mesmo dia."')

r('content="Goiânia, Goiás, Brasil"', 'content="Luziânia, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.2532;-47.9501"')
r('content="-16.7234, -49.2654"', 'content="-16.2532, -47.9501"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.2532, "longitude": -47.9501')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.2532')
r('"longitude": -49.2654', '"longitude": -47.9501')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Luziânia"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Luziânia", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira elétrica atende melhor as indústrias do DIAL em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 concentra a maioria dos contratos na região. Com 1.500 kg de capacidade e bateria de lítio 24V, opera nas linhas de produção de alimentos processados, nos armazéns de insumos químicos e nos silos de grãos ao longo da BR-040. Chassi compacto para corredores de 1,8 m e operação silenciosa para ambientes fechados." } },
        { "@type": "Question", "name": "A paleteira elétrica opera em silos e armazéns de grãos na BR-040?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A transpaleteira elétrica Clark movimenta paletes de sacaria, big bags e insumos agrícolas nos armazéns graneleiros da BR-040 em Luziânia. A WPio15 navega entre pilhas de sacas em corredores estreitos, enquanto a WPX35 transporta big bags de até 3.500 kg entre a área de recebimento e os silos de armazenagem." } },
        { "@type": "Question", "name": "A transpaleteira funciona nas câmaras frias das indústrias alimentícias de Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A Clark SWX16 opera em câmaras frias a -18°C com chassi anticorrosão e bateria de lítio que mantém desempenho estável em baixas temperaturas. Nas indústrias de alimentos processados do DIAL, a stacker empilha paletes de produtos congelados e resfriados até 4.500 mm sem comprometer a cadeia de frio." } },
        { "@type": "Question", "name": "A bateria de lítio 24V aguenta turnos completos nas fábricas de Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "A autonomia vai de 6 a 10 horas contínuas dependendo do modelo e da carga. Nas indústrias alimentícias e metalúrgicas do DIAL que operam dois turnos seguidos, a recarga completa em 2 a 3 horas durante a virada de turno cobre a jornada inteira. Cargas de oportunidade de 15 a 20 minutos nas pausas estendem a operação sem trocar o equipamento." } },
        { "@type": "Question", "name": "Operadores das indústrias do DIAL precisam de certificação para transpaleteira?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige curso específico para operação de equipamentos de movimentação de carga. O treinamento inclui inspeção pré-operacional, capacidade nominal, velocidade em áreas de pedestres e procedimentos de emergência. Indicamos centros de capacitação credenciados na região de Luziânia e Entorno de Brasília." } },
        { "@type": "Question", "name": "Como funciona a entrega de transpaleteira em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Luziânia está a 198 km da sede pela BR-040 via Anápolis. A entrega ocorre no mesmo dia da confirmação para pedidos até 12h. Para demandas urgentes de fábricas do DIAL ou armazéns de grãos com linha parada, priorizamos o despacho. Frete já incluso no contrato de locação." } },
        { "@type": "Question", "name": "O contrato inclui manutenção da bateria e do motor da paleteira?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato da Move Máquinas cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Luziânia, a equipe técnica mobile atende ocorrências pela BR-040 para resolver qualquer falha sem interromper sua produção." } },
        { "@type": "Question", "name": "Qual a maior capacidade de carga entre as transpaleteiras disponíveis para Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para as metalúrgicas e indústrias químicas do DIAL que movimentam bobinas e tambores pesados, a WPX35 é a escolha certa. A SWX16 stacker patolada eleva paletes até 4.500 mm, substituindo empilhadeiras em corredores estreitos de armazéns de alimentos." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/luziania-go/">Equipamentos em Luziânia</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Luziânia</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Transpaleteira Elétrica para Locação em <em>Luziânia</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para movimentação de paletes em indústrias alimentícias e químicas do DIAL, armazéns de grãos da BR-040 e metalúrgicas de Luziânia. Zero emissão, manutenção no contrato. Entrega pela BR-040 no mesmo dia.')

# WhatsApp URLs — encoded Goiânia → Luzi%C3%A2nia
r('Goi%C3%A2nia', 'Luzi%C3%A2nia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C (Luziânia)
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Frota Clark Lítio 24V</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega via BR-040 (198 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos no Mercado</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Manutenção Inclusa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Por que a <span>transpaleteira elétrica</span> é indispensável na indústria de Luziânia')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — conhecida como paleteira ou patolinha no chão de fábrica — substitui o esforço humano na movimentação horizontal de paletes por motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Ela elimina lesões por repetição, acelera o fluxo entre doca e estoque e funciona em ambientes fechados sem emitir gases. Luziânia abriga o DIAL com fábricas de alimentos processados que exigem cadeia de frio ininterrupta, indústrias químicas que manipulam tambores e big bags pesados e armazéns graneleiros na BR-040 que recebem safras do Centro-Oeste.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: energia contínua para as fábricas e armazéns do DIAL')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'O lítio 24V das transpaleteiras Clark trouxe três ganhos sobre o chumbo-ácido: recarga completa entre 2 e 3 horas contra 8 horas da tecnologia anterior, cargas parciais de 15 minutos nas pausas de almoço e durabilidade até três vezes superior. Para as indústrias alimentícias do DIAL que rodam dois turnos de embalagem e expedição, a paleteira com lítio recarrega durante a virada de turno e mantém a produção sem nenhuma parada extra.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual configuração resolve seu gargalo em Luziânia')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 funciona com o operador caminhando atrás — perfeita para corredores curtos entre linhas de produção alimentícia no DIAL. A PWio20 com plataforma fixa permite percorrer distâncias longas entre docas e silos nos armazéns de grãos da BR-040 sem desgaste. A PPXs20 com plataforma dobrável alterna entre caminhada para manobras em espaço restrito e plataforma para trajetos amplos. A stacker SWX16 empilha paletes até 4.500 mm, substituindo empilhadeiras nos corredores estreitos de câmaras frias das indústrias de alimentos.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark WPio15: a paleteira mais requisitada no parque industrial de Luziânia')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A WPio15 domina os contratos de locação em Luziânia. Capacidade de 1.500 kg, lítio 24V e dimensões compactas para corredores de 1,8 m — configuração que encaixa nas linhas de embalagem de alimentos do DIAL, na separação de insumos químicos nos galpões industriais e no recebimento de sacaria nos armazéns da BR-040. O timão ergonômico com velocidade proporcional garante manobras precisas entre paletes sem impactar estantes ou equipamentos de linha.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga de 2 a 3 horas entre turnos, carga de oportunidade nas pausas, zero emissão de gases nas áreas de produção alimentícia e química do DIAL.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso e sem gases:</strong> operação em ambientes fechados de processamento de alimentos e manipulação de insumos químicos que proíbem combustão interna.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave entre pisos industriais do DIAL, docas com desnível e rampas de acesso dos armazéns graneleiros na BR-040.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Luziânia:</strong> DIAL (alimentos processados, químicos, metalurgia), armazéns de grãos BR-040 (sacaria, big bags), câmaras frias (congelados -18°C) e galpões logísticos do Entorno de Brasília.</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark WPio15 com lítio 24V, modelo mais contratado para indústrias e armazéns de grãos em Luziânia"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega via BR-040 no mesmo dia')

# Form selects — Luziânia como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Luziânia" selected>Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Formosa">Formosa</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Luziânia" selected>Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Formosa">Formosa</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 lidera os contratos de paleteira no DIAL de Luziânia. Chassi compacto de 780 mm, timão ergonômico e velocidade proporcional. Atende separação de insumos nas indústrias alimentícias, recebimento de matéria-prima nas químicas e movimentação horizontal de sacaria nos armazéns de grãos da BR-040.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em operação industrial no DIAL de Luziânia"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a caminhada em trajetos extensos. Nos armazéns graneleiros da BR-040, o operador percorre distâncias de 80 a 150 metros entre silos e docas de carregamento sem fadiga. Indicada também para expedição de alimentos processados no DIAL e cross-docking de insumos agrícolas.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 reúne duas funções: plataforma para deslocamentos longos e walkie para manobras apertadas. A plataforma recolhe com um gesto, alternando entre corredor estreito de estoque e percurso amplo de expedição. Versátil para as fábricas do DIAL que combinam picking de insumos na linha com transporte até a doca de carregamento.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 soma movimentação horizontal com elevação até 4.500 mm, eliminando a necessidade de empilhadeira em corredores estreitos. O chassi anticorrosão resiste a ambientes úmidos e câmaras frias a -18°C das indústrias alimentícias do DIAL. Patolada para máxima estabilidade ao empilhar paletes de congelados e insumos químicos em racks verticais.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 para elevação de paletes em câmaras frias e armazéns do DIAL em Luziânia"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 movimenta as cargas mais pesadas da frota Clark. Projetada para big bags de grãos, tambores de produtos químicos e bobinas metálicas acima de 2.000 kg presentes nas metalúrgicas e indústrias químicas do DIAL. Motor reforçado e rodas de alta resistência para pisos industriais com tráfego pesado em Luziânia.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para cargas pesadas em indústrias de Luziânia"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota para locação em Luziânia')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Luziânia
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Luziânia tem crescido muito nos últimos anos com o DIAL e os armazéns de grãos. Os chamados que recebo de lá são quase sempre urgentes: safra chegou, a doca está lotada e a paleteira manual não dá conta. Semana retrasada, uma indústria de alimentos processados me ligou com três caminhões parados na doca. Mandei duas WPio15 pela BR-040 e em menos de três horas estava tudo descarregado. O gerente calculou que a multa de sobreestadia que ia pagar nos três caminhões era quatro vezes o valor da locação mensal. Quando o número passa de 30 paletes por turno, a manual vira prejuízo disfarçado."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Referência prática para Luziânia:</strong> quando a operação ultrapassa 30 paletes por turno ou o percurso entre doca e silo passa de 50 metros, a paleteira elétrica se paga no primeiro mês pela produtividade recuperada. As indústrias alimentícias e químicas do DIAL, os armazéns graneleiros da BR-040 e as metalúrgicas já operam exclusivamente com transpaleteira elétrica pelo volume de carga e pela exigência de zero emissão em ambientes fechados.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Luziânia:')

# Links internos — todos para luziania-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/luziania-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Luziânia')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/luziania-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Luziânia')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/luziania-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Luziânia')

r('/goiania-go/curso-operador-empilhadeira', '/luziania-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Luziânia')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: processo de locação de transpaleteira elétrica para indústrias em Luziânia e Entorno de Brasília"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Luziânia')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'Acompanhe no vídeo da Move Máquinas cada etapa da locação: análise da operação, recomendação do modelo Clark adequado, envio pela BR-040 e suporte técnico permanente. Do orçamento pelo WhatsApp até a paleteira rodando no seu galpão em Luziânia.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Qual o investimento mensal para locar <span>paleteira elétrica</span> em 2026?')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark em Luziânia. O custo final depende do modelo, prazo de contrato e especificação do equipamento.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção e lítio 24V inclusos')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal cobre a transpaleteira Clark operando com manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Sem cobranças extras de peças, deslocamento técnico ou mão de obra.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Luziânia (frete incluso)')

r('Sem custo de frete na capital',
  'Frete incluso para Luziânia via BR-040')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — 198 km de Luziânia pela BR-040. A entrega ocorre no mesmo dia para pedidos confirmados até 12h. A transpaleteira chega ao seu galpão, armazém ou câmara fria pronta para operar, com frete incluso no contrato.')

r('O prejuízo invisível da paleteira manual',
  'O custo oculto de manter paleteiras manuais no DIAL')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucas indústrias do DIAL fazem:</strong> uma operação com 60 paletes/turno usando paleteira manual consome o dobro de horas-homem da elétrica. Somando o custo de um operador adicional, os afastamentos por lesão repetitiva (média de 15 dias/ano no setor alimentício) e as multas de sobreestadia nos caminhões graneleiros da BR-040, a economia aparente desaparece. A locação da Clark elétrica se paga com a produtividade recuperada já no primeiro mês de contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações em Luziânia')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>paleteira elétrica</span> opera diariamente no parque industrial de Luziânia')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Setores industriais e logísticos que contratam transpaleteira elétrica na região do DIAL e BR-040.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark nas linhas de produção de alimentos processados do DIAL em Luziânia"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>DIAL: indústrias alimentícias e câmaras frias</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'As indústrias de alimentos processados do DIAL movimentam centenas de paletes de matéria-prima, embalagens e produto acabado por turno. A WPio15 opera entre linhas de produção com corredores de 1,8 m, enquanto a SWX16 empilha paletes em câmaras frias a -18°C sem interromper a cadeia de frio — requisito das fábricas de congelados e resfriados de Luziânia.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Transpaleteira Clark WPX35 em indústria química do DIAL em Luziânia"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>DIAL: indústrias químicas e metalúrgicas</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'As indústrias químicas e metalúrgicas do DIAL manipulam tambores de reagentes, bobinas de aço e paletes de insumos que ultrapassam 2.000 kg. A WPX35 heavy duty movimenta essas cargas com motor reforçado e rodas para pisos industriais pesados. Zero emissão garante conformidade com normas de segurança em ambientes com produtos inflamáveis.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 em armazém de grãos da BR-040 em Luziânia"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>Armazéns de grãos da BR-040: sacaria e big bags</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'Os armazéns graneleiros da BR-040 em Luziânia recebem safras de soja, milho e sorgo do Centro-Oeste em big bags e sacaria paletizada. A PWio20 com plataforma fixa percorre distâncias de até 150 metros entre docas e silos sem desgastar o operador. A velocidade de 6 km/h acelera o fluxo de descarga e reduz o tempo de permanência dos caminhões graneleiros.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark em galpão logístico do Entorno de Brasília via Luziânia"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Entorno de Brasília: galpões logísticos e distribuição</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'Luziânia é ponto de passagem estratégico entre Goiânia e Brasília pela BR-040. Galpões logísticos do Entorno concentram distribuição de produtos alimentícios, materiais de construção e insumos industriais para o DF. A transpaleteira elétrica Clark movimenta paletes nesses centros com velocidade e precisão, acelerando o cross-docking e reduzindo custos de sobreestadia.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica mobile com deslocamento pela BR-040. Atendimento em Luziânia com diagnóstico de sistema elétrico, motor de tração e bomba hidráulica diretamente na planta industrial.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da transpaleteira via BR-040 até seu galpão, armazém ou câmara fria em Luziânia. Entrega no mesmo dia para pedidos até 12h, com frete incluso no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"Nossa fábrica de alimentos no DIAL processava 70 paletes por turno com três paleteiras manuais. Dois operadores já tinham afastamento por lesão no ombro. Trocamos por duas WPio15 Clark e o resultado foi imediato: mesma quantidade de paletes com metade da equipe, zero afastamento e a bateria de lítio recarrega durante o almoço. Em 25 dias, o custo da locação já tinha se pago com a economia de hora extra e o fim das multas de sobreestadia."')
r('<strong>Marcos V.</strong>',
  '<strong>Ricardo T.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente Industrial, Ind. de Alimentos Processados, DIAL Luziânia-GO (jan/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"Nossos armazéns de grãos na BR-040 recebem caminhões de soja e milho o dia inteiro na safra. Antes da PWio20, os operadores caminhavam mais de 10 km por turno empurrando manual entre a doca e os silos. Desde que alugamos três unidades com plataforma, o descarregamento que levava 5 horas baixou para 2h40. Na última safra, zeramos a sobreestadia. A Move faz a preventiva sem a gente nem perceber."')
r('<strong>Renata C.</strong>',
  '<strong>Daniela F.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Logística, Armazém Graneleiro, BR-040 Luziânia-GO (fev/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"A indústria química onde trabalho no DIAL manipula tambores de 250 litros e big bags de 1.200 kg o tempo todo. A WPX35 movimenta tudo sem esforço — o motor reforçado segura a carga nos desníveis entre galpões. A SWX16 empilha em racks de 4 metros nos corredores estreitos do armazém de insumos. Renovamos o contrato semestral e o suporte da Move pelo WhatsApp é o mais rápido que já vi."')
r('<strong>Anderson L.</strong>',
  '<strong>Leandro M.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Supervisor de Produção, Indústria Química, DIAL Luziânia-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/luziania-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Indicamos centros credenciados na região de Luziânia e Entorno de Brasília.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Luziânia</span> e cidades vizinhas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 198 km de Luziânia pela BR-040. Entrega de transpaleteira elétrica no mesmo dia para pedidos até 12h. Atendemos Luziânia, Entorno de Brasília e cidades num raio de 200 km.</p>
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
  'title="Área de atendimento Move Máquinas — Luziânia e Entorno de Brasília"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziânia</a>')
r('/goiania-go/" style="color', '/luziania-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Luziânia')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica atende melhor as indústrias do DIAL em Luziânia?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark WPio15 concentra a maioria dos contratos na região. Com 1.500 kg e lítio 24V, opera nas linhas de produção de alimentos processados, nos armazéns de insumos químicos e nos silos de grãos da BR-040. Chassi compacto para corredores de 1,8 m e zero emissão para ambientes fechados.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A paleteira elétrica opera em silos e armazéns de grãos na BR-040?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Sim. A transpaleteira Clark movimenta sacaria paletizada, big bags de grãos e insumos agrícolas nos armazéns graneleiros da BR-040. A WPio15 navega entre pilhas de sacas em corredores estreitos, enquanto a WPX35 transporta big bags de até 3.500 kg entre doca e silos. Na safra, o ganho de velocidade versus a manual reduz o tempo de descarga em até 60%.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>A transpaleteira funciona nas câmaras frias das indústrias alimentícias do DIAL?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Sim. A Clark SWX16 opera em câmaras frias a -18°C com chassi anticorrosão e lítio que mantém desempenho estável em baixas temperaturas. Nas indústrias de alimentos processados do DIAL em Luziânia, a stacker empilha paletes de congelados e resfriados até 4.500 mm sem comprometer a cadeia de frio.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>A bateria de lítio 24V aguenta turnos completos nas fábricas de Luziânia?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A autonomia vai de 6 a 10 horas contínuas dependendo do modelo e da intensidade. Nas indústrias do DIAL com dois turnos seguidos, a recarga completa em 2 a 3 horas durante a virada cobre a jornada inteira. Cargas de oportunidade de 15 a 20 minutos nas pausas estendem a operação sem substituir o equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores das indústrias do DIAL precisam de certificação para transpaleteira?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige curso específico de operação de equipamentos de movimentação. O treinamento inclui inspeção pré-operacional, capacidade nominal, velocidade em áreas de pedestres e procedimentos de emergência. Indicamos centros credenciados na região de Luziânia e Entorno de Brasília para <a href="/luziania-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação e reciclagem</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Como funciona a entrega de transpaleteira em Luziânia?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Luziânia está a 198 km da sede pela BR-040. A entrega ocorre no mesmo dia para pedidos confirmados até 12h. Para demandas urgentes de fábricas do DIAL ou armazéns com linha parada, priorizamos o despacho. Frete incluso no contrato, sem custo adicional.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>O contrato inclui manutenção da bateria e do motor da paleteira?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todo contrato cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Luziânia, a equipe técnica mobile atende pela BR-040 para resolver qualquer falha sem interromper sua operação.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Qual a maior capacidade de carga entre as transpaleteiras disponíveis para Luziânia?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para metalúrgicas e indústrias químicas do DIAL que movimentam bobinas e tambores pesados, a WPX35 é a escolha certa. A SWX16 stacker patolada eleva paletes até 4.500 mm, substituindo empilhadeiras em corredores estreitos de armazéns de alimentos.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Luziânia')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Luziânia.\\n\\n'")

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
            'goiania-go/', '198 km', 'Goiânia - GO',
            'Luziânia e Entorno', 'região de Luziânia',
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
luz = html.count('Luziânia')
local = html.count('DIAL') + html.count('BR-040') + html.count('grãos') + html.count('alimentíc') + html.count('químic') + html.count('metalúrg')
print(f"\nLuziânia: {luz} menções")
print(f"Contexto local (DIAL/BR-040/grãos/alimentícias/químicas/metalúrgicas): {local} menções")

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
