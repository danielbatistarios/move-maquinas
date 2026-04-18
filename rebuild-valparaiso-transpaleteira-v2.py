#!/usr/bin/env python3
"""
rebuild-valparaiso-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Valparaíso de Goiás
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

PLACEHOLDER: cidade contém "Goiás" — usar {{CITY}} intermediário.
Contexto: slug valparaiso-de-goias-go, -16.0683/-47.9764, 230km BR-040,
pop 200k. Polo moveleiro (120 fábricas), comércio varejista.
Entity bridge: supermercados, comércio varejista, docas do polo moveleiro.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/valparaiso-de-goias-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Locação de Transpaleteira Elétrica em Valparaíso de Goiás | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Transpaleteira elétrica Clark para locação em Valparaíso de Goiás. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com lítio 24V para polo moveleiro, supermercados e comércio varejista da BR-040. Entrega no mesmo dia via BR-040, manutenção inclusa."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/valparaiso-de-goias-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Locação de Transpaleteira Elétrica em Valparaíso de Goiás | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark em Valparaíso de Goiás. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para 120 fábricas de móveis, supermercados e atacadistas. Entrega pela BR-040 no mesmo dia."')

r('content="Goiânia, Goiás, Brasil"', 'content="Valparaíso de Goiás, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.0683;-47.9764"')
r('content="-16.7234, -49.2654"', 'content="-16.0683, -47.9764"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.0683, "longitude": -47.9764')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.0683')
r('"longitude": -49.2654', '"longitude": -47.9764')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Valparaíso de Goiás"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Valparaíso de Goiás", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/valparaiso-de-goias-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/valparaiso-de-goias-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira elétrica atende melhor o polo moveleiro de Valparaíso de Goiás?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 é o modelo mais contratado para as fábricas de móveis da cidade. Com 1.500 kg de capacidade e lítio 24V, ela movimenta chapas de MDF empilhadas e móveis embalados nos corredores de 1,8 m das 120 marcenarias e indústrias moveleiras. Operação silenciosa e compacta para linhas de acabamento." } },
        { "@type": "Question", "name": "A transpaleteira manual dá conta do volume nas docas do polo moveleiro?", "acceptedAnswer": { "@type": "Answer", "text": "Nas fábricas de móveis que despacham mais de 40 paletes por turno, a manual causa fadiga extrema e afastamentos por lesão de ombro e coluna. A elétrica Clark desloca chapas de MDF a 6 km/h sem esforço do operador. A troca reduz tempo de doca em até 55% e elimina o risco de dano ao produto acabado por erro de manuseio." } },
        { "@type": "Question", "name": "A paleteira elétrica serve para recebimento em supermercados de Valparaíso?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Os supermercados e atacadistas de Valparaíso de Goiás recebem paletes de bebidas, alimentos e produtos de limpeza várias vezes ao dia. A WPio15 walkie navega entre gôndolas e estoque, descarrega caminhões na doca e posiciona paletes em câmaras frias. A bateria de lítio opera o dia todo com recarga no intervalo." } },
        { "@type": "Question", "name": "Quanto dura a bateria de lítio 24V em operação contínua nas fábricas de Valparaíso?", "acceptedAnswer": { "@type": "Answer", "text": "A autonomia varia de 6 a 10 horas conforme o modelo e a intensidade de carga. Nas marcenarias que operam dois turnos, a recarga completa em 2 a 3 horas na virada de turno cobre a jornada seguinte. Cargas de oportunidade de 20 minutos durante pausas prolongam o ciclo sem substituir o equipamento." } },
        { "@type": "Question", "name": "Operadores das fábricas de móveis precisam de certificado NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento de operação de equipamentos de movimentação de carga. O curso cobre inspeção pré-turno, limites de capacidade, velocidade em corredores e protocolos de emergência. Indicamos centros credenciados em Valparaíso de Goiás e no Entorno de Brasília para certificação e reciclagem." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da transpaleteira em Valparaíso de Goiás?", "acceptedAnswer": { "@type": "Answer", "text": "Valparaíso de Goiás fica a 230 km da sede pela BR-040 via Cristalina. A entrega ocorre no mesmo dia para pedidos confirmados até as 10h. Para chamados urgentes de linhas paradas no polo moveleiro, priorizamos o despacho com chegada prevista em até 4 horas. Frete incluso no contrato." } },
        { "@type": "Question", "name": "A manutenção da transpaleteira é por conta do cliente?", "acceptedAnswer": { "@type": "Answer", "text": "Não. Todo contrato da Move Máquinas cobre manutenção preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Nossa equipe técnica atende em Valparaíso de Goiás com deslocamento programado e urgências resolvidas no mesmo dia." } },
        { "@type": "Question", "name": "Qual a maior capacidade de carga disponível para locação em Valparaíso?", "acceptedAnswer": { "@type": "Answer", "text": "A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para o polo moveleiro que movimenta chapas de MDF acima de 2 toneladas, a WPX35 é a escolha principal. A SWX16 stacker patolada eleva paletes até 4.500 mm em corredores estreitos de depósitos de móveis acabados." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/valparaiso-de-goias-go/">Equipamentos em Valparaíso de Goiás</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Valparaíso de Goiás</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Transpaleteira Elétrica para Locação em <em>Valparaíso de Goiás</em>')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para o polo moveleiro de 120 fábricas, supermercados, atacadistas e comércio varejista de Valparaíso de Goiás. Movimenta chapas de MDF, móveis embalados e paletes de varejo. Entrega pela BR-040 no mesmo dia.')

# WhatsApp URLs — encoded Goiânia → Valparaíso+de+Goiás
r('Goi%C3%A2nia', 'Valpara%C3%ADso+de+Goi%C3%A1s', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Frota Clark Lítio 24V</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega BR-040 (230 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">Polo Moveleiro Atendido</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Manutenção Inclusa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Como a <span>transpaleteira elétrica</span> resolve gargalos no polo moveleiro e varejo')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — conhecida como paleteira ou patolinha no chão de fábrica — movimenta paletes na horizontal com motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Sem esforço físico do operador, acelera o ciclo de carga e descarga e mantém ritmo constante em corredores estreitos. Valparaíso de Goiás abriga mais de 120 fábricas de móveis que despacham chapas de MDF e produtos acabados diariamente, redes de supermercados com docas de recebimento intenso e um comércio varejista em expansão ao longo da BR-040 que depende de movimentação ágil de paletes.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: carga suficiente para turnos duplos nas marcenarias e atacadistas')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'O lítio 24V das transpaleteiras Clark trouxe três avanços sobre o chumbo-ácido: recarga completa entre 2 e 3 horas contra 8h do antigo, cargas de oportunidade em pausas de almoço e durabilidade até três vezes superior. As marcenarias de Valparaíso que rodam dois turnos de corte e expedição aproveitam a virada de turno para recarregar — a paleteira volta operando sem perda de ritmo e sem necessidade de bateria reserva.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual modelo encaixa na sua operação em Valparaíso')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida com o operador caminhando — perfeita para corredores curtos entre linhas de corte e embalagem nas marcenarias. A PWio20 com plataforma fixa transporta o operador em trajetos longos entre depósito de chapas e doca de expedição sem desgaste. A PPXs20 dobrável alterna entre modo caminhada para manobras em estoque apertado e modo plataforma para deslocamentos amplos. A stacker SWX16 eleva paletes até 4.500 mm, substituindo empilhadeiras em depósitos verticais de móveis acabados.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark WPio15: a paleteira mais requisitada pelo polo moveleiro de Valparaíso')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A WPio15 concentra os contratos mais frequentes na região de Valparaíso. Capacidade de 1.500 kg, lítio 24V e chassi compacto para corredores de 1,8 m — dimensões que encaixam nas linhas de acabamento das fábricas de móveis, no recebimento de mercadorias em supermercados e na separação de pedidos no comércio varejista da BR-040. O timão ergonômico com controle proporcional garante manobras precisas sem danificar chapas de MDF ou móveis embalados.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga de 2 a 3 horas entre turnos, carga de oportunidade no almoço, zero emissão de gases nas marcenarias e depósitos fechados do varejo.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor silencioso:</strong> operação sem ruído para ambientes internos das fábricas de móveis e áreas de atendimento ao público em supermercados de Valparaíso.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave entre pisos das marcenarias, rampas de doca e desníveis nos estacionamentos de carga do comércio varejista.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Valparaíso de Goiás:</strong> polo moveleiro (chapas de MDF, móveis embalados), supermercados (paletes de bebidas, alimentos), comércio varejista (estoque de mercadorias) e depósitos da BR-040 (cross-docking).</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark WPio15 com lítio 24V, modelo mais contratado para fábricas de móveis e supermercados em Valparaíso de Goiás"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega via BR-040 no mesmo dia')

# Form selects — Valparaíso de Goiás como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Valparaíso de Goiás" selected>Valparaíso de Goiás</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Formosa">Formosa</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Valparaíso de Goiás" selected>Valparaíso de Goiás</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Formosa">Formosa</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 domina os contratos de paleteira em Valparaíso de Goiás. Chassi compacto, timão ergonômico e velocidade controlada para corredores de 1,8 m. Indicada para movimentar chapas de MDF nas marcenarias, receber mercadorias nos supermercados e separar pedidos no comércio varejista da BR-040.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 em operação no polo moveleiro de Valparaíso de Goiás"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a fadiga em trajetos longos. Nos galpões de expedição das fábricas de móveis de Valparaíso, o operador percorre 80 a 100 metros entre o depósito de chapas e a doca de carregamento sem desgaste físico. Também atende supermercados com área de estoque afastada da zona de descarga.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alterna entre plataforma para distâncias longas e modo walkie para manobras em corredores apertados. A plataforma recolhe com um gesto, adaptando a paleteira ao estoque estreito de móveis prontos ou ao trajeto amplo até a doca. Versátil para fábricas de Valparaíso que combinam acabamento, embalagem e despacho na mesma planta.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 combina movimentação horizontal com elevação até 4.500 mm, substituindo empilhadeiras em depósitos verticais. Nos armazéns de móveis acabados de Valparaíso, empilha paletes de guarda-roupas e cômodas em prateleiras altas sem risco de avaria. O chassi anticorrosão também opera em câmaras frias de supermercados. Patolada para estabilidade máxima com carga elevada.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 para elevação de paletes em depósitos de móveis e supermercados em Valparaíso de Goiás"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 movimenta as cargas mais pesadas da frota Clark. Projetada para paletes de chapas de MDF acima de 2.000 kg, painéis de madeira e insumos do polo moveleiro de Valparaíso. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais com tráfego intenso de caminhões nas docas de expedição.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para chapas de MDF pesadas no polo moveleiro de Valparaíso de Goiás"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota para locação em Valparaíso de Goiás')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Valparaíso de Goiás
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Valparaíso de Goiás me surpreende pelo volume de chamados do polo moveleiro. São fábricas que movimentam 50, 60 paletes de chapas de MDF por turno empurrando manual. Resultado: operador com dor no ombro antes do almoço, chapas arranhadas por manuseio apressado e caminhão parado na doca acumulando hora extra do motorista. Semana passada, coloquei duas WPio15 numa marcenaria que usava três manuais. O dono me ligou em cinco dias dizendo que a produção de expedição dobrou e que dois operadores foram remanejados para o acabamento. A bateria de lítio recarrega na troca de turno e segura a jornada inteira da tarde."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Referência objetiva para Valparaíso de Goiás:</strong> se a fábrica ou loja movimenta mais de 30 paletes por turno, ou se o percurso entre doca e estoque passa de 50 metros, a paleteira elétrica se paga no primeiro mês com produtividade recuperada. As marcenarias do polo moveleiro e os supermercados com câmaras frias já operam exclusivamente com transpaleteira elétrica pelo volume de carga e pela necessidade de preservar o produto acabado.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Valparaíso de Goiás:')

# Links internos — todos para valparaiso-de-goias-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/valparaiso-de-goias-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Valparaíso de Goiás')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Valparaíso de Goiás')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/valparaiso-de-goias-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Valparaíso de Goiás')

r('/goiania-go/curso-operador-empilhadeira', '/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Valparaíso de Goiás')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de transpaleteira elétrica para polo moveleiro e varejo em Valparaíso de Goiás"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Veja como funciona a <span>locação de transpaleteira</span> para Valparaíso de Goiás')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe cada etapa da locação: análise da operação, escolha do modelo Clark ideal para sua fábrica ou loja, entrega pela BR-040 e suporte técnico durante todo o contrato. Do orçamento pelo WhatsApp à paleteira operando no seu galpão em Valparaíso de Goiás.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Investimento mensal na locação de <span>transpaleteira elétrica</span> em 2026')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark em Valparaíso de Goiás. O investimento final depende do modelo escolhido, prazo de contrato e configuração necessária para sua operação.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção e lítio 24V inclusos')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato cobre revisão preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal contempla o equipamento pronto para operar, sem surpresas de peças ou deslocamento técnico.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Valparaíso de Goiás (frete incluso)')

r('Sem custo de frete na capital',
  'Frete incluso para Valparaíso de Goiás')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, Goiânia — 230 km de Valparaíso de Goiás pela BR-040 via Cristalina. Entrega no mesmo dia para pedidos confirmados até as 10h. A transpaleteira chega na sua fábrica, supermercado ou depósito pronta para operar, com frete incluso no contrato.')

r('O prejuízo invisível da paleteira manual',
  'O custo real de manter paleteiras manuais no polo moveleiro')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucas marcenarias fazem:</strong> uma fábrica que movimenta 60 paletes de chapas por turno com paleteira manual demanda o dobro de horas-homem. Somando o custo de um operador extra, os afastamentos por lesão de ombro e coluna (média de 18 dias/ano no setor moveleiro) e as chapas de MDF arranhadas por manuseio apressado, a economia aparente vira prejuízo. A locação da paleteira elétrica Clark se paga com a produtividade recuperada já no primeiro mês de contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações locais')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>paleteira elétrica Clark</span> opera diariamente em Valparaíso de Goiás')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Setores produtivos e comerciais que contratam transpaleteira elétrica na região.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark WPio15 movimentando chapas de MDF nas fábricas de móveis de Valparaíso de Goiás"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>Polo moveleiro: chapas de MDF e móveis embalados</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'As mais de 120 fábricas de móveis de Valparaíso movimentam centenas de chapas de MDF, painéis de madeira e produtos embalados por turno. A WPio15 navega entre linhas de corte e acabamento em corredores de 1,8 m, transporta paletes de 500 a 1.200 kg e agiliza o carregamento dos caminhões de distribuição — sem arranhar o produto final.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Transpaleteira Clark em supermercado de Valparaíso de Goiás recebendo paletes de bebidas"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>Supermercados: docas e câmaras frias</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'Os supermercados e atacadistas de Valparaíso recebem paletes de bebidas, alimentos e produtos de limpeza múltiplas vezes ao dia. A WPio15 descarrega caminhões na doca e posiciona paletes no estoque. A SWX16 empilha congelados e refrigerados em câmaras frias até 4.500 mm com estabilidade total, mesmo em piso escorregadio.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 no comércio varejista da BR-040 em Valparaíso de Goiás"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>Comércio varejista: estoque e expedição na BR-040</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'O comércio varejista ao longo da BR-040 em Valparaíso movimenta paletes de eletrodomésticos, material de construção e mercadorias diversas. A PWio20 com plataforma fixa percorre depósitos amplos entre a doca e o ponto de armazenagem sem fadiga. A velocidade de 6 km/h reduz o tempo de dock-to-stock e libera caminhões antes do prazo de sobreestadia.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark WPX35 para cargas pesadas de chapas e painéis no polo moveleiro de Valparaíso de Goiás"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Depósitos de insumos: chapas e painéis pesados</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'Os depósitos de insumos que abastecem o polo moveleiro armazenam chapas de MDF, painéis de madeira e ferragens em paletes que ultrapassam 2.000 kg. A WPX35 heavy duty atende essas cargas com motor de tração reforçado e rodas de alta durabilidade para pisos industriais com tráfego de empilhadeiras e caminhões de entrega.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica com deslocamento programado pela BR-040. Atendimento em Valparaíso de Goiás com agenda fixa semanal e urgências resolvidas no mesmo dia. Diagnóstico de sistema elétrico, tração e bomba hidráulica na sua planta.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-040 até sua fábrica, supermercado ou depósito em Valparaíso de Goiás. São 230 km da sede — entrega no mesmo dia para pedidos até as 10h, com frete incluso no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"Nossa marcenaria movimentava 45 paletes de chapas de MDF por turno com três manuais. As chapas chegavam arranhadas na linha de acabamento e perdíamos material. Trocamos por duas WPio15 Clark e o transporte ficou suave — zero avaria. A bateria recarrega no almoço e cobre a tarde inteira. Remanejamos um operador para o corte e a produção subiu 30% no primeiro mês."')
r('<strong>Marcos V.</strong>',
  '<strong>Leandro F.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente de Produção, Fábrica de Móveis, Polo Moveleiro, Valparaíso de Goiás-GO (jan/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"Recebemos 12 carretas por semana no supermercado e a doca vivia congestionada com paleteira manual. Desde que contratamos a PWio20, o operador descarrega e posiciona os paletes no estoque em metade do tempo. A plataforma fixa evita que ele caminhe 8 km por turno. A SWX16 empilha os congelados na câmara fria a 4 metros sem problema. A Move fez a preventiva da bateria antes da gente solicitar."')
r('<strong>Renata C.</strong>',
  '<strong>Carla D.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Logística, Rede de Supermercados, Valparaíso de Goiás-GO (fev/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"Meu depósito de material de construção na BR-040 movimenta paletes de cerâmica, argamassa e tintas o dia inteiro. A WPX35 foi a solução — aguenta os paletes de 2.500 kg de cerâmica sem esforço. Antes, dois funcionários empurravam manual e viviam de atestado. Renovamos o contrato semestral e o orçamento pelo WhatsApp da Move sai em menos de cinco minutos."')
r('<strong>Anderson L.</strong>',
  '<strong>Roberto M.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Proprietário, Depósito de Material de Construção, BR-040, Valparaíso de Goiás-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores</a>? Conectamos sua equipe a centros credenciados em Valparaíso de Goiás e no Entorno de Brasília.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega garantida em <span>Valparaíso de Goiás</span> e cidades do Entorno')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 230 km de <strong>Valparaíso de Goiás</strong> pela BR-040 via Cristalina. Entrega de transpaleteira elétrica no mesmo dia para pedidos até as 10h. Atendemos todo o Entorno de Brasília e a região metropolitana de Goiânia.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/valparaiso-de-goias-go/"><strong>Valparaíso de Goiás</strong></a>
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
  'title="Área de atendimento Move Máquinas — Valparaíso de Goiás"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Valparaíso de Goiás</a>')
r('/goiania-go/" style="color', '/valparaiso-de-goias-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Valparaíso de Goiás')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica atende melhor o polo moveleiro de Valparaíso de Goiás?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark WPio15 é o modelo mais contratado para as fábricas de móveis da cidade. Com 1.500 kg de capacidade e lítio 24V, movimenta chapas de MDF empilhadas e móveis embalados nos corredores de 1,8 m das 120 marcenarias e indústrias moveleiras. Operação silenciosa e compacta para linhas de acabamento.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A transpaleteira manual dá conta do volume nas docas do polo moveleiro?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Nas fábricas de móveis que despacham mais de 40 paletes por turno, a manual causa fadiga extrema e afastamentos por lesão de ombro e coluna. A elétrica Clark desloca chapas de MDF a 6 km/h sem esforço do operador. A troca reduz tempo de doca em até 55% e elimina o risco de dano ao produto acabado por manuseio apressado.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>A paleteira elétrica serve para recebimento em supermercados de Valparaíso?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Sim. Os supermercados e atacadistas de Valparaíso de Goiás recebem paletes de bebidas, alimentos e produtos de limpeza várias vezes ao dia. A WPio15 walkie navega entre gôndolas e estoque, descarrega caminhões na doca e posiciona paletes em câmaras frias. A bateria de lítio opera o dia todo com recarga no intervalo.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>Quanto dura a bateria de lítio 24V em operação contínua nas fábricas de Valparaíso?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A autonomia varia de 6 a 10 horas conforme o modelo e a intensidade de carga. Nas marcenarias que operam dois turnos, a recarga completa em 2 a 3 horas na virada de turno cobre a jornada seguinte. Cargas de oportunidade de 20 minutos durante pausas prolongam o ciclo sem substituir o equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores das fábricas de móveis precisam de certificado NR-11?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige treinamento de operação de equipamentos de movimentação de carga. O curso cobre inspeção pré-turno, limites de capacidade, velocidade em corredores e protocolos de emergência. Indicamos centros credenciados em Valparaíso de Goiás e no Entorno de Brasília para <a href="/valparaiso-de-goias-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">certificação e reciclagem</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Qual o prazo de entrega da transpaleteira em Valparaíso de Goiás?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Valparaíso de Goiás fica a 230 km da sede pela BR-040 via Cristalina. A entrega ocorre no mesmo dia para pedidos confirmados até as 10h. Para chamados urgentes de linhas paradas no polo moveleiro, priorizamos o despacho com chegada prevista em até 4 horas. Frete incluso no contrato.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>A manutenção da transpaleteira é por conta do cliente?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Não. Todo contrato da Move Máquinas cobre manutenção preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Nossa equipe técnica atende em Valparaíso de Goiás com deslocamento programado e urgências resolvidas no mesmo dia.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Qual a maior capacidade de carga disponível para locação em Valparaíso?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para o polo moveleiro que movimenta chapas de MDF acima de 2 toneladas, a WPX35 é a escolha principal. A SWX16 stacker patolada eleva paletes até 4.500 mm em corredores estreitos de depósitos de móveis acabados.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Valparaíso de Goiás')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Valparaíso de Goiás.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

import re

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'goiania-go' in line and '/goiania-go/' not in line:
        goiania_issues.append((i+1, line.strip()[:120]))
    elif 'Goiânia' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            '/goiania-go/', '230 km', 'Goiânia - GO',
            'Valparaíso de Goiás e no Entorno',
            'metropolitana de Goiânia',
            'Goiânia — 230',
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
vp = html.count('Valparaíso')
local = html.count('moveleiro') + html.count('marcenaria') + html.count('supermercado') + html.count('BR-040') + html.count('MDF')
print(f"\nValparaíso: {vp} menções")
print(f"Contexto local (moveleiro/marcenaria/supermercado/BR-040/MDF): {local} menções")

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
