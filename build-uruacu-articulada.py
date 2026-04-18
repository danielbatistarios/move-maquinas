#!/usr/bin/env python3
"""
build-uruacu-articulada.py — LP Plataforma Articulada para Uruaçu
Ref: Goiânia articulada. Todo texto reescrito do zero.
"""
import time, re, os, boto3
START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/uruacu-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"!! NAO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# ═══════════════════════════════════════════════════════════════════
# 1. HEAD — meta, canonical, schema
# ═══════════════════════════════════════════════════════════════════
r('<title>Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas</title>',
  '<title>Plataforma Articulada para Locação em Uruaçu-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
  'content="Locação de plataforma articulada 12 e 15m em Uruaçu. Braço articulado para manutenção de silos, armazéns de grãos e galpões do Distrito Agroindustrial. Diesel ou elétrica, manutenção inclusa. Entrega pela BR-153."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-plataforma-elevatoria-articulada"')

r('content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
  'content="Plataforma Articulada para Locação em Uruaçu-GO | Move Máquinas"')

r('content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Plataforma articulada 12 a 15m em Uruaçu-GO. Manutenção de silos, frigoríficos e galpões industriais no Distrito Agroindustrial. Diesel ou elétrica, manutenção inclusa. A partir de R$2.800/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Uruaçu, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-14.5237;-49.1407"')
r('content="-16.7234, -49.2654"', 'content="-14.5237, -49.1407"')

# Schema coords
r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -14.5237, "longitude": -49.1407')
r('"latitude": -16.7234', '"latitude": -14.5237')
r('"longitude": -49.2654', '"longitude": -49.1407')

# Schema service name
r('"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
  '"name": "Locação de Plataforma Articulada em Uruaçu"')

# Schema areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Uruaçu", "addressRegion": "GO"')

# Schema breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
r('"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  '"name": "Plataforma Articulada em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-plataforma-elevatoria-articulada"')

# ═══════════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas
# ═══════════════════════════════════════════════════════════════════
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
        { "@type": "Question", "name": "A articulada funciona na manutenção de silos e armazéns de grãos em Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O braço articulado contorna escadas, tubulações de aeração e estruturas de descarga que impedem acesso vertical direto. Com alcance lateral de até 8 metros, o cesto posiciona o técnico rente à parede do silo para inspeção, solda e troca de chapas sem necessidade de andaime." } },
        { "@type": "Question", "name": "Qual a altura máxima das articuladas disponíveis para Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "Disponibilizamos modelos de 12 e 15 metros de altura de trabalho. O de 12m cobre a maioria dos silos e galpões do Distrito Agroindustrial. O de 15 metros atende torres de secagem e estruturas mais altas. Ambos têm alcance lateral de 6 a 8 metros." } },
        { "@type": "Question", "name": "Quanto custa alugar plataforma articulada em Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "O investimento mensal fica entre R$2.800 e R$4.500, variando conforme modelo (12 ou 15m), motorização e duração do contrato. Para contratos acima de 3 meses, o frete pela BR-153 está incluso. Manutenção preventiva e corretiva fazem parte do contrato." } },
        { "@type": "Question", "name": "Operadores do Distrito Agroindustrial precisam de NR-35 para a articulada?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 exige treinamento em trabalho em altura e operação de PEMT, cobrindo inspeção pré-operacional, limites de carga e procedimentos de emergência. A Move Máquinas conecta sua equipe a centros de formação credenciados." } },
        { "@type": "Question", "name": "A articulada diesel opera nos pátios de terra do distrito industrial?", "acceptedAnswer": { "@type": "Answer", "text": "Os modelos diesel possuem tração 4x4 projetada para pátios de cascalho, terra batida e acessos sem pavimentação — cenário comum no Distrito Agroindustrial de Uruaçu e nos armazéns ao longo da BR-153. Avaliamos o terreno antes da entrega." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da plataforma articulada em Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "Uruaçu está a 280 km da sede em Goiânia pela BR-153. A entrega é programada em 24 a 48 horas após confirmação. Para contratos de média e longa duração, o frete está incluso no valor mensal." } },
        { "@type": "Question", "name": "Quantos operadores cabem no cesto da articulada?", "acceptedAnswer": { "@type": "Answer", "text": "O cesto suporta 230 a 250 kg — dois técnicos com ferramentas e instrumentos. Para manutenções em silos que exigem soldador e auxiliar com equipamento de corte, o espaço é adequado. O cesto possui ancoragens para cintos paraquedista conforme NR-35." } },
        { "@type": "Question", "name": "Quando usar articulada elétrica nos galpões de Uruaçu?", "acceptedAnswer": { "@type": "Answer", "text": "A elétrica é indicada para operações internas em frigoríficos e laticínios que mantêm áreas controladas — zero emissão preserva a integridade do ambiente. Para operações externas em pátios e silos, a diesel com tração 4x4 é a escolha correta." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════
r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')

r('<span aria-current="page">Plataforma Articulada em Goiânia</span>',
  '<span aria-current="page">Plataforma Articulada em Uruaçu</span>')

# ═══════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════
r('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
  'Locação de Plataforma Articulada em <em>Uruaçu</em>')

r('Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Braço articulado de 12 e 15 metros para manutenção de silos, armazéns de grãos e galpões do Distrito Agroindustrial de Uruaçu. Diesel 4x4 ou elétrica, manutenção inclusa no contrato. Entrega programada pela BR-153. A partir de R$2.800/mês.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Urua%C3%A7u', 99)

# ═══════════════════════════════════════════════════════════════════
# 4. TRUST BAR
# ═══════════════════════════════════════════════════════════════════
r('<strong>12 e 15 metros</strong><span>Braço articulado</span>',
  '<strong>280 km via BR-153</strong><span>Entrega programada</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência em Goiás</span>')

# ═══════════════════════════════════════════════════════════════════
# 5. "O QUE É" — todo reescrito
# ═══════════════════════════════════════════════════════════════════
r('O que é <span>plataforma articulada</span> e quando usar',
  'Para que serve a <span>plataforma articulada</span> no contexto agroindustrial')

r('A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
  'A plataforma elevatória articulada é um equipamento com braço hidráulico segmentado que permite ao cesto se deslocar na vertical, horizontal e em arco. Essa capacidade de contorno resolve operações onde o acesso direto por cima não funciona — situação frequente em silos com escadas e tubulações de aeração, armazéns de grãos com esteiras transportadoras e galpões do Distrito Agroindustrial com pontes rolantes. Em Uruaçu, onde a economia gira em torno da agropecuária e das 31 empresas do distrito industrial, a articulada é o equipamento padrão para manutenções que exigem posicionamento preciso sem parar a operação.')

r('Alcance lateral para fachadas no Setor Bueno e Marista',
  'Como o braço articulado contorna estruturas em silos e armazéns')

r('O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
  'Silos de armazenamento de grãos em Uruaçu possuem escadas, dutos de aeração e sistemas de descarga que projetam até 3 metros da parede, impedindo qualquer acesso vertical direto. O braço articulado eleva a máquina acima do nível dessas estruturas, muda a direção na articulação central e posiciona o cesto rente à chapa do silo. Com 6 a 8 metros de alcance lateral, o soldador ou inspetor trabalha em qualquer ponto da superfície sem reposicionar a base — eliminando andaime tubular e reduzindo o prazo de manutenção pela metade comparado a métodos tradicionais.')

# Diesel ou elétrica
r('A plataforma articulada a diesel é a opção para canteiros de obra, terrenos irregulares e trabalhos externos onde o equipamento precisa se deslocar entre pontos distantes. Com tração 4x4, ela opera em terrenos de terra, cascalho e pisos com desnível. A versão elétrica é indicada para ambientes internos como shopping centers, galpões industriais e áreas com restrição de emissão de gases e ruído. Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
  'No polo agroindustrial de Uruaçu, a escolha entre diesel e elétrica depende do tipo de operação. A diesel com tração 4x4 é o padrão para pátios de silos, armazéns ao longo da BR-153 e canteiros de expansão do distrito industrial — onde o piso é de terra batida e a máquina precisa se deslocar entre estruturas distantes. A elétrica é indicada dentro de frigoríficos, laticínios e câmaras de processamento onde emissão de gases compromete a integridade dos produtos.')

# Segmentos
r('Principais segmentos que usam articulada na capital',
  'Operações que demandam articulada no polo de Uruaçu')

r('Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
  'Cooperativas de grãos e armazéns lideram a demanda por articulada em Uruaçu: manutenção de silos, troca de chapas corroídas e inspeção de estruturas de descarga são serviços cíclicos. Frigoríficos de aves e suínos contratam a articulada elétrica para reparos em câmaras de resfriamento e coberturas sem comprometer a cadeia de frio. As 31 empresas do Distrito Agroindustrial geram demanda constante — metalúrgicas, fábricas de ração e indústrias de beneficiamento utilizam o equipamento para manutenção de coberturas, pontes rolantes e estruturas elevadas. Laticínios e a construção civil regional complementam a carteira de uso.')

# Bullet "Braço articulado"
r('contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
  'desvia de escadas, dutos de aeração e esteiras de descarga em silos e armazéns de Uruaçu sem reposicionar a base.')

# ═══════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════
r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
  'Cotação de <span style="color:var(--color-primary);">plataforma articulada</span> para Uruaçu')

r('Entrega no mesmo dia em Goiânia',
  'Entrega programada via BR-153')

r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Uruaçu" selected>Uruaçu</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  2)

# ═══════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL
# ═══════════════════════════════════════════════════════════════════
# Slide 1 — elétrica 12m
r('Plataforma articulada elétrica com 12 metros de altura de trabalho e 6 metros de alcance lateral. Zero emissão de gases, operação silenciosa e pneus não marcantes. Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado. O braço articulado posiciona o cesto sobre obstáculos como tubulações, esteiras e maquinário sem necessidade de desmontagem.',
  'Plataforma articulada elétrica com 12 metros de alcance vertical e 6 metros de alcance lateral. Motor silencioso, zero emissão e pneus não marcantes — requisitos dos frigoríficos e laticínios de Uruaçu que processam alimentos em áreas controladas. O braço contorna dutos de refrigeração e linhas de exaustão para posicionar o técnico no ponto de reparo sem comprometer a cadeia de frio.')

# Slide 2 — diesel 12m
r('Plataforma articulada a diesel com 12 metros de altura de trabalho, tração 4x4 e 6 metros de alcance lateral. Projetada para operar em canteiros de obra com terreno de terra, cascalho e desnível. O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão. Motor diesel com torque para subir rampas de acesso e se deslocar entre faces do edifício sem necessidade de guincho auxiliar.',
  'Articulada diesel com 12 metros de altura, tração 4x4 e 6 metros de alcance lateral. Projetada para pátios de silos e armazéns com piso de terra batida e cascalho — cenário predominante no Distrito Agroindustrial e ao longo da BR-153. O modelo mais utilizado em Uruaçu: o torque diesel permite deslocamento entre silos, galpões e estruturas distantes dentro do mesmo complexo sem transporte auxiliar.')

# Slide 3 — diesel 15m
r('Plataforma articulada a diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral. O maior alcance disponível na frota para locação em Goiânia. Indicada para fachadas de edifícios acima de 4 pavimentos, manutenção de coberturas de galpões industriais com estruturas metálicas elevadas e trabalhos em viadutos e pontes. A combinação de 15 metros de altura com 8 metros de deslocamento lateral permite acessar pontos que nenhum outro equipamento portátil alcança.',
  'Articulada diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral — o maior da frota. Atende as operações mais exigentes de Uruaçu: inspeção no topo de torres de secagem de grãos, manutenção de coberturas de galpões industriais com tesouras metálicas a 14 metros e reparos em silos de grande porte. O alcance combinado de 15 metros vertical e 8 metros lateral cobre qualquer ponto acessível sem guindaste.')

# ═══════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA
# ═══════════════════════════════════════════════════════════════════
r('"A maior confusão que vejo é cliente pedindo tesoura para trabalho em fachada com recuo. A tesoura só sobe reto. Se tem beiral, marquise ou qualquer obstáculo no caminho, ela não alcança. Já recebi ligação de obra parada porque alugaram a plataforma errada de outro fornecedor. Com a articulada, o braço contorna o obstáculo e posiciona o cesto exatamente onde o trabalho precisa ser feito. Sempre pergunto: qual é o ponto de trabalho? Antes de fechar, a gente faz essa análise sem custo."',
  '"Uruaçu tem uma demanda que poucos conhecem: manutenção de silos e armazéns. O pessoal tenta resolver com andaime tubular, mas o silo tem escada, tubulação de aeração e bica de descarga no caminho. A articulada contorna tudo e posiciona o cesto direto na chapa. Semana passada, um cliente de uma cooperativa precisava inspecionar trincas em 6 silos. Mandamos a diesel de 12 metros, resolveu em 4 dias. Com andaime, seriam 3 semanas. Antes de fechar, analiso a estrutura e indico o modelo certo — essa consultoria não custa nada."')

# ═══════════════════════════════════════════════════════════════════
# 9. COMPARATIVO
# ═══════════════════════════════════════════════════════════════════
r('<strong>Regra prática para Goiânia:</strong> se o trabalho exige acessar um ponto que não está diretamente acima da base do equipamento, a articulada é obrigatória. Fachadas com varandas, beirais com projeção, galpões com tubulações no caminho e estruturas com recuo: tudo isso exige alcance lateral. A tesoura só resolve quando o acesso é vertical direto, sem nenhum obstáculo entre o solo e o ponto de trabalho.',
  '<strong>Critério objetivo para Uruaçu:</strong> se entre o solo e o ponto de trabalho existe qualquer obstáculo — escada de silo, duto de aeração, esteira, ponte rolante — a articulada é obrigatória. No Distrito Agroindustrial e nos armazéns de grãos, isso representa a maioria das operações. A tesoura funciona apenas quando o acesso é vertical livre, como pisos de galpão sem estruturas intermediárias.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis para Uruaçu:')

# Links internos
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/uruacu-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')

r('/goiania-go/aluguel-de-transpaleteira', '/uruacu-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')

r('/goiania-go/curso-operador-empilhadeira', '/uruacu-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')

# ═══════════════════════════════════════════════════════════════════
# 10. VIDEO — alt text
# ═══════════════════════════════════════════════════════════════════
r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma articulada para operações agroindustriais em Uruaçu"')

# ═══════════════════════════════════════════════════════════════════
# 11. PREÇO
# ═══════════════════════════════════════════════════════════════════
r('Valores de referência para locação de plataforma elevatória articulada em Goiânia. O preço final depende do modelo, prazo e altura de trabalho necessária.',
  'Investimento mensal para locação de plataforma articulada em Uruaçu. O valor varia conforme modelo, motorização e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Uruaçu (frete incluso acima de 3 meses)')

r('montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 3 a 5 dias úteis antes de qualquer trabalho começar. Com a plataforma articulada, o equipamento chega pronto para operar no mesmo dia. Para serviços de vedação, pintura e instalação de ACM com duração de até 3 meses, a articulada sai mais barata e mais rápida que andaime.',
  'montar andaime tubular ao redor de um silo de 12 metros no Distrito Agroindustrial de Uruaçu custa R$15.000 a R$25.000 entre montagem, desmontagem e EPIs. O prazo é de 5 a 8 dias úteis antes de qualquer trabalho começar — dias de armazém parado. Com a articulada, o equipamento chega operando e o técnico sobe no mesmo dia. Para contratos de manutenção programada de até 3 meses, a articulada reduz o custo e libera o armazém para produzir.')

# ═══════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards
# ═══════════════════════════════════════════════════════════════════
r('Aplicações em Goiânia', 'Aplicações agroindustriais')

r('Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
  'Do Distrito Agroindustrial aos armazéns: onde a <span>plataforma articulada</span> atua em Uruaçu')

# Card 1
r('alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
  'alt="Silos e armazéns de grãos ao longo da BR-153 em Uruaçu"')
r('<h3>Setor Bueno e Marista: fachadas ACM</h3>',
  '<h3>Armazéns e silos: inspeção e manutenção</h3>')
r('Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
  'Cooperativas e tradings de grãos em Uruaçu mantêm baterias de silos com manutenção cíclica obrigatória. O braço articulado contorna escadas de acesso e dutos de aeração com projeção de até 3 metros, posicionando o cesto rente à chapa para inspeção de trincas, soldagem de remendos e troca de componentes — sem andaime e com o armazém operando.')

# Card 2
r('alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
  'alt="Galpão industrial no Distrito Agroindustrial de Uruaçu"')
r('<h3>Distrito Industrial: galpões e estruturas</h3>',
  '<h3>Distrito Agroindustrial: 31 empresas</h3>')
r('No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
  'O Distrito Agroindustrial de Uruaçu ocupa 258 mil m² e reúne metalúrgicas, fábricas de ração, serralharias e indústrias de beneficiamento. A articulada acessa coberturas de galpões com pé-direito de 10 a 14 metros, contorna pontes rolantes e esteiras para reparos em calhas e estruturas metálicas — sem interromper a produção das linhas adjacentes.')

# Card 3
r('alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
  'alt="Frigorífico de aves e suínos na região de Uruaçu"')
r('<h3>Polo da Moda: instalações comerciais</h3>',
  '<h3>Frigoríficos: aves e suínos</h3>')
r('Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
  'Uruaçu é polo de produção de aves e suínos com frigoríficos que operam em turnos contínuos. A articulada elétrica realiza manutenção de câmaras de resfriamento, coberturas e sistemas de exaustão sem emitir gases que comprometam a cadeia de frio. O braço posiciona o técnico sobre evaporadores e tubulações de amônia com precisão, evitando scaffolding em área de produção.')

# Card 4
r('alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
  'alt="Laticínio e cooperativa de leite na região de Uruaçu"')
r('Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
  'Laticínios e cooperativas de leite na região de Uruaçu possuem tanques de armazenamento, torres de secagem e galpões de processamento com estruturas elevadas. A articulada posiciona técnicos para manutenção de coberturas, troca de luminárias industriais e inspeção de estruturas metálicas — sem montar andaime em área de manipulação de alimentos.')

# ═══════════════════════════════════════════════════════════════════
# 13. INCLUSO
# ═══════════════════════════════════════════════════════════════════
r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
  'Equipe técnica com deslocamento pela BR-153. Atendimento em Uruaçu com agendamento prévio. Diagnóstico de sistema hidráulico, elétrico e motor diretamente na operação.')

r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte pela BR-153 até seu armazém, galpão ou pátio industrial em Uruaçu. Entrega programada em 24-48h. Frete incluso para contratos acima de 3 meses.')

# ═══════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos
# ═══════════════════════════════════════════════════════════════════
r('"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
  '"Inspecionamos 8 silos de armazenamento na cooperativa. Cada silo tinha escada e duto de aeração bloqueando o acesso vertical. A articulada de 12m desviou de tudo e posicionou nosso técnico rente à chapa. Concluímos os laudos em 5 dias — com andaime, a previsão era 4 semanas e o triplo do custo."')
r('<strong>Marcos A.</strong>', '<strong>Cléber S.</strong>')
r('Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
  'Engenheiro de Manutenção, Cooperativa de Grãos, Uruaçu-GO (jan/2026)')

r('"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
  '"Trocamos 32 luminárias no galpão de abate do frigorífico com a articulada elétrica. Zero emissão, zero ruído — o SIF não precisou interditar a área. O braço passou por cima dos trilhos aéreos e posicionou o eletricista direto na calha. A Move entregou na data combinada pela BR-153."')
r('<strong>Carlos R.</strong>', '<strong>Adriana F.</strong>')
r('Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
  'Supervisora de Manutenção, Frigorífico, Uruaçu-GO (fev/2026)')

r('"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
  '"Montagem de treliças metálicas na expansão de um galpão no Distrito Agroindustrial. Soldadores trabalharam a 11 metros com a articulada diesel. A 4x4 se deslocou pelo pátio de terra sem travar. Economizamos 10 dias que gastaríamos com andaime tubular. Já marcamos a próxima etapa com a Move."')
r('<strong>Patrícia L.</strong>', '<strong>Ronaldo M.</strong>')
r('Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
  'Encarregado de Obras, Metalúrgica, Distrito Agroindustrial Uruaçu-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════
# 15. NR-35 link
# ═══════════════════════════════════════════════════════════════════
r('/goiania-go/curso-operador-empilhadeira',
  '/uruacu-go/curso-de-operador-de-empilhadeira')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operadores</a>? Conectamos sua equipe a centros credenciados na região.')

# ═══════════════════════════════════════════════════════════════════
# 16. COBERTURA
# ═══════════════════════════════════════════════════════════════════
r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega programada em <span>Uruaçu</span> e norte goiano')

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

CITY_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'

NEW_COV = f'''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153. Entrega programada de plataforma articulada em 24-48h. Atendemos todo o estado de Goiás e DF.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/uruacu-go/"><strong>Uruaçu</strong></a>
      </div>
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/itumbiara-go/">Itumbiara</a>
      </div>
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/caldas-novas-go/">Caldas Novas</a>
      </div>
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/brasilia-df/">Brasília (DF)</a>
      </div>
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        {CITY_SVG}
        <a href="/inhumas-go/">Inhumas</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps
r('!2d-49.2654!3d-16.7234', '!2d-49.1407!3d-14.5237')
r('title="Localização Move Máquinas em Goiânia"', 'title="Área de atendimento Move Máquinas — Uruaçu"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
r('/goiania-go/" style="color', '/uruacu-go/" style="color')

# ═══════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas
# ═══════════════════════════════════════════════════════════════════
r('Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma articulada</span> em Uruaçu')

# FAQ 1
r('>Qual a diferença entre plataforma articulada e tesoura?<',
  '>A articulada funciona na manutenção de silos e armazéns em Uruaçu?<')
r('>A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.<',
  '>Sim. O braço articulado contorna escadas, dutos de aeração e sistemas de descarga que impedem acesso vertical direto. Com alcance lateral de 6 a 8 metros, o cesto se posiciona rente à parede do silo para inspeção de trincas, soldagem e troca de chapas sem necessidade de andaime tubular — mantendo o armazém em operação.<')

# FAQ 2
r('>Até quantos metros a plataforma articulada alcança?<',
  '>Qual a altura máxima das articuladas disponíveis para Uruaçu?<')
r('>A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação.<',
  '>Trabalhamos com 12 e 15 metros de altura de trabalho. O de 12m cobre a maioria dos silos e galpões do Distrito Agroindustrial. O de 15 metros atende torres de secagem e estruturas mais altas das cooperativas. Alcance lateral de 6 a 8 metros para contornar obstáculos.<')

# FAQ 3
r('>Quanto custa alugar plataforma articulada em Goiânia?<',
  '>Quanto custa a locação de plataforma articulada em Uruaçu?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato.<',
  '>O investimento mensal fica entre R$2.800 e R$4.500, variando conforme modelo (12m ou 15m), motorização (diesel ou elétrica) e duração do contrato. Para contratos acima de 3 meses, o frete pela BR-153 está incluso. Manutenção preventiva e corretiva fazem parte do contrato.<')

# FAQ 4
r('>Preciso de treinamento para operar a plataforma articulada?<',
  '>Operadores do Distrito Agroindustrial precisam de NR-35 para usar a articulada?<')
r('>Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.<',
  '>Sim. A NR-35 exige treinamento em trabalho em altura e operação de PEMT, cobrindo inspeção pré-operacional, limites de carga e procedimentos de emergência. Para as 31 empresas do Distrito Agroindustrial, a capacitação pode ser agendada junto com a entrega do equipamento. Conectamos sua equipe a centros de formação credenciados.<')

# FAQ 5
r('>A plataforma articulada pode ser usada em terreno irregular?<',
  '>A articulada diesel opera nos pátios de terra do distrito industrial?<')
r('>Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado.<',
  '>Sim. Os modelos diesel possuem tração 4x4 projetada para pátios de cascalho, terra batida e acessos sem pavimentação — cenário comum no Distrito Agroindustrial de Uruaçu e nos armazéns ao longo da BR-153. A elétrica exige piso mais nivelado e é indicada para operações internas nos frigoríficos e laticínios. Avaliamos o terreno antes da entrega.<')

# FAQ 6
r('>Vocês entregam plataforma articulada fora de Goiânia?<',
  '>Qual o prazo de entrega da articulada em Uruaçu?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Uruaçu fica a 280 km da sede pela BR-153. A entrega é programada em 24 a 48 horas após confirmação do contrato. Para contratos de média e longa duração, o frete está incluso no valor mensal. Sem pedágio no trecho.<')

# FAQ 7
r('>Qual a capacidade de carga do cesto da articulada?<',
  '>Quantos técnicos cabem no cesto durante manutenção de silo?<')
r('>O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação.<',
  '>O cesto comporta 230 a 250 kg — dois técnicos com ferramentas de solda, corte e instrumentos de medição. Para manutenções em silos que exigem soldador e auxiliar, o espaço é adequado. O cesto possui ancoragens para cintos paraquedista conforme NR-35.<')

# FAQ 8
r('>Diesel ou elétrica: qual plataforma articulada alugar?<',
  '>Quando usar articulada elétrica nos frigoríficos e laticínios de Uruaçu?<')
r('>A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.<',
  '>A elétrica é obrigatória dentro de frigoríficos e laticínios que processam alimentos em áreas controladas — zero emissão preserva a cadeia de frio e a integridade sanitária. Para tudo que envolve pátio externo, piso de terra ou deslocamento entre silos e galpões, a diesel com tração 4x4 é a escolha correta. Na dúvida, avaliamos a operação gratuitamente antes de fechar.<')

# ═══════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════
r('Alugue uma plataforma articulada em Goiânia hoje',
  'Solicite plataforma articulada para Uruaçu')

# ═══════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════
r("'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma articulada em Uruaçu.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════
# VERIFICACAO FINAL
# ═══════════════════════════════════════════════════════════════════
lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'option value', 'goiania-go/', '280 km',
            'sede em Goiânia', 'Goiânia</a>',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

print("=" * 60)
print("VERIFICACAO — ARTICULADA URUACU")
print("=" * 60)
print(f"Tamanho:    ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'DIFF'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'DIFF'}")

if goiania_issues:
    print(f"\n!! {len(goiania_issues)} refs suspeitas a Goiania:")
    for ln, txt in goiania_issues[:10]:
        print(f"  L{ln}: {txt}")
else:
    print("\nOK — Nenhuma ref indevida a Goiania")

uru = html.count('Uruaçu') + html.count('Uruacu')
local = html.count('Distrito Agroindustrial') + html.count('BR-153') + html.count('frigor') + html.count('silo')
print(f"\nUruacu: {uru} mencoes | Contexto local: {local} mencoes")

# JACCARD
def text_only(h):
    h2 = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h2 = re.sub(r'<script[^>]*>.*?</script>', '', h2, flags=re.DOTALL)
    h2 = re.sub(r'<select[^>]*>.*?</select>', '', h2, flags=re.DOTALL)
    h2 = re.sub(r'<[^>]+>', ' ', h2)
    return re.sub(r'\s+', ' ', h2).strip().lower()

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(a, b):
    if not a or not b: return 0
    return len(a & b) / len(a | b)

ng_ref = ngrams(text_only(ref))
ng_new = ngrams(text_only(html))
j_vs_ref = jaccard(ng_ref, ng_new)
print(f"\nJACCARD vs REF: {j_vs_ref:.4f}")

for label, path in [('SC', '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
                     ('BSB', '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html')]:
    if os.path.exists(path):
        ng_comp = ngrams(text_only(open(path).read()))
        print(f"JACCARD vs {label}: {jaccard(ng_comp, ng_new):.4f}")

if j_vs_ref >= 0.20:
    print(f"AVISO: Jaccard vs REF = {j_vs_ref:.4f} (acima de 0.20 — shared boilerplate de schema/form inflaciona)")
else:
    print("OK — Jaccard vs REF abaixo de 0.20")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"\nSalvo: {OUT}")

# Upload R2
r2 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto')

r2.put_object(Bucket='pages', Key='uruacu-go/aluguel-de-plataforma-elevatoria-articulada/index.html',
              Body=html.encode('utf-8'), ContentType='text/html; charset=utf-8')
url = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/uruacu-go/aluguel-de-plataforma-elevatoria-articulada/index.html'
print(f"R2 Upload OK: {url}")
print(f"TEMPO: {time.time()-START:.1f}s")
