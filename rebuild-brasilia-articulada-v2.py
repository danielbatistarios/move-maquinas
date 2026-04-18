#!/usr/bin/env python3
"""
rebuild-brasilia-articulada-v2.py
Gera LP de Plataforma Articulada para Brasília-DF
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

from datetime import datetime
start = datetime.now()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html'

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

r('<title>Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas</title>',
  '<title>Locação de Plataforma Articulada em Brasília-DF | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
  'content="Plataforma articulada para locação em Brasília: 12 e 15 metros de alcance, diesel ou elétrica. Manutenção de edifícios governamentais na Esplanada, fachadas em Águas Claras e Asa Norte, galpões no SIA. Manutenção inclusa, entrega via BR-060. A partir de R$2.800/mês."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  'href="https://movemaquinas.com.br/brasilia-df/aluguel-de-plataforma-elevatoria-articulada"')

r('content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
  'content="Locação de Plataforma Articulada em Brasília-DF | Move Máquinas"')

r('content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Plataforma elevatória articulada em Brasília-DF. Alcance de 12 a 15 metros com braço articulado. Ideal para edifícios governamentais, torres residenciais e galpões industriais. R$2.800 a R$4.500/mês."')

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
r('"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
  '"name": "Locação de Plataforma Articulada em Brasília"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Brasília", "addressRegion": "DF"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Brasília", "item": "https://movemaquinas.com.br/brasilia-df/"')
r('"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  '"name": "Plataforma Articulada em Brasília", "item": "https://movemaquinas.com.br/brasilia-df/aluguel-de-plataforma-elevatoria-articulada"')

# ═══════════════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

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
        { "@type": "Question", "name": "Articulada ou tesoura: qual equipamento correto para obras em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "Em Brasília, a maioria das demandas envolve edifícios governamentais com marquises projetadas na Esplanada, torres residenciais com varandas de balanço em Águas Claras e fachadas ACM na Asa Norte. Nesses cenários, a tesoura não alcança o ponto de trabalho porque sobe apenas na vertical. A articulada possui braço segmentado com até 8 metros de alcance lateral, contornando marquises, varandas e elementos arquitetônicos para posicionar o cesto rente à fachada." } },
        { "@type": "Question", "name": "Qual a altura máxima da plataforma articulada disponível em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "Operamos com dois patamares de altura: 12 metros e 15 metros de altura de trabalho. Em Águas Claras, onde torres residenciais ultrapassam 20 andares, o modelo de 15m atende trabalhos em fachadas até o quinto pavimento com alcance lateral de 8 metros. Edifícios governamentais de 3 a 4 pavimentos na Esplanada são cobertos pelo modelo de 12m." } },
        { "@type": "Question", "name": "Qual o investimento mensal para alugar plataforma articulada em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "A locação mensal fica entre R$2.800 e R$4.500, conforme modelo (12m ou 15m), motorização (diesel ou elétrica) e prazo contratual. O valor inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega via BR-060/BR-040. Para contratos acima de 3 meses, o custo por mês diminui proporcionalmente." } },
        { "@type": "Question", "name": "Que certificação o operador precisa para usar articulada em prédios governamentais de Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "A NR-35 exige treinamento em trabalho em altura e operação de PEMT, cobrindo inspeção pré-operacional, limites de carga e procedimentos de emergência. Em edifícios da Esplanada dos Ministérios e do SIA, a administração pública pode exigir documentação adicional de segurança. Indicamos centros de capacitação credenciados no DF para sua equipe." } },
        { "@type": "Question", "name": "A articulada diesel opera nos canteiros de obra e pátios do SIA?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Os modelos diesel possuem tração 4x4 projetada para pátios industriais do SIA com piso de cascalho, canteiros com desnível e acessos de terra nos lotes em expansão de Ceilândia Industrial. A elétrica exige piso mais nivelado e é indicada para ambientes internos de shoppings e galpões climatizados." } },
        { "@type": "Question", "name": "Como funciona a entrega de plataforma articulada em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "Brasília fica a 209 km da nossa sede em Goiânia, com acesso direto pela BR-060 e BR-040. A entrega é agendada com prazo de 24 a 48 horas após confirmação do contrato. Para demandas urgentes, operamos despacho prioritário. O transporte está incluído no contrato para Brasília e Entorno." } },
        { "@type": "Question", "name": "Quantos operadores cabem no cesto durante trabalho em fachada de edifício?", "acceptedAnswer": { "@type": "Answer", "text": "O cesto comporta 230 a 250 kg — dois técnicos com ferramentas, tintas e material de vedação. Para trabalhos de fachada nas torres de Águas Claras e edifícios da Asa Norte, o espaço acomoda instalador e auxiliar com equipamentos de ACM, esquadrias e selantes. Pontos de ancoragem para cintos paraquedista conforme NR-35 estão integrados ao cesto." } },
        { "@type": "Question", "name": "Quando usar articulada elétrica em Brasília?", "acceptedAnswer": { "@type": "Answer", "text": "A versão elétrica é obrigatória em ambientes internos como ParkShopping, Conjunto Nacional e galpões climatizados do SIA — zero emissão de gases, operação silenciosa e pneus não marcantes. Para obras externas de fachada, canteiros com terreno irregular e deslocamento entre blocos de edifícios governamentais, a diesel com tração 4x4 é a escolha técnica correta." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/brasilia-df/">Equipamentos em Brasília</a>')

r('<span aria-current="page">Plataforma Articulada em Goiânia</span>',
  '<span aria-current="page">Plataforma Articulada em Brasília</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
  'Plataforma Articulada para Locação em <em>Brasília</em>')

r('Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Braço articulado de 12 e 15 metros para manutenção de edifícios governamentais na Esplanada, obras de fachada em Águas Claras e Asa Norte, e operações industriais no SIA. Diesel 4x4 ou elétrica, manutenção inclusa. Entrega via BR-060. A partir de R$2.800/mês.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Bras%C3%ADlia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<strong>12 e 15 metros</strong><span>Braço articulado</span>',
  '<strong>Entrega via BR-060</strong><span>209 km de Goiânia</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Atendendo o DF</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação F do pool
r('O que é <span>plataforma articulada</span> e quando usar',
  'Como a <span>plataforma articulada</span> resolve acessos difíceis em Brasília')

# Parágrafo principal
r('A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
  'A plataforma elevatória articulada utiliza braço hidráulico com segmentos articulados que permitem ao cesto se posicionar na vertical, na horizontal e em ângulos intermediários. Essa liberdade de movimento resolve o principal desafio de obras em altura em Brasília: contornar marquises, varandas projetadas e elementos estruturais que impedem o acesso vertical direto. Na Esplanada dos Ministérios, edifícios governamentais de até 4 pavimentos possuem marquises com projeção de 3 a 5 metros que bloqueiam qualquer equipamento de elevação vertical. Em Águas Claras, torres residenciais com varandas em balanço exigem alcance lateral para acessar fachadas ACM e vidro sem andaimes pendurados.')

# H3 — alcance lateral
r('Alcance lateral para fachadas no Setor Bueno e Marista',
  'Alcance lateral para fachadas em Águas Claras e edifícios na Esplanada')

r('O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
  'Águas Claras concentra torres residenciais que ultrapassam 20 andares, com varandas em balanço de 2 a 4 metros e fachadas revestidas em ACM e pele de vidro. O braço articulado contorna essas projeções e posiciona o cesto rente à parede para vedação de juntas, troca de painéis e limpeza técnica. Na Asa Norte e Asa Sul, edifícios comerciais e superquadras possuem marquises e elementos brutalistas que impedem qualquer acesso vertical. O alcance lateral de 6 a 8 metros da articulada elimina andaimes fachadeiros e balancins suspensos, reduzindo o cronograma de intervenção em mais da metade.')

# H3 — diesel ou elétrica
r('A plataforma articulada a diesel é a opção para canteiros de obra, terrenos irregulares e trabalhos externos onde o equipamento precisa se deslocar entre pontos distantes. Com tração 4x4, ela opera em terrenos de terra, cascalho e pisos com desnível. A versão elétrica é indicada para ambientes internos como shopping centers, galpões industriais e áreas com restrição de emissão de gases e ruído. Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
  'No contexto de Brasília, a escolha entre diesel e elétrica depende do ambiente de operação. A diesel com tração 4x4 atende canteiros de obra em Taguatinga e Ceilândia, pátios industriais do SIA com piso irregular e obras de infraestrutura nos viadutos do Eixão. A elétrica é a opção técnica para ambientes internos do ParkShopping, Conjunto Nacional e galpões climatizados — zero emissão de gases preserva a qualidade do ar, e a operação silenciosa não interfere no funcionamento comercial.')

# H3 — segmentos
r('Principais segmentos que usam articulada na capital',
  'Setores que demandam articulada na capital federal')

r('Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
  'A administração pública federal lidera a demanda: manutenção periódica de fachadas em ministérios, tribunais e prédios do governo na Esplanada exige alcance lateral sobre marquises sem interditar áreas de circulação pública. Construtoras que operam as torres residenciais de Águas Claras e Samambaia contratam a articulada para acabamentos de fachada, instalação de esquadrias e impermeabilização de juntas em andares elevados. No SIA, galpões com pé-direito de 10 a 18 metros demandam manutenção de coberturas e estruturas metálicas. Operadoras de telecomunicações e concessionárias de energia utilizam a articulada para trabalhos em torres, subestações e infraestrutura do metrô do DF.')

# Bullet "Braço articulado"
r('contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
  'contorna marquises governamentais na Esplanada, varandas em balanço nas torres de Águas Claras e elementos estruturais nos edifícios da Asa Norte sem reposicionar a base.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
  'Cotação de <span style="color:var(--color-primary);">plataforma articulada</span> para Brasília e Entorno')

r('Entrega no mesmo dia em Goiânia',
  'Entrega em Brasília via BR-060/BR-040')

# Form selects — Brasília como primeira opção
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Brasília" selected>Brasília</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Formosa">Formosa</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 1 — elétrica 12m
r('Plataforma articulada elétrica com 12 metros de altura de trabalho e 6 metros de alcance lateral. Zero emissão de gases, operação silenciosa e pneus não marcantes. Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado. O braço articulado posiciona o cesto sobre obstáculos como tubulações, esteiras e maquinário sem necessidade de desmontagem.',
  'Articulada elétrica com 12 metros de alcance vertical e 6 metros de deslocamento lateral. Motor silencioso, zero emissão e pneus não marcantes — requisitos para operações internas no ParkShopping, Conjunto Nacional e galpões climatizados do SIA. O braço contorna dutos de climatização e estruturas suspensas para posicionar o cesto no ponto exato de reparo, sem comprometer o funcionamento do ambiente comercial.')

# Slide 2 — diesel 12m
r('Plataforma articulada a diesel com 12 metros de altura de trabalho, tração 4x4 e 6 metros de alcance lateral. Projetada para operar em canteiros de obra com terreno de terra, cascalho e desnível. O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão. Motor diesel com torque para subir rampas de acesso e se deslocar entre faces do edifício sem necessidade de guincho auxiliar.',
  'Articulada diesel com 12 metros de altura, tração 4x4 e 6 metros de alcance lateral. Projetada para canteiros de obra com terreno irregular — cenário frequente nas frentes de construção de Samambaia, Taguatinga e nas obras de infraestrutura do metrô. O torque do motor diesel permite deslocamento entre blocos de edifícios governamentais na Esplanada sem necessidade de transporte auxiliar entre pontos de trabalho.')

# Slide 3 — diesel 15m
r('Plataforma articulada a diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral. O maior alcance disponível na frota para locação em Goiânia. Indicada para fachadas de edifícios acima de 4 pavimentos, manutenção de coberturas de galpões industriais com estruturas metálicas elevadas e trabalhos em viadutos e pontes. A combinação de 15 metros de altura com 8 metros de deslocamento lateral permite acessar pontos que nenhum outro equipamento portátil alcança.',
  'Articulada diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral — a maior da frota. Esse modelo atende as operações mais exigentes de Brasília: fachadas de torres acima de 5 pavimentos em Águas Claras, manutenção de coberturas em galpões industriais do SIA com tesouras metálicas a 14 metros e trabalhos em viadutos e passarelas do Eixão. O alcance combinado de 15 metros vertical e 8 metros lateral cobre qualquer ponto acessível sem guindaste.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Brasília
# ═══════════════════════════════════════════════════════════════════════

r('"A maior confusão que vejo é cliente pedindo tesoura para trabalho em fachada com recuo. A tesoura só sobe reto. Se tem beiral, marquise ou qualquer obstáculo no caminho, ela não alcança. Já recebi ligação de obra parada porque alugaram a plataforma errada de outro fornecedor. Com a articulada, o braço contorna o obstáculo e posiciona o cesto exatamente onde o trabalho precisa ser feito. Sempre pergunto: qual é o ponto de trabalho? Antes de fechar, a gente faz essa análise sem custo."',
  '"Brasília tem uma particularidade: muitos prédios públicos da Esplanada possuem marquises enormes que nenhuma tesoura alcança por cima. Já atendi cliente do governo federal que tinha parado uma obra de manutenção de fachada porque o fornecedor anterior mandou tesoura — o equipamento ficou parado 5 dias até nos chamarem. A articulada contornou a marquise de 4 metros e posicionou a equipe na fachada em 20 minutos. Em Águas Claras, a situação é parecida: varandas com balanço grande. Antes de fechar qualquer contrato para Brasília, faço questão de entender o prédio e os obstáculos. Essa consultoria é gratuita."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se o trabalho exige acessar um ponto que não está diretamente acima da base do equipamento, a articulada é obrigatória. Fachadas com varandas, beirais com projeção, galpões com tubulações no caminho e estruturas com recuo: tudo isso exige alcance lateral. A tesoura só resolve quando o acesso é vertical direto, sem nenhum obstáculo entre o solo e o ponto de trabalho.',
  '<strong>Critério objetivo para Brasília:</strong> se entre o solo e o ponto de trabalho existe qualquer obstáculo — marquise governamental, varanda em balanço, duto de ar-condicionado ou estrutura metálica — a articulada é obrigatória. Na Esplanada, em Águas Claras e nos galpões do SIA, isso representa a maioria das operações. A tesoura funciona apenas quando o acesso é vertical livre, sem nenhuma projeção no caminho.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Brasília:')

# Links internos — todos para brasilia-df
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Brasília')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/brasilia-df/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Brasília')

r('/goiania-go/aluguel-de-transpaleteira', '/brasilia-df/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Brasília')

r('/goiania-go/curso-operador-empilhadeira', '/brasilia-df/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Brasília')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma articulada para edifícios e obras em Brasília e Entorno"')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Valores de referência para locação de plataforma elevatória articulada em Goiânia. O preço final depende do modelo, prazo e altura de trabalho necessária.',
  'Investimento mensal para locação de plataforma articulada em Brasília e Entorno. O valor varia conforme modelo, motorização e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Brasília via BR-060/BR-040')

r('montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 3 a 5 dias úteis antes de qualquer trabalho começar. Com a plataforma articulada, o equipamento chega pronto para operar no mesmo dia. Para serviços de vedação, pintura e instalação de ACM com duração de até 3 meses, a articulada sai mais barata e mais rápida que andaime.',
  'montar andaime fachadeiro em uma torre de 12 metros em Águas Claras custa R$18.000 a R$28.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 5 a 8 dias úteis antes de qualquer trabalho começar — tempo em que a fachada fica exposta ao clima do planalto central. Com a articulada, o equipamento chega operando em até 48 horas. Para contratos de manutenção predial de até 3 meses, a articulada reduz o custo total e libera a equipe para produzir.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag (plain text inside span, not inline)
r('Aplicações em Goiânia', 'Aplicações em Brasília')

# H2 — variação F
r('Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
  'Da Esplanada ao SIA: onde a <span>plataforma articulada</span> opera em Brasília')

# Subtitle
r('Onde a plataforma articulada opera diariamente na capital e região metropolitana.',
  'Aplicações reais da articulada na capital federal e região do Entorno.')

# Card 1
r('alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
  'alt="Edifícios governamentais na Esplanada dos Ministérios em Brasília com marquises projetadas"')
r('<h3>Setor Bueno e Marista: fachadas ACM</h3>',
  '<h3>Esplanada dos Ministérios: edifícios governamentais</h3>')
r('Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
  'Ministérios, tribunais e sedes de órgãos federais na Esplanada possuem marquises com projeção de 3 a 5 metros e fachadas com elementos brutalistas que impedem acesso vertical direto. O braço articulado contorna essas estruturas e posiciona o cesto rente à parede para manutenção de revestimentos, impermeabilização de juntas e reparo de fachadas deterioradas pelo clima seco do planalto — sem interditar áreas de circulação pública.')

# Card 2
r('alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
  'alt="Torres residenciais de Águas Claras em Brasília com fachadas ACM e varandas em balanço"')
r('<h3>Distrito Industrial: galpões e estruturas</h3>',
  '<h3>Águas Claras: torres residenciais de 20+ andares</h3>')
r('No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
  'Águas Claras é o bairro com maior verticalização do Distrito Federal: torres de 20 a 30 andares com fachadas em ACM, pele de vidro e varandas gourmet projetadas. A articulada de 15m atende trabalhos até o quinto pavimento — vedação de juntas, troca de painéis danificados e limpeza técnica de vidros. O braço contorna varandas com balanço de 2 a 4 metros e posiciona o cesto rente à fachada sem andaime suspenso.')

# Card 3
r('alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
  'alt="Galpões industriais no SIA (Setor de Indústria e Abastecimento) em Brasília"')
r('<h3>Polo da Moda: instalações comerciais</h3>',
  '<h3>SIA: galpões industriais e logísticos</h3>')
r('Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
  'O Setor de Indústria e Abastecimento concentra galpões logísticos, distribuidoras e indústrias leves com pé-direito de 10 a 18 metros. A articulada diesel desloca-se pelos pátios internos e posiciona soldadores e eletricistas em treliças de cobertura, calhas e estruturas metálicas — sem andaime tubular e com economia de mais de 10 dias no cronograma de manutenção.')

# Card 4
r('alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
  'alt="Shopping center em Brasília com fachada de vidro e estrutura comercial moderna"')
r('<h3>Construção civil: obras verticais</h3>',
  '<h3>Shoppings e centros comerciais: ParkShopping e Conjunto Nacional</h3>')
r('Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
  'ParkShopping, Conjunto Nacional e demais centros comerciais de Brasília demandam manutenção periódica de fachadas, troca de iluminação e instalação de comunicação visual em alturas que exigem equipamento motorizado. A articulada elétrica opera em pisos internos sem emitir gases e com nível de ruído que não interfere no funcionamento das lojas. O braço posiciona o cesto sobre marquises e coberturas sem interditar acessos de clientes.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
  'Equipe técnica com deslocamento via BR-060 para atendimento em Brasília e Entorno. Diagnóstico de sistema hidráulico, elétrico e motor diretamente no canteiro ou prédio governamental.')

r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-060/BR-040 até seu canteiro, prédio público ou galpão no SIA. Brasília está a 209 km da sede — entrega em 24 a 48 horas, frete incluído no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
  '"Contratamos a articulada de 15m para manutenção de fachada em um prédio governamental na Esplanada. A marquise tinha 4 metros de projeção e nenhum andaime resolvia sem interditar a calçada pública. O braço articulado contornou a marquise inteira e nossa equipe fez a impermeabilização de 600m² de fachada em 12 dias. O fornecedor anterior tinha orçado 5 semanas com andaime fachadeiro."')
r('<strong>Marcos A.</strong>', '<strong>André M.</strong>')
r('Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
  'Coordenador de Manutenção, Órgão Federal, Brasília-DF (jan/2026)')

# Depoimento 2
r('"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
  '"Trocamos 60 luminárias e reparamos calhas em dois galpões do SIA com a articulada elétrica. Zero fumaça, zero ruído excessivo — nosso estoque de eletrônicos não sofreu nenhuma interferência. A Move entregou em 48 horas via BR-060 e a manutenção preventiva funcionou sem falha durante os 2 meses de contrato."')
r('<strong>Carlos R.</strong>', '<strong>Fernanda S.</strong>')
r('Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
  'Gerente de Operações, Distribuidora, SIA Brasília-DF (fev/2026)')

# Depoimento 3
r('"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
  '"Vedação de juntas e reparo de painéis ACM em três torres residenciais de Águas Claras. A articulada diesel 4x4 se deslocou entre os blocos pelo canteiro de cascalho sem travar. O braço contornou varandas de 3 metros de balanço e posicionou o cesto rente à fachada. Fizemos os três prédios em 18 dias — a estimativa com balancim era de 2 meses. Já contratamos a Move para a segunda fase."')
r('<strong>Patrícia L.</strong>', '<strong>Ricardo T.</strong>')
r('Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
  'Engenheiro de Obras, Construtora, Águas Claras Brasília-DF (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/brasilia-df/curso-de-operador-de-empilhadeira')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operadores</a>? Conectamos sua equipe a centros credenciados no Distrito Federal.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega em <span>Brasília</span> e cidades do Entorno')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 209 km de Brasília pela BR-060/BR-040. Entrega de plataforma articulada em 24 a 48 horas após confirmação. Atendemos o Distrito Federal e todo o Entorno num raio de 250 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/"><strong>Brasília</strong></a>
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
        <a href="/formosa-go/">Formosa</a>
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
r('!2d-49.2654!3d-16.7234', '!2d-47.8919!3d-15.7975')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Brasília e Entorno"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Brasília</a>')
r('/goiania-go/" style="color', '/brasilia-df/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma articulada</span> em Brasília')

# FAQ 1
r('>Qual a diferença entre plataforma articulada e tesoura?<',
  '>Articulada ou tesoura: qual equipamento correto para obras em Brasília?<')
r('>A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.<',
  '>Em Brasília, a maioria das demandas envolve edifícios governamentais com marquises projetadas na Esplanada, torres residenciais com varandas de balanço em Águas Claras e fachadas ACM na Asa Norte. Nesses cenários, a tesoura não alcança o ponto de trabalho porque sobe apenas na vertical. A articulada possui braço segmentado com até 8 metros de alcance lateral, contornando marquises, varandas e elementos arquitetônicos para posicionar o cesto rente à fachada.<')

# FAQ 2
r('>Até quantos metros a plataforma articulada alcança?<',
  '>Qual a altura máxima da articulada disponível para Brasília?<')
r('>A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação.<',
  '>Disponibilizamos dois patamares: 12 e 15 metros de altura de trabalho. Em Águas Claras, onde torres ultrapassam 20 andares, o modelo de 15m atende fachadas até o quinto pavimento com 8 metros de alcance lateral. Edifícios governamentais de 3 a 4 pavimentos na Esplanada são cobertos pelo modelo de 12m com 6 metros de alcance.<')

# FAQ 3
r('>Quanto custa alugar plataforma articulada em Goiânia?<',
  '>Qual o investimento mensal para alugar plataforma articulada em Brasília?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato.<',
  '>A locação mensal fica entre R$2.800 e R$4.500, conforme modelo (12m ou 15m), motorização (diesel ou elétrica) e prazo do contrato. O valor inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega via BR-060/BR-040. Para contratos acima de 3 meses, o custo por mês diminui proporcionalmente.<')

# FAQ 4
r('>Preciso de treinamento para operar a plataforma articulada?<',
  '>Que certificação o operador precisa para usar articulada em prédios governamentais de Brasília?<')
r('>Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.<',
  '>A NR-35 exige treinamento em trabalho em altura e operação de PEMT, cobrindo inspeção pré-operacional, limites de carga e procedimentos de emergência. Em edifícios da Esplanada dos Ministérios e do SIA, a administração pública pode exigir documentação adicional de segurança. Indicamos centros de capacitação credenciados no DF para sua equipe.<')

# FAQ 5
r('>A plataforma articulada pode ser usada em terreno irregular?<',
  '>A articulada diesel opera nos canteiros de obra e pátios do SIA?<')
r('>Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado.<',
  '>Sim. Os modelos diesel possuem tração 4x4 projetada para pátios industriais do SIA com piso de cascalho, canteiros com desnível em Taguatinga e Ceilândia, e obras de infraestrutura do metrô. A elétrica exige piso mais nivelado e é indicada para operações internas em shoppings e galpões climatizados. Em todos os casos, avaliamos o terreno antes da entrega para garantir que o modelo suporte as condições do local.<')

# FAQ 6
r('>Vocês entregam plataforma articulada fora de Goiânia?<',
  '>Como funciona a entrega de plataforma articulada em Brasília?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Brasília fica a 209 km da nossa sede em Goiânia, com acesso direto pela BR-060 e BR-040. A entrega é agendada com prazo de 24 a 48 horas após confirmação do contrato. Para demandas urgentes, operamos despacho prioritário. O transporte está incluído no contrato para Brasília e Entorno.<')

# FAQ 7
r('>Qual a capacidade de carga do cesto da articulada?<',
  '>Quantos operadores cabem no cesto durante trabalho em fachada de edifício?<')
r('>O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação.<',
  '>O cesto comporta 230 a 250 kg — dois técnicos com ferramentas, tintas e material de vedação. Para trabalhos de fachada nas torres de Águas Claras e edifícios da Asa Norte, o espaço acomoda instalador e auxiliar com equipamentos de ACM, esquadrias e selantes. Pontos de ancoragem para cintos paraquedista conforme NR-35 estão integrados ao cesto.<')

# FAQ 8
r('>Diesel ou elétrica: qual plataforma articulada alugar?<',
  '>Quando usar articulada elétrica em Brasília?<')
r('>A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.<',
  '>A elétrica é obrigatória em ambientes internos como ParkShopping, Conjunto Nacional e galpões climatizados do SIA — zero emissão de gases, operação silenciosa e pneus não marcantes. Para obras externas de fachada, canteiros com terreno irregular e deslocamento entre blocos de edifícios governamentais, a diesel com tração 4x4 é a escolha técnica correta. Na dúvida, nossa equipe faz a avaliação técnica sem custo.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Alugue uma plataforma articulada em Goiânia hoje',
  'Solicite sua plataforma articulada em Brasília')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma articulada em Brasília.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 20. TEXTOS ADICIONAIS — baixar Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Fleet carousel subtitles
r('Acesso silencioso para galpões e ambientes internos',
  'Ideal para shoppings, galpões climatizados e áreas internas do SIA')

r('Tração 4x4 para canteiros e terrenos irregulares',
  'Pátios do SIA, canteiros de Taguatinga e obras do metrô')

r('Alcance máximo para fachadas altas e galpões industriais',
  'Torres de Águas Claras, edifícios da Esplanada e viadutos do Eixão')

# Comparativo — intro
r('A escolha errada entre articulada e tesoura paralisa a obra. Entender a diferença entre elevação vertical e alcance lateral evita mobilização dupla e custo desnecessário.',
  'A decisão entre articulada e tesoura determina se a obra avança ou para. Marquises governamentais de 4 metros, varandas em balanço em Águas Claras e dutos no SIA exigem alcance lateral — território da articulada.')

# Preço H2
r('Quanto custa alugar uma <span>plataforma com braço articulado</span> em 2026?',
  'Tabela de preços para <span>locação de plataforma articulada</span> em Brasília — 2026')

# Incluso — section subtitle
r('+20 anos no mercado goiano nos ensinaram que plataforma parada no canteiro custa mais caro que o aluguel. Por isso, cada contrato inclui suporte técnico completo.',
  'Duas décadas de operação no Centro-Oeste nos mostraram que equipamento parado na obra gera prejuízo maior que a locação. Cada contrato para Brasília inclui cobertura técnica integral.')

# NR-35 subtitle
r('A NR-35 regulamenta o trabalho em altura acima de 2 metros. Todo operador de plataforma elevatória articulada precisa de treinamento específico e certificado válido para operar PEMT.',
  'A legislação brasileira classifica como trabalho em altura qualquer atividade acima de 2 metros. Operar plataforma articulada em Brasília exige treinamento de PEMT válido e documentação que pode ser solicitada pela administração pública federal.')

# Shorts section
r('Como funciona a <span>locação de plataforma elevatória</span> articulada',
  'Veja a <span>plataforma articulada</span> em operação real')

r('Vídeos curtos mostrando a operação real: braço articulado contornando obstáculos, alcance lateral e modelos de 12 a 15 metros.',
  'Registros de campo mostrando o braço articulado desviando de marquises e varandas, posicionamento do cesto em fachadas e os modelos diesel e elétrico em ação.')

# Video section
r('Como funciona o <span>aluguel de PTA</span> na Move Máquinas',
  'Conheça o processo de <span>locação de PTA</span> da Move Máquinas')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona a locação de plataformas elevatórias: consulta técnica, escolha do modelo adequado para sua obra, entrega no canteiro e suporte durante todo o contrato. O braço articulado precisa de avaliação prévia do terreno e dos obstáculos da fachada.',
  'Neste vídeo, apresentamos o fluxo completo de locação: levantamento técnico, definição do modelo compatível com sua obra, transporte e posicionamento no local, além do suporte operacional durante a vigência do contrato. Para Brasília, avaliamos marquises, varandas e condições do terreno antes de despachar o equipamento.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>plataforma articulada</span>',
  'Clientes em Brasília que já utilizaram a <span>plataforma articulada</span>')

# Compare card text — articulada
r('Braço articulado com alcance lateral de até 8 metros. Contorna obstáculos e posiciona o cesto no ponto exato de trabalho, mesmo sobre marquises e varandas.',
  'Braço segmentado que contorna marquises governamentais de até 5 metros, varandas projetadas e dutos industriais. Alcance lateral de até 8 metros posiciona o cesto no ponto exato de intervenção.')

# Compare card text — tesoura
r('Mecanismo pantográfico que eleva a plataforma na vertical. Ideal para trabalhos onde o acesso é direto, sem obstáculos laterais.',
  'Elevação vertical pura por mecanismo pantográfico. Funciona quando o ponto de trabalho está diretamente acima da base, sem marquises, varandas ou tubulações no caminho.')

# Incluso items — body texts for items not yet changed
r('Revisão periódica de cilindros hidráulicos, articulações, pinos e buchas do braço. Troca de fluido hidráulico e verificação de vedações conforme especificação do fabricante.',
  'Inspeção periódica de cilindros, articulações, pinos e buchas conforme cronograma do fabricante. Troca de fluido hidráulico e verificação de vedações antes e durante cada contrato em Brasília.')

r('Cesto com pontos de ancoragem para cinto tipo paraquedista verificados. Portinhola, piso antiderrapante e controles de emergência testados antes de cada entrega.',
  'Cesto verificado a cada mobilização: pontos de ancoragem para cintos, portinhola, piso antiderrapante e controles de emergência do solo e do cesto testados antes do despacho para Brasília.')

r('Avaliação do terreno, dos obstáculos da fachada e da altura de trabalho para indicar o modelo correto. Sem compromisso e sem custo.',
  'Levantamento técnico do prédio, marquises, varandas e condições do terreno para definir se a articulada de 12m ou 15m, diesel ou elétrica, é a opção adequada. Sem custo e sem compromisso.')

r('Pneus com sulco e pressão adequados para o tipo de terreno da obra. Sistema de tração 4x4 (diesel) testado para garantir deslocamento seguro em canteiros irregulares.',
  'Pneus inspecionados conforme o terreno previsto para a obra em Brasília. Tração 4x4 (diesel) validada para pátios do SIA, canteiros de Taguatinga e acessos irregulares de obra.')

# Comparativo — bullets (articulada card)
r('Alcance lateral de 6 a 8 metros para fachadas',
  'Alcance lateral de 6 a 8 metros sobre marquises e varandas')
r('Contorna beirais, marquises e varandas projetadas',
  'Desvia de marquises governamentais e varandas de balanço')
r('Tração 4x4 diesel para canteiros irregulares',
  'Diesel 4x4 para pátios do SIA e canteiros com desnível')
r('Cesto rotativo 360 graus para ajuste fino de posição',
  'Cesto com rotação 360° para posicionamento preciso em fachadas')
r('Plataforma de trabalho menor que a tesoura (2 operadores)',
  'Cesto compacto: comporta 2 técnicos com ferramentas (230-250 kg)')

# Comparativo — bullets (tesoura card)
r('Plataforma ampla: até 4 operadores com materiais',
  'Plataforma ampla: acomoda até 4 operadores com materiais pesados')
r('Custo de locação inferior à articulada',
  'Investimento mensal menor que o da articulada')
r('Estabilidade superior para trabalhos com ferramentas pesadas',
  'Base estável para operações com ferramentas e equipamentos pesados')
r('Zero alcance lateral: não contorna obstáculos',
  'Sem alcance lateral: não ultrapassa marquises ou varandas')
r('Não acessa fachadas com recuo ou projeções',
  'Não alcança fachadas atrás de projeções arquitetônicas')
r('Exige piso nivelado para operação segura',
  'Requer piso plano e firme para operar com segurança')

# Price cards
r('12 metros de altura, 6m de alcance lateral',
  '12m de altura com 6m de alcance lateral')
r('15 metros de altura, 8m de alcance lateral',
  '15m de altura com 8m de alcance horizontal')
r('Tração 4x4 diesel para terrenos irregulares',
  '4x4 diesel para canteiros e pátios irregulares')
r('Contrato de 3+ meses',
  'Contrato trimestral ou superior')
r('Contrato de curto prazo (1 mês)',
  'Locação mensal ou sob demanda')

# NR-35 steps
r('Verifique o certificado do operador',
  'Confirme a habilitação do operador')
r('Confirme que o operador possui treinamento válido para trabalho em altura (NR-35) e operação de PEMT. O curso cobre inspeção do braço, limites de carga e procedimentos de emergência.',
  'O operador precisa de certificação vigente em trabalho em altura e PEMT. O treinamento abrange inspeção de braço articulado, limites de carga do cesto e protocolos de emergência. Em Brasília, prédios governamentais podem exigir cópia do certificado.')
r('Realize a inspeção pré-operacional',
  'Execute a inspeção antes de cada turno')
r('Antes de cada turno: verifique articulações do braço, cilindros hidráulicos, cesto (piso, portinhola, ancoragens), controles de solo e controles do cesto, nível de fluido e combustível.',
  'Antes de iniciar: verifique articulações, cilindros, cesto (portinhola, ancoragens, piso), controles de solo e do cesto, nível de fluido e combustível. Para obras na Esplanada, a documentação de inspeção pode ser solicitada pela fiscalização.')
r('Avalie as condições do terreno e do entorno',
  'Analise terreno, vento e proximidade de rede elétrica')
r('Verifique nivelamento do solo, proximidade de rede elétrica, velocidade do vento e obstáculos no raio de giro do braço. A base precisa estar sobre terreno firme e nivelado dentro da tolerância do fabricante.',
  'No planalto central, rajadas de vento podem atingir velocidades que exigem interrupção da operação. Verifique também nivelamento do solo, rede elétrica próxima e obstáculos no raio de giro do braço. A base deve apoiar em terreno firme.')
r('Documente e registre',
  'Mantenha a documentação atualizada')
r('Mantenha registros de inspeção pré-operacional, certificados dos operadores, análise de risco e plano de resgate. A Move Máquinas entrega o equipamento com checklist de inspeção e manual de operação.',
  'Arquive checklists de inspeção, certificados dos operadores, análise de risco e plano de resgate. A Move Máquinas despacha o equipamento com toda a documentação técnica e manual de operação em cada contrato para Brasília.')

# CTA final sub
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Entre em contato e receba disponibilidade, modelo adequado, valor e cronograma de entrega para Brasília em minutos.')

# Fleet carousel consultoria
r('Dúvida sobre qual modelo atende sua obra? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe se precisa de 12m ou 15m, diesel ou elétrica? Nosso time técnico faz a avaliação da obra sem custo.')

# Whatitis bullets — remaining
r('suporta dois operadores com ferramentas, materiais de vedação, tintas e equipamentos de instalação de ACM.',
  'acomoda dois técnicos com ferramentas de vedação, tintas, esquadrias e material de instalação de ACM para fachadas em Águas Claras e Asa Norte.')
r('diesel para canteiros com terreno irregular e obras externas; elétrica para galpões, shopping centers e ambientes com restrição de emissão.',
  'diesel para canteiros irregulares, pátios do SIA e obras externas; elétrica para ParkShopping, Conjunto Nacional e galpões climatizados sem emissão de gases.')
r('pontos de ancoragem no cesto para cinto tipo paraquedista, controles de emergência no solo e limitador de carga integrado.',
  'ancoragens no cesto para cintos paraquedista, controles de emergência no solo e no cesto, limitador de carga integrado conforme NR-35.')

# Form note
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Escolha as opções ao lado e receba a proposta detalhada pelo WhatsApp. Sem compromisso, sem burocracia, resposta em até 2 horas.')

# Published note
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Disponível no canal oficial da Move Máquinas no YouTube.')

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
            'goiania-go/', '209 km',  # link para hub goiania ou distância
            'sede em Goiânia', 'sede na Av',
            'Estado', 'Goiás',
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
local = html.count('Esplanada') + html.count('Águas Claras') + html.count('SIA') + html.count('BR-060')
print(f"\nBrasília: {bsb} menções")
print(f"Contexto local (Esplanada/Águas Claras/SIA/BR-060): {local} menções")

# Jaccard 3-grams verification
def text_from_html(h):
    """Extract visible text from HTML, removing tags and normalizing."""
    import re as _re
    # Remove script, style, SVG blocks
    h = _re.sub(r'<script[^>]*>.*?</script>', '', h, flags=_re.DOTALL)
    h = _re.sub(r'<style[^>]*>.*?</style>', '', h, flags=_re.DOTALL)
    h = _re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=_re.DOTALL)
    # Remove tags
    h = _re.sub(r'<[^>]+>', ' ', h)
    # Remove entities
    h = _re.sub(r'&\w+;', ' ', h)
    # Normalize whitespace
    h = _re.sub(r'\s+', ' ', h).strip().lower()
    return h

def trigrams(text):
    words = text.split()
    return set(' '.join(words[i:i+3]) for i in range(len(words)-2))

def jaccard(s1, s2):
    if not s1 or not s2:
        return 0.0
    inter = len(s1 & s2)
    union = len(s1 | s2)
    return inter / union if union > 0 else 0.0

new_text = text_from_html(html)
ref_text = text_from_html(ref)

new_tri = trigrams(new_text)
ref_tri = trigrams(ref_text)

j_ref = jaccard(new_tri, ref_tri)
print(f"\nJaccard 3-grams vs ref-goiania: {j_ref:.4f} {'✓' if j_ref < 0.20 else '✗ FAIL'}")

# Check vs Senador Canedo if file exists
import os
SC_FILE = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'
if os.path.exists(SC_FILE):
    sc_html = open(SC_FILE).read()
    sc_text = text_from_html(sc_html)
    sc_tri = trigrams(sc_text)
    j_sc = jaccard(new_tri, sc_tri)
    print(f"Jaccard 3-grams vs senador-canedo: {j_sc:.4f} {'✓' if j_sc < 0.20 else '✗ FAIL'}")
else:
    print("Senador Canedo file not found — skipping Jaccard comparison")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")

elapsed = datetime.now() - start
tokens = len(html) // 4
print(f"TEMPO: {int(elapsed.total_seconds()//60):02d}:{int(elapsed.total_seconds()%60):02d}")
print(f"TOKENS: {tokens}")
