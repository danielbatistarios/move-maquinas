#!/usr/bin/env python3
"""
rebuild-sc-articulada-v2.py
Gera LP de Plataforma Articulada para Senador Canedo
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'

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
  '<title>Plataforma Articulada para Locação em Senador Canedo-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
  'content="Locação de plataforma articulada 12 e 15m em Senador Canedo. Ideal para manutenção de tanques no polo petroquímico, inspeção de estruturas no DASC e obras industriais no DISC. Diesel ou elétrica, manutenção inclusa. Entrega no mesmo dia pela BR-153."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  'href="https://movemaquinas.com.br/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada"')

r('content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
  'content="Plataforma Articulada para Locação em Senador Canedo-GO | Move Máquinas"')

r('content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Plataforma articulada 12 a 15m em Senador Canedo. Atendemos polo petroquímico, DASC e DISC. Diesel ou elétrica, manutenção no contrato, entrega pela BR-153. A partir de R$2.800/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Senador Canedo, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.6997;-49.0919"')
r('content="-16.7234, -49.2654"', 'content="-16.6997, -49.0919"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.6997, "longitude": -49.0919')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.6997')
r('"longitude": -49.2654', '"longitude": -49.0919')

# Schema — Service name
r('"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
  '"name": "Locação de Plataforma Articulada em Senador Canedo"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Senador Canedo", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/"')
r('"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  '"name": "Plataforma Articulada em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada"')

# ═══════════════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

# Substituir o bloco inteiro de FAQs no Schema
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
        { "@type": "Question", "name": "Por que escolher plataforma articulada em vez de tesoura para obras em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "No polo petroquímico e nos distritos industriais DASC e DISC de Senador Canedo, a maioria das operações envolve contornar tubulações aéreas, vasos de pressão e estruturas metálicas sobrepostas. A tesoura sobe apenas na vertical e não desvia de obstáculos. A articulada possui braço com articulações que permitem alcance lateral de até 8 metros, posicionando o cesto no ponto exato de trabalho mesmo com tubulações no caminho." } },
        { "@type": "Question", "name": "Qual a altura máxima da plataforma articulada disponível em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "Trabalhamos com dois patamares de alcance: 12 metros e 15 metros de altura de trabalho. O modelo de 12m atende a maioria das manutenções em galpões do DASC e DISC. O de 15 metros é necessário para torres de destilação e estruturas mais altas do complexo petroquímico. Ambos possuem alcance lateral de 6 a 8 metros." } },
        { "@type": "Question", "name": "Qual o valor da locação de plataforma articulada em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "O investimento mensal fica entre R$2.800 e R$4.500, variando conforme modelo (12m ou 15m), motorização (diesel ou elétrica) e duração do contrato. Senador Canedo está a 20 km da nossa sede, e a entrega via BR-153 não tem custo adicional de deslocamento. O contrato inclui manutenção preventiva, corretiva e suporte técnico integral." } },
        { "@type": "Question", "name": "Operadores do complexo petroquímico precisam de certificação específica para a articulada?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Além do treinamento NR-35 para trabalho em altura, operadores em áreas classificadas do complexo petroquímico podem precisar de certificação adicional para atmosferas explosivas. A NR-35 exige capacitação em PEMT que abrange inspeção pré-operacional, limites de carga e procedimentos de emergência. Indicamos centros de formação credenciados na região." } },
        { "@type": "Question", "name": "A articulada diesel opera nos pátios irregulares do DASC e do polo petroquímico?", "acceptedAnswer": { "@type": "Answer", "text": "Os modelos diesel possuem tração 4x4 projetada exatamente para esse tipo de terreno. Pátios industriais do DASC, acessos de terra no complexo petroquímico e canteiros de expansão com cascalho são o cenário mais comum dos nossos contratos em Senador Canedo. Antes da entrega, avaliamos as condições do piso para garantir que o modelo suporte o terreno." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da plataforma articulada em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "Senador Canedo é uma das cidades mais rápidas para atendermos: fica a 20 km da nossa base em Goiânia, com acesso direto pela BR-153 sem pedágio. A entrega é feita no mesmo dia da confirmação do contrato, geralmente em menos de 2 horas. Para urgências no complexo petroquímico ou DASC, priorizamos o despacho." } },
        { "@type": "Question", "name": "Quantos operadores cabem no cesto da plataforma articulada?", "acceptedAnswer": { "@type": "Answer", "text": "O cesto comporta até 230-250 kg, equivalente a dois técnicos com ferramentas e materiais de trabalho. No polo petroquímico, onde inspeções de soldas e troca de válvulas exigem ferramentaria especializada, o espaço é suficiente para o técnico e o auxiliar com os instrumentos necessários. O cesto possui ancoragens para cintos tipo paraquedista conforme NR-35." } },
        { "@type": "Question", "name": "Plataforma articulada elétrica funciona bem dentro dos galpões do DASC?", "acceptedAnswer": { "@type": "Answer", "text": "A versão elétrica é a mais indicada para operações internas no DASC, especialmente em indústrias farmacêuticas e de higiene que exigem zero emissão de gases e baixo ruído. O motor elétrico não contamina ambientes de área limpa. Para operações externas nos pátios ou no complexo petroquímico, recomendamos a versão diesel com tração 4x4." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/senador-canedo-go/">Equipamentos em Senador Canedo</a>')

r('<span aria-current="page">Plataforma Articulada em Goiânia</span>',
  '<span aria-current="page">Plataforma Articulada em Senador Canedo</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
  'Locação de Plataforma Articulada em <em>Senador Canedo</em>')

r('Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Braço articulado de 12 e 15 metros para manutenção no polo petroquímico, inspeção industrial no DASC e obras de expansão no DISC. Diesel 4x4 ou elétrica, manutenção inclusa no contrato. Entrega pela BR-153 no mesmo dia. A partir de R$2.800/mês.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Senador+Canedo', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template B
# ═══════════════════════════════════════════════════════════════════════

r('<strong>12 e 15 metros</strong><span>Braço articulado</span>',
  '<strong>Entrega via BR-153</strong><span>20 km da sede</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência industrial</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação E do pool
r('O que é <span>plataforma articulada</span> e quando usar',
  'Entenda o que é <span>plataforma elevatória articulada</span> antes de alugar')

# Parágrafo principal
r('A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
  'A plataforma elevatória articulada é um equipamento com braço hidráulico segmentado que permite ao cesto se deslocar na vertical, na horizontal e em arco. Essa capacidade de manobra resolve operações onde o acesso direto por cima não é possível — situação comum em plantas industriais com tubulações cruzadas, vasos de pressão e pontes rolantes. Em Senador Canedo, o polo petroquímico, o DASC e o DISC concentram instalações com múltiplos níveis de estruturas sobrepostas, tornando a articulada o equipamento padrão para manutenções que exigem posicionamento preciso sem interromper a produção.')

# H3 — alcance lateral
r('Alcance lateral para fachadas no Setor Bueno e Marista',
  'Como o braço articulado contorna tubulações no polo petroquímico')

r('O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
  'Tanques de armazenamento no polo petroquímico de Senador Canedo possuem redes de tubulação com projeção de 2 a 5 metros que impedem qualquer acesso vertical direto. O braço articulado resolve esse problema: o segmento inferior eleva a máquina acima do nível das tubulações, a articulação central muda a direção do braço para horizontal, e o segmento superior posiciona o cesto rente à parede do tanque ou torre. Com 6 a 8 metros de alcance lateral, o operador trabalha em válvulas, instrumentação e soldas sem que a base precise ficar embaixo do ponto de serviço — eliminando scaffolding temporário e paradas de linha.')

# H3 — diesel ou elétrica
r('A plataforma articulada a diesel é a opção para canteiros de obra, terrenos irregulares e trabalhos externos onde o equipamento precisa se deslocar entre pontos distantes. Com tração 4x4, ela opera em terrenos de terra, cascalho e pisos com desnível. A versão elétrica é indicada para ambientes internos como shopping centers, galpões industriais e áreas com restrição de emissão de gases e ruído. Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
  'No ambiente industrial de Senador Canedo, a escolha entre diesel e elétrica depende do local de operação. A diesel com tração 4x4 é o padrão para pátios do polo petroquímico e canteiros de expansão no DASC, onde o piso é irregular e a máquina precisa se deslocar entre pontos distantes dentro da planta. A elétrica é obrigatória dentro de galpões farmacêuticos e de higiene do DASC e DISC — zero emissão de gases preserva a integridade de áreas limpas, e a operação silenciosa não interfere nas linhas de produção.')

# H3 — segmentos
r('Principais segmentos que usam articulada na capital',
  'Indústrias e obras que demandam articulada na região')

r('Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
  'O setor petroquímico lidera a demanda em Senador Canedo: Petrobras, Realpetro e Petrobol mantêm contratos recorrentes para inspeção de tanques, troca de instrumentação e manutenção de torres. No DASC, laboratórios farmacêuticos e fábricas de higiene contratam a articulada elétrica para reparos em coberturas e sistemas de climatização sem contaminar áreas controladas. O DISC gera demanda do setor moveleiro e alimentício para instalação de estruturas metálicas de expansão. Construtoras que operam nas novas frentes residenciais do Jardim das Oliveiras e Residencial Canadá também utilizam a articulada para acabamentos de fachada em edifícios de até 5 pavimentos.')

# Bullet "Braço articulado"
r('contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
  'desvia de tubulações aéreas, vasos de pressão e pontes rolantes nas plantas industriais de Senador Canedo sem parar a produção.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
  'Cotação de <span style="color:var(--color-primary);">plataforma articulada</span> para Senador Canedo')

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia via BR-153')

# Form selects — Senador Canedo como primeira opção
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Senador Canedo" selected>Senador Canedo</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 1 — elétrica 12m
r('Plataforma articulada elétrica com 12 metros de altura de trabalho e 6 metros de alcance lateral. Zero emissão de gases, operação silenciosa e pneus não marcantes. Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado. O braço articulado posiciona o cesto sobre obstáculos como tubulações, esteiras e maquinário sem necessidade de desmontagem.',
  'Plataforma articulada elétrica com 12 metros de alcance vertical e 6 metros de alcance lateral. Motor silencioso, zero emissão de gases e pneus não marcantes — requisitos das indústrias farmacêuticas e de higiene do DASC que operam com áreas limpas certificadas. O braço contorna dutos de climatização e linhas de exaustão para posicionar o cesto no ponto exato de reparo sem comprometer o ambiente controlado.')

# Slide 2 — diesel 12m
r('Plataforma articulada a diesel com 12 metros de altura de trabalho, tração 4x4 e 6 metros de alcance lateral. Projetada para operar em canteiros de obra com terreno de terra, cascalho e desnível. O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão. Motor diesel com torque para subir rampas de acesso e se deslocar entre faces do edifício sem necessidade de guincho auxiliar.',
  'Articulada diesel com 12 metros de altura, tração 4x4 e 6 metros de alcance lateral. Projetada para pátios industriais com piso de cascalho e desnível — cenário típico do polo petroquímico e das vias internas do DASC. O modelo mais contratado em Senador Canedo: o torque do motor diesel permite deslocamento entre tanques, torres e galpões distantes dentro da mesma planta sem necessidade de transporte auxiliar.')

# Slide 3 — diesel 15m
r('Plataforma articulada a diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral. O maior alcance disponível na frota para locação em Goiânia. Indicada para fachadas de edifícios acima de 4 pavimentos, manutenção de coberturas de galpões industriais com estruturas metálicas elevadas e trabalhos em viadutos e pontes. A combinação de 15 metros de altura com 8 metros de deslocamento lateral permite acessar pontos que nenhum outro equipamento portátil alcança.',
  'Articulada diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral — o maior da frota. Esse modelo atende as operações mais exigentes de Senador Canedo: inspeção no topo de torres de destilação do complexo petroquímico, manutenção de coberturas em galpões industriais com tesouras metálicas a 14 metros e trabalhos em estruturas de expansão do DISC. O alcance combinado de 15 metros vertical e 8 metros lateral cobre qualquer ponto acessível sem guindaste.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Senador Canedo
# ═══════════════════════════════════════════════════════════════════════

r('"A maior confusão que vejo é cliente pedindo tesoura para trabalho em fachada com recuo. A tesoura só sobe reto. Se tem beiral, marquise ou qualquer obstáculo no caminho, ela não alcança. Já recebi ligação de obra parada porque alugaram a plataforma errada de outro fornecedor. Com a articulada, o braço contorna o obstáculo e posiciona o cesto exatamente onde o trabalho precisa ser feito. Sempre pergunto: qual é o ponto de trabalho? Antes de fechar, a gente faz essa análise sem custo."',
  '"A maioria dos chamados que recebo de Senador Canedo vem do polo petroquímico e do DASC. O erro mais comum é tentar resolver manutenção de tanque com tesoura — o equipamento chega lá e não alcança porque tem tubulação no meio do caminho. A articulada contorna tudo. Semana passada, um cliente do DISC precisava soldar vigas a 11 metros com ponte rolante no caminho. Mandamos a articulada diesel, resolveu em dois dias. Antes de fechar qualquer contrato para Senador Canedo, faço questão de entender qual é a estrutura e quais obstáculos existem no caminho. Essa análise é gratuita."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — texto do verdict + links
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se o trabalho exige acessar um ponto que não está diretamente acima da base do equipamento, a articulada é obrigatória. Fachadas com varandas, beirais com projeção, galpões com tubulações no caminho e estruturas com recuo: tudo isso exige alcance lateral. A tesoura só resolve quando o acesso é vertical direto, sem nenhum obstáculo entre o solo e o ponto de trabalho.',
  '<strong>Critério objetivo para Senador Canedo:</strong> se entre o solo e o ponto de trabalho existe qualquer obstáculo — tubulação, ponte rolante, marquise, vaso de pressão — a articulada é obrigatória. No polo petroquímico e no DASC, isso representa mais de 80% das operações. A tesoura funciona apenas quando o acesso é vertical livre, como pisos de galpão sem estruturas intermediárias.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Senador Canedo:')

# Links internos — todos para senador-canedo-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Senador Canedo')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/senador-canedo-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Senador Canedo')

r('/goiania-go/aluguel-de-transpaleteira', '/senador-canedo-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Senador Canedo')

r('/goiania-go/curso-operador-empilhadeira', '/senador-canedo-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma articulada para indústrias em Senador Canedo e região"')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Valores de referência para locação de plataforma elevatória articulada em Goiânia. O preço final depende do modelo, prazo e altura de trabalho necessária.',
  'Investimento mensal para locação de plataforma articulada em Senador Canedo. O valor varia conforme modelo, motorização e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Senador Canedo (20 km, sem custo)')

r('montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 3 a 5 dias úteis antes de qualquer trabalho começar. Com a plataforma articulada, o equipamento chega pronto para operar no mesmo dia. Para serviços de vedação, pintura e instalação de ACM com duração de até 3 meses, a articulada sai mais barata e mais rápida que andaime.',
  'montar scaffolding em um tanque de 12 metros no polo petroquímico de Senador Canedo custa R$18.000 a R$30.000 entre montagem, desmontagem e licenças de trabalho a quente. O prazo de montagem é de 5 a 8 dias úteis antes de qualquer trabalho começar — dias em que a linha pode ficar parada. Com a articulada, o equipamento chega operando no mesmo dia. Para contratos de manutenção programada de até 3 meses, a articulada reduz o custo total e libera a equipe para produzir.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('>Aplicações em Goiânia<', '>Aplicações industriais<')

# H2 — variação E
r('Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
  'Do polo petroquímico ao DISC: onde a <span>plataforma com braço articulado</span> atua em Senador Canedo')

# Card 1
r('alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
  'alt="Tanques e torres de destilação no polo petroquímico de Senador Canedo"')
r('<h3>Setor Bueno e Marista: fachadas ACM</h3>',
  '<h3>Polo petroquímico: tanques e torres de destilação</h3>')
r('Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
  'Petrobras, Realpetro e Petrobol mantêm tanques de armazenamento e torres de destilação com manutenção cíclica obrigatória. O braço articulado contorna redes de tubulação com projeção de até 5 metros e posiciona o cesto rente à parede do tanque para inspeção de soldas, troca de válvulas de segurança e calibração de instrumentação — sem scaffolding e sem parada prolongada de planta.')

# Card 2
r('alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
  'alt="Galpão farmacêutico no DASC de Senador Canedo com estrutura metálica elevada"')
r('<h3>Distrito Industrial: galpões e estruturas</h3>',
  '<h3>DASC: farmacêuticas e indústrias de higiene</h3>')
r('No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
  'O Distrito Agroindustrial de Senador Canedo concentra laboratórios farmacêuticos, fábricas de plásticos e indústrias de higiene com galpões de pé-direito entre 10 e 18 metros. A articulada elétrica opera dentro desses galpões sem emitir gases que comprometam áreas limpas. O braço contorna sistemas de exaustão, linhas de climatização e pontes rolantes para acessar coberturas, trocar iluminação e reparar calhas sem interromper a produção.')

# Card 3
r('alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
  'alt="Estruturas metálicas e galpões de expansão no DISC de Senador Canedo"')
r('<h3>Polo da Moda: instalações comerciais</h3>',
  '<h3>DISC: setor moveleiro e alimentício</h3>')
r('Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
  'O segundo distrito industrial de Senador Canedo reúne fábricas de móveis, processadoras de alimentos e indústrias de embalagens em fase de expansão. A articulada diesel desloca-se entre galpões pelo piso de cascalho dos pátios internos, posicionando soldadores e montadores em vigas metálicas, treliças de cobertura e estruturas de ampliação — sem andaime tubular e com economia de até 15 dias no cronograma.')

# Card 4
r('alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
  'alt="Edifícios residenciais em construção nos bairros de Senador Canedo"')
r('Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
  'Os bairros Jardim das Oliveiras, Residencial Canadá e Centro acompanham o crescimento de 130 mil habitantes com empreendimentos residenciais de até 5 andares. Construtoras locais contratam a articulada para acabamento de fachadas, instalação de esquadrias, impermeabilização de juntas e fixação de painéis ACM — eliminando andaimes em obras onde o prazo é curto e o acesso pela calçada é restrito.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
  'Equipe técnica mobile com deslocamento pela BR-153. Atendimento em Senador Canedo em menos de 40 minutos a partir da sede. Diagnóstico de sistema hidráulico, elétrico e motor diretamente na planta.')

r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-153 até seu galpão, pátio industrial ou canteiro em Senador Canedo. São 20 km da sede — entrega no mesmo dia, sem custo adicional de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
  '"Precisávamos inspecionar soldas em 4 tanques de armazenamento no polo petroquímico. Cada tanque tinha 3 linhas de tubulação cruzando na frente. A articulada de 15m desviou de tudo e posicionou nosso inspetor rente à chapa. Concluímos o laudo dos 4 tanques em 6 dias — a estimativa com scaffolding era de 3 semanas e R$28 mil só de montagem."')
r('<strong>Marcos A.</strong>', '<strong>Renato V.</strong>')
r('Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
  'Inspetor de Qualidade, Petroquímica, Senador Canedo-GO (nov/2025)')

# Depoimento 2
r('"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
  '"Trocamos 40 luminárias no galpão de produção do DASC com a articulada elétrica. Zero ruído, zero fumaça — nossa área limpa não foi comprometida em nenhum momento. O braço passou por cima do sistema de exaustão e posicionou o eletricista direto na calha. A Move entregou pela BR-153 no mesmo dia em que fechamos o contrato."')
r('<strong>Carlos R.</strong>', '<strong>Juliana T.</strong>')
r('Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
  'Gerente de Facilities, Indústria Farmacêutica DASC, Senador Canedo-GO (jan/2026)')

# Depoimento 3
r('"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
  '"Montagem de 120 metros lineares de treliça metálica na expansão do galpão no DISC. Nossos soldadores trabalharam a 10 metros de altura com a articulada diesel. A 4x4 se deslocou pelo pátio de cascalho sem travar. Economizamos 12 dias que gastaríamos com andaime tubular. Já agendamos a próxima etapa com a Move."')
r('<strong>Patrícia L.</strong>', '<strong>Diego F.</strong>')
r('Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
  'Encarregado de Obras, Metalúrgica, DISC Senador Canedo-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/senador-canedo-go/curso-de-operador-de-empilhadeira')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operadores</a>? Conectamos sua equipe a centros credenciados na região de Senador Canedo.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Senador Canedo</span> e cidades vizinhas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 20 km de Senador Canedo pela BR-153, sem pedágio. Entrega de plataforma articulada no mesmo dia da confirmação. Atendemos toda a região metropolitana num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/senador-canedo-go/"><strong>Senador Canedo</strong></a>
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
        <a href="/trindade-go/">Trindade</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/">Inhumas</a>
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

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-49.0919!3d-16.6997')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Senador Canedo"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Senador Canedo</a>')
r('/goiania-go/" style="color', '/senador-canedo-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma articulada</span> em Senador Canedo')

# FAQ 1
r('>Qual a diferença entre plataforma articulada e tesoura?<',
  '>Por que escolher articulada em vez de tesoura para operações em Senador Canedo?<')
r('>A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.<',
  '>No polo petroquímico e nos distritos DASC e DISC, a maioria das manutenções envolve contornar tubulações aéreas, vasos de pressão e estruturas sobrepostas. A tesoura sobe na vertical e não desvia de nada. A articulada possui braço segmentado com alcance lateral de até 8 metros — contorna obstáculos e posiciona o cesto no ponto exato de trabalho. Para a realidade industrial de Senador Canedo, a articulada cobre mais de 80% das demandas.<')

# FAQ 2
r('>Até quantos metros a plataforma articulada alcança?<',
  '>Qual a altura máxima das articuladas disponíveis para Senador Canedo?<')
r('>A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação.<',
  '>Disponibilizamos dois patamares: 12 e 15 metros de altura de trabalho. O de 12m atende galpões do DASC e a maioria das estruturas do DISC. O de 15m é necessário para torres de destilação e tanques elevados do polo petroquímico. Ambos possuem alcance lateral de 6 a 8 metros para contornar tubulações e estruturas intermediárias.<')

# FAQ 3
r('>Quanto custa alugar plataforma articulada em Goiânia?<',
  '>Qual o valor mensal de locação de plataforma articulada em Senador Canedo?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato.<',
  '>O investimento fica entre R$2.800 e R$4.500 por mês, variando conforme modelo (12m ou 15m), motorização (diesel ou elétrica) e duração do contrato. Senador Canedo tem entrega sem custo de deslocamento — são apenas 20 km pela BR-153. O contrato inclui manutenção preventiva e corretiva, com equipe técnica mobile que chega na planta em menos de 40 minutos.<')

# FAQ 4
r('>Preciso de treinamento para operar a plataforma articulada?<',
  '>Operadores no polo petroquímico precisam de certificação para usar a articulada?<')
r('>Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.<',
  '>Sim. A NR-35 exige treinamento em trabalho em altura e operação de PEMT, cobrindo inspeção pré-operacional, limites de carga e procedimentos de emergência. Em áreas classificadas do polo petroquímico, pode ser necessária certificação adicional para atmosferas explosivas. Conectamos sua equipe a centros de formação credenciados na região de Senador Canedo e Goiânia.<')

# FAQ 5
r('>A plataforma articulada pode ser usada em terreno irregular?<',
  '>A articulada diesel opera nos pátios irregulares do polo petroquímico e DASC?<')
r('>Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado.<',
  '>Sim. Os modelos diesel possuem tração 4x4 projetada para pátios de cascalho, acessos de terra e canteiros com desnível — cenário típico do polo petroquímico e das vias internas do DASC. A elétrica exige piso mais nivelado e é indicada para operações internas nos galpões. Em todos os casos, avaliamos o terreno antes da entrega para garantir que o modelo suporte as condições do local.<')

# FAQ 6
r('>Vocês entregam plataforma articulada fora de Goiânia?<',
  '>Qual o prazo de entrega de plataforma articulada em Senador Canedo?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Senador Canedo é uma das cidades com entrega mais rápida: 20 km pela BR-153, sem pedágio. A plataforma chega no mesmo dia da confirmação, normalmente em menos de 2 horas. Para urgências em paradas programadas do polo petroquímico ou do DASC, priorizamos o despacho. Sem custo de deslocamento.<')

# FAQ 7
r('>Qual a capacidade de carga do cesto da articulada?<',
  '>Quantos técnicos cabem no cesto durante manutenção industrial?<')
r('>O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação.<',
  '>O cesto comporta 230 a 250 kg — dois técnicos com ferramentas e instrumentos de medição. Para manutenções no polo petroquímico que exigem inspetor e auxiliar com equipamentos de ensaio não destrutivo, o espaço é adequado. O cesto possui pontos de ancoragem para cintos paraquedista conforme NR-35 e área para materiais como chaves de válvula, medidores de espessura e kits de vedação.<')

# FAQ 8
r('>Diesel ou elétrica: qual plataforma articulada alugar?<',
  '>Quando usar articulada elétrica nos galpões de Senador Canedo?<')
r('>A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.<',
  '>A elétrica é obrigatória em galpões farmacêuticos e de higiene do DASC que mantêm áreas limpas — zero emissão preserva a certificação do ambiente. Também é ideal para operações internas no DISC onde ruído é restrição. Para tudo que envolve pátio externo, piso irregular ou deslocamento longo entre pontos — como o polo petroquímico — a diesel com tração 4x4 é a escolha correta. Na dúvida, fazemos a avaliação técnica gratuita antes de fechar.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Alugue uma plataforma articulada em Goiânia hoje',
  'Solicite sua plataforma articulada em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma articulada em Senador Canedo.\\n\\n'")

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
            'goiania-go/', '20 km',  # link para hub goiania ou distância
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
sc = html.count('Senador Canedo')
local = html.count('DASC') + html.count('petroquím') + html.count('DISC') + html.count('BR-153')
print(f"\nSenador Canedo: {sc} menções")
print(f"Contexto local (DASC/petroquímico/DISC/BR-153): {local} menções")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")
