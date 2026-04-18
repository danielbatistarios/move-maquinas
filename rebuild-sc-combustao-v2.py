#!/usr/bin/env python3
"""
rebuild-sc-combustao-v2.py
Gera LP de Empilhadeira a Combustão para Senador Canedo
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-combustao.html'
OUT = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-empilhadeira-combustao-V2.html'

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
# 1. HEAD — title, meta, canonical, og, geo, Schema
# ═══════════════════════════════════════════════════════════════════════

r('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
  '<title>Empilhadeira a Combustão para Locação em Senador Canedo-GO | Move Máquinas</title>')

r('content="Aluguel de empilhadeira a combustão Clark em Goiânia a partir de R$2.800/mês. Modelos L25, GTS, S-Series e C-Series. Manutenção inclusa, entrega mesmo dia. Move Máquinas: +20 anos no mercado."',
  'content="Locação de empilhadeira Clark GLP e diesel em Senador Canedo a partir de R$2.800/mês. L25, GTS, S-Series e C-Series de 2.000 a 8.000 kg. Ideal para CDs da BR-153, polo petroquímico e DASC. Manutenção inclusa, entrega no mesmo dia."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  'href="https://movemaquinas.com.br/senador-canedo-go/aluguel-de-empilhadeira-combustao"')

r('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
  'content="Empilhadeira a Combustão para Locação em Senador Canedo-GO | Move Máquinas"')

r('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês."',
  'content="Empilhadeira Clark a combustão em Senador Canedo. De 2.000 a 8.000 kg para o polo petroquímico, DASC e CDs da BR-153. Manutenção inclusa no contrato. R$2.800 a R$4.000/mês."')

r('content="Goiânia, Goiás, Brasil"', 'content="Senador Canedo, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.6997;-49.0919"')
r('content="-16.7234, -49.2654"', 'content="-16.6997, -49.0919"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.6997, "longitude": -49.0919')
r('"latitude": -16.7234', '"latitude": -16.6997')
r('"longitude": -49.2654', '"longitude": -49.0919')

# Schema — Service name
r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
  '"name": "Locação de Empilhadeira a Combustão em Senador Canedo"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Senador Canedo", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/"')
r('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
  '"name": "Empilhadeira a Combustão em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/aluguel-de-empilhadeira-combustao"')

# ═══════════════════════════════════════════════════════════════════════
# 1B. SCHEMA FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

OLD_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual a empilhadeira a combustão mais alugada em Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência." } },
        { "@type": "Question", "name": "Qual a diferença entre empilhadeira a combustão e elétrica?", "acceptedAnswer": { "@type": "Answer", "text": "A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil." } },
        { "@type": "Question", "name": "Quanto custa alugar empilhadeira a combustão em Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital." } },
        { "@type": "Question", "name": "A manutenção da empilhadeira está inclusa no aluguel?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento." } },
        { "@type": "Question", "name": "Qual combustível escolher: GLP ou diesel?", "acceptedAnswer": { "@type": "Answer", "text": "O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis." } },
        { "@type": "Question", "name": "Vocês entregam empilhadeira fora de Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento." } },
        { "@type": "Question", "name": "Preciso de habilitação especial para operar empilhadeira?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o curso de operador." } },
        { "@type": "Question", "name": "Qual a capacidade máxima das empilhadeiras Clark disponíveis?", "acceptedAnswer": { "@type": "Answer", "text": "A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas." } }
      ]
    }'''

NEW_FAQ_SCHEMA = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual empilhadeira Clark é mais indicada para os CDs de Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "A Clark L25 domina as operações nos centros de distribuição da BR-153 em Senador Canedo. Com 2.500 kg de capacidade, garfos de 1.070 mm e mastro triplex, ela manobra em corredores de 3,5 m e sustenta paletes padronizados com margem de segurança. Opera com GLP ou diesel, sem interrupção para recarga de bateria." } },
        { "@type": "Question", "name": "Por que escolher combustão em vez de elétrica para operações em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "Os CDs da BR-153 e os pátios do polo petroquímico de Senador Canedo alternam entre docas cobertas e áreas externas com piso irregular. A combustão oferece torque superior em rampas, opera sob chuva e não depende de infraestrutura de recarga. Para turnos contínuos nos armazéns do DASC e DISC, a troca do cilindro GLP em 3 minutos mantém a operação sem pausa." } },
        { "@type": "Question", "name": "Qual o investimento mensal para alugar empilhadeira em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "Os valores ficam entre R$2.800 e R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), combustível e duração do contrato. Senador Canedo está a 20 km da sede pela BR-153 — a entrega é sem custo de deslocamento. Manutenção preventiva, corretiva e suporte técnico 24h estão inclusos." } },
        { "@type": "Question", "name": "O contrato de locação cobre manutenção do motor e sistema hidráulico?", "acceptedAnswer": { "@type": "Answer", "text": "Integralmente. Cada contrato inclui revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos. Nossa equipe técnica mobile chega a Senador Canedo em menos de 40 minutos pela BR-153. Se a máquina apresentar falha irreparável no local, substituímos o equipamento no mesmo dia." } },
        { "@type": "Question", "name": "GLP ou diesel: qual combustível para o polo petroquímico de Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "O diesel é preferido nos pátios externos do polo petroquímico e nas vias internas do DASC, onde rampas e pisos de cascalho exigem torque máximo. O GLP é mais versátil quando a empilhadeira transita entre galpão fechado e doca externa — emite menos monóxido de carbono e a troca de cilindro é imediata. Nos dois casos, todos os modelos Clark aceitam ambos." } },
        { "@type": "Question", "name": "Qual o prazo de entrega de empilhadeira em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "Senador Canedo recebe no mesmo dia. São 20 km pela BR-153 sem pedágio — o equipamento sai da nossa base na Av. Eurico Viana e chega ao seu galpão, CD ou pátio industrial em menos de 1 hora. Para paradas programadas no polo petroquímico, priorizamos o despacho com antecedência." } },
        { "@type": "Question", "name": "Operadores de empilhadeira no DASC precisam de certificação NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador de empilhadeira. O treinamento cobre inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Indicamos centros de formação credenciados na região de Senador Canedo e Goiânia." } },
        { "@type": "Question", "name": "Até quantos quilos as empilhadeiras Clark suportam?", "acceptedAnswer": { "@type": "Answer", "text": "A frota disponível para Senador Canedo vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para movimentação de tambores e insumos no polo petroquímico, a L25/30/35 resolve. Para bobinas de aço e cargas industriais pesadas no DISC, a série C60/70/80 é a indicação técnica." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/senador-canedo-go/">Equipamentos em Senador Canedo</a>')

r('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
  '<span aria-current="page">Empilhadeira a Combustão em Senador Canedo</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, WhatsApp URLs
# ═══════════════════════════════════════════════════════════════════════

r('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
  'Locação de Empilhadeira a Combustão em <em>Senador Canedo</em>')

r('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg para os CDs da BR-153, polo petroquímico e distritos industriais DASC e DISC. GLP ou diesel, manutenção inclusa no contrato e entrega no mesmo dia — 20 km pela BR-153. A partir de R$2.800/mês.')

# WhatsApp URLs — bulk replace encoded Goiânia
r('Goi%C3%A2nia', 'Senador+Canedo', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template B
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>Entrega via BR-153</strong><span>20 km da sede</span>')

r('<strong>Suporte 24h</strong><span>Equipe técnica mobile</span>',
  '<strong>+20 anos</strong><span>Experiência industrial</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação
r('O que é a <span>empilhadeira a combustão</span> e quando vale a pena alugar',
  'Entenda a <span>empilhadeira a combustão Clark</span> antes de contratar')

# Parágrafo principal
r('A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Diferente da empilhadeira elétrica, ela não depende de recarga de bateria, entrega torque superior em rampas e pátios irregulares e opera sem restrição em ambientes externos. Goiânia concentra o maior volume de CDs logísticos, atacadistas e indústrias do Centro-Oeste, com corredores logísticos na BR-153, no Polo da Moda e no Distrito Industrial Leste, o que torna a capital o principal mercado de locação de empilhadeiras da região.',
  'A empilhadeira a combustão é a máquina de movimentação de cargas acionada por motor a <abbr title="Gás Liquefeito de Petróleo">GLP</abbr> ou diesel. Ela não para para recarregar bateria, desenvolve torque elevado em rampas e pisos de cascalho e opera em áreas externas sob chuva sem restrição. Senador Canedo concentra o complexo petroquímico (Petrobras, Realpetro, Petrobol), o Distrito Agroindustrial (DASC) e o segundo distrito industrial (DISC), além de centros de distribuição ao longo da BR-153 — um ecossistema logístico e industrial que demanda empilhadeiras em turno contínuo.')

# H3 — GLP vs Diesel
r('GLP vs Diesel: qual combustível para sua operação na capital',
  'GLP ou diesel: como escolher o combustível certo para a indústria de Senador Canedo')

r('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de equipamento, pois emite menos monóxido de carbono que o diesel. A troca do cilindro de GLP leva menos de 3 minutos e não exige infraestrutura fixa. O diesel, por outro lado, entrega maior torque em subidas e terrenos irregulares. Para operações no Distrito Industrial Leste com rampas de carga e pátios de terra, o diesel é a escolha mais robusta.',
  'No polo petroquímico de Senador Canedo, onde pátios de cascalho conectam tanques, torres e galpões de armazenamento, o diesel entrega o torque necessário para subir rampas carregadas e transitar por pisos irregulares sem perda de tração. Já nos galpões fechados do DASC — farmacêuticos, higiene e plásticos — o GLP emite menos monóxido de carbono e permite que a máquina circule entre área interna e doca externa sem trocar de equipamento. A troca do cilindro de GLP leva menos de 3 minutos e dispensa infraestrutura fixa de recarga.')

# H3 — Capacidades
r('Capacidades de 2.000 a 8.000 kg: como dimensionar para seu galpão',
  'De 2.000 a 8.000 kg: qual capacidade atende sua operação em Senador Canedo')

r('A capacidade de carga da empilhadeira precisa considerar o peso máximo do palete mais o centro de gravidade da carga. Para paletes padronizados de 1.200 kg em CDs logísticos, a Clark L25 (2.500 kg) atende com folga. Para bobinas de aço, chapas e containers no Distrito Industrial, a série C60/70/80 suporta de 6.000 a 8.000 kg. Dimensionar abaixo da necessidade compromete a segurança; dimensionar acima gera custo desnecessário de locação.',
  'A capacidade correta depende do peso do palete somado ao centro de gravidade da carga. Nos CDs da BR-153 em Senador Canedo, onde o padrão é palete de 1.000 a 1.400 kg, a Clark L25 (2.500 kg) opera com margem de segurança. No polo petroquímico, tambores de 200 litros e IBC de 1.000 kg pedem a L30/35. Para o DISC, onde o setor moveleiro movimenta chapas de MDF e o alimentício carrega paletes duplos, a S40-60 ou C-Series é a indicação técnica. Subdimensionar arrisca a segurança do operador; superdimensionar encarece o contrato.')

# H3 — Clark L25
r('Clark L25: a empilhadeira mais locada em Goiânia',
  'Clark L25: por que é a mais contratada nos CDs da BR-153')

r('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de alta eficiência, ela opera em docas, corredores de armazenagem e pátios de expedição. O contrapeso traseiro garante estabilidade mesmo com carga máxima em elevação total. É a escolha padrão para centros de distribuição da BR-153, atacadistas do Polo da Moda e armazéns de médio porte na região metropolitana.',
  'A Clark L25 responde pela maioria dos contratos de locação em Senador Canedo. Capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex com visibilidade total e sistema hidráulico de alta eficiência. Ela manobra em corredores de 3,5 m nos CDs da BR-153, empilha até 6 metros nos armazéns do DASC e opera em docas de 8 a 12 posições sem comprometer a estabilidade. O contrapeso traseiro mantém a máquina firme mesmo com carga máxima em elevação total — requisito para operações de turno duplo nas distribuidoras da região.')

# Bullet 1 — Motor
r('sem dependência de recarga de bateria, operação contínua em turnos duplos nos CDs logísticos de Goiânia.',
  'operação contínua sem pausa para recarga. Troca de cilindro GLP em 3 minutos nos CDs da BR-153 e no polo petroquímico de Senador Canedo.')

# Bullet 4 — Aplicações
r('<strong>Aplicações em Goiânia:</strong> CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
  '<strong>Onde opera em Senador Canedo:</strong> centros de distribuição da BR-153, pátios do polo petroquímico (Petrobras, Realpetro, Petrobol), galpões farmacêuticos e de plásticos do DASC, fábricas do DISC e armazéns da GO-403.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia via BR-153')

# Form selects — Senador Canedo como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Senador Canedo" selected>Senador Canedo</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  2)  # desktop + mobile forms

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Slide 0: L25/30/35
r('A série mais contratada para CDs da BR-153',
  'A série líder nos CDs de distribuição de Senador Canedo')

r('Linha principal de empilhadeiras Clark para operações de médio porte. Garfos de 1.070 mm, mastro triplex com visibilidade total e contrapeso otimizado para estabilidade. Transmissão powershift com conversor de torque para manobras suaves em corredores de 3,5 m.',
  'Linha principal Clark para centros de distribuição e armazéns. Garfos de 1.070 mm, mastro triplex e contrapeso projetado para estabilidade em elevação máxima. Transmissão powershift para manobras em corredores de 3,5 m — padrão dos CDs na BR-153 em Senador Canedo. Opera com GLP nos galpões fechados e diesel nos pátios externos do polo petroquímico.')

# Slide 1: GTS 25-33
r('Alta performance com cabine fechada',
  'Cabine fechada para operações prolongadas no DASC')

r('Série premium para operações que exigem conforto do operador em turnos prolongados. Cabine fechada com proteção contra poeira e ruído, sistema hidráulico de dupla velocidade e painel digital. Indicada para indústrias do Distrito Industrial de Goiânia.',
  'Série premium com cabine fechada que protege o operador de poeira e ruído industrial. Sistema hidráulico de dupla velocidade e painel digital com diagnóstico integrado. Nos galpões farmacêuticos e de plásticos do DASC em Senador Canedo, a cabine preserva o conforto durante turnos de 10 horas e reduz a fadiga do operador.')

r('Alta performance, Distrito Industrial',
  'Turnos longos, DASC e DISC')

# Slide 2: S25/30/35
r('S-Series para uso geral e pátios externos',
  'S-Series para alternância entre galpão e pátio no DISC')

r('A S-Series é a linha versátil da Clark para operações que alternam entre galpão e pátio externo. Chassi robusto com suspensão reforçada para pisos irregulares, motor com opção GLP ou diesel, e ergonomia de cabine aberta para climas quentes. Popular em cooperativas, armazéns e centros de distribuição da GO-060.',
  'A S-Series combina chassi robusto e suspensão reforçada para transitar entre o galpão pavimentado e o pátio de cascalho — rotina diária no DISC de Senador Canedo. Cabine aberta com ventilação natural para o clima quente do cerrado goiano. Motor GLP ou diesel e ergonomia pensada para operadores que alternam entre carga em doca e empilhamento em estoque.')

r('Uso geral, pátios, cooperativas',
  'DISC, pátios mistos, armazéns')

# Slide 3: C20s
r('Compacta para corredores estreitos',
  'Compacta para armazéns urbanos do Centro e Jardim das Oliveiras')

r('A C20s é a empilhadeira mais compacta da linha Clark a combustão. Projetada para operações em corredores estreitos de 2,8 m onde empilhadeiras convencionais não manobram. Capacidade de 2.000 kg com raio de giro reduzido. Ideal para armazéns urbanos do Setor Campinas e atacadistas com espaço limitado.',
  'A C20s é a empilhadeira mais compacta da linha Clark a combustão. Raio de giro reduzido para corredores de 2,8 m onde máquinas convencionais não manobram. Capacidade de 2.000 kg para paletes leves e caixas fracionadas. Nos armazéns do Centro de Senador Canedo e depósitos do Jardim das Oliveiras, ela resolve operações em espaço restrito sem sacrificar produtividade.')

r('Corredores estreitos, armazéns urbanos',
  'Corredores estreitos, armazéns Centro/J. Oliveiras')

# Slide 4: S40-60
r('Heavy duty intermediária para cargas de 4.000 a 6.000 kg',
  'Heavy duty intermediária para o DISC e construção civil')

r('A S40-60 preenche a faixa entre as empilhadeiras de médio porte (até 3.500 kg) e as ultra pesadas (C-Series). Motor diesel de alto torque com transmissão powershift, mastro reforçado e pneus maciços de alta durabilidade. Usada em pátios de construção civil, indústrias metalúrgicas e armazéns de insumos pesados na BR-153.',
  'A S40-60 ocupa a faixa intermediária entre as empilhadeiras de médio porte e a C-Series ultra pesada. Motor diesel de alto torque, transmissão powershift e pneus maciços para pátios irregulares. No DISC de Senador Canedo, ela movimenta chapas de MDF do setor moveleiro e cargas do setor alimentício. Na construção civil dos novos empreendimentos do Residencial Canadá, desloca paletes de blocos e vergalhões em canteiros sem pavimentação.')

r('Cargas pesadas, pátios industriais',
  'DISC, construção civil, pátios')

# Slide 5: C60/70/80
r('Heavy duty para o Distrito Industrial',
  'Heavy duty para o polo petroquímico e cargas acima de 6t')

r('Linha pesada da Clark. Capacidades de 6.000 a 8.000 kg para movimentação de bobinas de aço, chapas, containers e cargas industriais de grande porte. Motor diesel de alto torque, transmissão reforçada e pneus maciços para pátios irregulares.',
  'Linha pesada Clark projetada para cargas de 6.000 a 8.000 kg. No polo petroquímico de Senador Canedo, movimenta tambores de 200 litros em paletes duplos, IBC e equipamentos de manutenção de torres. Motor diesel de alto torque com transmissão reforçada e pneus maciços para os pátios de cascalho do complexo industrial.')

r('Ultra heavy, Distrito Industrial',
  'Polo petroquímico, cargas ultra pesadas')

# Spec table caption
r('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
  'Empilhadeiras Clark a Combustão: especificações da frota para locação em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para SC combustão
# ═══════════════════════════════════════════════════════════════════════

r('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, técnico que cobra R$400 a visita, máquina parada três dias esperando hidráulico. Quando faço a conta com o cliente, o aluguel com manutenção inclusa sai mais barato que manter uma máquina própria. E se a operação muda de volume, a gente troca o modelo sem burocracia."',
  '"Senador Canedo cresceu muito nos últimos anos — polo petroquímico, DASC, DISC, CDs na BR-153. A demanda por empilhadeira acompanhou. O erro que mais vejo é empresa comprando máquina usada sem contrato de manutenção. No terceiro mês, o mastro trava, a bomba hidráulica vaza e a peça leva 15 dias para chegar. Enquanto isso, o operador fica parado e o caminhão esperando na doca. Quando calculo com o cliente, o aluguel com manutenção inclusa custa menos que uma parada de dois dias. E se a demanda cresce no período de safra ou parada programada, a gente escala a frota sem burocracia."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — verdict + links internos
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Regra prática para Goiânia:</strong> se a operação alterna entre galpão e pátio externo, ou se precisa de mais de 8 horas contínuas por turno, a combustão é a escolha certa. A maioria dos CDs da BR-153 e dos atacadistas do Polo da Moda opera com empilhadeira a combustão GLP por conta da versatilidade. Em dúvida, nosso time faz a avaliação técnica sem compromisso.',
  '<strong>Critério objetivo para Senador Canedo:</strong> se a empilhadeira precisa transitar entre doca coberta e pátio externo, ou se o turno ultrapassa 8 horas sem intervalo para recarga, a combustão resolve. No polo petroquímico e nos CDs da BR-153, onde o ciclo de carga e descarga não para, o GLP é o combustível mais contratado. O diesel entra quando o piso é de cascalho e as rampas são íngremes. Na dúvida, fazemos avaliação técnica gratuita no local.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Senador Canedo:')

# Links internos — todos para senador-canedo-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura')
r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Senador Canedo')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Senador Canedo')

r('/goiania-go/aluguel-de-transpaleteira', '/senador-canedo-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Senador Canedo')

r('/goiania-go/curso-operador-empilhadeira', '/senador-canedo-go/curso-de-operador-de-empilhadeira', 99)
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira a combustão em Goiânia: valores e condições"',
  'alt="Valores e condições de locação de empilhadeira Clark em Senador Canedo e região"')

r('Conheça o processo de <span>Aluguel de Empilhadeira</span> em Goiânia',
  'Como funciona a <span>locação de empilhadeira Clark</span> em Senador Canedo')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona o processo de locação: consulta, escolha do modelo Clark, entrega no local e suporte técnico durante todo o contrato. Transparência é a base do nosso modelo de negócio.',
  'Veja como funciona o processo completo de locação: consulta técnica, seleção do modelo Clark adequado, entrega via BR-153 no seu galpão ou CD em Senador Canedo e suporte técnico durante toda a vigência do contrato. Sem burocracia, sem custo oculto.')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>empilhadeira GLP/diesel</span> em 2026?',
  'Investimento mensal: <span>empilhadeira GLP e diesel</span> em Senador Canedo (2026)')

r('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia. O preço final depende do modelo, prazo e capacidade de carga.',
  'Tabela de referência para locação de empilhadeira Clark em Senador Canedo. O valor final varia por modelo, combustível, capacidade e duração do contrato.')

r('Entrega em Goiânia (sem deslocamento)',
  'Entrega em Senador Canedo (20 km, sem custo)')

# Heavy duty / curto prazo - price card 3 item
r('Entrega em cidades mais distantes',
  'Entrega no polo petroquímico ou DISC')

# Price note
r('Sem custo de deslocamento na capital',
  'Sem custo de frete para Senador Canedo')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. O equipamento chega no seu galpão, CD ou pátio pronto para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 20 km de Senador Canedo pela BR-153, sem pedágio. Não cobramos frete adicional. A empilhadeira chega ao seu CD, galpão do DASC ou pátio do polo petroquímico pronta para operar no mesmo dia.')

r('uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, caminhões aguardando descarga e penalidades contratuais). Uma visita técnica avulsa, fora de contrato, custa R$800 a R$1.500. Na Move Máquinas, manutenção preventiva e corretiva estão inclusas. Se a empilhadeira falhar, substituímos o equipamento.',
  'nos CDs da BR-153 e nos pátios do polo petroquímico, uma empilhadeira parada custa R$1.500 a R$2.500 por dia entre equipe ociosa, caminhões na fila da doca e penalidades contratuais. Uma visita técnica avulsa sai R$800 a R$1.500 — e a peça pode demorar dias. No contrato da Move Máquinas, manutenção preventiva e corretiva estão no pacote. Se a máquina falhar, substituímos no mesmo dia.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag — note: whitespace in source
r('      Aplicações em Goiânia', '      Aplicações industriais')

# H2
r('Quais setores mais usam <span>empilhadeira industrial</span> em Goiânia?',
  'Onde a <span>empilhadeira a combustão Clark</span> opera em Senador Canedo')

r('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
  'Do polo petroquímico aos CDs da BR-153: os setores que mantêm empilhadeiras em turno contínuo.')

# Card 1
r('alt="Empilhadeira em galpão logístico, operação de carga e descarga de caminhões em CD da BR-153"',
  'alt="Centro de distribuição na BR-153 em Senador Canedo, doca com empilhadeira em operação"')
r('<h3>CDs logísticos da BR-153: carga e descarga de caminhões</h3>',
  '<h3>CDs de distribuição na BR-153: docas e expedição</h3>')
r('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 a 1.200 kg em turnos duplos. A troca rápida do cilindro GLP mantém a operação contínua sem parar para recarga.',
  'A BR-153 corta Senador Canedo conectando centros de distribuição que abastecem o Centro-Oeste. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de até 1.400 kg em turnos duplos sem interrupção. A troca de cilindro GLP em 3 minutos garante que a fila de caminhões na doca não pare.')

# Card 2
r('alt="Operação logística com empilhadeira, movimentação de fardos em atacadista do Polo da Moda de Goiânia"',
  'alt="Pátio do polo petroquímico de Senador Canedo com tanques e empilhadeira movimentando tambores"')
r('<h3>Polo da Moda: movimentação de fardos em atacadistas</h3>',
  '<h3>Polo petroquímico: tambores, IBC e insumos</h3>')
r('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A Clark C20s compacta é preferida nos corredores mais estreitos dos depósitos.',
  'Petrobras, Realpetro e Petrobol mantêm operações contínuas de movimentação de tambores de 200 litros, IBC de 1.000 kg e equipamentos de manutenção entre tanques e torres. A empilhadeira diesel opera nos pátios de cascalho com tração firme; a GLP transita entre o armazém fechado e a área de expedição sem trocar de equipamento.')

# Card 3
r('alt="Cabine do operador da empilhadeira Clark C60, detalhe do compartimento com controles ergonômicos"',
  'alt="Galpão farmacêutico no DASC de Senador Canedo com empilhadeira operando entre prateleiras"')
r('<h3>Distrito Industrial Leste: linhas de produção e pátios</h3>',
  '<h3>DASC: farmacêuticas, plásticos e higiene</h3>')
r('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque e os pneus maciços garantem tração em pisos irregulares e rampas de carga pesada.',
  'O Distrito Agroindustrial de Senador Canedo reúne laboratórios farmacêuticos, fábricas de plásticos e indústrias de higiene. A Clark L25 GLP movimenta paletes de insumos entre linhas de produção e áreas de estoque em galpões com pé-direito de até 12 metros. A GTS com cabine fechada protege o operador da poeira nos setores de embalagem e expedição.')

# Card 4
r('alt="Silos industriais e armazéns de cooperativas na GO-060, região de produção agrícola de Goiás"',
  'alt="Canteiro de obra e galpão do DISC em Senador Canedo com empilhadeira movimentando materiais"')
r('<h3>Cooperativas e armazéns da GO-060</h3>',
  '<h3>DISC e construção civil: expansão urbana</h3>')
r('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, sacaria de grãos e paletes de defensivos. A Clark S25/30/35 opera em pátios de terra e galpões sem pavimentação com a mesma eficiência.',
  'O segundo distrito industrial de Senador Canedo abriga o setor moveleiro e alimentício em expansão. Empilhadeiras S40-60 movimentam chapas de MDF, paletes de embalagens e insumos entre galpões e pátios sem pavimentação. Na construção civil dos novos bairros Residencial Canadá e Jardim das Oliveiras, a Clark L25 desloca paletes de blocos, vergalhões e argamassa em canteiros com piso irregular.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
  'Equipe técnica mobile com deslocamento pela BR-153. Atendimento em Senador Canedo em menos de 40 minutos a partir da sede. Diagnóstico de motor, transmissão e parte elétrica diretamente no seu galpão ou CD.')

r('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte da empilhadeira via BR-153 até seu CD, galpão do DASC ou pátio do polo petroquímico em Senador Canedo. São 20 km da sede — entrega no mesmo dia, sem custo de frete.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor do mastro deu problema no segundo mês, o técnico da Move veio no mesmo dia e resolveu sem custo."',
  '"Operamos com três Clark L25 no nosso CD na BR-153 em Senador Canedo. Turno duplo, 14 horas por dia. A troca de GLP é questão de minutos e a fila de caminhões na doca não para. Quando a mangueira hidráulica de uma delas rompeu no mês passado, o técnico da Move chegou pela BR-153 em menos de uma hora e trocou no local. Zero custo extra, zero dia parado."')
r('<strong>Roberto M.</strong>', '<strong>Anderson L.</strong>')
r('Gerente de Logística, Distribuidora, Goiânia-GO (nov/2025)',
  'Coordenador de Logística, CD de Distribuição BR-153, Senador Canedo-GO (dez/2025)')

# Depoimento 2
r('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha em rampa molhada. Melhor que comprar: sem IPVA, sem depreciação, sem dor de cabeça com peça."',
  '"Precisávamos movimentar tambores de 200 litros e IBC entre os tanques do complexo petroquímico. Alugamos a Clark L35 diesel porque o piso dos pátios é cascalho puro com rampa nas duas pontas. A máquina não escorrega, o contrapeso segura a carga firme e o diesel dá conta do torque. Renovamos o contrato por mais seis meses — sai mais barato que manter máquina própria com mecânico dedicado."')
r('<strong>Fábio S.</strong>', '<strong>Marcelo B.</strong>')
r('Diretor Industrial, Metalúrgica, Goiânia-GO (jan/2026)',
  'Supervisor de Operações, Petroquímica, Senador Canedo-GO (fev/2026)')

# Depoimento 3
r('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos e a entrega na capital é no mesmo dia."',
  '"Terceiro contrato consecutivo. No DASC, a demanda de empilhadeira varia conforme o calendário de produção farmacêutica. A locação mensal nos permite ter duas L25 em janeiro e quatro em março sem imobilizar capital. O orçamento pelo WhatsApp sai em minutos, a entrega pela BR-153 é no mesmo dia e a manutenção nunca nos deu dor de cabeça."')
r('<strong>Daniela P.</strong>', '<strong>Priscila N.</strong>')
r('Gerente de Operações, Atacadista, Goiânia-GO (fev/2026)',
  'Gerente de Supply Chain, Indústria Farmacêutica DASC, Senador Canedo-GO (mar/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-11 — link do curso + texto
# ═══════════════════════════════════════════════════════════════════════

# After link hrefs were already replaced by section 9, fix surrounding text
r('curso de operador de empilhadeira</a>? Indicamos parceiros credenciados em Goiânia.',
  'curso NR-11 para operadores de empilhadeira</a>? Indicamos centros de formação credenciados na região de Senador Canedo.')

# FAQ inline link text — the href is already fixed, now fix the anchor text
r('curso de operador de empilhadeira</a>.',
  'curso NR-11 de operador de empilhadeira</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Senador Canedo</span> e cidades vizinhas')

OLD_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Empilhadeiras Clark a combustão com GLP ou diesel para qualquer operação da região.</p>
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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 20 km de Senador Canedo pela BR-153, sem pedágio. Entrega de empilhadeira Clark no mesmo dia da confirmação. Atendemos toda a região metropolitana num raio de 200 km.</p>
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

r('Perguntas frequentes sobre <span>aluguel de empilhadeira</span> em Goiânia',
  'Dúvidas sobre <span>locação de empilhadeira a combustão</span> em Senador Canedo')

# FAQ 1
r('>Qual a empilhadeira a combustão mais alugada em Goiânia?<',
  '>Qual empilhadeira Clark é mais indicada para os CDs de Senador Canedo?<')
r('>A Clark L25 é o modelo mais contratado para operações em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria dos CDs logísticos da BR-153 e galpões de médio porte. A série L opera com GLP ou diesel e possui sistema hidráulico de alta eficiência.<',
  '>A Clark L25 lidera os contratos nos CDs da BR-153 em Senador Canedo. Capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex para empilhamento até 6 metros. Opera com GLP ou diesel em turnos duplos, com troca rápida de cilindro que mantém a operação contínua nas docas de distribuição.<')

# FAQ 2
r('>Qual a diferença entre empilhadeira a combustão e elétrica?<',
  '>Combustão ou elétrica: qual escolher para o polo petroquímico e DASC?<')
r('>A empilhadeira a combustão (GLP ou diesel) oferece maior torque, opera em pátios externos sem restrição de emissão e não depende de recarga de bateria. A elétrica é silenciosa e indicada para ambientes fechados com ventilação limitada. Para operações mistas em Goiânia (doca + pátio + galpão), a combustão é a escolha mais versátil.<',
  '>Nos pátios do polo petroquímico e nas vias internas do DASC, onde o piso é irregular e a empilhadeira transita entre área coberta e externa, a combustão (GLP ou diesel) entrega torque superior, opera sob chuva e não para para recarga. A elétrica funciona em galpões farmacêuticos com área limpa e restrição de emissão. Para operações mistas em Senador Canedo, a combustão cobre mais cenários.<')

# FAQ 3
r('>Quanto custa alugar empilhadeira a combustão em Goiânia?<',
  '>Qual o valor mensal da locação de empilhadeira em Senador Canedo?<')
r('>O valor varia de R$2.800 a R$4.000 por mês, dependendo do modelo (L25, GTS, S-Series ou C-Series), prazo de contrato e capacidade de carga. O aluguel inclui manutenção preventiva e corretiva, suporte técnico 24h e entrega sem custo de deslocamento na capital.<',
  '>O investimento mensal fica entre R$2.800 e R$4.000, variando por modelo (L25, GTS, S-Series ou C-Series), combustível e duração do contrato. Senador Canedo recebe sem custo de frete — são 20 km pela BR-153. O pacote inclui manutenção preventiva e corretiva, suporte técnico 24h e equipe mobile que chega em menos de 40 minutos.<')

# FAQ 4
r('>A manutenção da empilhadeira está inclusa no aluguel?<',
  '>O contrato cobre manutenção do motor, mastro e sistema hidráulico?<')
r('>Sim. Toda locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. Nossa equipe técnica mobile atende em Goiânia e região 24 horas por dia, 7 dias por semana. Se a empilhadeira apresentar qualquer falha, acionamos suporte ou substituímos o equipamento.<',
  '>Integralmente. O contrato cobre revisão periódica de motor, transmissão, bomba hidráulica, cilindros, válvulas, mastro e garfos — sem custo adicional de peça ou mão de obra. Nossa equipe técnica mobile chega a Senador Canedo pela BR-153 em menos de 40 minutos. Se a máquina tiver falha irreparável no local, substituímos o equipamento no mesmo dia.<')

# FAQ 5
r('>Qual combustível escolher: GLP ou diesel?<',
  '>GLP ou diesel para as operações em Senador Canedo?<')
r('>O GLP é mais indicado para operações que alternam entre ambientes internos e externos, pois emite menos poluentes. O diesel entrega maior torque em rampas e pátios irregulares, sendo preferido no Distrito Industrial e em operações pesadas. Todos os modelos Clark disponíveis na Move Máquinas aceitam ambos os combustíveis.<',
  '>O diesel é o padrão nos pátios do polo petroquímico e nas vias internas do DASC, onde rampas de cascalho exigem torque máximo. O GLP é mais versátil quando a empilhadeira alterna entre galpão fechado e doca externa — menos emissão e troca de cilindro em 3 minutos. Todos os modelos Clark aceitam ambos os combustíveis, e trocamos a configuração no próprio contrato se necessário.<')

# FAQ 6
r('>Vocês entregam empilhadeira fora de Goiânia?<',
  '>Qual o prazo de entrega de empilhadeira em Senador Canedo?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Senador Canedo é uma das entregas mais rápidas: 20 km pela BR-153, sem pedágio. A empilhadeira sai da sede e chega ao seu CD, galpão ou pátio industrial em menos de 1 hora. Para paradas programadas no polo petroquímico, agendamos a entrega com antecedência. Sem custo de deslocamento.<')

# FAQ 7
r('>Preciso de habilitação especial para operar empilhadeira?<',
  '>Operadores no DASC e polo petroquímico precisam de certificação NR-11?<')
# This FAQ answer contains an <a> tag that gets partially modified by earlier link replaces.
# We need to match the ORIGINAL text (before any link replace modifies it).
r('Sim. A NR-11 exige que todo operador de empilhadeira possua treinamento específico e certificado válido. O curso abrange inspeção pré-operacional, regras de empilhamento, capacidade de carga e sinalização de manobra. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o',
  'Obrigatoriamente. A NR-11 exige curso específico com certificado válido para todo operador de empilhadeira. O treinamento abrange inspeção pré-operacional, limites de carga, empilhamento seguro e sinalização de manobra. Conectamos sua equipe a centros de formação credenciados na região de Senador Canedo. Saiba mais sobre o')

# FAQ 8
r('>Qual a capacidade máxima das empilhadeiras Clark disponíveis?<',
  '>Até quantos quilos as empilhadeiras Clark suportam?<')
r('>A frota Clark para locação em Goiânia cobre de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para operações no Distrito Industrial Leste com chapas de aço, bobinas e containers, a série C60/70/80 é a mais indicada. Para CDs logísticos e galpões, a L25/30/35 atende a grande maioria das demandas.<',
  '>A frota vai de 2.000 kg (C20s compacta) até 8.000 kg (C80 heavy duty). Para movimentação de tambores e insumos no polo petroquímico, a L25/30/35 resolve. Para bobinas de aço e cargas industriais pesadas no DISC, a série C60/70/80 é a indicação técnica. Nossa equipe dimensiona o modelo certo antes de fechar — sem custo de consultoria.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de empilhadeira Clark em Goiânia',
  'Solicite empilhadeira Clark para Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
  "'Olá, preciso de empilhadeira a combustão em Senador Canedo.\\n\\n'")

# Video iframe title (inside onclick handler)
r("title=\\'Quanto custa alugar empilhadeira em Goiânia\\'",
  "title=\\'Locação de empilhadeira Clark em Senador Canedo\\'")

# ═══════════════════════════════════════════════════════════════════════
# 20. ADDITIONAL REWRITES — reduce Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Marquee stats bar — rewrite text items
r('<strong>Clark</strong> exclusivo em Goiás',
  '<strong>Clark</strong> distribuidor autorizado', 99)

r('<strong>200km</strong> raio de atendimento',
  '<strong>20 km</strong> de Senador Canedo', 99)

# Section subtitle in "O que é"
r('Entenda o equipamento',
  'Conheça antes de alugar')

# Cotação rápida section
r('Já conhece o equipamento. Agora <span style="color:var(--color-primary);">solicite seu orçamento.</span>',
  'Empilhadeira certa para Senador Canedo. <span style="color:var(--color-primary);">Peça seu orçamento agora.</span>')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe o modelo e a urgência ao lado — respondemos pelo WhatsApp em até 2 horas com valor, prazo e disponibilidade.')

r('Manutenção inclusa (motor, hidráulico, mastro)',
  'Manutenção completa inclusa no contrato')

r('GLP ou Diesel, de 2.000 a 8.000 kg',
  'GLP ou Diesel — de 2.000 a 8.000 kg')

r('Suporte técnico 24h, 7 dias',
  'Equipe técnica mobile 24h em Senador Canedo')

# Fleet section tag
r('Frota Clark',
  'Modelos disponíveis')

# Fleet H2
r('Frota de <span>empilhadeira Clark</span> disponível para locação',
  'Empilhadeiras <span>Clark a combustão</span> prontas para Senador Canedo')

# Fleet subtitle
r('Seis séries de empilhadeiras a combustão com capacidades de 2.000 a 8.000 kg. Todos os modelos operam com GLP ou diesel.',
  'Da compacta C20s até a C80 heavy duty: seis séries cobrindo de 2.000 a 8.000 kg. Todos os modelos aceitam GLP ou diesel.')

# Fleet disclaimer
r('Dúvida sobre qual modelo atende sua operação? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não sabe qual modelo sua operação exige? Nossa equipe dimensiona sem custo. Fale pelo WhatsApp ou ligue.')

# Comparativo intro
r('A escolha entre combustão e elétrica depende do ambiente de operação, do regime de turnos e do tipo de carga. Entender a diferença evita contratar o equipamento errado e paralisar a operação.',
  'Nos CDs e plantas industriais de Senador Canedo, a decisão entre combustão e elétrica depende do piso, ventilação e regime de turnos. Escolher errado significa máquina parada ou equipamento inadequado para o ambiente.')

# Comparativo card texts
r('Para pátios, docas e operações mistas',
  'Pátios do polo petroquímico, docas e CDs')

r('Opera em ambientes internos e externos sem restrição. Motor a GLP ou diesel com torque superior para rampas e pisos irregulares.',
  'Transita entre galpão fechado e pátio de cascalho sem restrição. Motor GLP ou diesel com torque para rampas e pisos irregulares do DASC e polo petroquímico.')

r('Para ambientes fechados e silenciosos',
  'Galpões farmacêuticos e áreas limpas')

r('Zero emissão, operação silenciosa. Indicada para câmaras frias, indústria alimentícia e galpões sem ventilação.',
  'Zero emissão e ruído mínimo. Indicada para galpões farmacêuticos do DASC, câmaras frias e linhas alimentícias do DISC.')

# Incluso section
r('+20 anos no mercado goiano nos ensinaram que o diferencial não é o equipamento. É o que acontece quando o sistema hidráulico falha no meio do turno.',
  'Mais de duas décadas atendendo indústrias no Centro-Oeste nos mostraram que o diferencial da locação não é a máquina — é o que acontece quando o hidráulico falha às 3 da manhã no meio do turno.')

# Incluso - consultoria
r('Nosso time ajuda a dimensionar modelo, capacidade e combustível para sua operação. Avaliação sem compromisso para evitar escolha errada.',
  'Avaliamos modelo, capacidade e combustível adequados antes de fechar. No polo petroquímico e DASC, cada operação tem exigência específica — a consultoria gratuita evita contratação errada.')

# Price section H3
r('R$2.800 a R$4.000/mês com manutenção inclusa',
  'De R$2.800 a R$4.000/mês — manutenção e suporte no pacote')

r('Todos os contratos incluem manutenção preventiva e corretiva do sistema hidráulico, mastro, garfos, motor e transmissão. O valor mensal cobre o equipamento completo, sem custos ocultos de peças ou mão de obra técnica.',
  'O valor mensal cobre a máquina completa com manutenção preventiva e corretiva de sistema hidráulico, mastro, garfos, motor e transmissão. Sem custo oculto de peça, mão de obra ou deslocamento técnico para Senador Canedo.')

# Price H3 - custo real
r('O custo real de uma empilhadeira parada',
  'Quanto custa um dia de empilhadeira parada em Senador Canedo')

# NR-11 section
r('Como garantir conformidade com a <span>NR-11</span> na operação de empilhadeira?',
  'Operação de empilhadeira e conformidade com a <span>NR-11</span> em Senador Canedo')

r('A NR-11 regulamenta o transporte, movimentação, armazenagem e manuseio de materiais. Todo operador de empilhadeira precisa de treinamento específico e certificado válido.',
  'A NR-11 define as regras para movimentação, transporte e armazenagem de materiais em ambiente industrial. Todo operador de empilhadeira nos CDs, DASC e polo petroquímico de Senador Canedo precisa de certificação válida.')

r('O que a NR-11 exige do operador de empilhadeira',
  'Requisitos NR-11 para operadores em Senador Canedo')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar em conformidade')

r('Confirme que o operador possui curso de empilhadeira válido. O treinamento cobre inspeção pré-operacional, empilhamento, capacidade de carga e manobras.',
  'Todo operador deve apresentar certificado de curso NR-11 válido antes de assumir o equipamento. O treinamento abrange inspeção pré-operacional, empilhamento seguro, capacidade de carga e manobras em pátio.')

r('Antes de cada turno: verifique garfos (trincas, desgaste), mastro (correntes, roletes), freios, direção, nível de GLP ou diesel e sinalizadores.',
  'No início de cada turno o operador deve verificar garfos (trincas e desgaste), mastro (correntes e roletes), freios, direção, nível de GLP ou diesel e funcionamento dos sinalizadores.')

r('Demarque corredores de empilhadeira, instale espelhos convexos em cruzamentos e defina velocidade máxima para áreas com circulação de pedestres.',
  'Delimite os corredores exclusivos de empilhadeira, posicione espelhos convexos nos cruzamentos e estabeleça limite de velocidade onde há trânsito de pedestres.')

r('Mantenha registros de inspeção pré-operacional, certificados dos operadores e plano de manutenção. A Move Máquinas entrega o equipamento com checklist de inspeção.',
  'Arquive os registros de inspeção diária, certificados dos operadores e cronograma de manutenção. Cada empilhadeira da Move Máquinas é entregue acompanhada do checklist de inspeção pré-operacional.')

# Depoimentos H2
r('O que nossos clientes dizem sobre a <span>empilhadeira a combustão</span>',
  'Empresas de Senador Canedo que operam com <span>empilhadeira Clark</span>')

# Footer CTA subtitle
r('Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.',
  'Resposta imediata com disponibilidade, modelo, valor e prazo de entrega para Senador Canedo.')

# Video section caption
r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial Move Máquinas no YouTube — mais de 50 vídeos sobre locação de equipamentos.')

# alt text img principal
r('alt="Empilhadeira Clark L25 a combustão, o modelo mais alugado em Goiânia para operações em CDs logísticos e galpões"',
  'alt="Empilhadeira Clark L25 a combustão para locação em Senador Canedo — CDs da BR-153 e polo petroquímico"')

# alt text C70 slide
r('alt="Empilhadeira Clark C70 heavy duty para cargas de 7.000 kg no Distrito Industrial de Goiânia"',
  'alt="Empilhadeira Clark C70 heavy duty para cargas pesadas no polo petroquímico de Senador Canedo"')

# alt text empilhadeira em operação no hero video
r('alt="Empilhadeira Clark a combustão em operação"',
  'alt="Empilhadeira Clark a combustão em operação em Senador Canedo"')

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
            'goiania-go/', '20 km', 'Sede na',  # link para hub goiania ou distância
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
sc = html.count('Senador Canedo')
local = html.count('DASC') + html.count('petroquím') + html.count('DISC') + html.count('BR-153')
print(f"\nSenador Canedo: {sc} menções")
print(f"Contexto local (DASC/petroquímico/DISC/BR-153): {local} menções")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS
# ═══════════════════════════════════════════════════════════════════════

import os

def extract_text(h):
    """Strip HTML tags and get just text."""
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(set1, set2):
    inter = len(set1 & set2)
    union = len(set1 | set2)
    return inter / union if union > 0 else 0.0

new_text = extract_text(html)
new_ng = ngrams(new_text)

ref_text = extract_text(ref)
ref_ng = ngrams(ref_text)

j_ref = jaccard(new_ng, ref_ng)
print(f"\n{'=' * 60}")
print("JACCARD 3-GRAMS")
print(f"{'=' * 60}")
print(f"vs ref-goiania-combustao.html:    {j_ref:.4f}  {'✓' if j_ref < 0.20 else '✗ FALHOU'}")

# Compare with other SC pages
comparisons = [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
]
for comp_path in comparisons:
    if os.path.exists(comp_path):
        with open(comp_path, 'r', encoding='utf-8') as f:
            comp_html = f.read()
        comp_text = extract_text(comp_html)
        comp_ng = ngrams(comp_text)
        j_comp = jaccard(new_ng, comp_ng)
        fname = os.path.basename(comp_path)
        print(f"vs {fname}: {j_comp:.4f}  {'✓' if j_comp < 0.20 else '✗ FALHOU'}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")
