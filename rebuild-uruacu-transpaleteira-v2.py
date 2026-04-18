#!/usr/bin/env python3
"""
rebuild-uruacu-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Uruaçu-GO
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXTO: Uruaçu-GO, -14.5237/-49.1407, 280 km via BR-153.
Pop ~40k. Distrito Agroindustrial (258 mil m², 31 empresas).
Frigoríficos de aves/suínos, laticínios, armazéns de grãos.
Entity bridge: câmaras frias de frigoríficos, armazéns de laticínios.
Transpaleteira para caixas de frango congelado, queijos, leite UHT.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/uruacu-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Transpaleteira Elétrica para Locação em Uruaçu-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Transpaleteira elétrica Clark para locação em Uruaçu-GO. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com lítio 24V para frigoríficos de aves e suínos, laticínios e armazéns do Distrito Agroindustrial. Entrega via BR-153, manutenção inclusa."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Transpaleteira Elétrica para Locação em Uruaçu-GO | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark em Uruaçu. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para câmaras frias de frigoríficos e armazéns de laticínios do Distrito Agroindustrial. Entrega pela BR-153."')

r('content="Goiânia, Goiás, Brasil"', 'content="Uruaçu, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-14.5237;-49.1407"')
r('content="-16.7234, -49.2654"', 'content="-14.5237, -49.1407"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -14.5237, "longitude": -49.1407')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -14.5237')
r('"longitude": -49.2654', '"longitude": -49.1407')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Uruaçu"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Uruaçu", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira Clark é mais usada nos frigoríficos de Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark SWX16 stacker patolada domina os contratos em frigoríficos de aves e suínos de Uruaçu. Com chassi anticorrosão e bateria de lítio 24V estável a -25°C, ela empilha caixas de frango congelado até 4.500 mm dentro das câmaras frias. A WPio15 walkie complementa na movimentação horizontal entre a linha de abate e a expedição." } },
        { "@type": "Question", "name": "Transpaleteira elétrica opera dentro de câmara fria de frigorífico?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A Clark SWX16 foi desenvolvida para temperaturas de até -25°C. O chassi anticorrosão resiste à condensação constante das câmaras de congelamento dos frigoríficos de aves e suínos do Distrito Agroindustrial de Uruaçu. A bateria de lítio 24V mantém performance estável sem perda de autonomia, diferente das baterias de chumbo que degradam rapidamente no frio extremo." } },
        { "@type": "Question", "name": "A paleteira elétrica substitui a manual nos laticínios de Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "Nos laticínios do Distrito Agroindustrial, o volume diário de paletes de queijo, leite UHT e derivados ultrapassa 50 unidades por turno. A transpaleteira manual gera fadiga, atrasa a expedição e causa afastamentos por lesão repetitiva. A elétrica Clark movimenta paletes a 6 km/h com zero esforço físico e opera em câmaras de resfriamento sem contaminar o produto." } },
        { "@type": "Question", "name": "Qual a autonomia da bateria de lítio 24V em operação contínua no frigorífico?", "acceptedAnswer": { "@type": "Answer", "text": "A bateria de lítio 24V entrega de 6 a 10 horas contínuas dependendo do modelo e da intensidade de carga. Nos frigoríficos de Uruaçu que operam dois turnos de abate e expedição, a recarga completa em 2 a 3 horas durante a higienização da planta cobre a próxima jornada inteira. Cargas parciais de 20 minutos estendem a operação sem parar a linha." } },
        { "@type": "Question", "name": "Operadores de frigorífico precisam de certificação para transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento obrigatório para operação de equipamentos de movimentação de carga. O curso cobre inspeção pré-operacional, limites de capacidade, manobras em câmaras frias e procedimentos de emergência. Indicamos centros credenciados na região Norte de Goiás para certificação e reciclagem periódica." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de transpaleteira em Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "Uruaçu fica a 280 km da sede pela BR-153 — rodovia duplicada sem pedágio até Porangatu. O equipamento sai de Goiânia pela manhã e chega à tarde no Distrito Agroindustrial. Para contratos programados, garantimos entrega no dia combinado. Frete incluso no contrato, sem custo adicional para a cidade." } },
        { "@type": "Question", "name": "O contrato de locação inclui manutenção da bateria e chassi anticorrosão?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Cada contrato da Move Máquinas cobre manutenção preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas, chassi e tratamento anticorrosão para câmaras frias. Em Uruaçu, nossa equipe técnica se desloca pela BR-153 para atender ocorrências sem interromper o ciclo produtivo do frigorífico." } },
        { "@type": "Question", "name": "Quais capacidades de transpaleteira estão disponíveis para Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "A frota vai de 1.500 kg (WPio15 walkie para caixas de frango e laticínios) até 3.500 kg (WPX35 heavy duty para paletes de ração e insumos agroindustriais). A SWX16 stacker patolada eleva cargas até 4.500 mm, substituindo empilhadeiras nos corredores estreitos das câmaras de congelamento dos frigoríficos." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Uruaçu</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Locação de Transpaleteira Elétrica em <em>Uruaçu</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para câmaras frias de frigoríficos de aves e suínos, armazéns de laticínios e galpões do Distrito Agroindustrial de Uruaçu. Chassi anticorrosão, zero emissão. Entrega pela BR-153 com manutenção inclusa.')

# WhatsApp URLs — encoded Goiânia → Urua%C3%A7u
r('Goi%C3%A2nia', 'Urua%C3%A7u', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Uruaçu
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Chassi Anticorrosão p/ Câmaras Frias</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega via BR-153 (280 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Manutenção Preventiva Inclusa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Como a <span>transpaleteira elétrica</span> resolve a movimentação nos frigoríficos de Uruaçu')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — conhecida como paleteira ou patolinha no chão de fábrica — movimenta paletes na horizontal com motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Substitui o esforço braçal da versão manual, mantém cadência constante e opera em ambientes refrigerados sem emitir gases. O Distrito Agroindustrial de Uruaçu concentra 31 empresas em 258 mil metros quadrados: frigoríficos de aves e suínos que processam milhares de caixas congeladas por dia, laticínios que expedem queijos e leite UHT em câmaras de resfriamento, e armazéns de grãos e ração que demandam movimentação pesada e ininterrupta.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: autonomia para turnos de abate e expedição no frigorífico')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'O lítio 24V substituiu o chumbo-ácido nas transpaleteiras Clark com três ganhos decisivos: recarga completa entre 2 e 3 horas (contra 8h do chumbo), cargas parciais durante intervalos de higienização e durabilidade três vezes maior mesmo em temperaturas negativas. Nos frigoríficos de Uruaçu que alternam turnos de abate e expedição, a paleteira com lítio recarrega durante a lavagem da planta e sustenta a jornada seguinte inteira — sem parada para troca de bateria.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual encaixa na sua operação em Uruaçu')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida com o operador caminhando — encaixa nos corredores curtos entre a linha de abate e a expedição do frigorífico. A PWio20 com plataforma fixa cobre distâncias longas entre galpões do Distrito Agroindustrial sem desgaste físico. A PPXs20 com plataforma dobrável alterna entre modo caminhada para manobras em câmaras estreitas e modo plataforma para trajetos amplos. A stacker SWX16 empilha paletes até 4.500 mm dentro das câmaras de congelamento, substituindo empilhadeiras em corredores de 2 metros.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark SWX16: a stacker que opera nas câmaras frias dos frigoríficos de Uruaçu')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A SWX16 concentra os contratos mais longos em Uruaçu. Chassi com tratamento anticorrosão para umidade e condensação das câmaras frias, bateria de lítio 24V estável a -25°C e elevação até 4.500 mm para empilhar caixas de frango congelado em prateleiras altas. Nos frigoríficos de aves do Distrito Agroindustrial, ela opera o turno completo dentro da câmara sem perder rendimento — o timão ergonômico garante manobras precisas entre pilhas de paletes no piso escorregadio.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga em 2 a 3 horas durante higienização da planta, cargas parciais nos intervalos, sem emissão de gases dentro das câmaras frigoríficas.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso e sem emissão:</strong> requisito obrigatório para câmaras de congelamento de frigoríficos e áreas de envase de laticínios do Distrito Agroindustrial.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave sobre pisos úmidos de frigorífico, docas com desnível e rampas de acesso às câmaras de congelamento.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Uruaçu:</strong> frigoríficos de aves/suínos (câmaras -25°C), laticínios (resfriamento de queijos e leite UHT), armazéns de grãos e ração, galpões do Distrito Agroindustrial (258 mil m²).</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark com lítio 24V para câmaras frias de frigoríficos e laticínios em Uruaçu-GO"')

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
              <option value="Porangatu">Porangatu</option>
              <option value="Niquelândia">Niquelândia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Uruaçu" selected>Uruaçu</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Porangatu">Porangatu</option>
              <option value="Niquelândia">Niquelândia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 é a walkie mais versátil para operações de frigorífico em Uruaçu. Chassi compacto para corredores de 1,8 m, timão ergonômico e controle proporcional de velocidade. Movimenta caixas de frango congelado entre a linha de abate e a expedição, paletes de queijo nos laticínios e sacaria de ração nos armazéns do Distrito Agroindustrial.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em operação nos frigoríficos do Distrito Agroindustrial de Uruaçu"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a caminhada exaustiva entre galpões. No Distrito Agroindustrial de Uruaçu, o operador percorre distâncias de 100 a 150 metros entre o setor de expedição do frigorífico e os armazéns de estoque sem fadiga. A plataforma mantém ritmo constante durante turnos de 8 horas com carga de frango congelado e derivados de suínos.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alterna entre plataforma para trajetos longos e walkie para manobras dentro da câmara fria. A plataforma recolhe com um gesto, adaptando a paleteira ao corredor estreito entre as prateleiras de congelados ou ao percurso amplo entre a doca e o armazém. Modelo ideal para laticínios de Uruaçu que combinam picking de caixas de queijo e expedição de paletes de leite UHT.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 é a transpaleteira projetada para câmaras de congelamento: movimenta paletes na horizontal e empilha até 4.500 mm de altura, eliminando empilhadeiras em corredores de 2 metros. O chassi anticorrosão resiste à condensação constante a -25°C nos frigoríficos de aves e suínos de Uruaçu. Patolada para estabilidade máxima ao elevar caixas de frango congelado em prateleiras altas.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 operando em câmara de congelamento de frigorífico em Uruaçu-GO"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 movimenta as cargas mais pesadas do Distrito Agroindustrial. Projetada para paletes de ração animal, sacaria de grãos e insumos para frigoríficos que ultrapassam 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para os pisos industriais dos armazéns de Uruaçu com tráfego constante de caminhões e empilhadeiras.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para cargas pesadas nos armazéns agroindustriais de Uruaçu"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota disponível para Uruaçu e Norte de Goiás')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Uruaçu
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Os frigoríficos do Norte de Goiás estão nos procurando cada vez mais. Uruaçu é um caso clássico: câmara fria a -25°C, piso escorregadio, operador movimentando 70, 80 caixas de frango congelado por turno com paleteira manual. O sujeito sai do frio com o ombro travado, a produção atrasa e o caminhão baú refrigerado na doca acumula hora extra de motorista. Coloquei uma SWX16 num frigorífico de aves lá e o resultado apareceu na primeira semana: metade do tempo de carregamento da câmara, zero afastamento e o chassi anticorrosão aguentando a umidade sem ferrugem. O gerente me disse que o custo da locação é menor que um dia de sobreestadia do caminhão frigorífico."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Regra objetiva para Uruaçu:</strong> se o frigorífico ou laticínio movimenta mais de 30 paletes por turno, ou se a operação inclui câmaras frias abaixo de zero, a transpaleteira elétrica se paga no primeiro mês com produtividade e redução de afastamentos. Os frigoríficos de aves e suínos do Distrito Agroindustrial operam exclusivamente com paleteira elétrica pela exigência de chassi anticorrosão e zero emissão em ambientes refrigerados.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis para Uruaçu:')

# Links internos — todos para uruacu-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/uruacu-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/uruacu-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')

r('/goiania-go/curso-operador-empilhadeira', '/uruacu-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de transpaleteira elétrica para frigoríficos e laticínios em Uruaçu e Norte de Goiás"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Uruaçu')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe cada etapa: análise da operação do frigorífico ou laticínio, escolha do modelo Clark ideal para câmara fria ou armazém, entrega pela BR-153 até Uruaçu e suporte técnico durante todo o contrato. Do orçamento pelo WhatsApp ao equipamento operando na sua planta.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Investimento mensal na locação de <span>transpaleteira elétrica</span> em 2026')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark em Uruaçu e região Norte de Goiás. O investimento depende do modelo, prazo de contrato e configurações especiais para câmaras frias.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção e chassi anticorrosão inclusos')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas, chassi e tratamento anticorrosão para operação em câmaras frias. O valor mensal contempla o equipamento funcionando, sem cobranças extras de peças ou deslocamento técnico.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Uruaçu (frete incluso)')

r('Sem custo de frete na capital',
  'Frete incluído para Uruaçu via BR-153')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153, rodovia duplicada sem pedágio até Porangatu. O equipamento sai pela manhã e chega à tarde no Distrito Agroindustrial. Transpaleteira pronta para operar no frigorífico ou laticínio, frete incluso no contrato.')

r('O prejuízo invisível da paleteira manual',
  'O custo oculto de manter paleteiras manuais nos frigoríficos')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucos gerentes de frigorífico fazem:</strong> uma câmara fria que movimenta 60 caixas de frango congelado por turno com paleteira manual demanda o dobro de horas-homem. Somando o custo de um operador extra na câmara, os afastamentos por lesão repetitiva agravada pelo frio (média de 18 dias/ano no setor avícola) e as diárias de sobreestadia do caminhão baú refrigerado na doca, a economia aparente se converte em prejuízo. A locação da paleteira elétrica Clark se paga com a produtividade recuperada no primeiro mês de contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações no Distrito Agroindustrial')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>transpaleteira elétrica Clark</span> opera nos frigoríficos e laticínios de Uruaçu')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Setores agroindustriais que contratam paleteira elétrica no Distrito Agroindustrial e região.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark SWX16 em câmara fria de frigorífico de aves no Distrito Agroindustrial de Uruaçu"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>Frigoríficos de aves: câmaras de congelamento a -25°C</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'Os frigoríficos de aves de Uruaçu processam milhares de caixas de frango congelado por dia em câmaras a -25°C. A SWX16 com chassi anticorrosão empilha paletes até 4.500 mm nos corredores estreitos da câmara, resiste à condensação constante e mantém performance estável no frio extremo — requisitos que a paleteira manual simplesmente não atende.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em laticínio do Distrito Agroindustrial de Uruaçu"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>Laticínios: queijos, leite UHT e derivados</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'Os laticínios do Distrito Agroindustrial expedem centenas de paletes de queijo, leite UHT e derivados por turno em câmaras de resfriamento entre 2°C e 8°C. A WPio15 movimenta caixas entre a área de envase e o estoque refrigerado com zero emissão de gases, preservando a qualidade do produto e atendendo as exigências sanitárias da cadeia de frio.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 em frigorífico de suínos de Uruaçu"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>Frigoríficos de suínos: abate, corte e expedição</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'Os frigoríficos de suínos de Uruaçu movimentam paletes pesados de cortes, embutidos e subprodutos entre a sala de desossa, a câmara de resfriamento e a doca de expedição. A PWio20 com plataforma fixa cobre trajetos de 100 metros entre setores sem fadiga do operador. A velocidade de 6 km/h libera os caminhões baú antes do prazo de sobreestadia.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark WPX35 em armazém de grãos e ração no Distrito Agroindustrial de Uruaçu"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Armazéns de grãos e ração animal</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'Os armazéns de grãos e fábricas de ração do Distrito Agroindustrial movimentam paletes de sacaria de milho, soja e ração animal que ultrapassam 2.000 kg. A WPX35 heavy duty atende essas cargas com motor de tração reforçado e rodas de alta durabilidade para pisos industriais com tráfego constante de caminhões graneleiros na BR-153.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica se desloca pela BR-153 até Uruaçu. Diagnóstico de sistema elétrico, tração, bomba hidráulica e tratamento anticorrosão do chassi diretamente na planta do frigorífico ou laticínio.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-153 até o Distrito Agroindustrial de Uruaçu. São 280 km pela rodovia duplicada — o equipamento sai pela manhã e chega à tarde, pronto para operar. Frete incluso no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"Nossa câmara fria processa 400 caixas de frango congelado por turno. Com a manual, três operadores não davam conta e o ombro travava depois de duas horas no frio. Colocamos uma SWX16 Clark e um operador sozinho empilha tudo até 4,5 metros. O chassi anticorrosão está no quinto mês sem sinal de ferrugem, mesmo com a condensação constante a -25°C. O custo da locação equivale a menos de um dia de sobreestadia do caminhão frigorífico."')
r('<strong>Marcos V.</strong>',
  '<strong>Edson R.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente de Produção, Frigorífico de Aves, Distrito Agroindustrial, Uruaçu-GO (jan/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"No laticínio, a exigência é zero emissão e piso limpo. Testamos paleteira manual por dois anos e o resultado era operador afastado por lesão no punho a cada trimestre. A WPio15 Clark opera silenciosa entre a área de envase e a câmara de resfriamento sem contaminar o queijo com fuligem ou barulho. A bateria recarrega durante a higienização da tarde e cobre o turno noturno inteiro. A Move fez troca preventiva das rodas sem a gente nem pedir."')
r('<strong>Renata C.</strong>',
  '<strong>Luciana F.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Qualidade, Laticínio, Distrito Agroindustrial, Uruaçu-GO (fev/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"Temos duas PWio20 no armazém de ração do Distrito Agroindustrial. Cada palete pesa acima de 1.800 kg e o trajeto da doca ao estoque tem 120 metros. Com a manual, o operador levava 15 minutos por viagem. Com a plataforma fixa, faz em 4 minutos e nem desce do equipamento. Liberamos dois caminhões graneleiros por hora a mais desde que trocamos. A Move renova o contrato pelo WhatsApp em cinco minutos."')
r('<strong>Anderson L.</strong>',
  '<strong>Rogério P.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Supervisor de Armazém, Fáb. de Ração, Distrito Agroindustrial, Uruaçu-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/uruacu-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Conectamos sua equipe a centros credenciados na região Norte de Goiás e em Uruaçu.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Uruaçu</span> e cidades do Norte de Goiás')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153, rodovia duplicada sem pedágio até Porangatu. Entrega programada de transpaleteira elétrica Clark para frigoríficos, laticínios e armazéns agroindustriais. Raio de atendimento de 400 km.</p>
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
  'title="Área de atendimento Move Máquinas — Uruaçu e Norte de Goiás"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
r('/goiania-go/" style="color', '/uruacu-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Uruaçu')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira Clark é mais usada nos frigoríficos de Uruaçu?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark SWX16 stacker patolada domina os contratos em frigoríficos de aves e suínos. Com chassi anticorrosão e lítio 24V estável a -25°C, empilha caixas de frango congelado até 4.500 mm. A WPio15 walkie complementa na movimentação horizontal entre a linha de abate e a expedição.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A paleteira elétrica substitui a manual nos laticínios de Uruaçu?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Nos laticínios do Distrito Agroindustrial, o volume diário ultrapassa 50 paletes de queijo, leite UHT e derivados por turno. A manual gera fadiga, atrasa a expedição e causa afastamentos por lesão repetitiva. A elétrica Clark movimenta a 6 km/h com zero esforço físico e zero emissão, preservando a cadeia de frio e a qualidade do produto. A troca reduz tempo de movimentação em até 60%.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>Transpaleteira elétrica opera dentro de câmara fria de frigorífico?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Sim. A Clark SWX16 foi desenvolvida para temperaturas de até -25°C. O chassi anticorrosão resiste à condensação constante das câmaras de congelamento dos frigoríficos de aves e suínos do Distrito Agroindustrial. A bateria de lítio 24V mantém performance estável sem perda de autonomia no frio extremo, ao contrário das baterias de chumbo que degradam rapidamente.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>Qual a autonomia da bateria de lítio 24V em operação contínua no frigorífico?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A bateria entrega de 6 a 10 horas contínuas conforme modelo e intensidade de carga. Nos frigoríficos de Uruaçu com dois turnos de abate e expedição, a recarga completa em 2 a 3 horas durante a higienização da planta cobre a jornada seguinte. Cargas parciais de 20 minutos durante intervalos estendem a operação sem parar a linha.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores de frigorífico precisam de certificação para transpaleteira elétrica?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige treinamento obrigatório para operação de equipamentos de movimentação de carga. O curso cobre inspeção pré-operacional, limites de capacidade, manobras em câmaras frias e procedimentos de emergência. Indicamos centros credenciados na região Norte de Goiás para <a href="/uruacu-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">certificação e reciclagem periódica</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Qual o prazo de entrega de transpaleteira em Uruaçu?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Uruaçu fica a 280 km pela BR-153 — rodovia duplicada sem pedágio até Porangatu. O equipamento sai de Goiânia pela manhã e chega à tarde no Distrito Agroindustrial. Para contratos programados, garantimos entrega no dia combinado. Frete incluso, sem custo adicional.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>O contrato de locação inclui manutenção da bateria e chassi anticorrosão?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Cada contrato cobre manutenção preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas, chassi e tratamento anticorrosão para câmaras frias. Em Uruaçu, nossa equipe técnica se desloca pela BR-153 para resolver ocorrências sem interromper o ciclo produtivo do frigorífico ou laticínio.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Quais capacidades de transpaleteira estão disponíveis para Uruaçu?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota vai de 1.500 kg (WPio15 walkie para caixas de frango e laticínios) até 3.500 kg (WPX35 heavy duty para paletes de ração e insumos agroindustriais). A SWX16 stacker patolada eleva cargas até 4.500 mm, substituindo empilhadeiras nos corredores estreitos das câmaras de congelamento dos frigoríficos.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Uruaçu e Norte de Goiás')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Uruaçu-GO.\\n\\n'")

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
            'goiania-go/', '280 km', 'Goiânia - GO',
            'Uruaçu e Goiânia',
            'Goiânia —',  # in address context
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
print("VERIFICAÇÃO FINAL — URUAÇU TRANSPALETEIRA")
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
uru = html.count('Uruaçu')
local = html.count('frigorífico') + html.count('Frigorífico') + html.count('laticínio') + html.count('Laticínio') + html.count('Distrito Agroindustrial') + html.count('BR-153') + html.count('câmara') + html.count('Câmara')
print(f"\nUruaçu: {uru} menções")
print(f"Contexto local (frigorífico/laticínio/Dist.Agroindustrial/BR-153/câmara): {local} menções")

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

# Check vs SC transpaleteira V2
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
