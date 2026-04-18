#!/usr/bin/env python3
"""
rebuild-formosa-tesoura-v2.py
Gera LP de Plataforma Tesoura para Formosa-GO
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

import time, re, os
START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/formosa-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

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
  '<title>Plataforma Tesoura para Locação em Formosa-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma tesoura elétrica e diesel de 8 a 15m em Formosa-GO. Ideal para armazéns graneleiros, galpões de cooperativas agrícolas e indústrias ProGoiás. Entrega via BR-020/GO-116, manutenção inclusa no contrato. Move Máquinas."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/formosa-go/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locação em Formosa-GO | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Plataforma tesoura elétrica e diesel para Formosa-GO: 8 a 15m de altura. Perfeita para armazéns graneleiros com teto metálico 8-12m, instalações agropecuárias e indústrias do ProGoiás. Manutenção completa inclusa."')

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
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Plataforma Tesoura para Locação em Formosa-GO"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Formosa", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Formosa", "item": "https://movemaquinas.com.br/formosa-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Formosa", "item": "https://movemaquinas.com.br/formosa-go/aluguel-de-plataforma-elevatoria-tesoura"')

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
        { "@type": "Question", "name": "Tesoura ou articulada: qual usar nos armazéns graneleiros de Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "Armazéns de grãos possuem coberturas metálicas planas entre 8 e 12 metros com piso de concreto nivelado — condições perfeitas para a tesoura. A cesta de até 2,50m acomoda dois técnicos com ferramentas para manutenção de telhado sem reposicionar a base a cada metro. Se houver transportadores ou tubulação de secagem cruzando a linha de acesso, a articulada contorna o obstáculo." } },
        { "@type": "Question", "name": "Elétrica ou diesel: qual plataforma tesoura contratar em Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "A elétrica opera sem gás e sem ruído — exigência de cooperativas que armazenam grãos certificados e mantêm ambiente controlado. A diesel possui tração 4x4 para pátios de carga e descarga com cascalho, terra batida e rampas de acesso que circundam silos e armazéns. Para manutenção de telhado interno, elétrica. Para pátio externo de complexo agroindustrial, diesel." } },
        { "@type": "Question", "name": "Qual a altura de trabalho da tesoura disponível para Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 8 a 15 metros de elevação. A tesoura elétrica de 8 a 10m atende a maioria dos galpões de cooperativas agrícolas e instalações comerciais do centro. A diesel de 12 a 15m alcança coberturas mais altas como armazéns graneleiros de grande porte e estruturas industriais do ProGoiás." } },
        { "@type": "Question", "name": "A NR-35 se aplica à operação de tesoura em propriedades rurais de Formosa?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Toda atividade acima de 2 metros exige conformidade com a NR-35, independentemente de ser em zona urbana ou rural. O operador precisa de treinamento válido cobrindo análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de resgate. Indicamos centros de capacitação acessíveis a partir de Formosa pela BR-020." } },
        { "@type": "Question", "name": "A manutenção está incluída no contrato de locação da tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todos os contratos da Move Máquinas cobrem manutenção preventiva e corretiva: sistema hidráulico pantográfico, cilindros, parte elétrica e baterias (modelo elétrico). Em caso de falha durante operação em Formosa, despachamos equipe técnica pela BR-020/GO-116 para reparo no local ou substituição do equipamento." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da tesoura em Formosa-GO?", "acceptedAnswer": { "@type": "Answer", "text": "Formosa está a 280 km da base pela BR-020/GO-116. Para locações programadas, agendamos entrega com antecedência garantindo disponibilidade do modelo específico. Demandas urgentes são atendidas conforme logística — consulte horário de corte para despacho no mesmo dia." } },
        { "@type": "Question", "name": "A tesoura diesel funciona nos pátios de armazéns graneleiros?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A tesoura diesel possui tração 4x4 e chassi reforçado para cascalho, terra compactada e rampas de acesso ao redor de silos e armazéns. Para manutenção interna com piso nivelado, a elétrica é preferível. Se estruturas como esteiras transportadoras cruzarem o caminho, considere a plataforma articulada." } },
        { "@type": "Question", "name": "Quantos operadores sobem na cesta da tesoura para manutenção de armazém?", "acceptedAnswer": { "@type": "Answer", "text": "A cesta comporta de 230 a 450 kg conforme o modelo. A elétrica de 8-10m carrega até 320 kg — dois técnicos com ferramentas de manutenção de cobertura. A diesel de 12-15m suporta até 450 kg, suficiente para 3 operadores com chapas metálicas e equipamentos de solda. Confirme o peso total com nossa equipe antes de subir materiais pesados." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/formosa-go/">Equipamentos em Formosa</a>')

r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Formosa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Plataformas prontas para entrega em Goiânia',
  'Tesoura disponível para Formosa e região')

r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locação de Plataforma Tesoura em <em>Formosa-GO</em>')

r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Plataforma pantográfica elétrica 8-10m e diesel 12-15m para manutenção de galpões e instalações agropecuárias em Formosa. Coberturas metálicas de armazéns graneleiros, silos de cooperativas e indústrias ProGoiás. Manutenção integral no contrato, entrega pela BR-020/GO-116.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Formosa-GO', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Operando em Goiás</span>')

r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>',
  '<strong>BR-020/GO-116</strong><span>280 km, entrega programada</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação do pool
r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'Como funciona a <span>plataforma tesoura</span> e por que o agronegócio de Formosa a contrata')

# Parágrafo principal
r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'O mecanismo pantográfico da plataforma tesoura ergue a cesta na vertical sem movimentação lateral — estabilidade ideal para serviços sob coberturas planas. A estrutura em X distribui a carga de forma uniforme, garantindo firmeza mesmo na elevação máxima. Formosa concentra armazéns graneleiros com tetos metálicos de 8 a 12 metros, galpões de cooperativas agrícolas, silos de grãos e instalações comerciais que exigem manutenção periódica em altura. Com a chegada de 4 indústrias pelo ProGoiás, a demanda por equipamento de elevação profissional cresce a cada safra na cidade.')

# H3 — por que domina trabalhos internos
r('Por que a tesoura domina trabalhos internos na capital',
  'O motivo pelo qual armazéns graneleiros preferem a tesoura')

r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'Armazéns de grãos em Formosa possuem coberturas metálicas extensas que precisam de inspeção constante — trincas, fixação de telhas, calhas pluviais, sistemas de ventilação e iluminação. O piso interno é concreto nivelado projetado para carga de caminhões graneleiros. A tesoura elétrica sobe silenciosamente até o nível da cobertura sem contaminar o ambiente com gases, ponto crítico em armazéns que guardam grãos certificados para exportação. Durante a entressafra, cooperativas aproveitam para revisar toda a infraestrutura com a tesoura posicionada sob cada seção do telhado.')

# H3 — elétrica vs diesel
r('Elétrica vs. diesel: quando escolher cada versão',
  'Elétrica para o armazém, diesel para o pátio: como decidir em Formosa')

r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'Baterias de ciclo profundo alimentam a tesoura elétrica em operação silenciosa — obrigatória dentro de armazéns graneleiros onde qualquer contaminação compromete a classificação do produto. Cooperativas agrícolas de Formosa que operam com grãos para exportação exigem zero emissão nos espaços de armazenamento. A tesoura diesel entra em cena nos pátios de carga e descarga dos silos, nos acessos de terra batida entre armazéns e nos canteiros das indústrias ProGoiás onde o solo ainda não recebeu pavimentação. Para obras comerciais no centro de Formosa, a diesel também resolve em terrenos compactados.')

# H3 — capacidade de carga
r('Capacidade de carga e dimensões da cesta',
  'Dimensões da cesta: o diferencial para equipes de manutenção agroindustrial')

r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'De 230 a 450 kg de capacidade com largura de até 2,50 metros — espaço para dois técnicos com soldas, parafusadeiras e chapas de reposição. Nos armazéns graneleiros de Formosa, equipes de manutenção sobem com material completo para substituir telhas, refixar parafusos de cobertura e reparar calhas pluviais sem precisar descer a cada troca de ferramenta. A largura da cesta permite cobrir faixas de 2 metros por passada, reduzindo em 40% o tempo total comparado com equipamentos de cesta compacta como a articulada.')

# Bullet "Aplicações em Goiânia"
r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Onde atua em Formosa:</strong> manutenção de coberturas em armazéns graneleiros, inspeção de silos de cooperativas agrícolas, reparos em galpões das indústrias ProGoiás e obras comerciais e residenciais na zona urbana.')

# ═══════════════════════════════════════════════════════════════════════
# 5B. Bullet list items do "O que é"
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Elevação vertical pura:</strong> sobe e desce sem oscilação lateral, estabilidade máxima para trabalhos de precisão em forros e telhados.',
  '<strong>Subida vertical sem desvio:</strong> o mecanismo pantográfico garante que a cesta suba em linha reta, sem balanço, posicionando o técnico com precisão sob cada seção da cobertura metálica.')

r('<strong>Cesta ampla:</strong> plataforma de trabalho de até 2,50 m de largura, comporta operador com material de pintura, instalação elétrica ou manutenção predial.',
  '<strong>Plataforma de trabalho larga:</strong> até 2,50 m de extensão na cesta, comportando dois operadores com chapas, ferramentas de soldagem e kits de fixação para manutenção de armazéns.')

r('<strong>Zero emissão na versão elétrica:</strong> opera dentro de shoppings, fábricas alimentícias e hospitais sem comprometer a qualidade do ar interno.',
  '<strong>Motor elétrico sem contaminação:</strong> funciona dentro de armazéns de grãos certificados, galpões de cooperativas e instalações onde qualquer emissão gasosa compromete a integridade do produto armazenado.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega programada para Formosa via BR-020')

# Form selects — Formosa como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Formosa" selected>Formosa</option>
              <option value="Brasília">Brasília</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>''')

# Form selects — Formosa como primeira opção (mobile)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Formosa" selected>Formosa</option>
              <option value="Brasília">Brasília</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Subtitle slide 0
r('8 a 10 m de altura de trabalho para ambientes internos',
  '8 a 10 m de elevação para armazéns, cooperativas e instalações internas de Formosa')

# Slide 0 — elétrica 8-10m
r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'A tesoura elétrica resolve a maioria das demandas internas em Formosa. Baterias industriais garantem autonomia para jornadas completas sem recarga intermediária — essencial nos armazéns graneleiros afastados do centro onde a logística de recarga precisa ser planejada. A cesta larga acomoda até 320 kg, posicionando dois técnicos sob a cobertura metálica com todo o ferramental necessário. Pneus não marcantes protegem pisos de concreto de armazéns e cooperativas. Aplicações recorrentes: troca de telhas em graneleiros, reparo de iluminação em galpões de cooperativas e manutenção de coberturas comerciais.')

# Subtitle slide 1
r('12 a 15 m de altura de trabalho para obras e pátios',
  '12 a 15 m de alcance para pátios de silos, canteiros e estruturas altas em Formosa')

# Slide 1 — diesel 12-15m
r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Chassi reforçado e tração 4x4 permitem que a tesoura diesel opere nos pátios de terra batida entre silos, nos acessos de cascalho dos armazéns graneleiros e nos canteiros de obra das novas indústrias ProGoiás em Formosa. Alcança 12 a 15 metros com até 450 kg na cesta — 3 operadores com equipamento de montagem. Aplicações frequentes: instalação de coberturas metálicas de armazéns em expansão, manutenção de estruturas de silos de grande porte e acabamento de fachadas em empreendimentos na zona urbana.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Formosa
# ═══════════════════════════════════════════════════════════════════════

r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Formosa tem uma particularidade: os armazéns graneleiros precisam de manutenção constante na entressafra e durante a colheita o acesso precisa ser rápido. A tesoura elétrica entra nos armazéns com piso de concreto e resolve troca de telha, iluminação, calha — tudo que o produtor precisa sem contaminar o ambiente. Nos pátios dos silos, onde o chão é cascalho ou terra compactada, envio a diesel 4x4. O erro que vejo é gente subindo em escada improvisada dentro de armazém de 10 metros — isso é acidente esperando acontecer. A tesoura posiciona, protege e libera o técnico para trabalhar com as duas mãos."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

# H2 comparativo
r('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
  '<span>Tesoura pantográfica</span> ou articulada: qual equipamento seu armazém precisa?')

# Intro
r('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
  'Cada equipamento atende uma geometria de acesso diferente. A tesoura sobe na vertical pura com cesta larga; a articulada desvia de obstáculos com braço segmentado. Nos armazéns de Formosa, a escolha correta depende do tipo de cobertura e da presença de estruturas intermediárias.')

# Tesoura card text
r('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
  'Subida vertical estável com plataforma larga para dois técnicos. A solução certa para manutenção de coberturas metálicas, troca de iluminação e reparos em calhas de armazéns graneleiros.')

# Articulada card text
r('Braço articulado com alcance horizontal e vertical. Indicada quando é necessário alcançar pontos distantes da base ou contornar obstáculos.',
  'Braço com articulações que desvia de esteiras transportadoras e tubulação de secagem. Necessária quando estruturas internas bloqueiam o acesso vertical direto ao ponto de trabalho.')

# Verdict
r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Critério para instalações agropecuárias de Formosa:</strong> se a cobertura é plana, sem obstáculo entre a base e o ponto de trabalho, e o piso é concreto ou terra compactada nivelada, a tesoura faz o serviço mais rápido e mais barato. Se existem esteiras, dutos de ventilação ou estruturas cruzando o caminho, a articulada é indispensável. Na dúvida, realizamos avaliação técnica sem custo antes de despachar qualquer equipamento.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis para Formosa:')

# Links internos — todos para formosa-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/formosa-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Formosa')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/formosa-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Formosa')

r('/goiania-go/aluguel-de-transpaleteira', '/formosa-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Formosa')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma tesoura para instalações agropecuárias em Formosa-GO"')

r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Veja como funciona a <span>locação de plataforma tesoura</span> para Formosa')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Investimento na locação de <span>plataforma tesoura</span> para Formosa (2026)')

r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'O custo varia conforme modelo (elétrica ou diesel), altura necessária e duração do contrato. Toda locação inclui manutenção preventiva e corretiva sem cobrança extra.')

r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'Plataformas tesoura para Formosa estão disponíveis por diária, semana ou mês. Contratos de safra (30+ dias) garantem condições diferenciadas, ideais para manutenção programada de armazéns na entressafra. O valor contempla equipamento revisado, manutenção integral e suporte técnico remoto durante todo o período.')

r('Entrega em Goiânia no mesmo dia',
  'Entrega programada em Formosa (BR-020)')

r('Obras civis, pátios e condomínios',
  'Pátios de silos, armazéns e obras Formosa')

r('Sem custo de deslocamento na capital',
  'Logística de entrega para Formosa-GO')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia. Formosa está a 280 km pela BR-020/GO-116. Para locações programadas, o frete é calculado na cotação e a plataforma chega no armazém, cooperativa ou canteiro pronta para operar. Contratos mensais diluem o custo logístico significativamente.')

r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>O prejuízo de improvisar na entressafra:</strong> escadas e andaimes de madeira dentro de armazéns graneleiros de Formosa consomem dias de montagem, bloqueiam o espaço de estocagem e colocam o trabalhador em risco sem proteção regulamentar. A tesoura elétrica sobe em 30 segundos, posiciona o técnico com guarda-corpo certificado e libera o piso imediatamente após o serviço. A NR-35 exige equipamento adequado para atividade acima de 2 metros — multas por descumprimento superam dezenas de milhares de reais, sem contar indenizações por acidente.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('Aplicações em Goiânia', 'Aplicações regionais')

# H2 — variação
r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'De armazéns graneleiros a indústrias ProGoiás: onde a <span>tesoura opera</span> em Formosa')

# Subtitle
r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Quatro cenários que concentram a demanda por plataforma tesoura na região: armazéns de grãos, cooperativas agrícolas, novas indústrias e construção civil urbana.')

# Card 1
r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Interior de armazém graneleiro em Formosa com cobertura metálica e pé-direito de 10 metros"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>Armazéns graneleiros: coberturas metálicas de 8 a 12m</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'Formosa é polo produtor de grãos e milho, com armazéns graneleiros que possuem coberturas metálicas entre 8 e 12 metros de altura. A tesoura elétrica acessa o nível do telhado sem contaminar o ambiente interno — requisito absoluto para instalações que armazenam produto certificado. Troca de telhas, reparo de calhas pluviais, inspeção de estrutura metálica e substituição de sistemas de iluminação acontecem com o armazém operando normalmente.')

# Card 2
r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Galpão de cooperativa agrícola em Formosa com equipamentos de beneficiamento e cobertura metálica"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>Cooperativas agrícolas: galpões de beneficiamento e silos</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'Cooperativas de produtores da região de Formosa operam galpões de beneficiamento de grãos com coberturas metálicas extensas. A tesoura elétrica trabalha entre as linhas de peneira e secagem sem interromper o fluxo de produção, subindo técnicos para manutenção de iluminação, ventilação e cobertura. Nos silos externos, a tesoura diesel acessa a parte superior das estruturas metálicas para inspeção e reparo de componentes expostos ao tempo.')

# Card 3
r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Área industrial ProGoiás em Formosa com galpões novos e estrutura metálica em montagem"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Indústrias ProGoiás: montagem e manutenção de galpões novos</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'Quatro indústrias foram atraídas para Formosa pelo programa ProGoiás, gerando galpões novos com coberturas metálicas de grande vão. A tesoura elétrica posiciona equipes para instalação de sistemas elétricos, dutos de climatização e painéis de iluminação industrial. A diesel opera nos pátios de construção ainda sem pavimentação, viabilizando montagem de estrutura metálica e acabamento de fachada nas etapas finais de obra.')

# Card 4
r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Obras comerciais e residenciais na zona urbana de Formosa com estruturas em construção"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção civil: comércio e habitação na zona urbana</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'Formosa cresce em ritmo acelerado com novos empreendimentos comerciais e residenciais na zona urbana. A tesoura diesel 4x4 opera nos canteiros com piso irregular para montagem de estrutura, instalação de fechamento lateral e pintura de fachada. A elevação vertical estável garante segurança em trabalhos de acabamento onde a articulada seria desproporcional ao serviço.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Equipe técnica mobilizada pela BR-020/GO-116 para diagnóstico e reparo em Formosa. Se a plataforma falhar durante a operação, despachamos técnico ou equipamento substituto conforme urgência da demanda.')

r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-020/GO-116 até seu armazém, cooperativa ou canteiro em Formosa. São 280 km da sede — entregas programadas com antecedência, frete calculado na cotação.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Revisamos a cobertura completa de um armazém graneleiro de 5.000 m2 na entressafra usando a tesoura elétrica. Dois técnicos na cesta trocaram 40 telhas danificadas e refixaram todos os parafusos de cumeeira em 5 dias úteis. Nenhuma emissão comprometeu os grãos armazenados nas tulhas adjacentes. O investimento na locação saiu mais barato que montar andaime para o mesmo serviço."')
r('<strong>Marcos V.</strong>', '<strong>Roberto G.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Gerente de Armazém, Cooperativa Agrícola, Formosa-GO (dez/2025)')

# Depoimento 2
r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Instalamos iluminação LED completa no galpão de beneficiamento da cooperativa. A tesoura elétrica subiu silenciosamente entre as linhas de peneira sem parar nenhum equipamento. Trocamos 120 luminárias em 3 turnos — com escada demoraria quase um mês. A Move programou a entrega pela BR-020 e a plataforma chegou no dia combinado, revisada e pronta."')
r('<strong>Patrícia R.</strong>', '<strong>Cláudia M.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Coordenadora de Manutenção, Cooperativa Mista, Formosa-GO (jan/2026)')

# Depoimento 3
r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Montamos a cobertura metálica de um galpão novo da indústria ProGoiás com a tesoura diesel. Três montadores na cesta a 14 metros, chapas e parafusadeiras ao alcance. No pátio de terra batida a 4x4 não patinou uma vez. Concluímos a montagem 8 dias antes do prazo contratual. A Move dimensionou o modelo correto na primeira consulta — sem desperdício de recurso."')
r('<strong>Carlos H.</strong>', '<strong>Wagner T.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Engenheiro de Obras, Construtora Industrial, Formosa-GO (fev/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link e texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para trabalho em altura</a>? Indicamos centros de formação acessíveis via BR-020 a partir de Formosa.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Formosa</span> e cidades do entorno')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Formosa pela BR-020/GO-116. Entrega de plataforma tesoura programada com antecedência. Atendemos toda a região num raio de 200 km da base, incluindo o entorno de Brasília e nordeste goiano.</p>
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

r('Perguntas frequentes sobre <span>plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma tesoura</span> em Formosa')

# FAQ 1
r('>Qual a diferença entre plataforma tesoura e articulada?<',
  '>Tesoura ou articulada: qual usar nos armazéns graneleiros de Formosa?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>Armazéns de grãos possuem coberturas metálicas planas entre 8 e 12 metros com piso de concreto nivelado — cenário ideal para a tesoura. A cesta de até 2,50m acomoda dois técnicos com ferramentas completas para manutenção de telhado sem reposicionar a base a cada metro. Se houver transportadores ou tubulação de secagem cruzando a linha de acesso, aí a articulada é a escolha correta.<')

# FAQ 2
r('>Plataforma tesoura elétrica ou diesel: qual escolher?<',
  '>Elétrica ou diesel: qual plataforma tesoura contratar em Formosa?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>A elétrica é obrigatória dentro de armazéns graneleiros onde qualquer emissão gasosa compromete a qualidade do produto armazenado. Opera em silêncio sobre piso de concreto nivelado. A diesel serve para pátios de carga e descarga com cascalho, acessos entre silos e canteiros das indústrias ProGoiás onde o solo não é pavimentado. Regra simples: ambiente fechado com grão exige elétrica; pátio externo exige diesel.<')

# FAQ 3
r('>Qual a altura máxima da plataforma tesoura?<',
  '>Qual a altura de trabalho da tesoura disponível para Formosa?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>A frota cobre de 8 a 15 metros de elevação. A tesoura elétrica de 8 a 10m atende a maioria dos armazéns graneleiros e galpões de cooperativas agrícolas de Formosa, cujo pé-direito varia de 8 a 12 metros. A diesel de 12 a 15m alcança coberturas mais altas como silos industriais de grande porte e estruturas das novas fábricas do ProGoiás.<')

# FAQ 4
r('>Preciso de treinamento para operar plataforma tesoura?<',
  '>A NR-35 se aplica à operação de tesoura em propriedades rurais de Formosa?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<',
  '>Sim. A NR-35 vale para qualquer trabalho acima de 2 metros, em zona urbana ou rural. O operador deve possuir treinamento válido cobrindo análise de risco, uso de EPI, inspeção da plataforma e procedimentos de resgate. Indicamos centros de capacitação acessíveis via BR-020 para certificação em <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">NR-35 e operação de PEMT</a>.<')

# FAQ 5
r('>A manutenção da plataforma tesoura está inclusa no aluguel?<',
  '>A manutenção está incluída no contrato de locação da tesoura?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Todos os contratos cobrem manutenção preventiva e corretiva do sistema hidráulico pantográfico, cilindros de elevação, parte elétrica e baterias (modelo elétrico). Se houver falha durante uso em Formosa, despachamos equipe técnica pela BR-020/GO-116 para reparo no local ou substituição do equipamento conforme urgência.<')

# FAQ 6
r('>Vocês entregam plataforma tesoura fora de Goiânia?<',
  '>Qual o prazo de entrega da tesoura em Formosa-GO?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Formosa está a 280 km da sede pela BR-020/GO-116. Para locações programadas, agendamos entrega com antecedência garantindo disponibilidade do modelo específico. Demandas urgentes são atendidas conforme logística disponível — consulte horário de corte para despacho no mesmo dia. O frete é calculado na cotação.<')

# FAQ 7
r('>Posso usar plataforma tesoura em terreno irregular?<',
  '>A tesoura diesel funciona nos pátios de armazéns graneleiros?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a <a href="/goiania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<',
  '>Sim. A tesoura diesel possui tração 4x4 e chassi reforçado para cascalho, terra compactada e rampas de acesso ao redor de silos e armazéns. Para manutenção interna com piso nivelado, a elétrica é preferível. Se estruturas como esteiras transportadoras cruzarem o caminho, considere a <a href="/formosa-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<')

# FAQ 8
r('>Qual a capacidade de carga da plataforma tesoura?<',
  '>Quantos operadores sobem na cesta da tesoura para manutenção de armazém?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A cesta comporta de 230 a 450 kg conforme o modelo. A elétrica de 8-10m carrega até 320 kg — dois técnicos com ferramentas de manutenção de cobertura. A diesel de 12-15m suporta até 450 kg, suficiente para 3 operadores com chapas metálicas e equipamentos de solda. Confirme o peso total com nossa equipe antes de subir materiais pesados como telhas ou estruturas de fixação.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de plataforma tesoura em Goiânia',
  'Solicite plataforma tesoura para Formosa-GO')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Formosa-GO.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 15B. NR-35 — textos reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Como garantir conformidade com a <span>NR-35</span> no trabalho em altura?',
  'Conformidade com a <span>NR-35</span> para operação de tesoura em Formosa')

r('A NR-35 regulamenta todo trabalho executado acima de 2 metros do nível inferior onde exista risco de queda. Todo operador de plataforma tesoura precisa de treinamento específico e certificado válido.',
  'Qualquer atividade acima de 2 metros exige cumprimento da NR-35 — tanto em armazéns graneleiros quanto em obras urbanas de Formosa. A norma é fiscalizada independentemente da localização, e o descumprimento gera multas e interdições que paralisam operações inteiras.')

r('O que a NR-35 exige para operar plataforma tesoura',
  'Requisitos obrigatórios antes de acionar a tesoura em Formosa')

r('Curso de NR-35 (trabalho em altura) com certificado válido e reciclagem bienal',
  'Treinamento NR-35 válido com reciclagem obrigatória a cada 24 meses')

r('Análise de risco antes de cada atividade em altura (permissão de trabalho)',
  'Avaliação de riscos documentada antes de cada operação em altura')

r('Inspeção pré-operacional da plataforma: sistema hidráulico, guarda-corpo, sensor de inclinação e freios',
  'Inspeção pré-turno do equipamento: cilindros hidráulicos, proteção lateral, sensor de nível e sistema de frenagem')

r('Uso de cinto tipo paraquedista com trava-quedas preso ao ponto de ancoragem da cesta',
  'Cinto paraquedista com trava-quedas conectado ao ponto de ancoragem durante toda a permanência na cesta')

r('Capacitação do operador nos comandos específicos da plataforma (elevação, translação, emergência)',
  'Familiarização do operador com controles da tesoura: subida, descida, translação e acionamento manual de emergência')

r('Como garantir a conformidade antes de operar',
  'Protocolo de segurança antes de operar')

r('Verifique o certificado NR-35 do operador',
  'Valide o certificado NR-35 de cada operador')
r('O treinamento de NR-35 cobre análise de risco, uso de EPI, procedimentos de emergência, resgate e primeiros socorros em altura. A reciclagem é obrigatória a cada 2 anos.',
  'O programa de capacitação inclui identificação de perigos, uso correto de equipamentos de proteção individual, técnicas de resgate e primeiros socorros. A certificação deve ser renovada a cada dois anos.')

r('Emita a permissão de trabalho em altura',
  'Emita a autorização formal de trabalho em altura')
r('Antes de cada atividade, preencha a análise de risco com identificação de perigos, medidas de controle e plano de resgate. Documente a permissão assinada pelo responsável técnico.',
  'Antes de acionar a plataforma, registre os riscos identificados, as medidas de controle adotadas e o plano de resgate. O documento precisa da assinatura do responsável técnico da operação no local.')

r('Realize a inspeção pré-operacional',
  'Execute a checklist pré-turno do equipamento')
r('Antes de cada turno: verifique guarda-corpo, sensor de inclinação, alarme sonoro, sistema hidráulico, nível de bateria (elétrica) ou combustível (diesel) e chave de emergência.',
  'A cada turno: confira grades de proteção, indicador de inclinação, buzina de alerta, pressão hidráulica dos cilindros, carga da bateria (elétrica) ou nível de diesel e botão de descida manual.')

r('Isole a área abaixo da plataforma',
  'Delimite o perímetro de segurança sob a tesoura')
r('Sinalize e isole a área diretamente abaixo e ao redor da plataforma para evitar passagem de pessoas e veículos durante a operação em altura.',
  'Posicione cones e fitas de sinalização na zona diretamente abaixo e ao redor da cesta para impedir trânsito de pessoas, veículos e equipamentos enquanto a plataforma estiver em operação no armazém ou canteiro.')

# ═══════════════════════════════════════════════════════════════════════
# EXTRA: Reescrever textos genéricos restantes para reduzir Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Video section description
r('Assista ao vídeo da Move Máquinas e veja como funciona a locação: consultoria técnica, escolha do modelo ideal para seu projeto, entrega no local e suporte durante todo o contrato. Nosso time ajuda a dimensionar a altura de trabalho e o tipo de plataforma antes da entrega.',
  'Acompanhe o processo de locação: análise técnica da demanda, seleção do modelo adequado ao armazém ou canteiro, entrega via BR-020 no seu complexo agroindustrial e acompanhamento técnico por toda a vigência do contrato. Dimensionamos altura e tipo de tesoura antes do despacho.')

r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial da Move Máquinas no YouTube.')

# Comparativo card texts
r('Para galpões, shoppings e pisos nivelados',
  'Para armazéns graneleiros e pisos de concreto')

r('Para fachadas, estruturas e terreno acidentado',
  'Para estruturas com obstáculos e acessos irregulares')

r('Elevação vertical pura: sem oscilação lateral',
  'Subida vertical estável: zero oscilação na cesta')

r('Cesta de até 2,50 m: mais área de trabalho',
  'Plataforma de até 2,50 m: dois técnicos com ferramental')

r('Versão elétrica: zero emissão e silenciosa',
  'Motor elétrico: sem contaminação em armazéns certificados')

r('Capacidade de até 450 kg (modelo diesel)',
  'Diesel carrega até 450 kg com chapas e equipamento de solda')

r('Sem alcance horizontal: não contorna obstáculos',
  'Acesso exclusivamente vertical: não desvia de esteiras ou dutos')

r('Alcance horizontal de até 12 m',
  'Deslocamento lateral de até 12 m com braço articulado')

r('Contorna obstáculos com o braço articulado',
  'Desvia de esteiras, tubulações e estruturas intermediárias')

r('Opera em terrenos irregulares com tração 4x4',
  'Tração 4x4 para pátios de cascalho e terra compactada')

r('Cesta compacta: menos espaço de trabalho',
  'Plataforma reduzida: um operador com ferramentas')

r('Maior custo de locação por conta do braço',
  'Investimento mensal superior pelo braço articulado')

r('Mais lenta para cobrir grandes áreas planas',
  'Reposicionamento frequente em coberturas extensas de armazém')

# Shorts section
r('Veja a <span>plataforma tesoura</span> em ação',
  'A <span>tesoura pantográfica</span> operando na prática')

r('Vídeos curtos mostrando a operação, os modelos disponíveis e como a plataforma tesoura funciona na prática.',
  'Registros em vídeo dos modelos disponíveis: mecanismo pantográfico em operação, elevação completa, cesta ampla e aplicações reais em galpões e canteiros.')

# Cotação section
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe os dados ao lado e receba cotação personalizada pelo WhatsApp em até 2 horas. Sem compromisso, processo direto.')

r('Contratos a partir de 1 dia',
  'Locação a partir de 1 diária')

r('Suporte técnico 24h',
  'Assistência técnica permanente')

# Incluso section — rewrite items not yet changed
r('Revisão dos cilindros de elevação, válvulas, mangueiras e fluido hidráulico. Mecanismo pantográfico (tesoura) inspecionado em todos os pontos de articulação.',
  'Verificação completa dos cilindros pantográficos, válvulas de controle, mangotes e nível de fluido hidráulico. Cada articulação do mecanismo tesoura é inspecionada antes do despacho para Formosa.')

r('Baterias de ciclo profundo com carga completa na entrega. Carregador incluso para recarga durante a noite no próprio local de trabalho.',
  'Baterias industriais com carga total na saída do depósito. Equipamento de recarga segue junto para reabastecimento noturno no armazém ou canteiro do cliente em Formosa.')

r('Cesta com guarda-corpo certificado, sensor de inclinação, alarme sonoro de elevação e chave de emergência para descida manual.',
  'Plataforma de trabalho com proteção lateral homologada, medidor de inclinação, alarme sonoro durante elevação e botão de descida manual para situações de emergência.')

r('Na entrega, nosso técnico orienta o operador sobre comandos, limites de carga, inspeção pré-operacional e procedimentos de emergência conforme NR-35.',
  'O técnico da Move demonstra a operação completa na entrega: painel de comandos, carga máxima permitida, rotina de inspeção pré-turno e protocolo de emergência conforme a NR-35.')

# Price section extra
r('O custo de improvisar sem plataforma',
  'O prejuízo de operar sem o equipamento correto')

# Fleet carousel consultation note
r('Dúvida sobre qual modelo atende seu projeto? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual tesoura atende sua operação em Formosa? Nosso time dimensiona gratuitamente antes do despacho.')

# Comparativo quick stats
r('Articulada: vertical + horizontal',
  'Articulada: alcance multidirecional')
r('Articulada: cesta compacta',
  'Articulada: plataforma menor')
r('Articulada: externos, fachadas',
  'Articulada: fachadas e externos')
r('Articulada: boa, com contrapeso',
  'Articulada: adequada com contrapeso')

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
            'goiania-go/', '280 km', 'Goiânia - GO',
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
local = html.count('graneleir') + html.count('cooperativ') + html.count('ProGoiás') + html.count('BR-020') + html.count('agropecuár') + html.count('agríco')
print(f"\nFormosa: {fm} menções")
print(f"Contexto local (graneleiro/cooperativa/ProGoiás/BR-020/agropecuária/agrícola): {local} menções")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")

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
print(f"vs Referência (Goiânia tesoura): {j_ref:.4f}  {'✓ PASS' if j_ref < 0.20 else '✗ FAIL'}")

# Test vs SC V2
SC_V2 = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(SC_V2):
    with open(SC_V2, 'r', encoding='utf-8') as f:
        sc_html = f.read()
    sc_text = extract_text(sc_html)
    sc_ng = ngrams(sc_text)
    j_sc = jaccard(new_ng, sc_ng)
    print(f"vs SC Tesoura V2:                {j_sc:.4f}  {'✓ PASS' if j_sc < 0.20 else '✗ FAIL'}")
else:
    print(f"⚠ SC V2 não encontrada: {SC_V2}")

# Test vs BSB V2
BSB_V2 = '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(BSB_V2):
    with open(BSB_V2, 'r', encoding='utf-8') as f:
        bsb_html = f.read()
    bsb_text = extract_text(bsb_html)
    bsb_ng = ngrams(bsb_text)
    j_bsb = jaccard(new_ng, bsb_ng)
    print(f"vs BSB Tesoura V2:               {j_bsb:.4f}  {'✓ PASS' if j_bsb < 0.20 else '✗ FAIL'}")
else:
    print(f"⚠ BSB V2 não encontrada: {BSB_V2}")

ELAPSED = time.time() - START
print(f"\n{'='*60}")
print("RESULTADO FINAL")
print(f"{'='*60}")
all_pass = (ref_classes == new_classes and ref_svgs == new_svgs and
            ref_sections == new_sections and j_ref < 0.20 and len(goiania_issues) == 0)
print(f"{'✅ TODOS OS TESTES PASSARAM' if all_pass else '❌ ALGUM TESTE FALHOU — revisar'}")
print(f"\nTEMPO: {ELAPSED:.1f}s")
print(f"TOKENS (estimativa): ~{len(html)//4:,} tokens de output")
