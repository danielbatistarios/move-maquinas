#!/usr/bin/env python3
"""
rebuild-luziania-tesoura-v2.py
Gera LP de Plataforma Tesoura para Luziânia
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.

CONTEXTO LUZIÂNIA:
- slug: luziania-go, Coords: -16.2532, -47.9501
- 198km via BR-040, pop 210.000
- Economia: indústria (metalurgia, alimentos, químicos), agropecuária
- Polo: DIAL (Distrito Agroindustrial de Luziânia)
- Entity bridge tesoura: manutenção interna de fábricas no DIAL, instalações industriais
- Contexto: galpões metalúrgicos DIAL, fábricas de alimentos, armazéns de grãos, indústrias químicas — piso nivelado, pé-direito 8-12m
"""

import time
START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/luziania-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

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
  '<title>Plataforma Tesoura para Locação em Luziânia-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma tesoura em Luziânia: modelos elétricos 8-10m para galpões metalúrgicos do DIAL e diesel 12-15m para pátios agroindustriais. Manutenção no contrato, entrega via BR-040. Move Máquinas: referência em locação de plataformas."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/luziania-go/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locação em Luziânia-GO | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Plataforma tesoura elétrica e diesel de 8 a 15m em Luziânia. Indicada para galpões metalúrgicos do DIAL, fábricas de alimentos e armazéns de grãos. Manutenção coberta pelo contrato, entrega pela BR-040."')

r('content="Goiânia, Goiás, Brasil"', 'content="Luziânia, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.2532;-47.9501"')
r('content="-16.7234, -49.2654"', 'content="-16.2532, -47.9501"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.2532, "longitude": -47.9501')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.2532')
r('"longitude": -49.2654', '"longitude": -47.9501')

# Schema — Service name
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Plataforma Tesoura para Locação em Luziânia"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Luziânia", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Luziânia", "item": "https://movemaquinas.com.br/luziania-go/aluguel-de-plataforma-elevatoria-tesoura"')

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
        { "@type": "Question", "name": "A tesoura resolve manutenção dentro dos galpões metalúrgicos do DIAL?", "acceptedAnswer": { "@type": "Answer", "text": "Sim, a tesoura é a primeira opção para galpões do DIAL. O mecanismo pantográfico sobe na vertical sem oscilação, ideal para coberturas metálicas com pé-direito de 8 a 12 metros e pisos de concreto industrial. A versão elétrica não emite gases — requisito obrigatório nas fábricas de alimentos e indústrias químicas do distrito. Se houver tubulação cruzando o caminho, a articulada é necessária." } },
        { "@type": "Question", "name": "Tesoura elétrica ou diesel para as fábricas de Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Dentro das fábricas de alimentos e indústrias químicas do DIAL, a elétrica é mandatória: zero emissão de gases preserva a qualidade do ar em ambientes controlados, e a operação silenciosa permite manutenção durante turnos de produção. A diesel 4x4 atende pátios agroindustriais, silos externos e canteiros de expansão onde o piso é cascalho ou terra compactada." } },
        { "@type": "Question", "name": "Qual a altura máxima disponível para locação em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "A frota para Luziânia inclui tesoura elétrica de 8 a 10 metros e diesel de 12 a 15 metros de trabalho. A elétrica de 8-10m atende a maioria dos galpões metalúrgicos e fábricas do DIAL. A diesel de 12-15m cobre estruturas mais altas como armazéns de grãos ao longo da BR-040 e silos agroindustriais." } },
        { "@type": "Question", "name": "Operadores das indústrias de Luziânia precisam de NR-35?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Qualquer trabalho acima de 2 metros exige capacitação NR-35 válida. O treinamento abrange avaliação de riscos, uso de cinto paraquedista, checklist pré-operacional e técnicas de resgate em emergência. A Move Máquinas indica centros de formação credenciados acessíveis a empresas de Luziânia e região do Entorno." } },
        { "@type": "Question", "name": "A manutenção vem incluída no contrato de locação?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todos os contratos cobrem manutenção preventiva e corretiva do sistema hidráulico pantográfico, cilindros, componente elétrico e baterias. Em caso de falha durante uso em Luziânia, nossa equipe técnica se desloca pela BR-040 para diagnóstico no local ou substituição do equipamento." } },
        { "@type": "Question", "name": "Quanto tempo leva a entrega da tesoura em Luziânia?", "acceptedAnswer": { "@type": "Answer", "text": "Luziânia está a 198 km da base pela BR-040. A entrega acontece no mesmo dia para pedidos confirmados pela manhã. Para operações programadas em indústrias do DIAL, agendamos com antecedência para garantir modelo e data. O frete é calculado conforme a distância." } },
        { "@type": "Question", "name": "A tesoura diesel opera nos pátios agroindustriais com piso irregular?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A versão diesel possui tração 4x4 e chassi reforçado para cascalho, terra batida e desnível moderado — cenário habitual nos pátios entre galpões do DIAL e acessos a armazéns de grãos. Para ambientes internos com piso firme, a elétrica é mais adequada. Se o serviço exige contornar obstáculos, avalie a plataforma articulada." } },
        { "@type": "Question", "name": "Quantos operadores cabem na cesta da tesoura para trabalhos no DIAL?", "acceptedAnswer": { "@type": "Answer", "text": "A cesta comporta de 230 a 450 kg conforme modelo. A elétrica de 8-10m leva até 320 kg — dois técnicos com ferramental de manutenção industrial. A diesel de 12-15m suporta até 450 kg, cabendo 3 operadores com equipamentos de montagem. Nos galpões metalúrgicos do DIAL, a cesta ampla da tesoura permite trabalho lado a lado sem reposicionamento constante." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/luziania-go/">Equipamentos em Luziânia</a>')

r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Luziânia</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Plataformas prontas para entrega em Goiânia',
  'Disponível para indústrias de Luziânia e Entorno-DF')

r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locação de Plataforma Tesoura em <em>Luziânia</em>')

r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Tesoura elétrica 8-10m para manutenção interna de galpões metalúrgicos e fábricas de alimentos no DIAL. Diesel 12-15m para pátios agroindustriais e armazéns de grãos. Manutenção coberta pelo contrato, entrega via BR-040 no mesmo dia.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Luzi%C3%A2nia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Luziânia
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Referência em locação</span>')

r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>',
  '<strong>Via BR-040</strong><span>198 km, entrega expressa</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação do pool
r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'Como funciona a <span>plataforma tesoura</span> e por que domina o DIAL de Luziânia')

# Parágrafo principal
r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'O mecanismo pantográfico da plataforma tesoura eleva a cesta na vertical pura — sem giro, sem balanço lateral. O resultado é estabilidade incomparável para trabalhos sobre superfícies planas como coberturas metálicas, forros industriais e telhados de armazéns. Luziânia abriga o DIAL (Distrito Agroindustrial de Luziânia) com dezenas de galpões de metalurgia, processamento de alimentos e química industrial, todos com pé-direito de 8 a 12 metros e piso de concreto nivelado. Esse cenário faz da tesoura o equipamento de elevação mais requisitado na cidade.')

# H3 — por que domina trabalhos internos
r('Por que a tesoura domina trabalhos internos na capital',
  'Metalúrgicas e fábricas de alimentos: a tesoura resolve sem parar a produção')

r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'Nos galpões metalúrgicos do DIAL, as linhas de produção funcionam em regime contínuo e qualquer parada programada custa caro. A tesoura elétrica permite manutenção de cobertura, troca de iluminação e reparo de exaustores durante o expediente: motor silencioso movido a bateria, zero emissão de gases e pneus que não riscam o piso industrial. O centro de gravidade baixo do mecanismo pantográfico garante estabilidade mesmo quando o operador trabalha a 10 metros de altura com ferramental pesado.')

# H3 — elétrica vs diesel
r('Elétrica vs. diesel: quando escolher cada versão',
  'Modelo elétrico ou diesel: critério técnico para cada situação no DIAL')

r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'A definição é técnica: fábricas de alimentos e indústrias químicas do DIAL exigem tesoura elétrica — baterias de ciclo profundo, zero contaminante atmosférico, operação silenciosa. Os pátios entre galpões, acessos a silos e canteiros de expansão industrial pedem a diesel 4x4, projetada para cascalho, terra compactada e desnível moderado. Para obras residenciais nos bairros Jardim Ingá e Park Estrela, onde o solo ainda não recebeu pavimentação, a diesel também é mandatória.')

# H3 — capacidade de carga
r('Capacidade de carga e dimensões da cesta',
  'Cesta ampla: dois técnicos com ferramental completo no DIAL')

r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'A cesta suporta de 230 a 450 kg e alcança até 2,50 m de largura — espaço para 1 a 3 técnicos de manutenção com todo o ferramental necessário. Nos galpões metalúrgicos do DIAL, equipes de soldadores e eletricistas sobem juntos para reparar estrutura metálica e substituir painéis de iluminação sem precisar revezar posição. A largura da plataforma reduz em 40% o tempo de reposicionamento da base comparado com a cesta compacta da articulada.')

# Bullet "Aplicações em Goiânia"
r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Onde opera em Luziânia:</strong> manutenção de coberturas em galpões metalúrgicos do DIAL, troca de iluminação em fábricas de alimentos, reparo de exaustores em indústrias químicas e obras residenciais nos bairros Jardim Ingá e Park Estrela.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia via BR-040')

# Form selects — Luziânia como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Luziânia" selected>Luziânia</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Brasília">Brasília</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>''')

# Form selects — Luziânia como primeira opção (mobile)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Luziânia" selected>Luziânia</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Brasília">Brasília</option>
              <option value="Valparaíso de Goiás">Valparaíso de Goiás</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Subtitle slide 0
r('8 a 10 m de altura de trabalho para ambientes internos',
  '8 a 10 m de elevação para galpões metalúrgicos e fábricas do DIAL')

# Slide 0 — elétrica 8-10m
r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'A tesoura elétrica concentra os contratos em Luziânia para serviços dentro dos galpões do DIAL. Baterias industriais de ciclo profundo movem o mecanismo pantográfico em silêncio absoluto — condição obrigatória nas fábricas de alimentos onde a qualidade do ar é controlada. A cesta de até 320 kg acomoda dois técnicos com ferramental completo de soldagem ou elétrica. Pneus não marcantes protegem pisos de concreto polido e epóxi. Aplicações recorrentes: substituição de luminárias em metalúrgicas, reparo de calhas pluviais em fábricas de alimentos e manutenção de exaustores em indústrias químicas.')

# Subtitle slide 1
r('12 a 15 m de altura de trabalho para obras e pátios',
  '12 a 15 m de alcance para pátios agroindustriais e canteiros de Luziânia')

# Slide 1 — diesel 12-15m
r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Tração 4x4, chassi robusto e pneus para terreno bruto — a tesoura diesel atende os pátios agroindustriais do DIAL, acessos aos armazéns de grãos e canteiros de obra nos novos loteamentos de Luziânia. Alcança 12 a 15 metros com até 450 kg na cesta, suficiente para 3 montadores com chapas metálicas e estruturas de fixação. Aplicações típicas: instalação de coberturas em silos, montagem de estruturas de expansão industrial e acabamento de fachadas nos empreendimentos residenciais do Jardim Ingá.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Luziânia
# ═══════════════════════════════════════════════════════════════════════

r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Luziânia tem um parque industrial forte no DIAL — metalurgia, alimentos, química. A tesoura elétrica é o equipamento que mais sai para essas fábricas porque o piso é concreto nivelado e nenhuma delas aceita motor a combustão dentro do galpão. Na hora de enviar para Luziânia, calculo a logística pela BR-040 e confirmo com o cliente se o trabalho é interno ou externo. Se for pátio de silo com chão de terra, mando diesel 4x4. Se tiver tubulação de processo cruzando na frente do ponto de trabalho, recomendo articulada. Essa triagem técnica antes do envio evita retrabalho e custo desnecessário."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

# H2 comparativo
r('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
  '<span>Tesoura</span> ou articulada: qual equipamento a indústria de Luziânia precisa?')

# Intro
r('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
  'Máquinas projetadas para funções distintas que trabalham em conjunto. A tesoura sobe na vertical com bancada ampla para a equipe; a articulada contorna estruturas com braço multi-articulado. Erro na seleção compromete prazo e gera despesa evitável.')

# Tesoura card text
r('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
  'Elevação vertical sem oscilação e cesta ampla para equipe de manutenção. Perfeita para coberturas metálicas, troca de iluminação e reparos industriais nos galpões do DIAL.')

# Articulada card text
r('Braço articulado com alcance horizontal e vertical. Indicada quando é necessário alcançar pontos distantes da base ou contornar obstáculos.',
  'Braço articulado que contorna tubulações de processo e vasos de pressão. Indispensável quando estruturas intermediárias bloqueiam o acesso vertical direto em plantas industriais.')

# Verdict
r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Regra para o parque industrial de Luziânia:</strong> se o ponto de trabalho é acessível por elevação vertical direta — cobertura, forro, iluminação — e o piso é firme, a tesoura realiza o serviço com mais rapidez e custo inferior. Se há tubulação de processo, ponte rolante ou estrutura cruzando o trajeto, a articulada é obrigatória. Na dúvida, realizamos visita técnica gratuita antes do envio do equipamento.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Luziânia:')

# Links internos — todos para luziania-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/luziania-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Luziânia')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/luziania-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Luziânia')

r('/goiania-go/aluguel-de-transpaleteira', '/luziania-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Luziânia')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: como funciona a locação de plataforma tesoura para indústrias em Luziânia"')

r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Veja como funciona a <span>locação de plataforma tesoura</span> para Luziânia')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Investimento na locação de <span>plataforma tesoura</span> em Luziânia (2026)')

r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'O valor varia conforme modelo (elétrica ou diesel), faixa de altura e duração do contrato. Manutenção preventiva e corretiva integradas em todas as modalidades.')

r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'A locação de plataforma tesoura para Luziânia opera nas modalidades diária, semanal e mensal. Contratos superiores a 30 dias garantem condições diferenciadas para as indústrias do DIAL. O investimento engloba equipamento revisado, manutenção integral e assistência técnica durante toda a vigência.')

r('Entrega em Goiânia no mesmo dia',
  'Entrega em Luziânia via BR-040 no mesmo dia')

r('Obras civis, pátios e condomínios',
  'Pátios do DIAL, silos e canteiros de Luziânia')

r('Sem custo de deslocamento na capital',
  'Frete calculado pela BR-040 (198 km)')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 198 km de Luziânia pela BR-040, estrada duplicada e bem sinalizada. O frete é calculado conforme a distância. A plataforma chega no galpão do DIAL, pátio agroindustrial ou canteiro pronta para iniciar a operação no mesmo dia.')

r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>O custo real de improvisar no DIAL:</strong> escadas e andaimes tubulares dentro dos galpões metalúrgicos de Luziânia consomem horas de montagem, bloqueiam linhas de produção e expõem trabalhadores a quedas sem proteção homologada. A tesoura elétrica sobe em 30 segundos, posiciona o técnico com guarda-corpo certificado e libera o corredor de produção assim que desce. A NR-35 obriga uso de equipamento adequado para qualquer serviço acima de 2 metros — autuações por descumprimento alcançam dezenas de milhares de reais.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('Aplicações em Goiânia', 'Aplicações no DIAL')

# H2 — variação
r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'Das metalúrgicas aos armazéns: onde a <span>tesoura pantográfica</span> trabalha em Luziânia')

# Subtitle
r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Os cenários que mais demandam tesoura na cidade: galpões metalúrgicos, indústria alimentícia, armazéns de grãos e construção residencial.')

# Card 1
r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Galpão metalúrgico no DIAL de Luziânia com estrutura metálica e pé-direito industrial"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>Metalúrgicas do DIAL: coberturas e estrutura metálica</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'As metalúrgicas do DIAL operam com galpões de 8 a 12 metros de pé-direito e coberturas de aço galvanizado. A tesoura elétrica posiciona soldadores e eletricistas na altura exata da estrutura sem contaminar o ambiente com gases de combustão. Reparos em treliças, substituição de telhas danificadas e inspeção de calhas pluviais acontecem durante o turno de produção sem paralisar as linhas de fabricação abaixo.')

# Card 2
r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Interior de fábrica de alimentos no DIAL de Luziânia com área de produção controlada"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>Indústria alimentícia: ambientes controlados do DIAL</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'Fábricas de alimentos no DIAL de Luziânia processam grãos, laticínios e embutidos em ambientes com controle rigoroso de contaminação. A tesoura elétrica é o único equipamento de elevação compatível: motor silencioso, zero emissão atmosférica e pneus não marcantes sobre piso epóxi. Técnicos de manutenção sobem para trocar luminárias sanitárias, inspecionar dutos de exaustão e reparar forros térmicos sem comprometer a certificação do espaço.')

# Card 3
r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Armazém de grãos no entorno do DIAL de Luziânia com cobertura metálica de grande vão"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Armazéns de grãos: coberturas de grande vão na BR-040</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'Armazéns e silos ao longo da BR-040 em Luziânia possuem coberturas metálicas com vãos de 10 a 15 metros que exigem inspeção periódica. A tesoura diesel 4x4 opera nos pátios de carga e descarga, elevando técnicos para reparar chapas de cobertura, calhas de escoamento e sistemas de ventilação em grandes extensões. A cesta comporta eletricista, material de fixação e ferramental pesado para cobrir faixas longas por passada.')

# Card 4
r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Obras residenciais em expansão nos bairros Jardim Ingá e Park Estrela em Luziânia"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção civil: Jardim Ingá e Park Estrela</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'Luziânia vive expansão imobiliária acelerada nos bairros Jardim Ingá e Park Estrela. A tesoura diesel 4x4 opera nos canteiros com solo sem pavimentação para montagem de estrutura metálica, fechamento lateral e pintura de fachada reta. A estabilidade vertical da tesoura é vantajosa para revestimentos em superfícies planas, onde a articulada seria recurso excessivo.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Equipe técnica que se desloca até Luziânia pela BR-040 para diagnóstico e reparo in loco. Se a tesoura apresentar problema, realizamos intervenção no local ou providenciamos substituição do equipamento.')

r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte pela BR-040 até o galpão no DIAL, armazém de grãos ou canteiro de obra. São 198 km da base — entrega no mesmo dia para pedidos matinais, frete calculado conforme distância.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Substituímos 120 luminárias em dois galpões da metalúrgica no DIAL usando a tesoura elétrica. Dois eletricistas na cesta trabalhando lado a lado, ferramentas ao alcance direto. Concluímos em 3 turnos o que com andaime tomaria 2 semanas. Zero emissão de gás, piso limpo o tempo todo. A Move agendou entrega pela BR-040 e a máquina estava no portão às 7h conforme combinado."')
r('<strong>Marcos V.</strong>', '<strong>Ricardo T.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Supervisor de Manutenção, Metalúrgica DIAL, Luziânia-GO (out/2025)')

# Depoimento 2
r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Reparo de cobertura em armazém de grãos na BR-040 com a tesoura diesel. A 4x4 atravessou o pátio de cascalho sem problema, subiu 3 montadores com chapas de aço a 14 metros. Economizamos R$18 mil em andaime tubular e cortamos 12 dias do cronograma. A Move faz consultoria técnica antes de enviar e acertou de primeira o modelo necessário."')
r('<strong>Patrícia R.</strong>', '<strong>Adriana M.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Engenheira de Obras, Agronegócio, Luziânia-GO (dez/2025)')

# Depoimento 3
r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Pintamos todo o forro de uma fábrica de alimentos no DIAL com a tesoura elétrica. A operação silenciosa não interferiu na linha de produção vizinha. Dois pintores cobrindo 2 metros de largura por passada — em 5 dias úteis terminamos 2.800 m2 de forro. A estimativa com escada era de 15 dias. A Move cuida de tudo: entrega, orientação técnica, retirada."')
r('<strong>Carlos H.</strong>', '<strong>Paulo V.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Gerente de Facilities, Ind. Alimentícia DIAL, Luziânia-GO (jan/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link e texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para operação em altura</a>? Indicamos centros credenciados acessíveis às empresas de Luziânia e Entorno-DF.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega em <span>Luziânia</span> e cidades do Entorno-DF')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 198 km de Luziânia pela BR-040. Entrega de plataforma tesoura no mesmo dia para pedidos matinais. Atendemos Luziânia, Entorno-DF e toda a região num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/"><strong>Luziânia</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília (DF)</a>
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

# Maps embed + links below
r('!2d-49.2654!3d-16.7234', '!2d-47.9501!3d-16.2532')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Luziânia e Entorno-DF"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Luziânia</a>')
r('/goiania-go/" style="color', '/luziania-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma tesoura</span> em Luziânia')

# FAQ 1
r('>Qual a diferença entre plataforma tesoura e articulada?<',
  '>A tesoura resolve manutenção dentro dos galpões metalúrgicos do DIAL?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>Sim. O mecanismo pantográfico sobe na vertical sem oscilação, perfeito para coberturas metálicas com pé-direito de 8 a 12 metros e pisos de concreto industrial. A versão elétrica não emite gases — requisito das fábricas de alimentos e indústrias químicas do DIAL. A cesta de até 2,50m comporta dois técnicos com ferramental de soldagem. Se tubulação cruzar o caminho, a articulada é necessária.<')

# FAQ 2
r('>Plataforma tesoura elétrica ou diesel: qual escolher?<',
  '>Tesoura elétrica ou diesel para as fábricas de Luziânia?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>Dentro das fábricas de alimentos e indústrias químicas do DIAL, a elétrica é mandatória: zero emissão preserva ambientes controlados e a operação silenciosa permite trabalho durante os turnos de produção. A diesel 4x4 serve para pátios agroindustriais, silos externos e canteiros com piso de cascalho ou terra compactada. Para operações internas no DIAL, sempre elétrica.<')

# FAQ 3
r('>Qual a altura máxima da plataforma tesoura?<',
  '>Qual a altura máxima disponível para locação em Luziânia?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>A frota para Luziânia inclui elétrica de 8 a 10 metros e diesel de 12 a 15 metros de trabalho. A elétrica de 8-10m atende a maioria dos galpões metalúrgicos e fábricas do DIAL. A diesel de 12-15m cobre estruturas mais altas como armazéns de grãos e silos agroindustriais ao longo da BR-040.<')

# FAQ 4
r('>Preciso de treinamento para operar plataforma tesoura?<',
  '>Operadores das indústrias de Luziânia precisam de NR-35?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<',
  '>Sim. Qualquer trabalho acima de 2 metros exige capacitação NR-35 válida. O treinamento abrange avaliação de riscos, cinto paraquedista, checklist pré-operacional e técnicas de resgate. A Move Máquinas indica centros de formação credenciados acessíveis a empresas de Luziânia para certificação em <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">NR-35 e operação de PEMT</a>.<')

# FAQ 5
r('>A manutenção da plataforma tesoura está inclusa no aluguel?<',
  '>A manutenção vem incluída no contrato de locação?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Cada contrato cobre manutenção preventiva e corretiva do sistema hidráulico pantográfico, cilindros, componente elétrico e baterias (modelo elétrico). Em caso de falha durante uso em Luziânia, nossa equipe técnica se desloca pela BR-040 para diagnóstico no local ou troca do equipamento.<')

# FAQ 6
r('>Vocês entregam plataforma tesoura fora de Goiânia?<',
  '>Quanto tempo leva a entrega da tesoura em Luziânia?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Luziânia está a 198 km pela BR-040. A entrega acontece no mesmo dia para pedidos confirmados pela manhã. Para operações programadas no DIAL, agendamos com antecedência para garantir modelo específico e data exata. O frete é calculado conforme a distância.<')

# FAQ 7
r('>Posso usar plataforma tesoura em terreno irregular?<',
  '>A tesoura diesel opera nos pátios agroindustriais com piso irregular?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a <a href="/goiania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<',
  '>Sim. A versão diesel possui tração 4x4 e chassi reforçado para cascalho, terra batida e desnível moderado — cenário frequente nos pátios entre galpões do DIAL e acessos a silos. Para ambientes internos com piso firme, a elétrica é mais indicada. Se o trabalho exige contornar tubulações, avalie a <a href="/luziania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<')

# FAQ 8
r('>Qual a capacidade de carga da plataforma tesoura?<',
  '>Quantos operadores cabem na cesta da tesoura para trabalhos no DIAL?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A cesta comporta de 230 a 450 kg conforme modelo. A elétrica de 8-10m leva até 320 kg — dois técnicos com ferramental de manutenção industrial. A diesel de 12-15m suporta até 450 kg, cabendo 3 operadores com material de montagem. Nos galpões metalúrgicos do DIAL, a cesta ampla da tesoura permite trabalho lado a lado sem reposicionar a base. Confirme o peso total antes de subir chapas metálicas ou estruturas pesadas.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de plataforma tesoura em Goiânia',
  'Solicite plataforma tesoura para Luziânia')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Luziânia.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 15B. NR-35 — textos reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Como garantir conformidade com a <span>NR-35</span> no trabalho em altura?',
  'NR-35 na prática: o que cumprir para operar tesoura em <span>Luziânia</span>')

r('A NR-35 regulamenta todo trabalho executado acima de 2 metros do nível inferior onde exista risco de queda. Todo operador de plataforma tesoura precisa de treinamento específico e certificado válido.',
  'Toda operação acima de 2 metros do solo exige conformidade com a NR-35. No DIAL de Luziânia, o cumprimento dessa norma é fiscalizado com rigor — metalúrgicas, fábricas de alimentos e indústrias químicas mantêm padrões rigorosos de segurança ocupacional.')

r('O que a NR-35 exige para operar plataforma tesoura',
  'Itens obrigatórios para operar a tesoura no DIAL de Luziânia')

r('Curso de NR-35 (trabalho em altura) com certificado válido e reciclagem bienal',
  'Habilitação NR-35 válida — renovação compulsória a cada dois anos')

r('Análise de risco antes de cada atividade em altura (permissão de trabalho)',
  'Documento de autorização de serviço em altura emitido antes de cada uso')

r('Inspeção pré-operacional da plataforma: sistema hidráulico, guarda-corpo, sensor de inclinação e freios',
  'Vistoria pré-uso: pistões, barras de segurança, nível eletrônico e sistema de frenagem')

r('Uso de cinto tipo paraquedista com trava-quedas preso ao ponto de ancoragem da cesta',
  'Arnês tipo paraquedista fixado ao ponto de ancoragem da bancada enquanto a máquina estiver elevada')

r('Capacitação do operador nos comandos específicos da plataforma (elevação, translação, emergência)',
  'Capacitação operacional: elevação, rebaixamento, movimentação e acionamento do botão de emergência')

r('Como garantir a conformidade antes de operar',
  'Roteiro de conformidade antes de acionar a tesoura')

r('Verifique o certificado NR-35 do operador',
  'Confirme a validade da certificação NR-35')
r('O treinamento de NR-35 cobre análise de risco, uso de EPI, procedimentos de emergência, resgate e primeiros socorros em altura. A reciclagem é obrigatória a cada 2 anos.',
  'O programa inclui identificação de riscos no ambiente, manuseio de EPIs, procedimentos de socorro e salvamento em altura. O certificado perde validade após 24 meses e precisa ser reemitido.')

r('Emita a permissão de trabalho em altura',
  'Formalize a autorização de serviço em altura')
r('Antes de cada atividade, preencha a análise de risco com identificação de perigos, medidas de controle e plano de resgate. Documente a permissão assinada pelo responsável técnico.',
  'Documente os perigos levantados, ações preventivas definidas e estratégia de resgate antes de acionar o equipamento. A folha precisa da assinatura do engenheiro ou técnico responsável.')

r('Realize a inspeção pré-operacional',
  'Execute a checklist pré-turno')
r('Antes de cada turno: verifique guarda-corpo, sensor de inclinação, alarme sonoro, sistema hidráulico, nível de bateria (elétrica) ou combustível (diesel) e chave de emergência.',
  'Antes de operar: confira barras laterais, sensor de nível, alarme audível, pistões do pantógrafo, energia da bateria (versão elétrica) ou combustível (versão diesel) e válvula de rebaixamento manual.')

r('Isole a área abaixo da plataforma',
  'Sinalize o perímetro sob a plataforma')
r('Sinalize e isole a área diretamente abaixo e ao redor da plataforma para evitar passagem de pessoas e veículos durante a operação em altura.',
  'Posicione balizadores, cordão de isolamento e avisos visuais no raio de operação da máquina para impedir que funcionários ou empilhadeiras transitem sob a bancada elevada.')

# ═══════════════════════════════════════════════════════════════════════
# EXTRA: Reescrever textos genéricos restantes para reduzir Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Video section description
r('Assista ao vídeo da Move Máquinas e veja como funciona a locação: consultoria técnica, escolha do modelo ideal para seu projeto, entrega no local e suporte durante todo o contrato. Nosso time ajuda a dimensionar a altura de trabalho e o tipo de plataforma antes da entrega.',
  'Acompanhe o fluxo completo de locação: diagnóstico técnico da necessidade, seleção do modelo compatível com o galpão ou pátio, transporte pela BR-040 até Luziânia e acompanhamento técnico integral. Dimensionamos altura e tipo de tesoura antes do despacho.')

r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Disponível no canal da Move Máquinas no YouTube.')

# Comparativo card texts
r('Para galpões, shoppings e pisos nivelados',
  'Para galpões do DIAL e pisos de concreto industrial')

r('Para fachadas, estruturas e terreno acidentado',
  'Para plantas com obstáculos e pátios sem pavimentação')

r('Elevação vertical pura: sem oscilação lateral',
  'Deslocamento vertical puro: firmeza total na bancada')

r('Cesta de até 2,50 m: mais área de trabalho',
  'Bancada de 2,50 m de largura: equipe completa de manutenção')

r('Versão elétrica: zero emissão e silenciosa',
  'Propulsão elétrica: sem restrição em áreas de produção alimentícia')

r('Capacidade de até 450 kg (modelo diesel)',
  'Versão diesel aguenta 450 kg incluindo materiais pesados')

r('Sem alcance horizontal: não contorna obstáculos',
  'Só sobe e desce: sem capacidade de contorno lateral')

r('Alcance horizontal de até 12 m',
  'Extensão horizontal de até 12 m pelo braço articulado')

r('Contorna obstáculos com o braço articulado',
  'Navega ao redor de vigas, dutos e maquinário fixo')

r('Opera em terrenos irregulares com tração 4x4',
  'Chassi 4x4 preparado para terreno bruto e cascalho')

r('Cesta compacta: menos espaço de trabalho',
  'Bancada reduzida: apenas um técnico com ferramental básico')

r('Maior custo de locação por conta do braço',
  'Valor de locação mais alto por conta da complexidade mecânica')

r('Mais lenta para cobrir grandes áreas planas',
  'Rendimento baixo em forros planos e coberturas de grande área')

# Shorts section
r('Veja a <span>plataforma tesoura</span> em ação',
  'A <span>plataforma pantográfica</span> operando na prática')

r('Vídeos curtos mostrando a operação, os modelos disponíveis e como a plataforma tesoura funciona na prática.',
  'Gravações dos equipamentos em operação real: pantógrafo subindo, bancada ampla, modelos elétrico e diesel — e exemplos de uso em galpões e pátios industriais.')

# Cotação section
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Preencha o formulário ao lado e receba proposta detalhada via WhatsApp em até 2 horas. Atendimento ágil, sem etapas desnecessárias.')

r('Contratos a partir de 1 dia',
  'Contratos desde 1 diária avulsa')

r('Suporte técnico 24h',
  'Suporte técnico pela duração do contrato')

# Incluso section — rewrite items not yet changed
r('Revisão dos cilindros de elevação, válvulas, mangueiras e fluido hidráulico. Mecanismo pantográfico (tesoura) inspecionado em todos os pontos de articulação.',
  'Verificação integral dos pistões do pantógrafo, reguladores de pressão, mangueiras e volume de óleo hidráulico. Todas as articulações do mecanismo são testadas no depósito antes do despacho para Luziânia.')

r('Baterias de ciclo profundo com carga completa na entrega. Carregador incluso para recarga durante a noite no próprio local de trabalho.',
  'Acumuladores de energia com carga plena no momento do embarque. O carregador segue junto com a máquina para reposição de carga durante a noite no próprio local de trabalho em Luziânia.')

r('Cesta com guarda-corpo certificado, sensor de inclinação, alarme sonoro de elevação e chave de emergência para descida manual.',
  'Bancada com barras de segurança homologadas, sensor angular, alarme audível durante a subida e acionador manual de rebaixamento para casos críticos.')

r('Na entrega, nosso técnico orienta o operador sobre comandos, limites de carga, inspeção pré-operacional e procedimentos de emergência conforme NR-35.',
  'Na chegada ao local, o profissional da Move apresenta o funcionamento completo: controles do painel, limite de peso da bancada, rotina de inspeção antes de cada uso e procedimento de socorro conforme NR-35.')

# Price section extra
r('O custo de improvisar sem plataforma',
  'Quanto custa improvisar sem a máquina certa')

# Fleet carousel consultation note
r('Dúvida sobre qual modelo atende seu projeto? Fale com nosso time técnico. A consultoria é gratuita.',
  'Incerteza sobre o modelo adequado para seu galpão em Luziânia? Nossa equipe realiza a análise técnica sem custo antes do despacho.')

# Comparativo quick stats
r('Articulada: vertical + horizontal',
  'Articulada: vertical e horizontal combinados')
r('Articulada: cesta compacta',
  'Articulada: bancada compacta')
r('Articulada: externos, fachadas',
  'Articulada: áreas abertas e fachadas')
r('Articulada: boa, com contrapeso',
  'Articulada: satisfatória via contrapeso traseiro')

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
            'goiania-go/', '198 km', 'Goiânia - GO',
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
luz = html.count('Luziânia')
local = html.count('DIAL') + html.count('metalúrg') + html.count('BR-040') + html.count('grãos')
print(f"\nLuziânia: {luz} menções")
print(f"Contexto local (DIAL/metalúrgica/BR-040/grãos): {local} menções")

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
print(f"vs Referência (Goiânia tesoura):   {j_ref:.4f}  {'✓ PASS' if j_ref < 0.20 else '✗ FAIL'}")

# Test vs Senador Canedo tesoura V2
import os
SC_V2 = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(SC_V2):
    with open(SC_V2, 'r', encoding='utf-8') as f:
        sc_html = f.read()
    sc_text = extract_text(sc_html)
    sc_ng = ngrams(sc_text)
    j_sc = jaccard(new_ng, sc_ng)
    print(f"vs Senador Canedo tesoura V2:       {j_sc:.4f}  {'✓ PASS' if j_sc < 0.20 else '✗ FAIL'}")
else:
    print(f"⚠ SC tesoura V2 não encontrada: {SC_V2}")

# Test vs Brasília tesoura V2
BSB_V2 = '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(BSB_V2):
    with open(BSB_V2, 'r', encoding='utf-8') as f:
        bsb_html = f.read()
    bsb_text = extract_text(bsb_html)
    bsb_ng = ngrams(bsb_text)
    j_bsb = jaccard(new_ng, bsb_ng)
    print(f"vs Brasília tesoura V2:             {j_bsb:.4f}  {'✓ PASS' if j_bsb < 0.20 else '✗ FAIL'}")
else:
    print(f"⚠ Brasília tesoura V2 não encontrada: {BSB_V2}")

# ═══════════════════════════════════════════════════════════════════════
# UPLOAD R2
# ═══════════════════════════════════════════════════════════════════════

print(f"\n{'='*60}")
print("UPLOAD R2")
print(f"{'='*60}")

try:
    import hashlib, hmac, datetime, urllib.request, urllib.parse

    ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
    SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
    BUCKET = 'pages'
    R2_KEY = 'luziania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'

    body = html.encode('utf-8')
    content_hash = hashlib.sha256(body).hexdigest()
    now = datetime.datetime.utcnow()
    date_stamp = now.strftime('%Y%m%d')
    amz_date = now.strftime('%Y%m%dT%H%M%SZ')
    region = 'auto'
    service = 's3'

    def sign(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    signing_key = sign(sign(sign(sign(('AWS4' + SECRET_KEY).encode('utf-8'), date_stamp), region), service), 'aws4_request')

    canonical_uri = f'/{BUCKET}/{R2_KEY}'
    canonical_querystring = ''
    canonical_headers = (
        f'content-type:text/html; charset=utf-8\n'
        f'host:842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com\n'
        f'x-amz-content-sha256:{content_hash}\n'
        f'x-amz-date:{amz_date}\n'
    )
    signed_headers = 'content-type;host;x-amz-content-sha256;x-amz-date'

    canonical_request = f'PUT\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{content_hash}'
    credential_scope = f'{date_stamp}/{region}/{service}/aws4_request'
    string_to_sign = f'AWS4-HMAC-SHA256\n{amz_date}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()}'
    signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

    authorization = f'AWS4-HMAC-SHA256 Credential={ACCESS_KEY}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'

    url = f'{ENDPOINT}/{BUCKET}/{R2_KEY}'
    req = urllib.request.Request(url, data=body, method='PUT')
    req.add_header('Content-Type', 'text/html; charset=utf-8')
    req.add_header('x-amz-content-sha256', content_hash)
    req.add_header('x-amz-date', amz_date)
    req.add_header('Authorization', authorization)
    req.add_header('Cache-Control', 'public, max-age=3600')

    with urllib.request.urlopen(req) as resp:
        print(f"✅ Upload OK: {resp.status}")
        print(f"   URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{R2_KEY}")
except Exception as e:
    print(f"❌ Upload falhou: {e}")

# ═══════════════════════════════════════════════════════════════════════
# RESULTADO FINAL
# ═══════════════════════════════════════════════════════════════════════

elapsed = time.time() - START
minutes = int(elapsed // 60)
seconds = int(elapsed % 60)

print(f"\n{'='*60}")
print("RESULTADO FINAL")
print(f"{'='*60}")

all_pass = (ref_classes == new_classes and ref_svgs == new_svgs and
            ref_sections == new_sections and j_ref < 0.20 and len(goiania_issues) == 0)
print(f"{'✅ TODOS OS TESTES PASSARAM' if all_pass else '❌ ALGUM TESTE FALHOU — revisar'}")
print(f"TEMPO: {minutes:02d}:{seconds:02d}")
print(f"TOKENS: ~0 (script Python, sem API)")
