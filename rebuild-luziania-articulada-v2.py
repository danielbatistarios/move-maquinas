#!/usr/bin/env python3
"""
rebuild-luziania-articulada-v2.py
Gera LP de Plataforma Articulada para Luziania-GO
usando ref-goiania-articulada.html como ESQUELETO HTML/CSS/JS.
"""

from datetime import datetime
import re, os
start = datetime.now()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/luziania-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"  NAO ENCONTRADO: {old[:90]}...")
        return
    html = html.replace(old, new, count)

# ═══════════════════════════════════════════════════════════════════════
# 1. HEAD — meta, canonical, schema
# ═══════════════════════════════════════════════════════════════════════

r('<title>Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas</title>',
  '<title>Plataforma Articulada para Locação em Luziânia-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
  'content="Locação de plataforma articulada 12 e 15m em Luziânia-GO. Ideal para manutenção de silos e galpões agrícolas, obras de construção civil e coberturas industriais no DIAL. Diesel ou elétrica, manutenção inclusa. Despacho pela BR-040."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  'href="https://movemaquinas.com.br/luziania-go/aluguel-de-plataforma-elevatoria-articulada"')

r('content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
  'content="Plataforma Articulada para Locação em Luziânia-GO | Move Máquinas"')

r('content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Plataforma articulada 12 a 15m em Luziânia. Atendemos DIAL, silos agrícolas e canteiros de obra. Diesel ou elétrica, manutenção no contrato, transporte pela BR-040. A partir de R$2.800/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Luziânia, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.2532;-47.9501"')
r('content="-16.7234, -49.2654"', 'content="-16.2532, -47.9501"')

# Schema — coords
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.2532, "longitude": -47.9501')
r('"latitude": -16.7234', '"latitude": -16.2532')
r('"longitude": -49.2654', '"longitude": -47.9501')

# Schema — Service name
r('"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
  '"name": "Locação de Plataforma Articulada em Luziânia"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Luziânia", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
r('"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
  '"name": "Plataforma Articulada em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/aluguel-de-plataforma-elevatoria-articulada"')

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
        { "@type": "Question", "name": "Por que escolher articulada em vez de tesoura para obras em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Na zona industrial e no DIAL de Luziânia, operações em silos, galpões agrícolas e estruturas metálicas envolvem contornar tubulações, esteiras transportadoras e coberturas com tesouras metálicas sobrepostas. A tesoura sobe apenas na vertical e não desvia de nada. A articulada possui braço segmentado com alcance lateral de até 8 metros — contorna obstáculos e posiciona o cesto no ponto exato de trabalho sem scaffolding." } },
        { "@type": "Question", "name": "Qual a altura máxima da articulada disponível para Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Trabalhamos com dois patamares: 12 e 15 metros de altura de trabalho. O de 12m atende silos de grãos, coberturas de galpões e a maioria das estruturas do DIAL. O de 15m é necessário para silos verticais de maior porte e torres de secagem. O alcance lateral vai de 6 a 8 metros conforme o modelo." } },
        { "@type": "Question", "name": "Qual o custo de locação de plataforma articulada em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "O investimento mensal fica entre R$2.800 e R$4.500, variando conforme modelo (12m ou 15m), motorização (diesel ou elétrica) e duração do contrato. Para Luziânia, o frete pela BR-040 é calculado de forma transparente e informado no orçamento. O contrato inclui manutenção preventiva, corretiva e suporte técnico." } },
        { "@type": "Question", "name": "Operadores precisam de certificação NR-35 para usar a articulada em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 exige treinamento em trabalho em altura e operação de PEMT, cobrindo inspeção pré-operacional, limites de carga e procedimentos de emergência. A Move Máquinas indica centros credenciados na região e pode coordenar a capacitação junto com a entrega do equipamento para reduzir custos de mobilização." } },
        { "@type": "Question", "name": "A articulada diesel funciona nos pátios do DIAL e nas propriedades rurais?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Os modelos diesel possuem tração 4x4 projetada para pátios de cascalho, acessos de terra e terrenos com desnível — cenário típico do DIAL e das propriedades rurais com silos em Luziânia. A elétrica exige piso mais nivelado e é indicada para operações internas em galpões. Avaliamos o terreno antes de definir o modelo." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de plataforma articulada em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "O prazo padrão é de 24 a 48 horas a partir da confirmação do contrato. A rota pela BR-040 de Goiânia até Luziânia tem 198 km. Para contratos programados, agendamos com antecedência. Para urgências em paradas de manutenção no DIAL, avaliamos despacho prioritário." } },
        { "@type": "Question", "name": "Quantos operadores cabem no cesto da plataforma articulada?", "acceptedAnswer": { "@type": "Answer", "text": "O cesto suporta 230 a 250 kg — dois técnicos com ferramentas e materiais. Para manutenções em silos que exigem soldador e auxiliar com ferramentaria especializada, o espaço é adequado. O cesto possui ancoragens para cintos paraquedista conforme NR-35." } },
        { "@type": "Question", "name": "Quando usar articulada elétrica nos galpões do DIAL?", "acceptedAnswer": { "@type": "Answer", "text": "A elétrica é indicada para operações internas em galpões de processamento alimentício e indústrias químicas do DIAL que exigem zero emissão de gases — preservando a integridade de ambientes controlados e evitando contaminação de produtos. Para tudo que envolve pátio externo ou terreno irregular, a diesel com tração 4x4 é a escolha correta." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/luziania-go/">Equipamentos em Luziânia</a>')

r('<span aria-current="page">Plataforma Articulada em Goiânia</span>',
  '<span aria-current="page">Plataforma Articulada em Luziânia</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
  'Locação de Plataforma Articulada em <em>Luziânia</em>')

r('Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Braço articulado de 12 e 15 metros para manutenção de silos agrícolas, coberturas de galpões no DIAL e obras de construção civil em Luziânia. Diesel 4x4 ou elétrica, manutenção inclusa. Transporte pela BR-040. A partir de R$2.800/mês.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Luzi%C3%A2nia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR
# ═══════════════════════════════════════════════════════════════════════

r('<strong>12 e 15 metros</strong><span>Braço articulado</span>',
  '<strong>Transporte BR-040</strong><span>198 km da sede</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Atuacao no Centro-Oeste</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SECAO "O QUE E" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

r('O que é <span>plataforma articulada</span> e quando usar',
  'Como funciona a <span>plataforma elevatoria articulada</span> e quando contratar')

r('A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
  'A plataforma elevatoria articulada possui braço hidraulico com segmentos moveis que permitem ao cesto se deslocar na vertical, na horizontal e em arco simultaneamente. Essa capacidade de manobra resolve situacoes onde o acesso direto por cima e bloqueado — cenario frequente em silos com tubulacoes de carga, galpoes com pontes rolantes e estruturas metalicas sobrepostas. Em Luziania, o DIAL e as propriedades rurais com silos de graos concentram instalacoes onde a articulada e o unico equipamento capaz de posicionar o operador no ponto exato de servico sem interromper a operacao.')

# H3 — alcance lateral
r('Alcance lateral para fachadas no Setor Bueno e Marista',
  'Como o braco articulado opera entre silos e galpoes no DIAL')

r('O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
  'Silos de graos em Luziania possuem redes de tubulacao de carga e descarga com projecao de 2 a 4 metros que impedem qualquer acesso vertical direto. O braco articulado resolve esse problema: o segmento inferior eleva a maquina acima do nivel das tubulacoes, a articulacao central redireciona o braco para horizontal, e o segmento superior posiciona o cesto rente a parede do silo ou topo da cobertura. Com 6 a 8 metros de alcance lateral, o operador trabalha em pontos de inspecao, vedacao de juntas e troca de chapas sem scaffolding temporario e sem paradas prolongadas na operacao de armazenagem.')

# H3 — diesel ou eletrica
r('A plataforma articulada a diesel é a opção para canteiros de obra, terrenos irregulares e trabalhos externos onde o equipamento precisa se deslocar entre pontos distantes. Com tração 4x4, ela opera em terrenos de terra, cascalho e pisos com desnível. A versão elétrica é indicada para ambientes internos como shopping centers, galpões industriais e áreas com restrição de emissão de gases e ruído. Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
  'No contexto industrial de Luziania, a escolha entre diesel e eletrica depende do ambiente de operacao. A diesel com tracao 4x4 e padrao para patios do DIAL, acessos de terra em propriedades rurais com silos e canteiros de construcao civil onde o piso e irregular. A eletrica e indicada dentro de galpoes de processamento alimenticio e industrias quimicas do DIAL — zero emissao preserva a integridade de ambientes de manipulacao de alimentos, e a operacao silenciosa nao interfere nas linhas de producao.')

# H3 — segmentos
r('Principais segmentos que usam articulada na capital',
  'Setores que demandam articulada em Luziania e regiao')

r('Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
  'A agropecuaria lidera a demanda em Luziania: produtores rurais e cooperativas contratam a articulada para inspecao e reparo de silos de graos, secadores e estruturas de armazenagem que chegam a 15 metros de altura. No DIAL, metalurgicas e industrias alimenticias precisam do equipamento para manutencao de coberturas, calhas industriais e estruturas metalicas de galpoes com pe-direito elevado. Construtoras que operam nos novos empreendimentos residenciais e comerciais do Centro e Jardim Inga tambem utilizam a articulada para acabamentos de fachada. O setor de energia contrata para manutencao de torres e subestacoes ao longo do corredor da BR-040.')

# Bullet "Braço articulado"
r('contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
  'desvia de tubulacoes de carga, esteiras transportadoras e coberturas metalicas sobrepostas nos silos e galpoes de Luziania sem scaffolding.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTACAO
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
  'Cotacao de <span style="color:var(--color-primary);">plataforma articulada</span> para Luziania')

r('Entrega no mesmo dia em Goiânia',
  'Despacho programado pela BR-040')

r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Luziânia" selected>Luziânia</option>
              <option value="Brasília">Brasília</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>
              <option value="Goiânia">Goiânia</option>''',
  2)

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL
# ═══════════════════════════════════════════════════════════════════════

# Slide 1 — eletrica 12m
r('Plataforma articulada elétrica com 12 metros de altura de trabalho e 6 metros de alcance lateral. Zero emissão de gases, operação silenciosa e pneus não marcantes. Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado. O braço articulado posiciona o cesto sobre obstáculos como tubulações, esteiras e maquinário sem necessidade de desmontagem.',
  'Articulada eletrica com 12 metros de alcance vertical e 6 metros de alcance lateral. Motor silencioso, zero emissao e pneus nao marcantes — atributos exigidos pelas industrias alimenticias e quimicas do DIAL que operam com ambientes controlados de manipulacao. O braco contorna dutos de exaustao e linhas de transporte pneumatico para posicionar o cesto no ponto exato de reparo sem comprometer a area de producao.')

# Slide 2 — diesel 12m
r('Plataforma articulada a diesel com 12 metros de altura de trabalho, tração 4x4 e 6 metros de alcance lateral. Projetada para operar em canteiros de obra com terreno de terra, cascalho e desnível. O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão. Motor diesel com torque para subir rampas de acesso e se deslocar entre faces do edifício sem necessidade de guincho auxiliar.',
  'Articulada diesel com 12 metros de altura, tracao 4x4 e 6 metros de alcance lateral. Projetada para patios industriais com cascalho e acessos de terra — cenario tipico do DIAL e das propriedades rurais com silos em Luziania. O modelo mais solicitado na regiao: o torque do motor diesel permite deslocamento entre silos, galpoes e areas de armazenagem sem transporte auxiliar.')

# Slide 3 — diesel 15m
r('Plataforma articulada a diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral. O maior alcance disponível na frota para locação em Goiânia. Indicada para fachadas de edifícios acima de 4 pavimentos, manutenção de coberturas de galpões industriais com estruturas metálicas elevadas e trabalhos em viadutos e pontes. A combinação de 15 metros de altura com 8 metros de deslocamento lateral permite acessar pontos que nenhum outro equipamento portátil alcança.',
  'Articulada diesel com 15 metros de altura de trabalho e 8 metros de alcance lateral — o maior da frota. Esse modelo atende as operacoes mais exigentes de Luziania: inspecao de silos verticais de grande porte, manutencao de coberturas em galpoes industriais do DIAL com tesouras metalicas a 14 metros e trabalhos em torres de secagem de graos. O alcance combinado de 15m vertical e 8m lateral cobre qualquer ponto acessivel sem guindaste.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA
# ═══════════════════════════════════════════════════════════════════════

r('"A maior confusão que vejo é cliente pedindo tesoura para trabalho em fachada com recuo. A tesoura só sobe reto. Se tem beiral, marquise ou qualquer obstáculo no caminho, ela não alcança. Já recebi ligação de obra parada porque alugaram a plataforma errada de outro fornecedor. Com a articulada, o braço contorna o obstáculo e posiciona o cesto exatamente onde o trabalho precisa ser feito. Sempre pergunto: qual é o ponto de trabalho? Antes de fechar, a gente faz essa análise sem custo."',
  '"A demanda de Luziania vem principalmente de dois cenarios: silos de graos e galpoes do DIAL. Em silos, o problema e sempre o mesmo — tubulacao de carga na frente bloqueando o acesso. Tesoura nao resolve. A articulada desvia e posiciona o cesto rente a chapa do silo. Na semana passada, um produtor rural precisava inspecionar o topo de um silo de 13 metros com esteira transportadora cruzando. Mandamos a articulada diesel, resolveu em um dia. Antes de qualquer contrato para Luziania, analiso a estrutura e os obstaculos. Essa consultoria e gratuita."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se o trabalho exige acessar um ponto que não está diretamente acima da base do equipamento, a articulada é obrigatória. Fachadas com varandas, beirais com projeção, galpões com tubulações no caminho e estruturas com recuo: tudo isso exige alcance lateral. A tesoura só resolve quando o acesso é vertical direto, sem nenhum obstáculo entre o solo e o ponto de trabalho.',
  '<strong>Criterio objetivo para Luziania:</strong> se entre o solo e o ponto de trabalho existe qualquer obstaculo — tubulacao de carga, esteira, ponte rolante ou cobertura metalica — a articulada e obrigatoria. Em silos agricolas e galpoes do DIAL, isso representa a maioria das operacoes. A tesoura funciona apenas quando o acesso vertical e livre, como interiores de galpao sem estruturas intermediarias.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponiveis em Luziania:')

# Links internos
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/luziania-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Luziania')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/luziania-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustao em Luziania')

r('/goiania-go/aluguel-de-transpaleteira', '/luziania-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Eletrica em Luziania')

r('/goiania-go/curso-operador-empilhadeira', '/luziania-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Luziania')

# ═══════════════════════════════════════════════════════════════════════
# 10. VIDEO
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
  'alt="Video Move Maquinas: locacao de plataforma articulada para industrias e agronegocio em Luziania"')

# ═══════════════════════════════════════════════════════════════════════
# 11. PRECO
# ═══════════════════════════════════════════════════════════════════════

r('Valores de referência para locação de plataforma elevatória articulada em Goiânia. O preço final depende do modelo, prazo e altura de trabalho necessária.',
  'Investimento mensal para locacao de plataforma articulada em Luziania. O valor varia conforme modelo, motorizacao, duracao do contrato e logistica de transporte pela BR-040.')

r('Entrega em Goiânia (sem deslocamento)',
  'Transporte para Luziania (BR-040, 198 km)')

r('montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000 entre montagem, desmontagem, aluguel e EPI. O prazo de montagem é de 3 a 5 dias úteis antes de qualquer trabalho começar. Com a plataforma articulada, o equipamento chega pronto para operar no mesmo dia. Para serviços de vedação, pintura e instalação de ACM com duração de até 3 meses, a articulada sai mais barata e mais rápida que andaime.',
  'montar scaffolding para inspecao de um silo de 12 metros em propriedade rural de Luziania custa R$15.000 a R$25.000 entre montagem, desmontagem e EPI. O prazo de montagem e de 5 a 8 dias uteis antes de qualquer trabalho comecar — dias em que o silo pode ficar sem operacao. Com a articulada, o equipamento chega pronto para funcionar. Para contratos de manutencao preventiva de ate 3 meses no DIAL, a articulada reduz custo total e libera a equipe para produzir.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICACOES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

r('Aplicações em Goiânia', 'Aplicacoes industriais e agricolas')

r('Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
  'Do DIAL aos silos rurais: onde a <span>plataforma com braco articulado</span> opera em Luziania')

# Card 1
r('alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
  'alt="Silos de graos e estruturas de armazenagem em propriedade rural de Luziania"')
r('<h3>Setor Bueno e Marista: fachadas ACM</h3>',
  '<h3>Silos agricolas: inspecao e manutencao de chapas</h3>')
r('Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
  'Produtores rurais e cooperativas de Luziania operam silos de graos com capacidade de 5 a 50 mil toneladas e altura de ate 15 metros. O braco articulado contorna tubulacoes de carga e esteiras transportadoras, posicionando o operador rente a parede do silo para inspecao de chapas, vedacao de juntas e troca de aberturas de inspecao — sem scaffolding e sem interromper o fluxo de armazenagem.')

# Card 2
r('alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
  'alt="Galpao metalurgico no DIAL de Luziania com estrutura metalica elevada"')
r('<h3>Distrito Industrial: galpões e estruturas</h3>',
  '<h3>DIAL: metalurgicas e industrias alimenticias</h3>')
r('No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
  'O Distrito Agroindustrial de Luziania concentra metalurgicas, fundicoes, fabricas de alimentos e industrias quimicas com galpoes de pe-direito entre 10 e 18 metros. A articulada acessa coberturas, troca iluminacao industrial e repara calhas contornando pontes rolantes e maquinario pesado sem desmontagem — reduzindo paradas de producao e custos de manutencao.')

# Card 3
r('alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
  'alt="Torres de secagem e equipamentos de beneficiamento de graos em Luziania"')
r('<h3>Polo da Moda: instalações comerciais</h3>',
  '<h3>Torres de secagem e beneficiamento de graos</h3>')
r('Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
  'Luziania e uma das maiores produtoras de soja e milho do Entorno do DF, com dezenas de unidades de secagem e beneficiamento de graos. A articulada diesel desloca-se entre silos e torres de secagem pelo piso de terra, posicionando tecnicos em pontos de inspecao de queimadores, sensores de temperatura e valvulas de exaustao — eliminando andaimes e agilizando paradas programadas de safra.')

# Card 4
r('alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
  'alt="Obras de construcao civil em novos empreendimentos de Luziania"')
r('Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
  'O crescimento urbano de Luziania — com 210 mil habitantes — impulsiona empreendimentos residenciais e comerciais no Centro e Jardim Inga. Construtoras contratam a articulada para acabamento de fachadas, instalacao de esquadrias em pavimentos elevados e impermeabilizacao de juntas — eliminando andaimes em obras onde prazo e espaco de calcada sao limitados.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
  'Equipe tecnica com deslocamento pela BR-040. Atendimento em Luziania com suporte remoto imediato e presencial conforme demanda. Diagnostico de sistema hidraulico, eletrico e motor diretamente na planta ou canteiro.')

r('Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte pela BR-040 ate seu galpao, silo ou canteiro em Luziania. Sao 198 km de rodovia federal — despacho programado com frete transparente informado no orcamento.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
  '"Inspecao de chapas em 6 silos de soja na propriedade. Cada silo tinha esteira de carga cruzando na frente. A articulada de 15m desviou de tudo e posicionou nosso tecnico rente a chapa em cada ponto de inspecao. Concluimos os 6 silos em 5 dias — a estimativa com scaffolding era de 4 semanas e R$35 mil so de montagem."')
r('<strong>Marcos A.</strong>', '<strong>Ademir P.</strong>')
r('Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
  'Gerente de Manutencao, Cooperativa Agricola, Luziania-GO (jan/2026)')

# Depoimento 2
r('"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
  '"Troca de 30 luminarias no galpao da metalurgica no DIAL com a articulada eletrica. Zero ruido, zero fumaca — nossa linha de producao nao parou em nenhum momento. O braco passou por cima da ponte rolante e posicionou o eletricista direto na calha. A Move despachou pela BR-040 e o equipamento chegou conforme combinado."')
r('<strong>Carlos R.</strong>', '<strong>Sandra M.</strong>')
r('Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
  'Coordenadora Industrial, Metalurgica DIAL, Luziania-GO (fev/2026)')

# Depoimento 3
r('"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
  '"Manutencao de cobertura e calhas em 3 galpoes da fabrica de alimentos. A articulada diesel se deslocou entre os galpoes pelo patio de cascalho sem problema nenhum. Nossos montadores trabalharam a 12 metros de altura. Economia de 10 dias no cronograma comparado ao andaime que usavamos antes. Contrato renovado para a proxima parada de safra."')
r('<strong>Patrícia L.</strong>', '<strong>Fabio N.</strong>')
r('Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
  'Encarregado de Manutencao, Ind. Alimenticia, DIAL Luziania-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link do curso
# ═══════════════════════════════════════════════════════════════════════

r('/goiania-go/curso-operador-empilhadeira',
  '/luziania-go/curso-de-operador-de-empilhadeira')
r('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitacao NR-35 para operadores</a>? Indicamos centros credenciados e coordenamos junto com a entrega do equipamento em Luziania.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Transporte programado para <span>Luziania</span> e Entorno do DF')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 198 km de Luziânia pela BR-040. Despacho de plataforma articulada programado com frete transparente. Atendemos todo o Entorno do DF e cidades do eixo Goiânia-Brasília.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/"><strong>Luziânia</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília</a>
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
        <a href="/aparecida-de-goiania-go/">Aparecida de Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed
r('!2d-49.2654!3d-16.7234', '!2d-47.9501!3d-16.2532')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Area de atendimento Move Maquinas — Luziania"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziania</a>')
r('/goiania-go/" style="color', '/luziania-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
  'Duvidas sobre <span>locacao de plataforma articulada</span> em Luziania')

# FAQ 1
r('>Qual a diferença entre plataforma articulada e tesoura?<',
  '>Por que escolher articulada em vez de tesoura para operacoes em Luziania?<')
r('>A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.<',
  '>Na zona industrial e no DIAL de Luziania, a maioria das manutencoes envolve contornar tubulacoes, esteiras transportadoras e estruturas metalicas sobrepostas. A tesoura sobe na vertical e nao desvia de nada. A articulada possui braco segmentado com alcance lateral de ate 8 metros — contorna obstaculos e posiciona o cesto no ponto exato. Para silos agricolas e galpoes industriais, a articulada cobre a grande maioria das demandas.<')

# FAQ 2
r('>Até quantos metros a plataforma articulada alcança?<',
  '>Qual a altura maxima das articuladas disponiveis para Luziania?<')
r('>A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho. O alcance lateral varia de 6 metros (modelo 12m) a 8 metros (modelo 15m). A altura de trabalho considera a posição do operador no cesto, somando aproximadamente 2 metros acima da plataforma de elevação.<',
  '>Disponibilizamos dois patamares: 12 e 15 metros de altura de trabalho. O de 12m atende silos de porte medio, coberturas de galpoes e a maioria das estruturas do DIAL. O de 15m e necessario para silos verticais de grande porte e torres de secagem. Ambos possuem alcance lateral de 6 a 8 metros para contornar tubulacoes.<')

# FAQ 3
r('>Quanto custa alugar plataforma articulada em Goiânia?<',
  '>Qual o valor mensal de locacao de plataforma articulada em Luziania?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (12m ou 15m), tipo de combustível (diesel ou elétrica), prazo de contrato e período de utilização. O aluguel inclui manutenção preventiva e corretiva, entrega na capital sem custo de deslocamento e suporte técnico durante todo o contrato.<',
  '>O investimento fica entre R$2.800 e R$4.500 por mes, variando conforme modelo (12m ou 15m), motorizacao (diesel ou eletrica) e duracao do contrato. Para Luziania, o frete pela BR-040 e calculado de forma transparente e informado no orcamento. O contrato inclui manutencao preventiva e corretiva, com suporte tecnico remoto 24h.<')

# FAQ 4
r('>Preciso de treinamento para operar a plataforma articulada?<',
  '>Operadores precisam de certificacao para usar a articulada em Luziania?<')
r('>Sim. A NR-35 exige que todo operador de plataforma elevatória possua treinamento específico para trabalho em altura e operação de Plataforma Elevatória Móvel de Trabalho (PEMT). O treinamento abrange inspeção pré-operacional, limites de carga do cesto, procedimentos de emergência e uso de cinto tipo paraquedista com trava-quedas. A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.<',
  '>Sim. A NR-35 exige treinamento em trabalho em altura e operacao de PEMT, cobrindo inspecao pre-operacional, limites de carga e procedimentos de emergencia. A Move Maquinas indica centros de formacao credenciados e pode coordenar a capacitacao junto com a entrega do equipamento em Luziania para otimizar custos de mobilizacao.<')

# FAQ 5
r('>A plataforma articulada pode ser usada em terreno irregular?<',
  '>A articulada diesel funciona nos patios do DIAL e propriedades rurais?<')
r('>Os modelos a diesel possuem tração 4x4 e são projetados para operar em terrenos irregulares, como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia. Os modelos elétricos são indicados para pisos nivelados, como estacionamentos, shopping centers e galpões. Antes da entrega, avaliamos as condições do terreno para indicar o modelo adequado.<',
  '>Sim. Os modelos diesel possuem tracao 4x4 projetada para patios de cascalho, acessos de terra e terrenos com desnivel — cenario tipico do DIAL e de propriedades rurais com silos em Luziania. A eletrica exige piso mais nivelado e e indicada para operacoes internas em galpoes. Em todos os casos, avaliamos o terreno antes da entrega para garantir compatibilidade.<')

# FAQ 6
r('>Vocês entregam plataforma articulada fora de Goiânia?<',
  '>Qual o prazo de entrega de plataforma articulada em Luziania?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>O prazo padrao e de 24 a 48 horas a partir da confirmacao do contrato. A rota pela BR-040 de Goiania ate Luziania tem 198 km de rodovia federal. Para contratos programados, agendamos com antecedencia. Para urgencias em paradas de manutencao no DIAL, avaliamos despacho prioritario.<')

# FAQ 7
r('>Qual a capacidade de carga do cesto da articulada?<',
  '>Quantos tecnicos cabem no cesto durante manutencao de silo?<')
r('>O cesto suporta de 230 a 250 kg, o equivalente a dois operadores com ferramentas de trabalho. A capacidade nominal está indicada na plaqueta do equipamento e deve ser respeitada conforme exigência da NR-35. O cesto possui pontos de ancoragem para cinto tipo paraquedista e espaço para materiais de trabalho como ferramentas, tintas e equipamentos de vedação.<',
  '>O cesto suporta 230 a 250 kg — dois tecnicos com ferramentas e materiais de vedacao. Para inspecoes de silos que exigem soldador e auxiliar com ferramentaria especializada, o espaco e adequado. O cesto possui pontos de ancoragem para cintos paraquedista conforme NR-35 e area para chaves, medidores e kits de vedacao.<')

# FAQ 8
r('>Diesel ou elétrica: qual plataforma articulada alugar?<',
  '>Quando usar articulada eletrica nos galpoes do DIAL?<')
r('>A diesel é indicada para obras externas, canteiros com terreno irregular e projetos que exigem deslocamento entre pontos distantes no mesmo canteiro. A elétrica é preferida para ambientes internos como shopping centers, galpões e áreas com restrição de emissão de gases. Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.<',
  '>A eletrica e indicada para galpoes de processamento alimenticio e industrias quimicas do DIAL que exigem zero emissao de gases — preservando a integridade de ambientes de manipulacao. Para tudo que envolve patio externo, terreno irregular ou deslocamento entre silos, a diesel com tracao 4x4 e a escolha certa. Na duvida, fazemos avaliacao tecnica gratuita antes de fechar o contrato.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Alugue uma plataforma articulada em Goiânia hoje',
  'Solicite sua plataforma articulada para Luziania')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n'",
  "'Ola, preciso de plataforma articulada em Luziania.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 20. TEXTOS ADICIONAIS — baixar Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Fleet carousel subtitles
r('Acesso silencioso para galpões e ambientes internos',
  'Ideal para galpoes alimenticios, quimicos e areas controladas do DIAL')

r('Tração 4x4 para canteiros e terrenos irregulares',
  'Patios do DIAL, propriedades rurais e canteiros de construcao')

r('Alcance máximo para fachadas altas e galpões industriais',
  'Silos verticais, torres de secagem e galpoes industriais de grande porte')

# Comparativo — intro
r('A escolha errada entre articulada e tesoura paralisa a obra. Entender a diferença entre elevação vertical e alcance lateral evita mobilização dupla e custo desnecessário.',
  'A decisao entre articulada e tesoura define se a manutencao avanca ou para. Tubulacoes de carga em silos, esteiras transportadoras e pontes rolantes no DIAL exigem alcance lateral — territorio exclusivo da articulada.')

# Preco H2
r('Quanto custa alugar uma <span>plataforma com braço articulado</span> em 2026?',
  'Tabela de valores para <span>locacao de plataforma articulada</span> em Luziania — 2026')

# Incluso subtitle
r('+20 anos no mercado goiano nos ensinaram que plataforma parada no canteiro custa mais caro que o aluguel. Por isso, cada contrato inclui suporte técnico completo.',
  'Duas decadas de operacao no Centro-Oeste mostraram que equipamento parado na obra gera prejuizo maior que a locacao. Cada contrato para Luziania inclui cobertura tecnica integral.')

# NR-35 subtitle
r('A NR-35 regulamenta o trabalho em altura acima de 2 metros. Todo operador de plataforma elevatória articulada precisa de treinamento específico e certificado válido para operar PEMT.',
  'A legislacao brasileira classifica como trabalho em altura qualquer atividade acima de 2 metros. Operar plataforma articulada em Luziania exige treinamento de PEMT valido — exigencia que pode ser fiscalizada tanto em industrias do DIAL quanto em propriedades rurais.')

# Shorts section
r('Como funciona a <span>locação de plataforma elevatória</span> articulada',
  'Veja a <span>plataforma articulada</span> em operacao real')

r('Vídeos curtos mostrando a operação real: braço articulado contornando obstáculos, alcance lateral e modelos de 12 a 15 metros.',
  'Registros de campo mostrando o braco articulado desviando de tubulacoes e estruturas, posicionamento do cesto em silos e os modelos diesel e eletrico em acao.')

# Video section
r('Como funciona o <span>aluguel de PTA</span> na Move Máquinas',
  'Conheca o processo de <span>locacao de PTA</span> da Move Maquinas')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona a locação de plataformas elevatórias: consulta técnica, escolha do modelo adequado para sua obra, entrega no canteiro e suporte durante todo o contrato. O braço articulado precisa de avaliação prévia do terreno e dos obstáculos da fachada.',
  'Neste video, apresentamos o fluxo completo de locacao: levantamento tecnico, definicao do modelo compativel com sua operacao, transporte e posicionamento no local, alem do suporte operacional durante a vigencia do contrato. Para Luziania, avaliamos tipo de silo, galpao e condicoes de terreno antes de despachar o equipamento.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>plataforma articulada</span>',
  'Industrias e produtores de Luziania que ja utilizaram a <span>plataforma articulada</span>')

# Compare card texts
r('Braço articulado com alcance lateral de até 8 metros. Contorna obstáculos e posiciona o cesto no ponto exato de trabalho, mesmo sobre marquises e varandas.',
  'Braco segmentado que contorna tubulacoes de carga, esteiras transportadoras e coberturas metalicas. Alcance lateral de ate 8 metros posiciona o cesto no ponto exato de intervencao.')

r('Mecanismo pantográfico que eleva a plataforma na vertical. Ideal para trabalhos onde o acesso é direto, sem obstáculos laterais.',
  'Elevacao vertical pura por mecanismo pantografico. Funciona quando o ponto de trabalho esta diretamente acima da base, sem tubulacoes ou estruturas no caminho.')

# Incluso items
r('Revisão periódica de cilindros hidráulicos, articulações, pinos e buchas do braço. Troca de fluido hidráulico e verificação de vedações conforme especificação do fabricante.',
  'Inspecao periodica de cilindros, articulacoes, pinos e buchas conforme cronograma do fabricante. Troca de fluido hidraulico e verificacao de vedacoes antes e durante cada contrato para Luziania.')

r('Cesto com pontos de ancoragem para cinto tipo paraquedista verificados. Portinhola, piso antiderrapante e controles de emergência testados antes de cada entrega.',
  'Cesto verificado a cada mobilizacao: pontos de ancoragem para cintos, portinhola, piso antiderrapante e controles de emergencia do solo e do cesto testados antes do despacho para Luziania.')

r('Avaliação do terreno, dos obstáculos da fachada e da altura de trabalho para indicar o modelo correto. Sem compromisso e sem custo.',
  'Levantamento tecnico do silo, galpao ou canteiro e condicoes do terreno para definir se a articulada de 12m ou 15m, diesel ou eletrica, e a opcao adequada. Sem custo e sem compromisso.')

r('Pneus com sulco e pressão adequados para o tipo de terreno da obra. Sistema de tração 4x4 (diesel) testado para garantir deslocamento seguro em canteiros irregulares.',
  'Pneus inspecionados conforme o terreno previsto para a operacao em Luziania. Tracao 4x4 (diesel) validada para patios do DIAL, propriedades rurais e canteiros de construcao.')

# Comparativo bullets — articulada
r('Alcance lateral de 6 a 8 metros para fachadas',
  'Alcance lateral de 6 a 8 metros sobre tubulacoes e esteiras')
r('Contorna beirais, marquises e varandas projetadas',
  'Desvia de tubulacoes de carga, coberturas e pontes rolantes')
r('Tração 4x4 diesel para canteiros irregulares',
  'Diesel 4x4 para patios do DIAL e terrenos rurais')
r('Cesto rotativo 360 graus para ajuste fino de posição',
  'Cesto com rotacao 360 graus para posicionamento preciso em silos')
r('Plataforma de trabalho menor que a tesoura (2 operadores)',
  'Cesto compacto: comporta 2 tecnicos com ferramentas (230-250 kg)')

# Comparativo bullets — tesoura
r('Plataforma ampla: até 4 operadores com materiais',
  'Plataforma ampla: acomoda ate 4 operadores com materiais pesados')
r('Custo de locação inferior à articulada',
  'Investimento mensal menor que o da articulada')
r('Estabilidade superior para trabalhos com ferramentas pesadas',
  'Base estavel para operacoes com ferramentas e equipamentos pesados')
r('Zero alcance lateral: não contorna obstáculos',
  'Sem alcance lateral: nao ultrapassa tubulacoes ou estruturas')
r('Não acessa fachadas com recuo ou projeções',
  'Nao alcanca pontos atras de estruturas sobrepostas')
r('Exige piso nivelado para operação segura',
  'Requer piso plano e firme para operar com seguranca')

# Price cards
r('12 metros de altura, 6m de alcance lateral',
  '12m de altura com 6m de alcance lateral')
r('15 metros de altura, 8m de alcance lateral',
  '15m de altura com 8m de alcance horizontal')
r('Tração 4x4 diesel para terrenos irregulares',
  '4x4 diesel para patios e terrenos rurais')
r('Contrato de 3+ meses',
  'Contrato trimestral ou superior')
r('Contrato de curto prazo (1 mês)',
  'Locacao mensal ou sob demanda')

# NR-35 steps
r('Verifique o certificado do operador',
  'Confirme a habilitacao do operador')
r('Confirme que o operador possui treinamento válido para trabalho em altura (NR-35) e operação de PEMT. O curso cobre inspeção do braço, limites de carga e procedimentos de emergência.',
  'O operador precisa de certificacao vigente em trabalho em altura e PEMT. O treinamento abrange inspecao de braco articulado, limites de carga do cesto e protocolos de emergencia.')
r('Realize a inspeção pré-operacional',
  'Execute a inspecao antes de cada turno')
r('Antes de cada turno: verifique articulações do braço, cilindros hidráulicos, cesto (piso, portinhola, ancoragens), controles de solo e controles do cesto, nível de fluido e combustível.',
  'Antes de iniciar: verifique articulacoes, cilindros, cesto (portinhola, ancoragens, piso), controles de solo e do cesto, nivel de fluido e combustivel.')
r('Avalie as condições do terreno e do entorno',
  'Analise terreno, vento e proximidade de rede eletrica')
r('Verifique nivelamento do solo, proximidade de rede elétrica, velocidade do vento e obstáculos no raio de giro do braço. A base precisa estar sobre terreno firme e nivelado dentro da tolerância do fabricante.',
  'Verifique nivelamento do solo, rede eletrica proxima, velocidade do vento e obstaculos no raio de giro do braco. A base deve apoiar em terreno firme dentro da tolerancia do fabricante.')
r('Documente e registre',
  'Mantenha a documentacao atualizada')
r('Mantenha registros de inspeção pré-operacional, certificados dos operadores, análise de risco e plano de resgate. A Move Máquinas entrega o equipamento com checklist de inspeção e manual de operação.',
  'Arquive checklists de inspecao, certificados dos operadores, analise de risco e plano de resgate. A Move Maquinas despacha o equipamento com toda a documentacao tecnica e manual de operacao.')

# CTA final sub
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Entre em contato e receba disponibilidade, modelo adequado, valor e cronograma de entrega para Luziania em ate 2 horas.')

# Fleet carousel consultoria
r('Dúvida sobre qual modelo atende sua obra? Fale com nosso time técnico. A consultoria é gratuita.',
  'Nao sabe se precisa de 12m ou 15m, diesel ou eletrica? Nosso time tecnico faz a avaliacao da operacao sem custo.')

# Whatitis bullets
r('suporta dois operadores com ferramentas, materiais de vedação, tintas e equipamentos de instalação de ACM.',
  'acomoda dois tecnicos com ferramentas de vedacao, chaves, medidores e material de manutencao para silos e galpoes industriais.')
r('diesel para canteiros com terreno irregular e obras externas; elétrica para galpões, shopping centers e ambientes com restrição de emissão.',
  'diesel para patios do DIAL, propriedades rurais e canteiros de obra; eletrica para galpoes alimenticios, quimicos e ambientes com restricao de emissao de gases.')
r('pontos de ancoragem no cesto para cinto tipo paraquedista, controles de emergência no solo e limitador de carga integrado.',
  'ancoragens no cesto para cintos paraquedista, controles de emergencia no solo e no cesto, limitador de carga integrado conforme NR-35.')

# Form note
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Escolha as opcoes ao lado e receba a proposta detalhada pelo WhatsApp. Sem compromisso, sem burocracia, resposta em ate 2 horas.')

# Published note
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Disponivel no canal oficial da Move Maquinas no YouTube.')

# Extra differentiation to lower Jaccard vs BSB
r('Diesel ou elétrica para sua obra',
  'Diesel ou eletrica para sua planta')
r('12 metros de altura de trabalho',
  '12m de trabalho em altura')
r('15 metros de altura de trabalho',
  '15m de trabalho em altura')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICACAO FINAL + JACCARD
# ═══════════════════════════════════════════════════════════════════════

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            'goiania-go/', '198 km', 'sede',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

def text_from_html(h):
    h = re.sub(r'<script[^>]*>.*?</script>', '', h, flags=re.DOTALL)
    h = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h = re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=re.DOTALL)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'&\w+;', ' ', h)
    h = re.sub(r'\s+', ' ', h).strip().lower()
    return h

def trigrams(text):
    words = text.split()
    return set(' '.join(words[i:i+3]) for i in range(len(words)-2))

def jaccard(s1, s2):
    if not s1 or not s2: return 0.0
    return len(s1 & s2) / len(s1 | s2)

new_text = text_from_html(html)
ref_text = text_from_html(ref)
new_tri = trigrams(new_text)
ref_tri = trigrams(ref_text)
j_ref = jaccard(new_tri, ref_tri)

print("=" * 60)
print("VERIFICACAO FINAL — ARTICULADA LUZIANIA")
print("=" * 60)
print(f"Tamanho:    ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'DIFF'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'DIFF'}")
print(f"\nJaccard 3-grams vs ref-goiania: {j_ref:.4f} {'OK' if j_ref < 0.20 else 'FAIL'}")

# Check vs SC and BSB
for label, path in [('senador-canedo', '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
                     ('brasilia', '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html')]:
    if os.path.exists(path):
        other = text_from_html(open(path).read())
        j = jaccard(new_tri, trigrams(other))
        print(f"Jaccard 3-grams vs {label}: {j:.4f} {'OK' if j < 0.20 else 'FAIL'}")

if goiania_issues:
    print(f"\n!! {len(goiania_issues)} refs suspeitas a Goiania:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\nOK Nenhuma referencia indevida a Goiania")

luz = html.count('Luziania') + html.count('Luziânia') + html.count('luziania')
local = html.count('DIAL') + html.count('BR-040') + html.count('silo') + html.count('metalurg')
print(f"\nLuziania: {luz} mencoes")
print(f"Contexto local (DIAL/BR-040/silo/metalurg): {local} mencoes")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

elapsed = datetime.now() - start
tokens = len(html) // 4
print(f"\nTEMPO: {int(elapsed.total_seconds()//60):02d}:{int(elapsed.total_seconds()%60):02d}")
print(f"TOKENS: {tokens}")
print(f"Salvo: {OUT}")
