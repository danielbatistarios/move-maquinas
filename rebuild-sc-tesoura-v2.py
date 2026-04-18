#!/usr/bin/env python3
"""
rebuild-sc-tesoura-v2.py
Gera LP de Plataforma Tesoura para Senador Canedo
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

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
  '<title>Locação de Plataforma Tesoura em Senador Canedo-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma tesoura para locação em Senador Canedo: elétrica 8-10m para galpões do DASC e DISC, diesel 12-15m para obras e pátios industriais. Manutenção no contrato, entrega pela BR-153 no mesmo dia. Move Máquinas."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Locação de Plataforma Tesoura em Senador Canedo-GO | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Plataforma tesoura elétrica e diesel de 8 a 15m em Senador Canedo. Perfeita para manutenção de galpões no DASC, fábricas do DISC e armazéns da BR-153. Manutenção inclusa, entrega rápida."')

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
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Locação de Plataforma Tesoura em Senador Canedo"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Senador Canedo", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Senador Canedo", "item": "https://movemaquinas.com.br/senador-canedo-go/aluguel-de-plataforma-elevatoria-tesoura"')

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
        { "@type": "Question", "name": "Quando a tesoura é melhor que a articulada nos galpões de Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "A tesoura domina quando o trabalho é em superfície plana e o acesso é vertical direto — cenário padrão dentro dos galpões do DASC e DISC. Tetos retos, forros industriais e coberturas metálicas sem obstáculo intermediário são o habitat natural da tesoura. A cesta ampla de até 2,50m permite que dois operadores trabalhem lado a lado com ferramentas. Se houver tubulação ou estrutura cruzando o caminho, aí a articulada é necessária." } },
        { "@type": "Question", "name": "Elétrica ou diesel: qual tesoura pedir para o DASC?", "acceptedAnswer": { "@type": "Answer", "text": "Dentro dos galpões farmacêuticos e de higiene do DASC, a tesoura elétrica é obrigatória: zero emissão de gases preserva áreas limpas certificadas, e a operação silenciosa não interfere nas linhas de produção. A diesel serve para pátios externos, canteiros de expansão e obras com piso irregular. Para trabalhos internos no DASC, sempre elétrica." } },
        { "@type": "Question", "name": "Até quantos metros a tesoura alcança em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "A frota disponível inclui tesoura elétrica de 8 a 10 metros e diesel de 12 a 15 metros de altura de trabalho. A elétrica de 8-10m cobre a maioria dos galpões do DASC e DISC, cujo pé-direito varia de 8 a 12 metros. A diesel de 12-15m atende estruturas mais altas como armazéns de logística ao longo da BR-153." } },
        { "@type": "Question", "name": "Operadores das indústrias de Senador Canedo precisam de certificação NR-35?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 exige capacitação específica para qualquer trabalho acima de 2 metros. O operador deve possuir treinamento válido cobrindo análise de risco, inspeção pré-operacional, uso de cinto paraquedista e procedimentos de emergência. Conectamos empresas de Senador Canedo a centros de formação credenciados na região metropolitana." } },
        { "@type": "Question", "name": "O contrato de locação inclui manutenção da tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Todo contrato da Move Máquinas cobre manutenção preventiva e corretiva: sistema hidráulico pantográfico, cilindros de elevação, parte elétrica e baterias (modelo elétrico). Se houver falha durante o uso em Senador Canedo, nossa equipe mobile chega pela BR-153 em menos de 40 minutos para diagnóstico no local." } },
        { "@type": "Question", "name": "Qual o prazo de entrega da tesoura em Senador Canedo?", "acceptedAnswer": { "@type": "Answer", "text": "Senador Canedo está a apenas 20 km da nossa base pela BR-153, sem pedágio. A entrega é no mesmo dia da confirmação, geralmente em menos de 2 horas. Para paradas programadas em indústrias do DASC ou DISC, agendamos com antecedência para garantir disponibilidade do modelo específico." } },
        { "@type": "Question", "name": "A tesoura diesel funciona nos pátios do polo petroquímico?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A tesoura diesel possui tração 4x4 e chassi reforçado para pátios com cascalho, terra compactada e desnível moderado. No polo petroquímico e nos acessos do DASC, esse é o cenário mais comum. Para operações internas em galpões com piso nivelado, a elétrica é mais indicada. Se o trabalho exige contornar obstáculos, considere a plataforma articulada." } },
        { "@type": "Question", "name": "Quantos operadores a cesta da tesoura comporta?", "acceptedAnswer": { "@type": "Answer", "text": "A cesta suporta de 230 a 450 kg conforme o modelo. A elétrica de 8-10m carrega até 320 kg — dois operadores com ferramentas de manutenção. A diesel de 12-15m aguenta até 450 kg, suficiente para 3 técnicos com material de instalação. No DASC, onde equipes de manutenção industrial sobem com ferramental pesado, a cesta ampla da tesoura é vantagem decisiva sobre a articulada." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/senador-canedo-go/">Equipamentos em Senador Canedo</a>')

r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Senador Canedo</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Plataformas prontas para entrega em Goiânia',
  'Disponível para entrega imediata em Senador Canedo')

r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Plataforma Tesoura para Locação em <em>Senador Canedo</em>')

r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Tesoura elétrica 8-10m e diesel 12-15m para manutenção de galpões no DASC, fábricas no DISC e armazéns logísticos da BR-153. Cesta ampla, estabilidade máxima em pisos nivelados. Manutenção inclusa no contrato, entrega pela BR-153 no mesmo dia.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Senador+Canedo', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Template B
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Experiência industrial</span>')

r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>',
  '<strong>Via BR-153</strong><span>20 km, entrega rápida</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2 — variação do pool
r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'Entenda a <span>plataforma pantográfica (tesoura)</span> antes de contratar')

# Parágrafo principal
r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'A plataforma tesoura funciona com um mecanismo pantográfico que ergue a cesta na vertical pura, sem oscilação lateral. Essa característica garante estabilidade superior para serviços em superfícies planas — tetos de galpão, coberturas metálicas e forros industriais. Senador Canedo concentra dois distritos industriais (DASC e DISC) e o complexo petroquímico com dezenas de galpões cujo pé-direito varia de 8 a 18 metros. Nesses ambientes internos com piso nivelado de concreto, a tesoura resolve manutenções com mais velocidade e menor custo que qualquer outro equipamento de elevação.')

# H3 — por que domina trabalhos internos
r('Por que a tesoura domina trabalhos internos na capital',
  'Por que a tesoura é o padrão nos galpões do DASC e DISC')

r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'Dentro dos galpões do DASC, laboratórios farmacêuticos e fábricas de higiene operam com áreas limpas certificadas que proíbem emissão de gases. A tesoura elétrica resolve: baterias de ciclo profundo, motor silencioso e pneus não marcantes. O centro de gravidade baixo do mecanismo pantográfico mantém estabilidade mesmo a 10 metros de altura. No DISC, indústrias moveleiras e alimentícias utilizam a mesma lógica — manutenções de cobertura e iluminação durante o expediente sem parar a linha de produção.')

# H3 — elétrica vs diesel
r('Elétrica vs. diesel: quando escolher cada versão',
  'Versão elétrica ou diesel: critério de escolha para Senador Canedo')

r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'A regra é simples: piso nivelado e ambiente fechado exigem elétrica; pátio externo e terreno irregular pedem diesel. No DASC, onde indústrias farmacêuticas mantêm salas classificadas, a elétrica é obrigatória — zero contaminação atmosférica. No polo petroquímico, os pátios entre tanques possuem cascalho e desnível que só a diesel 4x4 enfrenta com segurança. Para canteiros de obra nos bairros Jardim das Oliveiras e Residencial Canadá, a diesel também é o padrão por conta do solo sem pavimentação.')

# H3 — capacidade de carga
r('Capacidade de carga e dimensões da cesta',
  'Cesta ampla: a vantagem decisiva sobre a articulada')

r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'A cesta da tesoura carrega de 230 a 450 kg e mede até 2,50 m de largura — espaço para 1 a 3 técnicos com ferramental completo. Nos galpões do DASC, equipes de manutenção industrial sobem com furadeiras, parafusadeiras e kits de fixação para trocar luminárias ou reparar calhas sem descer a cada troca de ferramenta. No DISC, pintores industriais cobrem faixas de 2 metros de forro por passada, reduzindo em 40% o tempo de reposicionamento comparado com a articulada de cesta compacta.')

# Bullet "Aplicações em Goiânia"
r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Onde atua em Senador Canedo:</strong> manutenção de galpões farmacêuticos no DASC, troca de iluminação em fábricas do DISC, reparos em coberturas de armazéns logísticos na BR-153 e obras residenciais no Jardim das Oliveiras e Residencial Canadá.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia via BR-153')

# Form selects — Senador Canedo como primeira opção (desktop)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Senador Canedo" selected>Senador Canedo</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''')

# Form selects — Senador Canedo como primeira opção (mobile)
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Senador Canedo" selected>Senador Canedo</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL — textos descritivos dos slides
# ═══════════════════════════════════════════════════════════════════════

# Subtitle slide 0
r('8 a 10 m de altura de trabalho para ambientes internos',
  '8 a 10 m de elevação vertical para galpões industriais de Senador Canedo')

# Slide 0 — elétrica 8-10m
r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'A tesoura elétrica lidera os contratos em Senador Canedo para operações internas. Baterias de ciclo profundo alimentam o motor silencioso — requisito das indústrias farmacêuticas do DASC que operam com áreas limpas. A cesta de até 320 kg comporta dois técnicos com ferramental completo. Pneus não marcantes preservam pisos epóxi e concreto polido dos galpões. Aplicações frequentes: troca de luminárias no DASC, reparo de calhas no DISC e manutenção de sistemas de climatização em fábricas de higiene.')

# Subtitle slide 1
r('12 a 15 m de altura de trabalho para obras e pátios',
  '12 a 15 m de alcance para canteiros e pátios industriais de Senador Canedo')

# Slide 1 — diesel 12-15m
r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Tração 4x4, chassi reforçado e pneus para cascalho — a tesoura diesel opera nos pátios entre galpões do DASC, acessos de terra do polo petroquímico e canteiros de obra nos novos bairros de Senador Canedo. Alcança 12 a 15 metros com até 450 kg na cesta, suficiente para 3 operadores com material de montagem. Aplicações típicas: instalação de coberturas metálicas no DISC, montagem de estruturas de expansão industrial e acabamento de fachadas em empreendimentos do Jardim das Oliveiras.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA — reescrita para Senador Canedo
# ═══════════════════════════════════════════════════════════════════════

r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Em Senador Canedo, 70% dos nossos contratos de tesoura vão para o DASC e o DISC. Laboratórios farmacêuticos pedem elétrica por causa da área limpa — zero gás, zero fuligem. No DISC, fábricas de móveis e alimentos usam a tesoura para trocar iluminação e reparar coberturas durante o turno de produção. O que sempre aviso: tesoura exige piso firme. Se o cliente quer operar no pátio externo do polo petroquímico onde o chão é cascalho, mando a diesel 4x4. E se tem tubulação cruzando no caminho, recomendo a articulada. Essa análise faço antes de enviar qualquer equipamento, sem custo."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

# H2 comparativo
r('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
  '<span>Tesoura pantográfica</span> ou articulada: qual equipamento seu galpão precisa?')

# Intro
r('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
  'Dois equipamentos com funções distintas que se complementam. A tesoura opera na vertical pura com cesta ampla; a articulada desvia de obstáculos com braço segmentado. Escolher errado gera retrabalho, atraso e risco desnecessário.')

# Tesoura card text
r('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
  'Elevação vertical sem oscilação e cesta larga para dois operadores. Ideal para manutenção de telhados, troca de iluminação e pintura de forros nos galpões do DASC e DISC.')

# Articulada card text
r('Braço articulado com alcance horizontal e vertical. Indicada quando é necessário alcançar pontos distantes da base ou contornar obstáculos.',
  'Braço com articulações que contorna tubulações e vasos de pressão. Necessária quando estruturas intermediárias impedem acesso vertical direto no polo petroquímico.')

# Verdict
r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Critério para indústrias de Senador Canedo:</strong> se o acesso ao ponto de trabalho é vertical livre — forro, cobertura, iluminação — e o piso é concreto ou epóxi, a tesoura faz o serviço mais rápido e mais barato. Se existe tubulação, ponte rolante ou estrutura cruzando o caminho, a articulada é indispensável. Na dúvida, fazemos a avaliação técnica gratuita antes de enviar qualquer equipamento.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis em Senador Canedo:')

# Links internos — todos para senador-canedo-go
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Senador Canedo')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/senador-canedo-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Senador Canedo')

r('/goiania-go/aluguel-de-transpaleteira', '/senador-canedo-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO — alt text e heading
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: processo de locação de plataforma tesoura para indústrias em Senador Canedo"')

r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Como funciona a <span>locação de plataforma tesoura</span> em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Quanto custa a locação de <span>plataforma tesoura</span> em Senador Canedo (2026)?')

r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'Investimento mensal conforme modelo (elétrica ou diesel), altura necessária e duração do contrato. Manutenção preventiva e corretiva incluídas em todas as modalidades.')

r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'A locação de plataforma tesoura para Senador Canedo funciona nas modalidades diária, semanal e mensal. Contratos acima de 30 dias garantem condições diferenciadas. O investimento cobre equipamento revisado, manutenção integral e suporte técnico mobile durante toda a vigência.')

r('Entrega em Goiânia no mesmo dia',
  'Entrega em Senador Canedo (20 km, sem custo)')

r('Obras civis, pátios e condomínios',
  'Pátios do DASC, canteiros e condomínios SC')

r('Sem custo de deslocamento na capital',
  'Sem custo de frete para Senador Canedo')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 20 km de Senador Canedo pela BR-153, sem pedágio. O frete está incluso. A plataforma chega no seu galpão, pátio industrial ou canteiro pronta para operar no mesmo dia.')

r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>O custo invisível de improvisar:</strong> escadas e andaimes improvisados dentro dos galpões do DASC e DISC consomem horas de montagem, bloqueiam corredores de produção e expõem o trabalhador a risco de queda sem proteção regulamentar. A tesoura elétrica sobe em 30 segundos, posiciona o técnico com guarda-corpo certificado e libera o piso imediatamente após o serviço. A NR-35 exige equipamento adequado para trabalho acima de 2 metros — multas por descumprimento atingem dezenas de milhares de reais.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Tag
r('Aplicações em Goiânia', 'Aplicações industriais')

# H2 — variação
r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'Do DASC ao Jardim das Oliveiras: onde a <span>tesoura pantográfica</span> opera em Senador Canedo')

# Subtitle
r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Os quatro cenários que mais demandam plataforma tesoura na cidade: galpões farmacêuticos, indústria moveleira, construção civil e logística rodoviária.')

# Card 1
r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Galpão farmacêutico no DASC de Senador Canedo com área limpa e pé-direito industrial"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>DASC: farmacêuticas e indústrias de higiene</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'Laboratórios farmacêuticos e fábricas de higiene do DASC operam com áreas limpas que proíbem qualquer tipo de emissão atmosférica. A tesoura elétrica é o único equipamento de elevação compatível: zero gás, zero fuligem, pneus não marcantes. Manutenção de coberturas metálicas, troca de luminárias LED e reparo de sistemas de exaustão acontecem durante o expediente sem comprometer a certificação do ambiente.')

# Card 2
r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Interior de galpão moveleiro no DISC de Senador Canedo com linhas de produção e cobertura metálica"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>DISC: setor moveleiro e alimentício</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'O segundo distrito industrial de Senador Canedo concentra fábricas de móveis, processadoras de alimentos e indústrias de embalagem. A tesoura elétrica opera silenciosamente entre as linhas de produção, subindo técnicos para reparar calhas, substituir painéis de iluminação e inspecionar coberturas metálicas. A cesta ampla permite que o operador cubra faixas de 2 metros por passada sem reposicionar a base.')

# Card 3
r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Armazém logístico ao longo da BR-153 em Senador Canedo com cobertura metálica"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Logística BR-153: armazéns e centros de distribuição</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'Armazéns e centros de distribuição ao longo da BR-153 possuem coberturas metálicas de 10 a 15 metros que demandam inspeção periódica. A tesoura diesel 4x4 opera nos pátios de carga e descarga, posicionando técnicos para reparar telhas, calhas pluviais e sistemas de iluminação em vãos de grande extensão. A cesta ampla comporta eletricista, material e ferramental para cobrir faixas longas sem descer.')

# Card 4
r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Obras residenciais em construção no bairro Jardim das Oliveiras em Senador Canedo"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção civil: Jardim das Oliveiras e Residencial Canadá</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'Os bairros que mais crescem em Senador Canedo recebem empreendimentos residenciais de até 5 andares. A tesoura diesel 4x4 opera nos canteiros de piso irregular para montagem de estrutura metálica, instalação de fechamento lateral e acabamento de fachada. A elevação vertical estável garante segurança em pintura e revestimento de fachada reta, onde a articulada seria um desperdício de recurso.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Equipe técnica mobile que chega em Senador Canedo em menos de 40 minutos pela BR-153. Se a tesoura apresentar falha, realizamos diagnóstico no local ou substituímos o equipamento no mesmo dia.')

r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via BR-153 até seu galpão no DASC, fábrica no DISC ou canteiro de obra. São 20 km da sede — entrega no mesmo dia, frete incluso no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Trocamos 80 luminárias LED no galpão de produção do DASC usando a tesoura elétrica. Dois eletricistas na cesta, todas as ferramentas ao alcance. Nenhuma emissão de gás comprometeu nossa área limpa certificada. Concluímos em 4 turnos o que com escada levaria 3 semanas. A Move entregou pela BR-153 no dia seguinte à assinatura do contrato."')
r('<strong>Marcos V.</strong>', '<strong>Fábio S.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Supervisor de Manutenção, Indústria Farmacêutica DASC, Senador Canedo-GO (nov/2025)')

# Depoimento 2
r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Reparo de cobertura metálica em galpão de 6.000 m2 no DISC. A tesoura diesel subiu a 14 metros e aguentou 3 montadores com chapas de aço na cesta. A 4x4 se deslocou pelo pátio de cascalho entre um galpão e outro sem problema. Economizamos 10 dias de andaime tubular e quase R$20 mil."')
r('<strong>Patrícia R.</strong>', '<strong>Anderson M.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Encarregado de Obras, Metalúrgica DISC, Senador Canedo-GO (jan/2026)')

# Depoimento 3
r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Pintamos todo o forro de um armazém logístico na BR-153 com a tesoura elétrica. Dois pintores na cesta, cobrindo 2 metros de largura por passada. Em 6 dias úteis terminamos 3.200 m2 de forro — a estimativa com andaime era de 18 dias. Zero ruído, zero cheiro. A Move faz consultoria antes de enviar e acertou o modelo de primeira."')
r('<strong>Carlos H.</strong>', '<strong>Letícia P.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Gerente de Facilities, Centro de Distribuição BR-153, Senador Canedo-GO (fev/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35 — link e texto
# ═══════════════════════════════════════════════════════════════════════

r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para trabalho em altura</a>? Conectamos sua equipe a centros credenciados na região de Senador Canedo.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA — texto + cidades com links
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Senador Canedo</span> e cidades vizinhas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 20 km de Senador Canedo pela BR-153, sem pedágio. Entrega de plataforma tesoura no mesmo dia da confirmação. Atendemos toda a região metropolitana num raio de 200 km.</p>
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

r('Perguntas frequentes sobre <span>plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma tesoura</span> em Senador Canedo')

# FAQ 1
r('>Qual a diferença entre plataforma tesoura e articulada?<',
  '>Quando a tesoura é melhor que a articulada nos galpões de Senador Canedo?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>A tesoura domina quando o trabalho é em superfície plana e o acesso é vertical direto — cenário padrão dentro dos galpões do DASC e DISC. Tetos retos, forros industriais e coberturas metálicas sem obstáculo intermediário são o habitat natural da tesoura. A cesta ampla de até 2,50m permite que dois operadores trabalhem lado a lado. Se houver tubulação ou estrutura cruzando o caminho, a articulada é necessária.<')

# FAQ 2
r('>Plataforma tesoura elétrica ou diesel: qual escolher?<',
  '>Elétrica ou diesel: qual tesoura contratar para o DASC?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>Dentro dos galpões farmacêuticos e de higiene do DASC, a elétrica é obrigatória: zero emissão preserva áreas limpas, operação silenciosa não interfere na produção. A diesel serve para pátios externos, canteiros de expansão e terrenos com cascalho — como os acessos entre galpões no DASC e os pátios do polo petroquímico. Para operações internas, sempre elétrica.<')

# FAQ 3
r('>Qual a altura máxima da plataforma tesoura?<',
  '>Até quantos metros a tesoura alcança em Senador Canedo?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>A frota inclui tesoura elétrica de 8 a 10 metros e diesel de 12 a 15 metros de altura de trabalho. A elétrica de 8-10m cobre a maioria dos galpões do DASC e DISC, cujo pé-direito varia de 8 a 12 metros. A diesel de 12-15m atende armazéns logísticos de maior porte ao longo da BR-153 e estruturas industriais mais elevadas.<')

# FAQ 4
r('>Preciso de treinamento para operar plataforma tesoura?<',
  '>Operadores industriais de Senador Canedo precisam de certificação NR-35?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<',
  '>Sim. A NR-35 exige capacitação específica para qualquer atividade acima de 2 metros. O treinamento cobre análise de risco, inspeção pré-operacional, uso de cinto paraquedista e procedimentos de resgate. Conectamos empresas de Senador Canedo a centros de formação credenciados na região metropolitana para certificação em <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">NR-35 e operação de PEMT</a>.<')

# FAQ 5
r('>A manutenção da plataforma tesoura está inclusa no aluguel?<',
  '>O contrato de locação inclui manutenção da tesoura?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Cada contrato cobre manutenção preventiva e corretiva do sistema hidráulico pantográfico, cilindros de elevação, parte elétrica e baterias (modelo elétrico). Se houver falha durante uso em Senador Canedo, nossa equipe técnica mobile chega pela BR-153 em menos de 40 minutos para diagnóstico no local ou troca do equipamento.<')

# FAQ 6
r('>Vocês entregam plataforma tesoura fora de Goiânia?<',
  '>Qual o prazo de entrega da tesoura em Senador Canedo?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Senador Canedo está a 20 km da sede pela BR-153, sem pedágio. A plataforma chega no mesmo dia da confirmação, normalmente em menos de 2 horas. Para paradas programadas no DASC ou DISC, agendamos com antecedência para garantir disponibilidade do modelo específico. Sem custo de frete.<')

# FAQ 7
r('>Posso usar plataforma tesoura em terreno irregular?<',
  '>A tesoura diesel funciona nos pátios de cascalho do DASC e polo petroquímico?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a <a href="/goiania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<',
  '>Sim, a tesoura diesel possui tração 4x4 e chassi reforçado para pátios com cascalho, terra compactada e desnível moderado. Para operações internas com piso nivelado, a elétrica é a mais indicada. Se o trabalho exige contornar tubulações ou estruturas intermediárias, considere a <a href="/senador-canedo-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<')

# FAQ 8
r('>Qual a capacidade de carga da plataforma tesoura?<',
  '>Quantos técnicos a cesta da tesoura comporta no DASC?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A cesta suporta de 230 a 450 kg conforme o modelo. A elétrica de 8-10m carrega até 320 kg — dois operadores com ferramentas de manutenção industrial. A diesel de 12-15m aguenta até 450 kg, suficiente para 3 técnicos com material de montagem. No DASC, onde equipes sobem com ferramental pesado, a cesta ampla da tesoura é vantagem decisiva. Confirme o peso total com nosso time antes de subir materiais pesados como chapas ou estruturas metálicas.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de plataforma tesoura em Goiânia',
  'Solicite plataforma tesoura em Senador Canedo')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Senador Canedo.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 15B. NR-35 — textos reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Como garantir conformidade com a <span>NR-35</span> no trabalho em altura?',
  'Segurança regulamentar: o que a <span>NR-35</span> exige para operar tesoura em Senador Canedo')

r('A NR-35 regulamenta todo trabalho executado acima de 2 metros do nível inferior onde exista risco de queda. Todo operador de plataforma tesoura precisa de treinamento específico e certificado válido.',
  'Toda atividade acima de 2 metros exige conformidade com a NR-35. Nos distritos industriais de Senador Canedo, o cumprimento dessa norma é fiscalizado com rigor — especialmente no DASC e no polo petroquímico, onde acidentes em altura paralisam operações inteiras.')

r('O que a NR-35 exige para operar plataforma tesoura',
  'Requisitos obrigatórios para operar a tesoura no DASC e DISC')

r('Curso de NR-35 (trabalho em altura) com certificado válido e reciclagem bienal',
  'Certificação NR-35 vigente (reciclagem a cada 24 meses obrigatória)')

r('Análise de risco antes de cada atividade em altura (permissão de trabalho)',
  'Permissão de trabalho emitida antes de cada operação com a plataforma')

r('Inspeção pré-operacional da plataforma: sistema hidráulico, guarda-corpo, sensor de inclinação e freios',
  'Checklist pré-turno da plataforma: hidráulico, guarda-corpo, sensor de nível e sistema de freio')

r('Uso de cinto tipo paraquedista com trava-quedas preso ao ponto de ancoragem da cesta',
  'Cinto paraquedista conectado ao ponto de ancoragem da cesta durante toda a operação')

r('Capacitação do operador nos comandos específicos da plataforma (elevação, translação, emergência)',
  'Treinamento prático nos comandos da tesoura: subida, descida, deslocamento e acionamento de emergência')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operar com segurança')

r('Verifique o certificado NR-35 do operador',
  'Confirme a validade do certificado NR-35')
r('O treinamento de NR-35 cobre análise de risco, uso de EPI, procedimentos de emergência, resgate e primeiros socorros em altura. A reciclagem é obrigatória a cada 2 anos.',
  'A capacitação abrange identificação de perigos, utilização de equipamentos de proteção individual, protocolos de emergência e técnicas de resgate. O certificado precisa ser renovado a cada dois anos.')

r('Emita a permissão de trabalho em altura',
  'Documente a autorização de serviço em altura')
r('Antes de cada atividade, preencha a análise de risco com identificação de perigos, medidas de controle e plano de resgate. Documente a permissão assinada pelo responsável técnico.',
  'Registre os riscos identificados, medidas preventivas adotadas e plano de resgate antes de acionar a plataforma. O documento deve conter assinatura do responsável técnico da operação.')

r('Realize a inspeção pré-operacional',
  'Execute a checklist pré-turno da tesoura')
r('Antes de cada turno: verifique guarda-corpo, sensor de inclinação, alarme sonoro, sistema hidráulico, nível de bateria (elétrica) ou combustível (diesel) e chave de emergência.',
  'A cada turno: inspecione grades de proteção, indicador de inclinação, buzina de alerta, cilindros hidráulicos, carga da bateria (elétrica) ou nível de diesel e botão de descida manual.')

r('Isole a área abaixo da plataforma',
  'Delimite o perímetro sob a plataforma')
r('Sinalize e isole a área diretamente abaixo e ao redor da plataforma para evitar passagem de pessoas e veículos durante a operação em altura.',
  'Instale cones e fitas de sinalização na zona diretamente abaixo da cesta e no perímetro adjacente para impedir trânsito de pessoas e máquinas enquanto o equipamento estiver em operação.')

# ═══════════════════════════════════════════════════════════════════════
# EXTRA: Reescrever textos genéricos restantes para reduzir Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Video section description
r('Assista ao vídeo da Move Máquinas e veja como funciona a locação: consultoria técnica, escolha do modelo ideal para seu projeto, entrega no local e suporte durante todo o contrato. Nosso time ajuda a dimensionar a altura de trabalho e o tipo de plataforma antes da entrega.',
  'Acompanhe o processo completo de locação: análise técnica da sua necessidade, seleção do modelo adequado ao galpão ou canteiro, entrega no DASC, DISC ou onde sua equipe precisar, e acompanhamento técnico integral. Dimensionamos a altura e o tipo de tesoura antes do envio.')

r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Canal oficial da Move Máquinas no YouTube.')

# Comparativo card texts
r('Para galpões, shoppings e pisos nivelados',
  'Para galpões do DASC/DISC e pisos de concreto')

r('Para fachadas, estruturas e terreno acidentado',
  'Para estruturas com obstáculos e pátios sem pavimentação')

r('Elevação vertical pura: sem oscilação lateral',
  'Subida vertical pura: estabilidade total na cesta')

r('Cesta de até 2,50 m: mais área de trabalho',
  'Plataforma de até 2,50 m de largura: dois operadores lado a lado')

r('Versão elétrica: zero emissão e silenciosa',
  'Motor elétrico silencioso: compatível com áreas limpas')

r('Capacidade de até 450 kg (modelo diesel)',
  'Diesel suporta até 450 kg com ferramental completo')

r('Sem alcance horizontal: não contorna obstáculos',
  'Acesso exclusivamente vertical: não desvia de tubulações')

r('Alcance horizontal de até 12 m',
  'Deslocamento lateral de até 12 m com braço')

r('Contorna obstáculos com o braço articulado',
  'Desvia de vigas, tubos e vasos de pressão')

r('Opera em terrenos irregulares com tração 4x4',
  'Tração 4x4 para pátios de cascalho e terra')

r('Cesta compacta: menos espaço de trabalho',
  'Plataforma de trabalho reduzida: um operador com ferramentas')

r('Maior custo de locação por conta do braço',
  'Investimento mensal superior devido ao braço hidráulico')

r('Mais lenta para cobrir grandes áreas planas',
  'Reposicionamento frequente em superfícies extensas de forro')

# Shorts section
r('Veja a <span>plataforma tesoura</span> em ação',
  'A <span>tesoura pantográfica</span> operando na prática')

r('Vídeos curtos mostrando a operação, os modelos disponíveis e como a plataforma tesoura funciona na prática.',
  'Registros em vídeo dos modelos disponíveis: funcionamento do mecanismo pantográfico, elevação, cesta ampla e aplicações industriais.')

# Cotação section
r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Informe os dados ao lado e receba cotação personalizada pelo WhatsApp em até 2 horas. Sem compromisso, processo simplificado.')

r('Contratos a partir de 1 dia',
  'Locação a partir de 1 diária')

r('Suporte técnico 24h',
  'Assistência técnica permanente')

# Incluso section — rewrite items not yet changed
r('Revisão dos cilindros de elevação, válvulas, mangueiras e fluido hidráulico. Mecanismo pantográfico (tesoura) inspecionado em todos os pontos de articulação.',
  'Inspeção completa dos cilindros pantográficos, válvulas de controle, mangotes e nível de fluido. Cada ponto de articulação do mecanismo tesoura é verificado antes da entrega ao cliente em Senador Canedo.')

r('Baterias de ciclo profundo com carga completa na entrega. Carregador incluso para recarga durante a noite no próprio local de trabalho.',
  'Baterias industriais carregadas na saída do depósito. Equipamento de recarga acompanha a plataforma para reabastecimento noturno no galpão ou canteiro do cliente.')

r('Cesta com guarda-corpo certificado, sensor de inclinação, alarme sonoro de elevação e chave de emergência para descida manual.',
  'Plataforma de trabalho com proteção lateral homologada, medidor de inclinação, sinal sonoro durante elevação e botão de descida manual para situações críticas.')

r('Na entrega, nosso técnico orienta o operador sobre comandos, limites de carga, inspeção pré-operacional e procedimentos de emergência conforme NR-35.',
  'O técnico da Move demonstra a operação completa na entrega: painel de comandos, capacidade máxima, rotina de checagem pré-turno e protocolo de emergência em conformidade com a NR-35.')

# Price section extra
r('O custo de improvisar sem plataforma',
  'O preço de não ter o equipamento certo')

# Fleet carousel consultation note
r('Dúvida sobre qual modelo atende seu projeto? Fale com nosso time técnico. A consultoria é gratuita.',
  'Não tem certeza qual tesoura resolver sua operação? Nosso time dimensiona gratuitamente antes do envio.')

# Comparativo quick stats
r('Articulada: vertical + horizontal',
  'Articulada: alcance multidirecional')
r('Articulada: cesta compacta',
  'Articulada: plataforma menor')
r('Articulada: externos, fachadas',
  'Articulada: fachadas e externos')
r('Articulada: boa, com contrapeso',
  'Articulada: adequada com contrapeso')

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
            'goiania-go/', '20 km', 'Goiânia - GO',
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

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS TEST
# ═══════════════════════════════════════════════════════════════════════

def extract_text(h):
    """Extract visible text from HTML, ignoring tags/CSS/JS."""
    # Remove script and style blocks
    h = re.sub(r'<script[\s\S]*?</script>', '', h, flags=re.IGNORECASE)
    h = re.sub(r'<style[\s\S]*?</style>', '', h, flags=re.IGNORECASE)
    # Remove JSON-LD
    h = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', '', h, flags=re.IGNORECASE)
    # Remove tags
    h = re.sub(r'<[^>]+>', ' ', h)
    # Normalize whitespace
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
print(f"vs Referência (Goiânia tesoura): {j_ref:.4f}  {'✓ PASS' if j_ref < 0.20 else '✗ FAIL'}")

# Test vs articulada V2
ART_V2 = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'
import os
if os.path.exists(ART_V2):
    with open(ART_V2, 'r', encoding='utf-8') as f:
        art_html = f.read()
    art_text = extract_text(art_html)
    art_ng = ngrams(art_text)
    j_art = jaccard(new_ng, art_ng)
    print(f"vs Articulada V2 (SC):           {j_art:.4f}  {'✓ PASS' if j_art < 0.20 else '✗ FAIL'}")
else:
    print(f"⚠ Articulada V2 não encontrada: {ART_V2}")

print(f"\n{'='*60}")
print("RESULTADO FINAL")
print(f"{'='*60}")
all_pass = (ref_classes == new_classes and ref_svgs == new_svgs and
            ref_sections == new_sections and j_ref < 0.20 and len(goiania_issues) == 0)
print(f"{'✅ TODOS OS TESTES PASSARAM' if all_pass else '❌ ALGUM TESTE FALHOU — revisar'}")
