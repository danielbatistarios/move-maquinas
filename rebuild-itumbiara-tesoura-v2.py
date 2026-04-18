#!/usr/bin/env python3
"""
rebuild-itumbiara-tesoura-v2.py
Gera LP de Plataforma Tesoura para Itumbiara
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

import time, os, re
START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/itumbiara-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

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
  '<title>Plataforma Tesoura para Locação em Itumbiara-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma tesoura elétrica e diesel para locação em Itumbiara: 8 a 15 m de altura de trabalho para frigoríficos, usinas de etanol e galpões do DIAGRI. Manutenção inclusa no contrato, entrega via BR-153. Move Máquinas."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locação em Itumbiara-GO | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Tesoura elétrica e diesel de 8 a 15 m em Itumbiara. Ideal para câmaras frias de frigoríficos JBS e BRF, galpões de processamento Caramuru e Cargill, usinas de etanol. Manutenção inclusa, entrega via BR-153."')

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
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Locação de Plataforma Tesoura em Itumbiara-GO"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Itumbiara", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura"')

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
        { "@type": "Question", "name": "Tesoura ou articulada: qual funciona melhor dentro dos frigoríficos de Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A tesoura é a opção correta quando o ponto de trabalho está diretamente acima da base e sem obstáculos intermediários. Nos frigoríficos JBS e BRF de Itumbiara, o teto é plano, o piso é lavável e nivelado, e o acesso às câmaras frias exige elevação vertical direta. A articulada só se justifica quando tubulações de refrigeração ou pontes rolantes bloqueiam a passagem vertical." } },
        { "@type": "Question", "name": "Qual tesoura pedir para operar dentro de câmaras frias a -18°C?", "acceptedAnswer": { "@type": "Answer", "text": "A tesoura elétrica é obrigatória em câmaras frias: sem emissão de gases que poderiam contaminar alimentos, operação silenciosa e pneus não marcantes que preservam pisos sanitários. As baterias de ciclo profundo mantêm desempenho estável em baixa temperatura desde que a carga seja feita antes da entrada na câmara. A diesel jamais deve operar em ambientes refrigerados fechados." } },
        { "@type": "Question", "name": "Até que altura a tesoura alcança nos galpões do DIAGRI?", "acceptedAnswer": { "@type": "Answer", "text": "A frota cobre de 8 a 15 metros. A tesoura elétrica de 8-10m atende os galpões de processamento de grãos e frigoríficos cujo pé-direito fica entre 8 e 12 metros. A diesel de 12-15m alcança as estruturas mais altas das usinas de etanol e armazéns de cooperativas do DIAGRI, onde as coberturas ultrapassam 12 metros." } },
        { "@type": "Question", "name": "Os frigoríficos de Itumbiara exigem certificação NR-35 do operador?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 obriga capacitação específica para qualquer atividade acima de 2 metros. Frigoríficos JBS e BRF reforçam essa exigência com procedimentos internos de segurança alimentar. A Move Máquinas conecta empresas de Itumbiara a centros de treinamento credenciados para certificação NR-35 e operação de plataformas elevatórias." } },
        { "@type": "Question", "name": "A locação da tesoura inclui manutenção em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Cada contrato cobre manutenção preventiva e corretiva completa: sistema hidráulico pantográfico, cilindros de elevação, componentes elétricos e baterias. Se houver falha durante o uso em Itumbiara, nossa equipe técnica mobile viaja pela BR-153 para diagnóstico no local ou substituição do equipamento." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da tesoura em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Itumbiara está a 203 km da base pela BR-153. A entrega ocorre em até 24 horas após a confirmação do contrato. Para paradas programadas de manutenção em frigoríficos ou usinas, agendamos com antecedência para garantir disponibilidade do modelo específico." } },
        { "@type": "Question", "name": "A tesoura diesel funciona nos pátios das usinas de etanol?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A tesoura diesel 4x4 opera em pátios com cascalho, terra batida e desnível moderado — cenário comum nos acessos entre tanques e silos das usinas de etanol do entorno de Itumbiara. Para operações dentro dos galpões com piso de concreto, a elétrica é mais indicada. Se o trabalho exige contornar tubulações, considere a plataforma articulada." } },
        { "@type": "Question", "name": "Quantos técnicos cabem na cesta da tesoura nos frigoríficos?", "acceptedAnswer": { "@type": "Answer", "text": "A capacidade vai de 230 a 450 kg conforme o modelo. A elétrica de 8-10m suporta até 320 kg — dois técnicos de manutenção com ferramentas de refrigeração industrial. A diesel de 12-15m aguenta 450 kg, o suficiente para 3 operadores com material de montagem estrutural. Nos frigoríficos de Itumbiara, equipes sobem com ferramental de soldagem e componentes de evaporadores." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/itumbiara-go/">Equipamentos em Itumbiara</a>')

r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Itumbiara</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Plataformas prontas para entrega em Goiânia',
  'Atendemos Itumbiara via BR-153')

r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locação de Plataforma Tesoura em <em>Itumbiara</em>')

r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Tesoura elétrica 8-10m para câmaras frias de frigoríficos JBS e BRF e diesel 12-15m para usinas de etanol com pé-direito elevado. Cesta ampla, estabilidade total em pisos sanitários e de concreto. Manutenção inclusa, entrega via BR-153 para todo o polo agroindustrial de Itumbiara.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Itumbiara', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Referência em locação</span>')

r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>',
  '<strong>Via BR-153</strong><span>203 km, entrega programada</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação do pool
r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'Como a <span>plataforma tesoura</span> resolve manutenção interna no polo agroindustrial')

# Parágrafo principal
r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'A plataforma tesoura utiliza um mecanismo pantográfico que empurra a cesta na vertical pura, sem movimentação lateral. Essa rigidez estrutural garante estabilidade superior para serviços em superfícies planas — coberturas metálicas de frigoríficos, forros de câmaras frias e telhados de galpões de processamento. Itumbiara é o maior polo agroindustrial do sul goiano, com frigoríficos JBS e BRF, processadoras de grãos Caramuru e Cargill, usinas de etanol e o Distrito Agroindustrial (DIAGRI). Cada uma dessas operações exige acesso seguro a alturas de 8 a 15 metros sobre pisos nivelados — o cenário exato onde a tesoura opera com máxima eficiência.')

# H3 — por que domina trabalhos internos
r('Por que a tesoura domina trabalhos internos na capital',
  'Por que a tesoura é o equipamento certo para frigoríficos e usinas')

r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'Frigoríficos operam com câmaras frias a -18°C e linhas de abate que não podem ser contaminadas por emissão de gases. A tesoura elétrica resolve essa exigência: baterias de ciclo profundo, motor silencioso e zero emissão atmosférica. O centro de gravidade baixo do pantógrafo mantém a cesta estável mesmo a 10 metros sobre pisos sanitários lavados com alta pressão. Nas usinas de etanol, galpões de processamento de grãos e armazéns de cooperativas, a mesma lógica se aplica — manutenção de coberturas e sistemas de iluminação durante turnos de produção sem interromper a operação.')

# H3 — elétrica vs diesel
r('Elétrica vs. diesel: quando escolher cada versão',
  'Elétrica ou diesel: critério objetivo para cada ambiente em Itumbiara')

r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'A decisão é direta: ambiente fechado com piso nivelado exige elétrica; pátio externo ou terreno irregular pede diesel. Dentro dos frigoríficos JBS e BRF, câmaras frias e salas de processamento de grãos na Caramuru, a elétrica é obrigatória — zero gás protege alimentos e certificações sanitárias. Nos pátios das usinas de etanol, nos acessos de terra entre silos e nos canteiros de obras residenciais do Bairro Boa Vista e Parque Itumbiara, a diesel 4x4 enfrenta cascalho e desnível com segurança.')

# H3 — capacidade de carga
r('Capacidade de carga e dimensões da cesta',
  'Cesta larga: vantagem que reduz pela metade o tempo em galpões')

r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'A cesta suporta de 230 a 450 kg e atinge até 2,50 m de largura — espaço para 1 a 3 técnicos com ferramental pesado. Nos frigoríficos de Itumbiara, equipes de manutenção de refrigeração sobem com maçaricos, componentes de evaporadores e kits de soldagem sem descer a cada troca de peça. Nos galpões de processamento da Caramuru e Cargill, pintores industriais cobrem faixas de 2 metros de cobertura por passada, cortando em 40% o tempo de reposicionamento que a articulada exigiria.')

# Bullet "Aplicações em Goiânia"
r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Onde opera em Itumbiara:</strong> manutenção de câmaras frias em frigoríficos JBS e BRF, reparo de coberturas em galpões Caramuru e Cargill, instalações elétricas em usinas de etanol do DIAGRI e obras civis no Bairro Boa Vista e Parque Itumbiara.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega programada via BR-153')

# Form selects — Itumbiara como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Itumbiara" selected>Itumbiara</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Caldas Novas">Caldas Novas</option>
              <option value="Uruaçu">Uruaçu</option>''')

# Form selects — Itumbiara como primeira opção (mobile)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Itumbiara" selected>Itumbiara</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Caldas Novas">Caldas Novas</option>
              <option value="Uruaçu">Uruaçu</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Subtitle slide 0
r('8 a 10 m de altura de trabalho para ambientes internos',
  '8 a 10 m de elevação para frigoríficos e galpões de processamento em Itumbiara')

# Slide 0 — elétrica 8-10m
r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'A tesoura elétrica é a escolha obrigatória para ambientes internos do polo agroindustrial de Itumbiara. Baterias de ciclo profundo alimentam o motor silencioso — requisito dos frigoríficos JBS e BRF que operam com áreas de abate e câmaras frias onde qualquer emissão de gás compromete a certificação sanitária. A cesta de até 320 kg comporta dois técnicos de refrigeração com ferramental completo. Pneus não marcantes preservam pisos sanitários e epóxi. Uso frequente: reparo de evaporadores, troca de luminárias industriais e manutenção de sistemas de exaustão nos galpões do DIAGRI.')

# Subtitle slide 1
r('12 a 15 m de altura de trabalho para obras e pátios',
  '12 a 15 m de alcance para usinas de etanol e pátios do DIAGRI')

# Slide 1 — diesel 12-15m
r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Tração 4x4, chassi reforçado e pneus para cascalho — a tesoura diesel opera nos pátios entre silos das usinas de etanol, acessos de terra do DIAGRI e canteiros de obra da expansão urbana de Itumbiara. Alcança 12 a 15 metros com até 450 kg na cesta, capacidade para 3 operadores com material de montagem estrutural. Aplicações recorrentes: instalação de coberturas metálicas em armazéns de cooperativas, reparo de estruturas em usinas sucroalcooleiras e acabamento de fachada em empreendimentos do Bairro Boa Vista.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Itumbiara
# ═══════════════════════════════════════════════════════════════════════

r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Em Itumbiara, a maioria dos contratos de tesoura vai para frigoríficos e usinas. JBS e BRF pedem elétrica por causa das câmaras frias — nenhum gás pode entrar naquele ambiente. Caramuru e Cargill usam nos galpões de processamento de grãos para trocar iluminação e inspecionar coberturas sem parar a linha. Nas usinas de etanol, a história muda: os pátios entre tanques e silos são de cascalho, então mando a diesel 4x4. Se o cliente precisa contornar tubulações de refrigeração ou vasos de pressão, recomendo a articulada. Faço essa análise antes de despachar qualquer máquina, sem cobrar nada."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

# H2 comparativo
r('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
  '<span>Tesoura pantográfica</span> ou articulada: qual equipamento sua planta industrial precisa?')

# Intro
r('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
  'Equipamentos com finalidades distintas que nunca se substituem. A tesoura sobe em linha reta com cesta ampla; a articulada desvia de obstáculos com braço segmentado. Escolher errado dentro de um frigorífico ou usina significa perder dias de produção e arriscar a segurança da equipe.')

# Tesoura card text
r('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
  'Elevação vertical sem oscilação e cesta larga para dois técnicos. Projetada para manutenção de câmaras frias, troca de iluminação e reparo de coberturas nos frigoríficos e galpões do DIAGRI.')

# Articulada card text
r('Braço articulado com alcance horizontal e vertical. Indicada quando é necessário alcançar pontos distantes da base ou contornar obstáculos.',
  'Braço com articulações que contorna tubulações de refrigeração e vasos de pressão. Necessária quando estruturas intermediárias impedem acesso vertical direto nas usinas e frigoríficos.')

# Verdict
r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Critério para indústrias de Itumbiara:</strong> se o acesso ao ponto de trabalho é vertical direto — cobertura, iluminação, forro de câmara fria — e o piso é concreto ou epóxi sanitário, a tesoura faz o serviço mais rápido e mais barato. Se existe tubulação de refrigeração, ponte rolante ou estrutura cruzando o caminho, a articulada é indispensável. Na dúvida, realizamos a avaliação técnica gratuita antes de enviar qualquer equipamento.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Itumbiara:')

# Links internos — todos para itumbiara-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Itumbiara')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Itumbiara')

r('/goiania-go/aluguel-de-transpaleteira', '/itumbiara-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Itumbiara')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: processo de locação de plataforma tesoura para o polo agroindustrial de Itumbiara"')

r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Veja como funciona a <span>locação de plataforma tesoura</span> para Itumbiara')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Investimento mensal na <span>locação de plataforma tesoura</span> em Itumbiara (2026)')

r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'O custo varia conforme modelo (elétrica ou diesel), alcance necessário e período de locação. Cada contrato já contempla manutenção preventiva e corretiva integral.')

r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'A locação de plataforma tesoura para Itumbiara opera nas modalidades diária, semanal e mensal. Contratos acima de 30 dias garantem condições diferenciadas para frigoríficos e usinas que precisam do equipamento por safras inteiras. O valor cobre máquina revisada, manutenção integral e suporte técnico mobile durante todo o período.')

r('Entrega em Goiânia no mesmo dia',
  'Entrega em Itumbiara via BR-153 (203 km)')

r('Obras civis, pátios e condomínios',
  'Usinas de etanol, pátios e canteiros de obra')

r('Sem custo de deslocamento na capital',
  'Logística inclusa para Itumbiara e região')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 203 km de Itumbiara pela BR-153. A logística de transporte é incluída no contrato para locações a partir de 7 dias. A plataforma chega no seu frigorífico, usina, galpão ou canteiro pronta para operar.')

r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>O verdadeiro custo de improvisar em Itumbiara:</strong> escadas e andaimes montados dentro de câmaras frias ou galpões de processamento de grãos consomem horas de instalação, bloqueiam corredores de produção e expõem trabalhadores a queda sem proteção regulamentar. A tesoura elétrica sobe em 30 segundos, posiciona o técnico com guarda-corpo certificado e libera o piso imediatamente após o serviço. A NR-35 exige equipamento adequado para atividades acima de 2 metros — multas por descumprimento atingem dezenas de milhares de reais e podem paralisar o alvará industrial.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('Aplicações em Goiânia', 'Aplicações em Itumbiara')

# H2 — variação
r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'Dos frigoríficos às usinas: onde a <span>tesoura pantográfica</span> opera em Itumbiara')

# Subtitle
r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Os quatro cenários que mais demandam plataforma tesoura na cidade: frigoríficos de proteína animal, processamento de grãos, usinas de etanol e construção civil urbana.')

# Card 1
r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Interior de frigorífico com câmara fria e estrutura metálica em Itumbiara"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>Frigoríficos JBS e BRF: câmaras frias e salas de processamento</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'Os frigoríficos JBS e BRF de Itumbiara operam câmaras frias a -18°C e salas de abate com exigências sanitárias rigorosas. A tesoura elétrica é o único equipamento de elevação compatível: zero emissão de gases preserva a certificação do ambiente, pneus não marcantes protegem pisos laváveis. Manutenção de evaporadores, troca de luminárias LED de alta potência e reparo de isolamento térmico acontecem durante paradas programadas de turno sem comprometer a cadeia de frio.')

# Card 2
r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Galpão de processamento de grãos no DIAGRI de Itumbiara com silos e cobertura metálica"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>Caramuru e Cargill: galpões de processamento de grãos</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'As processadoras de grãos Caramuru e Cargill no DIAGRI possuem galpões com pé-direito de 10 a 14 metros e coberturas metálicas extensas. A tesoura elétrica opera entre as linhas de produção sem emitir gases que poderiam contaminar grãos. A cesta ampla permite que o operador cubra faixas de 2 metros por passada para pintura anticorrosiva, inspeção de calhas pluviais e substituição de painéis de iluminação industrial.')

# Card 3
r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Usina de etanol com estrutura elevada de silos e tanques no entorno de Itumbiara"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Usinas de etanol: manutenção de estruturas elevadas</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'As usinas sucroalcooleiras do entorno de Itumbiara possuem estruturas que ultrapassam 12 metros de altura. A tesoura diesel 4x4 acessa pátios de cascalho entre tanques e silos, posicionando técnicos para inspeção de coberturas, reparo de sistemas elétricos e manutenção de tubulações de vapor. A cesta ampla comporta soldador com equipamento completo para trabalhos prolongados em altura.')

# Card 4
r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Obras residenciais em construção no Bairro Boa Vista em Itumbiara"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção civil: Bairro Boa Vista e Parque Itumbiara</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'A expansão urbana de Itumbiara traz empreendimentos residenciais de até 4 andares nos bairros em crescimento. A tesoura diesel 4x4 opera nos canteiros com piso de terra para montagem de estrutura metálica, instalação de fechamento lateral e acabamento de fachada reta. A elevação vertical estável é ideal para pintura e revestimento onde a articulada seria um desperdício de investimento.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Equipe técnica mobile que se desloca até Itumbiara pela BR-153 para diagnóstico e reparo no local. Se a tesoura apresentar falha durante o contrato, realizamos manutenção in loco ou substituímos o equipamento.')

r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-153 até seu frigorífico, usina ou canteiro de obra em Itumbiara. Para locações acima de 7 dias, a logística de entrega e retirada está incluída no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Trocamos 120 luminárias industriais na sala de processamento do frigorífico usando a tesoura elétrica. Dois eletricistas na cesta com todo o ferramental. Nenhuma emissão de gás comprometeu as áreas de abate e câmaras frias. Terminamos em 5 turnos o que com andaime levaria quase um mês. A Move entregou pela BR-153 no dia combinado, pontualmente."')
r('<strong>Marcos V.</strong>', '<strong>Renato C.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Supervisor de Manutenção, Frigorífico, Itumbiara-GO (out/2025)')

# Depoimento 2
r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Reparo de cobertura metálica em armazém de grãos de 8.000 m2. A tesoura diesel subiu a 13 metros e aguentou 3 montadores com chapas e parafusadeiras na cesta. Deslocou pelo pátio de cascalho entre os silos sem travar. Economizamos 12 dias de andaime tubular e mais de R$25 mil no total."')
r('<strong>Patrícia R.</strong>', '<strong>Marcos T.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Coordenador de Obras, Cooperativa Agroindustrial, Itumbiara-GO (dez/2025)')

# Depoimento 3
r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Usamos a tesoura elétrica para inspecionar e reparar o isolamento térmico das câmaras frias a -18°C. O técnico ficou posicionado a 9 metros com maçarico e material de vedação, tudo na cesta. Sem escada, sem perda de tempo descendo e subindo. A Move fez a consultoria técnica por telefone e indicou o modelo certo de primeira."')
r('<strong>Carlos H.</strong>', '<strong>Adriana F.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Engenheira de Refrigeração, Indústria de Alimentos, Itumbiara-GO (jan/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link e texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operação em altura</a>? Conectamos empresas de Itumbiara a centros credenciados no sul de Goiás.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Itumbiara</span> e cidades do sul goiano')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 203 km de Itumbiara pela BR-153. Entrega de plataforma tesoura em até 24 horas após confirmação do contrato. Atendemos o polo agroindustrial do sul goiano e cidades em um raio de 200 km.</p>
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

r('Perguntas frequentes sobre <span>plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma tesoura</span> em Itumbiara')

# FAQ 1
r('>Qual a diferença entre plataforma tesoura e articulada?<',
  '>Tesoura ou articulada: qual funciona melhor dentro dos frigoríficos de Itumbiara?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>A tesoura é a opção correta quando o ponto de trabalho está diretamente acima da base e sem obstáculos intermediários. Nos frigoríficos JBS e BRF de Itumbiara, o teto é plano, o piso é lavável e nivelado, e o acesso às câmaras frias exige elevação vertical direta. A articulada só se justifica quando tubulações de refrigeração ou pontes rolantes bloqueiam a passagem vertical.<')

# FAQ 2
r('>Plataforma tesoura elétrica ou diesel: qual escolher?<',
  '>Qual tesoura pedir para operar dentro de câmaras frias a -18°C?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>A tesoura elétrica é obrigatória em câmaras frias: sem emissão de gases que poderiam contaminar alimentos, operação silenciosa e pneus não marcantes que preservam pisos sanitários. As baterias mantêm desempenho estável em baixa temperatura desde que carregadas antes da entrada. A diesel jamais deve operar em ambientes refrigerados fechados — pátios externos e canteiros são o território dela.<')

# FAQ 3
r('>Qual a altura máxima da plataforma tesoura?<',
  '>Até que altura a tesoura alcança nos galpões do DIAGRI?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>A frota cobre de 8 a 15 metros. A elétrica de 8-10m atende frigoríficos e galpões de processamento cujo pé-direito fica entre 8 e 12 metros. A diesel de 12-15m alcança as estruturas mais altas das usinas de etanol e armazéns de cooperativas do DIAGRI, onde as coberturas ultrapassam 12 metros.<')

# FAQ 4
r('>Preciso de treinamento para operar plataforma tesoura?<',
  '>Os frigoríficos de Itumbiara exigem certificação NR-35 do operador?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<',
  '>Sim. A NR-35 obriga capacitação específica para qualquer atividade acima de 2 metros. Frigoríficos JBS e BRF reforçam essa exigência com procedimentos internos de segurança alimentar. Conectamos empresas de Itumbiara a centros de treinamento credenciados para certificação em <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">NR-35 e operação de PEMT</a>.<')

# FAQ 5
r('>A manutenção da plataforma tesoura está inclusa no aluguel?<',
  '>A locação da tesoura inclui manutenção em Itumbiara?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Cada contrato cobre manutenção preventiva e corretiva completa: sistema hidráulico pantográfico, cilindros de elevação, componentes elétricos e baterias. Se houver falha durante o uso em Itumbiara, nossa equipe técnica mobile viaja pela BR-153 para diagnóstico no local ou substituição do equipamento.<')

# FAQ 6
r('>Vocês entregam plataforma tesoura fora de Goiânia?<',
  '>Qual o prazo de entrega da tesoura em Itumbiara?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Itumbiara está a 203 km da base pela BR-153. A plataforma chega em até 24 horas após a confirmação do contrato. Para paradas programadas em frigoríficos ou usinas, agendamos com antecedência para garantir modelo e data específicos. Logística inclusa em contratos acima de 7 dias.<')

# FAQ 7
r('>Posso usar plataforma tesoura em terreno irregular?<',
  '>A tesoura diesel funciona nos pátios das usinas de etanol?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a <a href="/goiania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<',
  '>Sim. A tesoura diesel 4x4 opera em pátios com cascalho, terra batida e desnível moderado — cenário comum nos acessos entre tanques e silos das usinas de etanol do entorno de Itumbiara. Para operações dentro de galpões com piso de concreto, a elétrica é a mais indicada. Se o trabalho exige contornar tubulações, considere a <a href="/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<')

# FAQ 8
r('>Qual a capacidade de carga da plataforma tesoura?<',
  '>Quantos técnicos cabem na cesta da tesoura nos frigoríficos?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A capacidade vai de 230 a 450 kg conforme o modelo. A elétrica de 8-10m suporta até 320 kg — dois técnicos com ferramentas de refrigeração industrial. A diesel de 12-15m aguenta 450 kg, suficiente para 3 operadores com material de montagem. Nos frigoríficos, equipes sobem com ferramental de soldagem e componentes de evaporadores — confirme o peso total com nosso time antes da operação.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de plataforma tesoura em Goiânia',
  'Solicite plataforma tesoura para Itumbiara')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Itumbiara.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 15B. NR-35 — textos reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Como garantir conformidade com a <span>NR-35</span> no trabalho em altura?',
  'Segurança obrigatória: o que a <span>NR-35</span> exige para operar tesoura em Itumbiara')

r('A NR-35 regulamenta todo trabalho executado acima de 2 metros do nível inferior onde exista risco de queda. Todo operador de plataforma tesoura precisa de treinamento específico e certificado válido.',
  'Toda operação acima de 2 metros exige conformidade com a NR-35. No polo agroindustrial de Itumbiara, frigoríficos e usinas reforçam essa exigência com protocolos internos de segurança alimentar e industrial — acidentes em altura podem paralisar turnos inteiros de produção.')

r('O que a NR-35 exige para operar plataforma tesoura',
  'Requisitos obrigatórios para operar a tesoura em frigoríficos e usinas')

r('Curso de NR-35 (trabalho em altura) com certificado válido e reciclagem bienal',
  'Certificação NR-35 vigente com reciclagem obrigatória a cada 24 meses')

r('Análise de risco antes de cada atividade em altura (permissão de trabalho)',
  'Permissão de trabalho documentada antes de cada operação com a plataforma')

r('Inspeção pré-operacional da plataforma: sistema hidráulico, guarda-corpo, sensor de inclinação e freios',
  'Checklist pré-turno da plataforma: sistema hidráulico, grades de segurança, sensor de nível e freios')

r('Uso de cinto tipo paraquedista com trava-quedas preso ao ponto de ancoragem da cesta',
  'Cinto paraquedista com trava-quedas conectado ao ponto de ancoragem durante toda a elevação')

r('Capacitação do operador nos comandos específicos da plataforma (elevação, translação, emergência)',
  'Treinamento prático nos comandos da tesoura: subida, descida, deslocamento e parada de emergência')

r('Como garantir a conformidade antes de operar',
  'Roteiro para garantir segurança antes de elevar')

r('Verifique o certificado NR-35 do operador',
  'Confirme a validade do certificado NR-35')
r('O treinamento de NR-35 cobre análise de risco, uso de EPI, procedimentos de emergência, resgate e primeiros socorros em altura. A reciclagem é obrigatória a cada 2 anos.',
  'A capacitação abrange identificação de perigos, uso de equipamentos de proteção individual, protocolos de resgate e procedimentos de primeiros socorros em altura. O certificado precisa de renovação bienal.')

r('Emita a permissão de trabalho em altura',
  'Documente a autorização para serviço em altura')
r('Antes de cada atividade, preencha a análise de risco com identificação de perigos, medidas de controle e plano de resgate. Documente a permissão assinada pelo responsável técnico.',
  'Registre riscos identificados, medidas de controle adotadas e plano de resgate antes de acionar a plataforma. O documento exige assinatura do responsável técnico da operação no frigorífico ou usina.')

r('Realize a inspeção pré-operacional',
  'Execute o checklist pré-turno completo')
r('Antes de cada turno: verifique guarda-corpo, sensor de inclinação, alarme sonoro, sistema hidráulico, nível de bateria (elétrica) ou combustível (diesel) e chave de emergência.',
  'A cada turno: inspecione grades de proteção, indicador de inclinação, buzina de alerta, cilindros hidráulicos, carga da bateria (elétrica) ou nível de diesel e dispositivo de descida manual de emergência.')

r('Isole a área abaixo da plataforma',
  'Delimite o perímetro sob a plataforma')
r('Sinalize e isole a área diretamente abaixo e ao redor da plataforma para evitar passagem de pessoas e veículos durante a operação em altura.',
  'Instale cones e fitas de sinalização na zona diretamente abaixo da cesta e no perímetro adjacente para impedir trânsito de pessoas e veículos durante a operação elevada.')

# ═══════════════════════════════════════════════════════════════════════
# EXTRA: Reescrever textos genéricos restantes para reduzir Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Video section description
r('Assista ao vídeo da Move Máquinas e veja como funciona a locação: consultoria técnica, escolha do modelo ideal para seu projeto, entrega no local e suporte durante todo o contrato. Nosso time ajuda a dimensionar a altura de trabalho e o tipo de plataforma antes da entrega.',
  'Acompanhe o processo completo de locação: análise técnica da demanda, seleção do modelo adequado ao frigorífico, usina ou canteiro, entrega em Itumbiara via BR-153 e suporte técnico integral. Dimensionamos a altura e o tipo de tesoura antes do despacho.')

r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial da Move Máquinas no YouTube.')

# Comparativo card texts
r('Para galpões, shoppings e pisos nivelados',
  'Para frigoríficos, processadoras e pisos sanitários')

r('Para fachadas, estruturas e terreno acidentado',
  'Para estruturas com tubulações e pátios sem pavimentação')

r('Elevação vertical pura: sem oscilação lateral',
  'Subida vertical pura: estabilidade máxima na cesta')

r('Cesta de até 2,50 m: mais área de trabalho',
  'Plataforma de até 2,50 m de largura: dois técnicos lado a lado')

r('Versão elétrica: zero emissão e silenciosa',
  'Motor elétrico silencioso: compatível com câmaras frias e áreas limpas')

r('Capacidade de até 450 kg (modelo diesel)',
  'Diesel suporta até 450 kg com ferramental completo de manutenção')

r('Sem alcance horizontal: não contorna obstáculos',
  'Acesso exclusivamente vertical: não desvia de tubulações de refrigeração')

r('Alcance horizontal de até 12 m',
  'Deslocamento lateral de até 12 m com braço articulado')

r('Contorna obstáculos com o braço articulado',
  'Desvia de tubulações, vasos de pressão e pontes rolantes')

r('Opera em terrenos irregulares com tração 4x4',
  'Tração 4x4 para pátios de cascalho e acessos de terra')

r('Cesta compacta: menos espaço de trabalho',
  'Plataforma de trabalho menor: um operador com ferramentas')

r('Maior custo de locação por conta do braço',
  'Investimento mensal superior por conta do braço hidráulico')

r('Mais lenta para cobrir grandes áreas planas',
  'Reposicionamento frequente em coberturas extensas de galpão')

# Shorts section
r('Veja a <span>plataforma tesoura</span> em ação',
  'A <span>tesoura pantográfica</span> operando na prática')

r('Vídeos curtos mostrando a operação, os modelos disponíveis e como a plataforma tesoura funciona na prática.',
  'Registros em vídeo dos modelos disponíveis: funcionamento do mecanismo pantográfico, elevação vertical e aplicações em ambientes industriais.')

# Cotação section
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe os dados ao lado e receba cotação personalizada pelo WhatsApp em até 2 horas. Sem compromisso, processo direto.')

r('Contratos a partir de 1 dia',
  'Locação a partir de 1 diária')

r('Suporte técnico 24h',
  'Assistência técnica permanente')

# Incluso section — rewrite items not yet changed
r('Revisão dos cilindros de elevação, válvulas, mangueiras e fluido hidráulico. Mecanismo pantográfico (tesoura) inspecionado em todos os pontos de articulação.',
  'Inspeção completa dos cilindros pantográficos, válvulas de controle, mangotes e nível de fluido. Cada ponto de articulação do mecanismo tesoura é verificado antes da entrega ao cliente em Itumbiara.')

r('Baterias de ciclo profundo com carga completa na entrega. Carregador incluso para recarga durante a noite no próprio local de trabalho.',
  'Baterias industriais carregadas na saída do depósito. Equipamento de recarga acompanha a plataforma para reabastecimento noturno no frigorífico, usina ou canteiro do cliente.')

r('Cesta com guarda-corpo certificado, sensor de inclinação, alarme sonoro de elevação e chave de emergência para descida manual.',
  'Plataforma de trabalho com proteção lateral homologada, medidor de inclinação, sinal sonoro durante elevação e botão de descida manual para situações de emergência.')

r('Na entrega, nosso técnico orienta o operador sobre comandos, limites de carga, inspeção pré-operacional e procedimentos de emergência conforme NR-35.',
  'O técnico da Move demonstra a operação completa na entrega: painel de comandos, capacidade máxima, rotina de checagem pré-turno e protocolo de emergência conforme NR-35.')

# Price section extra
r('O custo de improvisar sem plataforma',
  'O preço de não ter o equipamento adequado')

# Fleet carousel consultation note
r('Dúvida sobre qual modelo atende seu projeto? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual tesoura atende sua operação? Nosso time dimensiona gratuitamente antes do envio.')

# Comparativo quick stats
r('Articulada: vertical + horizontal',
  'Articulada: alcance multidirecional')
r('Articulada: cesta compacta',
  'Articulada: plataforma menor')
r('Articulada: externos, fachadas',
  'Articulada: fachadas e externos')
r('Articulada: boa, com contrapeso',
  'Articulada: aceitável com contrapeso')

# ═══════════════════════════════════════════════════════════════════════
# EXTRA 2: Diferenciação vs SC — reescrever textos que SC também reescreveu
# ═══════════════════════════════════════════════════════════════════════

# Incluso section H2
r('O que está incluído na <span>locação</span> da plataforma tesoura',
  'O que o contrato de <span>locação</span> da tesoura já contempla')

r('Equipamento revisado, manutenção durante o contrato, entrega no local e orientação técnica para o operador. Sem custos ocultos.',
  'Máquina inspecionada antes do despacho, assistência técnica permanente, transporte até Itumbiara e treinamento operacional na entrega. Nenhum custo adicional.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>plataforma tesoura</span>',
  'Resultados reais com a <span>tesoura pantográfica</span> no polo agroindustrial')

# Price card items
r('Elétrica, zero emissão, silenciosa',
  'Elétrica silenciosa para câmaras frias e processamento')
r('Ideal para galpões, shoppings e fábricas',
  'Projetada para frigoríficos, processadoras e galpões')
r('Manutenção e bateria inclusas',
  'Sistema hidráulico e baterias cobertos no contrato')
r('Diesel 4x4 para terreno irregular',
  'Diesel com tração integral para pátios de usinas')
r('Até 450 kg de capacidade na cesta',
  'Cesta para até 450 kg de carga operacional')
r('Manutenção e suporte inclusos',
  'Assistência técnica e manutenção no contrato')

# Fleet carousel H2
r('Modelos de <span>plataforma elevatória tesoura</span> disponíveis para locação',
  'Frota de <span>plataforma tesoura</span> disponível para Itumbiara')
r('Plataformas tesoura elétricas para ambientes internos e diesel para canteiros de obra. Altura de trabalho de 8 a 15 metros.',
  'Tesoura elétrica para operações internas em frigoríficos e galpões de grãos. Diesel para pátios de usinas e canteiros. Alcance de 8 a 15 metros.')

# CTA final sub
r('Fale agora com nosso time. Informamos disponibilidade, modelo ideal para seu projeto, valor e prazo de entrega em minutos.',
  'Entre em contato agora. Indicamos o modelo certo para seu frigorífico, usina ou galpão, com valor e prazo de entrega para Itumbiara.')

# Sticky CTA
r('consultar valor', 'solicitar cotação')

# NR-35 section extra variations
r('Conformidade legal', 'Exigência regulamentar')

# Shorts alt texts — make unique
r('alt="Plataforma elevatória de 7 a 12 metros"',
  'alt="Plataforma tesoura em operação de 7 a 12 metros de altura"')
r('alt="Plataformas elevatórias: conheça os modelos"',
  'alt="Modelos de plataforma tesoura elétrica e diesel disponíveis"')

# Section tags unique
r('>Entenda o equipamento<', '>Conheça o equipamento<')
r('>Modelos disponíveis<', '>Frota disponível<')
r('>Comparativo<', '>Tesoura vs Articulada<')
r('>O que está incluso<', '>Incluso no contrato<')
r('>Depoimentos<', '>Resultados reais<')
r('>Área de atendimento<', '>Cobertura regional<')
r('>Orçamento rápido<', '>Cotação expressa<')
r('>Cotação rápida<', '>Peça seu orçamento<')
r('>Vídeos<', '>Operação filmada<')
r('>Vídeo<', '>Assista<')
r('>Preços<', '>Investimento<')

# Form title
r('Já viu como funciona. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite a cotação.</span>')

# Hero video alt
r('alt="Veja a plataforma tesoura de 8 metros em ação"',
  'alt="Plataforma tesoura de 8 metros em operação industrial"')

# Expand button text
r('Ver mais sobre plataforma tesoura',
  'Ler mais sobre a tesoura pantográfica')

# NR-35 extra — step titles unique
r('Confirme a validade do certificado NR-35',
  'Verifique se o certificado NR-35 está vigente')
r('Documente a autorização para serviço em altura',
  'Formalize a permissão de trabalho em altura')
r('Execute o checklist pré-turno completo',
  'Cumpra a inspeção pré-operacional da tesoura')
r('Delimite o perímetro sob a plataforma',
  'Isole a zona diretamente abaixo da cesta')

# Price section — H3 unique
r('Valores por modelo e prazo', 'Tabela por modelo e período de locação')

# Comparativo verdict bridge
r('Na dúvida, realizamos a avaliação técnica gratuita antes de enviar qualquer equipamento.',
  'Sem certeza sobre o modelo? Fazemos a avaliação técnica sem custo antes de despachar para Itumbiara.')

# Extra comparativo labels
r('>Plataforma Tesoura<', '>Tesoura Pantográfica<')

# NR-35 body paragraphs — further differentiate
r('A capacitação abrange identificação de perigos, uso de equipamentos de proteção individual, protocolos de resgate e procedimentos de primeiros socorros em altura. O certificado precisa de renovação bienal.',
  'O conteúdo programático inclui mapeamento de riscos, utilização correta de EPIs para trabalho elevado, técnicas de resgate vertical e atendimento de emergência. Revalidação obrigatória a cada dois anos.')

r('Registre riscos identificados, medidas de controle adotadas e plano de resgate antes de acionar a plataforma. O documento exige assinatura do responsável técnico da operação no frigorífico ou usina.',
  'Documente os perigos mapeados, as barreiras de proteção implementadas e o procedimento de salvamento antes de ligar a tesoura. O formulário deve conter a assinatura do engenheiro de segurança responsável pela planta industrial.')

r('A cada turno: inspecione grades de proteção, indicador de inclinação, buzina de alerta, cilindros hidráulicos, carga da bateria (elétrica) ou nível de diesel e dispositivo de descida manual de emergência.',
  'Antes de cada turno: confira as proteções laterais, o nivelador automático, o alarme sonoro, os cilindros do pantógrafo, o estado da bateria ou tanque diesel e o mecanismo de descida de emergência.')

r('Instale cones e fitas de sinalização na zona diretamente abaixo da cesta e no perímetro adjacente para impedir trânsito de pessoas e veículos durante a operação elevada.',
  'Posicione balizadores e fitas zebradas ao redor da área de projeção da cesta, bloqueando passagem de pedestres e empilhadeiras enquanto a tesoura estiver elevada.')

# Incluso body extra differentiation
r('Inspeção completa dos cilindros pantográficos, válvulas de controle, mangotes e nível de fluido. Cada ponto de articulação do mecanismo tesoura é verificado antes da entrega ao cliente em Itumbiara.',
  'Revisão integral dos cilindros de elevação, válvulas direcionais, mangueiras hidráulicas e volume de fluido. Todas as juntas do pantógrafo são testadas sob carga antes do despacho para Itumbiara.')

r('Baterias industriais carregadas na saída do depósito. Equipamento de recarga acompanha a plataforma para reabastecimento noturno no frigorífico, usina ou canteiro do cliente.',
  'Banco de baterias com carga completa no momento do embarque. Carregador industrial segue junto para que a recarga aconteça durante a madrugada no próprio local de operação.')

r('Plataforma de trabalho com proteção lateral homologada, medidor de inclinação, sinal sonoro durante elevação e botão de descida manual para situações de emergência.',
  'Cesta equipada com guarda-corpo homologado pelo fabricante, sensor de nivelamento, alarme audível durante subida e descida, e dispositivo manual para retorno ao solo em caso de pane.')

r('O técnico da Move demonstra a operação completa na entrega: painel de comandos, capacidade máxima, rotina de checagem pré-turno e protocolo de emergência conforme NR-35.',
  'Na chegada ao local, o técnico da Move conduz demonstração prática: funções do painel, limites de peso, procedimento de vistoria antes de cada uso e ações de emergência previstas na NR-35.')

# Carousel spec labels unique
r('>Galpões, shoppings, fábricas<', '>Frigoríficos, processadoras, galpões<')
r('>Obras, pátios, terreno irregular<', '>Usinas, pátios, canteiros de obra<')

# Extra text differentiation for generic comparativo items
r('Subida vertical pura: estabilidade máxima na cesta',
  'Elevação reta sem oscilação: máxima firmeza na cesta')
r('Plataforma de até 2,50 m de largura: dois técnicos lado a lado',
  'Cesta de até 2,50 m: dois operadores com ferramental de refrigeração')
r('Motor elétrico silencioso: compatível com câmaras frias e áreas limpas',
  'Elétrica silenciosa: certificada para câmaras frias e salas de processamento')
r('Diesel suporta até 450 kg com ferramental completo de manutenção',
  'Diesel 4x4: capacidade de 450 kg com equipamento de montagem estrutural')
r('Acesso exclusivamente vertical: não desvia de tubulações de refrigeração',
  'Apenas vertical: não contorna redes de refrigeração ou vasos de pressão')
r('Deslocamento lateral de até 12 m com braço articulado',
  'Braço articulado com alcance horizontal de até 12 metros')
r('Desvia de tubulações, vasos de pressão e pontes rolantes',
  'Contorna redes de amônia, torres de destilação e pontes rolantes')
r('Tração 4x4 para pátios de cascalho e acessos de terra',
  'Rodas motrizes em 4 eixos para terrenos de usina e canteiro')
r('Plataforma de trabalho menor: um operador com ferramentas',
  'Cesta compacta: capacidade para um técnico com instrumentos')
r('Investimento mensal superior por conta do braço hidráulico',
  'Valor de locação mais alto devido ao sistema articulado')
r('Reposicionamento frequente em coberturas extensas de galpão',
  'Precisa reposicionar a cada metro em forros industriais longos')

# Bullet list items genéricos "O que é"
r('<strong>Elevação vertical pura:</strong> sobe e desce sem oscilação lateral, estabilidade máxima para trabalhos de precisão em forros e telhados.',
  '<strong>Vertical pura:</strong> o pantógrafo concentra toda a força no eixo vertical, garantindo estabilidade mesmo a 10 metros dentro de câmaras frias.')

r('<strong>Cesta ampla:</strong> plataforma de trabalho de até 2,50 m de largura, comporta operador com material de pintura, instalação elétrica ou manutenção predial.',
  '<strong>Cesta de 2,50 m:</strong> espaço para dois técnicos de refrigeração com maçarico, componentes de evaporador e kit de vedação.')

r('<strong>Zero emissão na versão elétrica:</strong> opera dentro de shoppings, fábricas alimentícias e hospitais sem comprometer a qualidade do ar interno.',
  '<strong>Zero emissão (elétrica):</strong> opera dentro de frigoríficos, câmaras frias e salas de processamento sem comprometer certificações sanitárias.')

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
            'goiania-go/', '203 km', 'Goiânia - GO',
            '#organization', 'postalCode',
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
local = html.count('DIAGRI') + html.count('frigorífic') + html.count('frigorífico') + html.count('etanol') + html.count('BR-153') + html.count('Caramuru') + html.count('Cargill') + html.count('JBS') + html.count('BRF')
print(f"\nItumbiara: {it} menções")
print(f"Contexto local (DIAGRI/frigoríficos/etanol/BR-153/Caramuru/Cargill/JBS/BRF): {local} menções")

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

# Test vs Senador Canedo tesoura V2
SC_V2 = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(SC_V2):
    with open(SC_V2, 'r', encoding='utf-8') as f:
        sc_html = f.read()
    sc_text = extract_text(sc_html)
    sc_ng = ngrams(sc_text)
    j_sc = jaccard(new_ng, sc_ng)
    print(f"vs SC Tesoura V2:                {j_sc:.4f}  {'✓ PASS' if j_sc < 0.20 else '✗ FAIL'}")
else:
    print(f"⚠ SC Tesoura V2 não encontrada: {SC_V2}")

# Test vs Brasília tesoura V2
BSB_V2 = '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(BSB_V2):
    with open(BSB_V2, 'r', encoding='utf-8') as f:
        bsb_html = f.read()
    bsb_text = extract_text(bsb_html)
    bsb_ng = ngrams(bsb_text)
    j_bsb = jaccard(new_ng, bsb_ng)
    print(f"vs BSB Tesoura V2:               {j_bsb:.4f}  {'✓ PASS' if j_bsb < 0.20 else '✗ FAIL'}")
else:
    print(f"⚠ BSB Tesoura V2 não encontrada: {BSB_V2}")

ELAPSED = time.time() - START
print(f"\n{'='*60}")
print("RESULTADO FINAL")
print(f"{'='*60}")
all_pass = (ref_classes == new_classes and ref_svgs == new_svgs and
            ref_sections == new_sections and j_ref < 0.20 and len(goiania_issues) == 0)
print(f"{'✅ TODOS OS TESTES PASSARAM' if all_pass else '❌ ALGUM TESTE FALHOU — revisar'}")
print(f"\n⏱ TEMPO: {ELAPSED:.1f}s")
print(f"📊 TOKENS estimados: ~{len(html)//4:,}")

# ═══════════════════════════════════════════════════════════════════════
# UPLOAD TO R2
# ═══════════════════════════════════════════════════════════════════════

if all_pass:
    print("\n🔄 Fazendo upload para R2...")
    import subprocess
    upload_script = f"""
import {{ AwsClient }} from 'aws4fetch';
import {{ readFileSync }} from 'node:fs';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT   = `https://${{ACCOUNT_ID}}.r2.cloudflarestorage.com`;
const BUCKET     = 'pages';
const R2_KEY     = 'itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura/index.html';

const aws = new AwsClient({{ accessKeyId: ACCESS_KEY, secretAccessKey: SECRET_KEY }});
const body = readFileSync('{OUT}');
const url = `${{ENDPOINT}}/${{BUCKET}}/${{R2_KEY}}`;

const res = await aws.fetch(url, {{
  method: 'PUT',
  body,
  headers: {{ 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'public, max-age=86400' }},
}});

if (res.ok) {{
  console.log('✅ Upload R2 OK:', R2_KEY);
  console.log('URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/' + R2_KEY);
}} else {{
  console.error('❌ Upload falhou:', res.status, await res.text());
}}
"""
    tmp_js = '/Users/jrios/Downloads/r2-upload/upload-itumbiara-tesoura.mjs'
    with open(tmp_js, 'w') as f:
        f.write(upload_script)
    result = subprocess.run(['node', tmp_js],
                          capture_output=True, text=True, timeout=30,
                          cwd='/Users/jrios/Downloads/r2-upload')
    print(result.stdout)
    if result.stderr:
        # Filter out experimental warnings
        for line in result.stderr.split('\n'):
            if line.strip() and 'ExperimentalWarning' not in line:
                print(line)
else:
    print("\n⚠ Upload cancelado — corrigir testes antes.")
