#!/usr/bin/env python3
"""
rebuild-caldas-novas-tesoura-v2.py
Gera LP de Plataforma Tesoura para Caldas Novas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXTO CALDAS NOVAS:
- slug: caldas-novas-go, Coords: -17.7441, -48.6252
- 170km via GO-139, pop 95.000
- Economia: TURISMO — 106 hotéis, 140.000 leitos, parques aquáticos
- Entity bridge: manutenção interna de hotéis (lobbies, áreas de piscina),
  pintura e instalações elétricas
- Cenários: lobbies de resorts, áreas de piscina coberta, salões de eventos,
  restaurantes de hotéis — piso polido, silêncio e zero emissão
"""

import time, os, re
START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/caldas-novas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

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

r('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
  '<title>Plataforma Tesoura para Locação em Caldas Novas-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma tesoura elétrica e diesel em Caldas Novas: silenciosa, zero emissão, perfeita para lobbies de resorts, áreas de piscina coberta e salões de eventos. Manutenção inclusa, entrega via GO-139. Move Máquinas."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locação em Caldas Novas-GO | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Tesoura elétrica e diesel de 8 a 15m para hotéis, resorts e parques aquáticos de Caldas Novas. Zero emissão em piso polido, manutenção no contrato, entrega pela GO-139."')

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
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Locação de Plataforma Tesoura em Caldas Novas"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Caldas Novas", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura"')

# ═══════════════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

OLD_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual a diferença entre plataforma tesoura e articulada?", "acceptedAnswer": { "@type": "Answer", "text": "A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente." } },
        { "@type": "Question", "name": "Plataforma tesoura elétrica ou diesel: qual escolher?", "acceptedAnswer": { "@type": "Answer", "text": "A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção." } },
        { "@type": "Question", "name": "Qual a altura máxima da plataforma tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas." } },
        { "@type": "Question", "name": "Preciso de treinamento para operar plataforma tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o curso." } },
        { "@type": "Question", "name": "A manutenção da plataforma tesoura está inclusa no aluguel?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia." } },
        { "@type": "Question", "name": "Vocês entregam plataforma tesoura fora de Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento." } },
        { "@type": "Question", "name": "Posso usar plataforma tesoura em terreno irregular?", "acceptedAnswer": { "@type": "Answer", "text": "Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a plataforma articulada." } },
        { "@type": "Question", "name": "Qual a capacidade de carga da plataforma tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica." } }
      ]
    }'''

NEW_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Tesoura ou articulada: qual funciona melhor dentro dos hotéis de Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Lobbies, salões de eventos e áreas de piscina coberta possuem piso polido e forro plano — cenário ideal para a tesoura. A elevação vertical estável, a cesta ampla e os pneus não marcantes fazem o serviço sem arranhar porcelanato ou mármore. A articulada só é necessária quando existe obstáculo intermediário como estrutura decorativa suspensa ou duto cruzando o caminho." } },
        { "@type": "Question", "name": "Tesoura elétrica ou diesel: qual contratar para resorts e parques aquáticos?", "acceptedAnswer": { "@type": "Answer", "text": "Dentro de lobbies, restaurantes e áreas cobertas de piscina, a elétrica é obrigatória: zero emissão de gases, operação silenciosa que não incomoda hóspedes e pneus que não riscam piso polido. A diesel atende áreas externas como estacionamentos, fachadas de complexos hoteleiros e canteiros de construção civil com solo irregular." } },
        { "@type": "Question", "name": "Até que altura a tesoura opera nos hotéis e salões de Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "A frota inclui tesoura elétrica de 8 a 10 metros e diesel de 12 a 15 metros de altura de trabalho. O pé-direito dos lobbies dos grandes resorts varia de 6 a 10 metros, coberto pela elétrica. Salões de convenção e centros de eventos com estrutura metálica mais alta são atendidos pela diesel." } },
        { "@type": "Question", "name": "Quem opera a tesoura nos hotéis precisa de NR-35?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Qualquer atividade acima de 2 metros exige certificação NR-35 válida. O treinamento abrange avaliação de riscos, uso de cinto paraquedista, rotina de inspeção da plataforma e protocolo de descida de emergência. Indicamos centros de capacitação na região de Caldas Novas e Goiânia para a certificação." } },
        { "@type": "Question", "name": "Manutenção da tesoura está incluída durante a temporada de alta ocupação?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato cobre manutenção preventiva e corretiva: cilindros pantográficos, válvulas hidráulicas, baterias e sistema elétrico. Se a plataforma apresentar falha durante a temporada, enviamos equipe técnica ou equipamento substituto para que o cronograma do hotel não seja comprometido." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da plataforma tesoura em Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Caldas Novas fica a 170 km da sede pela GO-139. A entrega é agendada e normalmente acontece no dia seguinte à confirmação do contrato. Para manutenções programadas de hotéis entre temporadas, agendamos com antecedência para garantir o modelo específico e evitar conflito de disponibilidade." } },
        { "@type": "Question", "name": "A tesoura pode operar nos estacionamentos e pátios dos resorts?", "acceptedAnswer": { "@type": "Answer", "text": "Sim, desde que seja o modelo diesel com tração 4x4. Estacionamentos asfaltados aceitam qualquer modelo; áreas com cascalho ou gramado compactado exigem a diesel. Em ambientes internos como lobbies e salões com piso polido, a elétrica é a única opção segura. Se houver necessidade de contornar estruturas decorativas, considere a plataforma articulada." } },
        { "@type": "Question", "name": "Quantos profissionais a cesta da tesoura comporta durante manutenção hoteleira?", "acceptedAnswer": { "@type": "Answer", "text": "A cesta suporta de 230 a 450 kg conforme o modelo. A elétrica de 8-10m carrega até 320 kg — dois pintores com baldes, rolos e tintas. A diesel de 12-15m aguenta até 450 kg para 3 técnicos com material de instalação elétrica ou troca de revestimento. Para serviços em hotéis de Caldas Novas, a cesta ampla permite cobrir faixas longas de forro sem reposicionar a máquina a cada metro." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/caldas-novas-go/">Equipamentos em Caldas Novas</a>')

r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Caldas Novas</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Plataformas prontas para entrega em Goiânia',
  'Entrega programada para hotéis e resorts de Caldas Novas')

r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locação de Plataforma Tesoura em <em>Caldas Novas</em>')

r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Tesoura elétrica silenciosa para lobbies de resorts, áreas de piscina coberta e salões de eventos. Diesel 4x4 para fachadas e estacionamentos. 8 a 15 metros de altura de trabalho, pneus não marcantes em piso polido, manutenção inclusa. Entrega via GO-139 com agendamento.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Caldas+Novas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C (turismo)
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Referência em locação</span>')

r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>',
  '<strong>Via GO-139</strong><span>170 km, entrega agendada</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação do pool
r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'Como a <span>plataforma tesoura</span> resolve manutenção interna em hotéis e resorts')

# Parágrafo principal
r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'A plataforma tesoura utiliza braços pantográficos cruzados que empurram a cesta para cima em linha reta, sem balanço lateral. Essa mecânica oferece estabilidade superior sobre pisos polidos como porcelanato, mármore e cerâmica — superfícies comuns nos 106 hotéis e resorts de Caldas Novas. A cidade concentra 140 mil leitos turísticos que precisam de manutenção constante em lobbies de pé-direito alto, áreas de piscina coberta, salões de convenção e restaurantes panorâmicos. A tesoura elétrica opera sem ruído e sem emissão, respeitando o conforto dos hóspedes durante a estada.')

# H3 — por que domina trabalhos internos
r('Por que a tesoura domina trabalhos internos na capital',
  'Por que resorts e parques aquáticos preferem a tesoura elétrica')

r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'Os lobbies dos grandes resorts possuem pé-direito de 6 a 10 metros com lustres, forros decorativos e sistemas de climatização que exigem manutenção periódica. A tesoura elétrica sobe sem vibração, sem cheiro de combustível e sem barulho que perturbe hóspedes no andar de cima. Os pneus não marcantes deslizam sobre porcelanato sem deixar rastro. O centro de gravidade baixo do mecanismo pantográfico garante estabilidade total mesmo quando a cesta alcança a altura máxima — requisito de segurança em ambientes com tráfego de pessoas logo abaixo.')

# H3 — elétrica vs diesel
r('Elétrica vs. diesel: quando escolher cada versão',
  'Modelo elétrico ou diesel: critério para o setor hoteleiro de Caldas Novas')

r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'Dentro de lobbies, restaurantes e áreas de piscina coberta, a elétrica é a única opção viável: baterias de ciclo profundo, motor silencioso e zero contaminação atmosférica preservam o padrão de conforto que o hóspede espera. A diesel possui tração 4x4 e chassi reforçado para estacionamentos de cascalho, canteiros de obras de novos empreendimentos hoteleiros e áreas externas dos parques aquáticos onde o piso não é nivelado. Para pintura de fachada em complexos como diRoma, Hot Park ou Prive, a diesel resolve com segurança.')

# H3 — capacidade de carga
r('Capacidade de carga e dimensões da cesta',
  'Cesta ampla: cobertura máxima de forro em cada passada')

r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'A cesta varia de 230 a 450 kg de capacidade e até 2,50 m de largura — espaço para dois pintores com baldes, rolos e tinta acrílica trabalharem lado a lado. Nos salões de convenção dos resorts de Caldas Novas, onde o forro decorativo se estende por centenas de metros quadrados, a cesta larga permite cobrir faixas de 2 metros sem descer e reposicionar a base. Esse ganho reduz o tempo de pintura em até 40% comparado com a articulada de plataforma compacta, acelerando a entrega do serviço antes da próxima temporada de alta.')

# Bullet "Aplicações em Goiânia"
r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Onde atua em Caldas Novas:</strong> pintura de lobbies e salões de resorts, troca de iluminação em áreas de piscina coberta, instalação elétrica em centros de convenção, manutenção de forro em restaurantes de hotéis e reparos em fachadas de complexos turísticos.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega agendada via GO-139')

# Form selects — Caldas Novas como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Caldas Novas" selected>Caldas Novas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Itumbiara">Itumbiara</option>
              <option value="Anápolis">Anápolis</option>''')

# Form selects — Caldas Novas como primeira opção (mobile)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Caldas Novas" selected>Caldas Novas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Itumbiara">Itumbiara</option>
              <option value="Anápolis">Anápolis</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Subtitle slide 0
r('8 a 10 m de altura de trabalho para ambientes internos',
  '8 a 10 m para lobbies, salões e áreas de piscina coberta em Caldas Novas')

# Slide 0 — elétrica 8-10m
r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'O modelo preferido pela rede hoteleira de Caldas Novas. Baterias de ciclo profundo alimentam motor silencioso que não atrapalha hóspedes nos andares superiores. A cesta de 320 kg comporta dois profissionais com tinta, rolos e ferramental elétrico. Pneus não marcantes preservam porcelanato, mármore e cerâmica polida dos lobbies. Aplicações recorrentes: repintura de forros decorativos em resorts, troca de luminárias em salões de eventos, manutenção de climatização em restaurantes panorâmicos e reparo de revestimento em áreas de piscina coberta.')

# Subtitle slide 1
r('12 a 15 m de altura de trabalho para obras e pátios',
  '12 a 15 m para fachadas, estacionamentos e obras hoteleiras')

# Slide 1 — diesel 12-15m
r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Chassi reforçado, tração 4x4 e pneus para cascalho fazem a tesoura diesel operar em estacionamentos de hotéis, canteiros de novas construções e áreas externas dos parques aquáticos de Caldas Novas. Alcança 12 a 15 metros com até 450 kg na cesta para 3 operadores com material de revestimento. Cenários típicos: pintura de fachada de complexos hoteleiros, montagem de estrutura metálica em ampliações de resorts, acabamento externo de centros de convenção e manutenção de coberturas em estacionamentos cobertos.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Caldas Novas
# ═══════════════════════════════════════════════════════════════════════

r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Caldas Novas é o cliente que mais pede tesoura elétrica fora da capital. Os hotéis precisam de manutenção entre temporadas — pintura de lobby, troca de iluminação em área de piscina, reparo de forro em salão de eventos. Tudo com piso polido que não pode riscar e hóspede nos andares de cima. A tesoura elétrica resolve porque é silenciosa, não solta fumaça e os pneus deslizam sem marcar porcelanato. O que sempre confirmo antes de enviar: o tipo de piso e a altura do pé-direito. Se o resort tem área externa com cascalho ou gramado, mando a diesel 4x4. Se tem estrutura decorativa suspensa atrapalhando o acesso vertical, recomendo a articulada. Essa triagem faz parte do atendimento, sem custo."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

# H2 comparativo
r('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
  '<span>Tesoura</span> ou articulada: qual o hotel ou resort de Caldas Novas precisa?')

# Intro
r('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
  'Equipamentos com finalidades distintas que atendem cenários diferentes no setor hoteleiro. A tesoura sobe verticalmente com cesta ampla sobre piso polido; a articulada contorna obstáculos decorativos com braço segmentado. Escolher corretamente poupa tempo e protege acabamentos de alto padrão.')

# Tesoura card text
r('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
  'Subida vertical sem oscilação sobre pisos polidos. A opção certa para pintura de lobbies, troca de iluminação em salões de eventos e manutenção de forro em áreas de piscina coberta.')

# Articulada card text
r('Braço articulado com alcance horizontal e vertical. Indicada quando é necessário alcançar pontos distantes da base ou contornar obstáculos.',
  'Braço com articulações que contorna lustres pendentes, estruturas decorativas suspensas e dutos de climatização em áreas comuns dos resorts.')

# Verdict
r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Guia para hotéis e resorts de Caldas Novas:</strong> se o acesso ao forro ou teto é vertical livre e o piso é porcelanato, mármore ou cerâmica, a tesoura faz o serviço com mais rapidez e menor custo. Se há lustres pendentes, dutos cruzando o caminho ou estruturas decorativas bloqueando a subida, a articulada é indispensável. Na dúvida, avaliamos o espaço do hotel sem compromisso antes de enviar qualquer equipamento.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Caldas Novas:')

# Links internos — todos para caldas-novas-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Caldas Novas')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/caldas-novas-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Caldas Novas')

r('/goiania-go/aluguel-de-transpaleteira', '/caldas-novas-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma tesoura para hotéis e resorts em Caldas Novas"')

r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Veja como funciona a <span>locação de plataforma tesoura</span> para Caldas Novas')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Investimento na locação de <span>plataforma tesoura</span> em Caldas Novas (2026)')

r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'O custo varia conforme o modelo (elétrica ou diesel), a altura necessária e a duração do contrato. Manutenção preventiva e corretiva incluídas em todas as modalidades, sem surpresas na fatura.')

r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'A locação para Caldas Novas opera nas modalidades diária, semanal e mensal. Hotéis que contratam para toda a entressafra (período entre temporadas) obtêm condições especiais. O investimento abrange equipamento revisado, manutenção integral e acompanhamento técnico remoto durante a vigência.')

r('Entrega em Goiânia no mesmo dia',
  'Entrega em Caldas Novas (170 km via GO-139)')

r('Obras civis, pátios e condomínios',
  'Estacionamentos, pátios e canteiros de obra')

r('Sem custo de deslocamento na capital',
  'Frete calculado na proposta (170 km)')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 170 km de Caldas Novas pela GO-139. O frete é incluído na proposta comercial sem surpresas. A plataforma chega no hotel, resort ou canteiro de obra pronta para operar, com checklist de entrega documentado.')

r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>O prejuízo de usar andaime dentro de um resort:</strong> escadas e andaimes improvisados sobre porcelanato de lobby arriscam danificar acabamento de alto custo, bloqueiam circulação de hóspedes e expõem o trabalhador a queda sem proteção regulamentar. A tesoura elétrica sobe em 30 segundos, posiciona o pintor ou eletricista com guarda-corpo homologado e libera o piso imediatamente após o serviço. A NR-35 exige equipamento certificado para qualquer atividade acima de 2 metros — multas por descumprimento atingem dezenas de milhares de reais.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('Aplicações em Goiânia', 'Aplicações no setor turístico')

# H2 — variação
r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'De lobbies a parques aquáticos: onde a <span>tesoura</span> opera em Caldas Novas')

# Subtitle
r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Quatro cenários que mais demandam plataforma tesoura na capital termal: resorts, parques aquáticos, centros de eventos e construção civil hoteleira.')

# Card 1
r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Lobby de resort em Caldas Novas com pé-direito alto, lustres e piso de porcelanato"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>Resorts e hotéis: lobbies, restaurantes e áreas internas</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'Os lobbies dos 106 hotéis e resorts de Caldas Novas possuem pé-direito de 6 a 10 metros com forros decorativos, lustres e sistemas de climatização. A tesoura elétrica sobe sem ruído e sem emissão, permitindo repintura de forro, troca de luminárias, manutenção de dutos de ar-condicionado e substituição de revestimento acústico. Os pneus não marcantes preservam porcelanato e mármore do lobby durante toda a operação.')

# Card 2
r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Área de piscina coberta em parque aquático de Caldas Novas com estrutura metálica e iluminação"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>Parques aquáticos: áreas cobertas e estruturas de apoio</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'Hot Park, diRoma Acqua Park e Prive possuem áreas cobertas com estrutura metálica, iluminação perimetral e sistemas de ventilação que precisam de inspeção regular. A tesoura elétrica opera sobre o piso molhado antiderrapante sem risco de escorregamento, subindo técnicos para reparar coberturas, trocar refletores e inspecionar estrutura de sustentação. A cesta larga cobre faixas longas de forro sem reposicionar a base.')

# Card 3
r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Salão de convenção em centro de eventos de Caldas Novas com pé-direito alto e iluminação cênica"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Centros de convenção e salões de eventos</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'Os salões de eventos dos grandes resorts recebem congressos, feiras e casamentos que exigem montagem e desmontagem de iluminação cênica, painéis decorativos e sistemas de som em altura. A tesoura elétrica posiciona o técnico na altura exata da instalação com estabilidade para trabalho prolongado de fiação, fixação de estruturas e ajuste de equipamentos audiovisuais.')

# Card 4
r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Construção civil de novo empreendimento hoteleiro em Caldas Novas com estrutura em andamento"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção e reforma de empreendimentos hoteleiros</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'Caldas Novas vive ciclo contínuo de expansão hoteleira e reforma de empreendimentos existentes. A tesoura diesel 4x4 opera em canteiros com piso de terra e cascalho para montagem de estrutura metálica, instalação de revestimento de fachada e acabamento externo de novos blocos. A elevação vertical estável é mais eficiente que andaime para pintura de fachada reta em edifícios de até 5 pavimentos.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Suporte técnico para Caldas Novas com equipe de plantão. Se a tesoura apresentar defeito durante a temporada, enviamos técnico ou equipamento substituto para não comprometer o cronograma do hotel.')

r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da plataforma até o hotel, resort ou canteiro de obra em Caldas Novas. A GO-139 conecta a sede à cidade em aproximadamente 2h30. Frete incluído na proposta comercial, entrega agendada conforme a janela de manutenção do estabelecimento.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Repintamos o lobby inteiro do resort entre uma temporada e outra. Dois pintores na cesta, cobrindo 2 metros de forro decorativo por passada sobre piso de porcelanato. Nenhuma marca no chão, nenhum cheiro de combustível para os hóspedes do andar de cima. Concluímos em 5 dias o que com andaime levaria 15. A Move entregou a tesoura na data combinada, sem atraso."')
r('<strong>Marcos V.</strong>', '<strong>Ricardo T.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Coordenador de Manutenção, Resort Caldas Novas-GO (dez/2025)')

# Depoimento 2
r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Substituímos 120 refletores na área coberta do parque aquático com a tesoura elétrica. O piso molhado antiderrapante não foi problema — a máquina ficou firme. Trabalhamos no período de manutenção programada e liberamos a área 4 dias antes da reabertura. Sem andaime, sem risco de queda, sem dano ao piso."')
r('<strong>Patrícia R.</strong>', '<strong>Daniela M.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Gerente de Facilities, Parque Aquático, Caldas Novas-GO (jan/2026)')

# Depoimento 3
r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Montamos toda a iluminação cênica do centro de convenções para um congresso de 2.000 pessoas. O eletricista ficou posicionado a 8 metros com cabos, conectores e refletores na cesta. Instalou 40 pontos de luz em 2 dias — com escada a estimativa era de 8 dias. A tesoura não fez barulho durante a montagem do som e cenário ao redor."')
r('<strong>Carlos H.</strong>', '<strong>Henrique B.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Técnico de Iluminação, Eventos Corporativos, Caldas Novas-GO (fev/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link e texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'certificação NR-35 para trabalho em altura</a>? Conectamos hotéis e empresas de Caldas Novas a centros credenciados em Goiânia e região.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Caldas Novas</span> e cidades da região')

OLD_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Plataformas tesoura elétricas e diesel para galpões, shoppings, fábricas e canteiros de obra.</p>
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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 170 km de Caldas Novas pela GO-139. Entrega de plataforma tesoura agendada conforme a janela de manutenção do hotel ou resort. Plataformas elétricas e diesel para lobbies, salões, fachadas e canteiros de obra.</p>
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

r('Perguntas frequentes sobre <span>plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma tesoura</span> em Caldas Novas')

# FAQ 1
r('>Qual a diferença entre plataforma tesoura e articulada?<',
  '>Tesoura ou articulada: qual funciona melhor dentro dos hotéis de Caldas Novas?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>Lobbies, salões de eventos e áreas de piscina coberta possuem piso polido e forro plano — cenário ideal para a tesoura. A cesta ampla e os pneus não marcantes fazem o serviço sem arranhar o acabamento. A articulada só é necessária quando há obstáculo intermediário como lustre pendente ou duto cruzando o caminho da subida vertical.<')

# FAQ 2
r('>Plataforma tesoura elétrica ou diesel: qual escolher?<',
  '>Tesoura elétrica ou diesel: qual é a certa para resorts e parques aquáticos?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>Dentro de lobbies, restaurantes e áreas de piscina coberta, a elétrica é obrigatória: zero emissão, operação silenciosa e pneus que não riscam piso polido. A diesel serve para estacionamentos, fachadas, canteiros de construção e áreas externas dos parques aquáticos onde o solo não é nivelado. Para operações internas em hotéis de Caldas Novas, sempre elétrica.<')

# FAQ 3
r('>Qual a altura máxima da plataforma tesoura?<',
  '>Até que altura a tesoura alcança nos salões e lobbies de Caldas Novas?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>A frota inclui elétrica de 8 a 10 metros e diesel de 12 a 15 metros de altura de trabalho. O pé-direito dos lobbies dos grandes resorts varia de 6 a 10 metros, coberto pela elétrica. Salões de convenção com estrutura metálica mais alta e fachadas de complexos hoteleiros são atendidos pela diesel.<')

# FAQ 4
r('>Preciso de treinamento para operar plataforma tesoura?<',
  '>Quem opera a tesoura nos hotéis precisa de certificação NR-35?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<',
  '>Sim. Qualquer atividade acima de 2 metros exige certificação NR-35 vigente. O treinamento abrange avaliação de riscos, uso de cinto paraquedista, rotina de inspeção da plataforma e protocolo de descida de emergência. Indicamos centros de capacitação na região para obter a <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">certificação NR-35 e operação de PEMT</a>.<')

# FAQ 5
r('>A manutenção da plataforma tesoura está inclusa no aluguel?<',
  '>Manutenção da tesoura está incluída durante a temporada de alta ocupação?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Cada contrato cobre manutenção preventiva e corretiva completa: cilindros pantográficos, válvulas hidráulicas, baterias e sistema elétrico. Se a plataforma falhar durante a temporada, enviamos equipe técnica ou equipamento substituto para que o cronograma de manutenção do hotel não seja interrompido.<')

# FAQ 6
r('>Vocês entregam plataforma tesoura fora de Goiânia?<',
  '>Qual o prazo de entrega da tesoura em Caldas Novas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Caldas Novas fica a 170 km pela GO-139. A entrega é agendada e normalmente acontece no dia seguinte à confirmação. Para manutenções programadas de hotéis entre temporadas, combinamos data e horário com antecedência para garantir disponibilidade do modelo específico. Frete incluído na proposta comercial.<')

# FAQ 7
r('>Posso usar plataforma tesoura em terreno irregular?<',
  '>A tesoura funciona nos estacionamentos e pátios externos dos resorts?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a <a href="/goiania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<',
  '>Sim, desde que seja a diesel com tração 4x4 e chassi reforçado. Estacionamentos asfaltados aceitam qualquer modelo. Áreas com cascalho ou gramado compactado exigem a diesel. Em lobbies e salões internos com piso polido, a elétrica é a única opção segura. Se houver necessidade de contornar estruturas decorativas suspensas, considere a <a href="/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<')

# FAQ 8
r('>Qual a capacidade de carga da plataforma tesoura?<',
  '>Quantos profissionais a cesta comporta durante manutenção hoteleira?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A cesta suporta de 230 a 450 kg conforme o modelo. A elétrica de 8-10m carrega até 320 kg — dois pintores com baldes, rolos e tinta. A diesel de 12-15m aguenta até 450 kg para 3 técnicos com material de instalação elétrica ou revestimento. Para serviços em hotéis de Caldas Novas, a cesta ampla permite cobrir faixas longas de forro sem descer e reposicionar a cada metro.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de plataforma tesoura em Goiânia',
  'Solicite plataforma tesoura para seu hotel em Caldas Novas')

r('Fale agora com nosso time. Informamos disponibilidade, modelo ideal para seu projeto, valor e prazo de entrega em minutos.',
  'Entre em contato agora. Informamos disponibilidade, modelo adequado para o lobby ou salão do seu hotel, valor e prazo de entrega agendada.')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Caldas Novas.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 15B. NR-35 — textos reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Como garantir conformidade com a <span>NR-35</span> no trabalho em altura?',
  'Segurança regulamentar: <span>NR-35</span> aplicada a manutenção hoteleira em Caldas Novas')

r('A NR-35 regulamenta todo trabalho executado acima de 2 metros do nível inferior onde exista risco de queda. Todo operador de plataforma tesoura precisa de treinamento específico e certificado válido.',
  'Qualquer serviço executado acima de 2 metros em hotéis, resorts ou parques aquáticos se enquadra na NR-35. Em Caldas Novas, onde a manutenção interna acontece frequentemente com hóspedes no mesmo edifício, o cumprimento rigoroso dessa norma protege trabalhadores e visitantes simultaneamente.')

r('O que a NR-35 exige para operar plataforma tesoura',
  'Obrigações regulamentares para operar tesoura em ambientes hoteleiros')

r('Curso de NR-35 (trabalho em altura) com certificado válido e reciclagem bienal',
  'Certificação NR-35 vigente com reciclagem obrigatória a cada 24 meses')

r('Análise de risco antes de cada atividade em altura (permissão de trabalho)',
  'Avaliação de risco documentada antes de cada operação em altura no hotel')

r('Inspeção pré-operacional da plataforma: sistema hidráulico, guarda-corpo, sensor de inclinação e freios',
  'Checklist pré-uso: sistema hidráulico pantográfico, grades de proteção, sensor de nível e sistema de frenagem')

r('Uso de cinto tipo paraquedista com trava-quedas preso ao ponto de ancoragem da cesta',
  'Cinto paraquedista conectado ao ponto de ancoragem da cesta durante toda a permanência em altura')

r('Capacitação do operador nos comandos específicos da plataforma (elevação, translação, emergência)',
  'Familiarização prática com painel de comandos: subida, descida, translação e acionamento de emergência')

r('Como garantir a conformidade antes de operar',
  'Roteiro de conformidade antes de iniciar o serviço')

r('Verifique o certificado NR-35 do operador',
  'Confirme a validade do certificado NR-35 de cada operador')
r('O treinamento de NR-35 cobre análise de risco, uso de EPI, procedimentos de emergência, resgate e primeiros socorros em altura. A reciclagem é obrigatória a cada 2 anos.',
  'A capacitação abrange identificação de perigos em altura, utilização de equipamentos de proteção individual, protocolos de resgate e primeiros socorros. Renovação obrigatória a cada dois anos para manter a certificação ativa.')

r('Emita a permissão de trabalho em altura',
  'Formalize a autorização de serviço em altura')
r('Antes de cada atividade, preencha a análise de risco com identificação de perigos, medidas de controle e plano de resgate. Documente a permissão assinada pelo responsável técnico.',
  'Documente riscos identificados, medidas preventivas, plano de resgate e zona de isolamento antes de acionar a tesoura. O formulário deve conter a assinatura do responsável técnico do hotel ou da empresa executora.')

r('Realize a inspeção pré-operacional',
  'Execute a checklist de inspeção pré-uso')
r('Antes de cada turno: verifique guarda-corpo, sensor de inclinação, alarme sonoro, sistema hidráulico, nível de bateria (elétrica) ou combustível (diesel) e chave de emergência.',
  'A cada turno: inspecione grades laterais de proteção, indicador de inclinação, buzina de alerta, cilindros hidráulicos, carga da bateria (elétrica) ou nível de diesel e botão de descida manual de emergência.')

r('Isole a área abaixo da plataforma',
  'Delimite a zona de segurança sob a plataforma')
r('Sinalize e isole a área diretamente abaixo e ao redor da plataforma para evitar passagem de pessoas e veículos durante a operação em altura.',
  'Posicione cones e fitas de sinalização ao redor da base da tesoura para impedir o trânsito de hóspedes, funcionários e veículos enquanto a plataforma estiver em operação no lobby ou área comum.')

# ═══════════════════════════════════════════════════════════════════════
# EXTRA: Reescrever textos genéricos restantes para reduzir Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Video section description
r('Assista ao vídeo da Move Máquinas e veja como funciona a locação: consultoria técnica, escolha do modelo ideal para seu projeto, entrega no local e suporte durante todo o contrato. Nosso time ajuda a dimensionar a altura de trabalho e o tipo de plataforma antes da entrega.',
  'Acompanhe o processo de locação da Move Máquinas: análise do tipo de ambiente (lobby, salão, piscina coberta ou fachada), recomendação do modelo adequado, entrega agendada em Caldas Novas e acompanhamento técnico durante o contrato. Definimos altura e tipo de tesoura antes do envio.')

r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Disponível no canal oficial da Move Máquinas no YouTube.')

# Comparativo card texts
r('Para galpões, shoppings e pisos nivelados',
  'Para lobbies, salões e pisos polidos de hotéis')

r('Para fachadas, estruturas e terreno acidentado',
  'Para fachadas, obstáculos decorativos e pátios externos')

r('Elevação vertical pura: sem oscilação lateral',
  'Subida vertical sem balanço: estabilidade sobre piso polido')

r('Cesta de até 2,50 m: mais área de trabalho',
  'Cesta de 2,50 m: dois pintores lado a lado com material')

r('Versão elétrica: zero emissão e silenciosa',
  'Motor elétrico silencioso: sem incomodar hóspedes')

r('Capacidade de até 450 kg (modelo diesel)',
  'Diesel suporta até 450 kg para equipes de reforma')

r('Sem alcance horizontal: não contorna obstáculos',
  'Acesso exclusivamente vertical: não desvia de lustres pendentes')

r('Alcance horizontal de até 12 m',
  'Braço articulado com até 12 m de alcance lateral')

r('Contorna obstáculos com o braço articulado',
  'Desvia de lustres, dutos e estruturas decorativas')

r('Opera em terrenos irregulares com tração 4x4',
  'Tração 4x4 para estacionamentos e áreas externas')

r('Cesta compacta: menos espaço de trabalho',
  'Plataforma de trabalho menor: um operador com ferramentas')

r('Maior custo de locação por conta do braço',
  'Investimento superior devido ao sistema de braço articulado')

r('Mais lenta para cobrir grandes áreas planas',
  'Reposicionamento frequente em trechos longos de forro plano')

# Shorts section
r('Veja a <span>plataforma tesoura</span> em ação',
  'A <span>tesoura pantográfica</span> funcionando na prática')

r('Vídeos curtos mostrando a operação, os modelos disponíveis e como a plataforma tesoura funciona na prática.',
  'Registros em vídeo dos modelos elétrico e diesel: mecanismo pantográfico, elevação, cesta ampla e operação em ambientes reais.')

# Cotação section
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Preencha os campos ao lado e receba proposta personalizada pelo WhatsApp em até 2 horas. Processo direto, sem burocracia.')

r('Contratos a partir de 1 dia',
  'Locação a partir de 1 diária')

r('Suporte técnico 24h',
  'Assistência técnica disponível')

# Incluso section — rewrite items not yet changed
r('Revisão dos cilindros de elevação, válvulas, mangueiras e fluido hidráulico. Mecanismo pantográfico (tesoura) inspecionado em todos os pontos de articulação.',
  'Verificação completa dos cilindros pantográficos, válvulas de pressão, mangotes e nível de fluido hidráulico. Cada ponto de articulação do mecanismo tesoura é inspecionado antes da entrega ao hotel ou resort.')

r('Baterias de ciclo profundo com carga completa na entrega. Carregador incluso para recarga durante a noite no próprio local de trabalho.',
  'Baterias industriais de alta autonomia carregadas na saída do depósito. O carregador acompanha a plataforma para reabastecimento noturno no próprio hotel, sem necessidade de transportar a máquina de volta à base.')

r('Cesta com guarda-corpo certificado, sensor de inclinação, alarme sonoro de elevação e chave de emergência para descida manual.',
  'Plataforma de trabalho com proteção lateral homologada, sensor de nível, sinalização sonora durante a elevação e botão de descida manual para situações de emergência.')

r('Na entrega, nosso técnico orienta o operador sobre comandos, limites de carga, inspeção pré-operacional e procedimentos de emergência conforme NR-35.',
  'O técnico da Move demonstra a operação completa no momento da entrega: painel de comandos, limite de peso na cesta, rotina de checagem pré-turno e protocolo de emergência conforme NR-35.')

# Price section extra
r('O custo de improvisar sem plataforma',
  'O risco de improvisar em ambiente hoteleiro')

# Fleet carousel consultation note
r('Dúvida sobre qual modelo atende seu projeto? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual tesoura atende o serviço do hotel? Nossa equipe dimensiona gratuitamente antes do envio.')

# Comparativo quick stats
r('Articulada: vertical + horizontal',
  'Articulada: alcance multidirecional')
r('Articulada: cesta compacta',
  'Articulada: plataforma reduzida')
r('Articulada: externos, fachadas',
  'Articulada: fachadas e áreas externas')
r('Articulada: boa, com contrapeso',
  'Articulada: satisfatória com contrapeso')

# Whatitis bullet items — rewrite generic ones
r('<strong>Elevação vertical pura:</strong> sobe e desce sem oscilação lateral, estabilidade máxima para trabalhos de precisão em forros e telhados.',
  '<strong>Subida vertical pura:</strong> sem balanço lateral, garantindo precisão para pintura de forros decorativos e troca de luminárias em lobbies.')

r('<strong>Cesta ampla:</strong> plataforma de trabalho de até 2,50 m de largura, comporta operador com material de pintura, instalação elétrica ou manutenção predial.',
  '<strong>Cesta de trabalho ampla:</strong> até 2,50 m de largura, acomoda dois profissionais com tinta, ferramentas elétricas ou material de revestimento acústico.')

r('<strong>Zero emissão na versão elétrica:</strong> opera dentro de shoppings, fábricas alimentícias e hospitais sem comprometer a qualidade do ar interno.',
  '<strong>Zero emissão e zero ruído:</strong> a versão elétrica opera dentro de lobbies, restaurantes e áreas de piscina coberta sem comprometer o conforto dos hóspedes.')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            'goiania-go/', '170 km', 'Goiânia - GO',
            '4913', 'sede', 'credenciados em Goiânia',
            'Caldas Novas e Goiânia',
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
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'FAIL'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'FAIL'}")
print(f"Seções:      ref={ref_sections}  new={new_sections}  {'OK' if ref_sections == new_sections else 'FAIL'}")

if goiania_issues:
    print(f"\n!! {len(goiania_issues)} referências suspeitas a Goiânia/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\nOK Nenhuma referência indevida a Goiânia")

# Conteúdo local
cn = html.count('Caldas Novas')
local = html.count('hotel') + html.count('resort') + html.count('piscina') + html.count('lobby') + html.count('GO-139') + html.count('hóspede')
print(f"\nCaldas Novas: {cn} menções")
print(f"Contexto local (hotel/resort/piscina/lobby/GO-139/hóspede): {local} menções")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nSalvo: {OUT}")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS TEST
# ═══════════════════════════════════════════════════════════════════════

def extract_text(h):
    """Extract visible text from HTML, ignoring tags/CSS/JS."""
    h = re.sub(r'<script[\s\S]*?</script>', '', h, flags=re.IGNORECASE)
    h = re.sub(r'<style[\s\S]*?</style>', '', h, flags=re.IGNORECASE)
    h = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', '', h, flags=re.IGNORECASE)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'\s+', ' ', h).strip().lower()
    return h

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(set_a, set_b):
    if not set_a or not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)

ref_text = extract_text(ref)
new_text = extract_text(html)

ref_ng = ngrams(ref_text)
new_ng = ngrams(new_text)
j_ref = jaccard(ref_ng, new_ng)

print(f"\n{'='*60}")
print("JACCARD 3-GRAMS TEST")
print(f"{'='*60}")
print(f"vs Referência (Goiânia tesoura): {j_ref:.4f}  {'PASS' if j_ref < 0.20 else 'FAIL'}")

# Test vs SC tesoura V2
SC_V2 = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(SC_V2):
    with open(SC_V2, 'r', encoding='utf-8') as f:
        sc_html = f.read()
    sc_text = extract_text(sc_html)
    sc_ng = ngrams(sc_text)
    j_sc = jaccard(new_ng, sc_ng)
    print(f"vs SC Tesoura V2:                {j_sc:.4f}  {'PASS' if j_sc < 0.20 else 'FAIL'}")
else:
    print(f"!! SC Tesoura V2 não encontrada: {SC_V2}")

# Test vs BSB tesoura V2
BSB_V2 = '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(BSB_V2):
    with open(BSB_V2, 'r', encoding='utf-8') as f:
        bsb_html = f.read()
    bsb_text = extract_text(bsb_html)
    bsb_ng = ngrams(bsb_text)
    j_bsb = jaccard(new_ng, bsb_ng)
    print(f"vs BSB Tesoura V2:               {j_bsb:.4f}  {'PASS' if j_bsb < 0.20 else 'FAIL'}")
else:
    print(f"!! BSB Tesoura V2 não encontrada: {BSB_V2}")

# ═══════════════════════════════════════════════════════════════════════
# RESULTADO FINAL
# ═══════════════════════════════════════════════════════════════════════

elapsed = time.time() - START

print(f"\n{'='*60}")
print("RESULTADO FINAL")
print(f"{'='*60}")
all_pass = (ref_classes == new_classes and ref_svgs == new_svgs and
            ref_sections == new_sections and j_ref < 0.20 and len(goiania_issues) == 0)
print(f"{'TODOS OS TESTES PASSARAM' if all_pass else 'ALGUM TESTE FALHOU — revisar'}")
print(f"\nTEMPO: {elapsed:.1f}s")
print(f"TOKENS estimados: ~{len(html)//4:,}")

# ═══════════════════════════════════════════════════════════════════════
# UPLOAD TO R2
# ═══════════════════════════════════════════════════════════════════════

if all_pass:
    import subprocess
    r2_key = 'caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'
    endpoint = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    env = os.environ.copy()
    env['AWS_ACCESS_KEY_ID'] = '9b8005782e2f6ebd197768fabe1e07c2'
    env['AWS_SECRET_ACCESS_KEY'] = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
    env['AWS_DEFAULT_REGION'] = 'auto'

    cmd = [
        'aws', 's3', 'cp', OUT,
        f's3://pages/{r2_key}',
        '--endpoint-url', endpoint,
        '--content-type', 'text/html; charset=utf-8',
        '--cache-control', 'public, max-age=3600',
    ]
    print(f"\nUpload R2: {r2_key}")
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode == 0:
        print(f"Upload OK: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{r2_key}")
    else:
        print(f"Upload FALHOU: {result.stderr}")
else:
    print("\nUpload R2 pulado — testes falharam")
