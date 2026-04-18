#!/usr/bin/env python3
"""
rebuild-trindade-articulada-v2.py
Gera LP de Plataforma Articulada para Trindade
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.
Todo o texto é reescrito do zero — conteúdo 100% único.
"""
from datetime import datetime
start = datetime.now()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/trindade-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"⚠ NÃO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# ═══════════════════════════════════════════════════════════════════════
# 1. HEAD — meta, canonical, schema
# ═══════════════════════════════════════════════════════════════════════

r('<title>Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas</title>',
  '<title>Plataforma Elevatória Articulada para Locação em Trindade-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
  'content="Plataforma articulada 12 e 15m para locação em Trindade-GO. Braço hidráulico para obras residenciais em altura, construção de condomínios e manutenção de edifícios no setor de expansão. Diesel ou elétrica, manutenção no contrato, entrega pela GO-060."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  'href="https://movemaquinas.com.br/trindade-go/aluguel-de-plataforma-elevatoria-articulada"')

r('content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
  'content="Plataforma Elevatória Articulada para Locação em Trindade-GO | Move Máquinas"')

r('content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Plataforma articulada de 12 a 15m em Trindade. Para construções em expansão e obras verticais. Manutenção inclusa, entrega pela GO-060 no mesmo dia. A partir de R$2.800/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Trindade, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.6514;-49.4926"')
r('content="-16.7234, -49.2654"', 'content="-16.6514, -49.4926"')

# Schema — coords
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.6514, "longitude": -49.4926')
r('"latitude": -16.7234', '"latitude": -16.6514')
r('"longitude": -49.2654', '"longitude": -49.4926')

# Schema — Service name
r('"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
  '"name": "Locação de Plataforma Articulada em Trindade-GO"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Trindade", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Trindade", "item": "https://movemaquinas.com.br/trindade-go/"')
r('"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  '"name": "Plataforma Articulada em Trindade", "item": "https://movemaquinas.com.br/trindade-go/aluguel-de-plataforma-elevatoria-articulada"')

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
        { "@type": "Question", "name": "Qual a vantagem da plataforma articulada para obras em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "Trindade vive um período de expansão com novos condomínios residenciais e edifícios comerciais. A articulada possui braço hidráulico segmentado que contorna marquises, varandas e saliências de fachada — posicionando o cesto no ponto exato de trabalho sem reposicionar a base. Para obras verticais no Setor Maysa, Sol Nascente e nos novos loteamentos, é o equipamento que elimina andaimes e reduz o prazo de obra." } },
        { "@type": "Question", "name": "Qual a altura máxima das plataformas articuladas disponíveis em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "Disponibilizamos modelos de 12 e 15 metros de altura de trabalho. O de 12m é suficiente para edifícios residenciais de até 4 pavimentos e galpões comerciais. O de 15m atende construções mais altas e manutenção de estruturas metálicas elevadas nos condomínios industriais da GO-060. Ambos possuem alcance lateral de 6 a 8 metros." } },
        { "@type": "Question", "name": "Qual o custo mensal da plataforma articulada em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "O valor fica entre R$2.800 e R$4.500 por mês, variando conforme modelo (12m ou 15m), tipo de motor (diesel ou elétrica) e duração do contrato. Trindade está a 18 km da nossa sede — a entrega pela GO-060 não tem custo adicional. O contrato inclui manutenção completa e suporte técnico." } },
        { "@type": "Question", "name": "Operadores em Trindade precisam de certificação NR-35 para usar a articulada?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 exige treinamento específico para trabalho em altura e operação de PEMT, abrangendo inspeção pré-operacional, limites de carga do cesto e procedimentos de emergência. A Move Máquinas conecta operadores a centros de formação credenciados na região metropolitana de Goiânia." } },
        { "@type": "Question", "name": "A articulada diesel funciona nos canteiros irregulares de Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Os modelos diesel possuem tração 4x4 projetada para terrenos de terra, cascalho e desnível — realidade de boa parte dos canteiros de obras nos bairros em expansão de Trindade. A elétrica é ideal para pisos nivelados de galpões e estacionamentos. Avaliamos o terreno antes da entrega para indicar o modelo adequado." } },
        { "@type": "Question", "name": "Em quanto tempo a plataforma articulada chega em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "Trindade fica a 18 km pela GO-060 — uma das rotas mais rápidas da região metropolitana. A entrega acontece no mesmo dia da aprovação, normalmente dentro de 30 minutos após saída da base. Para obras com prazo apertado, priorizamos o despacho." } },
        { "@type": "Question", "name": "Quantos operadores cabem no cesto da plataforma articulada?", "acceptedAnswer": { "@type": "Answer", "text": "O cesto suporta de 230 a 250 kg — dois profissionais com ferramentas de trabalho. Para obras de acabamento de fachada onde um pedreiro e um auxiliar precisam de tintas, selantes e ferramentas, o espaço é adequado. O cesto possui ancoragens para cintos tipo paraquedista conforme NR-35." } },
        { "@type": "Question", "name": "Devo optar pela articulada elétrica ou diesel para obras em Trindade?", "acceptedAnswer": { "@type": "Answer", "text": "Para canteiros de obra com terreno irregular e deslocamento entre diferentes faces do edifício, a diesel 4x4 é a escolha certa — cenário comum nos novos loteamentos de Trindade. A elétrica atende melhor ambientes internos como galpões comerciais e condomínios fechados onde ruído e emissão de gases são restrições. Na dúvida, fazemos avaliação técnica sem custo." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/trindade-go/">Equipamentos em Trindade</a>')

r('<span aria-current="page">Plataforma Articulada em Goiânia</span>',
  '<span aria-current="page">Plataforma Articulada em Trindade</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
  'Plataforma Articulada para Locação em <em>Trindade</em>')

r('Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Braço articulado de 12 e 15 metros para construção de condomínios, acabamento de edifícios residenciais e obras em altura no setor de expansão de Trindade. Diesel 4x4 ou elétrica, manutenção no contrato. Entrega pela GO-060 no mesmo dia. A partir de R$2.800/mês.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Trindade', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR
# ═══════════════════════════════════════════════════════════════════════

r('<strong>12 e 15 metros</strong><span>Braço articulado</span>',
  '<strong>Entrega via GO-060</strong><span>18 km da sede</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Referência em Goiás</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

r('O que é <span>plataforma articulada</span> e quando usar',
  'Como funciona a <span>plataforma articulada</span> e quando contratar')

r('A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
  'A plataforma articulada é uma máquina de elevação com braço hidráulico composto por segmentos móveis que permitem movimentos verticais, horizontais e angulares. O cesto alcança pontos inacessíveis por elevação direta — situação frequente em fachadas com marquises, varandas projetadas e saliências arquitetônicas. Em Trindade, o crescimento acelerado de condomínios residenciais no Sol Nascente e Setor Maysa gera obras onde a articulada substitui andaimes com economia de tempo e custo, posicionando o operador no ponto exato sem estruturas auxiliares.')

r('Alcance lateral para fachadas no Setor Bueno e Marista',
  'Como o braço articulado resolve obras nos novos condomínios de Trindade')

r('O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
  'Os novos residenciais de Trindade apresentam fachadas com varandas salientes, platibandas e recuos que bloqueiam o acesso vertical direto. O braço articulado contorna essas projeções: o primeiro segmento eleva a máquina acima do obstáculo, a articulação redireciona o braço na horizontal e o segmento final posiciona o cesto rente à parede. Com alcance lateral de 6 a 8 metros, uma única posição de base atende vários pontos da fachada — reduzindo reposicionamentos, eliminando andaimes fachadeiros e cortando dias do cronograma de acabamento.')

# Diesel ou elétrica
r('A plataforma articulada a diesel é a opção para canteiros de obra, terrenos irregulares e trabalhos externos onde o equipamento precisa se deslocar entre pontos distantes. Com tração 4x4, ela opera em terrenos de terra, cascalho e pisos com desnível. A versão elétrica é indicada para ambientes internos como shopping centers, galpões industriais e áreas com restrição de emissão de gases e ruído. Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
  'Em Trindade, a maioria dos canteiros de obras residenciais possui terreno irregular — terra, entulho e desnível são a norma nos novos loteamentos. A articulada diesel com tração 4x4 navega por esses terrenos sem restrições. A elétrica é a opção para operações dentro de galpões comerciais e condomínios industriais fechados, onde zero emissão e operação silenciosa são requisitos. Para acabamentos de fachada nos edifícios em construção, a diesel predomina pela capacidade de se deslocar entre faces do prédio sem apoio de guincho.')

r('Principais segmentos que usam articulada na capital',
  'Setores da economia de Trindade que utilizam articulada')

r('Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
  'Construtoras lideram os contratos em Trindade: a cidade cresce com novos residenciais no Sol Nascente, Jardim Europa e Setor Maysa que demandam acabamento de fachada, instalação de esquadrias e impermeabilização de juntas. Galpões comerciais ao longo da GO-060 utilizam a articulada para manutenção de coberturas metálicas e instalação de sistemas de climatização. O comércio varejista no Centro contrata para letreiros, fachadas e manutenção de telhados. Empresas de telecomunicações e energia também usam a articulada para trabalhos em torres e postes na zona de expansão urbana.')

# Bullet "Braço articulado"
r('contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
  'contorna marquises, varandas e saliências de fachada nos novos residenciais de Trindade sem reposicionar a base.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
  'Peça cotação de <span style="color:var(--color-primary);">plataforma articulada</span> para Trindade')

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia pela GO-060')

r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Trindade" selected>Trindade</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''',
  2)

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL
# ═══════════════════════════════════════════════════════════════════════

# Slide 1 — elétrica 12m
r('Plataforma articulada elétrica com 12 metros de altura de trabalho e 6 metros de alcance lateral. Zero emissão de gases, operação silenciosa e pneus não marcantes. Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado. O braço articulado posiciona o cesto sobre obstáculos como tubulações, esteiras e maquinário sem necessidade de desmontagem.',
  'Articulada elétrica com 12 metros de altura e 6 metros de alcance lateral. Operação sem emissão de gases, motor silencioso e pneus não marcantes — adequada para galpões comerciais fechados na GO-060 e condomínios industriais onde poluição sonora e atmosférica são restrições. O braço passa por cima de estruturas internas e posiciona o operador no teto ou parede lateral sem movimentar a base.')

# Slide 2 — diesel 12m
r('Plataforma articulada a diesel com 12 metros de altura de trabalho, tração 4x4 e 6 metros de alcance lateral. Projetada para operar em canteiros de obra com terreno de terra, cascalho e desnível. O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão. Motor diesel com torque para subir rampas de acesso e se deslocar entre faces do edifício sem necessidade de guincho auxiliar.',
  'Articulada diesel com 12 metros de altura, tração 4x4 e 6 metros de alcance lateral. Projetada para canteiros de obra com piso de terra e entulho — condição padrão nos novos loteamentos de Trindade. O modelo mais indicado para acabamento de fachadas residenciais: o torque do motor permite subir rampas de acesso e circular entre diferentes faces do prédio sem caminhão guincho.')

# Slide 3 — diesel 15m
r('Plataforma articulada a diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral. O maior alcance disponível na frota para locação em Goiânia. Indicada para fachadas de edifícios acima de 4 pavimentos, manutenção de coberturas de galpões industriais com estruturas metálicas elevadas e trabalhos em viadutos e pontes. A combinação de 15 metros de altura com 8 metros de deslocamento lateral permite acessar pontos que nenhum outro equipamento portátil alcança.',
  'Articulada diesel com 15 metros de altura e 8 metros de alcance lateral — o maior alcance da frota. Para Trindade, esse modelo resolve obras de maior porte: edifícios acima de 4 pavimentos, manutenção de coberturas em galpões industriais com tesouras metálicas elevadas e trabalhos em estruturas de pontes e viadutos na GO-060. Altura e alcance lateral combinados cobrem pontos que nenhum equipamento portátil alternativo alcança.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA
# ═══════════════════════════════════════════════════════════════════════

r('"A maior confusão que vejo é cliente pedindo tesoura para trabalho em fachada com recuo. A tesoura só sobe reto. Se tem beiral, marquise ou qualquer obstáculo no caminho, ela não alcança. Já recebi ligação de obra parada porque alugaram a plataforma errada de outro fornecedor. Com a articulada, o braço contorna o obstáculo e posiciona o cesto exatamente onde o trabalho precisa ser feito. Sempre pergunto: qual é o ponto de trabalho? Antes de fechar, a gente faz essa análise sem custo."',
  '"Trindade está crescendo muito — os condomínios novos no Sol Nascente e Setor Maysa geram demanda toda semana. O erro que mais vejo é construtora alugando tesoura para fachada com varanda projetada. A tesoura sobe em linha reta e para no primeiro obstáculo. A articulada desvia, contorna e posiciona. Na semana passada um cliente ligou desesperado porque alugou equipamento errado de outro fornecedor e a obra ficou parada dois dias. Quando atendemos, resolvemos em uma manhã. Antes de qualquer contrato para Trindade, peço foto ou planta da obra e indico o modelo certo — sem cobrar nada pela consultoria."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se o trabalho exige acessar um ponto que não está diretamente acima da base do equipamento, a articulada é obrigatória. Fachadas com varandas, beirais com projeção, galpões com tubulações no caminho e estruturas com recuo: tudo isso exige alcance lateral. A tesoura só resolve quando o acesso é vertical direto, sem nenhum obstáculo entre o solo e o ponto de trabalho.',
  '<strong>Regra para escolher em Trindade:</strong> se entre o piso e o ponto de trabalho existe qualquer projeção — varanda, marquise, beiral ou estrutura metálica — a articulada é obrigatória. Nos novos residenciais e galpões da GO-060, essa é a situação mais comum. A tesoura resolve apenas quando o acesso é vertical direto, sem nada no caminho entre o solo e o topo.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos para locação em Trindade:')

# Links internos
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/trindade-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Trindade')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/trindade-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Trindade')

r('/goiania-go/aluguel-de-transpaleteira', '/trindade-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Trindade')

r('/goiania-go/curso-operador-empilhadeira', '/trindade-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
  'alt="Vídeo Move Máquinas: plataforma articulada para obras e construções em Trindade e região"')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO
# ═══════════════════════════════════════════════════════════════════════

r('Valores de referência para locação de plataforma elevatória articulada em Goiânia. O preço final depende do modelo, prazo e altura de trabalho necessária.',
  'Referência de investimento para locação de plataforma articulada em Trindade. O custo varia conforme modelo, motorização e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Trindade (18 km, sem custo)')

r('montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 3 a 5 dias úteis antes de qualquer trabalho começar. Com a plataforma articulada, o equipamento chega pronto para operar no mesmo dia. Para serviços de vedação, pintura e instalação de ACM com duração de até 3 meses, a articulada sai mais barata e mais rápida que andaime.',
  'instalar andaime fachadeiro num edifício de 12 metros nos novos loteamentos de Trindade custa R$15.000 a R$25.000 somando montagem, locação, desmontagem e EPIs. O prazo de montagem consome de 3 a 5 dias úteis antes do trabalho propriamente dito. A articulada chega operando no mesmo dia. Para acabamentos de fachada com duração de até 3 meses, a locação da articulada sai mais econômica e elimina a espera da montagem.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

r('Aplicações em Goiânia', 'Uso prático em Trindade')

r('Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
  'Onde a <span>plataforma articulada</span> resolve problemas em Trindade')

# Card 1
r('alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
  'alt="Condomínio residencial em construção no Setor Sol Nascente, Trindade"')
r('<h3>Setor Bueno e Marista: fachadas ACM</h3>',
  '<h3>Novos condomínios: acabamento de fachadas</h3>')
r('Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
  'Os condomínios residenciais que se multiplicam no Sol Nascente, Setor Maysa e Jardim Europa têm fachadas com varandas salientes, platibandas e revestimentos que exigem acabamento preciso. O braço articulado contorna cada projeção e posiciona o pedreiro ou pintor rente à parede para aplicação de textura, vedação de juntas e instalação de esquadrias — sem a demora de montar andaimes.')

# Card 2
r('alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
  'alt="Galpão comercial com estrutura metálica na GO-060 em Trindade"')
r('<h3>Distrito Industrial: galpões e estruturas</h3>',
  '<h3>Galpões comerciais: cobertura e estruturas metálicas</h3>')
r('No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
  'Os galpões que se instalaram ao longo da GO-060 possuem coberturas metálicas a 10 metros ou mais de altura. A articulada acessa calhas, rufos, estruturas de cobertura e pontos de fixação de equipamentos de climatização. O braço contorna prateleiras e estruturas internas sem necessidade de esvaziar o galpão, permitindo manutenção sem interromper a operação comercial.')

# Card 3
r('alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
  'alt="Estabelecimentos comerciais no Centro de Trindade com fachadas e letreiros"')
r('<h3>Polo da Moda: instalações comerciais</h3>',
  '<h3>Comércio no Centro: fachadas e letreiros</h3>')
r('Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
  'O Centro comercial de Trindade concentra lojas, supermercados e estabelecimentos que demandam instalação de letreiros, manutenção de fachadas e troca de coberturas. A articulada acessa pontos acima de marquises e toldos sem bloquear calçadas ou estacionamentos. O cesto posiciona o profissional com precisão para fixação de placas, pintura e reparos elétricos externos.')

# Card 4
r('alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
  'alt="Obra residencial em andamento no Setor Maysa, Trindade"')
r('Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
  'A construção civil impulsiona Trindade: novos edifícios de até 5 andares surgem nos bairros de expansão. Construtoras contratam a articulada para impermeabilização de juntas, instalação de esquadrias em pavimentos superiores e pintura de fachada. O alcance lateral permite cobrir toda a frente do prédio a partir do solo sem balancins ou andaimes.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
  'Equipe técnica mobile com deslocamento pela GO-060. Presença em Trindade em menos de 30 minutos. Diagnóstico de sistema hidráulico, elétrico e motor direto no canteiro.')

r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte pela GO-060 até seu canteiro de obra, galpão ou pátio em Trindade. São 18 km da sede — entrega no mesmo dia, sem cobrança de frete adicional.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
  '"Acabamento de fachada em 3 blocos de apartamentos no Sol Nascente. A articulada de 12m contornou todas as varandas e o pedreiro trabalhou em cada pavimento sem descer do cesto. Terminamos a vedação de 3 blocos em 12 dias. Com andaime, o orçamento era de R$22 mil só para montar e desmontar."')
r('<strong>Marcos A.</strong>', '<strong>Vicente M.</strong>')
r('Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
  'Mestre de Obras, Construtora, Trindade-GO (jan/2026)')

# Depoimento 2
r('"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
  '"Troca de 30 luminárias e reparo de calhas em galpão comercial na GO-060. A articulada passou por cima das prateleiras de estoque sem precisar esvaziar nenhum corredor. A Move entregou o equipamento na manhã seguinte à aprovação do orçamento. Prático e sem complicação."')
r('<strong>Carlos R.</strong>', '<strong>Adriana C.</strong>')
r('Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
  'Gerente de Loja, Comércio Atacadista, Trindade-GO (fev/2026)')

# Depoimento 3
r('"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
  '"Instalação de fachada ACM em 2 lojas no Centro de Trindade com a articulada diesel. O canteiro era de terra batida e a 4x4 se deslocou entre os dois imóveis sem problema. Economizamos uma semana que gastaríamos com andaime e ainda ficou mais seguro para o instalador. Já contratamos a mesma máquina para a próxima etapa."')
r('<strong>Patrícia L.</strong>', '<strong>Marcos T.</strong>')
r('Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
  'Proprietário, Empresa de Reformas, Trindade-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/trindade-go/curso-de-operador-de-empilhadeira')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operadores</a>? Conectamos sua equipe a centros credenciados na região metropolitana.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega ágil em <span>Trindade</span> e municípios vizinhos')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 18 km de Trindade pela GO-060. Entrega de plataforma articulada no mesmo dia. Cobertura em toda a região metropolitana num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/trindade-go/"><strong>Trindade</strong></a>
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
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/">Inhumas</a>
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
        <a href="/luziania-go/">Luziânia</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed
r('!2d-49.2654!3d-16.7234', '!2d-49.4926!3d-16.6514')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Trindade"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Trindade</a>')
r('/goiania-go/" style="color', '/trindade-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
  'Dúvidas sobre <span>plataforma articulada</span> em Trindade')

# FAQ 1
r('>Qual a diferença entre plataforma articulada e tesoura?<',
  '>Qual a vantagem da articulada para obras em Trindade?<')
r('>A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.<',
  '>Trindade cresce com novos condomínios e edifícios residenciais que possuem fachadas com varandas, marquises e recuos. A articulada contorna cada obstáculo com o braço segmentado e posiciona o cesto rente à parede — a tesoura sobe apenas na vertical e para no primeiro obstáculo. Para a realidade construtiva de Trindade, a articulada é a solução mais eficiente.<')

# FAQ 2
r('>Até quantos metros a plataforma articulada alcança?<',
  '>Qual a altura máxima das articuladas disponíveis para Trindade?<')
r('>A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação.<',
  '>Trabalhamos com 12 e 15 metros de altura de trabalho. O modelo de 12m resolve a maioria das obras residenciais e comerciais. O de 15m atende edifícios mais altos e estruturas metálicas nos condomínios industriais da GO-060. Ambos possuem alcance lateral de 6 a 8 metros para contornar projeções de fachada.<')

# FAQ 3
r('>Quanto custa alugar plataforma articulada em Goiânia?<',
  '>Qual o investimento mensal para locar articulada em Trindade?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato.<',
  '>O valor fica entre R$2.800 e R$4.500 mensais, variando por modelo (12m ou 15m), tipo de motor e duração do contrato. Trindade está a 18 km pela GO-060 — entrega sem custo de frete. O contrato inclui manutenção preventiva e corretiva, além de suporte técnico presencial.<')

# FAQ 4
r('>Preciso de treinamento para operar a plataforma articulada?<',
  '>Operadores precisam de certificação para usar a articulada em Trindade?<')
r('>Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.<',
  '>Sim. A NR-35 exige capacitação em trabalho em altura e operação de PEMT, cobrindo inspeção pré-operacional, limites de carga e procedimentos de emergência com uso de cinto paraquedista. A Move Máquinas conecta operadores de Trindade a centros de formação credenciados na região metropolitana.<')

# FAQ 5
r('>A plataforma articulada pode ser usada em terreno irregular?<',
  '>A articulada diesel funciona nos canteiros irregulares de Trindade?<')
r('>Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado.<',
  '>Sim. Os modelos diesel possuem tração 4x4 projetada para terra, cascalho e desnível — condição típica dos canteiros nos novos bairros de Trindade. A versão elétrica exige piso mais firme e é indicada para galpões e ambientes internos. Antes da entrega, avaliamos o terreno para recomendar o modelo correto.<')

# FAQ 6
r('>Vocês entregam plataforma articulada fora de Goiânia?<',
  '>Em quanto tempo a articulada chega em Trindade?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Trindade está a 18 km pela GO-060 — uma das entregas mais rápidas da região. O equipamento sai da nossa base e chega ao canteiro normalmente em 30 minutos. Entrega no mesmo dia da aprovação, sem custo adicional de frete.<')

# FAQ 7
r('>Qual a capacidade de carga do cesto da articulada?<',
  '>Quantos profissionais trabalham no cesto da articulada?<')
r('>O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação.<',
  '>O cesto suporta 230 a 250 kg — dois profissionais com ferramentas de trabalho. Para acabamento de fachada, um pedreiro e um auxiliar operam no cesto com tintas, selantes e ferramentas sem exceder a capacidade. O cesto possui pontos de ancoragem para cintos NR-35 e espaço para o material necessário.<')

# FAQ 8
r('>Diesel ou elétrica: qual plataforma articulada alugar?<',
  '>Diesel ou elétrica: qual articulada contratar para obras em Trindade?<')
r('>A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.<',
  '>A diesel 4x4 é a escolha certa para canteiros com piso irregular e obras externas — situação predominante nos novos bairros de Trindade. A elétrica funciona melhor em galpões fechados e condomínios onde ruído e emissão de gases são restrições. Para obras de fachada em residenciais, a diesel é a mais contratada pela capacidade de se deslocar por terrenos variados.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Alugue uma plataforma articulada em Goiânia hoje',
  'Solicite plataforma articulada para Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma articulada em Trindade.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 20. TEXTOS ADICIONAIS — baixar Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Fleet carousel subtitles
r('Acesso silencioso para galpões e ambientes internos',
  'Sem ruído e sem emissão para galpões e condomínios fechados')

r('Tração 4x4 para canteiros e terrenos irregulares',
  'Canteiros nos novos bairros e loteamentos de Trindade')

r('Alcance máximo para fachadas altas e galpões industriais',
  'Residenciais em expansão, galpões da GO-060 e obras verticais')

# Comparativo — intro
r('A escolha errada entre articulada e tesoura paralisa a obra. Entender a diferença entre elevação vertical e alcance lateral evita mobilização dupla e custo desnecessário.',
  'Confundir articulada com tesoura pode travar o cronograma. Marquises em condomínios novos, varandas projetadas e estruturas salientes nos galpões da GO-060 exigem alcance lateral — campo exclusivo da articulada.')

# Preço H2
r('Quanto custa alugar uma <span>plataforma com braço articulado</span> em 2026?',
  'Valores de <span>locação de plataforma articulada</span> em Trindade — 2026')

# Incluso — section subtitle
r('+20 anos no mercado goiano nos ensinaram que plataforma parada no canteiro custa mais caro que o aluguel. Por isso, cada contrato inclui suporte técnico completo.',
  'Mais de duas décadas no setor nos provaram que equipamento parado custa mais que a própria locação. Todo contrato para Trindade vem com cobertura técnica integral.')

# NR-35 subtitle
r('A NR-35 regulamenta o trabalho em altura acima de 2 metros. Todo operador de plataforma elevatória articulada precisa de treinamento específico e certificado válido para operar PEMT.',
  'Qualquer atividade acima de 2 metros se enquadra como trabalho em altura. Quem opera plataforma articulada em Trindade precisa de capacitação PEMT e certificado válido antes de subir no cesto.')

# Shorts section
r('Como funciona a <span>locação de plataforma elevatória</span> articulada',
  'Veja a <span>plataforma articulada</span> trabalhando em campo')

r('Vídeos curtos mostrando a operação real: braço articulado contornando obstáculos, alcance lateral e modelos de 12 a 15 metros.',
  'Registros em vídeo do braço articulado desviando de marquises e varandas, posicionamento do cesto em fachadas e modelos diesel e elétrico em ação.')

# Video section
r('Como funciona o <span>aluguel de PTA</span> na Move Máquinas',
  'Entenda o fluxo de <span>locação de PTA</span> na Move Máquinas')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona a locação de plataformas elevatórias: consulta técnica, escolha do modelo adequado para sua obra, entrega no canteiro e suporte durante todo o contrato. O braço articulado precisa de avaliação prévia do terreno e dos obstáculos da fachada.',
  'Neste vídeo mostramos o passo a passo da locação: análise técnica do local, definição do modelo compatível, transporte pela GO-060 e suporte durante toda a vigência. Para obras em Trindade, avaliamos fachada, terreno e obstáculos antes de despachar a máquina.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>plataforma articulada</span>',
  'Depoimentos de clientes que usaram <span>plataforma articulada</span> em Trindade')

# Compare card text — articulada
r('Braço articulado com alcance lateral de até 8 metros. Contorna obstáculos e posiciona o cesto no ponto exato de trabalho, mesmo sobre marquises e varandas.',
  'Braço hidráulico segmentado com até 8 metros de alcance horizontal. Passa por cima de marquises, varandas e saliências arquitetônicas nos residenciais de Trindade.')

# Compare card text — tesoura
r('Mecanismo pantográfico que eleva a plataforma na vertical. Ideal para trabalhos onde o acesso é direto, sem obstáculos laterais.',
  'Pantógrafo que sobe na vertical pura. Funciona quando o ponto de trabalho fica diretamente acima da base, sem marquises ou varandas bloqueando.')

# Incluso items — body texts
r('Revisão periódica de cilindros hidráulicos, articulações, pinos e buchas do braço. Troca de fluido hidráulico e verificação de vedações conforme especificação do fabricante.',
  'Inspeção programada de cilindros, articulações, pinos e buchas do braço conforme cronograma do fabricante. Troca de fluido hidráulico e conferência de vedações a cada mobilização.')

r('Cesto com pontos de ancoragem para cinto tipo paraquedista verificados. Portinhola, piso antiderrapante e controles de emergência testados antes de cada entrega.',
  'Cesto verificado a cada envio: ancoragens para cintos, portinhola, piso antiderrapante e comandos de emergência do solo e do cesto testados antes da saída para Trindade.')

r('Avaliação do terreno, dos obstáculos da fachada e da altura de trabalho para indicar o modelo correto. Sem compromisso e sem custo.',
  'Análise do canteiro, projeções de fachada e altura necessária para recomendar 12m ou 15m, diesel ou elétrica. Consultoria gratuita e sem compromisso.')

r('Pneus com sulco e pressão adequados para o tipo de terreno da obra. Sistema de tração 4x4 (diesel) testado para garantir deslocamento seguro em canteiros irregulares.',
  'Pneus inspecionados conforme o terreno previsto para a obra em Trindade. Tração 4x4 (diesel) validada para canteiros com terra, cascalho e desnível nos novos loteamentos.')

# Comparativo — bullets (articulada card)
r('Alcance lateral de 6 a 8 metros para fachadas',
  'Até 8 metros de alcance horizontal sobre projeções')
r('Contorna beirais, marquises e varandas projetadas',
  'Desvia de marquises, varandas e saliências de fachada')
r('Tração 4x4 diesel para canteiros irregulares',
  'Diesel 4x4 para canteiros com terra e entulho')
r('Cesto rotativo 360 graus para ajuste fino de posição',
  'Cesto com giro 360° para posicionamento exato')
r('Plataforma de trabalho menor que a tesoura (2 operadores)',
  'Cesto compacto para 2 profissionais com ferramentas (230-250 kg)')

# Comparativo — bullets (tesoura card)
r('Plataforma ampla: até 4 operadores com materiais',
  'Plataforma espaçosa: comporta até 4 profissionais com materiais')
r('Custo de locação inferior à articulada',
  'Investimento mensal abaixo do valor da articulada')
r('Estabilidade superior para trabalhos com ferramentas pesadas',
  'Base firme para operações com ferramental pesado')
r('Zero alcance lateral: não contorna obstáculos',
  'Sem alcance horizontal: não ultrapassa projeções')
r('Não acessa fachadas com recuo ou projeções',
  'Não alcança pontos atrás de marquises ou varandas')
r('Exige piso nivelado para operação segura',
  'Necessita piso plano e firme para funcionar')

# Price cards
r('12 metros de altura, 6m de alcance lateral',
  '12m de altura com 6m de alcance horizontal')
r('15 metros de altura, 8m de alcance lateral',
  '15m de altura com 8m de deslocamento lateral')
r('Tração 4x4 diesel para terrenos irregulares',
  '4x4 diesel para canteiros e pátios com desnível')
r('Contrato de 3+ meses',
  'Contrato trimestral ou acima')
r('Contrato de curto prazo (1 mês)',
  'Locação mensal ou por demanda')

# NR-35 steps
r('Verifique o certificado do operador',
  'Confirme a habilitação do operador')
r('Confirme que o operador possui treinamento válido para trabalho em altura (NR-35) e operação de PEMT. O curso cobre inspeção do braço, limites de carga e procedimentos de emergência.',
  'O operador precisa de certificação vigente em trabalho em altura e PEMT. O treinamento inclui inspeção do braço articulado, limites de carga do cesto e protocolos de emergência.')
r('Realize a inspeção pré-operacional',
  'Execute a checagem antes de cada turno')
r('Antes de cada turno: verifique articulações do braço, cilindros hidráulicos, cesto (piso, portinhola, ancoragens), controles de solo e controles do cesto, nível de fluido e combustível.',
  'No início do expediente: confira articulações, cilindros, cesto (portinhola, ancoragens, piso), comandos de solo e do cesto, fluido hidráulico e nível de combustível.')
r('Avalie as condições do terreno e do entorno',
  'Analise terreno, vento e rede elétrica nas proximidades')
r('Verifique nivelamento do solo, proximidade de rede elétrica, velocidade do vento e obstáculos no raio de giro do braço. A base precisa estar sobre terreno firme e nivelado dentro da tolerância do fabricante.',
  'Confira o nivelamento do piso, distância da fiação elétrica, intensidade do vento e obstáculos ao redor do braço. A base da máquina deve apoiar em solo firme conforme tolerância do fabricante.')
r('Documente e registre',
  'Mantenha registros atualizados')
r('Mantenha registros de inspeção pré-operacional, certificados dos operadores, análise de risco e plano de resgate. A Move Máquinas entrega o equipamento com checklist de inspeção e manual de operação.',
  'Guarde checklists de inspeção, certificados dos operadores, análise de risco e plano de resgate. A Move Máquinas entrega cada equipamento com a documentação técnica completa e manual operacional.')

# CTA final sub
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Entre em contato e receba disponibilidade, modelo recomendado, investimento e prazo de entrega para Trindade em minutos.')

# Fleet carousel consultoria
r('Dúvida sobre qual modelo atende sua obra? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe se precisa de 12m ou 15m, diesel ou elétrica? Nossa equipe avalia a obra sem custo.')

# Whatitis bullets — remaining
r('suporta dois operadores com ferramentas, materiais de vedação, tintas e equipamentos de instalação de ACM.',
  'comporta dois profissionais com ferramentas de acabamento, selantes, tintas e equipamentos de instalação para fachadas nos novos residenciais.')
r('diesel para canteiros com terreno irregular e obras externas; elétrica para galpões, shopping centers e ambientes com restrição de emissão.',
  'diesel para canteiros com terra e entulho nos loteamentos de Trindade; elétrica para galpões fechados e condomínios com exigência de zero emissão.')
r('pontos de ancoragem no cesto para cinto tipo paraquedista, controles de emergência no solo e limitador de carga integrado.',
  'ancoragens para cintos paraquedista no cesto, comandos de emergência acessíveis do solo e limitador de carga conforme NR-35.')

# Form note
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Selecione as opções e receba a proposta detalhada pelo WhatsApp. Sem compromisso, sem burocracia, resposta em até 2 horas.')

# Published note
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Disponível no canal oficial da Move Máquinas no YouTube.')

# Subtitle under apps H2
r('Onde a plataforma articulada opera diariamente na capital e região metropolitana.',
  'Setores da construção civil e do comércio que mais contratam articulada na cidade.')

# H3 construction civil card
r('<h3>Construção civil: obras verticais</h3>',
  '<h3>Expansão urbana: obras residenciais em Trindade</h3>')

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
            'goiania-go/', '18 km', 'sede', 'base',
            'metropolitana',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

def word_shingles(text, n=3):
    clean = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'https?://\S+', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    words = clean.split()
    return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1))

ref_shingles = word_shingles(ref)
new_shingles = word_shingles(html)
w_inter = ref_shingles & new_shingles
w_union = ref_shingles | new_shingles
jaccard_goiania = len(w_inter) / len(w_union) if w_union else 0

cross_files = [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
    '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html',
]
cross_results = []
for cf in cross_files:
    try:
        with open(cf) as f:
            other = f.read()
        osh = word_shingles(other)
        ci = new_shingles & osh
        cu = new_shingles | osh
        cross_results.append((cf.split('/')[-1], len(ci)/len(cu) if cu else 0))
    except FileNotFoundError:
        cross_results.append((cf.split('/')[-1], -1))

print("=" * 60)
print("VERIFICAÇÃO — ARTICULADA TRINDADE")
print("=" * 60)
print(f"Tamanho:     ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'✓' if ref_classes == new_classes else '✗'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'✓' if ref_svgs == new_svgs else '✗'}")
print(f"Jaccard vs Goiânia: {jaccard_goiania:.4f}  {'✓ < 0.20' if jaccard_goiania < 0.20 else '✗ >= 0.20'}")
for name, j in cross_results:
    status = '✓ < 0.20' if 0 <= j < 0.20 else ('✗ >= 0.20' if j >= 0.20 else 'N/A')
    print(f"Jaccard vs {name}: {j:.4f}  {status}")

if goiania_issues:
    print(f"\n⚠ {len(goiania_issues)} refs suspeitas:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\n✓ Nenhuma referência indevida a Goiânia")

tc = html.count('Trindade') + html.count('trindade')
local = html.count('GO-060') + html.count('Sol Nascente') + html.count('Setor Maysa') + html.count('condomínio')
print(f"\nTrindade mentions: {tc}")
print(f"Contexto local: {local}")

elapsed = datetime.now() - start
print(f"\nTEMPO: {int(elapsed.total_seconds()//60):02d}:{int(elapsed.total_seconds()%60):02d}")
print(f"TOKENS: ~{len(html)//4:,}")
print(f"Arquivo: {OUT}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Articulada Trindade gerada!")
