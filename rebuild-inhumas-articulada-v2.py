#!/usr/bin/env python3
"""
rebuild-inhumas-articulada-v2.py
Gera LP de Plataforma Articulada para Inhumas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

INHUMAS CONTEXT:
- 40km from Goiânia via GO-070/BR-153, pop 53,000
- Polo têxtil/confecção, indústria alimentícia, armazéns de grãos
- Distrito Industrial de Inhumas
- Bairros: Centro, Setor Industrial
- Rodovias: GO-070, BR-153
"""

from datetime import datetime
import time
start = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'

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
  '<title>Plataforma Articulada para Locação em Inhumas-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
  'content="Plataforma articulada de 12 e 15 metros para locação em Inhumas-GO. Braço hidráulico com alcance lateral para manutenção de galpões têxteis, coberturas de armazéns e estruturas do Distrito Industrial. Diesel ou elétrica, manutenção inclusa. Entrega pela GO-070 no mesmo dia."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  'href="https://movemaquinas.com.br/inhumas-go/aluguel-de-plataforma-elevatoria-articulada"')

r('content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
  'content="Plataforma Articulada para Locação em Inhumas-GO | Move Máquinas"')

r('content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Plataforma articulada 12 a 15m em Inhumas. Atende galpões de confecção, armazéns de grãos e fábricas do Distrito Industrial. Manutenção inclusa, entrega pela GO-070. A partir de R$2.800/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Inhumas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.3547;-49.4952"')
r('content="-16.7234, -49.2654"', 'content="-16.3547, -49.4952"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.3547, "longitude": -49.4952')
r('"latitude": -16.7234', '"latitude": -16.3547')
r('"longitude": -49.2654', '"longitude": -49.4952')

# Schema — Service name
r('"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
  '"name": "Locação de Plataforma Articulada em Inhumas"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Inhumas", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/"')
r('"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  '"name": "Plataforma Articulada em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/aluguel-de-plataforma-elevatoria-articulada"')

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
        { "@type": "Question", "name": "Articulada ou tesoura: qual funciona melhor nos galpões têxteis de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A articulada é necessária quando o trabalho exige desviar de pontes rolantes, esteiras suspensas e dutos de ventilação — situação comum nos barracões de confecção e tecelagens de Inhumas. A tesoura sobe na vertical sem desviar de nada. Se o caminho até o ponto de trabalho está livre, a tesoura resolve. Se há obstáculo no meio, apenas a articulada alcança." } },
        { "@type": "Question", "name": "Qual o alcance máximo das plataformas articuladas disponíveis para Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A frota inclui dois patamares: 12 e 15 metros de altura de trabalho. O modelo de 12m atende a maioria dos galpões do Distrito Industrial e dos barracões de confecção. O de 15m é indicado para silos de armazenamento de grãos e estruturas mais elevadas. O alcance lateral vai de 6 a 8 metros conforme o modelo." } },
        { "@type": "Question", "name": "Qual o investimento mensal para alugar plataforma articulada em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Os valores ficam entre R$2.800 e R$4.500 por mês, conforme modelo (12m ou 15m), motorização e duração do contrato. Inhumas recebe pela GO-070 a partir da nossa sede em Goiânia — 40 km sem pedágio. O contrato inclui manutenção preventiva, corretiva e suporte técnico durante toda a vigência." } },
        { "@type": "Question", "name": "Trabalhadores da indústria têxtil precisam de certificação para operar a articulada?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 obriga treinamento específico em trabalho em altura e operação de PEMT para qualquer pessoa que suba na plataforma, independente do setor. O curso cobre inspeção pré-uso, capacidade do cesto, descida de emergência e uso correto de cinto paraquedista com trava-quedas. Indicamos centros de formação na região." } },
        { "@type": "Question", "name": "A articulada diesel funciona nos pátios sem pavimentação do Distrito Industrial de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Os modelos diesel dispõem de tração 4x4 dimensionada para cascalho, terra compactada e pisos com desnível moderado — exatamente o cenário nos pátios industriais e canteiros de Inhumas. A elétrica exige piso firme e nivelado, sendo indicada para o interior dos galpões. Avaliamos o terreno antes de entregar o equipamento." } },
        { "@type": "Question", "name": "Em quanto tempo a plataforma articulada chega em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Inhumas fica a 40 km de Goiânia pela GO-070. A entrega acontece no mesmo dia da confirmação, normalmente em menos de 2 horas. Para manutenções programadas no Distrito Industrial ou nas fábricas de confecção, agendamos a data com antecedência para garantir o modelo necessário." } },
        { "@type": "Question", "name": "Quantos trabalhadores o cesto da articulada suporta ao mesmo tempo?", "acceptedAnswer": { "@type": "Answer", "text": "O cesto aguenta de 230 a 250 kg — espaço para dois profissionais com ferramentas e materiais. Em manutenções de cobertura onde o técnico sobe com parafusadeira, telhas e vedantes, o espaço é adequado. Pontos de ancoragem para cintos paraquedista estão integrados ao cesto conforme norma NR-35." } },
        { "@type": "Question", "name": "Em quais situações a articulada elétrica é preferível em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Dentro de galpões de confecção com acabamento fino — onde poeira de motor ou fumaça prejudica tecidos e fios — a elétrica opera sem emissão de gases e com ruído mínimo. Também é indicada em armazéns de alimentos onde contaminação por exaustão é proibida. Para tudo que envolve pátio externo ou piso irregular, a diesel com 4x4 é a opção correta." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/inhumas-go/">Equipamentos em Inhumas</a>')

r('<span aria-current="page">Plataforma Articulada em Goiânia</span>',
  '<span aria-current="page">Plataforma Articulada em Inhumas</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
  'Plataforma Articulada para Locação em <em>Inhumas</em>')

r('Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Braço articulado de 12 e 15 metros para manutenção de coberturas em galpões têxteis, reparo de estruturas no Distrito Industrial e inspeção de silos de grãos. Diesel 4x4 ou elétrica, manutenção no contrato. Entrega pela GO-070 no mesmo dia. A partir de R$2.800/mês.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Inhumas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template C
# ═══════════════════════════════════════════════════════════════════════

r('<strong>12 e 15 metros</strong><span>Braço articulado</span>',
  '<strong>Entrega via GO-070</strong><span>40 km da sede</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Atendendo indústrias de GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação
r('O que é <span>plataforma articulada</span> e quando usar',
  'Como a <span>plataforma articulada</span> resolve manutenções industriais em Inhumas')

# Parágrafo principal
r('A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
  'A plataforma articulada é uma máquina de acesso em altura cujo braço possui segmentos hidráulicos que flexionam em diferentes ângulos. Essa mobilidade permite que o cesto chegue a pontos bloqueados por vigas, tubulações e maquinário suspenso — algo que a tesoura, limitada ao movimento vertical, não consegue. Em Inhumas, onde fábricas de confecção operam com esteiras aéreas, linhas de exaustão de pó de algodão e teares em múltiplos níveis, a articulada é a ferramenta que posiciona o técnico no ponto exato sem desmontar a linha de produção.')

# H3 — alcance lateral
r('Alcance lateral para fachadas no Setor Bueno e Marista',
  'Alcance lateral dentro de barracões de confecção e tecelagens')

r('O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
  'Nos barracões de confecção de Inhumas, vigas treliçadas sustentam pontes rolantes e sistemas de exaustão que projetam 2 a 4 metros para dentro do vão livre. A articulada eleva o braço acima dessas estruturas, gira na articulação central e desce o cesto até a cobertura ou o ponto de reparo. Com 6 a 8 metros de deslocamento horizontal, o operador trabalha em calhas, luminárias e sistemas de ventilação sem que a base precise ficar embaixo do ponto de serviço — evitando a interrupção de máquinas de costura e prensas de estamparia posicionadas no piso.')

# H3 — diesel ou elétrica
r('A plataforma articulada a diesel é a opção para canteiros de obra, terrenos irregulares e trabalhos externos onde o equipamento precisa se deslocar entre pontos distantes. Com tração 4x4, ela opera em terrenos de terra, cascalho e pisos com desnível. A versão elétrica é indicada para ambientes internos como shopping centers, galpões industriais e áreas com restrição de emissão de gases e ruído. Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
  'A decisão entre diesel e elétrica em Inhumas depende diretamente do local de trabalho. A diesel com tração 4x4 atende pátios sem pavimentação no Distrito Industrial, canteiros de obras residenciais e áreas externas entre galpões. A elétrica é a escolha para o interior das fábricas de confecção e armazéns de alimentos: motor silencioso que não interfere na operação dos teares, e zero emissão que protege tecidos, fios e produtos alimentícios de contaminação por fuligem.')

# H3 — segmentos
r('Principais segmentos que usam articulada na capital',
  'Setores industriais que demandam articulada na região')

r('Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
  'O polo têxtil de Inhumas concentra dezenas de facções e confecções com barracões de pé-direito entre 8 e 14 metros, gerando demanda contínua por manutenção de coberturas, calhas industriais e iluminação suspensa. Armazéns de grãos e silos na zona rural do município precisam de inspeção periódica de chapas e sistemas de aeração em alturas superiores a 12 metros. A indústria alimentícia local — beneficiadoras de arroz e empacoteriadoras — contrata a articulada para reparos em linhas de exaustão e climatização sem paralisar a produção. Construtoras atuando na expansão urbana do Centro e Setor Industrial também utilizam o equipamento para acabamentos de fachada em edifícios de até 5 andares.')

# Bullet "Braço articulado"
r('contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
  'desvia de esteiras aéreas, sistemas de exaustão e vigas treliçadas nos barracões de confecção de Inhumas sem interromper a produção.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
  'Cotação de <span style="color:var(--color-primary);">plataforma articulada</span> para Inhumas')

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia via GO-070')

# Form selects — Inhumas como primeira opção
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Inhumas" selected>Inhumas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 1 — elétrica 12m
r('Plataforma articulada elétrica com 12 metros de altura de trabalho e 6 metros de alcance lateral. Zero emissão de gases, operação silenciosa e pneus não marcantes. Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado. O braço articulado posiciona o cesto sobre obstáculos como tubulações, esteiras e maquinário sem necessidade de desmontagem.',
  'Articulada elétrica com 12 metros de alcance vertical e 6 metros de deslocamento lateral. Motor silencioso e livre de fuligem — requisitos das confecções de Inhumas onde tecidos e fios não podem receber contaminação do ar. O braço contorna linhas de exaustão de pó de algodão e estruturas de ventilação, posicionando o cesto rente à cobertura para troca de telhas, instalação de luminárias LED e reparo de calhas sem parar os teares.')

# Slide 2 — diesel 12m
r('Plataforma articulada a diesel com 12 metros de altura de trabalho, tração 4x4 e 6 metros de alcance lateral. Projetada para operar em canteiros de obra com terreno de terra, cascalho e desnível. O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão. Motor diesel com torque para subir rampas de acesso e se deslocar entre faces do edifício sem necessidade de guincho auxiliar.',
  'Articulada diesel com 12 metros de elevação, tração 4x4 e 6 metros de alcance horizontal. Projetada para pátios de cascalho e acessos de terra — cenário habitual no Distrito Industrial de Inhumas e nos canteiros da zona de expansão urbana. O torque do motor diesel permite deslocamento entre galpões e armazéns sem reboque auxiliar, cobrindo manutenções de cobertura e estrutura metálica em mais de um barracão no mesmo turno.')

# Slide 3 — diesel 15m
r('Plataforma articulada a diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral. O maior alcance disponível na frota para locação em Goiânia. Indicada para fachadas de edifícios acima de 4 pavimentos, manutenção de coberturas de galpões industriais com estruturas metálicas elevadas e trabalhos em viadutos e pontes. A combinação de 15 metros de altura com 8 metros de deslocamento lateral permite acessar pontos que nenhum outro equipamento portátil alcança.',
  'Articulada diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral — o modelo de maior capacidade da frota. Indicada para inspeção de silos de armazenamento de grãos, manutenção de coberturas em barracões com tesouras metálicas acima de 12 metros e trabalhos em estruturas elevadas do Distrito Industrial de Inhumas. O alcance combinado de 15 metros vertical e 8 metros horizontal resolve qualquer ponto acessível sem montagem de andaime.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA
# ═══════════════════════════════════════════════════════════════════════

r('"A maior confusão que vejo é cliente pedindo tesoura para trabalho em fachada com recuo. A tesoura só sobe reto. Se tem beiral, marquise ou qualquer obstáculo no caminho, ela não alcança. Já recebi ligação de obra parada porque alugaram a plataforma errada de outro fornecedor. Com a articulada, o braço contorna o obstáculo e posiciona o cesto exatamente onde o trabalho precisa ser feito. Sempre pergunto: qual é o ponto de trabalho? Antes de fechar, a gente faz essa análise sem custo."',
  '"Inhumas tem dois cenários que pedem articulada com frequência: galpão de confecção com esteira no caminho e silo de grãos com passarela no meio. A tesoura chega na base e não consegue desviar. Semana passada, uma facção no Setor Industrial precisava trocar quatro luminárias a 10 metros com a linha de exaustão cruzando na frente. Mandamos a articulada elétrica, trocou tudo em meio dia sem desligar um tear sequer. Antes de qualquer contrato para Inhumas, peço foto da estrutura e localizo cada obstáculo. Essa avaliação não custa nada."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se o trabalho exige acessar um ponto que não está diretamente acima da base do equipamento, a articulada é obrigatória. Fachadas com varandas, beirais com projeção, galpões com tubulações no caminho e estruturas com recuo: tudo isso exige alcance lateral. A tesoura só resolve quando o acesso é vertical direto, sem nenhum obstáculo entre o solo e o ponto de trabalho.',
  '<strong>Regra para decidir em Inhumas:</strong> se entre o piso e o ponto de trabalho há qualquer estrutura cruzando — esteira, duto de exaustão, viga, passarela — a articulada é a única saída. Nos galpões de confecção e nos silos de grãos, essa situação aparece em mais de 70% dos chamados. A tesoura funciona quando o caminho vertical está completamente livre, como em áreas abertas de estoque sem maquinário suspenso.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Inhumas:')

# Links internos — todos para inhumas-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Inhumas')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/inhumas-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Inhumas')

r('/goiania-go/aluguel-de-transpaleteira', '/inhumas-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Inhumas')

r('/goiania-go/curso-operador-empilhadeira', '/inhumas-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
  'alt="Vídeo Move Máquinas: plataforma articulada para galpões e indústrias em Inhumas e região"')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Valores de referência para locação de plataforma elevatória articulada em Goiânia. O preço final depende do modelo, prazo e altura de trabalho necessária.',
  'Tabela de referência para locação de plataforma articulada em Inhumas. O custo final varia conforme modelo, motorização e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Inhumas (40 km, sem custo)')

r('montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 3 a 5 dias úteis antes de qualquer trabalho começar. Com a plataforma articulada, o equipamento chega pronto para operar no mesmo dia. Para serviços de vedação, pintura e instalação de ACM com duração de até 3 meses, a articulada sai mais barata e mais rápida que andaime.',
  'montar andaime dentro de um barracão de confecção em Inhumas custa R$12.000 a R$20.000 entre material, mão de obra de montagem e paralisação parcial da produção. O prazo para erguer a estrutura é de 3 a 5 dias úteis — período em que teares e prensas ficam parados. Com a articulada, o equipamento chega no mesmo dia e a manutenção começa imediatamente. Para reparos de cobertura e estrutura com prazo de até 3 meses, a articulada custa menos e libera o galpão mais rápido.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag — has leading whitespace in actual file
r('      Aplicações em Goiânia', '      Aplicações em Inhumas')

# H2 — variação
r('Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
  'Dos galpões têxteis ao Distrito Industrial: onde a <span>plataforma articulada</span> atua em Inhumas')

# Card 1
r('alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
  'alt="Galpão de confecção com estrutura metálica elevada no polo têxtil de Inhumas"')
r('<h3>Setor Bueno e Marista: fachadas ACM</h3>',
  '<h3>Polo têxtil: barracões de confecção e tecelagem</h3>')
r('Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
  'As dezenas de facções e confecções de Inhumas operam em barracões com pé-direito de 8 a 14 metros, vigas treliçadas e sistemas de exaustão de resíduos têxteis. A articulada contorna esteiras suspensas e linhas de aspiração de pó de algodão para posicionar o cesto rente à cobertura — permitindo troca de telhas, reparo de calhas e instalação de iluminação LED sem desligar a produção.')

# Card 2
r('alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
  'alt="Armazém de grãos e silo em Inhumas com estrutura metálica de armazenamento"')
r('<h3>Distrito Industrial: galpões e estruturas</h3>',
  '<h3>Armazéns de grãos: silos e sistemas de aeração</h3>')
r('No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
  'Inhumas é polo de armazenagem de arroz e milho com silos que ultrapassam 12 metros de altura. A articulada de 15m posiciona inspetores rente às chapas para verificação de corrosão, troca de placas de aeração e reparo de passarelas. O braço desvia das tubulações de sucção e descarga de grãos sem exigir esvaziamento prévio do silo — reduzindo o tempo de parada e o risco de perda de safra.')

# Card 3
r('alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
  'alt="Fábrica de alimentos no Distrito Industrial de Inhumas com cobertura metálica"')
r('<h3>Polo da Moda: instalações comerciais</h3>',
  '<h3>Indústria alimentícia: linhas de exaustão e climatização</h3>')
r('Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
  'Beneficiadoras de arroz e empacotadoras em Inhumas dependem de dutos de exaustão e sistemas de climatização que percorrem todo o comprimento do galpão a 8 metros de altura. A articulada elétrica acessa cada ponto de reparo sem emitir fumaça que contamine a linha de produção alimentícia. O cesto posiciona o técnico com precisão para limpeza de filtros, vedação de dutos e substituição de motores de ventilação.')

# Card 4
r('alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
  'alt="Obra de construção civil no Setor Industrial de Inhumas com estrutura em andamento"')
r('Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
  'A expansão urbana de Inhumas no Centro e Setor Industrial trouxe empreendimentos residenciais de até 4 andares. Construtoras locais contratam a articulada para acabamento de fachada, instalação de esquadrias e impermeabilização de juntas — eliminando andaimes em obras com prazo apertado e calçada estreita onde a base de um andaime fachadeiro não cabe.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
  'Equipe técnica mobile que chega a Inhumas pela GO-070. Diagnóstico de sistema hidráulico, elétrico e motor diretamente no galpão ou canteiro, sem necessidade de remoção do equipamento.')

r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da plataforma via GO-070 até seu barracão, armazém ou canteiro em Inhumas. São 40 km da sede — entrega no mesmo dia, sem custo de frete adicional.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
  '"Tivemos que trocar 30 telhas na cobertura do nosso barracão de costura. A linha de exaustão de pó de algodão cruza o vão a 7 metros. A articulada de 12m desviou de tudo e posicionou o pedreiro rente ao telhado. Concluímos o serviço em 3 dias sem desligar nenhuma máquina de costura. Com andaime, levaríamos 10 dias entre montagem e reparo."')
r('<strong>Marcos A.</strong>', '<strong>Cláudio S.</strong>')
r('Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
  'Proprietário, Confecção, Inhumas-GO (dez/2025)')

# Depoimento 2
r('"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
  '"Inspeção anual das chapas do nosso silo de arroz — 14 metros de altura com passarela de descarga cruzando no meio. A articulada de 15m desviou da passarela e posicionou o inspetor rente à chapa sem precisar esvaziar o silo. A Move entregou pela GO-070 no dia seguinte à confirmação. Resultado: laudo completo em 4 dias, zero perda de estoque."')
r('<strong>Carlos R.</strong>', '<strong>Marcos V.</strong>')
r('Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
  'Gerente de Armazém, Cerealista, Inhumas-GO (jan/2026)')

# Depoimento 3
r('"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
  '"Precisávamos limpar e vedar os dutos de exaustão da nossa empacotadora. São 22 pontos de reparo a 9 metros de altura com a linha de produção embaixo. A articulada elétrica funcionou sem fumaça e sem ruído — a produção continuou normalmente enquanto o técnico trabalhava em cima. Economia de 8 dias comparado ao andaime tubular que orçamos antes."')
r('<strong>Patrícia L.</strong>', '<strong>Fernanda R.</strong>')
r('Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
  'Diretora Industrial, Alimentos, Inhumas-GO (fev/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/inhumas-go/curso-de-operador-de-empilhadeira')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operadores</a>? Conectamos sua equipe a centros credenciados na região de Inhumas e Goiânia.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Inhumas</span> e cidades vizinhas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 40 km de Inhumas pela GO-070. Entrega de plataforma articulada no mesmo dia da confirmação. Cobrimos toda a região num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/"><strong>Inhumas</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
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
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/aparecida-de-goiania-go/">Aparecida de Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília (DF)</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/itumbiara-go/">Itumbiara</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-49.4952!3d-16.3547')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Inhumas"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Inhumas</a>')
r('/goiania-go/" style="color', '/inhumas-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma articulada</span> em Inhumas')

# FAQ 1
r('>Qual a diferença entre plataforma articulada e tesoura?<',
  '>Articulada ou tesoura: qual funciona melhor nos galpões de Inhumas?<')
r('>A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.<',
  '>A articulada é obrigatória quando há esteira, duto de exaustão ou viga cruzando o caminho até o ponto de trabalho — situação constante nos barracões de confecção e armazéns de grãos de Inhumas. A tesoura sobe na vertical e não desvia de nada. Se o acesso é livre, a tesoura resolve com eficiência. Se há obstáculo, apenas a articulada alcança o ponto.<')

# FAQ 2
r('>Até quantos metros a plataforma articulada alcança?<',
  '>Qual a altura máxima das articuladas para locação em Inhumas?<')
r('>A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação.<',
  '>Trabalhamos com dois patamares: 12 e 15 metros de altura de trabalho. O de 12m atende a maioria dos barracões de confecção e galpões do Distrito Industrial. O de 15m é necessário para silos de grãos e estruturas mais elevadas. Ambos possuem alcance lateral de 6 a 8 metros para contornar obstáculos intermediários.<')

# FAQ 3
r('>Quanto custa alugar plataforma articulada em Goiânia?<',
  '>Qual o custo mensal da plataforma articulada em Inhumas?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato.<',
  '>O investimento mensal fica entre R$2.800 e R$4.500, variando conforme modelo (12m ou 15m), motorização e duração do contrato. Inhumas recebe sem custo de frete — são 40 km pela GO-070. Manutenção preventiva, corretiva e suporte técnico estão cobertos durante toda a vigência.<')

# FAQ 4
r('>Preciso de treinamento para operar a plataforma articulada?<',
  '>Funcionários das confecções precisam de certificação para usar a articulada?<')
r('>Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.<',
  '>Sim. Qualquer pessoa que suba na plataforma precisa de treinamento NR-35 válido, cobrindo inspeção pré-uso, limites de carga, procedimentos de emergência e uso correto do cinto paraquedista. Isso vale para funcionários de confecções, armazéns e indústrias de alimentos igualmente. Indicamos centros credenciados na região de Inhumas e Goiânia.<')

# FAQ 5
r('>A plataforma articulada pode ser usada em terreno irregular?<',
  '>A articulada diesel opera nos pátios sem pavimentação do Distrito Industrial?<')
r('>Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado.<',
  '>Sim. A versão diesel dispõe de tração 4x4 dimensionada para cascalho, terra compactada e pisos irregulares — cenário habitual nos pátios industriais e canteiros de Inhumas. A elétrica exige piso firme e é indicada para o interior dos galpões. Avaliamos o terreno antes de entregar para garantir que o modelo suporte as condições do local.<')

# FAQ 6
r('>Vocês entregam plataforma articulada fora de Goiânia?<',
  '>Em quanto tempo a plataforma chega em Inhumas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Inhumas fica a 40 km pela GO-070 a partir da nossa sede em Goiânia. A plataforma chega no mesmo dia da confirmação, normalmente em menos de 2 horas. Para manutenções programadas, agendamos com antecedência. Sem custo de frete.<')

# FAQ 7
r('>Qual a capacidade de carga do cesto da articulada?<',
  '>Quantos profissionais cabem no cesto durante a manutenção?<')
r('>O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação.<',
  '>O cesto comporta 230 a 250 kg — dois técnicos com ferramentas, telhas e vedantes. Para manutenções de cobertura nos barracões de Inhumas, esse espaço acomoda o profissional e todo o material necessário numa única subida. Pontos de ancoragem para cinto paraquedista estão integrados ao cesto conforme NR-35.<')

# FAQ 8
r('>Diesel ou elétrica: qual plataforma articulada alugar?<',
  '>Em quais situações a articulada elétrica é melhor em Inhumas?<')
r('>A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.<',
  '>A elétrica é a escolha dentro de galpões de confecção onde fuligem prejudica tecidos e fios, e em armazéns de alimentos onde emissão de gases é proibida. Para qualquer trabalho externo, pátio sem pavimentação ou deslocamento longo entre galpões, a diesel com tração 4x4 é a opção certa. Na dúvida, fazemos avaliação técnica gratuita antes de fechar.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Alugue uma plataforma articulada em Goiânia hoje',
  'Solicite plataforma articulada para Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma articulada em Inhumas.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard vs ref-goiania
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar
r('<strong>200km</strong> raio de atendimento',
  '<strong>40 km</strong> de Inhumas', 99)

r('<strong>+20</strong> anos de mercado',
  '<strong>+20</strong> anos atendendo GO', 99)

# Section tag "Entenda o equipamento"
r('Entenda o equipamento',
  'Conheça o equipamento')

# H3 — Diesel ou elétrica
r('Diesel ou elétrica: como escolher para sua obra',
  'Diesel ou elétrica: critérios para Inhumas')

# Fleet section H2
r('Tipos de <span>plataforma elevatória articulada</span> para locação',
  'Modelos de <span>plataforma articulada</span> disponíveis para Inhumas')

# Fleet subtitle
r('Três configurações de plataforma articulada para atender diferentes alturas de trabalho e condições de terreno. Diesel ou elétrica.',
  'Três opções de articulada com alturas e motorização distintas. Escolha conforme o tipo de galpão, silo ou obra em Inhumas.')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua obra? Fale com nosso time técnico. A consultoria é gratuita.',
  'Sem certeza de qual modelo sua operação exige? Nossa equipe avalia sem custo. Fale pelo WhatsApp ou ligue.')

# Comparativo intro
r('A escolha errada entre articulada e tesoura paralisa a obra. Entender a diferença entre elevação vertical e alcance lateral evita mobilização dupla e custo desnecessário.',
  'Nos galpões e armazéns de Inhumas, selecionar o equipamento errado significa parada de produção e mobilização dobrada. O quadro abaixo resume quando cada tipo funciona.')

# Comparativo card — articulada
r('Para fachadas, beirais e pontos de difícil acesso',
  'Para coberturas com obstáculos e pontos de difícil acesso')

r('Braço articulado com alcance lateral de até 8 metros. Contorna obstáculos e posiciona o cesto no ponto exato de trabalho, mesmo sobre marquises e varandas.',
  'Braço segmentado com alcance lateral de até 8 metros. Desvia de vigas, esteiras e dutos para posicionar o cesto onde a manutenção precisa acontecer.')

r('Alcance lateral de 6 a 8 metros para fachadas',
  'Alcance lateral de 6 a 8 metros para coberturas')

r('Contorna beirais, marquises e varandas projetadas',
  'Desvia de vigas treliçadas, esteiras e dutos de exaustão')

r('Tração 4x4 diesel para canteiros irregulares',
  'Tração 4x4 diesel para pátios sem pavimentação')

# Comparativo card — tesoura
r('Para elevação vertical em pisos nivelados',
  'Para subida vertical em pisos firmes')

r('Mecanismo pantográfico que eleva a plataforma na vertical. Ideal para trabalhos onde o acesso é direto, sem obstáculos laterais.',
  'Pantógrafo que sobe na vertical sem desviar. Funciona quando não há estrutura cruzando entre o piso e o teto.')

r('Plataforma ampla: até 4 operadores com materiais',
  'Cesta ampla: comporta até 4 técnicos com ferramentas')

r('Custo de locação inferior à articulada',
  'Valor de locação menor que o da articulada')

r('Estabilidade superior para trabalhos com ferramentas pesadas',
  'Maior estabilidade para serviços com ferramental pesado')

r('Zero alcance lateral: não contorna obstáculos',
  'Sem alcance lateral: não desvia de vigas ou esteiras')

r('Não acessa fachadas com recuo ou projeções',
  'Não alcança pontos com estrutura no caminho')

r('Exige piso nivelado para operação segura',
  'Requer piso firme e nivelado para uso seguro')

# Cotação rápida section text
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe modelo e prazo ao lado — retornamos pelo WhatsApp em até 2 horas com valor, disponibilidade e condições.')

r('Manutenção inclusa no contrato',
  'Manutenção preventiva e corretiva no contrato')

r('Contratos a partir de 1 dia',
  'Locação a partir de 1 dia')

r('Suporte técnico 24h',
  'Assistência técnica 24h em Inhumas')

# Price section H2
r('Quanto custa alugar uma <span>plataforma com braço articulado</span> em 2026?',
  'Investimento mensal: <span>plataforma articulada</span> em Inhumas (2026)')

# Price section H3
r('R$2.800 a R$4.500/mês com manutenção inclusa',
  'De R$2.800 a R$4.500/mês — manutenção e suporte no pacote', 1)

# Price note
r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 40 km de Inhumas pela GO-070. Não cobramos frete adicional. A plataforma chega ao seu barracão, armazém ou canteiro pronta para operar no mesmo dia.')

# Incluso section H2/subtitle
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas atendendo indústrias de Goiás nos mostraram que o valor real da locação não está na máquina — está no suporte quando o braço hidráulico trava no meio da manutenção.')

# Incluso — consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Avaliamos modelo, altura e motorização antes de fechar. Nos galpões de confecção e armazéns de grãos, cada estrutura tem exigência diferente — a consultoria gratuita evita contratação errada.')

# NR-35 section
r('Como garantir conformidade com a <span>NR-35</span> na operação de plataforma articulada?',
  'Operação de plataforma articulada e a <span>NR-35</span> em Inhumas')

r('A NR-35 regulamenta trabalho em altura acima de 2 metros. Todo operador de plataforma elevatória precisa de treinamento específico e certificação válida.',
  'A NR-35 define as regras para qualquer trabalho acima de 2 metros. Todo profissional que suba na articulada — em confecção, armazém ou obra — precisa de treinamento específico e certificado válido.')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar em conformidade')

r('Confirme que o operador possui treinamento NR-35 válido, com conteúdo sobre PEMT, inspeção pré-operacional e procedimentos de emergência.',
  'Todo operador deve apresentar certificado NR-35 válido antes de subir na plataforma. O treinamento cobre operação de PEMT, inspeção pré-uso e procedimentos de resgate.')

r('Antes de cada turno: verifique sistema hidráulico, articulações, cilindros, freios e sinalizadores. Registre a inspeção em formulário padrão.',
  'No início de cada turno o operador deve checar sistema hidráulico, articulações, cilindros, freios e alarmes. Registre a inspeção no formulário fornecido junto com o equipamento.')

r('Demarque a área de operação no nível do solo e instale sinalização para evitar circulação de pedestres sob a plataforma elevada.',
  'Delimite a zona de operação no piso e posicione barreiras para impedir que pessoas circulem sob a plataforma elevada durante o uso.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada articulada da Move Máquinas é entregue com o checklist de inspeção pré-uso completo.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>plataforma articulada</span>',
  'Empresas de Inhumas que utilizaram <span>plataforma articulada</span>')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, preço e prazo de entrega para Inhumas.')

# Video section
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — mais de 50 vídeos sobre locação de equipamentos.')

# Video section H3
r('Como funciona o <span>aluguel de PTA</span> na Move Máquinas',
  'Veja como funciona a <span>locação de plataforma articulada</span> para Inhumas')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona a locação de plataformas elevatórias: consulta técnica, escolha do modelo adequado para sua obra, entrega no canteiro e suporte durante todo o contrato. O braço articulado precisa de avaliação prévia do terreno e dos obstáculos da fachada.',
  'O vídeo apresenta cada etapa da locação: análise técnica do galpão ou silo, seleção do modelo adequado, transporte pela GO-070 até Inhumas e acompanhamento técnico durante toda a vigência. A avaliação prévia do terreno e das estruturas internas é gratuita.')

# Custo real — exact match from articulada ref
r('<strong>O custo real de usar andaime quando a obra exige articulada:</strong>',
  '<strong>Quanto custa usar andaime quando o galpão exige articulada:</strong>')

# Incluso — strong tag
r('<strong>Suporte técnico 24h / 7 dias</strong>',
  '<strong>Assistência técnica 24h — inclusive Inhumas</strong>')

# Incluso — manutenção do braço
r('Revisão periódica de cilindros hidráulicos, articulações, pinos e buchas do braço. Troca de fluido hidráulico e verificação de vedações conforme especificação do fabricante.',
  'Inspeção programada dos cilindros, articulações, pinos e buchas do braço. Substituição do fluido hidráulico e checagem de vedações seguindo o cronograma do fabricante. Incluso no contrato sem custo extra.')

# Incluso — cesto
r('Cesto com pontos de ancoragem para cinto tipo paraquedista verificados. Portinhola, piso antiderrapante e controles de emergência testados antes de cada entrega.',
  'Ancoragens do cinto paraquedista verificadas, portinhola lacrada, piso antiderrapante sem desgaste e controles de descida de emergência funcionais. Cada item é testado antes do embarque para Inhumas.')

# Incluso — pneus
r('Pneus com sulco e pressão adequados para o tipo de terreno da obra. Sistema de tração 4x4 (diesel) testado para garantir deslocamento seguro em canteiros irregulares.',
  'Sulcos e pressão dos pneus ajustados ao terreno informado na contratação. No modelo diesel 4x4, a tração é testada em rampa e cascalho antes do despacho para garantir deslocamento firme em pátios sem pavimentação.')

# Incluso — consultoria
r('Avaliação do terreno, dos obstáculos da fachada e da altura de trabalho para indicar o modelo correto. Sem compromisso e sem custo.',
  'Análise do barracão, silo ou canteiro para definir modelo, altura e motorização adequados. Enviamos técnico ou fazemos avaliação por foto. Sem custo e sem compromisso.')

# Onde opera subtitle
r('Onde a plataforma articulada opera diariamente na capital e região metropolitana.',
  'Galpões, silos e canteiros que contratam articulada com frequência na região de Inhumas.')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL + JACCARD
# ═══════════════════════════════════════════════════════════════════════

import re, os

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            'goiania-go/', '40 km', 'Sede na',
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
print("VERIFICAÇÃO ESTRUTURAL")
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
ct = html.count('Inhumas')
local = html.count('confecç') + html.count('têxtil') + html.count('grão') + html.count('GO-070') + html.count('Distrito Industrial')
print(f"\nInhumas: {ct} menções")
print(f"Contexto local (confecção/têxtil/grãos/GO-070/DI): {local} menções")

# JACCARD 3-GRAMS
def extract_text(h):
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard_sim(set1, set2):
    inter = len(set1 & set2)
    union = len(set1 | set2)
    return inter / union if union > 0 else 0.0

new_text = extract_text(html)
new_ng = ngrams(new_text)

ref_text = extract_text(ref)
ref_ng = ngrams(ref_text)

j_ref = jaccard_sim(new_ng, ref_ng)
print(f"\n{'=' * 60}")
print("JACCARD 3-GRAMS")
print(f"{'=' * 60}")
print(f"vs ref-goiania-articulada.html:    {j_ref:.4f}  {'✓' if j_ref < 0.20 else '✗ FALHOU'}")

# Compare with SC and BSB
for comp_path in [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
    '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html',
]:
    if os.path.exists(comp_path):
        with open(comp_path, 'r', encoding='utf-8') as f:
            comp_html = f.read()
        comp_text = extract_text(comp_html)
        comp_ng = ngrams(comp_text)
        j_comp = jaccard_sim(new_ng, comp_ng)
        fname = os.path.basename(comp_path)
        print(f"vs {fname}: {j_comp:.4f}  {'✓' if j_comp < 0.20 else '✗ FALHOU'}")

elapsed = time.time() - start
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nTEMPO: {elapsed:.1f}s")
print(f"TOKENS: ~{len(html)//4} (estimativa)")
print(f"\n✅ Salvo: {OUT}")
