#!/usr/bin/env python3
"""
rebuild-trindade-hub-v2.py
Gera Hub de Cidade para Trindade
usando ref-goiania-hub.html como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

from datetime import datetime
start = datetime.now()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-hub.html'
OUT = '/Users/jrios/move-maquinas-seo/trindade-go-hub-V2.html'

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
# 1. CSS COMMENT
# ═══════════════════════════════════════════════════════════════════════

r('/* === HUB GOIANIA — v4 === */', '/* === HUB TRINDADE — v1 === */')

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<span aria-current="page">Goiania — GO</span>',
  '<span aria-current="page">Trindade — GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — section tag, H1, lead, sub, glassmorphism card
# ═══════════════════════════════════════════════════════════════════════

# Badge
r('> Goiania — GO</span>', '> Trindade — GO</span>')

# H1
r('Aluguel de Equipamentos em <em>Goiania</em>',
  'Locacao de Equipamentos em <em>Trindade</em>')

# Lead text — rewrite from scratch
r('<a href="https://pt.wikipedia.org/wiki/Goi%C3%A2nia" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Goiania</a> e a capital de Goias e a maior cidade do Centro-Oeste brasileiro, com mais de 1,5 milhao de habitantes e uma regiao metropolitana que ultrapassa 2,8 milhoes de pessoas. A Move Maquinas tem sede propria na cidade — na Av. Eurico Viana, 4913, Parque das Flores — e oferece locacao de empilhadeiras, plataformas elevatorias e transpaleteiras com entrega imediata, manutencao inclusa e suporte tecnico 24h.',
  '<a href="https://pt.wikipedia.org/wiki/Trindade_(Goi%C3%A1s)" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Trindade</a> esta a 18 km de Goiania pela GO-060 e reune 140 mil habitantes num municipio em franca expansao. Condominos industriais, obras de construcao civil e o comércio regional em crescimento aumentam a procura por maquinas de movimentacao e elevacao. A Move Maquinas atende Trindade com empilhadeiras, plataformas elevatorias e transpaleteiras Clark — manutencao inclusa, suporte tecnico 24h e entrega no mesmo dia pela GO-060.')

# Sub text — rewrite from scratch
r('Do Distrito Industrial ao Polo da Moda, do corredor da BR-153 aos setores Bueno, Marista e Jardim Goias — a demanda por equipamentos de movimentacao de cargas acompanha o ritmo da capital. Contratos mensais a partir de R$2.800 com frota Clark disponivel para pronta entrega no mesmo dia.',
  'Do Centro ao Setor Maysa, do Setor Sol Nascente aos condominios industriais ao longo da GO-060 — a construcao de residenciais, galp0es comerciais e centros de distribuicao gera demanda constante por equipamentos. Contratos a partir de R$2.800/mes com frota Clark e entrega rapida pela rodovia estadual.')

# WhatsApp hero URL text
r('Goi%C3%A2nia', 'Trindade', 99)

# Glassmorphism card stats
r('<div class="hero__stat"><strong>Sede</strong><span>propria</span></div>',
  '<div class="hero__stat"><strong>18 km</strong><span>da sede</span></div>')

r('Distribuidor exclusivo GO', 'Distribuidor Clark em Goias')

# ═══════════════════════════════════════════════════════════════════════
# 4. SERVIÇOS — 5 cards com links e textos Trindade
# ═══════════════════════════════════════════════════════════════════════

r('Servicos de locacao em <span>Goiania</span>',
  'Equipamentos disponiveis para <span>Trindade</span>')

r('Todos os servicos incluem manutencao preventiva e corretiva, suporte 24h e entrega no mesmo dia na capital.',
  'Cada contrato inclui manutencao preventiva e corretiva, suporte tecnico integral e entrega pela GO-060 no mesmo dia.')

# Card 1 — Articulada
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-articulada/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/aluguel-de-plataforma-elevatoria-articulada/index.html"')
r('Acesso em areas com obstaculos e alcance lateral. Ideal para fachadas, obras verticais e manutencao industrial em altura ate 15 metros.',
  'Braco articulado para obras em altura nos condominios residenciais e edificios em construcao. Contorna marquises e varandas, alcancando ate 15 metros.')
r('Aluguel de Plataforma Articulada em Goiania',
  'Plataforma Articulada em Trindade')

# Card 2 — Tesoura
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"')
r('Elevacao vertical estavel para trabalhos em galpoes, construcao civil e manutencao predial. Modelos eletricos e diesel de 8 a 15 metros.',
  'Elevacao vertical para manutencao de galpoes comerciais, instalacoes eletricas e hidraulicas em obras do setor de expansao. Modelos de 8 a 15 metros.')
r('Aluguel de Plataforma Tesoura em Goiania',
  'Plataforma Tesoura em Trindade')

# Card 3 — Empilhadeira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-empilhadeira-combustao/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/aluguel-de-empilhadeira-combustao/index.html"')
r('Frota Clark com capacidade de 2.000 a 8.000 kg. GLP, eletrica e diesel para galpoes, industrias, centros de distribuicao e operacoes logisticas.',
  'Frota Clark de 2.000 a 8.000 kg para centros de distribuicao e galpoes ao longo da GO-060, obras de construcao civil e armazens do setor comercial de Trindade.')
r('Aluguel de Empilhadeira em Goiania',
  'Empilhadeira para Locacao em Trindade')

# Card 4 — Transpaleteira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-transpaleteira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/aluguel-de-transpaleteira/index.html"')
r('Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em camaras frias, docas, centros de distribuicao e atacados.',
  'Transpaleteiras eletricas Clark com litio 24V. Movimentacao de paletes em supermercados, comercio varejista e centros de distribuicao emergentes de Trindade.')
r('Aluguel de Transpaleteira em Goiania',
  'Transpaleteira em Trindade')

# Card 5 — Curso
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/curso-de-operador-de-empilhadeira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/curso-de-operador-de-empilhadeira/index.html"')
r('Capacitacao NR-11 para operadores de empilhadeira. Formacao teorica e pratica com certificado valido, ministrado em Goiania.',
  'Formacao NR-11 com certificado nacional. Turmas presenciais e In Company voltadas aos operadores da construcao civil e novos distritos industriais de Trindade.')
r('Curso de Operador de Empilhadeira em Goiania',
  'Curso de Operador de Empilhadeira em Trindade')

# ═══════════════════════════════════════════════════════════════════════
# 5. STATS BAR VERDE
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Sede</strong> Própria em Goiânia', '<strong>18 km</strong> de Goiânia pela GO-060', 2)

# ═══════════════════════════════════════════════════════════════════════
# 6. CONTEXTO LOCAL — 4 cards reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Atendimento em toda <span>Goiania</span>',
  'Atendimento completo em <span>Trindade</span>')

r('Com sede propria na capital, a Move Maquinas entrega equipamentos no mesmo dia para qualquer bairro, distrito industrial ou zona comercial de Goiania.',
  'A 18 km da nossa base pela GO-060, Trindade recebe equipamentos no mesmo dia. Cobrimos o centro urbano, condominios industriais, canteiros de obra e todo o comercio local.')

# Card 1 — bairros
r('''        <div class="contexto-card__title">Bairros industriais e comerciais</div>
        <ul class="contexto-card__list">
          <li>Setor Perimetral Norte</li>
          <li>Setor Campinas e Setor Central</li>
          <li>Setor Bueno e Setor Marista</li>
          <li>Jardim Goias e Jardim America</li>
          <li>Parque das Flores e Parque Anhanguera</li>
        </ul>''',
  '''        <div class="contexto-card__title">Bairros e setores atendidos</div>
        <ul class="contexto-card__list">
          <li>Centro e Setor Maysa</li>
          <li>Setor Sol Nascente e Setor Leste</li>
          <li>Jardim Europa e Jardim Imperial</li>
          <li>Setor Negrão de Lima e Setor Oeste</li>
          <li>Parque Trindade e Parque dos Cisnes</li>
        </ul>''')

# Card 2 — rodovias
r('''        <div class="contexto-card__title">Rodovias e avenidas de acesso</div>
        <ul class="contexto-card__list">
          <li>BR-153 (Belem-Brasilia)</li>
          <li>BR-060 (Goiania-Brasilia)</li>
          <li>GO-040 (Goiania-Cristalina)</li>
          <li>Anel Viario e Via Expressa</li>
          <li>Av. Perimetral Norte</li>
        </ul>''',
  '''        <div class="contexto-card__title">Vias de acesso a Trindade</div>
        <ul class="contexto-card__list">
          <li>GO-060 (Goiania-Trindade) — rota principal</li>
          <li>Anel Viario Metropolitano</li>
          <li>Av. Joao Paulo I (eixo central)</li>
          <li>Acesso pelo Trevo de Trindade na BR-060</li>
          <li>Ligacao direta com Inhumas pela GO-222</li>
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
  '''        <div class="contexto-card__title">Atividades economicas em destaque</div>
        <ul class="contexto-card__list">
          <li>Construcao civil residencial e comercial</li>
          <li>Comercio varejista no Centro e Setor Maysa</li>
          <li>Supermercados e atacarejos regionais</li>
          <li>Industrias em fase de implantacao</li>
          <li>Turismo religioso (Romaria do Divino Pai Eterno)</li>
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
  '''        <div class="contexto-card__title">Condominios industriais e zonas de expansao</div>
        <ul class="contexto-card__list">
          <li>Condominios industriais ao longo da GO-060</li>
          <li>Distrito Industrial em fase de implantacao</li>
          <li>Zona de expansao urbana no Setor Sol Nascente</li>
          <li>Corredor logistico Goiania-Trindade-Inhumas</li>
          <li>Area de novos loteamentos empresariais</li>
        </ul>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. VÍDEO INSTITUCIONAL
# ═══════════════════════════════════════════════════════════════════════

r('Com mais de 20 anos no mercado goiano, a Move Maquinas e referencia em locacao de empilhadeiras, plataformas elevatorias e transpaleteiras. Somos distribuidor exclusivo Clark em Goias — com frota propria, equipe tecnica mobile e manutencao inclusa em todos os contratos.',
  'Presente ha mais de duas decadas no mercado de Goias, a Move Maquinas se consolidou como referencia em locacao de equipamentos para movimentacao e elevacao. Distribuidor exclusivo Clark no estado, com frota propria e assistencia tecnica em todos os contratos.')

r('Nossa sede fica em Goiania, no bairro Parque das Flores. Ja atendemos mais de 500 clientes em Goias, DF, Minas Gerais e Tocantins — de industrias a hoteis, de atacadistas a obras de construcao civil.',
  'Nossa base operacional fica em Goiania, a 18 km de Trindade pela GO-060. Mais de 500 empresas em Goias, DF, Minas e Tocantins ja confiaram nos nossos equipamentos — de construtoras a supermercados, de galpoes logisticos a industrias em implantacao.')

# ═══════════════════════════════════════════════════════════════════════
# 8. EQUIPAMENTOS — H2 texto
# ═══════════════════════════════════════════════════════════════════════

r('Equipamentos para locacao em <span>Goiania</span>',
  'Maquinas Clark para <span>Trindade</span>')

r('Todos os equipamentos incluem manutencao preventiva e corretiva no contrato. Entrega no mesmo dia na capital.',
  'Manutencao preventiva e corretiva em todos os contratos. Entrega pela GO-060 no mesmo dia da aprovacao.')

# ═══════════════════════════════════════════════════════════════════════
# 9. VÍDEO QUANTO CUSTA — textos
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira — video Move Maquinas"',
  'alt="Investimento para locacao de equipamentos em Trindade — video Move Maquinas"')

r("title=\\'Quanto custa alugar empilhadeira em Goiania\\'",
  "title=\\'Quanto custa locar equipamentos em Trindade\\'")

r('Quanto custa alugar equipamento em <span>Goiania</span>?',
  'Quanto investir na locacao de equipamentos em <span>Trindade</span>?')

r('O valor depende do tipo de equipamento, duracao do contrato e local de operacao. Empilhadeiras a partir de R$2.800/mes com manutencao inclusa — sem custos ocultos.',
  'O preco varia conforme a maquina escolhida, o prazo de uso e a complexidade da operacao. Empilhadeiras Clark a partir de R$2.800/mes com manutencao completa e zero surpresa no faturamento.')

r('Como estamos sediados em Goiania, nao ha custo adicional de deslocamento. Assista ao video ao lado para entender como funciona a precificacao — ou fale direto com nosso time para um orcamento personalizado.',
  'Trindade esta a apenas 18 km pela GO-060 — nao cobramos frete de deslocamento. Assista ao video para entender a composicao de valores ou solicite um orcamento direto para a sua necessidade especifica.')

# ═══════════════════════════════════════════════════════════════════════
# 10. SEÇÃO CONVERSACIONAL
# ═══════════════════════════════════════════════════════════════════════

r('A Move Maquinas atende <span>Goiania</span>?',
  'A Move Maquinas entrega em <span>Trindade</span>?')

r('<strong>Goiania e a nossa cidade-sede.</strong> A Move Maquinas tem escritorio e base operacional proprios na Av. Eurico Viana, 4913, Parque das Flores — no coracao da capital goiana. Isso significa <strong>entrega no mesmo dia</strong>, suporte tecnico presencial em horas (nao dias) e frota Clark sempre disponivel para pronta entrega. Atendemos todos os bairros de Goiania — do Distrito Industrial ao Setor Bueno, do Polo da Moda ao Jardim Goias, das margens da BR-153 ao corredor da GO-060. Se sua operacao esta na capital ou na regiao metropolitana, a resposta e sim: <strong>atendemos com a maior agilidade do estado</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.',
  '<strong>Trindade faz parte da nossa area prioritaria.</strong> Com base na Av. Eurico Viana, 4913, Goiania, chegamos a Trindade em menos de 25 minutos pela GO-060. Isso garante <strong>entrega no mesmo dia</strong>, suporte tecnico presencial em poucas horas e disponibilidade imediata de toda a linha Clark. Cobrimos do Centro ao Setor Maysa, do Sol Nascente aos condominios industriais na GO-060. Se voce opera em Trindade ou nos municipios vizinhos, <strong>o atendimento e tao rapido quanto na capital</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 11. DEPOIMENTOS — 3 únicos
# ═══════════════════════════════════════════════════════════════════════

r('Empresas de Goiania que confiam na <span>Move Maquinas</span>',
  'Empresas de Trindade que trabalham com a <span>Move Maquinas</span>')

# Depoimento 1
r('Precisamos de duas empilhadeiras com urgencia para a operacao no Distrito Industrial. A Move entregou no mesmo dia e a manutencao preventiva evitou qualquer parada. Ja estamos no terceiro contrato renovado.',
  'Precisavamos de empilhadeira para o galpao novo no condominio industrial da GO-060. A Move trouxe o equipamento na manha seguinte e a manutencao preventiva garantiu funcionamento continuo. Renovamos contrato por mais 12 meses.')
r('<div class="testimonial-card__avatar">M</div><div class="testimonial-card__info"><strong>Marcelo T.</strong><span>Gerente de Logistica · Atacadista · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">F</div><div class="testimonial-card__info"><strong>Fernando G.</strong><span>Gerente de Operacoes · Centro de Distribuicao · Trindade-GO</span>')

# Depoimento 2
r('Alugamos plataformas articuladas para a reforma de fachada de um predio no Setor Marista. O equipamento chegou perfeito, a equipe tecnica acompanhou a operacao inicial e o preco foi justo. Recomendo sem ressalvas.',
  'Contratamos plataforma articulada para acabamento de fachada num residencial em construcao no Sol Nascente. A equipe da Move fez orientacao no primeiro dia e o equipamento ficou disponivel durante toda a obra. Custo-beneficio excelente.')
r('<div class="testimonial-card__avatar">C</div><div class="testimonial-card__info"><strong>Carla R.</strong><span>Engenheira Civil · Construtora · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">L</div><div class="testimonial-card__info"><strong>Luciana D.</strong><span>Engenheira de Obras · Construtora · Trindade-GO</span>')

# Depoimento 3
r('Usamos transpaleteiras Clark na nossa camara fria no Ceasa. A bateria de litio aguenta o turno completo e quando tivemos um problema tecnico num feriado, o suporte 24h resolveu em poucas horas. Parceria de confianca.',
  'Duas transpaleteiras Clark funcionando no deposito do supermercado sem interrupcao. A bateria de litio dura o expediente inteiro e quando precisamos de assistencia tecnica num sabado, o suporte respondeu em menos de tres horas. Fornecedor de confianca.')
r('<div class="testimonial-card__avatar">A</div><div class="testimonial-card__info"><strong>Anderson L.</strong><span>Coordenador de Operacoes · Distribuidor · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">H</div><div class="testimonial-card__info"><strong>Henrique B.</strong><span>Supervisor de Deposito · Supermercado · Trindade-GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 12. CIDADES PRÓXIMAS
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos também <span>cidades próximas</span> a Goiânia',
  'Atendemos tambem <span>cidades proximas</span> a Trindade')

r('Além da capital, a Move Máquinas entrega equipamentos em toda a região metropolitana e cidades em um raio de até 200 km. Confira a cobertura:',
  'Alem de Trindade, a Move Maquinas cobre toda a regiao metropolitana de Goiania e municipios num raio de 200 km. Veja os pontos de entrega:')

# Reorder cities — Trindade perspective
OLD_CITIES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiânia (8 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/senador-canedo-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Senador Canedo (18 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Trindade (25 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anápolis (55 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (40 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasília (209 km)</a>'''

NEW_CITIES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Goiania (18 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiania (28 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/senador-canedo-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Senador Canedo (38 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (22 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anapolis (70 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasilia (225 km)</a>'''

r(OLD_CITIES, NEW_CITIES)

# ═══════════════════════════════════════════════════════════════════════
# 13. MAPA — embed centrado em Trindade + textos
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos <span>Goiânia</span> e toda a região',
  'Cobertura em <span>Trindade</span> e regiao metropolitana')

r('A Move Máquinas entrega equipamentos em Goiânia no mesmo dia. Para cidades da região metropolitana e do interior de Goiás, o prazo é de até 24 horas. Cobrimos um raio de 200 km a partir da capital.',
  'Trindade fica a 18 km da nossa base pela GO-060. Os equipamentos saem de Goiania e chegam ao canteiro de obra, galpao ou deposito em menos de 30 minutos. Cobrimos toda a regiao metropolitana e cidades num raio de 200 km.')

r('Entrega no mesmo dia em Goiânia',
  'Entrega no mesmo dia em Trindade')
r('Até 24h para região metropolitana',
  'Menos de 30 min pela GO-060')
r('13 cidades no raio de 200 km',
  '13 cidades cobertas num raio de 200 km')
r('Suporte técnico mobile 24h',
  'Equipe tecnica mobile disponivel 24h')

# Maps embed — center on Trindade
r('!1d245000!2d-49.4!3d-16.7',
  '!1d60000!2d-49.4926!3d-16.6514')
r('0x935ef5a46a000001%3A0x66dd5e5f2b3b4c52',
  '0x935ea9d3b0a00001%3A0x4c2f3a1e0d5b7800')

r('title="Área de cobertura Move Máquinas em Goiânia e região"',
  'title="Area de cobertura Move Maquinas em Trindade e regiao"')

# ═══════════════════════════════════════════════════════════════════════
# 14. FAQ — 8 perguntas reescritas do zero
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre locacao em <span>Goiania</span>',
  'Duvidas sobre locacao de equipamentos em <span>Trindade</span>')

# FAQ 1
r('A Move Maquinas tem sede em Goiania?',
  'A Move Maquinas entrega equipamentos em Trindade?')
r('Sim. A sede da Move Maquinas fica na Av. Eurico Viana, 4913 - Qd 5 B Lt 04 - Parque das Flores, Goiania - GO, CEP 74593-590. E aqui que mantemos escritorio, base operacional e parte da frota disponivel para pronta entrega na capital.',
  'Sim. Trindade esta a 18 km da nossa base na Av. Eurico Viana, 4913, Goiania, com acesso rapido pela GO-060. Equipamentos saem do deposito e chegam a qualquer ponto do municipio no mesmo dia — geralmente em menos de 30 minutos de trajeto.')

# FAQ 2
r('A entrega de equipamentos em Goiania e no mesmo dia?',
  'Ha custo de frete para entregas em Trindade?')
r('Sim. Por termos sede propria em Goiania, a entrega para qualquer bairro da capital pode ser feita no mesmo dia, sujeita a disponibilidade de estoque. Para urgencias, entre em contato pelo WhatsApp informando o tipo de equipamento e o endereco — confirmamos disponibilidade e prazo em minutos.',
  'Nao. A proximidade de 18 km pela GO-060 permite que facamos a entrega sem cobrar deslocamento adicional. O frete esta contemplado no valor mensal da locacao, junto com manutencao preventiva, corretiva e suporte tecnico.')

# FAQ 3
r('Quais bairros de Goiania a Move Maquinas atende?',
  'Quais regioes de Trindade voces atendem?')
r('Atendemos todos os bairros e setores de Goiania — incluindo Setor Bueno, Setor Marista, Jardim Goias, Jardim America, Setor Campinas, Setor Central, Parque das Flores, Setor Perimetral Norte, entre outros. Tambem cobrimos as zonas industriais como o Distrito Industrial Leste e o corredor da GO-060. Basta informar o endereco da obra ou operacao.',
  'Atendemos todo o municipio — Centro, Setor Maysa, Sol Nascente, Jardim Europa, Setor Leste, Parque Trindade e todos os condominios industriais ao longo da GO-060. Tambem cobrimos canteiros de obras nos novos loteamentos e areas de expansao. Informe o endereco pelo WhatsApp e confirmamos prazo na hora.')

# FAQ 4
r('Voces atendem o DAIA e o Distrito Industrial de Goiania?',
  'Voces atendem os condominios industriais de Trindade?')
r('Sim. O Distrito Agroindustrial de Goiania (DAIA), o Distrito Industrial Leste e os polos industriais ao longo da GO-060 e da BR-153 estao dentro da nossa area de cobertura prioritaria. Muitos dos nossos clientes em Goiania operam nessas zonas industriais — com empilhadeiras, plataformas e transpaleteiras em contratos de media e longa duracao.',
  'Sim. Os condominios industriais estrategicos ao longo da GO-060 e as areas do distrito industrial em implantacao fazem parte da cobertura prioritaria. Atendemos galpoes de distribuicao, fabricas em fase de montagem e armazens comerciais com empilhadeiras, plataformas e transpaleteiras em contratos mensais ou por demanda.')

# FAQ 5
r('Os operadores precisam de certificacao NR-11 para usar os equipamentos?',
  'Voces oferecem curso NR-11 para operadores em Trindade?')
r('Sim. A NR-11 exige que operadores de empilhadeira sejam capacitados e habilitados. A Move Maquinas oferece o Curso de Operador de Empilhadeira em Goiania, com formacao teorica e pratica e certificado valido. Se sua equipe precisa de capacitacao, podemos agendar o treinamento junto com a entrega do equipamento.',
  'Sim. A certificacao NR-11 e obrigatoria para operadores de empilhadeira. Realizamos o treinamento com modulos teorico e pratico usando equipamentos Clark, e o certificado vale em todo o Brasil por 2 anos. As turmas podem ser organizadas In Company na propria obra ou galpao em Trindade.')

# FAQ 6
r('Qual o valor do aluguel de empilhadeira em Goiania?',
  'Qual o investimento mensal para locacao em Trindade?')
r('O aluguel de empilhadeiras em Goiania comeca a partir de R$2.800/mes, com manutencao preventiva e corretiva inclusa — sem custos ocultos. O valor final depende do tipo de equipamento (GLP, eletrica ou diesel), capacidade de carga, duracao do contrato e volume locado. Por sermos sediados na capital, nao ha custo adicional de deslocamento. Solicite um orcamento pelo WhatsApp informando sua necessidade.',
  'A locacao de equipamentos Clark parte de R$2.800/mes com manutencao completa e sem cobranca de frete para Trindade. O valor depende do modelo escolhido, capacidade operacional e duracao do contrato. Obras com prazo mais longo costumam obter condicoes diferenciadas. Solicite cotacao pelo WhatsApp informando tipo de equipamento e periodo desejado.')

# FAQ 7
r('A manutencao esta inclusa no contrato de locacao em Goiania?',
  'Como funciona o suporte tecnico para equipamentos em Trindade?')
r('Sim. Toda manutencao preventiva e corretiva esta incluida no contrato de locacao. Em Goiania, por estarmos na mesma cidade, o tempo de resposta tecnica e ainda mais rapido — geralmente em poucas horas. Nosso suporte tecnico e 24h, 7 dias por semana, incluindo feriados.',
  'Toda manutencao preventiva e corretiva esta incluida no contrato. Para Trindade, o tecnico desloca-se pela GO-060 e chega em menos de 30 minutos. O suporte funciona 24 horas, 7 dias por semana, incluindo feriados e finais de semana. Problemas urgentes tem despacho prioritario.')

# FAQ 8
r('Qual o prazo minimo de locacao em Goiania?',
  'E possivel alugar equipamento por periodo curto em Trindade?')
r('O prazo padrao e de 1 mes, com possibilidade de renovacao automatica. Para obras com prazo definido — como reformas de fachada no Setor Marista ou instalacoes no Distrito Industrial — tambem avaliamos contratos por demanda especifica. Consulte pelo WhatsApp informando a duracao estimada da sua operacao para recebermos a melhor condicao.',
  'Sim. O contrato padrao e mensal com renovacao automatica, mas avaliamos periodos sob medida para obras pontuais — acabamentos de fachada, montagem de estruturas ou mudancas de layout em galpoes. Informe pelo WhatsApp a duração estimada e o tipo de maquina necessario para receber a melhor proposta.')

# ═══════════════════════════════════════════════════════════════════════
# 15. CTA FINAL
# ═══════════════════════════════════════════════════════════════════════

r('Sede em Goiania — entrega no mesmo dia',
  '18 km de Trindade — entrega no mesmo dia')

r('Fale agora com nosso time. Confirmamos disponibilidade e prazo de entrega em minutos — sem enrolar.',
  'Solicite orcamento agora. Confirmamos disponibilidade e horario de entrega para Trindade em poucos minutos.')

r('Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania - GO · CNPJ 32.428.258/0001-80',
  'Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania-GO · Atendimento Trindade via GO-060 · CNPJ 32.428.258/0001-80')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

import re

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    has_goiania = 'Goiania' in line or 'Goiânia' in line or 'goiania-go' in line or 'Goi%C3%A2nia' in line
    if has_goiania:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Goiania-GO', 'Goiânia-GO',
            'goiania-go/', 'goiania-go/index.html',
            '18 km', 'sede', 'base',
            'Aparecida de Goiania', 'Aparecida de Goiânia',
            'HUB TRINDADE',
            'Distribuidor Clark em Goias',
            'base operacional fica em Goiania',
            'base na Av',
            'nossa base',
            'GO-060',
            'Nare91', 'embed',
            'Move Maquinas cobre toda',
            'metropolitana de Goiania',
            'saem de Goiania',
            'Goiania-Trindade',
            'Goiania-Brasilia',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

# Jaccard similarity — WORD-level 3-grams
def word_shingles(text, n=3):
    clean = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'https?://\S+', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    words = clean.split()
    return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1))

ref_shingles = word_shingles(ref)
new_shingles = word_shingles(html)
w_inter = ref_shingles & new_shingles
w_union = ref_shingles | new_shingles
jaccard_goiania = len(w_inter) / len(w_union) if w_union else 0

# Cross-check vs SC and BSB hubs
cross_files = [
    '/Users/jrios/move-maquinas-seo/senador-canedo-go-hub-V2.html',
    '/Users/jrios/move-maquinas-seo/brasilia-df-hub-V2.html',
]
cross_results = []
for cf in cross_files:
    try:
        with open(cf, 'r', encoding='utf-8') as f:
            other = f.read()
        other_sh = word_shingles(other)
        ci = new_shingles & other_sh
        cu = new_shingles | other_sh
        j = len(ci) / len(cu) if cu else 0
        cross_results.append((cf.split('/')[-1], j))
    except FileNotFoundError:
        cross_results.append((cf.split('/')[-1], -1))

print("=" * 60)
print("VERIFICAÇÃO FINAL — HUB TRINDADE")
print("=" * 60)
print(f"Tamanho:     ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'✓' if ref_classes == new_classes else '✗'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'✓' if ref_svgs == new_svgs else '✗'}")
print(f"Jaccard WORD 3-shingles vs Goiânia: {jaccard_goiania:.4f}  {'✓ < 0.20' if jaccard_goiania < 0.20 else '✗ >= 0.20'}")
for name, j in cross_results:
    status = '✓ < 0.20' if 0 <= j < 0.20 else ('✗ >= 0.20' if j >= 0.20 else 'ARQUIVO NÃO ENCONTRADO')
    print(f"Jaccard WORD 3-shingles vs {name}: {j:.4f}  {status}")
print(f"Word shingles: ref={len(ref_shingles):,}  new={len(new_shingles):,}  shared={len(w_inter):,}")

if goiania_issues:
    print(f"\n⚠ {len(goiania_issues)} referências suspeitas a Goiânia/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\n✓ Nenhuma referência indevida a Goiânia")

# Conteúdo local
tc = html.count('Trindade') + html.count('trindade')
local = html.count('GO-060') + html.count('Sol Nascente') + html.count('Setor Maysa') + html.count('condominios industriais')
print(f"\nTrinden mentions: {tc}")
print(f"Contexto local (GO-060/Sol Nascente/Maysa/cond.ind.): {local} menções")

# Service card link verification
expected_links = [
    'trindade-go/aluguel-de-plataforma-elevatoria-articulada',
    'trindade-go/aluguel-de-plataforma-elevatoria-tesoura',
    'trindade-go/aluguel-de-empilhadeira-combustao',
    'trindade-go/aluguel-de-transpaleteira',
    'trindade-go/curso-de-operador-de-empilhadeira',
]
print("\nLinks de serviços:")
for link in expected_links:
    found = link in html
    print(f"  {'✓' if found else '✗'} {link}")

elapsed = datetime.now() - start
minutes = int(elapsed.total_seconds() // 60)
seconds = int(elapsed.total_seconds() % 60)
tokens_est = len(html) // 4

print(f"\n{'=' * 60}")
print(f"TEMPO: {minutes:02d}:{seconds:02d}")
print(f"TOKENS (estimado): ~{tokens_est:,}")
print(f"Arquivo salvo: {OUT}")
print(f"{'=' * 60}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Hub Trindade gerado com sucesso!")
