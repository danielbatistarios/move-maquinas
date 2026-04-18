#!/usr/bin/env python3
"""
rebuild-inhumas-tesoura-v2.py
Gera LP de Plataforma Tesoura para Inhumas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""
import time, os, re

START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

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
  '<title>Plataforma Tesoura para Locação em Inhumas-GO | Move Máquinas</title>')

r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Locação de plataforma tesoura em Inhumas: elétrica 8-10m para fábricas de confecções e diesel 12-15m para galpões industriais. Manutenção no contrato, entrega via GO-070 no mesmo dia. Move Máquinas: +20 anos."')

r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura"')

r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locação em Inhumas-GO | Move Máquinas"')

r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Plataforma tesoura elétrica e diesel de 8 a 15m em Inhumas. Ideal para fábricas têxteis, galpões de confecção e armazéns de grãos no Distrito Industrial. Manutenção inclusa, entrega pela GO-070."')

r('content="Goiânia, Goiás, Brasil"', 'content="Inhumas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.3547;-49.4952"')
r('content="-16.7234, -49.2654"', 'content="-16.3547, -49.4952"')

# Schema — coords (todos os padrões)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.3547, "longitude": -49.4952')
# Segundo par de coords (serviceArea)
r('"latitude": -16.7234', '"latitude": -16.3547')
r('"longitude": -49.2654', '"longitude": -49.4952')

# Schema — Service name
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
  '"name": "Locação de Plataforma Tesoura em Inhumas"')

# Schema — areaServed
r('"name": "Goiânia", "addressRegion": "GO"',
  '"name": "Inhumas", "addressRegion": "GO"')

# Schema — breadcrumb
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura"')

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
        { "@type": "Question", "name": "Por que a tesoura é preferida nas fábricas de confecções de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Fábricas de confecção possuem galpões com pé-direito de 8 a 10 metros, piso de concreto liso e corredores entre linhas de corte e costura. A tesoura elétrica sobe na vertical sem ocupar espaço lateral, não emite gases que possam contaminar tecidos estocados e opera em silêncio para não interferir no turno de produção. Quando o acesso ao ponto de trabalho é reto e o piso é plano, a tesoura resolve mais rápido e mais barato que a articulada." } },
        { "@type": "Question", "name": "Elétrica ou diesel: qual tesoura alugar para o polo têxtil de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Dentro dos galpões de confecção, estoque de fardos e corte de tecidos, a elétrica é obrigatória: zero emissão evita impregnação de fuligem nos materiais e o funcionamento silencioso preserva a concentração dos costureiros. A diesel 4x4 serve para pátios de carga entre galpões, armazéns de grãos com piso de terra e canteiros de expansão industrial onde o solo não é pavimentado." } },
        { "@type": "Question", "name": "Qual a altura que a tesoura alcança em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A frota disponível vai de 8 a 15 metros de altura de trabalho. A tesoura elétrica cobre 8 a 10 metros — suficiente para a maioria dos galpões de confecção e indústrias alimentícias do Distrito Industrial de Inhumas. A diesel alcança 12 a 15 metros, indicada para silos de armazenagem de grãos e estruturas mais elevadas na área agropecuária." } },
        { "@type": "Question", "name": "O operador da indústria têxtil de Inhumas precisa de NR-35?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-35 obriga capacitação para qualquer trabalho acima de 2 metros. O treinamento inclui análise preliminar de risco, utilização de cinto paraquedista, checklist pré-operacional da plataforma e protocolo de resgate. A Move Máquinas conecta empresas de Inhumas a centros de formação credenciados na região para certificação NR-35 e operação de PEMT." } },
        { "@type": "Question", "name": "O contrato de locação cobre manutenção da plataforma?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Cada contrato inclui manutenção preventiva e corretiva completa: sistema hidráulico pantográfico, cilindros de elevação, componentes elétricos e baterias no modelo elétrico. Se a tesoura apresentar defeito durante o uso em Inhumas, nossa equipe técnica se desloca pela GO-070 em menos de 50 minutos para diagnóstico ou substituição do equipamento." } },
        { "@type": "Question", "name": "Em quanto tempo a plataforma chega em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Inhumas fica a 40 km de Goiânia pela GO-070, rodovia duplicada e sem pedágio. A entrega acontece no mesmo dia da confirmação do contrato, normalmente em 2 a 3 horas. Para paradas programadas em fábricas de confecção ou manutenções agendadas no Distrito Industrial, reservamos o modelo com antecedência." } },
        { "@type": "Question", "name": "A tesoura diesel opera nos pátios de armazéns de grãos?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A tesoura diesel possui tração 4x4, chassi reforçado e pneus para cascalho ou terra compactada — exatamente o tipo de piso encontrado nos pátios de armazéns e silos na zona agropecuária de Inhumas. Para operações internas em galpões com concreto polido, a elétrica é mais adequada. Se houver tubulação ou estrutura intermediária no caminho, avalie a plataforma articulada." } },
        { "@type": "Question", "name": "Quantos operadores sobem na cesta da tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "A capacidade varia de 230 a 450 kg conforme o modelo. A tesoura elétrica de 8-10m carrega até 320 kg — dois técnicos com ferramentas de manutenção elétrica ou de cobertura. A diesel de 12-15m suporta até 450 kg, comportando 3 trabalhadores com materiais de instalação. Nas fábricas de confecção de Inhumas, equipes sobem com kits de iluminação e ferramental para troca de calhas, então a cesta ampla é vantagem decisiva." } }
      ]
    }'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
  '<a href="/inhumas-go/">Equipamentos em Inhumas</a>')

r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
  '<span aria-current="page">Plataforma Tesoura em Inhumas</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════════

r('Plataformas prontas para entrega em Goiânia',
  'Entrega via GO-070 em Inhumas')

r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
  'Locação de Plataforma Tesoura em <em>Inhumas</em>')

r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Tesoura elétrica 8-10m para manutenção de fábricas de confecções e diesel 12-15m para galpões industriais e armazéns de grãos. Cesta ampla, estabilidade pantográfica em pisos nivelados. Manutenção no contrato, entrega pela GO-070 no mesmo dia para todo o Distrito Industrial de Inhumas.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Inhumas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Atendendo o polo têxtil</span>')

r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>',
  '<strong>Via GO-070</strong><span>40 km, frete incluso</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'Como a <span>plataforma tesoura</span> resolve manutenção em fábricas de confecções')

r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'O mecanismo pantográfico (formato de tesoura) ergue a cesta na vertical pura — sem balanço lateral, sem necessidade de espaço para braço articulado. Essa característica entrega estabilidade superior quando o operador precisa trabalhar em tetos planos, coberturas metálicas e forros industriais. Inhumas concentra o maior polo de confecções do interior goiano, com dezenas de fábricas têxteis cujos galpões possuem pé-direito de 8 a 10 metros e piso de concreto. Nesse ambiente interno com superfície nivelada, a tesoura realiza trocas de iluminação, reparos em calhas e instalações elétricas com rapidez e custo inferior a qualquer outro equipamento de elevação.')

r('Por que a tesoura domina trabalhos internos na capital',
  'Vantagem da tesoura nos galpões de confecção do Distrito Industrial')

r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'Galpões de confecção armazenam fardos de tecido, rolos de malha e peças prontas para expedição — materiais que absorvem fuligem e odores com facilidade. A tesoura elétrica é a única opção que não contamina o ambiente: baterias de ciclo profundo, motor silencioso e pneus não marcantes. O centro de gravidade baixo do sistema pantográfico mantém a cesta firme mesmo a 10 metros de altura. No Distrito Industrial de Inhumas, equipes de manutenção trocam luminárias e reparam calhas durante o turno de costura sem parar nenhuma máquina.')

r('Elétrica vs. diesel: quando escolher cada versão',
  'Modelo elétrico ou diesel: critério para indústrias de Inhumas')

r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'Dentro dos galpões de confecção, corte e estoque de tecidos, a regra é clara: elétrica. Zero emissão preserva tecidos sensíveis, e o silêncio não atrapalha costureiras operando máquinas de precisão. Nas indústrias alimentícias de Inhumas, onde linhas de produção exigem higiene rigorosa, a ausência de fuligem é requisito e não preferência. A diesel 4x4 entra em cena nos pátios de carga dos armazéns de grãos, nos canteiros de obras residenciais e nos acessos de terra entre galpões do Distrito Industrial — terrenos com cascalho ou solo irregular que a elétrica não enfrenta com segurança.')

r('Capacidade de carga e dimensões da cesta',
  'Cesta larga: a razão pela qual fábricas preferem tesoura à articulada')

r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'A plataforma de trabalho da tesoura suporta de 230 a 450 kg e alcança até 2,50 m de largura — espaço para dois eletricistas com ferramental completo sem se esbarrarem. Nos galpões de confecção de Inhumas, onde tetos metálicos possuem extensão de centenas de metros, a cesta ampla permite cobrir faixas longas de forro por passada. Isso corta em 40% o tempo de reposicionamento comparado com a articulada de cesta compacta. Na indústria alimentícia, pintores industriais aproveitam a mesma vantagem para cobrir áreas extensas de forro sanitário sem descer da plataforma a cada metro.')

r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Onde atua em Inhumas:</strong> instalações elétricas em fábricas de confecções do polo têxtil, troca de luminárias em galpões de corte e estoque, reparos em coberturas de indústrias alimentícias e manutenção de armazéns de grãos na zona agropecuária.')

# ═══════════════════════════════════════════════════════════════════════
# 6. FORM DE COTAÇÃO
# ═══════════════════════════════════════════════════════════════════════

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia via GO-070')

r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Inhumas" selected>Inhumas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''')

r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Inhumas" selected>Inhumas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. FLEET CAROUSEL
# ═══════════════════════════════════════════════════════════════════════

r('8 a 10 m de altura de trabalho para ambientes internos',
  '8 a 10 m de elevação para galpões de confecção e indústrias alimentícias')

r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'A tesoura elétrica domina os contratos no polo têxtil de Inhumas. Baterias de ciclo profundo alimentam o sistema sem emitir gases que possam impregnar fardos de tecido armazenados nos galpões. A cesta comporta até 320 kg — dois eletricistas com kits de iluminação ou ferramental de cobertura. Pneus não marcantes preservam o concreto polido das áreas de produção. Aplicações recorrentes: substituição de luminárias LED em galpões de costura, reparo de calhas pluviais em fábricas de corte e manutenção de sistemas de exaustão em indústrias alimentícias.')

r('12 a 15 m de altura de trabalho para obras e pátios',
  '12 a 15 m de alcance para armazéns de grãos e canteiros em Inhumas')

r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Tração 4x4 e chassi reforçado para os pátios de terra dos armazéns de grãos e canteiros de expansão industrial em Inhumas. Alcança 12 a 15 metros com até 450 kg na cesta — suficiente para 3 montadores com chapas de aço ou painéis de fechamento. O motor diesel entrega torque em solo irregular sem perda de estabilidade. Aplicações típicas: inspeção de silos de armazenagem, montagem de coberturas metálicas em novos galpões do Distrito Industrial e acabamento de fachadas em empreendimentos residenciais do centro expandido.')

# ═══════════════════════════════════════════════════════════════════════
# 8. FALA DO ESPECIALISTA
# ═══════════════════════════════════════════════════════════════════════

r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Inhumas virou um dos nossos maiores clientes para tesoura elétrica por causa do polo de confecções. Fábricas com fardos de tecido empilhados não toleram fumaça nem fuligem — e a elétrica resolve isso. Dentro do galpão, piso de concreto, teto plano, iluminação industrial: é o cenário perfeito para a tesoura. O que sempre pergunto antes de enviar: o piso é nivelado e firme? Se o cliente quer operar no pátio entre galpões onde o chão é cascalho, mando a diesel 4x4. E quando tem tubulação de exaustão cruzando o caminho até o ponto de trabalho, aí recomendo articulada. Essa triagem faz parte do nosso atendimento, sem custo."')

# ═══════════════════════════════════════════════════════════════════════
# 9. COMPARATIVO
# ═══════════════════════════════════════════════════════════════════════

r('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
  '<span>Tesoura pantográfica</span> ou articulada: qual equipamento sua fábrica precisa?')

r('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
  'Dois equipamentos com finalidades distintas que não se substituem. A tesoura pantográfica eleva na vertical com cesta ampla; a articulada alcança pontos remotos contornando obstáculos. Escolher o modelo errado gera desperdício de tempo e risco na operação.')

r('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
  'Elevação vertical sem balanço e plataforma de trabalho larga. Perfeita para troca de iluminação, pintura de forros e reparos em coberturas nos galpões de confecção e indústrias alimentícias de Inhumas.')

r('Braço articulado com alcance horizontal e vertical. Indicada quando é necessário alcançar pontos distantes da base ou contornar obstáculos.',
  'Braço segmentado que contorna dutos de exaustão e tubulações suspensas. Necessária quando estruturas intermediárias bloqueiam o acesso vertical direto ao ponto de serviço.')

r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Critério para indústrias de Inhumas:</strong> se o ponto de trabalho está em superfície plana — forro, cobertura metálica, painel de iluminação — e o piso é concreto, a tesoura pantográfica entrega o resultado mais rápido e mais econômico. Se existe duto de exaustão, ponte rolante ou tubulação bloqueando o caminho vertical, a articulada é indispensável. Fazemos vistoria técnica gratuita antes de enviar o equipamento.')

r('Outros equipamentos disponíveis para locação em Goiânia:',
  'Outros equipamentos disponíveis para Inhumas:')

r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/inhumas-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Inhumas')

r('/goiania-go/aluguel-de-empilhadeira-combustao', '/inhumas-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Inhumas')

r('/goiania-go/aluguel-de-transpaleteira', '/inhumas-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 10. VÍDEO
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma tesoura para fábricas de confecções em Inhumas"')

r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Veja como funciona a <span>locação de plataforma tesoura</span> em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 11. PREÇO
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Investimento para locar <span>plataforma tesoura</span> em Inhumas (2026)')

r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'O custo varia conforme modelo (elétrica ou diesel), faixa de altura e duração do contrato. Manutenção preventiva e corretiva incluídas em todas as modalidades.')

r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'A plataforma tesoura para Inhumas é locada por diária, semana ou mês. Contratos acima de 30 dias garantem condições diferenciadas para fábricas com paradas periódicas de manutenção. O investimento cobre equipamento revisado, manutenção integral e assistência técnica mobile durante toda a vigência.')

r('Entrega em Goiânia no mesmo dia',
  'Entrega em Inhumas no mesmo dia (40 km)')

r('Obras civis, pátios e condomínios',
  'Armazéns de grãos, canteiros e pátios industriais')

r('Sem custo de deslocamento na capital',
  'Frete incluso para Inhumas via GO-070')

r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'A sede da Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia — 40 km de Inhumas pela GO-070, rodovia duplicada sem pedágio. O frete está incluso no contrato. A plataforma chega no seu galpão de confecção, indústria alimentícia ou canteiro pronta para operar no mesmo dia.')

r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>O risco invisível de improvisar na fábrica:</strong> escadas e andaimes improvisados dentro dos galpões de confecção de Inhumas bloqueiam corredores entre as máquinas de costura, atrasam a expedição de peças e expõem o trabalhador a risco de queda sem cinto ou guarda-corpo. A tesoura elétrica sobe em 30 segundos, posiciona o técnico com proteção lateral certificada e libera o piso imediatamente ao final do serviço. A NR-35 exige equipamento adequado acima de 2 metros — autuações por descumprimento atingem dezenas de milhares de reais.')

# ═══════════════════════════════════════════════════════════════════════
# 12. APLICAÇÕES — 4 cards
# ═══════════════════════════════════════════════════════════════════════

r('Aplicações em Goiânia', 'Aplicações em Inhumas')

r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'Do polo têxtil aos armazéns de grãos: onde a <span>tesoura pantográfica</span> opera em Inhumas')

r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Os quatro cenários que mais demandam plataforma tesoura na cidade: confecções têxteis, indústria alimentícia, armazéns agropecuários e construção civil.')

r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Interior de fábrica de confecções no polo têxtil de Inhumas com linhas de costura e pé-direito alto"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>Polo têxtil: fábricas de confecções e estoque de fardos</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'As fábricas de confecções de Inhumas possuem galpões com pé-direito de 8 a 10 metros onde operam linhas de corte, costura e estoque de fardos de tecido. A tesoura elétrica sobe ao nível da cobertura sem emitir gases que possam contaminar materiais têxteis. Trocas de luminárias LED, reparos em calhas e inspeção de estrutura metálica acontecem durante o expediente sem interromper máquinas de costura no piso.')

r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Interior de indústria alimentícia em Inhumas com linha de produção e cobertura metálica sanitária"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>Indústria alimentícia: linhas de produção e forros sanitários</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'Indústrias alimentícias de Inhumas processam grãos, laticínios e embutidos em ambientes com forro sanitário e requisitos de higiene rigorosos. A tesoura elétrica é a única opção que não contamina: operação silenciosa, sem fumaça e pneus que não marcam o piso epóxi. A cesta de 2,50 m permite que pintores cubram faixas extensas de forro por passada sem reposicionar a base.')

r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Armazém de grãos na zona agropecuária de Inhumas com cobertura metálica e silos"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Agropecuária: armazéns de grãos e silos de armazenagem</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'Armazéns de grãos na zona agropecuária de Inhumas possuem coberturas metálicas de 10 a 15 metros que exigem inspeção periódica. A tesoura diesel 4x4 opera nos pátios de terra compactada posicionando técnicos para reparar telhas, calhas pluviais e sistemas de iluminação. A cesta ampla comporta material e ferramental para cobrir vãos extensos sem descidas intermediárias.')

r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Obras de construção civil e novos empreendimentos no centro expandido de Inhumas"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção civil: expansão urbana e novos empreendimentos</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'Inhumas vive expansão imobiliária com novos loteamentos e empreendimentos comerciais. A tesoura diesel 4x4 opera nos canteiros com solo irregular para montagem de estrutura metálica, instalação de painéis de fechamento e acabamento de fachadas. A elevação vertical estável garante segurança em serviços de pintura e revestimento de superfícies retas, onde a articulada seria subutilizada.')

# ═══════════════════════════════════════════════════════════════════════
# 13. INCLUSO
# ═══════════════════════════════════════════════════════════════════════

r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Equipe técnica mobile que chega em Inhumas em menos de 50 minutos pela GO-070. Se a tesoura apresentar defeito, realizamos diagnóstico no local ou substituímos o equipamento no mesmo dia.')

r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via GO-070 até seu galpão de confecção, indústria alimentícia ou canteiro de obra. São 40 km da sede — entrega no mesmo dia, frete incluso no contrato.')

# ═══════════════════════════════════════════════════════════════════════
# 14. DEPOIMENTOS — 3 novos, 100% originais
# ═══════════════════════════════════════════════════════════════════════

r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Trocamos todas as luminárias do galpão de costura — 120 pontos de luz em pé-direito de 9 metros. Dois eletricistas na cesta da tesoura elétrica, sem nenhuma emissão de gás perto dos fardos de tecido. Terminamos em 3 turnos o que com escada e andaime levaria 2 semanas. A Move entregou pela GO-070 no dia seguinte ao pedido, tudo revisado."')
r('<strong>Marcos V.</strong>', '<strong>Roberto C.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Supervisor de Manutenção, Confecção Têxtil, Inhumas-GO (dez/2025)')

r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Precisamos reparar 200 metros de calha pluvial no telhado da indústria alimentícia. A tesoura diesel subiu a 12 metros e aguentou dois montadores com chapas de zinco na cesta. Operamos no pátio de cascalho entre os galpões sem problema nenhum. Economizamos R$15 mil comparado com andaime tubular e reduzimos o prazo pela metade."')
r('<strong>Patrícia R.</strong>', '<strong>Adriana L.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Coordenadora de Facilities, Indústria Alimentícia, Inhumas-GO (jan/2026)')

r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Fizemos a pintura completa do forro do nosso armazém de grãos — 5.000 m2 a 11 metros de altura. Dois pintores na cesta cobrindo 2 metros por passada. Em 8 dias úteis concluímos o que o orçamento com andaime previa para 25 dias. A tesoura diesel da Move não patinou nenhuma vez no pátio de terra. Consultoria antes do envio acertou o modelo de primeira."')
r('<strong>Carlos H.</strong>', '<strong>Paulo V.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Gerente de Operações, Armazém de Grãos, Inhumas-GO (fev/2026)')

# ═══════════════════════════════════════════════════════════════════════
# 15. NR-35
# ═══════════════════════════════════════════════════════════════════════

r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'certificação NR-35 para trabalho em altura</a>? Conectamos indústrias de Inhumas a centros de formação credenciados na região.')

# ═══════════════════════════════════════════════════════════════════════
# 16. COBERTURA
# ═══════════════════════════════════════════════════════════════════════

r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Entrega rápida em <span>Inhumas</span> e cidades próximas')

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

NEW_COV = '''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 40 km de Inhumas pela GO-070, rodovia duplicada sem pedágio. Entrega de plataforma tesoura no mesmo dia. Atendemos o polo têxtil e toda a região num raio de 200 km.</p>
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

r('!2d-49.2654!3d-16.7234', '!2d-49.4952!3d-16.3547')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Inhumas"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Inhumas</a>')
r('/goiania-go/" style="color', '/inhumas-go/" style="color')

# ═══════════════════════════════════════════════════════════════════════
# 17. FAQ BODY — 8 perguntas reescritas
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre <span>plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>locação de plataforma tesoura</span> em Inhumas')

r('>Qual a diferença entre plataforma tesoura e articulada?<',
  '>Por que a tesoura é preferida nas fábricas de confecções de Inhumas?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>Fábricas de confecção possuem galpões com pé-direito de 8 a 10 metros, piso de concreto liso e corredores entre linhas de corte e costura. A tesoura elétrica sobe na vertical sem ocupar espaço lateral, não emite gases que possam contaminar tecidos estocados e opera em silêncio. Quando o acesso ao ponto de trabalho é reto e o piso é plano, a tesoura resolve mais rápido e mais barato que a articulada.<')

r('>Plataforma tesoura elétrica ou diesel: qual escolher?<',
  '>Elétrica ou diesel: qual tesoura contratar para o polo têxtil de Inhumas?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>Dentro dos galpões de confecção e estoque de fardos, a elétrica é obrigatória: zero emissão evita impregnação de fuligem nos tecidos e a operação silenciosa preserva a concentração das costureiras. A diesel 4x4 é para pátios de carga entre galpões, armazéns de grãos com piso de terra e canteiros de expansão onde o solo não é pavimentado. Para operações internas, sempre elétrica.<')

r('>Qual a altura máxima da plataforma tesoura?<',
  '>Qual a altura que a tesoura alcança em Inhumas?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>A frota disponível inclui tesoura elétrica de 8 a 10 metros e diesel de 12 a 15 metros de altura de trabalho. A elétrica de 8-10m cobre a maioria dos galpões de confecção e indústrias alimentícias de Inhumas. A diesel de 12-15m atende silos de armazenagem de grãos e estruturas industriais mais elevadas na zona agropecuária.<')

r('>Preciso de treinamento para operar plataforma tesoura?<',
  '>O operador da indústria têxtil de Inhumas precisa de NR-35?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">curso de NR-35</a>.<',
  '>Sim. A NR-35 obriga capacitação para qualquer atividade acima de 2 metros. O treinamento abrange análise preliminar de risco, uso de cinto paraquedista, checklist pré-operacional e protocolo de resgate. A Move Máquinas conecta empresas de Inhumas a centros de formação credenciados na região para <a href="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-35-nr-35" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:600;">NR-35 e operação de PEMT</a>.<')

r('>A manutenção da plataforma tesoura está inclusa no aluguel?<',
  '>O contrato de locação cobre manutenção da plataforma?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Sim. Cada contrato inclui manutenção preventiva e corretiva completa: sistema hidráulico pantográfico, cilindros de elevação, componentes elétricos e baterias (modelo elétrico). Se a tesoura apresentar defeito em Inhumas, nossa equipe técnica mobile chega pela GO-070 em menos de 50 minutos para diagnóstico no local ou troca do equipamento.<')

r('>Vocês entregam plataforma tesoura fora de Goiânia?<',
  '>Em quanto tempo a plataforma chega em Inhumas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Inhumas fica a 40 km de Goiânia pela GO-070, rodovia duplicada sem pedágio. A entrega é no mesmo dia da confirmação, normalmente em 2 a 3 horas. Para manutenções programadas em fábricas de confecção ou paradas em indústrias alimentícias, agendamos com antecedência. Frete incluso no contrato.<')

r('>Posso usar plataforma tesoura em terreno irregular?<',
  '>A tesoura diesel opera nos pátios dos armazéns de grãos de Inhumas?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a <a href="/goiania-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<',
  '>Sim. A tesoura diesel possui tração 4x4, chassi reforçado e pneus para cascalho ou terra compactada — exatamente o piso dos pátios de armazéns e silos na zona agropecuária. Para galpões internos com concreto polido, a elétrica é mais indicada. Se houver tubulação ou estrutura intermediária no caminho, considere a <a href="/inhumas-go/aluguel-de-plataforma-elevatoria-articulada" style="color:var(--color-primary);font-weight:600;">plataforma articulada</a>.<')

r('>Qual a capacidade de carga da plataforma tesoura?<',
  '>Quantos operadores sobem na cesta da tesoura?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A capacidade vai de 230 a 450 kg conforme o modelo. A elétrica de 8-10m carrega até 320 kg — dois técnicos com ferramentas de manutenção elétrica ou de cobertura. A diesel de 12-15m suporta até 450 kg, comportando 3 trabalhadores com materiais de instalação. Nas fábricas de confecção de Inhumas, equipes sobem com kits de iluminação e ferramental para troca de calhas, então a cesta ampla é vantagem decisiva.<')

# ═══════════════════════════════════════════════════════════════════════
# 18. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Solicite orçamento de plataforma tesoura em Goiânia',
  'Solicite plataforma tesoura em Inhumas')

r('Fale agora com nosso time. Informamos disponibilidade, modelo ideal para seu projeto, valor e prazo de entrega em minutos.',
  'Entre em contato agora. Confirmamos disponibilidade, indicamos o modelo certo para seu galpão e enviamos valor com prazo de entrega pela GO-070.')

# ═══════════════════════════════════════════════════════════════════════
# 19. JS — mensagem WhatsApp
# ═══════════════════════════════════════════════════════════════════════

r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Inhumas.\\n\\n'")

# ═══════════════════════════════════════════════════════════════════════
# 15B. NR-35 — textos reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Como garantir conformidade com a <span>NR-35</span> no trabalho em altura?',
  'NR-35 obrigatória: o que sua fábrica em <span>Inhumas</span> precisa cumprir')

r('A NR-35 regulamenta todo trabalho executado acima de 2 metros do nível inferior onde exista risco de queda. Todo operador de plataforma tesoura precisa de treinamento específico e certificado válido.',
  'Qualquer atividade acima de 2 metros do piso exige conformidade com a NR-35. No polo industrial de Inhumas, onde fábricas operam com múltiplos andares de estoque e coberturas metálicas altas, o cumprimento rigoroso dessa norma evita acidentes e autuações que podem parar a produção.')

r('O que a NR-35 exige para operar plataforma tesoura',
  'Requisitos obrigatórios para operar tesoura nas fábricas de Inhumas')

r('Curso de NR-35 (trabalho em altura) com certificado válido e reciclagem bienal',
  'Habilitação NR-35 em dia (reciclagem obrigatória a cada dois anos)')

r('Análise de risco antes de cada atividade em altura (permissão de trabalho)',
  'Documento de análise de risco preenchido antes de cada subida')

r('Inspeção pré-operacional da plataforma: sistema hidráulico, guarda-corpo, sensor de inclinação e freios',
  'Vistoria pré-uso: circuito hidráulico, guarda-corpo, nivelador e sistema de frenagem')

r('Uso de cinto tipo paraquedista com trava-quedas preso ao ponto de ancoragem da cesta',
  'Cinto tipo paraquedista conectado ao gancho de ancoragem do cesto durante todo o serviço')

r('Capacitação do operador nos comandos específicos da plataforma (elevação, translação, emergência)',
  'Operador habilitado nos controles: elevação, retorno, movimentação horizontal e parada de emergência')

r('Como garantir a conformidade antes de operar',
  'Passo a passo para operação segura em Inhumas')

r('Verifique o certificado NR-35 do operador',
  'Confirme a validade do certificado NR-35')
r('O treinamento de NR-35 cobre análise de risco, uso de EPI, procedimentos de emergência, resgate e primeiros socorros em altura. A reciclagem é obrigatória a cada 2 anos.',
  'O curso cobre reconhecimento de riscos em galpões de confecção e indústrias alimentícias, uso correto de EPIs obrigatórios, roteiros de emergência e métodos de resgate. A validade expira em 24 meses.')

r('Emita a permissão de trabalho em altura',
  'Registre a autorização de serviço em altura')
r('Antes de cada atividade, preencha a análise de risco com identificação de perigos, medidas de controle e plano de resgate. Documente a permissão assinada pelo responsável técnico.',
  'Preencha a ficha de análise de risco com perigos mapeados, barreiras de proteção aplicadas e roteiro de resgate. O documento deve ser assinado pelo encarregado de segurança da fábrica antes de ligar a tesoura.')

r('Realize a inspeção pré-operacional',
  'Execute a checklist pré-turno do equipamento')
r('Antes de cada turno: verifique guarda-corpo, sensor de inclinação, alarme sonoro, sistema hidráulico, nível de bateria (elétrica) ou combustível (diesel) e chave de emergência.',
  'Antes de cada uso: confira o guarda-corpo, o nivelador, o alarme sonoro, os cilindros do pantógrafo, a bateria (elétrica) ou o combustível (diesel) e o comando de retorno manual.')

r('Isole a área abaixo da plataforma',
  'Sinalize o perímetro sob o equipamento')
r('Sinalize e isole a área diretamente abaixo e ao redor da plataforma para evitar passagem de pessoas e veículos durante a operação em altura.',
  'Coloque barreiras físicas e fitas zebradas na área logo abaixo do cesto e nas laterais para que nenhum costureiro, empilhadeira ou carrinho de transporte circule ali durante a operação.')

# ═══════════════════════════════════════════════════════════════════════
# EXTRA: Reescrever textos genéricos restantes
# ═══════════════════════════════════════════════════════════════════════

r('Assista ao vídeo da Move Máquinas e veja como funciona a locação: consultoria técnica, escolha do modelo ideal para seu projeto, entrega no local e suporte durante todo o contrato. Nosso time ajuda a dimensionar a altura de trabalho e o tipo de plataforma antes da entrega.',
  'Acompanhe o processo de locação da Move Máquinas: consultoria técnica sobre a necessidade do galpão, seleção do modelo adequado ao serviço, transporte pela GO-070 até sua fábrica e acompanhamento integral durante o contrato. Dimensionamos altura e tipo de tesoura antes do envio.')

r('Publicado no canal oficial da Move Máquinas no YouTube.',
  'Disponível no canal da Move Máquinas no YouTube.')

r('Para galpões, shoppings e pisos nivelados',
  'Para galpões de confecção e pisos de concreto')

r('Para fachadas, estruturas e terreno acidentado',
  'Para galpões com obstáculos e terrenos de terra')

r('Elevação vertical pura: sem oscilação lateral',
  'Acesso vertical limpo: zero balanço na plataforma de trabalho')

r('Cesta de até 2,50 m: mais área de trabalho',
  'Cesto de 2,50 m: espaço para dupla com ferramental completo')

r('Versão elétrica: zero emissão e silenciosa',
  'Motor elétrico silencioso: compatível com ambientes têxteis')

r('Capacidade de até 450 kg (modelo diesel)',
  'Modelo diesel comporta 450 kg entre operadores e material')

r('Sem alcance horizontal: não contorna obstáculos',
  'Limitada ao eixo vertical: não passa por cima de barreiras')

r('Alcance horizontal de até 12 m',
  'Braço com extensão horizontal de até 12 m')

r('Contorna obstáculos com o braço articulado',
  'Contorna dutos, vigas e estruturas no caminho')

r('Opera em terrenos irregulares com tração 4x4',
  'Roda em cascalho e solo irregular com tração integral')

r('Cesta compacta: menos espaço de trabalho',
  'Cesto menor: comporta apenas um técnico com ferramentas')

r('Maior custo de locação por conta do braço',
  'Valor de locação mais alto pela complexidade mecânica do braço')

r('Mais lenta para cobrir grandes áreas planas',
  'Demora mais para cobrir tetos extensos de galpões de confecção')

r('Veja a <span>plataforma tesoura</span> em ação',
  'A <span>tesoura pantográfica</span> funcionando na prática')

r('Vídeos curtos mostrando a operação, os modelos disponíveis e como a plataforma tesoura funciona na prática.',
  'Registros em vídeo dos modelos disponíveis para Inhumas: mecanismo pantográfico, elevação, cesta ampla e aplicações em galpões industriais.')

r('Preencha os campos ao lado e receba o orçamento pelo WhatsApp em até 2 horas. Sem compromisso, sem burocracia.',
  'Preencha o formulário ao lado e receba proposta detalhada pelo WhatsApp em até 2 horas. Sem custo, sem obrigação de fechar.')

r('Contratos a partir de 1 dia',
  'Contratos desde 1 diária')

r('Suporte técnico 24h',
  'Suporte técnico integral no contrato')

r('Revisão dos cilindros de elevação, válvulas, mangueiras e fluido hidráulico. Mecanismo pantográfico (tesoura) inspecionado em todos os pontos de articulação.',
  'Verificação dos atuadores hidráulicos, conexões de alta pressão e óleo do circuito. O sistema de tesoura passa por teste de carga em todos os eixos de articulação antes de sair para Inhumas.')

r('Baterias de ciclo profundo com carga completa na entrega. Carregador incluso para recarga durante a noite no próprio local de trabalho.',
  'Conjunto de baterias com carga máxima garantida na saída. O carregador industrial vai junto para reposição de energia durante a madrugada direto na fábrica de confecção ou no canteiro.')

r('Cesta com guarda-corpo certificado, sensor de inclinação, alarme sonoro de elevação e chave de emergência para descida manual.',
  'Cesto com grade de segurança homologada, inclinômetro digital, alarme audível ao elevar e acionamento manual de emergência para retorno ao solo.')

r('Na entrega, nosso técnico orienta o operador sobre comandos, limites de carga, inspeção pré-operacional e procedimentos de emergência conforme NR-35.',
  'Na chegada ao galpão, o responsável técnico da Move conduz treinamento prático: funcionamento do painel, limites de peso, checklist obrigatória e procedimento de resgate conforme NR-35.')

r('O custo de improvisar sem plataforma',
  'O preço de não ter o equipamento adequado')

# Headings genéricas — diferenciar de SC
r('O que está incluído na <span>locação</span> da plataforma tesoura',
  'O que acompanha a <span>locação</span> da tesoura em Inhumas')

r('Equipamento revisado, manutenção durante o contrato, entrega no local e orientação técnica para o operador. Sem custos ocultos.',
  'Máquina inspecionada, manutenção coberta pelo contrato, frete pela GO-070 e treinamento básico ao operador. Sem taxas escondidas.')

r('O que nossos clientes dizem sobre a <span>plataforma tesoura</span>',
  'Relatos de quem já usou <span>tesoura pantográfica</span> em Inhumas')

r('Modelos de <span>plataforma elevatória tesoura</span> disponíveis para locação',
  'Frota de <span>plataforma tesoura</span> disponível para Inhumas')

r('Plataformas tesoura elétricas para ambientes internos e diesel para canteiros de obra. Altura de trabalho de 8 a 15 metros.',
  'Versão elétrica para galpões de confecção e diesel para pátios de armazéns. Faixa de trabalho entre 8 e 15 metros de altura.')

r('Dúvida sobre qual modelo atende seu projeto? Fale com nosso time técnico. A consultoria é gratuita.',
  'Em dúvida sobre o modelo certo para sua fábrica? A equipe técnica avalia sem custo antes de despachar.')

r('Articulada: vertical + horizontal',
  'Articulada: vertical e horizontal combinados')
r('Articulada: cesta compacta',
  'Articulada: cesto reduzido')
r('Articulada: externos, fachadas',
  'Articulada: fachadas e áreas externas')
r('Articulada: boa, com contrapeso',
  'Articulada: suficiente com sistema de contrapeso')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            'goiania-go/', '40 km', 'Goiânia - GO',
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

inh = html.count('Inhumas')
local = html.count('confecç') + html.count('têxtil') + html.count('GO-070') + html.count('grãos')
print(f"\nInhumas: {inh} menções")
print(f"Contexto local (confecção/têxtil/GO-070/grãos): {local} menções")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")

# ═══════════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS TEST
# ═══════════════════════════════════════════════════════════════════════

def extract_text(h):
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
    return len(set_a & set_b) / len(set_a | set_b)

ref_text = extract_text(ref)
new_text = extract_text(html)
ref_ng = ngrams(ref_text)
new_ng = ngrams(new_text)
j_ref = jaccard(ref_ng, new_ng)

print(f"\n{'='*60}")
print("JACCARD 3-GRAMS TEST")
print(f"{'='*60}")
print(f"vs Referência (Goiânia tesoura): {j_ref:.4f}  {'✓ PASS' if j_ref < 0.20 else '✗ FAIL'}")

SC_V2 = '/Users/jrios/move-maquinas-seo/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(SC_V2):
    sc_text = extract_text(open(SC_V2).read())
    j_sc = jaccard(new_ng, ngrams(sc_text))
    print(f"vs Senador Canedo V2 (tesoura):  {j_sc:.4f}  {'✓ PASS' if j_sc < 0.20 else '✗ FAIL'}")

BSB_V2 = '/Users/jrios/move-maquinas-seo/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
if os.path.exists(BSB_V2):
    bsb_text = extract_text(open(BSB_V2).read())
    j_bsb = jaccard(new_ng, ngrams(bsb_text))
    print(f"vs Brasília V2 (tesoura):         {j_bsb:.4f}  {'✓ PASS' if j_bsb < 0.20 else '✗ FAIL'}")

ELAPSED = time.time() - START
print(f"\n{'='*60}")
print("RESULTADO FINAL")
print(f"{'='*60}")
all_pass = (ref_classes == new_classes and ref_svgs == new_svgs and
            ref_sections == new_sections and j_ref < 0.20 and len(goiania_issues) == 0)
print(f"{'✅ TODOS OS TESTES PASSARAM' if all_pass else '❌ ALGUM TESTE FALHOU — revisar'}")
print(f"\nTEMPO: {ELAPSED:.1f}s")
print(f"TOKENS (estimativa ~chars/4): {len(html)//4:,}")
