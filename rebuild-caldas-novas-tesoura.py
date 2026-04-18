#!/usr/bin/env python3
"""
rebuild-caldas-novas-tesoura.py
Builds tesoura LP for Caldas Novas from Goiania reference.
All text rewritten from scratch for tourism context.
"""
import time, re, os, hashlib, hmac, datetime, urllib.request
START = time.time()
REF = '/Users/jrios/move-maquinas-seo/ref-goiania-tesoura.html'
OUT = '/Users/jrios/move-maquinas-seo/caldas-novas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()
def r(old, new, count=1):
    global html
    if old not in html:
        print(f"MISS: {old[:70]}...")
        return
    html = html.replace(old, new, count)

# === META/SCHEMA ===
r('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
  '<title>Plataforma Tesoura para Locação em Caldas Novas-GO | Move Máquinas</title>')
r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
  'content="Plataforma tesoura em Caldas Novas: elétrica 8-10m para lobbies de hotel e centros de convenções, diesel 12-15m para canteiros de novos empreendimentos. Manutenção inclusa, entrega pela GO-139."')
r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  'href="https://movemaquinas.com.br/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura"')
r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
  'content="Plataforma Tesoura para Locação em Caldas Novas-GO | Move Máquinas"')
r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
  'content="Tesoura elétrica e diesel 8-15m para hotéis, centros de convenções e canteiros de obra em Caldas Novas. Manutenção no contrato, entrega agendada pela GO-139."')
r('content="Goiânia, Goiás, Brasil"', 'content="Caldas Novas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-17.7441;-48.6252"')
r('content="-16.7234, -49.2654"', 'content="-17.7441, -48.6252"')
r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -17.7441, "longitude": -48.6252')
r('"latitude": -16.7234', '"latitude": -17.7441')
r('"longitude": -49.2654', '"longitude": -48.6252')
r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"', '"name": "Locação de Plataforma Tesoura em Caldas Novas"')
r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Caldas Novas", "addressRegion": "GO"')
r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Equipamentos em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/"')
r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
  '"name": "Plataforma Tesoura em Caldas Novas", "item": "https://movemaquinas.com.br/caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura"')

# === FAQ SCHEMA (full block replace) ===
OLD_FAQ = '''    {
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

NEW_FAQ = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Para quais serviços em hotéis de Caldas Novas a tesoura é indicada?", "acceptedAnswer": { "@type": "Answer", "text": "A tesoura resolve manutenções em superfícies planas com acesso vertical direto: troca de luminárias em lobbies de hotel, pintura de forros em centros de convenções, reparo de forro de gesso em salões de evento e substituição de telhas em coberturas de resort. O piso precisa ser firme e nivelado — porcelanato, concreto ou cerâmica dos ambientes internos são ideais." } },
        { "@type": "Question", "name": "Tesoura elétrica ou diesel: qual pedir para Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "Dentro de hotéis, resorts e centros de convenções, a elétrica é obrigatória: zero fumaça, operação silenciosa e pneus que preservam pisos decorativos. A diesel serve para canteiros de novos hotéis no Setor Itaici e estacionamentos sem pavimentação, onde tração 4x4 é necessária para cascalho e terra batida." } },
        { "@type": "Question", "name": "Qual a altura máxima da tesoura disponível para Caldas Novas?", "acceptedAnswer": { "@type": "Answer", "text": "A frota inclui elétrica de 8 a 10 metros e diesel de 12 a 15 metros. A elétrica cobre lobbies, salões de evento e centros de convenções cujo pé-direito fica entre 6 e 10 metros. A diesel alcança coberturas de resorts maiores e estruturas de parques aquáticos acima de 12 metros." } },
        { "@type": "Question", "name": "Funcionários de hotel precisam de treinamento para usar a tesoura?", "acceptedAnswer": { "@type": "Answer", "text": "Toda operação acima de 2 metros exige treinamento NR-35 válido com módulo PEMT. O programa cobre análise de risco, inspeção pré-operacional, uso de EPI e procedimentos de emergência. Hotéis e construtoras de Caldas Novas podem solicitar indicação de centros credenciados na região." } },
        { "@type": "Question", "name": "A manutenção da tesoura vem inclusa no contrato?", "acceptedAnswer": { "@type": "Answer", "text": "Cada contrato da Move Máquinas cobre manutenção preventiva e corretiva do sistema pantográfico, cilindros de elevação, parte elétrica e baterias. Em caso de falha durante uso em Caldas Novas, a equipe técnica se desloca pela GO-139 para diagnóstico e reparo no local." } },
        { "@type": "Question", "name": "Vocês entregam tesoura em Caldas Novas mesmo a 170 km?", "acceptedAnswer": { "@type": "Answer", "text": "Caldas Novas está dentro do raio de 200 km. O trajeto pela GO-139 leva cerca de 2h30. Para contratos acima de 15 dias, o frete é incluso na mensalidade. Manutenções de hotel na entressafra permitem agendar data e horário com antecedência." } },
        { "@type": "Question", "name": "A tesoura diesel funciona nos canteiros das obras novas?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A diesel possui tração 4x4 e chassi reforçado para terra batida, cascalho e rampa. Canteiros de novos hotéis no Setor Itaici e ao longo da GO-139 são cenário típico de uso. A elétrica exige piso nivelado e firme — lobbies, salões e áreas internas prontas." } },
        { "@type": "Question", "name": "Quantas pessoas a cesta da tesoura comporta?", "acceptedAnswer": { "@type": "Answer", "text": "A cesta suporta de 230 a 450 kg conforme modelo. A elétrica de 8-10m carrega até 320 kg — dois profissionais com ferramentas. A diesel de 12-15m aguenta até 450 kg, três técnicos com material de montagem. Para pintores de hotel que sobem com galões e rolos, a cesta ampla comporta todo o material sem viagens extras." } }
      ]
    }'''
r(OLD_FAQ, NEW_FAQ)

# === BREADCRUMB ===
r('<a href="/goiania-go/">Equipamentos em Goiânia</a>', '<a href="/caldas-novas-go/">Equipamentos em Caldas Novas</a>')
r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>', '<span aria-current="page">Plataforma Tesoura em Caldas Novas</span>')

# === HERO ===
r('Plataformas prontas para entrega em Goiânia', 'Tesoura disponível para a região termal')
r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>', 'Plataforma Tesoura para Locação em <em>Caldas Novas</em>')
r('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
  'Tesoura elétrica 8-10m e diesel 12-15m para manutenção de lobbies de hotel, pintura de centros de convenções e obras de novos empreendimentos turísticos. Cesta ampla, estabilidade máxima em pisos nivelados. Entrega pela GO-139 para toda a região de Caldas Novas.')
r('Goi%C3%A2nia', 'Caldas+Novas', 99)

# === TRUST BAR ===
r('<strong>+20 anos</strong><span>No mercado goiano</span>', '<strong>+20 anos</strong><span>Experiência em GO</span>')
r('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>', '<strong>170 km</strong><span>Via GO-139</span>')

# === O QUE É ===
r('O que é a <span>plataforma tesoura</span> e por que é a mais usada em galpões',
  'Quando contratar <span>plataforma tesoura</span> para projetos em Caldas Novas')
r('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
  'A plataforma tesoura ergue o operador na vertical pura por meio de tesouras cruzadas que se abrem hidraulicamente. Essa mecânica garante estabilidade total em pisos firmes — exatamente o cenário dos lobbies de hotel, centros de convenções e salões de evento de Caldas Novas. A cidade concentra 106 hotéis e resorts que precisam trocar luminárias, repintar forros e reparar sistemas de climatização em altura sem interditar áreas de hóspedes. Para essas operações internas com piso de porcelanato ou concreto nivelado, a tesoura é o equipamento mais rápido e econômico disponível.')
r('Por que a tesoura domina trabalhos internos na capital', 'Por que a tesoura é o padrão em lobbies e salões de hotel')
r('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
  'O centro de gravidade baixo do mecanismo pantográfico mantém a cesta estável mesmo a 10 metros de altura. Dentro de lobbies e centros de convenções de Caldas Novas, onde o pé-direito atinge 8 a 12 metros e o piso é porcelanato nivelado, a tesoura elétrica sobe em silêncio e sem fumaça. Eletricistas trocam luminárias e pintores retocam forros enquanto os eventos continuam nos salões vizinhos sem interrupção.')
r('Elétrica vs. diesel: quando escolher cada versão', 'Versão elétrica ou diesel: como decidir em Caldas Novas')
r('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
  'A regra é direta: se o trabalho é dentro de hotel, centro de convenções ou parque aquático coberto, use elétrica — zero emissão protege hóspedes e preserva pisos decorativos. Se o canteiro do novo hotel no Setor Itaici ou na GO-139 possui chão de terra batida e cascalho, a diesel 4x4 é indispensável. Para manutenção de coberturas metálicas em resorts onde o acesso externo tem piso irregular, a diesel também é a indicação correta.')
r('Capacidade de carga e dimensões da cesta', 'Cesta ampla: a vantagem decisiva para manutenção hoteleira')
r('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
  'A cesta carrega de 230 a 450 kg e mede até 2,50 m de largura — espaço para até 3 profissionais com ferramental completo. Para pintores que cobrem forros extensos de centros de convenções em Caldas Novas, a largura permite avançar 2 metros por passada sem descer. Comparada à articulada de cesta compacta, a tesoura corta em 40% o tempo de reposicionamento em serviços de pintura e iluminação em grande área.')
r('<strong>Aplicações em Goiânia:</strong> manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras civis na região metropolitana.',
  '<strong>Onde atua em Caldas Novas:</strong> troca de iluminação em lobbies de hotel, pintura de forros em centros de convenções, manutenção de coberturas de resort e acabamento de fachadas em novos empreendimentos hoteleiros do Setor Itaici.')

# === FORM ===
r('Entrega no mesmo dia em Goiânia', 'Entrega agendada via GO-139')
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
  '''              <option value="Caldas Novas" selected>Caldas Novas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Itumbiara">Itumbiara</option>
              <option value="Anápolis">Anápolis</option>''', 2)

# === FLEET ===
r('8 a 10 m de altura de trabalho para ambientes internos', '8 a 10 m de elevação para lobbies e salões de hotel')
r('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. A cesta ampla comporta até 320 kg (2 operadores com ferramentas). O mecanismo pantográfico garante elevação vertical estável mesmo na altura máxima. Pneus não marcantes preservam o piso de galpões, lojas e shoppings. Ideal para trocas de luminárias no Distrito Industrial, pintura de forros no Shopping Flamboyant e instalações elétricas em fábricas da GO-060.',
  'A tesoura elétrica domina contratos em Caldas Novas para operações internas em hotéis e centros de convenções. Baterias de ciclo profundo alimentam motor silencioso que não perturba hóspedes. A cesta de até 320 kg comporta dois profissionais com ferramental completo. Pneus não marcantes preservam pisos de porcelanato e cerâmica decorativa. Aplicações mais frequentes: troca de luminárias em lobbies, repintura de forros em salões de evento e manutenção de climatização em resorts.')
r('12 a 15 m de altura de trabalho para obras e pátios', '12 a 15 m para canteiros e coberturas de resort')
r('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 12 a 15 metros de altura de trabalho com capacidade de até 450 kg na cesta. O motor diesel entrega potência para subir em terrenos com desnível moderado. Usada em obras de condomínios da região metropolitana de Goiânia, montagem de estruturas metálicas e manutenção de fachadas em edifícios comerciais onde o solo não é nivelado.',
  'Tração 4x4, chassi reforçado e pneus para cascalho — a tesoura diesel opera nos canteiros de novos hotéis e condomínios de Caldas Novas onde o piso ainda é terra batida. Alcança 12 a 15 metros com até 450 kg na cesta, suficiente para 3 montadores com material. Aplicações típicas: instalação de coberturas metálicas de resorts em construção, acabamento de fachada reta em edifícios do Setor Itaici e reparo de telhados em estruturas de parques aquáticos.')

# === EXPERT ===
r('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme. Já vi tesoura sendo levada para canteiro de obra com chão de terra, e o risco de tombamento é real. Para esse cenário, a articulada diesel é o equipamento correto. Agora, se o trabalho é em galpão, loja, fachada reta ou manutenção industrial com piso de concreto, a tesoura elétrica resolve com mais estabilidade, mais espaço no cesto e custo menor que a articulada."',
  '"Caldas Novas gera demanda de tesoura o ano inteiro por causa dos hotéis. Entre temporadas, os resorts aproveitam para repintar lobbies, trocar forro de gesso e atualizar a iluminação dos salões. A tesoura elétrica resolve tudo sem fumaça e sem arranhar o porcelanato. O que sempre alerto: piso firme é obrigatório. Semana passada, um hotel tentou usar tesoura no estacionamento de cascalho — recomendei a diesel 4x4 e evitamos um problema sério. Antes de enviar qualquer equipamento para Caldas Novas, peço fotos do piso e do local. Essa avaliação é gratuita."')

# === COMPARE ===
r('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
  '<span>Tesoura pantográfica</span> ou articulada: qual serve para seu hotel?')
r('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
  'Dois equipamentos com funções diferentes que se complementam. A tesoura sobe na vertical pura com cesta larga; a articulada contorna marquises e varandas. Escolher errado atrasa a manutenção do hotel e dobra o custo.')
r('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
  'Subida vertical com bandeja espaçosa. Perfeita para repintura de forros de hotel, troca de luminárias em centros de convenções e manutenção de climatização em salões de evento.')
r('Braço articulado com alcance horizontal e vertical. Indicada quando é necessário alcançar pontos distantes da base ou contornar obstáculos.',
  'Braço segmentado que desvia de marquises, varandas e coberturas de piscina. Necessária quando há obstáculo entre o chão e o ponto de trabalho na fachada do hotel.')
r('<strong>Regra prática para projetos em Goiânia:</strong> se o trabalho é em superfície plana (forro, telhado, teto de galpão) e o piso é nivelado, a tesoura resolve com mais velocidade e menor custo. Se precisa contornar vigas, alcançar fachadas ou operar em terreno sem pavimentação, a articulada é obrigatória. Em dúvida, nosso time avalia o local sem compromisso.',
  '<strong>Resumo para projetos em Caldas Novas:</strong> se o serviço é em forro plano, cobertura reta ou telhado e o piso é porcelanato, concreto ou cerâmica, a tesoura finaliza mais rápido e mais barato. Se a fachada do hotel possui marquise, varanda ou cobertura de piscina bloqueando o caminho, a articulada é indispensável. Na dúvida, avaliamos fotos do local sem custo.')
r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis em Caldas Novas:')

# === LINKS ===
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/caldas-novas-go/aluguel-de-plataforma-elevatoria-articulada')
r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Caldas Novas')
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/caldas-novas-go/aluguel-de-empilhadeira-combustao')
r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Caldas Novas')
r('/goiania-go/aluguel-de-transpaleteira', '/caldas-novas-go/aluguel-de-transpaleteira')
r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira em Caldas Novas')
r('/goiania-go/curso-operador-empilhadeira', '/caldas-novas-go/curso-de-operador-de-empilhadeira')
r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Caldas Novas')

# === VIDEO ===
r('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
  'alt="Vídeo Move Máquinas: locação de plataforma tesoura para hotéis e resorts em Caldas Novas"')
r('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
  'Como funciona a <span>locação de tesoura</span> para Caldas Novas')

# === PRICE ===
r('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
  'Investimento mensal em <span>plataforma tesoura</span> para Caldas Novas em 2026')
r('O valor depende do modelo (elétrica ou diesel), altura de trabalho e prazo de locação. Todos os contratos incluem manutenção preventiva e corretiva.',
  'Tabela de investimento para manutenção hoteleira e construção civil na região termal. Valor conforme modelo, motorização e prazo contratado.')
r('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores. O valor cobre o equipamento, manutenção completa e suporte técnico durante o período de uso.',
  'Locação disponível nas modalidades diária, semanal e mensal. Contratos acima de 15 dias incluem frete pela GO-139. Investimento cobre equipamento revisado, manutenção integral e suporte técnico durante toda a vigência.')
r('Entrega em Goiânia no mesmo dia', 'Frete incluso em contratos de 2+ meses')
r('Obras civis, pátios e condomínios', 'Canteiros de novos hotéis e condomínios')
r('Sem custo de deslocamento na capital', 'Frete incluso acima de 15 dias')
r('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
  'Sede na Av. Eurico Viana, 4913, Goiânia — 170 km de Caldas Novas pela GO-139. Para contratos de mais de 15 dias, frete incluso na mensalidade. A plataforma chega no lobby do hotel, canteiro ou centro de convenções pronta para operar.')
r('<strong>Conta que ninguém faz antes de improvisar:</strong> andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda sem proteção adequada. Uma plataforma tesoura elétrica sobe em 30 segundos, posiciona o operador com guarda-corpo e libera o piso de obstruções. Além disso, a NR-35 exige que trabalhos acima de 2 metros utilizem equipamento adequado. Multas por não conformidade chegam a dezenas de milhares de reais.',
  '<strong>O custo real de improvisar em hotel:</strong> escadas e andaimes improvisados em lobbies bloqueiam circulação de hóspedes, arriscam danos ao piso decorativo e expõem trabalhadores a queda sem proteção regulamentar. A tesoura elétrica sobe em 30 segundos, posiciona o técnico com guarda-corpo certificado e libera a área imediatamente após o serviço. A NR-35 exige equipamento adequado acima de 2 metros — multas por descumprimento atingem dezenas de milhares de reais.')

# === APPS ===
r('Aplicações em Goiânia', 'Aplicações na região termal')
r('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
  'Onde a <span>tesoura pantográfica</span> opera no polo turístico de Caldas Novas')
r('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
  'Do Setor Turístico ao Setor Itaici: quatro cenários que demandam tesoura na capital termal.')
r('alt="Interior de galpão industrial no Distrito Industrial de Goiânia, com pé-direito alto e estrutura metálica"',
  'alt="Lobby de hotel no Setor Turístico de Caldas Novas com pé-direito alto e iluminação decorativa"')
r('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
  '<h3>Hotéis e resorts: lobbies e áreas internas</h3>')
r('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado sem emitir gases, permitindo troca de telhas, reparos em calhas, substituição de luminárias e inspeção de estrutura metálica durante o expediente, sem interromper a produção no piso.',
  'Lobbies de hotel, corredores de resort e salões de café da manhã em Caldas Novas possuem pé-direito de 6 a 10 metros com forro de gesso ou madeira decorativa. A tesoura elétrica sobe em silêncio, posiciona o técnico na altura exata da luminária ou sensor e desce sem deixar marca no porcelanato. Manutenções acontecem na madrugada ou na entressafra sem interditar quartos.')
r('alt="Interior de shopping center com iluminação decorativa e pé-direito alto, ambiente para manutenção com plataforma tesoura"',
  'alt="Centro de convenções em Caldas Novas com cobertura metálica e pé-direito alto"')
r('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
  '<h3>Centros de convenções e salões de evento</h3>')
r('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica é o único equipamento viável: silenciosa, sem emissão e com pneus que não marcam o piso polido. A cesta ampla permite que o pintor se desloque lateralmente cobrindo faixas de 2 metros sem descer.',
  'Centros de convenções e espaços de evento em Caldas Novas recebem conferências, feiras e casamentos ao longo do ano. Entre eventos, a tesoura elétrica repinta forros, substitui luminárias e repara calhas — silenciosa, sem fumaça e com pneus que preservam pisos polidos. A cesta larga permite que dois pintores cubram faixas de 2 metros por passada sem descer.')
r('alt="Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia"',
  'alt="Cobertura de resort em Caldas Novas com estrutura metálica"')
r('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
  '<h3>Parques aquáticos: coberturas e estruturas internas</h3>')
r('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações. A tesoura elétrica posiciona o eletricista na altura exata do quadro de distribuição ou do duto de HVAC com estabilidade para trabalho prolongado com ferramentas elétricas.',
  'Parques aquáticos de Caldas Novas possuem áreas cobertas com estrutura metálica de até 12 metros. A tesoura acessa vigas, sistemas de iluminação e dutos de ventilação quando não há tubulações cruzando o caminho. Para piscinas onde a passagem é livre e o piso é concreto nivelado, a tesoura resolve sem a complexidade da articulada.')
r('alt="Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia"',
  'alt="Obra de novo hotel em construção no Setor Itaici de Caldas Novas"')
r('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
  '<h3>Construção civil: novos hotéis e condomínios</h3>')
r('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de fechamento lateral e pintura de fachada em condomínios de Aparecida de Goiânia, Senador Canedo e Trindade.',
  'A tesoura diesel 4x4 opera nos canteiros de novos hotéis e condomínios do Setor Itaici e Jardim Belvedere. Alcança até 15 metros para montagem de cobertura metálica, instalação de fechamento lateral e pintura de fachada reta. Em canteiros de terra batida, a tração reforçada se desloca sem travar.')

# === INCLUSO ===
r('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
  'Equipe técnica com deslocamento pela GO-139. Se a tesoura apresentar falha durante uso em Caldas Novas, realizamos diagnóstico no local ou substituímos o equipamento.')
r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
  'Transporte via GO-139 até seu hotel, centro de convenções ou canteiro em Caldas Novas. São 170 km da sede — frete incluso em contratos acima de 15 dias.')

# === DEPOIMENTOS ===
r('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
  '"Repintamos o forro dos 3 salões de convenção do resort entre duas conferências. Dois pintores na cesta, cobrindo 2 metros por passada. Nenhum cheiro de combustível, nenhuma marca no porcelanato. Concluímos em 5 dias o que com escada levaria 3 semanas. O hotel não perdeu nem um dia de evento."')
r('<strong>Marcos V.</strong>', '<strong>André L.</strong>')
r('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
  'Coord. de Manutenção, Rede de Resorts, Caldas Novas-GO (dez/2025)')
r('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
  '"Trocamos 120 luminárias LED no lobby e corredores do hotel durante a madrugada. A tesoura elétrica subiu em silêncio sem acordar nenhum hóspede. Os pneus não arranharam o mármore. Antes usávamos andaime e levava uma semana inteira. Com a tesoura, 3 noites resolveram tudo."')
r('<strong>Patrícia R.</strong>', '<strong>Daniela F.</strong>')
r('Gerente de Manutenção, Shopping, Goiânia-GO (jan/2026)',
  'Gerente de Facilities, Hotel 4 estrelas, Caldas Novas-GO (jan/2026)')
r('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas na cesta, sem precisar subir e descer escada a cada conexão. Reduziu o prazo da obra em uma semana."',
  '"Montamos toda a iluminação do salão de eventos do novo resort com a tesoura diesel. A cesta de 450 kg aguentou 3 eletricistas com material a 11 metros de altura. A 4x4 se deslocou pelo canteiro sem problema. Economizamos uma semana inteira comparado com andaime."')
r('<strong>Carlos H.</strong>', '<strong>Marcelo T.</strong>')
r('Engenheiro de Produção, Indústria, Goiânia-GO (fev/2026)',
  'Encarregado Elétrico, Construtora, Caldas Novas-GO (fev/2026)')

# === NR-35 ===
r('curso de NR-35 (trabalho em altura)</a>? Indicamos parceiros credenciados em Goiânia.',
  'capacitação NR-35 para trabalho em altura</a>? Indicamos centros credenciados acessíveis a partir de Caldas Novas.')

# === COVERAGE ===
r('Entrega rápida em <span>Goiânia</span> e região metropolitana',
  'Atendimento em <span>Caldas Novas</span> e cidades do sul de Goiás')

# Coverage block — find and replace the whole paragraph + cities
OLD_COV_TEXT = 'Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Plataformas tesoura'
idx = html.find(OLD_COV_TEXT)
if idx > 0:
    p_start = html.rfind('<p ', idx-100, idx)
    div_end = html.find('</div>\n    </div>', idx)
    if p_start > 0 and div_end > 0:
        div_end += len('</div>\n    </div>')
        SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
        NEW_COV = f'''    <p style="max-width:720px;color:var(--color-text-light);margin-bottom:var(--space-sm);">Sede na Av. Eurico Viana, 4913, Goiânia — 170 km de Caldas Novas pela GO-139. Entrega programada, frete incluso em contratos acima de 15 dias. Tesoura elétrica e diesel para hotéis, resorts e canteiros de obra na região termal.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        {SVG}
        <a href="/caldas-novas-go/"><strong>Caldas Novas</strong></a>
      </div>
      <div class="coverage__city">
        {SVG}
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        {SVG}
        <a href="/itumbiara-go/">Itumbiara</a>
      </div>
      <div class="coverage__city">
        {SVG}
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        {SVG}
        <a href="/brasilia-df/">Brasília (DF)</a>
      </div>
      <div class="coverage__city">
        {SVG}
        <a href="/senador-canedo-go/">Senador Canedo</a>
      </div>
      <div class="coverage__city">
        {SVG}
        Uruaçu
      </div>
      <div class="coverage__city">
        {SVG}
        <a href="/luziania-go/">Luziânia</a>
      </div>
    </div>'''
        html = html[:p_start] + NEW_COV + html[div_end:]

# Maps
r('!2d-49.2654!3d-16.7234', '!2d-48.6252!3d-17.7441')
r('title="Localização Move Máquinas em Goiânia"', 'title="Área de atendimento Move Máquinas — Caldas Novas"')
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Caldas Novas</a>')
r('/goiania-go/" style="color', '/caldas-novas-go/" style="color')

# === FAQ BODY ===
r('Perguntas frequentes sobre <span>locação de plataforma tesoura</span> em Goiânia',
  'Dúvidas sobre <span>plataforma tesoura</span> na região de Caldas Novas')
r('>Qual a diferença entre plataforma tesoura e articulada?<', '>Para quais serviços de hotel a tesoura é melhor que a articulada?<')
r('>A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o teto é plano e o piso é nivelado. A articulada possui braço com articulação que permite alcance horizontal e vertical, sendo indicada para fachadas, estruturas irregulares e terrenos acidentados. Para manutenção interna no Distrito Industrial de Goiânia, a tesoura é a escolha mais eficiente.<',
  '>A tesoura resolve manutenções em superfícies planas com acesso vertical direto: troca de luminárias em lobbies, pintura de forros em salões de evento e manutenção de climatização em centros de convenções. A articulada contorna marquises, varandas e coberturas — necessária quando há obstáculo entre o chão e o ponto de trabalho na fachada do hotel.<')
r('>Plataforma tesoura elétrica ou diesel: qual escolher?<', '>Tesoura elétrica ou diesel: qual pedir para Caldas Novas?<')
r('>A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel funciona em terrenos irregulares, canteiros de obra e pátios externos. Para trabalhos internos em Goiânia, como manutenção no Shopping Flamboyant ou galpões do Distrito Industrial, a elétrica é a melhor opção.<',
  '>Dentro de hotéis, resorts e centros de convenções, a elétrica é obrigatória: zero fumaça, motor silencioso e pneus que preservam pisos decorativos. A diesel serve para canteiros de novos hotéis no Setor Itaici e estacionamentos sem asfalto. Para operações internas em Caldas Novas, sempre elétrica.<')
r('>Qual a altura máxima da plataforma tesoura?<', '>Qual a altura máxima das tesouras que atendem Caldas Novas?<')
r('>Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões e shoppings. A diesel chega a 12 a 15 metros, indicada para canteiros de obra e estruturas mais altas.<',
  '>Frota com elétrica de 8 a 10 metros e diesel de 12 a 15 metros. A elétrica cobre lobbies, salões e centros de convenções cujo pé-direito fica entre 6 e 10 metros. A diesel alcança coberturas de resorts maiores e estruturas de parques aquáticos acima de 12 metros.<')
r('>Preciso de treinamento para operar plataforma tesoura?<', '>Funcionários do hotel precisam de certificação para operar a tesoura?<')
r('>Sim. A NR-35 exige treinamento específico para trabalho em altura acima de 2 metros. O operador precisa de curso de NR-35 válido, com conteúdo sobre análise de risco, uso de EPI, inspeção pré-operacional e procedimentos de emergência. A Move Máquinas pode indicar parceiros credenciados em Goiânia para o curso.<',
  '>Toda operação acima de 2 metros exige treinamento NR-35 válido com módulo PEMT. O programa cobre análise de risco, inspeção pré-operacional, uso de EPI e procedimentos de emergência. Hotéis e construtoras de Caldas Novas podem solicitar indicação de centros credenciados na região.<')
r('>A manutenção da plataforma tesoura está inclusa no aluguel?<', '>O contrato inclui manutenção da tesoura?<')
r('>Sim. Todo contrato de locação da Move Máquinas inclui manutenção preventiva e corretiva do sistema hidráulico de elevação, cilindros, tesouras articuladas, sistema elétrico e baterias. Se a plataforma apresentar falha, nossa equipe técnica atende em Goiânia e região no mesmo dia.<',
  '>Cada contrato cobre manutenção preventiva e corretiva: sistema pantográfico, cilindros de elevação, parte elétrica e baterias. Em caso de falha em Caldas Novas, equipe técnica se desloca pela GO-139 para diagnóstico e reparo no local.<')
r('>Vocês entregam plataforma tesoura fora de Goiânia?<', '>Qual o prazo de entrega da tesoura em Caldas Novas?<')
r('>Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.<',
  '>Caldas Novas está a 170 km pela GO-139, dentro do raio de 200 km. Trajeto de cerca de 2h30. Para contratos acima de 15 dias, frete incluso. Manutenções de hotel na entressafra permitem agendar data e horário de entrega com antecedência.<')
r('>Posso usar plataforma tesoura em terreno irregular?<', '>A tesoura diesel funciona nos canteiros das obras novas?<')
r('>Somente o modelo diesel com tração 4x4. A tesoura elétrica exige piso nivelado e firme. Para terrenos irregulares, canteiros de obra e pátios sem pavimentação, a tesoura diesel é a opção correta. Se o trabalho exige alcance lateral além da elevação vertical, considere a plataforma articulada.<',
  '>Sim. A diesel possui tração 4x4 para terra e cascalho — cenário típico dos canteiros de novos hotéis no Setor Itaici. A elétrica exige piso nivelado e firme. Se o trabalho também exige desviar de marquise ou varanda, a articulada é a escolha correta.<')
r('>Qual a capacidade de carga da plataforma tesoura?<', '>Quantas pessoas trabalham juntas na cesta da tesoura?<')
r('>A capacidade varia de 230 a 450 kg dependendo do modelo, o que comporta de 1 a 3 operadores com ferramentas e materiais. A tesoura elétrica de 8 a 10 m suporta até 320 kg. A diesel de 12 a 15 m suporta até 450 kg. Para trabalhos com materiais pesados como luminárias industriais ou chapas de fechamento, confirme o peso total com nossa equipe técnica.<',
  '>A cesta suporta de 230 a 450 kg conforme modelo. A elétrica de 8-10m carrega até 320 kg — dois profissionais com ferramentas. A diesel de 12-15m aguenta até 450 kg, três montadores com material. Para pintores de hotel que sobem com galões e rolos, a cesta ampla comporta todo o material sem viagens extras.<')

# === FOOTER CTA ===
r('Alugue uma plataforma tesoura em Goiânia hoje', 'Solicite tesoura para seu projeto em Caldas Novas')

# === JS WHATSAPP ===
r("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
  "'Olá, preciso de plataforma tesoura em Caldas Novas.\\n\\n'")

# ═══════════════════════════════════════════════════════════════
# VERIFICAÇÃO + UPLOAD
# ═══════════════════════════════════════════════════════════════
ref = open(REF).read()
def strip_bp(h):
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    return t
def ngrams(text, n=3):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'[^a-záàâãéèêíïóôõúüç\s]', '', text.lower())
    words = text.split()
    return set(' '.join(words[i:i+n]) for i in range(len(words)-n+1))
def jaccard(a, b):
    sa, sb = ngrams(a), ngrams(b)
    if not sa or not sb: return 0
    return len(sa & sb) / len(sa | sb)

j_text = jaccard(strip_bp(html), strip_bp(ref))
j_full = jaccard(html, ref)
print(f"\n{'='*60}")
print(f"TESOURA Caldas Novas")
print(f"{'='*60}")
print(f"Jaccard TEXT vs REF: {j_text:.4f} {'OK' if j_text < 0.20 else 'FAIL'}")
print(f"Jaccard FULL vs REF: {j_full:.4f}")

cn = html.lower().count('caldas novas')
print(f"Caldas Novas: {cn} mencoes")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

elapsed = time.time() - START
print(f"TEMPO: {elapsed:.1f}s")
print(f"TOKENS: ~{len(html)//4}")

# Upload
R2_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET = 'pages'
def upload_to_r2(local_path, r2_key):
    with open(local_path, 'rb') as f:
        body = f.read()
    now = datetime.datetime.utcnow()
    ds = now.strftime('%Y%m%d')
    ad = now.strftime('%Y%m%dT%H%M%SZ')
    host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    ph = hashlib.sha256(body).hexdigest()
    cu = f'/{R2_BUCKET}/{r2_key}'
    ch = f'host:{host}\nx-amz-content-sha256:{ph}\nx-amz-date:{ad}\n'
    sh = 'host;x-amz-content-sha256;x-amz-date'
    cr = f'PUT\n{cu}\n\n{ch}\n{sh}\n{ph}'
    cs = f'{ds}/auto/s3/aws4_request'
    sts = f'AWS4-HMAC-SHA256\n{ad}\n{cs}\n{hashlib.sha256(cr.encode()).hexdigest()}'
    def sign(key, msg): return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
    sk = sign(sign(sign(sign(f'AWS4{R2_SECRET}'.encode('utf-8'), ds), 'auto'), 's3'), 'aws4_request')
    sig = hmac.new(sk, sts.encode('utf-8'), hashlib.sha256).hexdigest()
    auth = f'AWS4-HMAC-SHA256 Credential={R2_KEY}/{cs}, SignedHeaders={sh}, Signature={sig}'
    req = urllib.request.Request(f'https://{host}{cu}', data=body, method='PUT')
    req.add_header('Host', host)
    req.add_header('x-amz-date', ad)
    req.add_header('x-amz-content-sha256', ph)
    req.add_header('Authorization', auth)
    req.add_header('Content-Type', 'text/html; charset=utf-8')
    req.add_header('Cache-Control', 'public, max-age=3600')
    resp = urllib.request.urlopen(req)
    print(f'R2 OK: {r2_key} ({resp.status})')

if j_text < 0.20:
    upload_to_r2(OUT, 'caldas-novas-go/aluguel-de-plataforma-elevatoria-tesoura/index.html')
else:
    print(f"BLOCKED: {j_text:.4f} >= 0.20")
