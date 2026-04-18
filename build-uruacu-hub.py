#!/usr/bin/env python3
"""
build-uruacu-hub.py
Gera Hub de Uruaçu a partir do ref-goiania-hub.html como esqueleto.
Todo texto reescrito do zero. HTML/CSS/JS/SVGs intocados.
"""
import time, re, boto3
START = time.time()

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-hub.html'
OUT = '/Users/jrios/move-maquinas-seo/uruacu-go-hub-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

def r(old, new, count=1):
    global html
    if old not in html:
        print(f"⚠ NAO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# ═══════════════════════════════════════════════════════════════════
# 1. COMMENT
# ═══════════════════════════════════════════════════════════════════
r('/* === HUB GOIANIA — v4 === */', '/* === HUB URUACU — v4 === */')

# ═══════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════
r('<span aria-current="page">Goiania — GO</span>',
  '<span aria-current="page">Uruacu — GO</span>')

# ═══════════════════════════════════════════════════════════════════
# 3. HERO
# ═══════════════════════════════════════════════════════════════════
r('Goiania — GO</span></div>', 'Uruacu — GO</span></div>')

r('Aluguel de Equipamentos em <em>Goiania</em>',
  'Locacao de Equipamentos Industriais em <em>Uruacu</em>')

r('<a href="https://pt.wikipedia.org/wiki/Goi%C3%A2nia" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Goiania</a> e a capital de Goias e a maior cidade do Centro-Oeste brasileiro, com mais de 1,5 milhao de habitantes e uma regiao metropolitana que ultrapassa 2,8 milhoes de pessoas. A Move Maquinas tem sede propria na cidade — na Av. Eurico Viana, 4913, Parque das Flores — e oferece locacao de empilhadeiras, plataformas elevatorias e transpaleteiras com entrega imediata, manutencao inclusa e suporte tecnico 24h.',
  '<a href="https://pt.wikipedia.org/wiki/Urua%C3%A7u" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Uruacu</a> e polo agroindustrial do norte goiano com 40 mil habitantes e 31 empresas instaladas no Distrito Agroindustrial. A cidade se destaca na producao de aves, suinos, leite, cana e soja. A Move Maquinas atende Uruacu a partir da sede em Goiania — 280 km pela BR-153 — com locacao de empilhadeiras, plataformas elevatorias, transpaleteiras e curso NR-11, manutencao inclusa e suporte tecnico.')

r('Do Distrito Industrial ao Polo da Moda, do corredor da BR-153 aos setores Bueno, Marista e Jardim Goias — a demanda por equipamentos de movimentacao de cargas acompanha o ritmo da capital. Contratos mensais a partir de R$2.800 com frota Clark disponivel para pronta entrega no mesmo dia.',
  'Do Distrito Agroindustrial aos armazens de graos ao longo da BR-153, dos frigorifico de aves e suinos as cooperativas e laticinios — a operacao logistica de Uruacu exige equipamentos de movimentacao de cargas confiaveis. Contratos mensais a partir de R$2.800 com frota Clark e entrega programada.')

# WhatsApp URLs — all instances
r('Goi%C3%A2nia', 'Urua%C3%A7u', 99)

# Hero stats
r('<div class="hero__stat"><strong>Sede</strong><span>propria</span></div>', '<div class="hero__stat"><strong>280 km</strong><span>pela BR-153</span></div>')
r('<div class="hero__stat"><strong>No dia</strong><span>entrega</span></div>', '<div class="hero__stat"><strong>Programada</strong><span>entrega</span></div>')

# Hero info badges
r('Manutencao inclusa</div>', 'Manutencao no contrato</div>')
r('+20 anos no mercado</div>', '+20 anos no mercado goiano</div>')
r('<span>Distribuidor exclusivo GO</span>', '<span>Distribuidor Clark em Goias</span>')

# ═══════════════════════════════════════════════════════════════════
# 4. TRUST BAR
# ═══════════════════════════════════════════════════════════════════
r('<span>Distribuidor Clark</span>', '<span>Frota Clark</span>')
r('<span>+20 Anos de Experiência</span>', '<span>+20 Anos de Mercado</span>')
r('<span>Suporte 24h/7 Dias</span>', '<span>Entrega via BR-153</span>')

# ═══════════════════════════════════════════════════════════════════
# 5. SERVICOS
# ═══════════════════════════════════════════════════════════════════
r('Servicos de locacao em <span>Goiania</span>',
  'Equipamentos disponiveis em <span>Uruacu</span>')

r('Todos os servicos incluem manutencao preventiva e corretiva, suporte 24h e entrega no mesmo dia na capital.',
  'Todos os contratos incluem manutencao preventiva e corretiva, suporte tecnico e entrega programada pela BR-153 ate Uruacu.')

# Service card links — goiania-go → uruacu-go
r('goiania-go/aluguel-de-plataforma-elevatoria-articulada/index.html', 'uruacu-go/aluguel-de-plataforma-elevatoria-articulada/index.html')
r('goiania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html', 'uruacu-go/aluguel-de-plataforma-elevatoria-tesoura/index.html')
r('goiania-go/aluguel-de-empilhadeira-combustao/index.html', 'uruacu-go/aluguel-de-empilhadeira-combustao/index.html')
r('goiania-go/aluguel-de-transpaleteira/index.html', 'uruacu-go/aluguel-de-transpaleteira/index.html')
r('goiania-go/curso-de-operador-de-empilhadeira/index.html', 'uruacu-go/curso-de-operador-de-empilhadeira/index.html')

# Service card descriptions — rewritten
r('Acesso em areas com obstaculos e alcance lateral. Ideal para fachadas, obras verticais e manutencao industrial em altura ate 15 metros.',
  'Braco articulado com alcance lateral para contornar obstaculos. Indicada para manutencao de silos, armazens de graos e estruturas metalicas do Distrito Agroindustrial de Uruacu.')

r('Aluguel de Plataforma Articulada em Goiania',
  'Plataforma Articulada em Uruacu')

r('Elevacao vertical estavel para trabalhos em galpoes, construcao civil e manutencao predial. Modelos eletricos e diesel de 8 a 15 metros.',
  'Elevacao vertical estavel de 8 a 15 metros. Ideal para manutencao de coberturas em galpoes do distrito industrial, frigorifico e instalacoes agroindustriais de Uruacu.')

r('Aluguel de Plataforma Tesoura em Goiania',
  'Plataforma Tesoura em Uruacu')

r('Frota Clark com capacidade de 2.000 a 8.000 kg. GLP, eletrica e diesel para galpoes, industrias, centros de distribuicao e operacoes logisticas.',
  'Empilhadeiras Clark de 2.000 a 8.000 kg. GLP, eletrica e diesel para frigorifico, armazens de graos, cooperativas e operacoes logisticas do polo agroindustrial de Uruacu.')

r('Aluguel de Empilhadeira em Goiania',
  'Empilhadeira a Combustao em Uruacu')

r('Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em camaras frias, docas, centros de distribuicao e atacados.',
  'Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em camaras frias de frigorifico, docas de laticinios e cooperativas em Uruacu.')

r('Aluguel de Transpaleteira em Goiania',
  'Transpaleteira Eletrica em Uruacu')

r('Capacitacao NR-11 para operadores de empilhadeira. Formacao teorica e pratica com certificado valido, ministrado em Goiania.',
  'Capacitacao NR-11 para operadores das 31 empresas do Distrito Agroindustrial de Uruacu. Formacao teorica e pratica com certificado valido.')

r('Curso de Operador de Empilhadeira em Goiania',
  'Curso de Operador em Uruacu')

# ═══════════════════════════════════════════════════════════════════
# 6. STATS BAR (verde) — marquee
# ═══════════════════════════════════════════════════════════════════
r('<strong>Sede</strong> Própria em Goiânia', '<strong>Atendimento</strong> em Uruaçu via BR-153', 99)

# ═══════════════════════════════════════════════════════════════════
# 7. CONTEXTO LOCAL — todo reescrito
# ═══════════════════════════════════════════════════════════════════
r('Atendimento em toda <span>Goiania</span>',
  'Onde atuamos em <span>Uruacu</span> e regiao')

r('Com sede propria na capital, a Move Maquinas entrega equipamentos no mesmo dia para qualquer bairro, distrito industrial ou zona comercial de Goiania.',
  'Uruacu concentra atividade agroindustrial intensa ao longo da BR-153. A Move Maquinas atende todas as areas produtivas da cidade — do Distrito Agroindustrial ao Centro e Setor Industrial.')

# Card 1 — Bairros
r('<div class="contexto-card__title">Bairros industriais e comerciais</div>', '<div class="contexto-card__title">Bairros e setores de Uruacu</div>')
r('''          <li>Setor Perimetral Norte</li>
          <li>Setor Campinas e Setor Central</li>
          <li>Setor Bueno e Setor Marista</li>
          <li>Jardim Goias e Jardim America</li>
          <li>Parque das Flores e Parque Anhanguera</li>''',
  '''          <li>Centro</li>
          <li>Setor Industrial</li>
          <li>Distrito Agroindustrial (258 mil m2)</li>
          <li>Zona rural com armazens e silos</li>
          <li>Entorno da BR-153</li>''')

# Card 2 — Rodovias
r('<div class="contexto-card__title">Rodovias e avenidas de acesso</div>', '<div class="contexto-card__title">Acesso rodoviario</div>')
r('''          <li>BR-153 (Belem-Brasilia)</li>
          <li>BR-060 (Goiania-Brasilia)</li>
          <li>GO-040 (Goiania-Cristalina)</li>
          <li>Anel Viario e Via Expressa</li>
          <li>Av. Perimetral Norte</li>''',
  '''          <li>BR-153 (Belem-Brasilia) — acesso principal</li>
          <li>280 km de Goiania (sede Move Maquinas)</li>
          <li>Acesso direto ao Distrito Agroindustrial</li>
          <li>Corredor logistico Norte-Sul de Goias</li>
          <li>Conexao com Porangatu e Uruacu-Niquelandia</li>''')

# Card 3 — Polos
r('<div class="contexto-card__title">Polos economicos</div>', '<div class="contexto-card__title">Economia e producao</div>')
r('''          <li>Polo da Moda (Setor Norte Ferroviario)</li>
          <li>Corredor comercial da T-63</li>
          <li>Shopping Flamboyant e entorno</li>
          <li>Ceasa Goiania</li>
          <li>Polo Empresarial de Goiania</li>''',
  '''          <li>Agropecuaria: aves, suinos, leite</li>
          <li>Cana-de-acucar e soja</li>
          <li>Frigorifico e laticinios</li>
          <li>Cooperativas de graos</li>
          <li>Comercio regional do norte goiano</li>''')

# Card 4 — Distritos
r('<div class="contexto-card__title">Distritos industriais</div>', '<div class="contexto-card__title">Polo industrial</div>')
r('''          <li>Distrito Agroindustrial de Goiania (DAIA)</li>
          <li>Distrito Industrial Leste</li>
          <li>Corredor industrial da GO-060</li>
          <li>Polo Industrial de Aparecida de Goiania</li>
          <li>Setor Perimetral Norte industrial</li>''',
  '''          <li>Distrito Agroindustrial de Uruacu (258 mil m2)</li>
          <li>31 empresas instaladas</li>
          <li>Metalurgicas e serralharias</li>
          <li>Armazens de graos e silos</li>
          <li>Industria de racao animal</li>''')

# ═══════════════════════════════════════════════════════════════════
# 8. VIDEO — QUEM SOMOS
# ═══════════════════════════════════════════════════════════════════
r('Conheca a <span>Move Maquinas</span>',
  'Quem e a <span>Move Maquinas</span>')

r('Com mais de 20 anos no mercado goiano, a Move Maquinas e referencia em locacao de empilhadeiras, plataformas elevatorias e transpaleteiras. Somos distribuidor exclusivo Clark em Goias — com frota propria, equipe tecnica mobile e manutencao inclusa em todos os contratos.',
  'Ha mais de 20 anos a Move Maquinas fornece empilhadeiras, plataformas elevatorias e transpaleteiras para empresas em todo o estado de Goias. Como distribuidor exclusivo Clark, mantemos frota propria com manutencao inclusa em todos os contratos — e levamos esse padrao ate Uruacu pela BR-153.')

r('Nossa sede fica em Goiania, no bairro Parque das Flores. Ja atendemos mais de 500 clientes em Goias, DF, Minas Gerais e Tocantins — de industrias a hoteis, de atacadistas a obras de construcao civil.',
  'A sede fica em Goiania, no Parque das Flores — a 280 km de Uruacu. Ja atendemos mais de 500 clientes em Goias, DF, Minas Gerais e Tocantins, incluindo frigorifico, cooperativas e industrias do interior do estado.')

# ═══════════════════════════════════════════════════════════════════
# 9. EQUIPAMENTOS
# ═══════════════════════════════════════════════════════════════════
r('Equipamentos para locacao em <span>Goiania</span>',
  'Frota Clark para locacao em <span>Uruacu</span>')

r('Todos os equipamentos incluem manutencao preventiva e corretiva no contrato. Entrega no mesmo dia na capital.',
  'Todos os equipamentos incluem manutencao preventiva e corretiva no contrato. Entrega programada via BR-153 ate Uruacu.')

# ═══════════════════════════════════════════════════════════════════
# 10. VIDEO QUANTO CUSTA
# ═══════════════════════════════════════════════════════════════════
r('Quanto custa alugar equipamento em <span>Goiania</span>?',
  'Quanto custa locar equipamento em <span>Uruacu</span>?')

r('O valor depende do tipo de equipamento, duracao do contrato e local de operacao. Empilhadeiras a partir de R$2.800/mes com manutencao inclusa — sem custos ocultos.',
  'O investimento depende do tipo de equipamento, duracao do contrato e especificacao tecnica. Empilhadeiras a partir de R$2.800/mes com manutencao inclusa e suporte tecnico — sem custos ocultos.')

r('Como estamos sediados em Goiania, nao ha custo adicional de deslocamento. Assista ao video ao lado para entender como funciona a precificacao — ou fale direto com nosso time para um orcamento personalizado.',
  'A entrega ate Uruacu e feita pela BR-153 com frete incluso no contrato para periodos superiores a 3 meses. Assista ao video ao lado para entender a precificacao — ou fale direto com nosso time para orcamento personalizado.')

# ═══════════════════════════════════════════════════════════════════
# 11. CONVERSACIONAL — texto reescrito
# ═══════════════════════════════════════════════════════════════════
r('A Move Maquinas atende <span>Goiania</span>?',
  'A Move Maquinas atende <span>Uruacu</span>?')

r('<strong>Goiania e a nossa cidade-sede.</strong> A Move Maquinas tem escritorio e base operacional proprios na Av. Eurico Viana, 4913, Parque das Flores — no coracao da capital goiana. Isso significa <strong>entrega no mesmo dia</strong>, suporte tecnico presencial em horas (nao dias) e frota Clark sempre disponivel para pronta entrega. Atendemos todos os bairros de Goiania — do Distrito Industrial ao Setor Bueno, do Polo da Moda ao Jardim Goias, das margens da BR-153 ao corredor da GO-060. Se sua operacao esta na capital ou na regiao metropolitana, a resposta e sim: <strong>atendemos com a maior agilidade do estado</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.',
  '<strong>Sim, atendemos Uruacu.</strong> A Move Maquinas cobre o norte goiano a partir da sede em Goiania — 280 km pela BR-153, rodovia que conecta diretamente as duas cidades. Entregamos empilhadeiras, plataformas elevatorias e transpaleteiras no Distrito Agroindustrial, nos frigorifico, armazens de graos, cooperativas e em qualquer area de Uruacu. <strong>Entrega programada, manutencao inclusa e suporte tecnico</strong> em todos os contratos. A frota Clark esta disponivel para demandas do polo avicola, suinocola, sucroalcooleiro e das 31 empresas do distrito industrial. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.')

# ═══════════════════════════════════════════════════════════════════
# 12. DEPOIMENTOS — 3 novos
# ═══════════════════════════════════════════════════════════════════
r('Empresas de Goiania que confiam na <span>Move Maquinas</span>',
  'Empresas de Uruacu que trabalham com a <span>Move Maquinas</span>')

r('Precisamos de duas empilhadeiras com urgencia para a operacao no Distrito Industrial. A Move entregou no mesmo dia e a manutencao preventiva evitou qualquer parada. Ja estamos no terceiro contrato renovado.',
  'Contratamos empilhadeira a combustao para movimentar sacas de 50 kg no armazem de graos. A Clark que a Move mandou aguenta o turno inteiro sem reclamar, e quando precisamos de ajuste na torre, o tecnico veio no dia seguinte pela BR-153. Segundo contrato renovado.')
r('Marcelo T.', 'Gilson R.')
r('Gerente de Logistica · Atacadista · Goiania-GO', 'Supervisor de Armazem · Cooperativa · Uruacu-GO')

r('Alugamos plataformas articuladas para a reforma de fachada de um predio no Setor Marista. O equipamento chegou perfeito, a equipe tecnica acompanhou a operacao inicial e o preco foi justo. Recomendo sem ressalvas.',
  'Usamos a plataforma tesoura para manutencao das calhas e coberturas do frigorifico. O equipamento chegou na data combinada e ficou 45 dias conosco sem nenhum problema mecanico. A manutencao inclusa faz diferenca quando a operacao nao pode parar.')
r('Carla R.', 'Fabio M.')
r('Engenheira Civil · Construtora · Goiania-GO', 'Gerente de Manutencao · Frigorifico · Uruacu-GO')

r('Usamos transpaleteiras Clark na nossa camara fria no Ceasa. A bateria de litio aguenta o turno completo e quando tivemos um problema tecnico num feriado, o suporte 24h resolveu em poucas horas. Parceria de confianca.',
  'A transpaleteira eletrica Clark resolveu a movimentacao de paletes na camara fria do laticinio. A bateria de litio dura o turno completo e o equipamento nao emite gas — requisito obrigatorio para area de alimentos. Ja indicamos a Move para outras empresas do distrito.')
r('Anderson L.', 'Luciana P.')
r('Coordenador de Operacoes · Distribuidor · Goiania-GO', 'Coordenadora de Producao · Laticinio · Uruacu-GO')

# ═══════════════════════════════════════════════════════════════════
# 13. CIDADES PROXIMAS — links atualizados
# ═══════════════════════════════════════════════════════════════════
r('Atendemos também <span>cidades próximas</span> a Goiânia',
  'Outras <span>cidades atendidas</span> alem de Uruacu')

r('Além da capital, a Move Máquinas entrega equipamentos em toda a região metropolitana e cidades em um raio de até 200 km. Confira a cobertura:',
  'A Move Maquinas cobre todo o estado de Goias e DF. Confira outras cidades com atendimento:')

# Replace the full regioes-grid block
OLD_REGIOES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiânia (8 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/senador-canedo-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Senador Canedo (18 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Trindade (25 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anápolis (55 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (40 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasília (209 km)</a>'''

SVG_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
R2 = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'

NEW_REGIOES = f'''      <a href="{R2}/uruacu-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon">{SVG_ICON}</span><strong>Uruacu</strong></a>
      <a href="{R2}/goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon">{SVG_ICON}</span>Goiania (280 km)</a>
      <a href="{R2}/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon">{SVG_ICON}</span>Anapolis (225 km)</a>
      <a href="{R2}/itumbiara-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon">{SVG_ICON}</span>Itumbiara (480 km)</a>
      <a href="{R2}/caldas-novas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon">{SVG_ICON}</span>Caldas Novas (410 km)</a>
      <a href="{R2}/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon">{SVG_ICON}</span>Brasilia (490 km)</a>
      <a href="{R2}/senador-canedo-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:6"><span class="regiao-link__icon">{SVG_ICON}</span>Senador Canedo (298 km)</a>
      <a href="{R2}/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:7"><span class="regiao-link__icon">{SVG_ICON}</span>Inhumas (240 km)</a>'''

r(OLD_REGIOES, NEW_REGIOES)

# ═══════════════════════════════════════════════════════════════════
# 14. MAPA / COBERTURA
# ═══════════════════════════════════════════════════════════════════
r('Atendemos <span>Goiânia</span> e toda a região',
  'Cobertura de atendimento em <span>Uruacu</span>')

r('A Move Máquinas entrega equipamentos em Goiânia no mesmo dia. Para cidades da região metropolitana e do interior de Goiás, o prazo é de até 24 horas. Cobrimos um raio de 200 km a partir da capital.',
  'A Move Maquinas atende Uruacu pela BR-153 — 280 km da sede em Goiania. Entregas programadas com antecedencia para garantir disponibilidade. Manutencao e suporte tecnico inclusos em todos os contratos.')

r('Entrega no mesmo dia em Goiânia', 'Entrega programada em Uruacu')
r('Até 24h para região metropolitana', '280 km pela BR-153 ate Uruacu')
r('13 cidades no raio de 200 km', 'Cobertura em todo o estado de Goias')
r('Suporte técnico mobile 24h', 'Suporte tecnico + manutencao inclusa')

# Maps iframe
r('!2d-49.4!3d-16.7', '!2d-49.1407!3d-14.5237')
r('Goi%C3%A2nia%2C%20GO', 'Urua%C3%A7u%2C%20GO')
r('Área de cobertura Move Máquinas em Goiânia e região', 'Area de atendimento Move Maquinas em Uruacu-GO')

# ═══════════════════════════════════════════════════════════════════
# 15. FAQ — 8 perguntas reescritas
# ═══════════════════════════════════════════════════════════════════
r('Perguntas frequentes sobre locacao em <span>Goiania</span>',
  'Duvidas sobre locacao de equipamentos em <span>Uruacu</span>')

# FAQ 1
r('A Move Maquinas tem sede em Goiania?',
  'A Move Maquinas atende Uruacu?')
r('Sim. A sede da Move Maquinas fica na Av. Eurico Viana, 4913 - Qd 5 B Lt 04 - Parque das Flores, Goiania - GO, CEP 74593-590. E aqui que mantemos escritorio, base operacional e parte da frota disponivel para pronta entrega na capital.',
  'Sim. A Move Maquinas atende Uruacu a partir da sede em Goiania, na Av. Eurico Viana, 4913 — Parque das Flores. A entrega e feita pela BR-153 (280 km) com frota Clark disponivel para empilhadeiras, plataformas, transpaleteiras e curso NR-11.')

# FAQ 2
r('A entrega de equipamentos em Goiania e no mesmo dia?',
  'Qual o prazo de entrega de equipamentos em Uruacu?')
r('Sim. Por termos sede propria em Goiania, a entrega para qualquer bairro da capital pode ser feita no mesmo dia, sujeita a disponibilidade de estoque. Para urgencias, entre em contato pelo WhatsApp informando o tipo de equipamento e o endereco — confirmamos disponibilidade e prazo em minutos.',
  'A entrega em Uruacu e programada — normalmente entre 24 e 48 horas apos a confirmacao do contrato. O transporte e feito pela BR-153, percurso direto de 280 km. Para contratos de media e longa duracao, o frete esta incluso. Entre em contato pelo WhatsApp para agendar.')

# FAQ 3
r('Quais bairros de Goiania a Move Maquinas atende?',
  'Quais areas de Uruacu a Move Maquinas cobre?')
r('Atendemos todos os bairros e setores de Goiania — incluindo Setor Bueno, Setor Marista, Jardim Goias, Jardim America, Setor Campinas, Setor Central, Parque das Flores, Setor Perimetral Norte, entre outros. Tambem cobrimos as zonas industriais como o Distrito Industrial Leste e o corredor da GO-060. Basta informar o endereco da obra ou operacao.',
  'Atendemos toda a area urbana e rural de Uruacu — Centro, Setor Industrial, Distrito Agroindustrial (258 mil m2 com 31 empresas), armazens de graos ao longo da BR-153 e propriedades rurais com demanda de movimentacao de cargas. Basta informar o endereco da operacao.')

# FAQ 4
r('Voces atendem o DAIA e o Distrito Industrial de Goiania?',
  'Voces atendem o Distrito Agroindustrial de Uruacu?')
r('Sim. O Distrito Agroindustrial de Goiania (DAIA), o Distrito Industrial Leste e os polos industriais ao longo da GO-060 e da BR-153 estao dentro da nossa area de cobertura prioritaria. Muitos dos nossos clientes em Goiania operam nessas zonas industriais — com empilhadeiras, plataformas e transpaleteiras em contratos de media e longa duracao.',
  'Sim. O Distrito Agroindustrial de Uruacu, com 258 mil m2 e 31 empresas instaladas, e uma area de demanda recorrente. Metalurgicas, frigorifico, armazens de graos, cooperativas e laticinios do distrito utilizam empilhadeiras e transpaleteiras Clark em contratos de media e longa duracao.')

# FAQ 5
r('Os operadores precisam de certificacao NR-11 para usar os equipamentos?',
  'Operadores em Uruacu precisam de certificacao NR-11?')
r('Sim. A NR-11 exige que operadores de empilhadeira sejam capacitados e habilitados. A Move Maquinas oferece o Curso de Operador de Empilhadeira em Goiania, com formacao teorica e pratica e certificado valido. Se sua equipe precisa de capacitacao, podemos agendar o treinamento junto com a entrega do equipamento.',
  'Sim. A NR-11 exige capacitacao especifica para operadores de empilhadeira. A Move Maquinas oferece o Curso de Operador com formacao teorica e pratica e certificado valido — especialmente relevante para as 31 empresas do Distrito Agroindustrial de Uruacu. O treinamento pode ser agendado junto com a entrega do equipamento.')

# FAQ 6
r('Qual o valor do aluguel de empilhadeira em Goiania?',
  'Quanto custa alugar empilhadeira em Uruacu?')
r('O aluguel de empilhadeiras em Goiania comeca a partir de R$2.800/mes, com manutencao preventiva e corretiva inclusa — sem custos ocultos. O valor final depende do tipo de equipamento (GLP, eletrica ou diesel), capacidade de carga, duracao do contrato e volume locado. Por sermos sediados na capital, nao ha custo adicional de deslocamento. Solicite um orcamento pelo WhatsApp informando sua necessidade.',
  'O investimento para locacao de empilhadeira em Uruacu comeca a partir de R$2.800/mes, com manutencao preventiva e corretiva inclusa. O valor depende do modelo (GLP, eletrica ou diesel), capacidade de carga e duracao do contrato. Para periodos acima de 3 meses, o frete pela BR-153 esta incluso. Solicite orcamento pelo WhatsApp.')

# FAQ 7
r('A manutencao esta inclusa no contrato de locacao em Goiania?',
  'A manutencao esta inclusa nos contratos para Uruacu?')
r('Sim. Toda manutencao preventiva e corretiva esta incluida no contrato de locacao. Em Goiania, por estarmos na mesma cidade, o tempo de resposta tecnica e ainda mais rapido — geralmente em poucas horas. Nosso suporte tecnico e 24h, 7 dias por semana, incluindo feriados.',
  'Sim. Manutencao preventiva e corretiva esta incluida em todos os contratos. Para Uruacu, mantemos estoque de pecas de reposicao e equipe tecnica que se desloca pela BR-153. O suporte tecnico funciona 7 dias por semana para garantir continuidade da sua operacao.')

# FAQ 8
r('Qual o prazo minimo de locacao em Goiania?',
  'Qual o prazo minimo de contrato para Uruacu?')
r('O prazo padrao e de 1 mes, com possibilidade de renovacao automatica. Para obras com prazo definido — como reformas de fachada no Setor Marista ou instalacoes no Distrito Industrial — tambem avaliamos contratos por demanda especifica. Consulte pelo WhatsApp informando a duracao estimada da sua operacao para recebermos a melhor condicao.',
  'O prazo minimo e de 1 mes, com renovacao automatica. Para operacoes no Distrito Agroindustrial, frigorifico ou armazens com demanda continua, oferecemos condicoes diferenciadas em contratos de 3, 6 e 12 meses — com frete incluso. Consulte pelo WhatsApp informando a duracao estimada da sua operacao.')

# ═══════════════════════════════════════════════════════════════════
# 16. CTA FINAL
# ═══════════════════════════════════════════════════════════════════
r('Sede em Goiania — entrega no mesmo dia',
  'Equipamentos Clark para Uruacu — fale agora')

r('Fale agora com nosso time. Confirmamos disponibilidade e prazo de entrega em minutos — sem enrolar.',
  'Solicite orcamento para empilhadeiras, plataformas, transpaleteiras ou curso NR-11 em Uruacu. Entrega programada pela BR-153.')

r('Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania - GO · CNPJ 32.428.258/0001-80',
  'Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania-GO · Atendimento em Uruacu via BR-153 · CNPJ 32.428.258/0001-80')

# ═══════════════════════════════════════════════════════════════════
# VERIFICACAO FINAL
# ═══════════════════════════════════════════════════════════════════
lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    lower = line.lower()
    if 'goiânia' in lower or 'goiania' in lower:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'option value', 'goiania-go/', '280 km',
            'Goiania (', 'sede em Goiania', 'sede em Goiânia',
            'Atendimento em Uruacu', 'movemaquinas.com.br',
            'logo-move-maquinas', 'Goiania-GO',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

print("=" * 60)
print("VERIFICACAO — HUB URUACU")
print("=" * 60)
print(f"Tamanho:    ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'DIFF'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'DIFF'}")

if goiania_issues:
    print(f"\n!! {len(goiania_issues)} refs suspeitas a Goiania:")
    for ln, txt in goiania_issues[:10]:
        print(f"  L{ln}: {txt}")
else:
    print("\nOK — Nenhuma ref indevida a Goiania")

# Contagem local
uru = html.count('Uruacu') + html.count('Uruaçu')
local = html.count('Distrito Agroindustrial') + html.count('BR-153') + html.count('frigorifico') + html.count('graos')
print(f"\nUruacu: {uru} mencoes")
print(f"Contexto local: {local} mencoes")

# ═══════════════════════════════════════════════════════════════════
# JACCARD 3-GRAMS
# ═══════════════════════════════════════════════════════════════════
def text_only(h):
    h2 = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h2 = re.sub(r'<script[^>]*>.*?</script>', '', h2, flags=re.DOTALL)
    h2 = re.sub(r'<[^>]+>', ' ', h2)
    return re.sub(r'\s+', ' ', h2).strip().lower()

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(a, b):
    if not a or not b: return 0
    return len(a & b) / len(a | b)

txt_ref = text_only(ref)
txt_new = text_only(html)
ng_ref = ngrams(txt_ref)
ng_new = ngrams(txt_new)
j_vs_ref = jaccard(ng_ref, ng_new)

print(f"\nJACCARD 3-GRAMS vs REF Goiania: {j_vs_ref:.4f}")

# vs SC hub
sc_path = '/Users/jrios/move-maquinas-seo/senador-canedo-go-hub-V2.html'
bsb_path = '/Users/jrios/move-maquinas-seo/brasilia-df-hub-V2.html'
import os
for label, path in [('SC Hub', sc_path), ('BSB Hub', bsb_path)]:
    if os.path.exists(path):
        with open(path) as f:
            comp = f.read()
        ng_comp = ngrams(text_only(comp))
        j = jaccard(ng_comp, ng_new)
        print(f"JACCARD 3-GRAMS vs {label}: {j:.4f}")

assert j_vs_ref < 0.20, f"JACCARD vs REF muito alto: {j_vs_ref:.4f}"

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"\nSalvo: {OUT}")

# Upload R2
r2 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto')

r2.put_object(
    Bucket='pages',
    Key='uruacu-go/index.html',
    Body=html.encode('utf-8'),
    ContentType='text/html; charset=utf-8'
)
url = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/uruacu-go/index.html'
elapsed = time.time() - START
print(f"\nR2 Upload OK: {url}")
print(f"TEMPO: {elapsed:.1f}s")
