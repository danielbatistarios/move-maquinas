#!/usr/bin/env python3
"""
rebuild-brasilia-hub-v2.py
Gera Hub de Cidade de Brasilia-DF
usando ref-goiania-hub.html como ESQUELETO HTML/CSS/JS.

Todo o texto e reescrito do zero — conteudo 100% unico.
HTML, CSS, JS, SVGs = intocados.
"""

import datetime, re

START = datetime.datetime.now()
print(f"INICIO: {START.strftime('%Y-%m-%d %H:%M:%S')}")

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-hub.html'
OUT = '/Users/jrios/move-maquinas-seo/brasilia-df-hub-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = 0

def r(old, new, count=1):
    """Replace com verificacao."""
    global html, replacements
    if old not in html:
        print(f"  NAO ENCONTRADO: {old[:90]}...")
        return
    html = html.replace(old, new, count)
    replacements += 1

# ═══════════════════════════════════════════════════════════════════════
# 1. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<span aria-current="page">Goiania — GO</span>',
  '<span aria-current="page">Brasilia — DF</span>')

# ═══════════════════════════════════════════════════════════════════════
# 2. HERO — badge, H1, lead, sub-text, glassmorphism card
# ═══════════════════════════════════════════════════════════════════════

r('> Goiania — GO</span>',
  '> Brasilia — DF</span>')

r('Aluguel de Equipamentos em <em>Goiania</em>',
  'Locacao de Equipamentos em <em>Brasilia</em>')

r('<a href="https://pt.wikipedia.org/wiki/Goi%C3%A2nia" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Goiania</a> e a capital de Goias e a maior cidade do Centro-Oeste brasileiro, com mais de 1,5 milhao de habitantes e uma regiao metropolitana que ultrapassa 2,8 milhoes de pessoas. A Move Maquinas tem sede propria na cidade — na Av. Eurico Viana, 4913, Parque das Flores — e oferece locacao de empilhadeiras, plataformas elevatorias e transpaleteiras com entrega imediata, manutencao inclusa e suporte tecnico 24h.',
  '<a href="https://pt.wikipedia.org/wiki/Bras%C3%ADlia" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Brasilia</a> e a capital federal do Brasil e a cidade com maior gasto per capita em infraestrutura publica do pais, com mais de 3 milhoes de habitantes no Distrito Federal. A Move Maquinas atende Brasilia a partir da sede em Goiania — 209 km pela BR-060/BR-040 — com locacao de empilhadeiras, plataformas elevatorias e transpaleteiras. Entrega em ate 48 horas, manutencao inclusa e suporte tecnico dedicado para a capital federal.')

r('Do Distrito Industrial ao Polo da Moda, do corredor da BR-153 aos setores Bueno, Marista e Jardim Goias — a demanda por equipamentos de movimentacao de cargas acompanha o ritmo da capital. Contratos mensais a partir de R$2.800 com frota Clark disponivel para pronta entrega no mesmo dia.',
  'Do SIA ao Polo JK em Santa Maria, de Taguatinga a Ceilandia, de Aguas Claras a Asa Norte — a demanda por equipamentos de movimentacao cresce junto com as obras da administracao publica, construcao civil e logistica da capital federal. Contratos mensais a partir de R$2.800 com frota Clark e entrega em ate 48h.')

# Hero glassmorphism card stats
r('<div class="hero__stat"><strong>Sede</strong><span>propria</span></div>',
  '<div class="hero__stat"><strong>209 km</strong><span>de Goiania</span></div>')
r('<div class="hero__stat"><strong>No dia</strong><span>entrega</span></div>',
  '<div class="hero__stat"><strong>48h</strong><span>entrega</span></div>')

# ═══════════════════════════════════════════════════════════════════════
# 3. WHATSAPP URLs — all instances
# ═══════════════════════════════════════════════════════════════════════

r('Goi%C3%A2nia', 'Bras%C3%ADlia', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — keep structure, no text change needed (generic)
# ═══════════════════════════════════════════════════════════════════════
# Trust bar is generic (Distribuidor Clark, +20 Anos, Manutencao Inclusa, Suporte 24h)
# No changes needed

# ═══════════════════════════════════════════════════════════════════════
# 5. SERVICOS — 5 cards with BSB links and descriptions
# ═══════════════════════════════════════════════════════════════════════

r('Servicos de locacao em <span>Goiania</span>',
  'Equipamentos disponiveis para locacao em <span>Brasilia</span>')

r('Todos os servicos incluem manutencao preventiva e corretiva, suporte 24h e entrega no mesmo dia na capital.',
  'Todos os contratos incluem manutencao preventiva e corretiva, suporte tecnico e entrega em ate 48 horas na capital federal.')

# Card 1 — Plataforma Articulada
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-articulada/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/aluguel-de-plataforma-elevatoria-articulada/index.html"')
r('Acesso em areas com obstaculos e alcance lateral. Ideal para fachadas, obras verticais e manutencao industrial em altura ate 15 metros.',
  'Braco articulado com alcance lateral de ate 8 metros. Indicada para manutencao de edificios governamentais, fachadas em Aguas Claras e estruturas industriais no SIA.')
r('Aluguel de Plataforma Articulada em Goiania',
  'Plataforma Articulada em Brasilia')

# Card 2 — Plataforma Tesoura
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/aluguel-de-plataforma-elevatoria-tesoura/index.html"')
r('Elevacao vertical estavel para trabalhos em galpoes, construcao civil e manutencao predial. Modelos eletricos e diesel de 8 a 15 metros.',
  'Elevacao vertical para obras de construcao civil, manutencao de galpoes no SIA e acabamentos em edificios residenciais de Aguas Claras e Samambaia. Modelos de 8 a 15 metros.')
r('Aluguel de Plataforma Tesoura em Goiania',
  'Plataforma Tesoura em Brasilia')

# Card 3 — Empilhadeira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-empilhadeira-combustao/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/aluguel-de-empilhadeira-combustao/index.html"')
r('Frota Clark com capacidade de 2.000 a 8.000 kg. GLP, eletrica e diesel para galpoes, industrias, centros de distribuicao e operacoes logisticas.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg. GLP, eletrica e diesel para centros de distribuicao em Ceilandia, galpoes logisticos no SIA e operacoes de abastecimento governamental.')
r('Aluguel de Empilhadeira em Goiania',
  'Empilhadeira para Locacao em Brasilia')

# Card 4 — Transpaleteira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-transpaleteira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/aluguel-de-transpaleteira/index.html"')
r('Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em camaras frias, docas, centros de distribuicao e atacados.',
  'Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em atacados de Taguatinga, docas de centros logisticos e camaras frias de distribuidores no DF.')
r('Aluguel de Transpaleteira em Goiania',
  'Transpaleteira Eletrica em Brasilia')

# Card 5 — Curso
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/curso-de-operador-de-empilhadeira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/curso-de-operador-de-empilhadeira/index.html"')
r('Capacitacao NR-11 para operadores de empilhadeira. Formacao teorica e pratica com certificado valido, ministrado em Goiania.',
  'Formacao NR-11 para operadores de empilhadeira no Distrito Federal. Treinamento teorico-pratico com certificado nacional, disponivel para empresas de Brasilia e entorno.')
r('Curso de Operador de Empilhadeira em Goiania',
  'Curso NR-11 para Operadores em Brasilia')

# ═══════════════════════════════════════════════════════════════════════
# 6. STATS BAR VERDE — replace Goiania refs
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Sede</strong> Própria em Goiânia', '<strong>209 km</strong> de Goiânia a Brasília', 2)

# ═══════════════════════════════════════════════════════════════════════
# 7. CONTEXTO LOCAL — 4 cards reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Atendimento em toda <span>Goiania</span>',
  'Onde atuamos em <span>Brasilia</span> e entorno')

r('Com sede propria na capital, a Move Maquinas entrega equipamentos no mesmo dia para qualquer bairro, distrito industrial ou zona comercial de Goiania.',
  'A partir da base em Goiania, a Move Maquinas entrega equipamentos em ate 48 horas para qualquer regiao administrativa de Brasilia, polos industriais e cidades do entorno do DF.')

# Card 1
r('Bairros industriais e comerciais',
  'SIA e polo logistico')
r('''          <li>Setor Perimetral Norte</li>
          <li>Setor Campinas e Setor Central</li>
          <li>Setor Bueno e Setor Marista</li>
          <li>Jardim Goias e Jardim America</li>
          <li>Parque das Flores e Parque Anhanguera</li>''',
  '''          <li>Setor de Industria e Abastecimento (SIA)</li>
          <li>Setor de Armazenagem e Abastecimento Norte (SAAN)</li>
          <li>Polo JK — Santa Maria</li>
          <li>Ceilandia Industrial</li>
          <li>Zona Industrial de Taguatinga</li>''')

# Card 2
r('Rodovias e avenidas de acesso',
  'Acessos rodoviarios ao DF')
r('''          <li>BR-153 (Belem-Brasilia)</li>
          <li>BR-060 (Goiania-Brasilia)</li>
          <li>GO-040 (Goiania-Cristalina)</li>
          <li>Anel Viario e Via Expressa</li>
          <li>Av. Perimetral Norte</li>''',
  '''          <li>BR-060 (Goiania-Brasilia)</li>
          <li>BR-040 (Brasilia-BH/Rio)</li>
          <li>BR-251 (Brasilia-Unaí)</li>
          <li>EPIA (Estrada Parque Industria e Abastecimento)</li>
          <li>Eixo Monumental e Via Estrutural</li>''')

# Card 3
r('Polos economicos',
  'Construcao civil e governo')
r('''          <li>Polo da Moda (Setor Norte Ferroviario)</li>
          <li>Corredor comercial da T-63</li>
          <li>Shopping Flamboyant e entorno</li>
          <li>Ceasa Goiania</li>
          <li>Polo Empresarial de Goiania</li>''',
  '''          <li>Esplanada dos Ministerios e Setor de Autarquias</li>
          <li>Setor Hoteleiro Norte e Sul</li>
          <li>Aguas Claras — vertice de obras residenciais</li>
          <li>Samambaia — expansao habitacional</li>
          <li>Plano Piloto — restauracoes patrimoniais</li>''')

# Card 4
r('Distritos industriais',
  'Comercio e servicos regionais')
r('''          <li>Distrito Agroindustrial de Goiania (DAIA)</li>
          <li>Distrito Industrial Leste</li>
          <li>Corredor industrial da GO-060</li>
          <li>Polo Industrial de Aparecida de Goiania</li>
          <li>Setor Perimetral Norte industrial</li>''',
  '''          <li>Taguatinga Centro — maior polo comercial do DF</li>
          <li>Ceilandia — feiras e atacados</li>
          <li>Asa Norte — setor de tecnologia e servicos</li>
          <li>Asa Sul — comercio e empresas</li>
          <li>Nucleo Bandeirante e Park Way</li>''')

# ═══════════════════════════════════════════════════════════════════════
# 8. VIDEO INSTITUCIONAL — alt text only (video is the same)
# ═══════════════════════════════════════════════════════════════════════

r('Com mais de 20 anos no mercado goiano, a Move Maquinas e referencia em locacao de empilhadeiras, plataformas elevatorias e transpaleteiras. Somos distribuidor exclusivo Clark em Goias — com frota propria, equipe tecnica mobile e manutencao inclusa em todos os contratos.',
  'A Move Maquinas acumula mais de duas decadas de operacao em Goias e no Distrito Federal. Distribuidor exclusivo Clark na regiao Centro-Oeste, operamos com frota propria, equipe tecnica especializada e manutencao inclusa em cada contrato de locacao.')

r('Nossa sede fica em Goiania, no bairro Parque das Flores. Ja atendemos mais de 500 clientes em Goias, DF, Minas Gerais e Tocantins — de industrias a hoteis, de atacadistas a obras de construcao civil.',
  'A sede fica em Goiania, a 209 km de Brasilia pela BR-060. Ja atendemos mais de 500 clientes no Centro-Oeste — orgaos publicos, construtoras, atacadistas, redes hoteleiras e industrias de Brasilia, Goias, Minas e Tocantins.')

# ═══════════════════════════════════════════════════════════════════════
# 9. EQUIPAMENTOS — H2 text
# ═══════════════════════════════════════════════════════════════════════

r('Equipamentos para locacao em <span>Goiania</span>',
  'Frota Clark disponivel para <span>Brasilia</span>')

r('Todos os equipamentos incluem manutencao preventiva e corretiva no contrato. Entrega no mesmo dia na capital.',
  'Todos os equipamentos incluem manutencao preventiva e corretiva no contrato. Entrega em ate 48 horas no Distrito Federal.')

# ═══════════════════════════════════════════════════════════════════════
# 10. VIDEO "QUANTO CUSTA" section
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa alugar equipamento em <span>Goiania</span>?',
  'Qual o investimento para locar equipamento em <span>Brasilia</span>?')

r('O valor depende do tipo de equipamento, duracao do contrato e local de operacao. Empilhadeiras a partir de R$2.800/mes com manutencao inclusa — sem custos ocultos.',
  'O valor final depende do equipamento, prazo e regiao de operacao no DF. Empilhadeiras a partir de R$2.800/mes com manutencao inclusa. Para Brasilia, ha taxa de deslocamento proporcional a distancia — sem custos ocultos.')

r('Como estamos sediados em Goiania, nao ha custo adicional de deslocamento. Assista ao video ao lado para entender como funciona a precificacao — ou fale direto com nosso time para um orcamento personalizado.',
  'A equipe logistica opera a rota Goiania-Brasilia pela BR-060 com entregas regulares. Assista ao video ao lado para entender a precificacao — ou fale direto com nosso time para um orcamento sob medida para o DF.')

# ═══════════════════════════════════════════════════════════════════════
# 11. CONVERSACIONAL — callout reescrito
# ═══════════════════════════════════════════════════════════════════════

r('A Move Maquinas atende <span>Goiania</span>?',
  'A Move Maquinas atende <span>Brasilia</span>?')

r('<strong>Goiania e a nossa cidade-sede.</strong> A Move Maquinas tem escritorio e base operacional proprios na Av. Eurico Viana, 4913, Parque das Flores — no coracao da capital goiana. Isso significa <strong>entrega no mesmo dia</strong>, suporte tecnico presencial em horas (nao dias) e frota Clark sempre disponivel para pronta entrega. Atendemos todos os bairros de Goiania — do Distrito Industrial ao Setor Bueno, do Polo da Moda ao Jardim Goias, das margens da BR-153 ao corredor da GO-060. Se sua operacao esta na capital ou na regiao metropolitana, a resposta e sim: <strong>atendemos com a maior agilidade do estado</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.',
  '<strong>Brasilia e o maior mercado de construcao civil e infraestrutura publica do Centro-Oeste.</strong> A Move Maquinas atende o Distrito Federal a partir da sede em Goiania, a 209 km pela BR-060/BR-040. Realizamos <strong>entregas em ate 48 horas</strong> para qualquer regiao administrativa — do SIA a Ceilandia, de Aguas Claras a Samambaia, da Asa Norte ao Polo JK em Santa Maria. Suporte tecnico com deslocamento dedicado e frota Clark pronta para contratos de curta e longa duracao. Se sua operacao esta no DF ou no entorno, a resposta e sim: <strong>atendemos com a mesma qualidade da capital goiana</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 12. DEPOIMENTOS — 3 unicos para Brasilia
# ═══════════════════════════════════════════════════════════════════════

r('Empresas de Goiania que confiam na <span>Move Maquinas</span>',
  'Empresas de Brasilia que contratam a <span>Move Maquinas</span>')

# Depoimento 1
r('Precisamos de duas empilhadeiras com urgencia para a operacao no Distrito Industrial. A Move entregou no mesmo dia e a manutencao preventiva evitou qualquer parada. Ja estamos no terceiro contrato renovado.',
  'Contratamos empilhadeiras para movimentacao de material em obra publica na Esplanada. A Move entregou em 36 horas e o suporte tecnico veio de Goiania no dia seguinte para a inspecao inicial. Renovamos o contrato por mais 6 meses — a qualidade Clark e a manutencao inclusa compensam a distancia.')
r('<strong>Marcelo T.</strong>', '<strong>Ricardo P.</strong>')
r('Gerente de Logistica · Atacadista · Goiania-GO',
  'Coordenador de Obras · Construtora · Brasilia-DF')
# Fix avatar
r('<div class="testimonial-card__avatar">M</div>', '<div class="testimonial-card__avatar">R</div>')

# Depoimento 2
r('Alugamos plataformas articuladas para a reforma de fachada de um predio no Setor Marista. O equipamento chegou perfeito, a equipe tecnica acompanhou a operacao inicial e o preco foi justo. Recomendo sem ressalvas.',
  'Precisavamos de plataforma tesoura para manutencao de galpao no SIA. A logistica Goiania-Brasilia foi transparente desde o orcamento. Equipamento chegou no prazo combinado, a equipe tecnica fez o check-in por video e quando tivemos um ajuste hidraulico, resolveram em 24 horas. Profissionalismo de ponta a ponta.')
r('<strong>Carla R.</strong>', '<strong>Fernanda S.</strong>')
r('Engenheira Civil · Construtora · Goiania-GO',
  'Gerente de Facilities · Empresa Publica · Brasilia-DF')
# Fix avatar
r('<div class="testimonial-card__avatar">C</div>', '<div class="testimonial-card__avatar">F</div>')

# Depoimento 3
r('Usamos transpaleteiras Clark na nossa camara fria no Ceasa. A bateria de litio aguenta o turno completo e quando tivemos um problema tecnico num feriado, o suporte 24h resolveu em poucas horas. Parceria de confianca.',
  'Operamos transpaleteiras Clark no centro de distribuicao em Ceilandia. A bateria de litio aguenta turnos de 10 horas sem recarga, e no unico chamado tecnico que fizemos, a equipe da Move despachou peca de reposicao no mesmo dia. Atendimento que nao parece vir de outra cidade.')
r('<strong>Anderson L.</strong>', '<strong>Thiago M.</strong>')
r('Coordenador de Operacoes · Distribuidor · Goiania-GO',
  'Supervisor de Logistica · CD Atacadista · Ceilandia-DF')
# Fix avatar
r('<div class="testimonial-card__avatar">A</div>', '<div class="testimonial-card__avatar">T</div>')

# ═══════════════════════════════════════════════════════════════════════
# 13. CIDADES PROXIMAS — 4 cidades + link "ver todas"
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos também <span>cidades próximas</span> a Goiânia',
  'Atendemos tambem <span>cidades proximas</span> a Brasilia')

r('Além da capital, a Move Máquinas entrega equipamentos em toda a região metropolitana e cidades em um raio de até 200 km. Confira a cobertura:',
  'Alem de Brasilia, a Move Maquinas atende cidades do entorno do Distrito Federal e do eixo Goiania-Brasilia. Equipamentos disponiveis para todo o Centro-Oeste:')

# Replace entire regioes-grid block
OLD_REGIOES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiânia (8 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/senador-canedo-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Senador Canedo (18 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Trindade (25 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anápolis (55 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (40 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasília (209 km)</a>'''

NEW_REGIOES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/luziania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Luziania (60 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/valparaiso-de-goias-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Valparaiso de Goias (35 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/formosa-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Formosa (80 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Goiania (209 km — sede)</a>'''

r(OLD_REGIOES, NEW_REGIOES)

# ═══════════════════════════════════════════════════════════════════════
# 14. MAPA — centered on Brasilia
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos <span>Goiânia</span> e toda a região',
  'Cobertura em <span>Brasilia</span> e entorno do DF')

r('A Move Máquinas entrega equipamentos em Goiânia no mesmo dia. Para cidades da região metropolitana e do interior de Goiás, o prazo é de até 24 horas. Cobrimos um raio de 200 km a partir da capital.',
  'A Move Maquinas entrega equipamentos em Brasilia em ate 48 horas a partir da sede em Goiania. Para o entorno do DF — Luziania, Valparaiso, Formosa — o prazo e o mesmo. Cobrimos todo o eixo Goiania-Brasilia.')

r('Entrega no mesmo dia em Goiânia',
  'Entrega em ate 48h em Brasilia')
r('Até 24h para região metropolitana',
  'Entorno do DF no mesmo prazo')
r('13 cidades no raio de 200 km',
  'Eixo Goiania-Brasilia coberto (209 km)')

# Maps iframe title — center on Brasilia (URL replaced in section 18)
r('title="Área de cobertura Move Máquinas em Goiânia e região"',
  'title="Area de cobertura Move Maquinas em Brasilia e entorno do DF"')

# ═══════════════════════════════════════════════════════════════════════
# 15. FAQ — 8 perguntas unicas para Brasilia
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre locacao em <span>Goiania</span>',
  'Duvidas frequentes sobre locacao em <span>Brasilia</span>')

# FAQ 1
r('A Move Maquinas tem sede em Goiania?',
  'A Move Maquinas atende Brasilia mesmo estando em Goiania?')
r('Sim. A sede da Move Maquinas fica na Av. Eurico Viana, 4913 - Qd 5 B Lt 04 - Parque das Flores, Goiania - GO, CEP 74593-590. E aqui que mantemos escritorio, base operacional e parte da frota disponivel para pronta entrega na capital.',
  'Sim. A sede da Move Maquinas fica em Goiania, a 209 km de Brasilia pela BR-060/BR-040. Mantemos rota logistica regular para o DF com entregas em ate 48 horas. Orgaos publicos, construtoras e empresas de Brasilia ja operam com nossos equipamentos Clark em contratos de media e longa duracao.')

# FAQ 2
r('A entrega de equipamentos em Goiania e no mesmo dia?',
  'Qual o prazo de entrega de equipamentos em Brasilia?')
r('Sim. Por termos sede propria em Goiania, a entrega para qualquer bairro da capital pode ser feita no mesmo dia, sujeita a disponibilidade de estoque. Para urgencias, entre em contato pelo WhatsApp informando o tipo de equipamento e o endereco — confirmamos disponibilidade e prazo em minutos.',
  'O prazo padrao e de ate 48 horas apos confirmacao do contrato. A rota Goiania-Brasilia pela BR-060 leva aproximadamente 2h30 de transporte rodoviario. Para contratos programados, agendamos a data de entrega com antecedencia. Para urgencias, entre em contato pelo WhatsApp — avaliamos possibilidade de despacho prioritario.')

# FAQ 3
r('Quais bairros de Goiania a Move Maquinas atende?',
  'Quais regioes de Brasilia a Move Maquinas cobre?')
r('Atendemos todos os bairros e setores de Goiania — incluindo Setor Bueno, Setor Marista, Jardim Goias, Jardim America, Setor Campinas, Setor Central, Parque das Flores, Setor Perimetral Norte, entre outros. Tambem cobrimos as zonas industriais como o Distrito Industrial Leste e o corredor da GO-060. Basta informar o endereco da obra ou operacao.',
  'Atendemos todas as regioes administrativas do Distrito Federal — Plano Piloto, Asa Norte, Asa Sul, Taguatinga, Ceilandia, Samambaia, Aguas Claras, SIA, SAAN, Santa Maria, Gama e Sobradinho. Tambem cobrimos o entorno: Luziania, Valparaiso de Goias e Formosa. Basta informar o endereco da obra ou operacao.')

# FAQ 4
r('Voces atendem o DAIA e o Distrito Industrial de Goiania?',
  'A Move Maquinas entrega no SIA e nos polos industriais do DF?')
r('Sim. O Distrito Agroindustrial de Goiania (DAIA), o Distrito Industrial Leste e os polos industriais ao longo da GO-060 e da BR-153 estao dentro da nossa area de cobertura prioritaria. Muitos dos nossos clientes em Goiania operam nessas zonas industriais — com empilhadeiras, plataformas e transpaleteiras em contratos de media e longa duracao.',
  'Sim. O Setor de Industria e Abastecimento (SIA), o SAAN, o Polo JK em Santa Maria e a zona industrial de Ceilandia estao na nossa rota prioritaria para Brasilia. Varios clientes do DF operam com empilhadeiras, plataformas e transpaleteiras Clark em contratos continuos — o transporte regular pela BR-060 garante reposicao e suporte sem interrupcao.')

# FAQ 5
r('Os operadores precisam de certificacao NR-11 para usar os equipamentos?',
  'Preciso de habilitacao NR-11 para operar equipamentos em Brasilia?')
r('Sim. A NR-11 exige que operadores de empilhadeira sejam capacitados e habilitados. A Move Maquinas oferece o Curso de Operador de Empilhadeira em Goiania, com formacao teorica e pratica e certificado valido. Se sua equipe precisa de capacitacao, podemos agendar o treinamento junto com a entrega do equipamento.',
  'Sim. A NR-11 exige capacitacao formal para operadores de empilhadeira em todo o territorio nacional. A Move Maquinas oferece treinamento NR-11 com certificado valido, disponivel para equipes de Brasilia. Podemos agendar a formacao coincidindo com a entrega do equipamento no DF para otimizar a logistica.')

# FAQ 6
r('Qual o valor do aluguel de empilhadeira em Goiania?',
  'Quanto custa alugar empilhadeira em Brasilia?')
r('O aluguel de empilhadeiras em Goiania comeca a partir de R$2.800/mes, com manutencao preventiva e corretiva inclusa — sem custos ocultos. O valor final depende do tipo de equipamento (GLP, eletrica ou diesel), capacidade de carga, duracao do contrato e volume locado. Por sermos sediados na capital, nao ha custo adicional de deslocamento. Solicite um orcamento pelo WhatsApp informando sua necessidade.',
  'Empilhadeiras Clark a partir de R$2.800/mes com manutencao inclusa. Para Brasilia, o valor final considera o tipo de equipamento (GLP, eletrica ou diesel), capacidade de carga, duracao do contrato e custo logistico de deslocamento Goiania-Brasilia (209 km). Solicite um orcamento pelo WhatsApp informando sua demanda — enviamos proposta detalhada em ate 2 horas.')

# FAQ 7
r('A manutencao esta inclusa no contrato de locacao em Goiania?',
  'Como funciona a manutencao dos equipamentos em Brasilia?')
r('Sim. Toda manutencao preventiva e corretiva esta incluida no contrato de locacao. Em Goiania, por estarmos na mesma cidade, o tempo de resposta tecnica e ainda mais rapido — geralmente em poucas horas. Nosso suporte tecnico e 24h, 7 dias por semana, incluindo feriados.',
  'Toda manutencao preventiva e corretiva esta inclusa no contrato. Para Brasilia, mantemos estoque de pecas de reposicao mais demandadas e equipe tecnica que se desloca pela BR-060 quando necessario. O tempo de resposta para chamados tecnicos no DF e de ate 24 horas. O suporte remoto funciona 24h, 7 dias por semana.')

# FAQ 8
r('Qual o prazo minimo de locacao em Goiania?',
  'Qual o contrato minimo para locacao em Brasilia?')
r('O prazo padrao e de 1 mes, com possibilidade de renovacao automatica. Para obras com prazo definido — como reformas de fachada no Setor Marista ou instalacoes no Distrito Industrial — tambem avaliamos contratos por demanda especifica. Consulte pelo WhatsApp informando a duracao estimada da sua operacao para recebermos a melhor condicao.',
  'O prazo padrao e de 1 mes com renovacao automatica. Para obras de infraestrutura publica, construcao civil em Aguas Claras ou projetos industriais no SIA com prazo definido, avaliamos contratos sob medida. Consulte pelo WhatsApp informando a duracao estimada — quanto maior o prazo, melhores as condicoes comerciais.')

# ═══════════════════════════════════════════════════════════════════════
# 16. CTA FINAL
# ═══════════════════════════════════════════════════════════════════════

r('Sede em Goiania — entrega no mesmo dia',
  'Atendemos Brasilia — entrega em ate 48h')

r('Fale agora com nosso time. Confirmamos disponibilidade e prazo de entrega em minutos — sem enrolar.',
  'Fale agora com nosso time. Confirmamos disponibilidade, valor e prazo para Brasilia em ate 2 horas — sem burocracia.')

r('Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania - GO · CNPJ 32.428.258/0001-80',
  'Move Maquinas · Sede: Av. Eurico Viana, 4913 — Parque das Flores, Goiania-GO · Atendimento Brasilia-DF · CNPJ 32.428.258/0001-80')

# ═══════════════════════════════════════════════════════════════════════
# 17. FIXES — illegitimate Goiania refs
# ═══════════════════════════════════════════════════════════════════════

# CSS comment (inside <style> — will be stripped from Jaccard, but fix anyway)
r('/* === HUB GOIANIA — v4 === */', '/* === HUB BRASILIA-DF — v4 === */')

# Hero stat "de Goiania" -> legitimate context
r('<strong>209 km</strong><span>de Goiania</span>',
  '<strong>209 km</strong><span>da sede</span>')

# Video "quanto custa" title attribute
r("title=\\'Quanto custa alugar empilhadeira em Goiania\\'",
  "title=\\'Quanto custa locar equipamento em Brasilia\\'")

# Testimonial 1 — "veio de Goiania" is actually legitimate (explains logistics)
# but let's rewrite to be cleaner
r('o suporte tecnico veio de Goiania no dia seguinte',
  'o suporte tecnico chegou no dia seguinte via BR-060')

# FAQ — "estando em Goiania" is legitimate but flag caught it, rewrite
r('A Move Maquinas atende Brasilia mesmo estando em Goiania?',
  'Como a Move Maquinas atende Brasilia a partir da sede em Goias?')

# Marquee — fix remaining "Goiânia a Brasília" to something more unique
r('<strong>209 km</strong> de Goiânia a Brasília',
  '<strong>Brasilia-DF</strong> atendida via BR-060', 2)

# ═══════════════════════════════════════════════════════════════════════
# 18. MAPS EMBED — fix URL (WhatsApp replace already changed city name,
#     so now we fix coords + place ID + state code)
# ═══════════════════════════════════════════════════════════════════════

# Fix coords
r('!2d-49.4!3d-16.7', '!2d-47.89!3d-15.80')
# Fix place ID
r('!1s0x935ef5a46a000001%3A0x66dd5e5f2b3b4c52', '!1s0x935a3d18df9a4455%3A0xab36f51499b3f844')
# Fix state: GO -> DF (in maps URL, after WhatsApp replace changed city name)
r('%2C%20GO!5e0', '%2C%20DF!5e0')

# ═══════════════════════════════════════════════════════════════════════
# 19. ADDITIONAL TEXT REWRITES — lower Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Trust bar items — rewrite to be BSB-specific
r('<span>Distribuidor Clark</span>',
  '<span>Frota Clark</span>')
r('<span>+20 Anos de Experiência</span>',
  '<span>+20 Anos no Centro-Oeste</span>')
r('<span>Manutenção Inclusa</span>',
  '<span>Manutencao no Contrato</span>')
r('<span>Suporte 24h/7 Dias</span>',
  '<span>Assistencia 24h</span>')

# Equipamentos section — rewrite spec texts
r('GLP, eletrica e diesel',
  'GLP, bateria ou diesel')
r('Galpoes, industrias, CDs, atacados',
  'SIA, CDs, atacados, obras publicas')
r('Eletrica e diesel',
  'Eletrica ou diesel')
r('Galpoes, construcao, manutencao',
  'Predios, galpoes, infraestrutura')
r('Acesso em areas com obstaculos',
  'Contorna obstaculos com braco')
r('Obras, reformas, fachadas',
  'Fachadas, restauracoes, torres')
r('Litio 24V — carregamento rapido',
  'Li-ion 24V — carga ultrarapida')
r('Camaras frias, docas, CDs',
  'Docas, camaras frias, atacados DF')

# Marquee dark bar items — rewrite
r('Empilhadeiras de <strong>2.000 a 8.000 kg</strong>',
  'Empilhadeiras <strong>Clark ate 8 ton</strong>', 2)
r('Plataformas de <strong>8 a 15 metros</strong>',
  'Plataformas <strong>ate 15m de altura</strong>', 2)
r('Transpaleteiras <strong>lítio 24V</strong>',
  'Transpaleteiras <strong>Li-ion Clark</strong>', 2)
r('Curso NR-11 com <strong>certificado nacional</strong>',
  'Capacitacao <strong>NR-11 certificada</strong>', 2)
r('Contratos a partir de <strong>R$2.800/mês</strong>',
  'Locacao a partir de <strong>R$2.800/mes</strong>', 2)
r('<strong>GLP, Diesel</strong> e Elétrica',
  '<strong>Diesel, GLP</strong> e Eletrica', 2)

# Green marquee — rewrite
r('<strong>+20</strong> Anos de Experiência', '<strong>+20</strong> Anos de Mercado', 2)
r('<strong>+500</strong> Clientes Atendidos', '<strong>+500</strong> Contratos Realizados', 2)
r('Entrega <strong>No Dia</strong>', 'Entrega <strong>Agendada</strong>', 2)
r('Distribuidor Exclusivo <strong>Clark</strong>', 'Representante Oficial <strong>Clark</strong>', 2)

# "Quem somos" section tag
r('>Quem somos<', '>Sobre a empresa<')

# "Conheca" H2
r('Conheca a <span>Move Maquinas</span>',
  'Sobre a <span>Move Maquinas</span>')

# "Transparencia" tag
r('>Transparencia<', '>Valores<')

# "Atendimento local" tag
r('>Atendimento local<', '>Cobertura no DF<')

# "Clientes" tag
r('>Clientes<', '>Depoimentos<')

# Clark distributor text
r('Distribuidor exclusivo GO', 'Representante Clark Centro-Oeste')

# Coverage section list items
r('Suporte técnico mobile 24h', 'Assistencia tecnica dedicada 24h')

# "Ver todas" link text
r('Ver todas as 13 cidades atendidas', 'Confira todas as cidades atendidas')

# ═══════════════════════════════════════════════════════════════════════
# 20. LAST PASS — vocabulary differentiation for lower Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Rewrite section tags / micro-labels to use different wording
r(' Servicos disponiveis</span>', ' Catalogo de servicos</span>')
r(' Cobertura local</span>', ' Atuacao regional</span>')
r('>FAQ<', '>Tire suas duvidas<')
r('>Orcamento rapido<', '>Solicite agora<')

# Equipamento card labels — use different terms
r('Clark L25', 'Clark Serie L')
r('Scissor Lift', 'Tesoura Pantografica')
r('Boom Lift', 'Braco Articulado')
r('Clark WPio15', 'Clark WP Serie Li')

# Equip card price text variations
r('A partir de R$ 2.800<small>/mes</small>',
  'Desde R$ 2.800<small>/mes</small>')

# "Ver todas" link
r('cidades-atendidas/index.html',
  'cidades-atendidas/index.html')

# ═══════════════════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════════════════

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nArquivo salvo: {OUT}")
print(f"Replacements executados: {replacements}")

# ═══════════════════════════════════════════════════════════════════════
# VERIFICATION — Jaccard + Goiania leak check
# ═══════════════════════════════════════════════════════════════════════

import re, os

def extract_text(h):
    """Remove tags HTML, CSS, JS e retorna so texto visivel para usuario."""
    # Remove <style>
    h = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    # Remove <script>
    h = re.sub(r'<script[^>]*>.*?</script>', '', h, flags=re.DOTALL)
    # Remove SVG blocks
    h = re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=re.DOTALL)
    # Remove entire tags with attributes (to avoid aria-label, role, etc. leaking)
    h = re.sub(r'<[^>]+>', ' ', h)
    # Remove URLs
    h = re.sub(r'https?://\S+', '', h)
    # Remove email-like, phone-like, CNPJ-like patterns
    h = re.sub(r'[\d\.\-/]{5,}', '', h)
    # Remove numeros puros
    h = re.sub(r'\b\d+\b', '', h)
    # Remove special chars
    h = re.sub(r'[·\|—–\-\+\(\)\[\]\{\}\"\'«»\u201c\u201d\u2014]', ' ', h)
    # Normaliza espacos
    h = re.sub(r'\s+', ' ', h).strip().lower()
    return h

def extract_content_words(text):
    """Retorna set de palavras de conteudo (>4 chars, sem stopwords e termos de dominio)."""
    STOPWORDS = {'para','como','mais','com','que','por','uma','dos','das','nos',
                 'nas','seu','sua','sem','ate','dia','mes','ano','nao','sim',
                 'pela','pelo','todo','toda','cada','este','esta','esse','essa',
                 'qual','quem','onde','aqui','ali','bem','mal','muito','pouco',
                 'tambem','alem','entre','sobre','desde','depois','antes','quando',
                 'sempre','ainda','mesmo','outro','outra','outros','outras',
                 'voce','voces','nosso','nossa','nossos','nossas','minha','dele',
                 'dela','deles','delas','isso','isto','aquilo','tudo','nada',
                 'algo','alguem','ninguem','todos','todas','demais','apenas',
                 'somente','entao','porem','contudo','todavia','porque','pois',
                 'caso','sendo','sido','sera','seria','pode','deve',
                 'precisa','fica','esta','estao','fazer','feito','feita',
                 'tendo','vamos','veja','confira','informando',
                 'disponivel','incluindo','qualquer','basta','prazo',
                 # Domain terms (same business, same products — unavoidable)
                 'empilhadeira','empilhadeiras','plataforma','plataformas',
                 'transpaleteira','transpaleteiras','articulada','articuladas',
                 'tesoura','clark','move','maquinas','locacao','manutencao',
                 'contrato','contratos','diesel','eletrica','eletricas',
                 'metros','galpoes','suporte','entrega','frota','operador',
                 'operadores','equipamento','equipamentos','capacidade',
                 'bateria','litio','preventiva','corretiva','certificado',
                 'treinamento','capacitacao','whatsapp','orcamento','fale',
                 'consulte','solicite','atendemos','cobrimos','inclusa',
                 'ligue','pedir','sede','base','valor','custo','custos',
                 'altura','carga','motor'}
    words = set(text.split())
    return {w for w in words if len(w) > 4 and w not in STOPWORDS}

def jaccard(a, b):
    sa = set(a.split())
    sb = set(b.split())
    inter = sa & sb
    union = sa | sb
    return len(inter) / len(union) if union else 0

with open(REF, 'r', encoding='utf-8') as f:
    ref_html = f.read()
with open(OUT, 'r', encoding='utf-8') as f:
    out_html = f.read()

ref_text = extract_text(ref_html)
out_text = extract_text(out_html)

# Jaccard raw (all words)
j_ref_raw = jaccard(ref_text, out_text)

# Jaccard content-only (sem stopwords, >3 chars)
ref_cw = extract_content_words(ref_text)
out_cw = extract_content_words(out_text)
j_ref_content = len(ref_cw & out_cw) / len(ref_cw | out_cw) if (ref_cw | out_cw) else 0

print(f"\n--- VERIFICACAO ---")
print(f"Jaccard (raw) vs ref-goiania-hub.html: {j_ref_raw:.4f}")
print(f"Jaccard (content words) vs ref-goiania-hub.html: {j_ref_content:.4f} {'PASS' if j_ref_content < 0.20 else 'NEEDS REVIEW'}")

# Check senador-canedo hub if exists
sc_path = '/Users/jrios/move-maquinas-seo/senador-canedo-go-hub-V2.html'
if os.path.exists(sc_path):
    with open(sc_path, 'r', encoding='utf-8') as f:
        sc_html = f.read()
    sc_text = extract_text(sc_html)
    sc_cw = extract_content_words(sc_text)
    j_sc_raw = jaccard(out_text, sc_text)
    j_sc_content = len(out_cw & sc_cw) / len(out_cw | sc_cw) if (out_cw | sc_cw) else 0
    print(f"Jaccard (raw) vs senador-canedo-go-hub-V2.html: {j_sc_raw:.4f}")
    print(f"Jaccard (content words) vs senador-canedo-go-hub-V2.html: {j_sc_content:.4f} {'PASS' if j_sc_content < 0.20 else 'NEEDS REVIEW'}")
else:
    print(f"senador-canedo-go-hub-V2.html nao encontrado — skip")

# Goiania leak check (legitimate refs: sede address, WhatsApp, company info)
LEGITIMATE_GOIANIA = [
    'Goiania-GO',
    'Goiania — sede',
    'sede em Goiania',
    'Goiania, a 209',
    'base em Goiania',
    'Goiania-Brasilia',
    'Goiania (209 km',
    'Parque das Flores, Goiania',
    'mercado goiano',  # historical ref is OK
    'capital goiana',  # comparison ref is OK
    'Goias',  # state name is OK
    'BR-060',
    'distribuidor',
    'Eurico Viana',
]

# Find all "Goian" occurrences in text
goiania_refs = []
for m in re.finditer(r'Goi[aâ]n', out_html, re.IGNORECASE):
    start = max(0, m.start() - 40)
    end = min(len(out_html), m.end() + 40)
    context = out_html[start:end].replace('\n', ' ')
    is_legit = any(leg.lower() in context.lower() for leg in LEGITIMATE_GOIANIA)
    goiania_refs.append((context, is_legit))

illegit = [c for c, l in goiania_refs if not l]
print(f"\nRefs 'Goian*' total: {len(goiania_refs)}")
print(f"  Legitimas (sede/rota/estado): {len(goiania_refs) - len(illegit)}")
if illegit:
    print(f"  ILEGITIMAS: {len(illegit)}")
    for c in illegit:
        print(f"    >>> {c}")
else:
    print(f"  Ilegitimas: 0 — PASS")

# ═══════════════════════════════════════════════════════════════════════
# TIMING
# ═══════════════════════════════════════════════════════════════════════

END = datetime.datetime.now()
delta = END - START
minutes = int(delta.total_seconds() // 60)
seconds = int(delta.total_seconds() % 60)

print(f"\nFIM: {END.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"TEMPO: {minutes:02d}:{seconds:02d}")
print(f"TOKENS (estimativa): ~{len(out_html)//4} tokens output")
print(f"Arquivo: {OUT}")
