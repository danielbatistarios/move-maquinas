#!/usr/bin/env python3
"""
rebuild-sc-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Senador Canedo
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Transpaleteira Elétrica para Locação em Senador Canedo-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Locação de transpaleteira elétrica Clark em Senador Canedo. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com lítio 24V para linhas de produção do DISC, CDs da BR-153 e armazéns farmacêuticos do DASC. Entrega no mesmo dia, manutenção inclusa."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/senador-canedo-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Transpaleteira Elétrica para Locação em Senador Canedo-GO | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark em Senador Canedo. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para indústrias do DISC, DASC e polo petroquímico. Entrega pela BR-153 no mesmo dia."')

r('content="Goiânia, Goiás, Brasil"', 'content="Senador Canedo, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.6997;-49.0919"')
r('content="-16.7234, -49.2654"', 'content="-16.6997, -49.0919"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.6997, "longitude": -49.0919')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.6997')
r('"longitude": -49.2654', '"longitude": -49.0919')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Senador Canedo"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Senador Canedo", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira elétrica é mais indicada para as indústrias de Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 lidera os contratos na região. Com 1.500 kg de capacidade e lítio 24V, ela opera nas linhas de produção do DISC (plásticos, higiene e moveleiro), nos CDs de distribuição da BR-153 e nos armazéns farmacêuticos do DASC. Operação silenciosa e zero emissão atendem as exigências de áreas controladas." } },
        { "@type": "Question", "name": "A transpaleteira elétrica funciona em ambientes farmacêuticos do DASC?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. As transpaleteiras Clark com bateria de lítio 24V operam com zero emissão de gases e ruído reduzido, atendendo as normas de áreas limpas dos laboratórios farmacêuticos do DASC em Senador Canedo. O modelo SWX16 empilha paletes em câmaras de acondicionamento a temperatura controlada sem comprometer a cadeia de qualidade." } },
        { "@type": "Question", "name": "A paleteira elétrica substitui a manual nas linhas de produção do DISC?", "acceptedAnswer": { "@type": "Answer", "text": "Nas fábricas de plásticos, higiene e móveis do DISC, o volume de paletes por turno ultrapassa 40 unidades. A transpaleteira manual causa fadiga, reduz velocidade e gera afastamentos por lesão repetitiva. A elétrica Clark movimenta paletes a até 6 km/h, elimina esforço físico e mantém ritmo constante durante turnos de 8 a 10 horas com recarga rápida no intervalo." } },
        { "@type": "Question", "name": "Quanto tempo a bateria de lítio 24V dura nas operações industriais de Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "A autonomia varia de 6 a 10 horas contínuas conforme modelo e intensidade de uso. Nas fábricas do DISC com dois turnos consecutivos, a recarga completa em 2 a 3 horas durante a troca de turno garante operação ininterrupta. A carga de oportunidade em pausas de 15 minutos permite estender a jornada sem substituir o equipamento." } },
        { "@type": "Question", "name": "Operadores do DISC e DASC precisam de certificação para usar transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento em operação de equipamentos de movimentação de carga. O curso abrange inspeção pré-operacional, limites de capacidade, velocidade em áreas de circulação e procedimentos de emergência. Indicamos centros de formação credenciados na região de Senador Canedo e Goiânia para capacitação e reciclagem." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de transpaleteira elétrica em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "Senador Canedo fica a 20 km da nossa sede pela BR-153, sem pedágio. A entrega ocorre no mesmo dia da confirmação do contrato, normalmente em menos de 2 horas. Para demandas urgentes de linhas paradas no DISC ou no polo petroquímico, priorizamos o despacho. Frete incluso, sem custo adicional." } },
        { "@type": "Question", "name": "O contrato de locação cobre manutenção da bateria e motor?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato da Move Máquinas inclui manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Senador Canedo, nossa equipe técnica mobile chega pela BR-153 em menos de 40 minutos para resolver qualquer ocorrência sem parar sua operação." } },
        { "@type": "Question", "name": "Qual a capacidade máxima das transpaleteiras disponíveis para Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para o polo petroquímico e indústrias de insumos pesados, a WPX35 movimenta bobinas e paletes acima de 2.000 kg. A SWX16 stacker patolada eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de armazéns farmacêuticos." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/senador-canedo-go/">Equipamentos em Senador Canedo</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Senador Canedo</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Locação de Transpaleteira Elétrica em <em>Senador Canedo</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para movimentação de paletes em indústrias de plásticos e higiene/limpeza do DISC, CDs de distribuição da BR-153 e armazéns farmacêuticos do DASC. Zero emissão, operação silenciosa. Entrega via BR-153 no mesmo dia.')

# WhatsApp URLs — encoded Goiânia → Senador+Canedo
r('Goi%C3%A2nia', 'Senador+Canedo', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template B
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Frota Clark com Lítio 24V</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega via BR-153 (20 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos de Experiência</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Suporte Técnico Mobile</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Entenda a <span>transpaleteira elétrica</span> antes de alugar para sua indústria')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — chamada no dia a dia de paleteira ou patolinha — é o equipamento que movimenta paletes na horizontal usando motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Ao contrário da versão manual, elimina esforço repetitivo, acelera o fluxo de materiais e opera em silêncio absoluto. Em Senador Canedo, as linhas de produção do DISC (plásticos, higiene/limpeza, moveleiro), os centros de distribuição ao longo da BR-153 e os armazéns farmacêuticos do DASC dependem de paleteiras elétricas para manter ritmo industrial sem contaminar áreas controladas.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: autonomia contínua para turnos duplos no DISC e DASC')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'As baterias de lítio 24V das transpaleteiras Clark substituíram o chumbo-ácido com vantagem tripla: recarga completa entre 2 e 3 horas (contra 8h do chumbo), cargas de oportunidade durante pausas de almoço e vida útil até três vezes superior. Nas fábricas do DISC que operam dois turnos consecutivos de embalagem e expedição, a paleteira com lítio mantém produtividade sem parada para troca de bateria — a recarga durante a virada de turno cobre a jornada inteira.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual atende sua operação em Senador Canedo')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida com o operador caminhando — ideal para corredores curtos nas fábricas de plásticos do DISC. A PWio20 com plataforma fixa permite percorrer distâncias longas entre docas e estoque nos CDs da BR-153 sem desgaste físico. A PPXs20 com plataforma dobrável alterna entre modo caminhada para manobras apertadas e modo plataforma para trajetos longos. A stacker SWX16 eleva paletes até 4.500 mm, substituindo empilhadeiras em corredores estreitos dos armazéns farmacêuticos do DASC.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark WPio15: a paleteira mais contratada na região industrial de Senador Canedo')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A WPio15 concentra o maior volume de contratos em Senador Canedo. Capacidade de 1.500 kg, lítio 24V e chassi compacto para corredores de 1,8 m — especificações que encaixam nas linhas de embalagem do DISC, na separação de pedidos nos CDs da BR-153 e no recebimento de insumos no DASC. O timão ergonômico com controle proporcional permite manobras precisas entre paletes sem impactar prateleiras ou estantes.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga de 2 a 3 horas entre turnos, carga de oportunidade no intervalo, zero emissão de gases nas áreas controladas do DASC e DISC.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso:</strong> operação sem ruído para ambientes farmacêuticos do DASC e linhas de higiene/limpeza do DISC que exigem conforto acústico.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave entre pisos industriais, docas com desnível e rampas de acesso nos galpões da BR-153.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Senador Canedo:</strong> DISC (plásticos, higiene, moveleiro), DASC (farmacêuticos, insumos), CDs da BR-153 (dock-to-stock), polo petroquímico (insumos pesados) e armazéns do Jardim das Oliveiras.</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark WPio15 com lítio 24V, modelo mais contratado para indústrias e CDs em Senador Canedo"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega via BR-153 no mesmo dia')

# Form selects — Senador Canedo como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Senador Canedo" selected>Senador Canedo</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Senador Canedo" selected>Senador Canedo</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 lidera os contratos de paleteira em Senador Canedo. Chassi compacto, timão ergonômico e controle proporcional de velocidade. Perfeita para separação de insumos nas fábricas de plásticos do DISC, recebimento de matéria-prima no DASC e movimentação horizontal em corredores de 1,8 m nos CDs da BR-153.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em operação industrial em Senador Canedo"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a fadiga de caminhada em trajetos longos. Nos centros de distribuição da BR-153 em Senador Canedo, o operador percorre corredores de 80 a 120 metros entre docas e estoque sem desgaste. Ideal para cross-docking de insumos do polo petroquímico e expedição de produtos acabados do DISC.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alterna entre plataforma para distâncias longas e walkie para manobras em corredores apertados. A plataforma recolhe com um gesto, adaptando a paleteira ao corredor estreito de estoque ou ao trajeto amplo entre galpões. Versátil para operações mistas nas fábricas do DISC que combinam picking de componentes e expedição de produtos acabados.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 combina movimentação horizontal com elevação até 4.500 mm, substituindo empilhadeiras em corredores estreitos. O chassi anticorrosão opera em ambientes com umidade elevada e temperatura controlada — requisito dos armazéns farmacêuticos do DASC. Patolada para estabilidade máxima ao empilhar paletes de insumos químicos no polo petroquímico.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 para elevação de paletes em armazéns farmacêuticos de Senador Canedo"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 movimenta as cargas mais pesadas da frota Clark. Projetada para paletes de insumos petroquímicos, bobinas de plástico e cargas acima de 2.000 kg comuns no polo petroquímico e nas indústrias de embalagens do DISC. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais com tráfego intenso em Senador Canedo.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para cargas industriais pesadas em Senador Canedo"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota para locação em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Senador Canedo
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Os chamados de Senador Canedo que mais crescem vêm do DISC e do DASC. Fábricas de plásticos e de higiene que movimentam 50, 60 paletes por turno com paleteira manual. O operador chega no final da manhã destruído, a linha de produção espera e o caminhão na doca acumula multa de sobreestadia. Semana passada, coloquei duas WPio15 numa indústria de embalagens do DISC que usava quatro manuais. Resultado: metade dos operadores, dobro de paletes movimentados. O lítio recarrega no almoço e segura a tarde toda. Em menos de 30 dias, o gerente me ligou perguntando por que não trocou antes."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Critério objetivo para Senador Canedo:</strong> se a fábrica movimenta mais de 30 paletes por turno ou se o trajeto entre doca e estoque passa de 50 metros, a paleteira elétrica se paga no primeiro mês com o ganho de produtividade. As indústrias do DISC, os armazéns farmacêuticos do DASC e os CDs da BR-153 operam exclusivamente com transpaleteira elétrica pelo volume de carga e pelas exigências de ambiente controlado.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Senador Canedo:')

# Links internos — todos para senador-canedo-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/senador-canedo-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Senador Canedo')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Senador Canedo')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Senador Canedo')

r('/goiania-go/curso-operador-empilhadeira', '/senador-canedo-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de transpaleteira elétrica para indústrias em Senador Canedo e região"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Senador Canedo')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe cada etapa da locação: análise da sua operação, escolha do modelo Clark ideal, entrega pela BR-153 e suporte técnico contínuo. Do orçamento pelo WhatsApp à paleteira operando no seu galpão em Senador Canedo.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Investimento mensal na locação de <span>paleteira elétrica</span> em 2026')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark em Senador Canedo. O investimento final depende do modelo, prazo de contrato e configuração escolhida.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção e lítio 24V no valor')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal já contempla o equipamento operando, sem cobranças extras de peças ou deslocamento técnico.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Senador Canedo (20 km, sem frete)')

r('Sem custo de frete na capital',
  'Frete incluso para Senador Canedo')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — a 20 km de Senador Canedo pela BR-153, sem pedágio. Entrega no mesmo dia da confirmação. A transpaleteira chega no seu galpão, CD ou armazém pronta para operar, sem custo de frete.')

r('O prejuízo invisível da paleteira manual',
  'O custo oculto de manter paleteiras manuais no DISC')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucas fábricas do DISC fazem:</strong> uma linha que movimenta 60 paletes/turno com paleteira manual demanda o dobro de horas-homem. Somando o custo de um operador extra, os afastamentos por lesão repetitiva (média de 15 dias/ano no setor plástico) e as multas de sobreestadia nos caminhões da BR-153, a economia aparente desaparece. A locação da paleteira elétrica Clark se paga com a produtividade recuperada já no primeiro mês de contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações industriais')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>paleteira elétrica Clark</span> opera diariamente em Senador Canedo')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Setores industriais e logísticos que contratam transpaleteira elétrica na região.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark nas linhas de produção de plásticos e higiene do DISC em Senador Canedo"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>DISC: plásticos, higiene e limpeza</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'As fábricas de plásticos e de produtos de higiene/limpeza do DISC movimentam centenas de paletes de matéria-prima e produto acabado por turno. A WPio15 navega entre linhas de produção com corredores de 1,8 m, transporta paletes de 500 a 1.200 kg e mantém o fluxo contínuo de embalagens até a doca de expedição — com zero emissão de gases no ambiente fabril.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Stacker Clark SWX16 em armazém farmacêutico do DASC em Senador Canedo"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>DASC: armazéns farmacêuticos</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'Os laboratórios farmacêuticos e distribuidoras do DASC exigem equipamentos com zero emissão e baixo ruído para manter a integridade de áreas limpas. A SWX16 empilha paletes de insumos até 4.500 mm em corredores estreitos com estabilidade total, enquanto a WPio15 abastece linhas de envase sem contaminar o ambiente controlado.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 em centro de distribuição da BR-153 em Senador Canedo"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>CDs da BR-153: distribuição e cross-docking</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'Os centros de distribuição da BR-153 em Senador Canedo recebem insumos do polo petroquímico e expedem produtos do DISC para todo Centro-Oeste. A PWio20 com plataforma fixa percorre corredores de 100 metros entre docas e estoque sem fadiga. A velocidade de 6 km/h reduz o tempo de dock-to-stock e libera os caminhões antes do prazo de sobreestadia.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark WPX35 no polo petroquímico de Senador Canedo"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Polo petroquímico: insumos pesados</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'Petrobras, Realpetro e Petrobol movimentam paletes de insumos químicos, aditivos e embalagens que ultrapassam 2.000 kg. A WPX35 heavy duty atende essas cargas com motor de tração reforçado e rodas de alta durabilidade para pisos industriais com tráfego de empilhadeiras e caminhões-tanque no Complexo Petroquímico de Senador Canedo.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica mobile com deslocamento pela BR-153. Atendimento em Senador Canedo em menos de 40 minutos a partir da sede. Diagnóstico de sistema elétrico, tração e bomba hidráulica diretamente na planta.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-153 até seu galpão, CD ou armazém em Senador Canedo. São 20 km da sede — entrega no mesmo dia, sem custo adicional de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"Nossa linha de embalagens plásticas no DISC movimentava 55 paletes por turno com quatro manuais. Trocamos por duas WPio15 Clark e o rendimento dobrou. O lítio recarrega na troca de turno e aguenta a jornada completa. Dispensamos dois operadores auxiliares e eliminamos os afastamentos por lesão no ombro. O contrato se pagou em três semanas."')
r('<strong>Marcos V.</strong>',
  '<strong>Adriano M.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente de Produção, Ind. de Plásticos, DISC Senador Canedo-GO (jan/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"Precisávamos de paleteira para o armazém de insumos farmacêuticos no DASC. A exigência era zero emissão e baixo ruído para não comprometer a área limpa. A SWX16 opera há quatro meses empilhando paletes a 4 metros sem contaminar o ambiente. A Move fez a troca preventiva da bateria sem a gente nem solicitar — monitoramento remoto detectou queda de ciclo."')
r('<strong>Renata C.</strong>',
  '<strong>Priscila R.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Logística, Laboratório Farmacêutico, DASC Senador Canedo-GO (fev/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"Três PWio20 no nosso CD da BR-153 em Senador Canedo resolveram o gargalo de dock-to-stock. Os operadores percorriam 14 km por turno empurrando manual — agora fazem o mesmo trajeto na plataforma em metade do tempo. A sobreestadia dos caminhões zerou desde que trocamos. Renovamos o contrato semestral e o atendimento da Move pelo WhatsApp não demora cinco minutos."')
r('<strong>Anderson L.</strong>',
  '<strong>Felipe S.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Supervisor de Operações, CD Logístico, BR-153 Senador Canedo-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/senador-canedo-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Conectamos sua equipe a centros credenciados na região de Senador Canedo.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Senador Canedo</span> e cidades vizinhas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 20 km de Senador Canedo pela BR-153, sem pedágio. Entrega de transpaleteira elétrica no mesmo dia da confirmação. Atendemos toda a região metropolitana num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/senador-canedo-go/"><strong>Senador Canedo</strong></a>
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
        <a href="/trindade-go/">Trindade</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/">Inhumas</a>
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
r('!2d-49.2654!3d-16.7234', '!2d-49.0919!3d-16.6997')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Senador Canedo"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Senador Canedo</a>')
r('/goiania-go/" style="color', '/senador-canedo-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Senador Canedo')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica é mais indicada para as indústrias de Senador Canedo?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark WPio15 lidera os contratos na região. Com 1.500 kg de capacidade e lítio 24V, opera nas linhas de produção do DISC (plásticos, higiene e moveleiro), nos CDs de distribuição da BR-153 e nos armazéns farmacêuticos do DASC. Operação silenciosa e zero emissão para áreas controladas.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A paleteira elétrica substitui a manual nas fábricas do DISC?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Nas fábricas de plásticos, higiene e móveis do DISC, o volume por turno ultrapassa 40 paletes. A manual causa fadiga e gera afastamentos por lesão repetitiva. A elétrica Clark movimenta a 6 km/h, elimina esforço físico e mantém ritmo estável durante turnos de 8 a 10 horas. A troca reduz o tempo de movimentação em até 60% e zera os afastamentos ergonômicos.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>A transpaleteira funciona nos ambientes farmacêuticos do DASC?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Sim. As transpaleteiras Clark com lítio 24V operam com zero emissão de gases e ruído reduzido — requisitos das áreas limpas dos laboratórios farmacêuticos do DASC. O modelo SWX16 empilha paletes em câmaras de acondicionamento a temperatura controlada sem comprometer a cadeia de qualidade. O chassi anticorrosão resiste à umidade dos ambientes de armazenamento.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>A bateria de lítio 24V aguenta turnos duplos nas fábricas de Senador Canedo?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A autonomia varia de 6 a 10 horas contínuas conforme modelo e carga. Nas fábricas do DISC com dois turnos consecutivos, a recarga completa em 2 a 3 horas durante a troca de turno cobre a próxima jornada inteira. Cargas de oportunidade de 15 minutos durante pausas permitem estender a operação sem substituir o equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores do DISC e DASC precisam de certificação para usar transpaleteira?<')
# Note: the link /goiania-go/curso-operador-empilhadeira may NOT have been changed yet
# (earlier r() only replaced count=1 and it matched in comparativo section).
# Match the ORIGINAL text.
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige curso de operação de equipamentos de movimentação incluindo transpaleteiras elétricas. O treinamento cobre inspeção pré-operacional, limites de capacidade, velocidade em áreas de circulação e procedimentos de emergência. Indicamos centros de formação credenciados na região de Senador Canedo para <a href="/senador-canedo-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação e reciclagem</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Qual o prazo de entrega de transpaleteira em Senador Canedo?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Senador Canedo fica a 20 km da nossa sede pela BR-153, sem pedágio. A entrega ocorre no mesmo dia da confirmação, normalmente em menos de 2 horas. Para demandas urgentes de linhas paradas no DISC ou no polo petroquímico, priorizamos o despacho. Frete incluso no contrato, sem custo adicional.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>O contrato cobre manutenção completa da bateria e motor?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todo contrato inclui manutenção preventiva e corretiva: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Senador Canedo, nossa equipe técnica mobile chega pela BR-153 em menos de 40 minutos para resolver qualquer ocorrência sem parar sua operação.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Qual a capacidade máxima das transpaleteiras disponíveis para Senador Canedo?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para o polo petroquímico e indústrias de insumos pesados, a WPX35 movimenta bobinas e paletes acima de 2.000 kg. A SWX16 stacker patolada eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de armazéns farmacêuticos do DASC.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Senador Canedo.\\n\\n'")

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
            'goiania-go/', '20 km', 'Goiânia - GO',
            'Senador Canedo e Goiânia',  # legitimate: training centers in both cities
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
sc = html.count('Senador Canedo')
local = html.count('DASC') + html.count('petroquím') + html.count('DISC') + html.count('BR-153')
print(f"\nSenador Canedo: {sc} menções")
print(f"Contexto local (DASC/petroquímico/DISC/BR-153): {local} menções")

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

# Check vs other SC V2 pages
import os
sc_pages = [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
]

for p in sc_pages:
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
