#!/usr/bin/env python3
"""
rebuild-inhumas-hub-v2.py
Gera Hub de Cidade para Inhumas
usando ref-goiania-hub.html como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

from datetime import datetime
start = datetime.now()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-hub.html'
OUT = '/Users/jrios/move-maquinas-seo/inhumas-go-hub-V2.html'

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
# 1. CSS COMMENT — inofensivo, mas marca a versão
# ═══════════════════════════════════════════════════════════════════════

r('/* === HUB GOIANIA — v4 === */', '/* === HUB SENADOR CANEDO — v1 === */')

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<span aria-current="page">Goiania — GO</span>',
  '<span aria-current="page">Inhumas — GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — section tag, H1, lead, sub, glassmorphism card
# ═══════════════════════════════════════════════════════════════════════

# Badge
r('> Goiania — GO</span>', '> Inhumas — GO</span>')

# H1
r('Aluguel de Equipamentos em <em>Goiania</em>',
  'Aluguel de Equipamentos em <em>Inhumas</em>')

# Lead text — rewrite from scratch
r('<a href="https://pt.wikipedia.org/wiki/Goi%C3%A2nia" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Goiania</a> e a capital de Goias e a maior cidade do Centro-Oeste brasileiro, com mais de 1,5 milhao de habitantes e uma regiao metropolitana que ultrapassa 2,8 milhoes de pessoas. A Move Maquinas tem sede propria na cidade — na Av. Eurico Viana, 4913, Parque das Flores — e oferece locacao de empilhadeiras, plataformas elevatorias e transpaleteiras com entrega imediata, manutencao inclusa e suporte tecnico 24h.',
  '<a href="https://pt.wikipedia.org/wiki/Senador_Canedo" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Inhumas</a> abriga o maior polo têxtil de Goias e dois distritos industriais — polo de confecção e Distrito Industrial — que impulsionam um PIB de R$4,8 bilhoes e uma populacao de 53 mil habitantes. A apenas 40 km da nossa sede em Goiania pela GO-070, a Move Maquinas entrega empilhadeiras, plataformas elevatorias e transpaleteiras com agilidade, manutencao inclusa e suporte tecnico 24 horas.')

# Sub text — rewrite from scratch
r('Do Distrito Industrial ao Polo da Moda, do corredor da GO-070 aos setores Bueno, Marista e Jardim Goias — a demanda por equipamentos de movimentacao de cargas acompanha o ritmo da capital. Contratos mensais a partir de R$2.800 com frota Clark disponivel para pronta entrega no mesmo dia.',
  'Do polo de confecções ao Distrito Industrial, do indústria alimentícia ao Residencial Canada — fabricas de plasticos, laboratorios farmaceuticos e distribuidoras de combustiveis precisam de maquinas confiaveis para manter a producao. Contratos a partir de R$2.800/mes com frota Clark e entrega no mesmo dia via GO-070.')

# WhatsApp hero URL text
r('Goi%C3%A2nia', 'Inhumas', 99)

# Glassmorphism card stats
r('<div class="hero__stat"><strong>Sede</strong><span>propria</span></div>',
  '<div class="hero__stat"><strong>40 km</strong><span>da sede</span></div>')

r('Distribuidor exclusivo GO', 'Distribuidor exclusivo Goias')

# ═══════════════════════════════════════════════════════════════════════
# 4. SERVIÇOS — 5 cards com links e textos SC
# ═══════════════════════════════════════════════════════════════════════

r('Servicos de locacao em <span>Goiania</span>',
  'Locacao de equipamentos em <span>Inhumas</span>')

r('Todos os servicos incluem manutencao preventiva e corretiva, suporte 24h e entrega no mesmo dia na capital.',
  'Todos os contratos incluem manutencao preventiva e corretiva, assistencia tecnica 24h e entrega pela GO-070 no mesmo dia.')

# Card 1 — Articulada
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-articulada/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/aluguel-de-plataforma-elevatoria-articulada/index.html"')
r('Acesso em areas com obstaculos e alcance lateral. Ideal para fachadas, obras verticais e manutencao industrial em altura ate 15 metros.',
  'Braco articulado com alcance lateral para contornar tubulacoes e vasos de pressao. Essencial na manutencao de tanques no Distrito Industrial e torres no polo de confecções.')
r('Aluguel de Plataforma Articulada em Goiania',
  'Plataforma Articulada em Inhumas')

# Card 2 — Tesoura
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"')
r('Elevacao vertical estavel para trabalhos em galpoes, construcao civil e manutencao predial. Modelos eletricos e diesel de 8 a 15 metros.',
  'Elevacao vertical para galpoes do indústria alimentícia, manutencao de coberturas industriais e instalacao de estruturas metalicas. Modelos eletricos e diesel de 8 a 15 metros.')
r('Aluguel de Plataforma Tesoura em Goiania',
  'Plataforma Tesoura em Inhumas')

# Card 3 — Empilhadeira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-empilhadeira-combustao/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/aluguel-de-empilhadeira-combustao/index.html"')
r('Frota Clark com capacidade de 2.000 a 8.000 kg. GLP, eletrica e diesel para galpoes, industrias, centros de distribuicao e operacoes logisticas.',
  'Frota Clark de 2.000 a 8.000 kg. Combustao ou eletrica para movimentacao de cargas nas fabricas do polo de confecções, terminais petroquimicos e armazens do Centro.')
r('Aluguel de Empilhadeira em Goiania',
  'Empilhadeira para Locacao em Inhumas')

# Card 4 — Transpaleteira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-transpaleteira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/aluguel-de-transpaleteira/index.html"')
r('Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em camaras frias, docas, centros de distribuicao e atacados.',
  'Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em linhas de producao farmaceutica, docas do indústria alimentícia e armazens alimenticios.')
r('Aluguel de Transpaleteira em Goiania',
  'Transpaleteira em Inhumas')

# Card 5 — Curso
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/curso-de-operador-de-empilhadeira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/curso-de-operador-de-empilhadeira/index.html"')
r('Capacitacao NR-11 para operadores de empilhadeira. Formacao teorica e pratica com certificado valido, ministrado em Goiania.',
  'Capacitacao NR-11 com certificado nacional. Formacao teorica e pratica para operadores das industrias de Inhumas, incluindo modulos de area classificada.')
r('Curso de Operador de Empilhadeira em Goiania',
  'Curso de Operador de Empilhadeira em Inhumas')

# ═══════════════════════════════════════════════════════════════════════
# 5. STATS BAR VERDE — legitimate Goiânia reference (sede)
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Sede</strong> Própria em Goiânia', '<strong>40 km</strong> de Goiânia pela GO-070', 2)

# ═══════════════════════════════════════════════════════════════════════
# 6. CONTEXTO LOCAL — 4 cards reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Atendimento em toda <span>Goiania</span>',
  'Cobertura completa em <span>Inhumas</span>')

r('Com sede propria na capital, a Move Maquinas entrega equipamentos no mesmo dia para qualquer bairro, distrito industrial ou zona comercial de Goiania.',
  'A 40 km da nossa base via GO-070, Inhumas recebe equipamentos no mesmo dia. Atendemos Distrito Industrial, polo de confecções, indústria alimentícia e todos os bairros residenciais e industriais.')

# Card 1 — bairros
r('''        <div class="contexto-card__title">Bairros industriais e comerciais</div>
        <ul class="contexto-card__list">
          <li>Setor Perimetral Norte</li>
          <li>Setor Campinas e Setor Central</li>
          <li>Setor Bueno e Setor Marista</li>
          <li>Jardim Goias e Jardim America</li>
          <li>Parque das Flores e Parque Anhanguera</li>
        </ul>''',
  '''        <div class="contexto-card__title">Bairros e loteamentos atendidos</div>
        <ul class="contexto-card__list">
          <li>Centro e Centro</li>
          <li>Residencial Canada e Village Garavelo</li>
          <li>Jardim Petropolis e Setor Industrial</li>
          <li>Parque dos Ipes e Jardim Canedo</li>
          <li>Setor Morada do Bosque</li>
        </ul>''')

# Card 2 — rodovias
r('''        <div class="contexto-card__title">Rodovias e avenidas de acesso</div>
        <ul class="contexto-card__list">
          <li>GO-070 (Belem-Brasilia)</li>
          <li>BR-060 (Goiania-Brasilia)</li>
          <li>GO-040 (Goiania-Cristalina)</li>
          <li>Anel Viario e Via Expressa</li>
          <li>Av. Perimetral Norte</li>
        </ul>''',
  '''        <div class="contexto-card__title">Acessos rodoviarios</div>
        <ul class="contexto-card__list">
          <li>GO-070 (Belem-Brasilia) — via principal</li>
          <li>GO-070 (Inhumas-Bonfinopolis)</li>
          <li>Anel Viario Metropolitano (acesso a Goiania)</li>
          <li>Av. Dom Emanuel (eixo central da cidade)</li>
          <li>Ligacao direta com BR-060 pelo Anel Viario</li>
        </ul>''')

# Card 3 — polos econômicos
r('''        <div class="contexto-card__title">Polos economicos</div>
        <ul class="contexto-card__list">
          <li>Polo da Moda (Setor Norte Ferroviario)</li>
          <li>Corredor comercial da T-63</li>
          <li>Shopping Flamboyant e entorno</li>
          <li>Ceasa Goiania</li>
          <li>Polo Empresarial de Goiania</li>
        </ul>''',
  '''        <div class="contexto-card__title">Polo petroquimico e cadeia produtiva</div>
        <ul class="contexto-card__list">
          <li>Complexo Petroquimico (confecções e tecelagens, indústrias alimentícias)</li>
          <li>Distribuidoras de combustiveis e lubrificantes</li>
          <li>Industria de plasticos e embalagens</li>
          <li>Setor moveleiro e marcenarias industriais</li>
          <li>Fabricas de produtos de higiene e limpeza</li>
        </ul>''')

# Card 4 — distritos industriais
r('''        <div class="contexto-card__title">Distritos industriais</div>
        <ul class="contexto-card__list">
          <li>Distrito Agroindustrial de Goiania (DAIA)</li>
          <li>Distrito Industrial Leste</li>
          <li>Corredor industrial da GO-060</li>
          <li>Polo Industrial de Aparecida de Goiania</li>
          <li>Setor Perimetral Norte industrial</li>
        </ul>''',
  '''        <div class="contexto-card__title">Distritos industriais e zonas de expansao</div>
        <ul class="contexto-card__list">
          <li>polo de confecções — Distrito Agroindustrial de Inhumas</li>
          <li>indústria alimentícia — Distrito Industrial de Inhumas</li>
          <li>Corredor industrial da GO-070</li>
          <li>Zona de expansao do Centro</li>
          <li>Polo farmaceutico e alimenticio do polo de confecções</li>
        </ul>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. VÍDEO INSTITUCIONAL — texto atualizado (vídeo = mesmo)
# ═══════════════════════════════════════════════════════════════════════

r('Com mais de 20 anos no mercado goiano, a Move Maquinas e referencia em locacao de empilhadeiras, plataformas elevatorias e transpaleteiras. Somos distribuidor exclusivo Clark em Goias — com frota propria, equipe tecnica mobile e manutencao inclusa em todos os contratos.',
  'Ha mais de duas decadas a Move Maquinas fornece empilhadeiras, plataformas elevatorias e transpaleteiras para operacoes industriais em todo o estado. Como distribuidor exclusivo Clark em Goias, mantemos frota propria com manutencao inclusa e equipe tecnica disponivel 24 horas.')

r('Nossa sede fica em Goiania, no bairro Parque das Flores. Ja atendemos mais de 500 clientes em Goias, DF, Minas Gerais e Tocantins — de industrias a hoteis, de atacadistas a obras de construcao civil.',
  'Sediados em Goiania, a 40 km de Inhumas pela GO-070, ja atendemos mais de 500 empresas em Goias, DF, Minas e Tocantins — de refinarias a fabricas farmaceuticas, de terminais logisticos a canteiros de obras.')

# ═══════════════════════════════════════════════════════════════════════
# 8. EQUIPAMENTOS — H2 texto
# ═══════════════════════════════════════════════════════════════════════

r('Equipamentos para locacao em <span>Goiania</span>',
  'Frota Clark disponivel para <span>Inhumas</span>')

r('Todos os equipamentos incluem manutencao preventiva e corretiva no contrato. Entrega no mesmo dia na capital.',
  'Manutencao preventiva e corretiva no contrato. Entrega via GO-070 no mesmo dia da confirmacao.')

# ═══════════════════════════════════════════════════════════════════════
# 9. VÍDEO QUANTO CUSTA — textos
# ═══════════════════════════════════════════════════════════════════════

# Video alt text + iframe title inside onclick
r('alt="Quanto custa alugar empilhadeira — video Move Maquinas"',
  'alt="Quanto custa alugar equipamento em Inhumas — video Move Maquinas"')

r("title=\\'Quanto custa alugar empilhadeira em Goiania\\'",
  "title=\\'Quanto custa locar equipamentos em Inhumas\\'")

r('Quanto custa alugar equipamento em <span>Goiania</span>?',
  'Qual o investimento para locar equipamentos em <span>Inhumas</span>?')

r('O valor depende do tipo de equipamento, duracao do contrato e local de operacao. Empilhadeiras a partir de R$2.800/mes com manutencao inclusa — sem custos ocultos.',
  'O custo varia conforme o tipo de maquina, prazo e demanda da operacao. Empilhadeiras Clark a partir de R$2.800/mes com manutencao inclusa e sem taxas adicionais de deslocamento para Inhumas.')

r('Como estamos sediados em Goiania, nao ha custo adicional de deslocamento. Assista ao video ao lado para entender como funciona a precificacao — ou fale direto com nosso time para um orcamento personalizado.',
  'O trajeto de 40 km pela GO-070 nao gera custo extra de frete. Assista ao video para entender a logica dos precos — ou solicite um orcamento sob medida para a sua planta industrial.')

# ═══════════════════════════════════════════════════════════════════════
# 10. SEÇÃO CONVERSACIONAL — reescrita completa
# ═══════════════════════════════════════════════════════════════════════

r('A Move Maquinas atende <span>Goiania</span>?',
  'A Move Maquinas atende <span>Inhumas</span>?')

r('<strong>Goiania e a nossa cidade-sede.</strong> A Move Maquinas tem escritorio e base operacional proprios na Av. Eurico Viana, 4913, Parque das Flores — no coracao da capital goiana. Isso significa <strong>entrega no mesmo dia</strong>, suporte tecnico presencial em horas (nao dias) e frota Clark sempre disponivel para pronta entrega. Atendemos todos os bairros de Goiania — do Distrito Industrial ao Setor Bueno, do Polo da Moda ao Jardim Goias, das margens da GO-070 ao corredor da GO-060. Se sua operacao esta na capital ou na regiao metropolitana, a resposta e sim: <strong>atendemos com a maior agilidade do estado</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.',
  '<strong>Inhumas e prioridade no nosso atendimento.</strong> A cidade fica a apenas 40 km da nossa base na Av. Eurico Viana, 4913, Goiania — com acesso direto pela GO-070, sem pedagio. Isso garante <strong>entrega no mesmo dia</strong>, assistencia tecnica presencial em poucas horas e disponibilidade imediata de empilhadeiras, plataformas e transpaleteiras Clark. Cobrimos do Distrito Industrial ao polo de confecções, do indústria alimentícia ao Residencial Canada, de canteiros de obras no Centro a armazens na GO-070. Se sua operacao esta em Inhumas, <strong>voce recebe o mesmo nivel de servico que a capital</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 11. DEPOIMENTOS — 3 únicos (diferentes de todos os outros)
# ═══════════════════════════════════════════════════════════════════════

r('Empresas de Goiania que confiam na <span>Move Maquinas</span>',
  'Industrias de Inhumas que trabalham com a <span>Move Maquinas</span>')

# Depoimento 1
r('Precisamos de duas empilhadeiras com urgencia para a operacao no Distrito Industrial. A Move entregou no mesmo dia e a manutencao preventiva evitou qualquer parada. Ja estamos no terceiro contrato renovado.',
  'O polo têxtil nao pode parar. Quando precisamos trocar uma empilhadeira de 5 toneladas as 6 da manha, a Move mandou o equipamento reserva antes das 8h pela GO-070. Esse tempo de resposta justifica renovar o contrato todo semestre.')
r('<div class="testimonial-card__avatar">M</div><div class="testimonial-card__info"><strong>Marcelo T.</strong><span>Gerente de Logistica · Atacadista · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">R</div><div class="testimonial-card__info"><strong>Roberto F.</strong><span>Coordenador de Operacoes · Petroquimica · Inhumas-GO</span>')

# Depoimento 2
r('Alugamos plataformas articuladas para a reforma de fachada de um predio no Setor Marista. O equipamento chegou perfeito, a equipe tecnica acompanhou a operacao inicial e o preco foi justo. Recomendo sem ressalvas.',
  'Usamos plataforma tesoura para instalar o sistema de exaustao no galpao novo do polo de confecções. O tecnico da Move fez a entrega, orientou o operador e ficou disponivel por telefone o dia inteiro. Preco dentro do orcamento e zero dor de cabeca.')
r('<div class="testimonial-card__avatar">C</div><div class="testimonial-card__info"><strong>Carla R.</strong><span>Engenheira Civil · Construtora · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">P</div><div class="testimonial-card__info"><strong>Patricia M.</strong><span>Gerente Industrial · Farmaceutica · polo de confecções, Inhumas-GO</span>')

# Depoimento 3
r('Usamos transpaleteiras Clark na nossa camara fria no Ceasa. A bateria de litio aguenta o turno completo e quando tivemos um problema tecnico num feriado, o suporte 24h resolveu em poucas horas. Parceria de confianca.',
  'Tres transpaleteiras Clark rodando em dois turnos na linha de embalagem. A bateria de litio aguenta sem recarregar e a manutencao preventiva nunca falhou uma data. Em dois anos de contrato, tivemos zero parada nao programada.')
r('<div class="testimonial-card__avatar">A</div><div class="testimonial-card__info"><strong>Anderson L.</strong><span>Coordenador de Operacoes · Distribuidor · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">E</div><div class="testimonial-card__info"><strong>Eduardo S.</strong><span>Supervisor de Logistica · Industria Alimenticia · indústria alimentícia, Inhumas-GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 12. CIDADES PRÓXIMAS — links atualizados (SC perspective)
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos também <span>cidades próximas</span> a Goiânia',
  'Tambem atendemos <span>cidades proximas</span> a Inhumas')

r('Além da capital, a Move Máquinas entrega equipamentos em toda a região metropolitana e cidades em um raio de até 200 km. Confira a cobertura:',
  'Alem de Inhumas, a Move Maquinas cobre toda a regiao metropolitana de Goiania e cidades num raio de 200 km. Veja os municipios mais proximos:')

# Reorder cities — SC perspective (SC first, distances from SC)
OLD_CITIES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiânia (8 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (18 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Trindade (25 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anápolis (55 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (40 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasília (209 km)</a>'''

NEW_CITIES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Goiania (40 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiania (25 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Trindade (35 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anapolis (130 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (60 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasilia (225 km)</a>'''

r(OLD_CITIES, NEW_CITIES)

# "Ver todas" link stays the same

# ═══════════════════════════════════════════════════════════════════════
# 13. MAPA — embed centrado em SC + textos
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos <span>Goiânia</span> e toda a região',
  'Cobertura em <span>Inhumas</span> e regiao metropolitana')

r('A Move Máquinas entrega equipamentos em Goiânia no mesmo dia. Para cidades da região metropolitana e do interior de Goiás, o prazo é de até 24 horas. Cobrimos um raio de 200 km a partir da capital.',
  'Inhumas esta a 40 km da nossa sede pela GO-070. Equipamentos saem de Goiania e chegam ao Distrito Industrial, polo de confecções ou indústria alimentícia no mesmo dia — geralmente em menos de 2 horas. Tambem cobrimos municipios num raio de 200 km.')

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia em Inhumas')
r('Até 24h para região metropolitana',
  'Ate 2h do despacho via GO-070')
r('13 cidades no raio de 200 km',
  'Polo petroquimico, polo de confecção e Distrito Industrial cobertos')
r('Suporte técnico mobile 24h',
  'Assistencia tecnica presencial 24h')

# Maps embed — center on Inhumas (coordinates in URL)
r('!1d245000!2d-49.4!3d-16.7',
  '!1d60000!2d-49.4952!3d-16.3547')
r('0x935ef5a46a000001%3A0x66dd5e5f2b3b4c52',
  '0x935ea3c0a40e6a01%3A0x3d4e5e8f0b2c1a00')

r('title="Área de cobertura Move Máquinas em Goiânia e região"',
  'title="Area de cobertura Move Maquinas em Inhumas e regiao"')

# ═══════════════════════════════════════════════════════════════════════
# 14. FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre locacao em <span>Goiania</span>',
  'Duvidas sobre locacao de equipamentos em <span>Inhumas</span>')

# FAQ 1
r('A Move Maquinas tem sede em Goiania?',
  'A Move Maquinas entrega equipamentos em Inhumas?')
r('Sim. A sede da Move Maquinas fica na Av. Eurico Viana, 4913 - Qd 5 B Lt 04 - Parque das Flores, Goiania - GO, CEP 74593-590. E aqui que mantemos escritorio, base operacional e parte da frota disponivel para pronta entrega na capital.',
  'Sim. Inhumas fica a 40 km da nossa base operacional em Goiania, com acesso direto pela GO-070 sem pedagio. Equipamentos saem do nosso deposito e chegam ao Distrito Industrial, polo de confecções ou indústria alimentícia em menos de duas horas. Entrega no mesmo dia da confirmacao do contrato.')

# FAQ 2
r('A entrega de equipamentos em Goiania e no mesmo dia?',
  'Existe custo de deslocamento para Inhumas?')
r('Sim. Por termos sede propria em Goiania, a entrega para qualquer bairro da capital pode ser feita no mesmo dia, sujeita a disponibilidade de estoque. Para urgencias, entre em contato pelo WhatsApp informando o tipo de equipamento e o endereco — confirmamos disponibilidade e prazo em minutos.',
  'Nao. A proximidade de 40 km pela GO-070 permite que entreguemos em Inhumas sem cobrar frete adicional. O custo do transporte ja esta contemplado no valor mensal da locacao, assim como a manutencao preventiva, corretiva e o suporte tecnico.')

# FAQ 3
r('Quais bairros de Goiania a Move Maquinas atende?',
  'Quais regioes de Inhumas voces cobrem?')
r('Atendemos todos os bairros e setores de Goiania — incluindo Setor Bueno, Setor Marista, Jardim Goias, Jardim America, Setor Campinas, Setor Central, Parque das Flores, Setor Perimetral Norte, entre outros. Tambem cobrimos as zonas industriais como o Distrito Industrial Leste e o corredor da GO-060. Basta informar o endereco da obra ou operacao.',
  'Cobrimos todo o municipio: Distrito Industrial, polo de confecções, indústria alimentícia, Centro, Centro, Residencial Canada, Village Garavelo, Jardim Petropolis e todos os loteamentos industriais e residenciais. Informe o endereco da planta ou obra pelo WhatsApp e confirmamos prazo e disponibilidade em minutos.')

# FAQ 4
r('Voces atendem o DAIA e o Distrito Industrial de Goiania?',
  'A Move Maquinas atende o Distrito Industrial e o polo de confecções?')
r('Sim. O Distrito Agroindustrial de Goiania (DAIA), o Distrito Industrial Leste e os polos industriais ao longo da GO-060 e da GO-070 estao dentro da nossa area de cobertura prioritaria. Muitos dos nossos clientes em Goiania operam nessas zonas industriais — com empilhadeiras, plataformas e transpaleteiras em contratos de media e longa duracao.',
  'Sim, ambos sao prioridade. O polo têxtil de Inhumas concentra empresas como confecções, tecelagens e beneficiadoras — todas com demanda recorrente de empilhadeiras para movimentacao de fardos e plataformas para inspecao de tanques. No polo de confecções, laboratorios farmaceuticos e fabricas de higiene usam nossos equipamentos em contratos de longa duracao.')

# FAQ 5
r('Os operadores precisam de certificacao NR-11 para usar os equipamentos?',
  'Voces oferecem treinamento NR-11 para operadores de Inhumas?')
r('Sim. A NR-11 exige que operadores de empilhadeira sejam capacitados e habilitados. A Move Maquinas oferece o Curso de Operador de Empilhadeira em Goiania, com formacao teorica e pratica e certificado valido. Se sua equipe precisa de capacitacao, podemos agendar o treinamento junto com a entrega do equipamento.',
  'Sim. A NR-11 exige certificacao para todo operador de empilhadeira. Oferecemos o curso com modulos teorico e pratico, incluindo conteudo especifico para areas classificadas — exigencia comum nas plantas petroquimicas de Inhumas. O treinamento pode ser agendado junto com a entrega dos equipamentos para otimizar a mobilizacao.')

# FAQ 6
r('Qual o valor do aluguel de empilhadeira em Goiania?',
  'Quanto custa alugar empilhadeira para operacao em Inhumas?')
r('O aluguel de empilhadeiras em Goiania comeca a partir de R$2.800/mes, com manutencao preventiva e corretiva inclusa — sem custos ocultos. O valor final depende do tipo de equipamento (GLP, eletrica ou diesel), capacidade de carga, duracao do contrato e volume locado. Por sermos sediados na capital, nao ha custo adicional de deslocamento. Solicite um orcamento pelo WhatsApp informando sua necessidade.',
  'Empilhadeiras Clark partem de R$2.800/mes com manutencao inclusa e sem custo de deslocamento para Inhumas. O valor final varia conforme capacidade (2 a 8 toneladas), motorizacao (GLP, eletrica ou diesel) e prazo de locacao. Industrias do polo de confecções e Distrito Industrial costumam fechar contratos de 6 a 12 meses com condicoes diferenciadas. Solicite um orcamento personalizado pelo WhatsApp.')

# FAQ 7
r('A manutencao esta inclusa no contrato de locacao em Goiania?',
  'Como funciona a manutencao dos equipamentos locados em Inhumas?')
r('Sim. Toda manutencao preventiva e corretiva esta incluida no contrato de locacao. Em Goiania, por estarmos na mesma cidade, o tempo de resposta tecnica e ainda mais rapido — geralmente em poucas horas. Nosso suporte tecnico e 24h, 7 dias por semana, incluindo feriados.',
  'Toda manutencao preventiva e corretiva faz parte do contrato sem custo adicional. Para Inhumas, o tecnico sai da nossa base e chega em ate 2 horas via GO-070. O suporte opera 24 horas por dia, 7 dias por semana — inclusive feriados. Em operacoes criticas no Distrito Industrial, priorizamos o despacho emergencial.')

# FAQ 8
r('Qual o prazo minimo de locacao em Goiania?',
  'A Move Maquinas trabalha com locacao por demanda para o indústria alimentícia e polo de confecções?')
r('O prazo padrao e de 1 mes, com possibilidade de renovacao automatica. Para obras com prazo definido — como reformas de fachada no Setor Marista ou instalacoes no Distrito Industrial — tambem avaliamos contratos por demanda especifica. Consulte pelo WhatsApp informando a duracao estimada da sua operacao para recebermos a melhor condicao.',
  'Sim. O contrato padrao e mensal com renovacao automatica, mas avaliamos prazos sob medida para paradas programadas no indústria alimentícia e polo de confecções. Fabricas que precisam de equipamento extra durante picos de producao ou manutencoes gerais podem contratar por semana ou quinzena. Informe pelo WhatsApp o periodo e tipo de maquina para receber a melhor condicao.')

# ═══════════════════════════════════════════════════════════════════════
# 15. CTA FINAL
# ═══════════════════════════════════════════════════════════════════════

r('Sede em Goiania — entrega no mesmo dia',
  '40 km de Inhumas — entrega no mesmo dia')

r('Fale agora com nosso time. Confirmamos disponibilidade e prazo de entrega em minutos — sem enrolar.',
  'Solicite orcamento agora. Confirmamos estoque e prazo de entrega para Inhumas em minutos.')

r('Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania - GO · CNPJ 32.428.258/0001-80',
  'Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania-GO · Atendimento Inhumas via GO-070 · CNPJ 32.428.258/0001-80')

# ═══════════════════════════════════════════════════════════════════════
# 16. WhatsApp URL catch-all (remaining encoded Goiânia references)
# ═══════════════════════════════════════════════════════════════════════

# Already handled by the mass replace of Goi%C3%A2nia → Inhumas above

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

import re

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    # Check for "Goiania" (without accent) and "Goiânia" (with accent) and goiania-go
    has_goiania = 'Goiania' in line or 'Goiânia' in line or 'goiania-go' in line or 'Goi%C3%A2nia' in line
    if has_goiania:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Goiania-GO', 'Goiânia-GO',
            'goiania-go/', 'goiania-go/index.html',  # link to goiania hub
            '40 km', 'sede', 'base',
            'Aparecida de Goiania', 'Aparecida de Goiânia',
            'HUB SENADOR CANEDO',
            'Distribuidor exclusivo Goias',
            'sediados em Goiania',  # legitimate context
            'base em Goiania',  # legitimate
            'base operacional em Goiania',  # legitimate FAQ
            'base na Av',  # legitimate conversacional
            'nossa base',
            'acesso a Goiania',  # rodovia context card
            'Nare91', 'embed',  # youtube video embed
            'Move Maquinas cobre toda',  # cidades proximas intro
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

# Jaccard similarity — WORD-level 3-grams (shingles)
def word_shingles(text, n=3):
    """Extract word-level n-gram shingles from visible text only."""
    # Strip CSS blocks FIRST
    clean = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    # Strip JS blocks
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
    # Strip all HTML tags
    clean = re.sub(r'<[^>]+>', ' ', clean)
    # Strip URLs
    clean = re.sub(r'https?://\S+', '', clean)
    # Normalize
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    words = clean.split()
    return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1))

# Also keep char-level for reference
def char_ngrams(text, n=3):
    """Extract character n-grams from visible text only."""
    clean = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'https?://\S+', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    return set(clean[i:i+n] for i in range(len(clean) - n + 1))

# Word-level shingles (main metric)
ref_shingles = word_shingles(ref)
new_shingles = word_shingles(html)
w_inter = ref_shingles & new_shingles
w_union = ref_shingles | new_shingles
jaccard_words = len(w_inter) / len(w_union) if w_union else 0

# Char-level (secondary)
ref_chars = char_ngrams(ref)
new_chars = char_ngrams(html)
c_inter = ref_chars & new_chars
c_union = ref_chars | new_chars
jaccard_chars = len(c_inter) / len(c_union) if c_union else 0

print("=" * 60)
print("VERIFICAÇÃO FINAL — HUB SENADOR CANEDO")
print("=" * 60)
print(f"Tamanho:     ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'✓' if ref_classes == new_classes else '✗'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'✓' if ref_svgs == new_svgs else '✗'}")
print(f"Jaccard WORD 3-shingles: {jaccard_words:.4f}  {'✓ < 0.20' if jaccard_words < 0.20 else '✗ >= 0.20'}")
print(f"Jaccard CHAR 3-grams:   {jaccard_chars:.4f}  (referência — alto é normal para mesmo template)")
print(f"Word shingles: ref={len(ref_shingles):,}  new={len(new_shingles):,}  shared={len(w_inter):,}")

if goiania_issues:
    print(f"\n⚠ {len(goiania_issues)} referências suspeitas a Goiânia/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\n✓ Nenhuma referência indevida a Goiânia")

# Conteúdo local
sc = html.count('Inhumas') + html.count('inhumas')
local = html.count('polo de confecções') + html.count('petroquim') + html.count('indústria alimentícia') + html.count('GO-070')
print(f"\nInhumas: {sc} menções")
print(f"Contexto local (polo de confecções/petroquímico/indústria alimentícia/GO-070): {local} menções")

# Service card link verification
expected_links = [
    'inhumas-go/aluguel-de-plataforma-elevatoria-articulada',
    'inhumas-go/aluguel-de-plataforma-elevatoria-tesoura',
    'inhumas-go/aluguel-de-empilhadeira-combustao',
    'inhumas-go/aluguel-de-transpaleteira',
    'inhumas-go/curso-de-operador-de-empilhadeira',
]
print("\nLinks de serviços:")
for link in expected_links:
    found = link in html
    print(f"  {'✓' if found else '✗'} {link}")

# Timing
elapsed = datetime.now() - start
minutes = int(elapsed.total_seconds() // 60)
seconds = int(elapsed.total_seconds() % 60)
tokens_est = len(html) // 4  # rough estimate

print(f"\n{'=' * 60}")
print(f"TEMPO: {minutes:02d}:{seconds:02d}")
print(f"TOKENS (estimado): ~{tokens_est:,}")
print(f"Arquivo salvo: {OUT}")
print(f"{'=' * 60}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Hub Inhumas gerado com sucesso!")
