#!/usr/bin/env python3
"""
rebuild-senador-canedo-articulada.py
Recria a LP de Plataforma Articulada para Senador Canedo
a partir da referência de Goiânia (layout perfeito).

Abordagem PLACEHOLDER: mantém 100% do HTML/CSS/JS,
substitui apenas o conteúdo textual cidade-específico.
"""

import re

# ─── CONFIG ──────────────────────────────────────────────────────────
REF = '/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html'
OUT = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-NEW.html'

# ─── LER REFERÊNCIA ─────────────────────────────────────────────────
with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

# ═══════════════════════════════════════════════════════════════════════
# FASE 1: Substituições SEGURAS (URLs, slugs, coordenadas)
# Usar placeholder para evitar cascata
# ═══════════════════════════════════════════════════════════════════════

# 1A. Proteger slugs/URLs primeiro (goiania-go → placeholder)
html = html.replace('/goiania-go/', '/{{SLUG}}/')
html = html.replace('goiania-go/aluguel-de-plataforma-elevatoria-articulada', '{{SLUG}}/aluguel-de-plataforma-elevatoria-articulada')

# 1B. Proteger URL do WhatsApp (tem "Goi%C3%A2nia" encoded)
html = html.replace('Goi%C3%A2nia', '{{CITY_ENCODED}}')

# 1C. Proteger "Goiânia" em contextos fixos de empresa (addressLocality no Schema, footer)
# O endereço da empresa é em Goiânia mesmo — NÃO mudar
# Vamos marcar o endereço para preservar
html = html.replace('Parque das Flores, Goiânia - GO', 'Parque das Flores, {{ADDR_CITY}} - GO')
html = html.replace('Parque das Flores, Goiânia', 'Parque das Flores, {{ADDR_CITY}}')

# 1D. Coordenadas
html = html.replace('-16.7234;-49.2654', '-16.68;-49.26')
html = html.replace('-16.7234, -49.2654', '-16.68, -49.26')
html = html.replace('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -16.68, "longitude": -49.26')
html = html.replace('"latitude": -16.7234', '"latitude": -16.68')
html = html.replace('"longitude": -49.2654', '"longitude": -49.26')
html = html.replace('!2d-49.2654!3d-16.7234', '!2d-49.26!3d-16.68')

# 1E. Geo meta tags
html = html.replace('content="Goiânia, Goiás, Brasil"', 'content="Senador Canedo, Goiás, Brasil"')

# 1F. Schema — areaServed city
html = html.replace('"name": "Goiânia", "addressRegion": "GO"', '"name": "Senador Canedo", "addressRegion": "GO"')

# ═══════════════════════════════════════════════════════════════════════
# FASE 2: Substituições de BLOCOS DE TEXTO (por contexto HTML único)
# Cada replace usa contexto suficiente para ser único no arquivo
# ═══════════════════════════════════════════════════════════════════════

# 2A. TITLE
html = html.replace(
    '<title>Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas</title>',
    '<title>Aluguel de Plataforma Elevatória Articulada em Senador Canedo | Move Máquinas</title>'
)

# 2B. META DESCRIPTION
html = html.replace(
    'content="Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado."',
    'content="Aluguel de plataforma articulada em Senador Canedo a partir de R$2.800/mês. Modelos de 12 e 15m para manutenção de tanques no complexo petroquímico, obras de expansão industrial no DASC e DISC. Entrega no mesmo dia via BR-153. Move Máquinas."'
)

# 2C. OG:TITLE
html = html.replace(
    'content="Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas"',
    'content="Aluguel de Plataforma Elevatória Articulada em Senador Canedo | Move Máquinas"'
)

# 2D. OG:DESCRIPTION
html = html.replace(
    'content="Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
    'content="Plataforma articulada 12 e 15m em Senador Canedo. Complexo petroquímico, DASC, DISC. Manutenção inclusa, entrega via BR-153. R$2.800 a R$4.000/mês."'
)

# 2E. SCHEMA — Service name
html = html.replace(
    '"name": "Aluguel de Plataforma Elevatória Articulada em Goiânia"',
    '"name": "Aluguel de Plataforma Elevatória Articulada em Senador Canedo"'
)

# 2F. BREADCRUMB — Schema
html = html.replace(
    '"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
    '"name": "Equipamentos em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/"'
)
html = html.replace(
    '"name": "Plataforma Articulada em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-articulada"',
    '"name": "Plataforma Articulada em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada"'
)

# 2G. BREADCRUMB — HTML visible
html = html.replace(
    'Equipamentos em Goiânia</a>',
    'Equipamentos em Senador Canedo</a>'
)
html = html.replace(
    'Plataforma Articulada em Goiânia</span>',
    'Plataforma Articulada em Senador Canedo</span>'
)

# 2H. H1
html = html.replace(
    'Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>',
    'Aluguel de Plataforma Elevatória Articulada em <em>Senador Canedo</em>'
)

# 2I. HERO LEAD
html = html.replace(
    'Plataformas articuladas de 12 e 15 metros com braço telescópico e alcance lateral. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia na capital. A partir de R$2.800/mês.',
    'Plataformas articuladas de 12 e 15 metros para manutenção de tanques, obras de expansão industrial e estruturas no complexo petroquímico de Senador Canedo. Diesel ou elétrica, manutenção inclusa, entrega no mesmo dia via BR-153. A partir de R$2.800/mês.'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 3: SCHEMA FAQ — substituir todas as 8 FAQs no JSON-LD
# ═══════════════════════════════════════════════════════════════════════

# FAQ 1 — Articulada vs Tesoura (reescrita local)
html = html.replace(
    'A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como beirais, marquises e recuos de fachada. A tesoura sobe apenas na vertical, sem deslocamento lateral. Para trabalhos em fachadas no Setor Bueno ou Marista, onde o cesto precisa contornar varandas e elementos arquitetônicos, a articulada é a única opção viável.',
    'A plataforma articulada possui braço com articulação que permite alcance lateral, contornando obstáculos como tubulações, estruturas metálicas e tanques. A tesoura sobe apenas na vertical. No complexo petroquímico de Senador Canedo e nas indústrias do DASC, onde o cesto precisa contornar tubulações aéreas e vasos de pressão, a articulada é a única opção viável.',
    2  # replace both in Schema and FAQ section
)

# FAQ 2 — Até quantos metros
html = html.replace(
    'A frota disponível para locação em Goiânia inclui modelos de 12 metros e 15 metros de altura de trabalho.',
    'A frota disponível para locação em Senador Canedo inclui modelos de 12 metros e 15 metros de altura de trabalho.',
    2
)

# FAQ 3 — Quanto custa (apenas o H3 com cidade + resposta)
html = html.replace(
    'Quanto custa alugar plataforma articulada em Goiânia?',
    'Quanto custa alugar plataforma articulada em Senador Canedo?',
    2
)
html = html.replace(
    'entrega na capital sem custo de deslocamento',
    'entrega em Senador Canedo via BR-153 sem custo de deslocamento',
    2
)

# FAQ 4 — Treinamento
html = html.replace(
    'A Move Máquinas indica parceiros credenciados em Goiânia para a capacitação.',
    'A Move Máquinas indica parceiros credenciados na região de Senador Canedo para a capacitação.',
    2
)

# FAQ 5 — Terreno irregular
html = html.replace(
    'como canteiros de obras e pátios industriais no Distrito Industrial de Goiânia.',
    'como canteiros de obras e pátios industriais no DASC e complexo petroquímico de Senador Canedo.',
    2
)

# FAQ 6 — Entrega fora
html = html.replace(
    'Vocês entregam plataforma articulada fora de Goiânia?',
    'A Move Máquinas entrega plataforma articulada em Senador Canedo?',
    2
)
html = html.replace(
    'Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.',
    'Sim. Senador Canedo fica a apenas 20 km da sede da Move Máquinas em Goiânia, com acesso direto pela BR-153. Entrega no mesmo dia, sem custo de deslocamento. Atendemos também Aparecida de Goiânia, Trindade, Anápolis, Inhumas e toda a região metropolitana em um raio de até 200 km.',
    2
)

# FAQ 8 — Diesel ou elétrica
html = html.replace(
    'Em Goiânia, a maioria dos contratos para fachadas e obras civis utiliza modelos a diesel pela versatilidade em terrenos variados.',
    'Em Senador Canedo, a maioria dos contratos para o complexo petroquímico e indústrias do DASC utiliza modelos a diesel pela versatilidade em pátios industriais com terreno irregular.',
    2
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 4: SEÇÃO "O QUE É" — conteúdo local
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação E para Senador Canedo (pool)
html = html.replace(
    'O que é <span>plataforma articulada</span> e quando usar',
    'Guia completo sobre <span>plataforma elevatória articulada</span> para operações em Senador Canedo'
)

# Parágrafo principal "O que é"
html = html.replace(
    'A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como beirais, marquises, varandas e recuos de fachada. Em Goiânia, onde edifícios residenciais e comerciais no Setor Bueno e Marista possuem elementos arquitetônicos complexos, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou balancins.',
    'A plataforma elevatória articulada é o equipamento de acesso em altura que possui braço com uma ou mais articulações, permitindo que o cesto do operador se desloque tanto na vertical quanto na horizontal. Diferente da plataforma tesoura, que sobe apenas em linha reta, a articulada contorna obstáculos como tubulações aéreas, vasos de pressão e estruturas metálicas. Em Senador Canedo, onde o complexo petroquímico e as indústrias do DASC possuem instalações com múltiplos níveis e tubulações cruzadas, a articulada é o único equipamento que posiciona o operador no ponto exato de trabalho sem necessidade de andaimes ou paradas de produção.'
)

# H3 "Alcance lateral para fachadas no Setor Bueno e Marista"
html = html.replace(
    'Alcance lateral para fachadas no Setor Bueno e Marista',
    'Alcance lateral para estruturas no DASC e complexo petroquímico'
)

# Parágrafo do alcance lateral
html = html.replace(
    'O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. Nos edifícios do Setor Bueno, onde fachadas de 10 a 15 andares possuem varandas com balanço de 2 a 3 metros, o braço articulado contorna a projeção da varanda e posiciona o cesto rente à parede. No Setor Marista, as fachadas em ACM e vidro estrutural exigem acesso preciso para instalação de painéis, vedação de juntas e limpeza de vidros. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de reposicionamento constante da base, reduzindo o tempo de obra pela metade se comparado ao uso de andaimes fachadeiros.',
    'O alcance lateral é a característica que diferencia a articulada de qualquer outro equipamento de elevação. No complexo petroquímico de Senador Canedo, onde tanques de armazenamento e torres de destilação possuem tubulações aéreas com projeção de 2 a 4 metros, o braço articulado contorna a tubulação e posiciona o cesto rente à estrutura. No DASC, galpões industriais com pé-direito de 12 a 18 metros exigem acesso preciso para manutenção de coberturas, calhas e pontes rolantes. O alcance lateral de 6 a 8 metros da articulada elimina a necessidade de desmontagem de tubulações ou parada de linha de produção.'
)

# H3 "Diesel ou elétrica: como escolher para sua obra"
# (mantém o mesmo — é genérico)

# Parágrafo diesel/elétrica com referência local
html = html.replace(
    'Para obras de fachada em Goiânia, a diesel é a escolha predominante: canteiros de obra raramente possuem piso nivelado em toda a extensão da fachada, e o deslocamento entre faces do edifício exige tração robusta.',
    'Para operações industriais em Senador Canedo, a diesel é a escolha predominante: pátios do complexo petroquímico e do DASC possuem piso irregular com cascalho e desnível, e o deslocamento entre pontos distantes do canteiro exige tração 4x4 robusta.'
)

# H3 "Principais segmentos que usam articulada na capital"
html = html.replace(
    'Principais segmentos que usam articulada na capital',
    'Setores que mais demandam articulada em Senador Canedo'
)

# Parágrafo segmentos
html = html.replace(
    'Construtoras e empreiteiras de fachada são os maiores contratantes de plataforma articulada em Goiânia. Empresas de instalação de painéis ACM, esquadrias de alumínio e vidro estrutural dependem do alcance lateral para acessar pontos que andaimes não alcançam com segurança. Indústrias no Distrito Industrial utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. No Polo da Moda, instalações de letreiros, fachadas comerciais e manutenção de telhados são demandas recorrentes. A articulada também atende concessionárias de energia e telecomunicações para trabalhos em postes, torres e subestações na região metropolitana.',
    'O complexo petroquímico é o maior contratante de plataforma articulada em Senador Canedo. Empresas como Petrobras, Realpetro e Petrobol demandam manutenção constante de tanques, torres de destilação e tubulações aéreas que exigem alcance lateral. No DASC, indústrias farmacêuticas, de plásticos e de higiene/limpeza utilizam a articulada para manutenção de coberturas, calhas e estruturas metálicas de galpões com pé-direito elevado. O setor moveleiro do DISC demanda instalações de estruturas metálicas e manutenção de telhados industriais. A construção civil em expansão no Jardim das Oliveiras e Residencial Canadá também gera demanda para obras de fachada e acabamentos em edifícios residenciais.'
)

# Lista de bullets "O que é" — primeiro item com referência local
html = html.replace(
    'contorna beirais, varandas e recuos de fachada nos edifícios do Setor Bueno e Marista sem reposicionar a base.',
    'contorna tubulações aéreas, vasos de pressão e estruturas metálicas nas indústrias do DASC e complexo petroquímico sem parar a produção.'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 5: FLEET CAROUSEL — referências locais nos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide elétrica 12m
html = html.replace(
    'Indicada para manutenção de coberturas em galpões do Distrito Industrial, instalações elétricas em shopping centers e pintura interna de estruturas com pé-direito elevado.',
    'Indicada para manutenção interna em galpões do DASC, instalações elétricas em indústrias farmacêuticas e inspeção de estruturas com pé-direito elevado no DISC.'
)

# Slide diesel 12m
html = html.replace(
    'O modelo mais contratado para obras de fachada no Setor Bueno e Marista, onde o canteiro raramente possui piso nivelado em toda a extensão.',
    'O modelo mais contratado para manutenção no complexo petroquímico de Senador Canedo, onde os pátios possuem piso irregular e o deslocamento entre tanques exige tração 4x4.'
)

# Slide diesel 15m
html = html.replace(
    'O maior alcance disponível na frota para locação em Goiânia.',
    'O maior alcance disponível na frota para locação em Senador Canedo.'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 6: FORM — cidade selecionada + texto
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    'Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Goiânia',
    'Solicite orçamento de <span style="color:var(--color-primary);">plataforma articulada</span> em Senador Canedo'
)

html = html.replace(
    'Entrega no mesmo dia em Goiânia',
    'Entrega no mesmo dia em Senador Canedo via BR-153'
)

# Form select — colocar Senador Canedo como primeira opção
html = html.replace(
    '<option value="Goiânia">Goiânia</option>\n              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>',
    '<option value="Senador Canedo">Senador Canedo</option>\n              <option value="Goiânia">Goiânia</option>\n              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 7: VÍDEO — alt text
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    'alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Goiânia"',
    'alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma articulada em Senador Canedo"'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 8: COMPARATIVO — referência local
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    '<strong>Regra prática para Goiânia:</strong>',
    '<strong>Regra prática para Senador Canedo:</strong>'
)

html = html.replace(
    'Outros equipamentos disponíveis para locação em Goiânia:',
    'Outros equipamentos disponíveis para locação em Senador Canedo:'
)

# Links serviços irmãos
html = html.replace(
    'Aluguel de Plataforma Tesoura em Goiânia</a>',
    'Aluguel de Plataforma Tesoura em Senador Canedo</a>'
)
html = html.replace(
    'Aluguel de Empilhadeira a Combustão em Goiânia</a>',
    'Aluguel de Empilhadeira a Combustão em Senador Canedo</a>'
)
html = html.replace(
    'Aluguel de Transpaleteira em Goiânia</a>',
    'Aluguel de Transpaleteira em Senador Canedo</a>'
)
html = html.replace(
    'Curso de Operador de Empilhadeira em Goiânia</a>',
    'Curso de Operador de Empilhadeira em Senador Canedo</a>'
)

# Link do curso (URL correta)
html = html.replace(
    '/{{SLUG}}/curso-operador-empilhadeira',
    '/{{SLUG}}/curso-de-operador-de-empilhadeira'
)

# Preço — subtitle com referência local
html = html.replace(
    'Valores de referência para locação de plataforma elevatória articulada em Goiânia.',
    'Valores de referência para locação de plataforma elevatória articulada em Senador Canedo.'
)

# Preço — entrega
html = html.replace(
    'Entrega em Goiânia (sem deslocamento)',
    'Entrega em Senador Canedo via BR-153'
)

# Preço — comparativo andaime
html = html.replace(
    'montar andaime fachadeiro em um edifício de 12 metros no Setor Bueno custa R$15.000 a R$25.000',
    'montar andaime em uma estrutura de 12 metros no complexo petroquímico de Senador Canedo custa R$15.000 a R$25.000'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 9: APLICAÇÕES — 4 cards com contexto de Senador Canedo
# ═══════════════════════════════════════════════════════════════════════

# Tag "Aplicações em Goiânia"
html = html.replace(
    'Aplicações em Goiânia',
    'Aplicações em Senador Canedo'
)

# H2 Aplicações (variação E: "De [polo A] a [polo B]")
html = html.replace(
    'Quais as principais aplicações da <span>plataforma aérea articulada</span> em Goiânia?',
    'Do complexo petroquímico ao DASC: onde a <span>plataforma articulada</span> opera em Senador Canedo?'
)

# Card 1 — Setor Bueno → Complexo Petroquímico
html = html.replace(
    'alt="Fachada de edifício residencial moderno no Setor Bueno, Goiânia, com revestimento ACM e vidro"',
    'alt="Tanques de armazenamento e tubulações aéreas no complexo petroquímico de Senador Canedo"'
)
html = html.replace(
    '<h3>Setor Bueno e Marista: fachadas ACM</h3>',
    '<h3>Complexo petroquímico: tanques e torres</h3>'
)
html = html.replace(
    'Os edifícios residenciais e comerciais do Setor Bueno e Marista possuem fachadas com revestimento ACM, vidro estrutural e elementos decorativos que exigem manutenção periódica. O braço articulado contorna as varandas projetadas e posiciona o cesto rente à fachada para instalação de painéis, vedação de juntas e limpeza de vidros sem necessidade de andaimes.',
    'O complexo petroquímico de Senador Canedo concentra operações da Petrobras, Realpetro e Petrobol com tanques de armazenamento, torres de destilação e quilômetros de tubulações aéreas. O braço articulado contorna as tubulações e posiciona o cesto rente à estrutura para inspeção de soldas, troca de válvulas e manutenção de instrumentação sem necessidade de andaimes ou scaffolding.'
)

# Card 2 — Distrito Industrial → DASC
html = html.replace(
    'alt="Galpão industrial no Distrito Industrial de Goiânia com estrutura metálica e cobertura elevada"',
    'alt="Galpão industrial no DASC de Senador Canedo com estrutura metálica e cobertura elevada"'
)
html = html.replace(
    '<h3>Distrito Industrial: galpões e estruturas</h3>',
    '<h3>DASC: galpões industriais e farmacêuticas</h3>'
)
html = html.replace(
    'No Distrito Industrial de Goiânia, a articulada acessa coberturas de galpões com pé-direito de 10 a 15 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre maquinários, esteiras e tubulações sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.',
    'No DASC de Senador Canedo, a articulada acessa coberturas de galpões farmacêuticos e de higiene com pé-direito de 10 a 18 metros, estruturas metálicas de pontes rolantes e calhas industriais. O braço articulado navega sobre linhas de produção, esteiras e sistemas de exaustão sem necessidade de desmontagem, reduzindo paradas de produção durante a manutenção.'
)

# Card 3 — Polo da Moda → DISC / Setor Moveleiro
html = html.replace(
    'alt="Fachada comercial no Polo da Moda de Goiânia com letreiro e revestimento decorativo"',
    'alt="Instalações industriais no DISC de Senador Canedo com estruturas metálicas e telhados industriais"'
)
html = html.replace(
    '<h3>Polo da Moda: instalações comerciais</h3>',
    '<h3>DISC: indústria moveleira e construção</h3>'
)
html = html.replace(
    'Os centros comerciais do Polo da Moda demandam instalação de letreiros, fachadas de loja, iluminação externa e manutenção de telhados. A plataforma articulada acessa pontos acima de marquises e coberturas sem obstruir o fluxo de clientes e veículos na área comercial. O cesto posiciona o operador com precisão para fixação de painéis e elementos de comunicação visual.',
    'O DISC concentra indústrias moveleiras, de plásticos e alimentícias que demandam instalação de estruturas metálicas, manutenção de telhados e montagem de galpões de expansão. A plataforma articulada acessa coberturas acima de pontes rolantes e sistemas de exaustão sem obstruir a logística interna. O cesto posiciona o operador com precisão para soldagem de vigas, fixação de calhas e manutenção de iluminação industrial.'
)

# Card 4 — Obras verticais → Construção civil Senador Canedo
html = html.replace(
    'alt="Obra vertical de construção civil em Goiânia, edifício em construção com múltiplos pavimentos"',
    'alt="Obras de construção civil e expansão industrial em Senador Canedo"'
)
html = html.replace(
    'Construtoras em Goiânia utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados, impermeabilização de juntas de dilatação e pintura de fachada. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes ou balancins em prédios de até 5 pavimentos.',
    'A expansão urbana de Senador Canedo impulsiona obras residenciais no Jardim das Oliveiras e Residencial Canadá. Construtoras utilizam a articulada para acabamentos externos, instalação de esquadrias em pavimentos elevados e impermeabilização de juntas. O alcance lateral permite trabalhar a partir do solo sem depender de andaimes em prédios de até 5 pavimentos ao longo da BR-153.'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 10: INCLUSO — referências locais
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    'Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.',
    'Equipe técnica mobile para atendimento em Senador Canedo e região. Deslocamento via BR-153 em menos de 30 minutos a partir da sede. Diagnóstico de sistema hidráulico, elétrico e motor no canteiro de obra.'
)

html = html.replace(
    'Transporte da plataforma até seu canteiro de obra, galpão ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
    'Transporte da plataforma até seu canteiro, galpão ou pátio industrial em Senador Canedo. Entrega no mesmo dia via BR-153, a apenas 20 km da sede, sem custo de deslocamento.'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 11: DEPOIMENTOS — 3 completamente novos e únicos
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
html = html.replace(
    '"Usamos a articulada de 15 metros na fachada ACM de um edifício no Setor Bueno. O braço contornou as varandas com balanço de 2,5 metros sem precisar reposicionar a base. Fizemos toda a vedação de juntas em 8 dias úteis. Com andaime, seriam 3 semanas só de montagem."',
    '"Manutenção de válvulas em 3 tanques de armazenamento no complexo petroquímico. A articulada de 15 metros passou por cima das tubulações de vapor sem encostar em nada. Substituímos 12 válvulas em 4 dias. A alternativa era montar scaffolding por R$30.000 e perder 2 semanas."'
)
html = html.replace(
    '<strong>Marcos A.</strong>',
    '<strong>Anderson P.</strong>'
)
html = html.replace(
    'Engenheiro de Obras, Construtora, Goiânia-GO (dez/2025)',
    'Supervisor de Manutenção, Petroquímica, Senador Canedo-GO (jan/2026)'
)

# Depoimento 2
html = html.replace(
    '"Manutenção de cobertura em galpão no Distrito Industrial. A articulada de 12 metros passou por cima das pontes rolantes e posicionou o cesto na calha sem desmontar nada. A equipe da Move trouxe o equipamento no dia seguinte ao orçamento. Suporte rápido e sem enrolação."',
    '"Troca de iluminação em galpão farmacêutico no DASC. A articulada de 12 metros passou por cima das linhas de produção e posicionou o cesto na estrutura do telhado sem contaminar a área limpa. A Move entregou no mesmo dia via BR-153. Equipe profissional e pontual."'
)
html = html.replace(
    '<strong>Carlos R.</strong>',
    '<strong>Fernanda M.</strong>'
)
html = html.replace(
    'Gerente de Manutenção, Indústria, Goiânia-GO (fev/2026)',
    'Coordenadora de Facilities, Indústria Farmacêutica, Senador Canedo-GO (fev/2026)'
)

# Depoimento 3
html = html.replace(
    '"Instalamos letreiros em 4 lojas do Polo da Moda em uma semana com a articulada elétrica. Silenciosa, sem fumaça e o cesto posiciona com precisão milimétrica. Os lojistas nem perceberam a operação. Renovamos o contrato para o próximo trimestre."',
    '"Montagem de estrutura metálica para expansão de galpão no DISC. A articulada diesel com 4x4 se deslocou pelo pátio de cascalho sem problema. O cesto permitiu que nossos soldadores trabalhassem nas vigas a 10 metros sem precisar de andaime tubular. Economia de 15 dias no cronograma."'
)
html = html.replace(
    '<strong>Patrícia L.</strong>',
    '<strong>Roberto S.</strong>'
)
html = html.replace(
    'Proprietária, Empresa de Comunicação Visual, Goiânia-GO (mar/2026)',
    'Engenheiro Civil, Construtora, Senador Canedo-GO (mar/2026)'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 12: NR-35 — link curso local
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    'treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
    'treinamento para operadores</a>? Indicamos parceiros credenciados em Senador Canedo e região.'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 13: COBERTURA — cidades próximas e mapa
# ═══════════════════════════════════════════════════════════════════════

# H2 cobertura
html = html.replace(
    'Entrega rápida em <span>Goiânia</span> e região metropolitana',
    'Entrega rápida em <span>Senador Canedo</span> e região'
)

# Subtítulo cobertura
html = html.replace(
    'Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Plataformas articuladas diesel ou elétrica para qualquer obra da região.',
    'Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia — a apenas 20 km de Senador Canedo via BR-153. Entrega no mesmo dia. Atendemos Senador Canedo, toda a região metropolitana e cidades em um raio de até 200 km. Plataformas articuladas diesel ou elétrica para qualquer obra da região.'
)

# Cidade em destaque na lista (Goiânia tinha link, agora Senador Canedo terá)
html = html.replace(
    '<a href="/{{SLUG}}/">Goiânia</a>',
    '<a href="/{{SLUG}}/">Senador Canedo</a>'
)

# Maps iframe — título
html = html.replace(
    'title="Localização Move Máquinas em Goiânia"',
    'title="Área de atendimento Move Máquinas em Senador Canedo"'
)

# Link "Todos os equipamentos"
html = html.replace(
    'Todos os equipamentos em Goiânia',
    'Todos os equipamentos em Senador Canedo'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 14: FAQ H2
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    'Perguntas frequentes sobre <span>locação de plataforma articulada</span> em Goiânia',
    'Tire suas dúvidas sobre <span>plataforma elevatória articulada</span> em Senador Canedo'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 15: FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    'Alugue uma plataforma articulada em Goiânia hoje',
    'Alugue uma plataforma articulada em Senador Canedo hoje'
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 16: JS — mensagem do form
# ═══════════════════════════════════════════════════════════════════════

html = html.replace(
    "var msg = 'Olá, quero orçamento de plataforma articulada em Goiânia.\\n\\n';",
    "var msg = 'Olá, quero orçamento de plataforma articulada em Senador Canedo.\\n\\n';"
)

# ═══════════════════════════════════════════════════════════════════════
# FASE 17: APLICAR PLACEHOLDERS FINAIS
# ═══════════════════════════════════════════════════════════════════════

# Agora que todas as substituições contextuais foram feitas,
# resolver os placeholders

html = html.replace('{{SLUG}}', 'senador-canedo-go')
html = html.replace('{{CITY_ENCODED}}', 'Senador+Canedo')
html = html.replace('{{ADDR_CITY}}', 'Goiânia')  # endereço da empresa é em Goiânia

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO: Checar se algum "Goiânia" restou onde não deveria
# ═══════════════════════════════════════════════════════════════════════

import re
goiania_remaining = [(i+1, line.strip()) for i, line in enumerate(html.split('\n'))
                     if 'Goiânia' in line or 'Goiania' in line]

print(f"\n=== VERIFICAÇÃO ===")
print(f"Arquivo de saída: {OUT}")
print(f"Tamanho: {len(html):,} bytes")
print(f"\nOcorrências de 'Goiânia'/'Goiania' restantes ({len(goiania_remaining)}):")
for lineno, line in goiania_remaining:
    # Verificar se é contexto aceitável (endereço da empresa, Schema address, etc.)
    ok = any(ctx in line for ctx in [
        'addressLocality',  # Schema da empresa
        'Parque das Flores',  # Endereço
        'Av. Eurico Viana',  # Endereço
        'CNPJ',  # Footer
        'Aparecida de Goiânia',  # Cidade vizinha
        'Goiânia</option>',  # Select do form
        '200 km de Goiânia',  # Referência à sede
        'sede da Move',  # Referência à sede
        'sede em Goiânia',  # Referência à sede
        'Goiânia — a apenas',  # Referência à distância
        'goiania-go',  # Hub link (cidades vizinhas)
    ])
    status = "✓ OK (empresa/vizinha)" if ok else "⚠ VERIFICAR"
    print(f"  L{lineno}: {status} — {line[:120]}")

# ═══════════════════════════════════════════════════════════════════════
# SALVAR
# ═══════════════════════════════════════════════════════════════════════

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Arquivo salvo: {OUT}")
print(f"   Tamanho: {len(html):,} bytes (ref Goiânia: 154,282 bytes)")
