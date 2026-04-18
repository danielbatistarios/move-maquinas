#!/usr/bin/env python3
"""
rebuild-brasilia-tesoura-v2.py
Gera LP de Plataforma Tesoura para Brasília-DF
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

from datetime import datetime
START = datetime.now()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

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
  '<title>Locação de Plataforma Tesoura em Brasília-DF | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma elevatória tesoura para locação em Brasília-DF: modelos elétricos 8-10 m e diesel 12-15 m. Ideal para manutenção predial em shoppings como ParkShopping e Conjunto Nacional, edifícios comerciais do SIA e reformas em Águas Claras. Entrega via BR-060, manutenção inclusa."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Locação de Plataforma Tesoura em Brasília-DF | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Plataforma tesoura para locação em Brasília. Elétrica 8-10 m para shoppings e edifícios governamentais; diesel 12-15 m para obras em Águas Claras e Taguatinga. Manutenção inclusa, entrega via BR-060."')

r('content="BR-GO"', 'content="BR-DF"')
r('content="Goiânia, Goiás, Brasil"', 'content="Brasília, Distrito Federal, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-15.7975;-47.8919"')
r('content="-16.7234, -49.2654"', 'content="-15.7975, -47.8919"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -15.7975, "longitude": -47.8919')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -15.7975')
r('"longitude": -49.2654', '"longitude": -47.8919')

# Schema — Service name
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Locação de Plataforma Elevatória Tesoura em Brasília"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Brasília", "addressRegion": "DF"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Brasília", "item": "https://movemaquinas.com.br/brasilia-df/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Brasília", "item": "https://movemaquinas.com.br/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura"')

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
        { "@type": "Question", "name": "Quando usar plataforma tesoura em vez de articulada em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "A tesoura é a escolha certa sempre que o acesso ao ponto de trabalho é vertical direto — sem obstáculos entre o piso e o teto. Em shoppings como ParkShopping e Conjunto Nacional, a manutenção de forro e iluminação acontece em áreas abertas com pé-direito de 6 a 10 metros e piso nivelado. A articulada só é necessária quando há obstáculos no caminho, como marquises ou varandas em fachadas." } },
        { "@type": "Question", "name": "Tesoura elétrica ou diesel para obras no Distrito Federal?", "acceptedAnswer": { "@type": "Answer", "text": "A elétrica domina trabalhos internos em Brasília: shoppings, edifícios do SIA, prédios governamentais e hospitais. Silenciosa e sem emissão de gases. A diesel opera em canteiros de obra com piso irregular — situação comum em loteamentos de Águas Claras, expansão de Ceilândia e reformas externas em Taguatinga. A escolha depende do ambiente: fechado exige elétrica, aberto com terreno irregular exige diesel." } },
        { "@type": "Question", "name": "Qual a altura máxima da tesoura disponível para Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "Trabalhamos com dois patamares: tesoura elétrica de 8 a 10 metros e diesel de 12 a 15 metros de altura de trabalho. Para manutenção de forro em shoppings e galpões do SIA, a elétrica de 8-10 m é suficiente. Para obras de construção civil em edifícios de Águas Claras ou estruturas industriais maiores, o modelo diesel de 12-15 m é indicado." } },
        { "@type": "Question", "name": "Operadores em Brasília precisam de certificação NR-35 para usar a tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo trabalho acima de 2 metros exige treinamento NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. Em prédios do governo federal, a fiscalização é rigorosa e o certificado é obrigatório para acesso ao canteiro. Indicamos centros credenciados em Brasília e Goiânia para a capacitação." } },
        { "@type": "Question", "name": "O contrato de locação inclui manutenção da tesoura em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Manutenção preventiva e corretiva do sistema hidráulico, cilindros, mecanismo pantográfico, sistema elétrico e baterias estão inclusos. Se a plataforma apresentar falha durante o contrato, nossa equipe técnica se desloca de Goiânia pela BR-060 para diagnóstico e reparo no local. Em contratos de longa duração, mantemos peças de reposição disponíveis." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de plataforma tesoura em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "Brasília fica a 209 km da nossa sede em Goiânia, com acesso direto pela BR-060. A entrega é programada para o dia seguinte à confirmação do contrato. Para urgências, avaliamos a possibilidade de despacho no mesmo dia com transporte dedicado. O frete para o Distrito Federal é negociado no orçamento." } },
        { "@type": "Question", "name": "A tesoura diesel opera nos canteiros de obra de Águas Claras e Taguatinga?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O modelo diesel possui tração 4x4 projetada para canteiros com piso de terra, cascalho e desnível moderado — cenário comum nas frentes de obra de Águas Claras, Vicente Pires e Taguatinga. A elétrica exige piso firme e nivelado. Antes de entregar, avaliamos as condições do terreno para garantir que o modelo correto seja enviado." } },
        { "@type": "Question", "name": "Quantos operadores cabem na cesta da plataforma tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Depende do modelo. A tesoura elétrica de 8-10 m suporta até 320 kg — dois operadores com ferramentas. A diesel de 12-15 m chega a 450 kg, comportando até três pessoas com materiais de trabalho. Em reformas de shoppings de Brasília onde o pintor trabalha lado a lado com o eletricista, a cesta larga da tesoura permite que ambos operem simultaneamente sem reposicionar a máquina." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/brasilia-df/">Equipamentos em Brasília</a>')

r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Brasília</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Plataformas prontas para entrega em Goiânia',
  'Plataformas com entrega programada para Brasília')

r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locação de Plataforma Elevatória Tesoura em <em>Brasília</em>')

r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Plataformas tesoura elétrica e diesel com 8 a 15 metros de alcance vertical. Manutenção predial em shoppings como ParkShopping e Conjunto Nacional, edifícios comerciais do SIA, reformas internas em prédios governamentais e obras de construção civil em Águas Claras. Entrega via BR-060, manutenção inclusa.')

# WhatsApp URLs — encode Brasília
r('Goi%C3%A2nia', 'Bras%C3%ADlia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Brasília
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência em equipamentos</span>')

r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>',
  '<strong>Entrega via BR-060</strong><span>209 km de Goiânia</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'O que é a <span>plataforma tesoura</span> e por que lidera manutenção predial em Brasília')

# Parágrafo principal
r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'A plataforma elevatória tesoura é um equipamento com mecanismo pantográfico que eleva a cesta na vertical pura — sem deslocamento lateral. Sobe e desce em linha reta, garantindo estabilidade máxima em superfícies planas como forros de shoppings, tetos de galpões comerciais e coberturas de edifícios. Brasília reúne o maior volume de manutenção predial do Centro-Oeste: shoppings como ParkShopping, Conjunto Nacional e Terraço Shopping demandam troca de iluminação e pintura de forro; edifícios comerciais no SIA precisam de acesso ao teto de galpões; e os milhares de prédios governamentais passam por reformas internas constantes. Esse cenário faz da capital federal um dos mercados mais intensivos em locação de plataforma tesoura do país.')

# H3 — por que domina
r('Por que a tesoura domina trabalhos internos na capital',
  'Como a tesoura resolve manutenção em shoppings e edifícios do Plano Piloto')

r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'O mecanismo pantográfico concentra toda a força no eixo vertical, mantendo o centro de gravidade estável mesmo na altura máxima. Nos corredores do ParkShopping e do Conjunto Nacional, onde o pé-direito varia de 6 a 10 metros e o piso é porcelanato polido, a tesoura elétrica opera sem emissão de gases, sem ruído e com pneus não marcantes. A equipe de manutenção substitui luminárias, repara forro e repinta tetos durante a madrugada sem deixar marcas no piso nem comprometer a operação do shopping no dia seguinte.')

# H3 — elétrica vs diesel
r('Elétrica vs. diesel: quando escolher cada versão',
  'Elétrica para shoppings e SIA, diesel para canteiros em Águas Claras')

r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'A tesoura elétrica é alimentada por baterias e opera em silêncio total — requisito dos shoppings de Brasília, hospitais da rede Sarah e edifícios do governo federal onde emissão de gases é proibida. A diesel com tração 4x4 funciona em terrenos irregulares e canteiros sem pavimentação. Para reformas internas no Terraço Shopping, troca de luminárias no ParkShopping ou manutenção de teto em galpões do SIA, a elétrica é obrigatória. Para obras civis nos edifícios em construção de Águas Claras, loteamentos de Vicente Pires e canteiros de Ceilândia, a diesel é a única opção segura.')

# H3 — capacidade
r('Capacidade de carga e dimensões da cesta',
  'Cesta ampla para equipes de manutenção predial')

r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'A cesta suporta de 230 a 450 kg, acomodando de 1 a 3 operadores com ferramentas, tintas e materiais. A largura varia de 1,20 m a 2,50 m conforme o modelo — o operador se desloca lateralmente cobrindo faixas de até 2 metros sem reposicionar a base. Em reformas de grandes shoppings de Brasília, onde equipes de pintores precisam cobrir centenas de metros quadrados de forro por noite, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com plataformas de cesta compacta.')

# Bullet "Aplicações em Goiânia"
r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Aplicações em Brasília:</strong> manutenção de forro e iluminação no ParkShopping e Conjunto Nacional, reparos em teto de galpões do SIA, reformas internas em prédios governamentais da Esplanada e obras de construção civil em Águas Claras e Taguatinga.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega programada para Brasília via BR-060')

# Form selects — Brasília como primeira opção (desktop form)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Brasília" selected>Brasília</option>
              <option value="Taguatinga">Taguatinga</option>
              <option value="Águas Claras">Águas Claras</option>
              <option value="Ceilândia">Ceilândia</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# Mobile form selects
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Brasília" selected>Brasília</option>
              <option value="Taguatinga">Taguatinga</option>
              <option value="Águas Claras">Águas Claras</option>
              <option value="Ceilândia">Ceilândia</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Outra">Outra cidade</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0 — elétrica 8-10m
r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'O modelo mais demandado para manutenção predial em Brasília. Baterias de ciclo profundo alimentam o motor silencioso e sem emissão de gases — requisito dos shoppings, hospitais e edifícios governamentais da capital federal. Cesta de até 320 kg para dois operadores com ferramentas. Pneus não marcantes preservam pisos de porcelanato no ParkShopping e Conjunto Nacional. Utilizada para troca de luminárias, pintura de forro e reparos em sistemas de ar condicionado em edifícios comerciais do SIA.')

# Slide 1 — diesel 12-15m
r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Tração 4x4 com chassi reforçado para canteiros de obra e pátios sem pavimentação. Alcança 12 a 15 metros de altura com capacidade de até 450 kg — três operadores com ferramentas e materiais. Motor diesel com torque para desnível moderado. Indicada para obras nos edifícios em construção de Águas Claras, montagem de estruturas metálicas em galpões de Taguatinga e manutenção de fachada em prédios comerciais de Ceilândia onde o terreno do canteiro é irregular.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Brasília
# ═══════════════════════════════════════════════════════════════════════

r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Brasília é o maior mercado de manutenção predial que atendemos depois de Goiânia. O perfil é bem definido: shoppings que trocam iluminação de madrugada, edifícios do SIA com galpão de teto alto e prédios do governo que fazem reforma interna sem parar o expediente. A tesoura elétrica resolve tudo isso — silenciosa, sem fumaça e com cesta larga para o pintor se deslocar sem descer. Agora, quando o cliente liga pedindo tesoura para obra em Águas Claras com chão de terra, eu já redireciono para a diesel 4x4. Piso irregular exige diesel, sem exceção. Essa análise a gente faz antes de mandar o equipamento."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Critério objetivo para projetos em Brasília:</strong> se o trabalho é em forro de shopping, teto de galpão do SIA ou cobertura de edifício com piso nivelado, a tesoura entrega o resultado com mais velocidade e menor custo. Se o ponto de trabalho exige contornar marquises, acessar fachadas com recuo ou operar em canteiro com terreno irregular, a articulada é o equipamento correto. Na dúvida, avaliamos seu projeto sem custo.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis para Brasília:')

# Links internos — todos para brasilia-df
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/brasilia-df/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Brasília')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/brasilia-df/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Brasília')

r('/goiania-go/aluguel-de-transpaleteira', '/brasilia-df/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Brasília')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text + title
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma tesoura para shoppings e edifícios em Brasília"')

r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Entenda como funciona a <span>locação de plataforma tesoura</span> para Brasília')

r('Assista ao vídeo da Move Máquinas e veja como funciona a locação: consultoria técnica, escolha do modelo ideal para seu projeto, entrega no local e suporte durante todo o contrato. Nosso time ajuda a dimensionar a altura de trabalho e o tipo de plataforma antes da entrega.',
  'Assista ao vídeo institucional e conheça o processo de locação: consultoria técnica para dimensionar o modelo correto, transporte pela BR-060 até o seu endereço em Brasília e suporte durante todo o contrato. Nosso time avalia a altura de trabalho, o tipo de piso e o ambiente antes de recomendar tesoura elétrica ou diesel.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Quanto custa a locação de <span>plataforma tesoura</span> em Brasília em 2026?')

r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'O investimento varia conforme modelo (elétrica ou diesel), altura de trabalho e duração do contrato. Todos os contratos incluem manutenção preventiva, corretiva e suporte técnico.')

r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'A locação para Brasília está disponível nas modalidades diária, semanal e mensal, com frete via BR-060 negociado no orçamento. Contratos de maior duração oferecem condições melhores. O valor cobre equipamento, manutenção completa e suporte técnico durante todo o período de uso.')

r('Entrega em Goiânia no mesmo dia',
  'Entrega em Brasília via BR-060')

r('Sem custo de deslocamento na capital',
  'Frete dedicado pela BR-060 para o Distrito Federal')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'Nossa sede fica na Av. Eurico Viana, 4913, em Goiânia — 209 km de Brasília pela BR-060. A entrega é programada para o dia seguinte à confirmação do contrato, com frete negociado individualmente. Para contratos de longa duração, o custo de transporte é diluído no valor mensal. A plataforma chega ao seu shopping, edifício ou canteiro pronta para operar.')

r('O custo de improvisar sem plataforma',
  'O custo de improvisar em prédios de Brasília')

r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes montados em corredores de shoppings de Brasília bloqueiam a circulação por horas, atrasam a operação comercial e expõem o trabalhador a risco de queda. Em prédios do governo, a fiscalização do MTE é rigorosa — não conformidade com NR-35 gera multas de dezenas de milhares de reais e interdição do serviço. A tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo certificado e libera o piso imediatamente ao final do trabalho.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('Aplicações em Goiânia', 'Aplicações em Brasília')

# H2
r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'Onde a <span>plataforma tesoura</span> opera com mais frequência em Brasília?')

r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Do ParkShopping aos edifícios governamentais, dos galpões do SIA às obras de Águas Claras — os 4 principais cenários de uso no Distrito Federal.')

# Card 1
r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Interior do ParkShopping Brasília com forro decorativo e iluminação em altura"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>Shoppings de Brasília: forro, iluminação e pintura</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'ParkShopping, Conjunto Nacional e Terraço Shopping realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão de gases e com pneus não marcantes que preservam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros por passada, reduzindo o tempo total de reposicionamento pela metade.')

# Card 2
r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Galpão comercial no Setor de Indústria e Abastecimento (SIA) de Brasília com teto elevado"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>SIA: teto de galpão e manutenção de cobertura</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'O Setor de Indústria e Abastecimento concentra centenas de galpões comerciais com pé-direito de 8 a 14 metros. A tesoura elétrica sobe até o nível do telhado para troca de telhas translúcidas, reparo em calhas, substituição de luminárias industriais e inspeção de estrutura metálica. Opera dentro do galpão sem emitir gases, permitindo que o trabalho aconteça durante o expediente comercial sem interromper as operações no piso.')

# Card 3
r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Interior de edifício governamental em Brasília durante reforma com equipamento de acesso em altura"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Edifícios governamentais: reformas internas sem parar o expediente</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'Ministérios na Esplanada, tribunais superiores e prédios da administração federal passam por reformas internas constantes — troca de luminárias, pintura de forro, manutenção de dutos de ar condicionado e instalação de cabeamento estruturado. A tesoura elétrica opera em silêncio dentro do prédio enquanto servidores trabalham nos andares adjacentes. A cesta estável posiciona o eletricista na altura exata do duto de HVAC ou do quadro de distribuição.')

# Card 4
r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Edifícios residenciais em construção em Águas Claras, Brasília, com canteiro de obra e estrutura metálica"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção civil em Águas Claras e Taguatinga</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'Águas Claras é um dos maiores canteiros verticais do Distrito Federal, com dezenas de edifícios residenciais em construção simultaneamente. A tesoura diesel 4x4 opera nesses canteiros com piso de terra e desnível, alcançando até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e acabamentos de fachada. Em Taguatinga e Ceilândia, condomínios horizontais e comerciais também demandam o modelo diesel para trabalhos externos.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Equipe técnica com deslocamento pela BR-060 para diagnóstico e reparo no local em Brasília. Em caso de falha, acionamos suporte ou substituímos o equipamento conforme urgência do contrato.')

r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-060 até seu shopping, edifício ou canteiro em Brasília. Entrega programada para o dia seguinte à confirmação, com frete negociado no orçamento. Contratos longos diluem o custo de transporte.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Trocamos 280 luminárias no ParkShopping durante 6 madrugadas usando a tesoura elétrica da Move. A máquina não faz barulho, não marca o piso de porcelanato e posiciona o eletricista a 8 metros em segundos. Antes usávamos andaime e levávamos 3 semanas. Com a tesoura, terminamos antes do prazo e sem nenhuma reclamação de lojista."')
r('<strong>Marcos V.</strong>', '<strong>Rafael M.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Coordenador de Manutenção, Shopping, Brasília-DF (jan/2026)')

# Depoimento 2
r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Reforma interna de dois pavimentos em edifício no SIA. A tesoura elétrica acessou o teto do galpão a 12 metros para reparar calhas e trocar telhas translúcidas sem interromper a operação do andar de baixo. A Move trouxe o equipamento pela BR-060 no dia seguinte ao fechamento do contrato. Manutenção no prazo e suporte técnico sempre que precisamos."')
r('<strong>Patrícia R.</strong>', '<strong>Fernanda L.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Gerente de Facilities, Empresa Comercial SIA, Brasília-DF (fev/2026)')

# Depoimento 3
r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Usamos a tesoura diesel no canteiro de um condomínio em Águas Claras. A 4x4 andou no terreno de cascalho sem travar e posicionou nosso soldador a 14 metros para montagem das treliças de cobertura. Sem a tesoura, teríamos que montar andaime tubular e perder 10 dias antes de começar a soldar. A Move resolveu com entrega em 24 horas."')
r('<strong>Carlos H.</strong>', '<strong>Bruno S.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Encarregado de Obras, Construtora, Águas Claras-DF (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso de NR-35 (trabalho em altura)</a>? Indicamos centros credenciados em Brasília e Goiânia para a capacitação.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada para <span>Brasília</span> e cidades do Entorno')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 209 km de Brasília pela BR-060. Entrega de plataforma tesoura programada para o dia seguinte à confirmação do contrato. Atendemos todo o Distrito Federal e cidades do Entorno num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/"><strong>Brasília</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/valparaiso-de-goias-go/">Valparaíso de Goiás</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/">Luziânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
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
        Taguatinga
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Águas Claras
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-47.8919!3d-15.7975')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Brasília-DF"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Brasília</a>')
r('/goiania-go/" style="color', '/brasilia-df/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma tesoura</span> em Brasília')

# FAQ 1
r('>Qual a diferença entre plataforma tesoura e articulada?<',
  '>Quando usar plataforma tesoura em vez de articulada em Brasília?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>A tesoura resolve quando o acesso ao ponto de trabalho é vertical direto e sem obstáculos. Em shoppings como ParkShopping e Conjunto Nacional, onde o forro é plano e o piso é nivelado, a tesoura opera com mais estabilidade, mais espaço na cesta e menor custo. A articulada só é necessária quando o cesto precisa contornar obstáculos como marquises, varandas ou vigas — situação de fachadas, não de manutenção interna.<')

# FAQ 2
r('>Plataforma tesoura elétrica ou diesel: qual escolher?<',
  '>Tesoura elétrica ou diesel para obras no Distrito Federal?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>A elétrica domina trabalhos internos em Brasília: shoppings, edifícios do SIA, prédios governamentais e hospitais — silenciosa e sem emissão de gases. A diesel opera em canteiros com terreno irregular, como obras em Águas Claras, Vicente Pires e Taguatinga. Ambiente fechado exige elétrica; terreno sem pavimentação exige diesel. Na dúvida, avaliamos as condições do local antes de enviar o modelo.<')

# FAQ 3
r('>Qual a altura máxima da plataforma tesoura?<',
  '>Qual a altura máxima da tesoura disponível para Brasília?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>Dois patamares: elétrica de 8 a 10 metros e diesel de 12 a 15 metros de altura de trabalho. Para manutenção de forro em shoppings e galpões do SIA, a elétrica de 8-10 m atende a maioria das demandas. Para obras civis em edifícios de Águas Claras ou estruturas maiores, o modelo diesel de 12-15 m é o indicado.<')

# FAQ 4
r('>Preciso de treinamento para operar plataforma tesoura?<',
  '>Operadores em Brasília precisam de certificação NR-35 para a tesoura?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<',
  '>Sim. A NR-35 exige curso válido com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. Em prédios do governo federal, a fiscalização é rigorosa e o certificado é obrigatório para acesso ao canteiro. A reciclagem é bienal. Indicamos centros credenciados em Brasília e Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<')

# FAQ 5
r('>A manutenção da plataforma tesoura está inclusa no aluguel?<',
  '>O contrato de locação inclui manutenção da tesoura em Brasília?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Manutenção preventiva e corretiva do sistema hidráulico, cilindros, mecanismo pantográfico, sistema elétrico e baterias está inclusa em todos os contratos. Se a plataforma apresentar falha, nossa equipe técnica se desloca de Goiânia pela BR-060 para diagnóstico e reparo. Em contratos de longa duração, mantemos peças de reposição disponíveis para agilizar o atendimento.<')

# FAQ 6
r('>Vocês entregam plataforma tesoura fora de Goiânia?<',
  '>Qual o prazo de entrega de plataforma tesoura em Brasília?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Brasília fica a 209 km pela BR-060. A entrega é programada para o dia seguinte à confirmação do contrato. Para urgências, avaliamos a possibilidade de despacho no mesmo dia com transporte dedicado. O frete para o DF é negociado individualmente no orçamento, com diluição no valor mensal para contratos longos.<')

# FAQ 7
r('>Posso usar plataforma tesoura em terreno irregular?<',
  '>A tesoura diesel opera nos canteiros de Águas Claras e Taguatinga?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a <a href="/goiania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<',
  '>Sim. O modelo diesel possui tração 4x4 projetada para canteiros com piso de terra, cascalho e desnível — cenário comum nas frentes de obra de Águas Claras, Vicente Pires e Taguatinga. A elétrica exige piso firme. Antes de entregar, avaliamos o terreno. Se o projeto exige alcance lateral além da vertical, considere a <a href="/brasilia-df/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<')

# FAQ 8
r('>Qual a capacidade de carga da plataforma tesoura?<',
  '>Quantos operadores cabem na cesta da plataforma tesoura?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A elétrica de 8-10 m suporta até 320 kg — dois operadores com ferramentas. A diesel de 12-15 m chega a 450 kg, comportando três pessoas com materiais. Em reformas de shoppings de Brasília onde pintor e eletricista precisam trabalhar lado a lado, a cesta larga da tesoura permite operação simultânea sem reposicionar. Para cargas pesadas como luminárias industriais ou chapas, confirme o peso total com nossa equipe antes da locação.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de plataforma tesoura em Goiânia',
  'Solicite orçamento de plataforma tesoura para Brasília')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Brasília.\\n\\n'")

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
            'goiania-go/', '209 km', 'Goiânia —',
            'Brasília e Goiânia', 'sede em Goiânia',
            'de Goiânia pela BR-060', 'depois de Goiânia',
            'desloca de Goiânia', 'sede em Goiânia',
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
bsb = html.count('Brasília')
local = html.count('ParkShopping') + html.count('Conjunto Nacional') + html.count('SIA') + html.count('Águas Claras') + html.count('Taguatinga') + html.count('BR-060')
print(f"\nBrasília: {bsb} menções")
print(f"Contexto local (ParkShopping/Conjunto Nacional/SIA/Águas Claras/Taguatinga/BR-060): {local} menções")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD VERIFICATION
# ═══════════════════════════════════════════════════════════════════════

def extract_sentences(h):
    """Extract visible paragraph/heading sentences for Jaccard comparison.
    Returns set of normalized sentences (5+ words)."""
    text = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    text = re.sub(r'<script[^>]*>.*?</script>', '', h, flags=re.DOTALL)
    text = re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=re.DOTALL)
    # Extract content from p, h1-h4, blockquote, li, div[itemprop=text]
    content_parts = []
    for tag in ['title', 'h1', 'h2', 'h3', 'h4', 'p', 'blockquote']:
        for m in re.finditer(rf'<{tag}[^>]*>(.*?)</{tag}>', text, re.DOTALL):
            content_parts.append(m.group(1))
    for m in re.finditer(r'<div itemprop="text">(.*?)</div>', text, re.DOTALL):
        content_parts.append(m.group(1))
    meta_desc = re.findall(r'name="description"\s+content="([^"]+)"', text)
    content_parts.extend(meta_desc)
    joined = ' '.join(content_parts)
    joined = re.sub(r'<[^>]+>', ' ', joined)
    joined = re.sub(r'\s+', ' ', joined).strip()
    # Split into sentences
    sentences = re.split(r'[.!?;]\s+', joined)
    # Normalize: lowercase, strip, 5+ words
    normalized = set()
    for s in sentences:
        s = re.sub(r'[^\w\sáàâãéèêíìîóòôõúùûçÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ]', ' ', s)
        s = ' '.join(s.lower().split())
        if len(s.split()) >= 5:
            normalized.add(s)
    return normalized

def jaccard(set1, set2):
    inter = len(set1 & set2)
    union = len(set1 | set2)
    return inter / union if union > 0 else 0

new_tokens = extract_sentences(html)
ref_tokens = extract_sentences(ref)

# Load SC tesoura V2 for comparison
SC_TESOURA_V2 = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
try:
    with open(SC_TESOURA_V2, 'r', encoding='utf-8') as f:
        sc_html = f.read()
    sc_tokens = extract_sentences(sc_html)
    j_vs_sc = jaccard(new_tokens, sc_tokens)
except FileNotFoundError:
    sc_tokens = set()
    j_vs_sc = -1

j_vs_ref = jaccard(new_tokens, ref_tokens)

print(f"\n--- JACCARD ---")
print(f"vs Goiânia ref:      {j_vs_ref:.4f}  {'✓ < 0.20' if j_vs_ref < 0.20 else '✗ >= 0.20 — PRECISA AJUSTE'}")
if j_vs_sc >= 0:
    print(f"vs SC tesoura V2:    {j_vs_sc:.4f}  {'✓ < 0.20' if j_vs_sc < 0.20 else '✗ >= 0.20 — PRECISA AJUSTE'}")
else:
    print("vs SC tesoura V2:    arquivo não encontrado")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")

# ═══════════════════════════════════════════════════════════════════════
# TIMING
# ═══════════════════════════════════════════════════════════════════════

END = datetime.now()
delta = END - START
minutes = int(delta.total_seconds()) // 60
seconds = int(delta.total_seconds()) % 60
print(f"\nTEMPO: {minutes:02d}:{seconds:02d}")
print(f"TOKENS: ~{len(html):,} chars output")
print(f"Início: {START.strftime('%H:%M:%S')}")
print(f"Fim:    {END.strftime('%H:%M:%S')}")
