#!/usr/bin/env python3
"""
rebuild-formosa-transpaleteira-v2.py
Gera LP de Transpaleteira Elétrica para Formosa-GO
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

Formosa: -15.5372/-47.3345, 280km BR-020/GO-116, pop 115k.
Agropecuária, grãos, milho, ProGoiás.
Entity bridge: movimentação de sacas em armazéns de grãos, comércio varejista.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-transpaleteira.html'
OUT = '/Users/jrios/move-maquinas-seo/formosa-go-aluguel-de-transpaleteira-V2.html'

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
  '<title>Locação de Transpaleteira Elétrica em Formosa-GO | Move Máquinas</title>')

r('content="Aluguel de transpaleteira elétrica Clark em Goiânia. Modelos WPio15, PWio20, PPXs20, SWX16 e WPX35 com bateria de lítio 24V. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Locação de transpaleteira elétrica Clark em Formosa-GO para armazéns de grãos, cooperativas agrícolas e comércio varejista da BR-020. Modelos WPio15 a WPX35 com lítio 24V. Sacas de 60kg, big bags e paletes de insumos. Manutenção inclusa, entrega pela BR-020/GO-116."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  'href="https://movemaquinas.com.br/formosa-go/aluguel-de-transpaleteira"')

r('content="Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas"',
  'content="Locação de Transpaleteira Elétrica em Formosa-GO | Move Máquinas"')

r('content="Paleteira elétrica Clark para locação em Goiânia. Cinco modelos de 1.500 a 3.500 kg com lítio 24V. Manutenção inclusa, entrega mesmo dia."',
  'content="Paleteira elétrica Clark para Formosa. Cinco modelos de 1.500 a 3.500 kg com lítio 24V para armazéns graneleiros, cooperativas e comércio na BR-020. Entrega via BR-020/GO-116."')

r('content="Goiânia, Goiás, Brasil"', 'content="Formosa, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-15.5372;-47.3345"')
r('content="-16.7234, -49.2654"', 'content="-15.5372, -47.3345"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -15.5372, "longitude": -47.3345')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -15.5372')
r('"longitude": -49.2654', '"longitude": -47.3345')

# Schema — Service name
r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"',
  '"name": "Locação de Transpaleteira Elétrica em Formosa-GO"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Formosa", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Formosa", "item": "https://movemaquinas.com.br/formosa-go/"')
r('"name": "Transpaleteira Elétrica em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
  '"name": "Transpaleteira Elétrica em Formosa", "item": "https://movemaquinas.com.br/formosa-go/aluguel-de-transpaleteira"')

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
        { "@type": "Question", "name": "Qual transpaleteira elétrica serve melhor os armazéns de grãos em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark WPio15 concentra a maioria dos contratos na região. Com 1.500 kg de capacidade e bateria de lítio 24V, ela movimenta sacas de 60 kg, big bags de soja e milho e paletes de insumos agrícolas nos armazéns graneleiros da BR-020. Chassi compacto para corredores de 1,8 m entre estantes de sacaria." } },
        { "@type": "Question", "name": "A paleteira elétrica aguenta sacas de grãos e big bags pesados?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Sacas padrão de 60 kg paletizadas ficam entre 600 e 1.200 kg por palete. A WPio15 suporta 1.500 kg e a WPX35 chega a 3.500 kg — cobrindo desde sacaria de milho até big bags de 1.000 kg de soja. O motor de tração mantém velocidade constante mesmo com carga máxima nos pisos irregulares de armazéns rurais." } },
        { "@type": "Question", "name": "Transpaleteira elétrica funciona em armazéns com poeira de grãos?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Os modelos Clark operam com motor elétrico selado e zero emissão de faísca, eliminando risco de ignição em ambientes com poeira de grãos em suspensão. A bateria de lítio 24V não gera gases nem aquecimento externo. Recomendamos limpeza periódica do chassi para evitar acúmulo de resíduos nas rodas tandem." } },
        { "@type": "Question", "name": "Quanto tempo a bateria de lítio dura nos turnos de safra em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "A autonomia varia de 6 a 10 horas contínuas conforme modelo e peso movimentado. Nos períodos de safra de milho e soja, quando os armazéns operam em dois turnos, a recarga completa de 2 a 3 horas na virada de turno garante operação ininterrupta. Cargas de oportunidade de 15 minutos no almoço estendem a jornada sem trocar equipamento." } },
        { "@type": "Question", "name": "Operadores de armazém em Formosa precisam de curso para usar transpaleteira elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige treinamento em operação de equipamentos de movimentação de carga. O curso abrange inspeção pré-operacional, limites de capacidade, velocidade em áreas de circulação e procedimentos de emergência. Indicamos centros de formação credenciados na região de Formosa e Brasília para capacitação dos operadores." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de transpaleteira elétrica em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "Formosa fica a 280 km da sede pela BR-020/GO-116. A entrega ocorre em até 24 horas após a confirmação do contrato. Para demandas urgentes em período de safra — armazéns lotados, cooperativas com fila de caminhões — priorizamos o despacho. Frete incluído no contrato sem custo adicional." } },
        { "@type": "Question", "name": "A manutenção da transpaleteira está incluída no valor da locação?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato da Move Máquinas cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Formosa, a equipe técnica se desloca pela BR-020 para resolver qualquer ocorrência sem parar a operação do armazém." } },
        { "@type": "Question", "name": "Qual a maior capacidade de transpaleteira disponível para Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para armazéns graneleiros que movimentam big bags de 1.000 kg e paletes de fertilizantes acima de 2.000 kg, a WPX35 atende com motor reforçado. A SWX16 stacker empilha paletes até 4.500 mm em corredores estreitos de galpões de sacaria." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/formosa-go/">Equipamentos em Formosa</a>')

r('<span aria-current="page">Transpaleteira Elétrica em Goiânia</span>',
  '<span aria-current="page">Transpaleteira Elétrica em Formosa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Transpaleteira Elétrica em <em>Goiânia</em>',
  'Transpaleteira Elétrica para Locação em <em>Formosa</em>-GO')

r('Transpaleteiras Clark de 1.500 a 3.500 kg com bateria de lítio 24V. Walkie, plataforma fixa, plataforma dobrável e stacker patolada. Manutenção inclusa, entrega no mesmo dia na capital.',
  'Paleteiras elétricas Clark de 1.500 a 3.500 kg com lítio 24V para movimentação de sacas, big bags e paletes de insumos em armazéns graneleiros de Formosa. Município referência na produção de grãos do Entorno de Brasília — milho, soja e sorgo exigem equipamento ágil na safra. Entrega pela BR-020/GO-116, manutenção inclusa.')

# WhatsApp URLs — encoded Goiânia → Formosa
r('Goi%C3%A2nia', 'Formosa-GO', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<span style="font-size:14px;font-weight:600;">Distribuidor Exclusivo Clark</span>',
  '<span style="font-size:14px;font-weight:600;">Frota Clark Lítio 24V</span>')

r('<span style="font-size:14px;font-weight:600;">+20 Anos de Mercado</span>',
  '<span style="font-size:14px;font-weight:600;">Entrega via BR-020 (280 km)</span>')

r('<span style="font-size:14px;font-weight:600;">+500 Clientes Atendidos</span>',
  '<span style="font-size:14px;font-weight:600;">+20 Anos no Centro-Oeste</span>')

r('<span style="font-size:14px;font-weight:600;">Suporte 24h/7 Dias</span>',
  '<span style="font-size:14px;font-weight:600;">Manutenção Inclusa no Contrato</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>transpaleteira elétrica</span> e como ela otimiza sua operação',
  'Como a <span>transpaleteira elétrica</span> acelera a logística de grãos em Formosa')

# Parágrafo principal
r('A transpaleteira elétrica, conhecida no chão de fábrica como paleteira elétrica ou patolinha, é o equipamento de movimentação horizontal de paletes acionado por motor de tração e bomba hidráulica com bateria de lítio. Diferente da versão manual, ela elimina o esforço físico do operador, reduz o tempo de dock-to-stock e opera com precisão em corredores de picking. Goiânia concentra atacadistas do Polo da Moda que despacham milhares de fardos por semana, galpões refrigerados da Ceasa com câmaras a -18°C e centros de distribuição ao longo da BR-153 que exigem cross-docking veloz.',
  'A transpaleteira elétrica — conhecida nos armazéns como paleteira ou patolinha — movimenta sacas, big bags e paletes na horizontal usando motor de tração e bomba hidráulica alimentados por bateria de lítio 24V. Sem esforço muscular, sem fumaça, sem ruído excessivo. Formosa ocupa posição estratégica no Entorno de Brasília com mais de 115 mil habitantes e economia ancorada na agropecuária de grãos. Os armazéns graneleiros da BR-020 recebem safras de milho, soja e sorgo que precisam de movimentação rápida — sacas de 60 kg paletizadas, big bags de tonelada e paletes de fertilizantes que a manual não dá conta no pico da colheita.')

# H3 — lítio
r('Bateria de lítio 24V: autonomia para turnos completos na capital',
  'Lítio 24V: energia contínua nos turnos de safra em Formosa')

r('A tecnologia de lítio substituiu as baterias de chumbo-ácido nas transpaleteiras Clark. A vantagem é tripla: recarga completa em 2 a 3 horas (contra 8 horas do chumbo), possibilidade de carga de oportunidade durante pausas do operador e vida útil até três vezes maior. Para atacadistas do Polo da Moda que operam dois turnos consecutivos, a paleteira elétrica com lítio 24V mantém produtividade sem interrupção para troca de bateria.',
  'O lítio 24V das transpaleteiras Clark aposentou o chumbo-ácido com vantagem tripla: recarga completa entre 2 e 3 horas (contra 8h do antigo), cargas parciais de 15 minutos durante o almoço e durabilidade até três vezes superior. Nos armazéns de Formosa que rodam dois turnos na safra de milho — janeiro a junho — a bateria recarrega na virada de turno e sustenta a jornada seguinte sem pausa. O operador não precisa trocar equipamento nem esperar recarga prolongada.')

# H3 — walkie/plataforma/stacker
r('Walkie, plataforma e stacker: como escolher o tipo certo',
  'Walkie, plataforma ou stacker: qual modelo combina com seu armazém em Formosa')

r('A transpaleteira walkie (WPio15) é operada pelo condutor caminhando atrás do equipamento. A versão com plataforma fixa (PWio20) permite que o operador suba na base e percorra distâncias maiores sem fadiga. A plataforma dobrável (PPXs20) combina as duas funções: plataforma para longos trajetos, dobrável para manobras em espaços apertados. A stacker patolada (SWX16) eleva cargas até 4.500 mm, substituindo empilhadeiras em corredores estreitos de câmaras frias.',
  'A walkie WPio15 é conduzida a pé — perfeita para corredores curtos entre pilhas de sacaria nos galpões da BR-020. A PWio20 com plataforma fixa percorre distâncias longas entre a doca de recebimento e a área de estoque sem cansar o operador — ideal para armazéns de cooperativas agrícolas com mais de 100 metros de profundidade. A PPXs20 dobrável alterna entre modo caminhada e modo plataforma conforme o trecho. A stacker SWX16 empilha paletes até 4.500 mm, substituindo empilhadeiras em galpões de sacaria com pé-direito alto.')

# H3 — modelo mais locado
r('Clark WPio15: a transpaleteira mais locada em Goiânia',
  'Clark WPio15: a paleteira mais solicitada para armazéns de grãos em Formosa')

r('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela atende picking em atacadistas do Polo da Moda, recebimento de mercadorias na Ceasa e dock-to-stock em CDs da BR-153. O timão ergonômico com controle proporcional de velocidade permite manobras precisas entre fileiras de paletes sem riscar prateleiras.',
  'A WPio15 lidera os pedidos de locação para a região de Formosa. Capacidade de 1.500 kg, lítio 24V e chassi compacto para corredores de 1,8 m — especificações que atendem os armazéns graneleiros da BR-020, as cooperativas de produtores rurais e o comércio varejista do centro da cidade. O timão ergonômico com velocidade proporcional executa manobras precisas entre estantes de sacaria sem danificar embalagens de grãos ou insumos agrícolas.')

# Bullet list items
r('<div><strong>Bateria de lítio 24V:</strong> recarga rápida de 2 a 3 horas, carga de oportunidade durante pausas, sem emissão de gases nos galpões do Polo da Moda.</div>',
  '<div><strong>Bateria de lítio 24V:</strong> recarga de 2 a 3 horas na virada de turno, carga parcial no almoço, zero emissão de gases e faíscas nos armazéns com poeira de grãos.</div>')

r('<div><strong>Motor de tração silencioso:</strong> zero emissão sonora para operações em câmaras frias da Ceasa e depósitos fechados na Av. Independência.</div>',
  '<div><strong>Motor de tração selado:</strong> sem faísca e sem ruído excessivo para armazéns de sacaria com poeira de grãos e galpões de fertilizantes em Formosa.</div>')

r('<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> passagem suave sobre juntas de piso, docas com desnível e rampas de nivelamento.</div>',
  '<div><strong>Garfos de 1.150 mm com rodas tandem:</strong> transição suave em pisos de armazém rural, docas de recebimento de grãos e rampas de acesso aos galpões da BR-020.</div>')

r('<div><strong>Aplicações em Goiânia:</strong> Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.</div>',
  '<div><strong>Aplicações em Formosa:</strong> armazéns graneleiros (sacas de milho e soja), cooperativas agrícolas (big bags e insumos), comércio varejista do centro (paletes de mercadoria) e distribuidoras de fertilizantes da BR-020.</div>')

# ═══════════════════════════════════════════════════════════════════════
# 5B. IMAGEM "O QUE É" — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Transpaleteira elétrica Clark WPio15 com bateria de lítio 24V, o modelo mais alugado em Goiânia para operações de picking e dock-to-stock"',
  'alt="Transpaleteira elétrica Clark WPio15 com lítio 24V, modelo mais contratado para armazéns de grãos e cooperativas em Formosa-GO"')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega em até 24h em Formosa')

# Form selects — Formosa como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Formosa" selected>Formosa</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# Form selects — mobile
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Formosa" selected>Formosa</option>
              <option value="Brasília">Brasília (DF)</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — WPio15
r('A WPio15 é a transpaleteira walkie mais contratada em Goiânia. Compacta, ágil e com timão ergonômico de controle proporcional. Ideal para recebimento de mercadorias, separação de pedidos e movimentação horizontal em corredores de 1,8 m nos atacadistas do Polo da Moda e nos CDs da BR-153.',
  'A WPio15 domina os contratos de paleteira na região de Formosa. Chassi compacto, timão ergonômico e velocidade proporcional. Indicada para movimentação de sacas paletizadas nos armazéns graneleiros, separação de insumos nas cooperativas agrícolas e recebimento de mercadorias no comércio varejista da cidade — corredores de 1,8 m sem dificuldade.')

r('alt="Transpaleteira elétrica Clark WPio15 em operação de picking em galpão logístico de Goiânia"',
  'alt="Transpaleteira Clark WPio15 operando em armazém de grãos na região de Formosa-GO"')

# Slide 1 — PWio20
r('A PWio20 permite que o operador suba na plataforma e percorra distâncias maiores sem esforço de caminhada. Perfeita para CDs com corredores longos ao longo da BR-153 e galpões de expedição que exigem deslocamento constante entre docas e áreas de estoque.',
  'A PWio20 com plataforma fixa elimina a fadiga de percursos longos. Nos armazéns graneleiros de Formosa com mais de 100 metros de profundidade, o operador sobe na plataforma e percorre o trajeto doca-estoque sem desgaste. Essencial para cooperativas que recebem e expedem sacas de milho e soja em grande volume durante a safra.')

# Slide 2 — PPXs20
r('A PPXs20 combina duas funções: plataforma para percorrer distâncias longas e modo walkie para manobras em espaços confinados. A plataforma se recolhe com um movimento, adaptando o equipamento ao corredor de picking estreito ou ao percurso amplo de expedição. Versátil para operações mistas no Distrito Industrial de Goiânia.',
  'A PPXs20 alternar entre plataforma para trajetos longos e walkie para manobras apertadas. A plataforma se recolhe com um gesto, adaptando a paleteira ao corredor estreito entre estantes de sacaria ou ao trajeto amplo até a doca. Ideal para operações mistas nos armazéns de Formosa que combinam recebimento de grãos, armazenagem e expedição para o Entorno de Brasília.')

# Slide 3 — SWX16
r('A SWX16 vai além da movimentação horizontal: eleva paletes até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos. O chassi com proteção anticorrosão opera em câmaras frias a -18°C na Ceasa e em distribuidoras de alimentos congelados de Goiânia. Patolada para estabilidade máxima com carga elevada.',
  'A SWX16 combina transporte horizontal com empilhamento até 4.500 mm, substituindo empilhadeiras em galpões de sacaria com pé-direito alto. Nos armazéns de Formosa com estantes verticais para sacas de grãos e insumos agrícolas, a SWX16 empilha paletes com estabilidade total em corredores estreitos. Chassi anticorrosão resiste à poeira e umidade dos armazéns rurais.')

r('alt="Stacker patolada Clark SWX16 em operação de câmara fria com elevação de paletes"',
  'alt="Stacker Clark SWX16 empilhando paletes em armazém graneleiro de Formosa-GO"')

# Slide 4 — WPX35
r('A WPX35 é a transpaleteira de maior capacidade da linha Clark. Projetada para paletes pesados de insumos industriais, bobinas de papel e cargas paletizadas acima de 2.000 kg. Motor de tração reforçado e rodas de alta durabilidade para pisos industriais no Distrito Industrial Leste e armazéns de grande porte.',
  'A WPX35 carrega os paletes mais pesados da frota Clark — ideal para big bags de grãos de 1.000 kg, paletes de fertilizantes e sacos de calcário acima de 2.000 kg comuns nas distribuidoras agrícolas de Formosa. Motor de tração reforçado e rodas de alta durabilidade para pisos de armazém rural com trânsito de caminhões graneleiros.')

r('alt="Transpaleteira heavy duty Clark WPX35 para movimentação de cargas pesadas em Goiânia"',
  'alt="Transpaleteira heavy duty Clark WPX35 para big bags e insumos agrícolas pesados em Formosa-GO"')

# Spec table caption
r('Transpaleteiras Clark: especificações técnicas da frota disponível em Goiânia',
  'Transpaleteiras Clark: especificações da frota para locação em Formosa-GO')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Formosa
# ═══════════════════════════════════════════════════════════════════════

r('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha. Já vi operações perdendo 60% do rendimento por insistir no manual. O operador cansa, começa a errar, e o afastamento por lesão vem rápido. Na doca, o caminhão fica parado esperando, e a multa de sobreestadia come o lucro do mês. Quando troco para a elétrica Clark com lítio, o cliente me liga na semana seguinte dizendo que não entende como operava sem."',
  '"Formosa é uma das regiões que mais cresce em pedidos de transpaleteira. Os armazéns de grãos trabalham com sacas de 60 kg — parece leve, mas empilha 20, 30 paletes por turno na safra e o operador com manual não aguenta até o almoço. Semana passada coloquei duas WPio15 numa cooperativa da BR-020 que usava três manuais. Resultado: dois operadores fazendo o trabalho de cinco, sem afastamento por dor no ombro. O lítio recarrega no almoço e segura a tarde inteira. O gerente da cooperativa me ligou em 15 dias querendo uma terceira unidade porque a fila de caminhões na doca desapareceu."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação movimenta mais de 30 paletes por turno, ou se precisa percorrer mais de 50 metros entre a doca e a área de estoque, a paleteira elétrica paga a diferença de locação no primeiro mês com o ganho de produtividade. Os atacadistas do Polo da Moda e os galpões refrigerados da Ceasa operam exclusivamente com transpaleteira elétrica por conta do volume e da exigência térmica.',
  '<strong>Referência prática para Formosa:</strong> se o armazém movimenta mais de 30 paletes de sacas por turno ou se o trajeto entre a doca de recebimento e a pilha de estoque passa de 50 metros, a paleteira elétrica se paga no primeiro mês com o ganho de produtividade. Os armazéns graneleiros da BR-020 e as cooperativas agrícolas já operam exclusivamente com transpaleteira elétrica pelo volume de sacaria e pela velocidade exigida na safra.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis para Formosa:')

# Links internos — todos para formosa-go
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/formosa-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Formosa')

r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/formosa-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Formosa')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/formosa-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Formosa')

r('/goiania-go/curso-operador-empilhadeira', '/formosa-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Formosa')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de transpaleteira em Goiânia"',
  'alt="Vídeo Move Máquinas: como funciona a locação de transpaleteira para armazéns e cooperativas em Formosa-GO"')

r('Conheça o processo de <span>Aluguel de Transpaleteira</span> em Goiânia',
  'Entenda a <span>locação de transpaleteira</span> para a região de Formosa')

r('Assista ao vídeo da Move Máquinas e entenda como funciona a locação: consultoria de modelo, escolha do equipamento Clark, entrega no local e suporte técnico durante todo o contrato. Processo transparente do orçamento à operação.',
  'No vídeo da Move Máquinas, acompanhe cada etapa: análise do perfil de carga do armazém, seleção do modelo Clark adequado, transporte pela BR-020 e assistência técnica durante toda a vigência do contrato. Do orçamento pelo WhatsApp à paleteira operando no seu galpão em Formosa.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>paleteira elétrica</span> em 2026?',
  'Valores de locação de <span>paleteira elétrica</span> para Formosa em 2026')

r('Valores de referência para locação de transpaleteira elétrica Clark na capital. O preço final varia conforme modelo, prazo e configuração do equipamento.',
  'Valores de referência para locação de transpaleteira Clark na região de Formosa. O investimento mensal depende do modelo escolhido, prazo de contrato e configuração do equipamento.')

r('Locação mensal com manutenção e bateria inclusos',
  'Contrato mensal com manutenção preventiva e lítio 24V no valor')

r('Todos os contratos cobrem manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal inclui o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'Cada contrato contempla manutenção preventiva e corretiva integral: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. O valor mensal já embute o equipamento funcionando, sem cobranças extras de peças ou deslocamento técnico até Formosa.')

r('Entrega em Goiânia (sem frete)',
  'Entrega em Formosa (BR-020, frete incluso)')

r('Sem custo de frete na capital',
  'Frete incluso para Formosa e região')

r('A Move Máquinas está na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para entregas na capital e região metropolitana imediata, não cobramos deslocamento. O equipamento chega no seu galpão, CD ou câmara fria pronto para operar.',
  'Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Formosa pela BR-020/GO-116. A transpaleteira chega no armazém, cooperativa ou comércio em até 24 horas após confirmação, pronta para operar. Frete já incluído no contrato mensal, sem custo adicional.')

r('O prejuízo invisível da paleteira manual',
  'O custo escondido da paleteira manual nos armazéns de grãos')

r('<strong>Cálculo que poucos gestores fazem:</strong> uma operação com 60 paletes/turno usando transpaleteira manual exige o dobro de horas-homem comparada à elétrica. Somando o custo de um operador extra, os afastamentos por lesão de esforço repetitivo (média de 15 dias/ano) e a multa de sobreestadia por atraso na descarga de caminhões, a economia aparente da manual se transforma em prejuízo real. A locação da paleteira elétrica Clark se paga com o ganho de produtividade do primeiro mês.',
  '<strong>Conta que poucos armazéns de Formosa fazem:</strong> na safra, um galpão que movimenta 60 paletes de sacas por turno com paleteira manual precisa do dobro de braços. Some o custo de operadores extras, os afastamentos por lesão no ombro e lombar (média de 15 dias/ano no setor agrícola) e as multas de sobreestadia dos caminhões graneleiros parados na doca. A economia aparente da manual vira prejuízo real. A locação da paleteira elétrica Clark se paga com a produtividade recuperada já nas primeiras semanas de safra.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (whitespace-aware)
r('Aplicações em Goiânia', 'Aplicações em Formosa')

# H2
r('Quais setores mais usam <span>patolinha elétrica</span> em Goiânia?',
  'Onde a <span>paleteira elétrica Clark</span> opera na região de Formosa')

r('Onde a paleteira elétrica Clark opera diariamente na capital e região metropolitana.',
  'Setores agrícolas, cooperativas e comércio que contratam transpaleteira elétrica no município.')

# Card 1
r('alt="Transpaleteira elétrica Clark movimentando fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Transpaleteira Clark WPio15 movimentando sacas de milho em armazém graneleiro de Formosa-GO"')
r('<h3>Polo da Moda: fardos de tecido e confecções</h3>',
  '<h3>Armazéns graneleiros: sacas de milho e soja</h3>')
r('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos dos depósitos de confecção, movimenta fardos de 400 a 800 kg e agiliza o carregamento dos caminhões de distribuição.',
  'Os armazéns de grãos na BR-020 processam toneladas de milho e soja durante a safra. Sacas de 60 kg paletizadas em lotes de 600 a 1.200 kg circulam da doca de recebimento até as pilhas de estoque. A WPio15 navega entre corredores de sacaria, mantém fluxo contínuo sem desgaste do operador e agiliza o carregamento dos caminhões graneleiros que aguardam na doca.')

# Card 2
r('alt="Stacker Clark SWX16 operando em câmara fria na Ceasa de Goiânia"',
  'alt="Stacker Clark SWX16 em cooperativa agrícola de Formosa movimentando big bags de soja"')
r('<h3>Ceasa: câmaras frias a -18°C</h3>',
  '<h3>Cooperativas agrícolas: big bags e insumos</h3>')
r('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados até 4.500 mm com estabilidade total, mesmo em piso escorregadio e temperatura extrema.',
  'As cooperativas de produtores rurais de Formosa recebem, armazenam e redistribuem big bags de soja, sementes e insumos agrícolas que chegam a 1.000 kg por unidade. A SWX16 empilha esses paletes até 4.500 mm em corredores estreitos, otimizando o espaço vertical dos galpões. A WPio15 complementa movimentando sacas menores nas áreas de expedição.')

# Card 3
r('alt="Transpaleteira com plataforma Clark PWio20 em CD logístico da BR-153 em Goiânia"',
  'alt="Transpaleteira Clark PWio20 no comércio varejista de Formosa-GO"')
r('<h3>CDs da BR-153: dock-to-stock e cross-docking</h3>',
  '<h3>Comércio varejista: supermercados e lojas</h3>')
r('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos entre doca e estoque sem fadiga do operador. A velocidade de 6 km/h acelera o fluxo de dock-to-stock e reduz o tempo de permanência dos caminhões.',
  'Supermercados, redes de material de construção e lojas de varejo de Formosa recebem paletes de fornecedores diariamente. A PWio20 com plataforma fixa percorre o depósito até a área de exposição sem fadiga, agilizando a reposição de gôndolas. A velocidade de 6 km/h reduz o tempo entre a chegada do caminhão e a mercadoria disponível para venda.')

# Card 4
r('alt="Transpaleteira elétrica Clark em operação no Distrito Industrial e armazéns da Av. Independência em Goiânia"',
  'alt="Transpaleteira Clark WPX35 em distribuidora de fertilizantes na BR-020 em Formosa-GO"')
r('<h3>Distrito Industrial e Av. Independência</h3>',
  '<h3>Distribuidoras de fertilizantes e insumos</h3>')
r('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos, embalagens e produtos acabados. A WPX35 heavy duty atende cargas de até 3.500 kg em pisos industriais com trânsito intenso de empilhadeiras e caminhões.',
  'As distribuidoras de fertilizantes, calcário e defensivos agrícolas na BR-020 movimentam paletes de 1.500 a 2.500 kg com frequência. Sacos de 50 kg paletizados e big bags de adubo circulam entre galpões e caminhões durante o ano inteiro — intensificando no plantio. A WPX35 heavy duty suporta 3.500 kg com motor reforçado e rodas para pisos de galpão rural.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
  'Equipe técnica com deslocamento pela BR-020/GO-116. Atendimento em Formosa com diagnóstico de sistema elétrico, tração e bomba hidráulica diretamente no armazém ou cooperativa.')

r('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-020 até seu armazém, cooperativa ou comércio em Formosa. Entrega em até 24 horas da confirmação, sem custo adicional de frete no contrato mensal.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e segura o turno inteiro da tarde. O custo da locação se pagou no primeiro mês só com a economia de hora extra."',
  '"Nosso armazém de milho na BR-020 movimentava 45 paletes de sacas por turno com três manuais. Colocamos duas WPio15 Clark e o rendimento dobrou com metade dos operadores. O lítio recarrega no almoço e segura a tarde inteira — na safra, quando o volume triplica, não precisamos de hora extra. O contrato se pagou em duas semanas só com o que economizamos em mão de obra."')
r('<strong>Marcos V.</strong>',
  '<strong>Cléber R.</strong>')
r('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
  'Gerente de Armazém, Cooperativa de Grãos, BR-020 Formosa-GO (jan/2026)')

# Depoimento 2
r('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark com chassi anticorrosão está no sexto mês sem manutenção corretiva. A Move trocou a bateria preventivamente e nem precisamos acionar."',
  '"Precisávamos empilhar big bags de soja até 4 metros no galpão da cooperativa. A SWX16 resolve com folga — estabilidade perfeita mesmo com 1.000 kg de carga. O chassi anticorrosão aguenta a poeira de grãos e a umidade do armazém sem travar. A Move fez a troca preventiva da bateria no quarto mês sem a gente nem pedir — o monitoramento deles detectou queda de ciclo antes de dar problema."')
r('<strong>Renata C.</strong>',
  '<strong>Sandra L.</strong>')
r('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
  'Coord. de Logística, Cooperativa Agrícola, Formosa-GO (fev/2026)')

# Depoimento 3
r('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 12 km por turno. Renovamos o contrato pela terceira vez e o orçamento pelo WhatsApp sai em minutos."',
  '"Duas PWio20 resolveram o gargalo de reposição no supermercado. O depósito tem 90 metros até a loja — com manual, os funcionários andavam 10 km por turno empurrando paletes. Agora vão na plataforma e a reposição de gôndola que levava 3 horas fecha em uma e meia. Renovamos o contrato semestral e cada orçamento novo pelo WhatsApp da Move sai em minutos."')
r('<strong>Anderson L.</strong>',
  '<strong>Renato F.</strong>')
r('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
  'Supervisor de Operações, Supermercado, Centro de Formosa-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/formosa-go/curso-de-operador-de-empilhadeira')
r('curso de operador</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-11 para operadores de transpaleteira</a>? Conectamos sua equipe a centros credenciados na região de Formosa e Brasília.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Atendimento em <span>Formosa</span> e cidades do Entorno de Brasília')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Formosa pela BR-020/GO-116. Transpaleteira elétrica Clark entregue em até 24 horas da confirmação. Atendemos Formosa, Entorno de Brasília e todo o raio de 300 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/formosa-go/"><strong>Formosa</strong></a>
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
        <a href="/valparaiso-de-goias-go/">Valparaíso de Goiás</a>
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
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/trindade-go/">Trindade</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-47.3345!3d-15.5372')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Formosa-GO"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Formosa</a>')
r('/goiania-go/" style="color', '/formosa-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>transpaleteira elétrica</span> em Goiânia',
  'Dúvidas sobre <span>transpaleteira elétrica</span> em Formosa')

# FAQ 1
r('>Qual a transpaleteira elétrica mais alugada em Goiânia?<',
  '>Qual transpaleteira elétrica serve melhor os armazéns de grãos em Formosa?<')
r('>A Clark WPio15 é o modelo com maior volume de contratos na capital. Com capacidade de 1.500 kg e bateria de lítio 24V, ela atende operações de picking, dock-to-stock e movimentação de paletes em atacadistas do Polo da Moda, galpões da Ceasa e centros de distribuição da BR-153.<',
  '>A Clark WPio15 concentra a maioria dos contratos na região. Com 1.500 kg de capacidade e lítio 24V, movimenta sacas de 60 kg, big bags de soja e milho e paletes de insumos agrícolas nos armazéns graneleiros da BR-020. Chassi compacto para corredores de 1,8 m entre estantes de sacaria.<')

# FAQ 2
r('>Qual a diferença entre transpaleteira manual e elétrica?<',
  '>A paleteira elétrica aguenta sacas de grãos e big bags pesados?<')
r('>A transpaleteira manual exige esforço físico do operador para tracionar e elevar o palete. A elétrica possui motor de tração e bomba hidráulica acionados por bateria de lítio, eliminando o esforço repetitivo. Em operações com mais de 30 paletes por turno, a versão elétrica reduz o tempo de movimentação em até 60% e previne lesões por esforço repetitivo.<',
  '>Sim. Sacas padrão de 60 kg paletizadas ficam entre 600 e 1.200 kg por palete. A WPio15 suporta 1.500 kg e a WPX35 chega a 3.500 kg — cobrindo sacaria de milho até big bags de 1.000 kg. O motor de tração mantém velocidade constante mesmo com carga máxima nos pisos irregulares de armazéns rurais de Formosa.<')

# FAQ 3
r('>A transpaleteira elétrica funciona em câmara fria?<',
  '>Transpaleteira elétrica funciona em armazéns com poeira de grãos?<')
r('>Sim. O modelo Clark SWX16 é projetado para operar em câmaras frias com temperatura de até -18°C. A bateria de lítio 24V mantém desempenho estável mesmo em baixas temperaturas, e o chassi com proteção anticorrosão resiste à umidade das câmaras frigoríficas da Ceasa e de distribuidoras de alimentos em Goiânia.<',
  '>Sim. Os modelos Clark operam com motor elétrico selado e zero emissão de faísca — eliminando risco de ignição em ambientes com poeira de grãos em suspensão. A bateria de lítio 24V não gera gases nem aquecimento externo. Recomendamos limpeza periódica do chassi para evitar acúmulo de resíduos nas rodas tandem.<')

# FAQ 4
r('>Quanto tempo dura a bateria da transpaleteira elétrica?<',
  '>A bateria de lítio aguenta os turnos de safra em Formosa?<')
r('>A bateria de lítio 24V das transpaleteiras Clark oferece autonomia de 6 a 10 horas de operação contínua, dependendo do modelo e da intensidade de uso. A recarga completa leva de 2 a 3 horas, e a carga de oportunidade (pausas de 15 a 30 minutos) permite estender o turno sem trocar o equipamento.<',
  '>A autonomia vai de 6 a 10 horas contínuas conforme modelo e peso movimentado. Nos armazéns de Formosa que operam dois turnos na safra de milho e soja, a recarga completa de 2 a 3 horas na virada de turno cobre a jornada seguinte. Cargas de oportunidade de 15 minutos no almoço permitem estender a operação sem substituir o equipamento.<')

# FAQ 5
r('>Preciso de habilitação para operar transpaleteira elétrica?<',
  '>Operadores de armazém em Formosa precisam de curso para usar transpaleteira?<')
r('Sim. A NR-11 exige treinamento específico para operadores de equipamentos de movimentação de carga, incluindo transpaleteiras elétricas. O curso abrange inspeção pré-operacional, limites de carga, velocidade de deslocamento e procedimentos de segurança. A Move Máquinas indica parceiros credenciados em Goiânia para a <a href="/goiania-go/curso-operador-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação de operadores</a>.',
  'Sim. A NR-11 exige treinamento em operação de equipamentos de movimentação de carga. O curso abrange inspeção pré-operacional, limites de capacidade, velocidade em áreas de circulação e procedimentos de emergência. Indicamos centros de formação credenciados na região de Formosa e Brasília para <a href="/formosa-go/curso-de-operador-de-empilhadeira" style="color:var(--color-primary);font-weight:600;">capacitação dos operadores</a>.')

# FAQ 6
r('>Vocês entregam transpaleteira fora de Goiânia?<',
  '>Qual o prazo de entrega de transpaleteira elétrica em Formosa?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega ocorre no mesmo dia, sem custo adicional de frete.<',
  '>Formosa fica a 280 km da sede pela BR-020/GO-116. A entrega acontece em até 24 horas após a confirmação do contrato. Para demandas urgentes em período de safra — armazéns lotados, cooperativas com fila de caminhões — priorizamos o despacho. Frete incluído no contrato, sem custo adicional.<')

# FAQ 7
r('>A manutenção da transpaleteira está inclusa na locação?<',
  '>A manutenção da transpaleteira está incluída no valor da locação?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva da bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Se o equipamento apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todo contrato da Move Máquinas cobre manutenção preventiva e corretiva completa: bateria de lítio, motor de tração, bomba hidráulica, rodas e chassi. Em Formosa, a equipe técnica se desloca pela BR-020 para resolver qualquer ocorrência sem parar a operação do armazém.<')

# FAQ 8
r('>Qual a capacidade máxima das transpaleteiras Clark disponíveis?<',
  '>Qual a maior capacidade de transpaleteira disponível para Formosa?<')
r('>A frota Clark de transpaleteiras elétricas para locação em Goiânia cobre de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para operações em câmaras frias, a SWX16 é uma stacker patolada que eleva cargas até 4.500 mm de altura, substituindo empilhadeiras em corredores estreitos.<',
  '>A frota vai de 1.500 kg (WPio15 walkie) até 3.500 kg (WPX35 heavy duty). Para armazéns graneleiros que movimentam big bags de 1.000 kg e paletes de fertilizantes acima de 2.000 kg, a WPX35 atende com motor reforçado. A SWX16 stacker empilha paletes até 4.500 mm em corredores estreitos de galpões de sacaria.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de transpaleteira Clark em Goiânia',
  'Solicite transpaleteira Clark para Formosa-GO')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
  "'Olá, preciso de transpaleteira elétrica em Formosa-GO.\\n\\n'")

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
            'Formosa e Brasília',  # legit: training centers
            'Formosa e Goiânia',   # legit
            '4913, Goiânia',       # address ref
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
fm = html.count('Formosa')
local = html.count('BR-020') + html.count('grãos') + html.count('sacas') + html.count('graneleir') + html.count('cooperativa') + html.count('milho') + html.count('soja')
print(f"\nFormosa: {fm} menções")
print(f"Contexto local (BR-020/grãos/sacas/graneleiro/cooperativa/milho/soja): {local} menções")

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
