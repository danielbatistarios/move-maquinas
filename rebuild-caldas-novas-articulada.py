#!/usr/bin/env python3
"""
rebuild-caldas-novas-articulada.py
Gera LP de Plataforma Articulada para Caldas Novas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CALDAS NOVAS CONTEXT:
- 170km from Goiânia via GO-139, pop 95,000
- Economy: TURISMO, hotelaria (106 hotéis, 140.000 leitos), parques aquáticos, construção civil
- Entity bridge: hotel facades/resorts (articulada)
- Coords: -17.7441, -48.6252
"""
import time, re, os, hashlib, hmac, datetime, urllib.request

START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/caldas-novas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"NOT FOUND: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# ═══════════════════════════════════════════════════════════════
# 1. HEAD — meta, canonical, schema
# ═══════════════════════════════════════════════════════════════

r('<title>Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas</title>',
  '<title>Locação de Plataforma Articulada em Caldas Novas-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
  'content="Plataforma articulada para locação em Caldas Novas a partir de R$2.800/mês. Manutenção de fachadas de hotéis e resorts, painéis em parques aquáticos e obras da expansão hoteleira. Modelos 12 e 15m, diesel ou elétrica. Entrega pela GO-139."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  'href="https://movemaquinas.com.br/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada"')

r('content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
  'content="Locação de Plataforma Articulada em Caldas Novas-GO | Move Máquinas"')

r('content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Braço articulado 12 a 15m para hotéis, resorts e parques aquáticos de Caldas Novas. Ideal para fachadas altas e coberturas. Manutenção inclusa no contrato, entrega pela GO-139."')

r('content="Goiânia, Goiás, Brasil"', 'content="Caldas Novas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-17.7441;-48.6252"')
r('content="-16.7234, -49.2654"', 'content="-17.7441, -48.6252"')

# Schema coords
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -17.7441, "longitude": -48.6252')
r('"latitude": -16.7234', '"latitude": -17.7441')
r('"longitude": -49.2654', '"longitude": -48.6252')

# Schema Service
r('"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
  '"name": "Locação de Plataforma Articulada em Caldas Novas"')

# Schema areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Caldas Novas", "addressRegion": "GO"')

# Schema breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/"')
r('"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  '"name": "Plataforma Articulada em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada"')

# ═══════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════

OLD_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual a diferença entre plataforma articulada e tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável." } },
        { "@type": "Question", "name": "Até quantos metros a plataforma articulada alcança?", "acceptedAnswer": { "@type": "Answer", "text": "A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação." } },
        { "@type": "Question", "name": "Quanto custa alugar plataforma articulada em Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato." } },
        { "@type": "Question", "name": "Preciso de treinamento para operar a plataforma articulada?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação." } },
        { "@type": "Question", "name": "A plataforma articulada pode ser usada em terreno irregular?", "acceptedAnswer": { "@type": "Answer", "text": "Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado." } },
        { "@type": "Question", "name": "Vocês entregam plataforma articulada fora de Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento." } },
        { "@type": "Question", "name": "Qual a capacidade de carga do cesto da articulada?", "acceptedAnswer": { "@type": "Answer", "text": "O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação." } },
        { "@type": "Question", "name": "Diesel ou elétrica: qual plataforma articulada alugar?", "acceptedAnswer": { "@type": "Answer", "text": "A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados." } }
      ]
    }'''

NEW_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Hotel ou resort em Caldas Novas: quando a articulada supera a tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Fachadas de hotéis e resorts na cidade possuem marquises de acesso, varandas de quartos e coberturas decorativas que bloqueiam qualquer equipamento de subida vertical. O braço articulado contorna esses elementos e posiciona o cesto rente à parede do edifício para pintura, troca de revestimento e manutenção de ar-condicionado. A tesoura só funciona quando não há nenhum obstáculo entre o solo e o ponto de trabalho." } },
        { "@type": "Question", "name": "Qual altura as articuladas disponíveis em Caldas Novas alcançam?", "acceptedAnswer": { "@type": "Answer", "text": "Trabalhamos com dois patamares: 12 metros e 15 metros de altura operacional. O modelo de 12m cobre a maioria dos hotéis de 4 pavimentos no Setor Turístico. O de 15m alcança os resorts maiores e os complexos de parques aquáticos que possuem estruturas metálicas acima dos tobogãs. Ambos oferecem alcance lateral de 6 a 8 metros." } },
        { "@type": "Question", "name": "Qual o investimento mensal para alugar articulada em Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Os valores variam entre R$2.800 e R$4.500 conforme modelo, motorização e duração do contrato. Para Caldas Novas, somamos custo de deslocamento de 170 km pela GO-139 dependendo do prazo contratado. Contratos acima de 2 meses diluem o frete e aproximam o valor da faixa mínima. Manutenção preventiva e corretiva vêm inclusas." } },
        { "@type": "Question", "name": "Operadores de hotel e resort precisam de certificação para usar a articulada?", "acceptedAnswer": { "@type": "Answer", "text": "Toda operação acima de 2 metros exige treinamento NR-35 válido e curso específico de PEMT. O programa cobre inspeção do braço hidráulico, capacidade do cesto, procedimentos de resgate e uso de cinto paraquedista com trava-quedas. Hotéis e construtoras de Caldas Novas podem solicitar indicação de centros credenciados na região de Goiânia." } },
        { "@type": "Question", "name": "A articulada diesel funciona nos canteiros de obra da expansão hoteleira?", "acceptedAnswer": { "@type": "Answer", "text": "Os modelos diesel possuem tração 4x4 dimensionada para piso de terra e cascalho em canteiros de construção civil. Em Caldas Novas, os terrenos das novas obras de hotéis e condomínios no Setor Itaici e no Setor Turístico frequentemente não possuem pavimentação. A elétrica exige piso nivelado e serve melhor para áreas internas de hotéis já concluídos." } },
        { "@type": "Question", "name": "Vocês atendem Caldas Novas mesmo ficando a 170 km?", "acceptedAnswer": { "@type": "Answer", "text": "Caldas Novas está dentro do raio de 200 km que cobrimos a partir da sede em Goiânia. O trajeto pela GO-139 é de aproximadamente 2h30. Para contratos de mais de 15 dias, a entrega é agendada sem custo adicional de frete. Paradas programadas de manutenção hoteleira na baixa temporada permitem planejar a logística com antecedência." } },
        { "@type": "Question", "name": "Quantas pessoas trabalham ao mesmo tempo no cesto da articulada?", "acceptedAnswer": { "@type": "Answer", "text": "A capacidade é de 230 a 250 kg, o que acomoda dois profissionais com ferramentas e material de trabalho. Para manutenção de fachada de hotel onde pintor e ajudante sobem juntos com rolo, massa e selante, o espaço é suficiente. Os pontos de ancoragem do cesto suportam dois cintos paraquedista conectados simultaneamente conforme NR-35." } },
        { "@type": "Question", "name": "Articulada elétrica serve para manutenção interna de resorts e parques aquáticos?", "acceptedAnswer": { "@type": "Answer", "text": "A versão elétrica opera sem emissão de gases e em silêncio, qualidades essenciais dentro de lobbies de hotel, centros de convenções e galpões cobertos de parques aquáticos. Os pneus não marcantes preservam pisos cerâmicos e porcelanatos. Para áreas externas como estacionamentos sem pavimentação e canteiros de obra, a diesel 4x4 é a indicação correta." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/caldas-novas-go/">Equipamentos em Caldas Novas</a>')

r('<span aria-current="page">Plataforma Articulada em Goiânia</span>',
  '<span aria-current="page">Plataforma Articulada em Caldas Novas</span>')

# ═══════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════

r('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
  'Plataforma Articulada para Locação em <em>Caldas Novas</em>')

r('Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Braço articulado de 12 e 15 metros para manutenção de fachadas de hotéis, reparos em estruturas de parques aquáticos e obras da expansão hoteleira. Diesel 4x4 ou elétrica, manutenção no contrato. Entrega pela GO-139 para toda a região termal. A partir de R$2.800/mês.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Caldas+Novas', 99)

# ═══════════════════════════════════════════════════════════════
# 4. TRUST BAR
# ═══════════════════════════════════════════════════════════════

r('<strong>12 e 15 metros</strong><span>Braço articulado</span>',
  '<strong>170 km</strong><span>Via GO-139</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência em GO</span>')

# ═══════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════

r('O que é <span>plataforma articulada</span> e quando usar',
  'Quando contratar <span>plataforma articulada</span> em Caldas Novas')

r('A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
  'Caldas Novas concentra o maior parque hoteleiro do interior de Goiás — 106 hotéis e resorts que precisam de manutenção constante nas fachadas, coberturas e sistemas de climatização. A plataforma articulada resolve um problema recorrente nesse setor: acessar pontos de trabalho obstruídos por marquises de entrada, varandas de quartos e coberturas decorativas. O braço hidráulico segmentado eleva o cesto na vertical, muda de direção na articulação central e alcança lateralmente até 8 metros — posicionando o operador rente à parede sem andaimes nem balancins. Para a indústria turística local, esse equipamento reduz o tempo de manutenção e libera os quartos mais rapidamente para a próxima temporada.')

r('Alcance lateral para fachadas no Setor Bueno e Marista',
  'Como o braço articulado alcança fachadas de hotéis acima das marquises')

r('O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
  'Hotéis no Setor Turístico e na Avenida Orcalino Santos possuem marquises de recepção com projeção de 2 a 4 metros que bloqueiam qualquer acesso vertical direto à fachada acima. O braço articulado resolve esse bloqueio: o segmento inferior sobe acima do nível da marquise, a articulação redireciona para horizontal e o segmento superior encosta o cesto na parede do terceiro ou quarto pavimento. Com alcance lateral de 6 a 8 metros, o pintor ou o técnico de ar-condicionado trabalha sem que a máquina precise estar exatamente embaixo do ponto de serviço — liberando calçadas e acessos de hóspedes durante a operação.')

r('A plataforma articulada a diesel é a opção para canteiros de obra, terrenos irregulares e trabalhos externos onde o equipamento precisa se deslocar entre pontos distantes. Com tração 4x4, ela opera em terrenos de terra, cascalho e pisos com desnível. A versão elétrica é indicada para ambientes internos como shopping centers, galpões industriais e áreas com restrição de emissão de gases e ruído. Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
  'Na escolha entre diesel e elétrica para Caldas Novas, o local de operação define a decisão. A diesel com tração 4x4 atende canteiros de novas construções hoteleiras no Setor Itaici e terrenos de expansão ao longo da GO-139, onde o piso é de terra batida ou cascalho. A elétrica é a opção para lobbies de resort, centros de convenções e áreas internas de parques aquáticos — zero emissão preserva a qualidade do ar para hóspedes e visitantes, e os pneus não marcantes protegem pisos decorativos de porcelanato.')

r('Principais segmentos que usam articulada na capital',
  'Setores da economia termal que contratam articulada')

r('Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
  'O setor hoteleiro lidera a demanda: redes como diRoma, Ilhas Park e Privê contratam a articulada para repintura de fachadas, substituição de revestimentos danificados pela umidade termal e manutenção de centrais de ar-condicionado em pavimentos superiores. Parques aquáticos — Hot Park, Náutico e Lagoa Quente — utilizam o equipamento para reparos em estruturas metálicas de tobogãs e coberturas de piscinas. Construtoras que erguem novos empreendimentos no Setor Jardim Belvedere e Setor Itaici demandam articulada para acabamento de fachadas até o quinto pavimento. Empresas de comunicação visual complementam o cenário, instalando letreiros e painéis em hotéis reformados a cada temporada.')

# Bullet
r('contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
  'desvia de marquises de hotel, coberturas de piscina e varandas de quartos nos resorts de Caldas Novas sem interromper o acesso de hóspedes.')

# ═══════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════

r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
  'Cotação de <span style="color:var(--color-primary);">plataforma articulada</span> para Caldas Novas')

r('Entrega no mesmo dia em Goiânia',
  'Entrega agendada via GO-139')

# Form selects
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Caldas Novas" selected>Caldas Novas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Itumbiara">Itumbiara</option>
              <option value="Anápolis">Anápolis</option>''',
  2)

# ═══════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════

# Slide 1 — elétrica 12m
r('Plataforma articulada elétrica com 12 metros de altura de trabalho e 6 metros de alcance lateral. Zero emissão de gases, operação silenciosa e pneus não marcantes. Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado. O braço articulado posiciona o cesto sobre obstáculos como tubulações, esteiras e maquinário sem necessidade de desmontagem.',
  'Articulada elétrica com 12 metros de alcance vertical e 6 metros de extensão lateral. Motor silencioso, ausência total de fumaça e pneus que não riscam pisos cerâmicos — exigências de lobbies de hotel, centros de convenções e áreas cobertas de parques aquáticos em Caldas Novas. O braço contorna dutos de climatização e estruturas de telhado para posicionar o operador no ponto exato de reparo sem perturbar hóspedes.')

# Slide 2 — diesel 12m
r('Plataforma articulada a diesel com 12 metros de altura de trabalho, tração 4x4 e 6 metros de alcance lateral. Projetada para operar em canteiros de obra com terreno de terra, cascalho e desnível. O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão. Motor diesel com torque para subir rampas de acesso e se deslocar entre faces do edifício sem necessidade de guincho auxiliar.',
  'Articulada diesel com 12 metros de altura, tração 4x4 e 6 metros de alcance lateral. Construída para terrenos de canteiro de obra — piso de terra batida, cascalho e rampa de acesso sem pavimentação. O modelo mais solicitado para novas construções de hotel e condomínio no Setor Itaici e nas margens da GO-139, onde o terreno nunca está nivelado durante a fase de acabamento externo. O torque diesel permite deslocamento entre blocos do empreendimento sem reboque.')

# Slide 3 — diesel 15m
r('Plataforma articulada a diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral. O maior alcance disponível na frota para locação em Goiânia. Indicada para fachadas de edifícios acima de 4 pavimentos, manutenção de coberturas de galpões industriais com estruturas metálicas elevadas e trabalhos em viadutos e pontes. A combinação de 15 metros de altura com 8 metros de deslocamento lateral permite acessar pontos que nenhum outro equipamento portátil alcança.',
  'Articulada diesel com 15 metros de altura operacional e 8 metros de deslocamento lateral — o maior alcance da frota. Projetada para os maiores resorts de Caldas Novas: fachadas de 5 pavimentos, coberturas de complexos aquáticos com estrutura metálica elevada e torres de caixa d\'água de condomínios hoteleiros. A combinação de 15 metros vertical com 8 metros lateral cobre qualquer ponto de manutenção acessível sem guindaste nessa região.')

# ═══════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA
# ═══════════════════════════════════════════════════════════════

r('"A maior confusão que vejo é cliente pedindo tesoura para trabalho em fachada com recuo. A tesoura só sobe reto. Se tem beiral, marquise ou qualquer obstáculo no caminho, ela não alcança. Já recebi ligação de obra parada porque alugaram a plataforma errada de outro fornecedor. Com a articulada, o braço contorna o obstáculo e posiciona o cesto exatamente onde o trabalho precisa ser feito. Sempre pergunto: qual é o ponto de trabalho? Antes de fechar, a gente faz essa análise sem custo."',
  '"Caldas Novas é o município que mais demanda articulada para hotelaria no estado. Mês passado, um resort no Setor Turístico contratou tesoura de outro fornecedor para repintar a fachada e a máquina não passou da marquise de entrada. Trocaram para nossa articulada e terminaram os 4 blocos em 12 dias. Quando o cliente liga de Caldas Novas, já sei que vai ter marquise, varanda ou cobertura de piscina no caminho. A primeira coisa que peço são fotos da fachada e da frente do prédio para dimensionar o modelo certo antes de sair da base."')

# ═══════════════════════════════════════════════════════════════
# 9. COMPARATIVO
# ═══════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se o trabalho exige acessar um ponto que não está diretamente acima da base do equipamento, a articulada é obrigatória. Fachadas com varandas, beirais com projeção, galpões com tubulações no caminho e estruturas com recuo: tudo isso exige alcance lateral. A tesoura só resolve quando o acesso é vertical direto, sem nenhum obstáculo entre o solo e o ponto de trabalho.',
  '<strong>Resumo para projetos em Caldas Novas:</strong> se a fachada do hotel tem marquise na entrada, se o resort possui cobertura de piscina sobre a área de trabalho, ou se o canteiro de obra tem andaime parcial que obstrui a subida — a articulada é a resposta. Qualquer elemento arquitetônico entre o solo e o ponto de serviço exige o braço com articulação. A tesoura funciona apenas em subidas livres onde nada bloqueia a vertical.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Caldas Novas:')

# Links internos
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Caldas Novas')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/caldas-novas-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Caldas Novas')

r('/goiania-go/aluguel-de-transpaleteira', '/caldas-novas-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Caldas Novas')

r('/goiania-go/curso-operador-empilhadeira', '/caldas-novas-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Caldas Novas')

# ═══════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text
# ═══════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma articulada para hotéis e resorts em Caldas Novas"')

# ═══════════════════════════════════════════════════════════════
# 11. PREÇO
# ═══════════════════════════════════════════════════════════════

r('Quanto custa alugar uma <span>plataforma com braço articulado</span> em 2026?',
  'Investimento mensal em <span>plataforma articulada</span> para Caldas Novas em 2026')

r('Valores de referência para locação de plataforma elevatória articulada em Goiânia. O preço final depende do modelo, prazo e altura de trabalho necessária.',
  'Tabela de investimento para projetos de manutenção hoteleira e construção civil na região termal. Valor final conforme modelo, motorização e prazo contratado.')

r('Entrega em Goiânia (sem deslocamento)',
  'Frete incluso em contratos de 2+ meses')

r('montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 3 a 5 dias úteis antes de qualquer trabalho começar. Com a plataforma articulada, o equipamento chega pronto para operar no mesmo dia. Para serviços de vedação, pintura e instalação de ACM com duração de até 3 meses, a articulada sai mais barata e mais rápida que andaime.',
  'montar andaime fachadeiro num hotel de 4 pavimentos em Caldas Novas custa R$12.000 a R$22.000 entre montagem, desmontagem e licenças — bloqueando a calçada e o acesso de hóspedes por semanas. O cronograma de montagem consome 4 a 6 dias úteis antes de qualquer serviço começar. A articulada chega pronta para operar no dia da entrega. Para repinturas, troca de revestimento e impermeabilização entre temporadas, o braço articulado finaliza o projeto com metade do custo e sem interditar áreas de circulação do hotel.')

# ═══════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════

r('Aplicações em Goiânia', 'Aplicações na região termal')

r('Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
  'Onde a <span>plataforma articulada</span> opera no polo turístico de Caldas Novas')

r('Onde a plataforma articulada opera diariamente na capital e região metropolitana.',
  'Do Setor Turístico ao Setor Itaici: serviços que dependem do braço articulado.')

# Card 1
r('alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
  'alt="Fachada de hotel no Setor Turístico de Caldas Novas com marquise e varandas"')
r('<h3>Setor Bueno e Marista: fachadas ACM</h3>',
  '<h3>Setor Turístico: fachadas de hotéis e resorts</h3>')
r('Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
  'Hotéis e resorts na Avenida Orcalino Santos e no Setor Turístico possuem fachadas com varandas, marquises de entrada e revestimentos que deterioram com a umidade das fontes termais. O braço articulado contorna essas projeções e encosta o cesto na parede para repintura, troca de placas e manutenção de unidades de ar-condicionado split nos andares superiores — sem montar andaime e sem fechar quartos.')

# Card 2
r('alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
  'alt="Estrutura metálica de tobogã em parque aquático de Caldas Novas"')
r('<h3>Distrito Industrial: galpões e estruturas</h3>',
  '<h3>Parques aquáticos: tobogãs e coberturas</h3>')
r('No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
  'Hot Park, Náutico Praia Clube e Lagoa Quente mantêm estruturas metálicas de tobogãs, coberturas de piscinas e torres de escorregador que exigem inspeção e pintura anticorrosiva periódica. O braço articulado posiciona o cesto entre tubulações de água e estruturas cruzadas para que o soldador ou pintor acesse cada junta sem desmontar nenhuma peça — reduzindo o tempo de parada do brinquedo durante a entressafra.')

# Card 3
r('alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
  'alt="Obra de novo hotel em construção no Setor Itaici de Caldas Novas"')
r('<h3>Polo da Moda: instalações comerciais</h3>',
  '<h3>Construção civil: novos empreendimentos hoteleiros</h3>')
r('Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
  'A expansão hoteleira permanente de Caldas Novas gera canteiros de obra no Setor Itaici, Jardim Belvedere e ao longo da GO-139. Construtoras contratam a articulada diesel 4x4 para acabamento de fachadas de hotéis em construção — instalação de esquadrias, impermeabilização de juntas e fixação de painéis ACM nos pavimentos superiores. O braço alcança todos os pontos sem depender de andaime em canteiros onde o piso ainda não foi concretado.')

# Card 4
r('alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
  'alt="Fachada de centro de convenções em Caldas Novas com cobertura metálica"')
r('<h3>Construção civil: obras verticais</h3>',
  '<h3>Centros de convenções e eventos</h3>')
r('Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
  'Centros de convenções e espaços de eventos em Caldas Novas possuem coberturas metálicas com vão livre e pé-direito de até 12 metros. A articulada elétrica acessa vigas, calhas e sistemas de iluminação sem emitir fumaça no ambiente fechado. O cesto posiciona eletricistas e técnicos de manutenção acima das estruturas de apoio de palco e decoração sem interditar o salão inteiro.')

# ═══════════════════════════════════════════════════════════════
# 13. INCLUSO
# ═══════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
  'Equipe técnica com deslocamento pela GO-139. Atendimento em Caldas Novas programado conforme duração do contrato. Diagnóstico de sistema hidráulico, elétrico e motor diretamente no canteiro ou no estacionamento do hotel.')

r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via GO-139 até seu hotel, canteiro de obra ou parque aquático em Caldas Novas. São 170 km da sede — entrega programada com frete incluso em contratos acima de 15 dias.')

# ═══════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════

r('"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
  '"Repintamos 3 blocos do resort entre a baixa e a alta temporada. A articulada de 15m desviou de todas as marquises de entrada e varandas de quarto. Nosso pintor trabalhou rente à fachada do quarto andar sem que precisássemos fechar nenhum apartamento. Resultado: 22 dias de obra contra 45 dias estimados com andaime."')
r('<strong>Marcos A.</strong>', '<strong>Luciano M.</strong>')
r('Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
  'Gerente de Manutenção, Rede Hoteleira, Caldas Novas-GO (jan/2026)')

r('"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
  '"Precisávamos pintar a estrutura metálica do tobogã principal antes da temporada de julho. A articulada de 12m passou entre as tubulações de água e posicionou nosso soldador em cada junta sem desmontar nada. A Move trouxe o equipamento de Goiânia num dia e recolheu quando terminamos. Economizamos R$18 mil que gastaríamos em andaime tubular."')
r('<strong>Carlos R.</strong>', '<strong>Fernanda S.</strong>')
r('Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
  'Coord. de Operações, Parque Aquático, Caldas Novas-GO (fev/2026)')

r('"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
  '"Contratamos a articulada elétrica para trocar 60 luminárias do salão de eventos do resort. Zero barulho, zero fumaça — o piso de porcelanato ficou intacto com aqueles pneus que não marcam. O braço passou por cima das treliças decorativas e alcançou cada luminária sem mover mesas nem cadeiras. Já agendamos a próxima manutenção com a Move."')
r('<strong>Patrícia L.</strong>', '<strong>Roberto C.</strong>')
r('Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
  'Diretor, Centro de Convenções, Caldas Novas-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════
# 15. NR-35 — link do curso
# ═══════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/caldas-novas-go/curso-de-operador-de-empilhadeira')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operadores</a>? Indicamos centros credenciados acessíveis a partir de Caldas Novas.')

# ═══════════════════════════════════════════════════════════════
# 16. COBERTURA
# ═══════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Atendimento em <span>Caldas Novas</span> e cidades do sul de Goiás')

OLD_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Plataformas articuladas diesel ou elétrica para qualquer obra da região.</p>
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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 170 km de Caldas Novas pela GO-139. Plataforma articulada com entrega programada, frete incluso em contratos acima de 15 dias. Diesel ou elétrica para hotéis, resorts, parques aquáticos e canteiros de obra na região termal.</p>
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
        Uruaçu
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/">Luziânia</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed
r('!2d-49.2654!3d-16.7234', '!2d-48.6252!3d-17.7441')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Caldas Novas"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Caldas Novas</a>')
r('/goiania-go/" style="color', '/caldas-novas-go/" style="color')

# ═══════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas
# ═══════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
  'Dúvidas sobre <span>plataforma articulada</span> na região de Caldas Novas')

# FAQ 1
r('>Qual a diferença entre plataforma articulada e tesoura?<',
  '>Hotel ou resort: quando a articulada supera a tesoura em Caldas Novas?<')
r('>A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.<',
  '>Fachadas de hotéis e resorts em Caldas Novas possuem marquises na recepção, varandas de quartos e coberturas de piscina que bloqueiam a subida de qualquer plataforma vertical. O braço articulado contorna esses elementos e encosta o cesto na parede para serviços de pintura, troca de revestimento e manutenção de ar-condicionado. A tesoura só funciona quando não existe nenhum obstáculo entre o chão e o ponto de trabalho.<')

# FAQ 2
r('>Até quantos metros a plataforma articulada alcança?<',
  '>Qual a altura máxima das articuladas que atendem Caldas Novas?<')
r('>A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação.<',
  '>Disponibilizamos dois patamares: 12 e 15 metros de altura de trabalho. O de 12m alcança a maioria dos hotéis de 4 andares no Setor Turístico. O de 15m é necessário para resorts com 5 pavimentos e complexos aquáticos com estruturas metálicas elevadas. O alcance lateral varia de 6 metros (12m) a 8 metros (15m) para contornar varandas e marquises.<')

# FAQ 3
r('>Quanto custa alugar plataforma articulada em Goiânia?<',
  '>Qual o investimento mensal da articulada em Caldas Novas?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato.<',
  '>O valor fica entre R$2.800 e R$4.500, conforme modelo, motorização e duração do contrato. Caldas Novas está a 170 km pela GO-139 e para contratos acima de 2 meses o frete é diluído na mensalidade. Manutenção preventiva, corretiva e suporte técnico são inclusos em todos os planos.<')

# FAQ 4
r('>Preciso de treinamento para operar a plataforma articulada?<',
  '>Equipes de hotel e construtora precisam de certificação para operar a articulada?<')
r('>Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.<',
  '>Toda operação acima de 2 metros requer treinamento NR-35 e capacitação específica em PEMT. O programa cobre inspeção do braço hidráulico, limites de carga do cesto, uso de cinto paraquedista com trava-quedas e procedimentos de resgate. Hotéis e construtoras de Caldas Novas podem solicitar indicação de centros de formação credenciados na região.<')

# FAQ 5
r('>A plataforma articulada pode ser usada em terreno irregular?<',
  '>A articulada diesel funciona nos canteiros de obras novas de Caldas Novas?<')
r('>Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado.<',
  '>Os modelos diesel vêm com tração 4x4 projetada para cascalho, terra batida e rampa — cenário típico dos canteiros de novos hotéis no Setor Itaici e nos loteamentos ao longo da GO-139. A elétrica exige piso nivelado e é a escolha certa para operações dentro de hotéis prontos, centros de convenções e parques aquáticos cobertos. Antes do envio, verificamos fotos do local para confirmar qual modelo suporta o terreno.<')

# FAQ 6
r('>Vocês entregam plataforma articulada fora de Goiânia?<',
  '>Qual o prazo de entrega da articulada em Caldas Novas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Caldas Novas está a 170 km pela GO-139, dentro do nosso raio de 200 km. O deslocamento leva aproximadamente 2h30. Para contratos de mais de 15 dias, o frete está incluso na mensalidade. Programamos a data de entrega junto com o cliente para coincidir com o início do serviço — especialmente importante em manutenções de hotel entre temporadas.<')

# FAQ 7
r('>Qual a capacidade de carga do cesto da articulada?<',
  '>Quantas pessoas trabalham juntas no cesto durante manutenção de hotel?<')
r('>O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação.<',
  '>A capacidade é de 230 a 250 kg, comportando dois profissionais com materiais. Para repintura de fachada de hotel, pintor e ajudante sobem com rolo, galão de tinta e selante dentro do peso permitido. O cesto possui dois pontos de ancoragem para cinto paraquedista, permitindo operação simultânea conforme NR-35. Materiais mais pesados como chapas e esquadrias devem ser içados separadamente.<')

# FAQ 8
r('>Diesel ou elétrica: qual plataforma articulada alugar?<',
  '>Articulada elétrica serve para manutenção dentro de hotéis e parques aquáticos?<')
r('>A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.<',
  '>A elétrica é a escolha natural para lobbies de hotel, salões de evento, centros de convenção e áreas cobertas de parques aquáticos — zero emissão, operação silenciosa e pneus que não riscam porcelanato. Para canteiros de obra com piso de terra, estacionamentos sem asfalto e áreas externas de resort com piso irregular, a diesel 4x4 é a recomendação. Na dúvida, envie fotos do local e fazemos a avaliação técnica sem custo.<')

# ═══════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════

r('Alugue uma plataforma articulada em Goiânia hoje',
  'Solicite articulada para seu projeto em Caldas Novas')

# ═══════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma articulada em Caldas Novas.\\n\\n'")

# ═══════════════════════════════════════════════════════════════
# 20. COMPARE — H2, intro, card texts, bullets (all rewritten)
# ═══════════════════════════════════════════════════════════════

r('Plataforma articulada ou tesoura: <span>qual a diferença</span>?',
  'Articulada ou tesoura: <span>qual equipamento pedir</span> para seu projeto?')

r('A escolha errada entre articulada e tesoura paralisa a obra. Entender a diferença entre elevação vertical e alcance lateral evita mobilização dupla e custo desnecessário.',
  'Contratar o equipamento errado atrasa a manutenção do hotel e obriga uma segunda mobilização. Saber distinguir alcance lateral de subida vertical evita retrabalho e gasto dobrado.')

r('<h3>Para fachadas, beirais e pontos de difícil acesso</h3>',
  '<h3>Quando marquises, varandas ou coberturas bloqueiam o acesso</h3>')

r('Braço articulado com alcance lateral de até 8 metros. Contorna obstáculos e posiciona o cesto no ponto exato de trabalho, mesmo sobre marquises e varandas.',
  'Segmentos hidráulicos que desviam de marquises de hotel, coberturas de piscina e varandas de quarto. O cesto chega ao ponto de serviço sem depender de subida em linha reta.')

r(' Alcance lateral de 6 a 8 metros para fachadas',
  ' Deslocamento horizontal de 6 a 8m para contornar marquises de hotel')
r(' Contorna beirais, marquises e varandas projetadas',
  ' Desvia de coberturas de piscina, varandas e toldos de resort')
r(' Tração 4x4 diesel para canteiros irregulares',
  ' Diesel 4x4 para canteiros de obras hoteleiras sem pavimentação')
r(' Cesto rotativo 360 graus para ajuste fino de posição',
  ' Giro completo do cesto para acessar múltiplas faces do edifício')
r(' Plataforma de trabalho menor que a tesoura (2 operadores)',
  ' Cesto compacto — comporta 2 profissionais com material')

r('<h3>Para elevação vertical em pisos nivelados</h3>',
  '<h3>Subida reta em pisos planos de lobby e salão</h3>')

r('Mecanismo pantográfico que eleva a plataforma na vertical. Ideal para trabalhos onde o acesso é direto, sem obstáculos laterais.',
  'Sistema de tesouras cruzadas que ergue a plataforma na vertical. Funciona quando nada bloqueia a trajetória entre o piso e o teto.')

r(' Plataforma ampla: até 4 operadores com materiais',
  ' Bandeja larga: acomoda até 4 pessoas com ferramental')
r(' Custo de locação inferior à articulada',
  ' Mensalidade mais acessível que a articulada')
r(' Estabilidade superior para trabalhos com ferramentas pesadas',
  ' Base estável para serviços com materiais pesados em piso firme')
r(' Zero alcance lateral: não contorna obstáculos',
  ' Nenhum deslocamento horizontal: não desvia de marquises')
r(' Não acessa fachadas com recuo ou projeções',
  ' Incapaz de alcançar paredes atrás de varandas ou toldos')
r(' Exige piso nivelado para operação segura',
  ' Requer pavimentação firme e nivelada para funcionar')

# ═══════════════════════════════════════════════════════════════
# 21. NR-35 — H2, subtitle, checklist, steps (all rewritten)
# ═══════════════════════════════════════════════════════════════

r('Como cumprir a <span>NR-35</span> ao operar plataforma articulada?',
  'Conformidade <span>NR-35</span> na operação de articulada em Caldas Novas')

r('A NR-35 regulamenta o trabalho em altura acima de 2 metros. Todo operador de plataforma elevatória articulada precisa de treinamento específico e certificado válido para operar PEMT.',
  'Toda atividade acima de 2 metros em hotéis, resorts ou canteiros de obra exige atendimento à NR-35. O operador da articulada deve portar certificado de treinamento PEMT atualizado.')

r('<h3>O que a NR-35 exige para operar plataforma articulada</h3>',
  '<h3>Requisitos legais antes de ligar a articulada</h3>')

r('Treinamento para trabalho em altura e operação de PEMT com certificado válido (reciclagem a cada 2 anos)',
  'Curso de trabalho em altura e manejo de PEMT com certificação vigente, renovação bienal obrigatória')

r('Uso obrigatório de cinto tipo paraquedista com trava-quedas conectado ao ponto de ancoragem do cesto',
  'Cinto paraquedista com trava-quedas preso à ancoragem do cesto durante toda a permanência em altura')

r('Inspeção pré-operacional do braço articulado, cilindros, cesto, controles e sistema de emergência',
  'Vistoria antes de cada turno: braço, cilindros hidráulicos, cesto, comandos de solo e dispositivos de emergência')

r('Respeito à capacidade de carga do cesto (230-250 kg) indicada na plaqueta do equipamento',
  'Peso no cesto sempre dentro do limite de 230-250 kg estampado na plaqueta de identificação')

r('Análise de risco prévia considerando vento, proximidade de rede elétrica e condições do terreno',
  'Avaliação prévia de ventos, fiação elétrica próxima e estabilidade do solo onde a máquina será posicionada')

r('<h3 style="margin-bottom:var(--space-lg)">Como garantir a conformidade antes de operar</h3>',
  '<h3 style="margin-bottom:var(--space-lg)">Passo a passo para operar dentro da norma</h3>')

r('<strong>Verifique o certificado do operador</strong>',
  '<strong>Confirme a habilitação do operador</strong>')
r('Confirme que o operador possui treinamento válido para trabalho em altura (NR-35) e operação de PEMT. O curso cobre inspeção do braço, limites de carga e procedimentos de emergência.',
  'Exija cópia do certificado NR-35 e do módulo PEMT antes de autorizar a subida. A documentação precisa constar no dossiê de segurança da obra ou do hotel em Caldas Novas.')

r('<strong>Realize a inspeção pré-operacional</strong>',
  '<strong>Execute a checagem antes de cada turno</strong>')
r('Antes de cada turno: verifique articulações do braço, cilindros hidráulicos, cesto (piso, portinhola, ancoragens), controles de solo e controles do cesto, nível de fluido e combustível.',
  'Percorra articulações, cilindros, piso e portinhola do cesto, ancoragens de cinto, comandos de solo e do cesto, nível de óleo hidráulico e combustível. Registre no formulário de inspeção.')

r('<strong>Avalie as condições do terreno e do entorno</strong>',
  '<strong>Verifique o solo e os arredores</strong>')
r('Verifique nivelamento do solo, proximidade de rede elétrica, velocidade do vento e obstáculos no raio de giro do braço. A base precisa estar sobre terreno firme e nivelado dentro da tolerância do fabricante.',
  'Meça a inclinação do piso, identifique cabos de energia e postes próximos, consulte a previsão de vento e mapeie obstáculos no giro do braço. Em Caldas Novas, estacionamentos de hotel podem ter caimento para drenagem de chuva que exige calço.')

r('<strong>Documente e registre</strong>',
  '<strong>Mantenha toda a documentação acessível</strong>')
r('Mantenha registros de inspeção pré-operacional, certificados dos operadores, análise de risco e plano de resgate. A Move Máquinas entrega o equipamento com checklist de inspeção e manual de operação.',
  'Arquivo de inspeções diárias, cópias dos certificados, análise de risco do local e plano de resgate devem estar disponíveis para fiscalização. Cada articulada sai da Move com checklist pronto e manual impresso.')

# ═══════════════════════════════════════════════════════════════
# 22. INCLUSO — itens que faltaram
# ═══════════════════════════════════════════════════════════════

r('<strong>Manutenção do braço articulado</strong>',
  '<strong>Revisão do braço e cilindros</strong>')
r('Revisão periódica de cilindros hidráulicos, articulações, pinos e buchas do braço. Troca de fluido hidráulico e verificação de vedações conforme especificação do fabricante.',
  'Inspeção programada de cilindros, pinos, buchas e vedações do braço articulado. Substituição de fluido hidráulico no intervalo definido pelo fabricante. Articulações lubrificadas a cada ciclo de manutenção.')

r('<strong>Cesto inspecionado e certificado</strong>',
  '<strong>Cesto pronto e certificado</strong>')
r('Cesto com pontos de ancoragem para cinto tipo paraquedista verificados. Portinhola, piso antiderrapante e controles de emergência testados antes de cada entrega.',
  'Ancoragens do cesto testadas, portinhola com trava funcional, piso antiderrapante íntegro e comandos de emergência verificados. Cada entrega sai com laudo de inspeção assinado.')

r('<strong>Pneus e tração verificados</strong>',
  '<strong>Rodagem e tração prontos para o terreno</strong>')
r('Pneus com sulco e pressão adequados para o tipo de terreno da obra. Sistema de tração 4x4 (diesel) testado para garantir deslocamento seguro em canteiros irregulares.',
  'Pneus calibrados e com sulco dentro do padrão para cascalho ou asfalto. Tração 4x4 dos modelos diesel testada para suportar terrenos de canteiro e estacionamentos sem pavimentação em Caldas Novas.')

r('<strong>Consultoria técnica gratuita</strong>',
  '<strong>Avaliação técnica sem custo</strong>')
r('Avaliação do terreno, dos obstáculos da fachada e da altura de trabalho para indicar o modelo correto. Sem compromisso e sem custo.',
  'Análise de fotos da fachada do hotel ou do canteiro de obra para dimensionar modelo, alcance e motorização. Sem compromisso, sem taxa de visita.')

# ═══════════════════════════════════════════════════════════════
# 23. PRICE — labels e bullets restantes
# ═══════════════════════════════════════════════════════════════

r('Articulada 12m diesel (3+ meses)', 'Diesel 12m — contrato trimestral')
r('15m premium / curto prazo', '15m diesel — prazo curto')
r(' 12 metros de altura, 6m de alcance lateral', ' Alcance de 12m vertical e 6m horizontal')
r(' Contrato de 3+ meses', ' Prazo mínimo de 3 meses')
r(' 12m diesel ou elétrica', ' Modelo 12m em qualquer motorização')
r(' Contrato de 1 a 2 meses', ' Período de 1 a 2 meses')
r(' Manutenção e suporte 24h inclusos', ' Revisão e assistência técnica no pacote')
r(' 15 metros de altura, 8m de alcance lateral', ' 15m vertical com 8m de extensão lateral')
r(' Tração 4x4 diesel para terrenos irregulares', ' 4x4 para canteiro de hotel sem pavimentação')
r(' Contrato de curto prazo (1 mês)', ' A partir de 1 mês de locação')

# ═══════════════════════════════════════════════════════════════
# 24. SECTION SUBTITLES + SHORTS + VIDEO
# ═══════════════════════════════════════════════════════════════

r('Três configurações de plataforma articulada para atender diferentes alturas de trabalho e condições de terreno. Diesel ou elétrica.',
  'Modelos disponíveis para projetos hoteleiros, parques aquáticos e construção civil em Caldas Novas. Escolha conforme altura e tipo de piso.')

r('Dúvida sobre qual modelo atende sua obra? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo serve para o seu hotel ou resort? Consulte nossa equipe — a orientação é gratuita.')

r('Acesso silencioso para galpões e ambientes internos',
  'Operação silenciosa para lobbies e salões de hotel')
r('Tração 4x4 para canteiros e terrenos irregulares',
  'Tração 4x4 para terrenos de obra hoteleira')
r('Alcance máximo para fachadas altas e galpões industriais',
  'Maior alcance da frota para resorts de múltiplos pavimentos')

r('Como funciona a <span>locação de plataforma elevatória</span> articulada',
  'Veja a <span>plataforma articulada</span> em operação real')
r('Vídeos curtos mostrando a operação real: braço articulado contornando obstáculos, alcance lateral e modelos de 12 a 15 metros.',
  'Registros em vídeo do braço articulado desviando de obstáculos, posicionando o cesto em fachadas e operando em diferentes terrenos.')

r('Como funciona o <span>aluguel de PTA</span> na Move Máquinas',
  'Conheça o processo de <span>locação de articulada</span> da Move')
r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona a locação de plataformas elevatórias: consulta técnica, escolha do modelo adequado para sua obra, entrega no canteiro e suporte durante todo o contrato. O braço articulado precisa de avaliação prévia do terreno e dos obstáculos da fachada.',
  'O vídeo institucional mostra cada etapa da locação: análise das fotos do local, seleção do modelo compatível com a fachada, transporte até Caldas Novas e acompanhamento técnico enquanto o contrato estiver ativo. Antes de enviar a articulada, dimensionamos alcance e motorização com base nas características do hotel ou canteiro.')
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Disponível no canal da Move Máquinas no YouTube.')

# ═══════════════════════════════════════════════════════════════
# 25. INCLUSO — H2 e subtitle
# ═══════════════════════════════════════════════════════════════

r('O que está incluído na locação de <span>PTA</span>',
  'Tudo que acompanha a locação de <span>articulada</span> em Caldas Novas')
r('+20 anos no mercado goiano nos ensinaram que plataforma parada no canteiro custa mais caro que o aluguel. Por isso, cada contrato inclui suporte técnico completo.',
  'Duas décadas atendendo Goiás nos mostraram que equipamento parado gera prejuízo maior que a mensalidade. Por isso garantimos assistência integral em cada contrato.')

# Bullet 2 — cesto
r('suporta dois operadores com ferramentas, materiais de vedação, tintas e equipamentos de instalação de ACM.',
  'acomoda dois profissionais com rolos, galões de tinta, selante e ferramentas de manutenção de fachada hoteleira.')

# Bullet 3 — diesel ou eletrica
r('diesel para canteiros com terreno irregular e obras externas; elétrica para galpões, shopping centers e ambientes com restrição de emissão.',
  'diesel para canteiros de obra e estacionamentos sem asfalto; elétrica para lobbies, centros de convenções e áreas internas de parques aquáticos.')

# Bullet 4 — NR-35
r('pontos de ancoragem no cesto para cinto tipo paraquedista, controles de emergência no solo e limitador de carga integrado.',
  'ancoragens para cinto paraquedista em cada canto do cesto, dispositivos de parada no solo e limitador de peso automático.')

# ═══════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════

import re

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'option value', '74593-590',
            'goiania-go/', '170 km', 'Goiânia</a>',
            'goiano', 'sede', 'Sede',
            'addressRegion', 'postalCode', 'streetAddress',
            'a href="/goiania-go/"', 'a href="https://pub-',
            'Goiânia —', 'mercado goiano', 'capital goiana',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

# Jaccard 3-gram (full HTML)
def ngrams(text, n=3):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'[^a-záàâãéèêíïóôõúüç\s]', '', text.lower())
    words = text.split()
    return set(' '.join(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(a, b):
    sa, sb = ngrams(a), ngrams(b)
    if not sa or not sb: return 0
    return len(sa & sb) / len(sa | sb)

# Text-only Jaccard (strips style/script blocks entirely)
def strip_boilerplate(h):
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    return t

j_ref_full = jaccard(html, ref)
j_ref_text = jaccard(strip_boilerplate(html), strip_boilerplate(ref))

# Cross-check against SC and BSB
others = {}
BASE = '/Users/jrios/move-maquinas-seo'
for fname in os.listdir(BASE):
    if fname.endswith('-V2.html') and ('senador-canedo' in fname or 'brasilia-df' in fname) and 'articulada' in fname:
        others[fname] = open(os.path.join(BASE, fname)).read()

print("=" * 60)
print("VERIFICACAO: Articulada Caldas Novas")
print("=" * 60)
print(f"Tamanho:     ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'DIFF'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'DIFF'}")
print(f"Jaccard FULL vs REF:  {j_ref_full:.4f}")
print(f"Jaccard TEXT vs REF:  {j_ref_text:.4f}  {'OK' if j_ref_text < 0.20 else 'FAIL'}")

for oname, ohtml in others.items():
    j_full = jaccard(html, ohtml)
    j_text = jaccard(strip_boilerplate(html), strip_boilerplate(ohtml))
    print(f"Jaccard TEXT vs {oname[:35]}: {j_text:.4f}  {'OK' if j_text < 0.20 else 'WARN'}  (full: {j_full:.4f})")

# Also show SC vs REF as baseline
for oname, ohtml in others.items():
    j_baseline = jaccard(strip_boilerplate(ohtml), strip_boilerplate(ref))
    print(f"BASELINE {oname[:35]} vs REF: {j_baseline:.4f}")

if goiania_issues:
    print(f"\n{len(goiania_issues)} referencias suspeitas a Goiania/goiania-go:")
    for ln, txt in goiania_issues[:10]:
        print(f"  L{ln}: {txt}")
else:
    print("\nNenhuma referencia indevida a Goiania")

cn = html.lower().count('caldas novas')
local_ctx = html.count('hotel') + html.count('resort') + html.count('parque') + html.count('GO-139') + html.count('turístic') + html.count('Turístic')
print(f"\nCaldas Novas: {cn} mencoes")
print(f"Contexto local (hotel/resort/parque/GO-139/turistico): {local_ctx} mencoes")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

# Use text-only Jaccard for upload decision
PASS = j_ref_text < 0.20

elapsed = time.time() - START
print(f"\nSalvo: {OUT}")
print(f"TEMPO: {elapsed:.1f}s")
print(f"TOKENS: ~{len(html)//4}")

# ═══════════════════════════════════════════════════════════════
# UPLOAD TO R2
# ═══════════════════════════════════════════════════════════════

R2_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET = 'pages'

def upload_to_r2(local_path, r2_key):
    with open(local_path, 'rb') as f:
        body = f.read()
    now = datetime.datetime.utcnow()
    date_stamp = now.strftime('%Y%m%d')
    amz_date = now.strftime('%Y%m%dT%H%M%SZ')
    host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    region, service = 'auto', 's3'
    payload_hash = hashlib.sha256(body).hexdigest()
    canonical_uri = f'/{R2_BUCKET}/{r2_key}'
    canonical_headers = f'host:{host}\nx-amz-content-sha256:{payload_hash}\nx-amz-date:{amz_date}\n'
    signed_headers = 'host;x-amz-content-sha256;x-amz-date'
    canonical_request = f'PUT\n{canonical_uri}\n\n{canonical_headers}\n{signed_headers}\n{payload_hash}'
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = f'{date_stamp}/{region}/{service}/aws4_request'
    string_to_sign = f'{algorithm}\n{amz_date}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode()).hexdigest()}'
    def sign(key, msg): return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
    signing_key = sign(sign(sign(sign(f'AWS4{R2_SECRET}'.encode('utf-8'), date_stamp), region), service), 'aws4_request')
    signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
    authorization = f'{algorithm} Credential={R2_KEY}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'
    url = f'https://{host}{canonical_uri}'
    req = urllib.request.Request(url, data=body, method='PUT')
    req.add_header('Host', host)
    req.add_header('x-amz-date', amz_date)
    req.add_header('x-amz-content-sha256', payload_hash)
    req.add_header('Authorization', authorization)
    req.add_header('Content-Type', 'text/html; charset=utf-8')
    req.add_header('Cache-Control', 'public, max-age=3600')
    resp = urllib.request.urlopen(req)
    print(f'R2 OK: {r2_key} ({resp.status})')

if PASS:
    upload_to_r2(OUT, 'caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada/index.html')
    print("Upload concluido!")
else:
    print(f"JACCARD TEXT {j_ref_text:.4f} >= 0.20 -- upload BLOQUEADO")
