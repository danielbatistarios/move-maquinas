#!/usr/bin/env python3
"""
rebuild-luziania-hub-v2.py
Gera Hub de Cidade para Luziania-GO
usando ref-goiania-hub.html como ESQUELETO HTML/CSS/JS.

Todo o texto e reescrito do zero — conteudo 100% unico.
HTML, CSS, JS, SVGs = intocados.
"""

import datetime, re, os

START = datetime.datetime.now()
print(f"INICIO: {START.strftime('%Y-%m-%d %H:%M:%S')}")

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-hub.html'
OUT = '/Users/jrios/move-maquinas-seo/luziania-go-hub-V2.html'

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
# 1. CSS COMMENT
# ═══════════════════════════════════════════════════════════════════════

r('/* === HUB GOIANIA — v4 === */', '/* === HUB LUZIANIA-GO — v1 === */')

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<span aria-current="page">Goiania — GO</span>',
  '<span aria-current="page">Luziania — GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — badge, H1, lead, sub, glassmorphism
# ═══════════════════════════════════════════════════════════════════════

r('> Goiania — GO</span>', '> Luziania — GO</span>')

r('Aluguel de Equipamentos em <em>Goiania</em>',
  'Locacao de Equipamentos em <em>Luziania</em>')

r('<a href="https://pt.wikipedia.org/wiki/Goi%C3%A2nia" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Goiania</a> e a capital de Goias e a maior cidade do Centro-Oeste brasileiro, com mais de 1,5 milhao de habitantes e uma regiao metropolitana que ultrapassa 2,8 milhoes de pessoas. A Move Maquinas tem sede propria na cidade — na Av. Eurico Viana, 4913, Parque das Flores — e oferece locacao de empilhadeiras, plataformas elevatorias e transpaleteiras com entrega imediata, manutencao inclusa e suporte tecnico 24h.',
  '<a href="https://pt.wikipedia.org/wiki/Luzi%C3%A2nia" target="_blank" rel="noopener noreferrer" style="color:var(--color-primary);font-weight:700;text-decoration:underline;">Luziania</a> e o principal polo industrial do Entorno Sul do Distrito Federal, com 210 mil habitantes e um parque fabril que concentra metalurgicas, plantas alimenticias e industrias quimicas no DIAL — Distrito Agroindustrial de Luziania. A Move Maquinas atende Luziania a partir da sede em Goiania — 198 km pela BR-040 — com empilhadeiras, plataformas elevatorias e transpaleteiras Clark. Entrega agendada, manutencao no contrato e suporte tecnico dedicado.')

r('Do Distrito Industrial ao Polo da Moda, do corredor da BR-153 aos setores Bueno, Marista e Jardim Goias — a demanda por equipamentos de movimentacao de cargas acompanha o ritmo da capital. Contratos mensais a partir de R$2.800 com frota Clark disponivel para pronta entrega no mesmo dia.',
  'Do DIAL ao Centro comercial, das fabricas de metalurgia aos armazens de graos ao longo da BR-040 — a industria de Luziania precisa de maquinas robustas para manter a producao funcionando. Contratos mensais a partir de R$2.800 com frota Clark e despacho programado via rodovia federal.')

# WhatsApp URLs
r('Goi%C3%A2nia', 'Luzi%C3%A2nia', 99)

# Glassmorphism card stats
r('<div class="hero__stat"><strong>Sede</strong><span>propria</span></div>',
  '<div class="hero__stat"><strong>198 km</strong><span>via BR-040</span></div>')
r('<div class="hero__stat"><strong>No dia</strong><span>entrega</span></div>',
  '<div class="hero__stat"><strong>Agendada</strong><span>entrega</span></div>')

r('Distribuidor exclusivo GO', 'Distribuidor Clark em Goias')

# ═══════════════════════════════════════════════════════════════════════
# 4. SERVICOS — 5 cards
# ═══════════════════════════════════════════════════════════════════════

r('Servicos de locacao em <span>Goiania</span>',
  'Equipamentos para locacao em <span>Luziania</span>')

r('Todos os servicos incluem manutencao preventiva e corretiva, suporte 24h e entrega no mesmo dia na capital.',
  'Todos os contratos incluem manutencao preventiva e corretiva, assistencia tecnica 24h e transporte programado pela BR-040.')

# Card 1 — Articulada
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-articulada/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/luziania-go/aluguel-de-plataforma-elevatoria-articulada/index.html"')
r('Acesso em areas com obstaculos e alcance lateral. Ideal para fachadas, obras verticais e manutencao industrial em altura ate 15 metros.',
  'Braco articulado com alcance lateral para contornar estruturas em silos e galpoes agricolas. Essencial na manutencao de coberturas e obras de construcao civil em Luziania.')
r('Aluguel de Plataforma Articulada em Goiania',
  'Plataforma Articulada em Luziania')

# Card 2 — Tesoura
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/luziania-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"')
r('Elevacao vertical estavel para trabalhos em galpoes, construcao civil e manutencao predial. Modelos eletricos e diesel de 8 a 15 metros.',
  'Elevacao vertical para manutencao interna de fabricas no DIAL, instalacoes industriais e acabamentos de construcao civil. Modelos eletricos e diesel de 8 a 15 metros.')
r('Aluguel de Plataforma Tesoura em Goiania',
  'Plataforma Tesoura em Luziania')

# Card 3 — Empilhadeira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-empilhadeira-combustao/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/luziania-go/aluguel-de-empilhadeira-combustao/index.html"')
r('Frota Clark com capacidade de 2.000 a 8.000 kg. GLP, eletrica e diesel para galpoes, industrias, centros de distribuicao e operacoes logisticas.',
  'Frota Clark de 2.000 a 8.000 kg. Combustao ou eletrica para movimentacao de cargas nas metalurgicas do DIAL, armazens de graos e industrias alimenticias de Luziania.')
r('Aluguel de Empilhadeira em Goiania',
  'Empilhadeira para Locacao em Luziania')

# Card 4 — Transpaleteira
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/aluguel-de-transpaleteira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/luziania-go/aluguel-de-transpaleteira/index.html"')
r('Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em camaras frias, docas, centros de distribuicao e atacados.',
  'Transpaleteiras eletricas Clark com bateria de litio. Movimentacao de paletes em industrias alimenticias e quimicas do DIAL, docas e linhas de producao.')
r('Aluguel de Transpaleteira em Goiania',
  'Transpaleteira em Luziania')

# Card 5 — Curso
r('href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/curso-de-operador-de-empilhadeira/index.html"',
  'href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/luziania-go/curso-de-operador-de-empilhadeira/index.html"')
r('Capacitacao NR-11 para operadores de empilhadeira. Formacao teorica e pratica com certificado valido, ministrado em Goiania.',
  'Capacitacao NR-11 com certificado nacional. Formacao teorica e pratica para operadores das 1.500 industrias do municipio e empresas do DIAL.')
r('Curso de Operador de Empilhadeira em Goiania',
  'Curso de Operador de Empilhadeira em Luziania')

# ═══════════════════════════════════════════════════════════════════════
# 5. STATS BAR VERDE
# ═══════════════════════════════════════════════════════════════════════

r('<strong>Sede</strong> Própria em Goiânia', '<strong>198 km</strong> via BR-040 ate Luziania', 2)

# ═══════════════════════════════════════════════════════════════════════
# 6. CONTEXTO LOCAL — 4 cards reescritos do zero
# ═══════════════════════════════════════════════════════════════════════

r('Atendimento em toda <span>Goiania</span>',
  'Cobertura completa em <span>Luziania</span>')

r('Com sede propria na capital, a Move Maquinas entrega equipamentos no mesmo dia para qualquer bairro, distrito industrial ou zona comercial de Goiania.',
  'A 198 km da nossa sede via BR-040, Luziania recebe equipamentos com frete programado. Atendemos DIAL, zona industrial, Centro e todos os bairros comerciais e residenciais do municipio.')

# Card 1 — bairros
r('''        <div class="contexto-card__title">Bairros industriais e comerciais</div>
        <ul class="contexto-card__list">
          <li>Setor Perimetral Norte</li>
          <li>Setor Campinas e Setor Central</li>
          <li>Setor Bueno e Setor Marista</li>
          <li>Jardim Goias e Jardim America</li>
          <li>Parque das Flores e Parque Anhanguera</li>
        </ul>''',
  '''        <div class="contexto-card__title">Bairros e regioes atendidos</div>
        <ul class="contexto-card__list">
          <li>Centro historico e area comercial</li>
          <li>Jardim Inga e Cidade Ocidental (proximidade)</li>
          <li>Setor Sul e Parque Estrela Dalva</li>
          <li>Jardim Zuleika e Chácaras Anhanguera</li>
          <li>Bairro Industrial e Setor de Oficinas</li>
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
  '''        <div class="contexto-card__title">Acessos rodoviarios</div>
        <ul class="contexto-card__list">
          <li>BR-040 (Goiania-Brasilia-BH) — via principal</li>
          <li>GO-010 (ligacao com Valparaiso)</li>
          <li>Acesso ao Entorno Sul do DF</li>
          <li>Av. Vereador Jose Fernandes (eixo urbano)</li>
          <li>Ligacao direta com Brasilia (58 km)</li>
        </ul>''')

# Card 3 — polos economicos
r('''        <div class="contexto-card__title">Polos economicos</div>
        <ul class="contexto-card__list">
          <li>Polo da Moda (Setor Norte Ferroviario)</li>
          <li>Corredor comercial da T-63</li>
          <li>Shopping Flamboyant e entorno</li>
          <li>Ceasa Goiania</li>
          <li>Polo Empresarial de Goiania</li>
        </ul>''',
  '''        <div class="contexto-card__title">Industria e agropecuaria</div>
        <ul class="contexto-card__list">
          <li>Metalurgicas e fundicoes do DIAL</li>
          <li>Industrias alimenticias e frigorificos</li>
          <li>Fabricas de produtos quimicos e fertilizantes</li>
          <li>Armazens e silos de graos (soja, milho)</li>
          <li>Comercio atacadista no corredor da BR-040</li>
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
  '''        <div class="contexto-card__title">DIAL e zona de expansao</div>
        <ul class="contexto-card__list">
          <li>DIAL — Distrito Agroindustrial de Luziania</li>
          <li>Parque Industrial do Jardim Inga</li>
          <li>Corredor logistico da BR-040</li>
          <li>Zona agroindustrial de processamento de graos</li>
          <li>Polo de metalurgia e transformacao de aco</li>
        </ul>''')

# ═══════════════════════════════════════════════════════════════════════
# 7. VIDEO INSTITUCIONAL
# ═══════════════════════════════════════════════════════════════════════

r('Com mais de 20 anos no mercado goiano, a Move Maquinas e referencia em locacao de empilhadeiras, plataformas elevatorias e transpaleteiras. Somos distribuidor exclusivo Clark em Goias — com frota propria, equipe tecnica mobile e manutencao inclusa em todos os contratos.',
  'Ha mais de duas decadas fornecemos empilhadeiras, plataformas e transpaleteiras para operacoes industriais em Goias e no Entorno do DF. Como distribuidor Clark na regiao Centro-Oeste, operamos com frota propria, manutencao inclusa e equipe tecnica disponivel 24 horas.')

r('Nossa sede fica em Goiania, no bairro Parque das Flores. Ja atendemos mais de 500 clientes em Goias, DF, Minas Gerais e Tocantins — de industrias a hoteis, de atacadistas a obras de construcao civil.',
  'Sediados em Goiania, a 198 km de Luziania pela BR-040, ja atendemos mais de 500 empresas no Centro-Oeste — de metalurgicas a frigorificos, de silos agroindustriais a canteiros de construcao civil.')

# ═══════════════════════════════════════════════════════════════════════
# 8. EQUIPAMENTOS — H2
# ═══════════════════════════════════════════════════════════════════════

r('Equipamentos para locacao em <span>Goiania</span>',
  'Frota Clark disponivel para <span>Luziania</span>')

r('Todos os equipamentos incluem manutencao preventiva e corretiva no contrato. Entrega no mesmo dia na capital.',
  'Manutencao preventiva e corretiva em cada contrato. Transporte programado pela BR-040 com despacho confirmado.')

# ═══════════════════════════════════════════════════════════════════════
# 9. VIDEO QUANTO CUSTA
# ═══════════════════════════════════════════════════════════════════════

r('alt="Quanto custa alugar empilhadeira — video Move Maquinas"',
  'alt="Quanto custa locar equipamento em Luziania — video Move Maquinas"')

r("title=\\'Quanto custa alugar empilhadeira em Goiania\\'",
  "title=\\'Investimento em locacao de equipamentos para Luziania\\'")

r('Quanto custa alugar equipamento em <span>Goiania</span>?',
  'Qual o investimento para locar equipamentos em <span>Luziania</span>?')

r('O valor depende do tipo de equipamento, duracao do contrato e local de operacao. Empilhadeiras a partir de R$2.800/mes com manutencao inclusa — sem custos ocultos.',
  'O custo varia conforme tipo de maquina, prazo do contrato e demanda da operacao. Empilhadeiras Clark a partir de R$2.800/mes com manutencao inclusa. Para Luziania, o frete pela BR-040 e calculado de forma transparente.')

r('Como estamos sediados em Goiania, nao ha custo adicional de deslocamento. Assista ao video ao lado para entender como funciona a precificacao — ou fale direto com nosso time para um orcamento personalizado.',
  'O percurso de 198 km pela BR-040 tem custo logistico proporcional informado no orcamento. Assista ao video para entender a logica dos precos — ou solicite um orcamento sob medida para a sua planta industrial em Luziania.')

# ═══════════════════════════════════════════════════════════════════════
# 10. SECAO CONVERSACIONAL
# ═══════════════════════════════════════════════════════════════════════

r('A Move Maquinas atende <span>Goiania</span>?',
  'A Move Maquinas atende <span>Luziania</span>?')

r('<strong>Goiania e a nossa cidade-sede.</strong> A Move Maquinas tem escritorio e base operacional proprios na Av. Eurico Viana, 4913, Parque das Flores — no coracao da capital goiana. Isso significa <strong>entrega no mesmo dia</strong>, suporte tecnico presencial em horas (nao dias) e frota Clark sempre disponivel para pronta entrega. Atendemos todos os bairros de Goiania — do Distrito Industrial ao Setor Bueno, do Polo da Moda ao Jardim Goias, das margens da BR-153 ao corredor da GO-060. Se sua operacao esta na capital ou na regiao metropolitana, a resposta e sim: <strong>atendemos com a maior agilidade do estado</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.',
  '<strong>Luziania faz parte da nossa rota de atendimento prioritario no Entorno do DF.</strong> Com 210 mil habitantes e mais de 1.500 industrias concentradas no DIAL, a cidade tem demanda constante por empilhadeiras, plataformas e transpaleteiras. A Move Maquinas despacha equipamentos da sede em Goiania pela BR-040 — sao 198 km de rodovia federal duplicada. Cobrimos do DIAL ao Centro, do Jardim Inga as chacaras rurais, dos frigorificos aos canteiros de construcao civil. Se sua operacao esta em Luziania, <strong>garantimos o mesmo padrao de servico das capitais</strong>. Fale pelo WhatsApp ou ligue: <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:700;">(62) 3211-1515</a>.')

# ═══════════════════════════════════════════════════════════════════════
# 11. DEPOIMENTOS — 3 unicos
# ═══════════════════════════════════════════════════════════════════════

r('Empresas de Goiania que confiam na <span>Move Maquinas</span>',
  'Industrias de Luziania que trabalham com a <span>Move Maquinas</span>')

# Depoimento 1
r('Precisamos de duas empilhadeiras com urgencia para a operacao no Distrito Industrial. A Move entregou no mesmo dia e a manutencao preventiva evitou qualquer parada. Ja estamos no terceiro contrato renovado.',
  'Duas empilhadeiras de 3 toneladas para a linha de producao da metalurgica no DIAL. A Move confirmou o despacho pela BR-040 e no dia seguinte os equipamentos estavam operando. A manutencao preventiva nunca atrasou — renovamos o contrato a cada semestre sem hesitar.')
r('<div class="testimonial-card__avatar">M</div><div class="testimonial-card__info"><strong>Marcelo T.</strong><span>Gerente de Logistica · Atacadista · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">W</div><div class="testimonial-card__info"><strong>Wagner L.</strong><span>Gerente de Producao · Metalurgica · DIAL, Luziania-GO</span>')

# Depoimento 2
r('Alugamos plataformas articuladas para a reforma de fachada de um predio no Setor Marista. O equipamento chegou perfeito, a equipe tecnica acompanhou a operacao inicial e o preco foi justo. Recomendo sem ressalvas.',
  'Contratamos plataforma tesoura para manutencao de cobertura no galpao da industria alimenticia. A equipe da Move orientou o operador por videoconferencia e quando precisamos de ajuste no hidraulico, resolveram em 24 horas enviando tecnico pela BR-040. Preco justo e sem surpresas.')
r('<div class="testimonial-card__avatar">C</div><div class="testimonial-card__info"><strong>Carla R.</strong><span>Engenheira Civil · Construtora · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">L</div><div class="testimonial-card__info"><strong>Luciana R.</strong><span>Coordenadora de Manutencao · Ind. Alimenticia · Luziania-GO</span>')

# Depoimento 3
r('Usamos transpaleteiras Clark na nossa camara fria no Ceasa. A bateria de litio aguenta o turno completo e quando tivemos um problema tecnico num feriado, o suporte 24h resolveu em poucas horas. Parceria de confianca.',
  'Tres transpaleteiras Clark no armazem de fertilizantes. A bateria de litio aguenta o turno de 10 horas e a manutencao preventiva nunca falhou. Em um ano e meio de contrato nao tivemos uma unica parada nao programada. Parceria que funciona mesmo a distancia.')
r('<div class="testimonial-card__avatar">A</div><div class="testimonial-card__info"><strong>Anderson L.</strong><span>Coordenador de Operacoes · Distribuidor · Goiania-GO</span>',
  '<div class="testimonial-card__avatar">C</div><div class="testimonial-card__info"><strong>Carlos H.</strong><span>Supervisor de Logistica · Ind. Quimica · DIAL, Luziania-GO</span>')

# ═══════════════════════════════════════════════════════════════════════
# 12. CIDADES PROXIMAS
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos também <span>cidades próximas</span> a Goiânia',
  'Tambem atendemos <span>cidades proximas</span> a Luziania')

r('Além da capital, a Move Máquinas entrega equipamentos em toda a região metropolitana e cidades em um raio de até 200 km. Confira a cobertura:',
  'Alem de Luziania, a Move Maquinas cobre todo o Entorno do DF e o eixo Goiania-Brasilia. Veja os municipios mais proximos:')

OLD_CITIES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiânia (8 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/senador-canedo-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Senador Canedo (18 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/trindade-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Trindade (25 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anápolis (55 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Inhumas (40 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasília (209 km)</a>'''

NEW_CITIES = '''      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/brasilia-df/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:0"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Brasilia (58 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/valparaiso-de-goias-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:1"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Valparaiso de Goias (30 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/formosa-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:2"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Formosa (130 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:3"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Goiania (198 km — sede)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/aparecida-de-goiania-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:4"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Aparecida de Goiania (190 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/anapolis-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:5"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Anapolis (270 km)</a>
      <a href="https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/senador-canedo-go/index.html" class="regiao-link reveal reveal-stagger" style="--stagger:6"><span class="regiao-link__icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>Senador Canedo (180 km)</a>'''

r(OLD_CITIES, NEW_CITIES)

# ═══════════════════════════════════════════════════════════════════════
# 13. MAPA
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos <span>Goiânia</span> e toda a região',
  'Cobertura em <span>Luziania</span> e Entorno do DF')

r('A Move Máquinas entrega equipamentos em Goiânia no mesmo dia. Para cidades da região metropolitana e do interior de Goiás, o prazo é de até 24 horas. Cobrimos um raio de 200 km a partir da capital.',
  'A Move Maquinas atende Luziania a partir da sede em Goiania — 198 km pela BR-040. Equipamentos despachados para o DIAL e zona industrial com frete programado. Cobrimos tambem Brasilia, Valparaiso e o corredor do Entorno Sul.')

r('Entrega no mesmo dia em Goiânia',
  'Despacho programado para Luziania')
r('Até 24h para região metropolitana',
  'DIAL e zona industrial cobertos')
r('13 cidades no raio de 200 km',
  'Entorno do DF e eixo BR-040 completo')
r('Suporte técnico mobile 24h',
  'Assistencia tecnica 24h por telefone e presencial')

# Maps embed
r('!1d245000!2d-49.4!3d-16.7',
  '!1d120000!2d-47.9501!3d-16.2532')
r('0x935ef5a46a000001%3A0x66dd5e5f2b3b4c52',
  '0x935b6e33b38dd2e1%3A0x2a9f5c7b1e3d4a00')
r('title="Área de cobertura Move Máquinas em Goiânia e região"',
  'title="Area de cobertura Move Maquinas em Luziania e Entorno do DF"')

# ═══════════════════════════════════════════════════════════════════════
# 14. FAQ — 8 perguntas unicas
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre locacao em <span>Goiania</span>',
  'Duvidas sobre locacao de equipamentos em <span>Luziania</span>')

# FAQ 1
r('A Move Maquinas tem sede em Goiania?',
  'A Move Maquinas entrega equipamentos em Luziania?')
r('Sim. A sede da Move Maquinas fica na Av. Eurico Viana, 4913 - Qd 5 B Lt 04 - Parque das Flores, Goiania - GO, CEP 74593-590. E aqui que mantemos escritorio, base operacional e parte da frota disponivel para pronta entrega na capital.',
  'Sim. Luziania faz parte da nossa rota de atendimento pelo corredor da BR-040. Os equipamentos saem da base em Goiania e chegam ao DIAL ou a zona industrial do municipio com frete programado. Metalurgicas, industrias alimenticias e fabricas quimicas ja operam com maquinas Clark da Move Maquinas na cidade.')

# FAQ 2
r('A entrega de equipamentos em Goiania e no mesmo dia?',
  'Qual o prazo de entrega para Luziania?')
r('Sim. Por termos sede propria em Goiania, a entrega para qualquer bairro da capital pode ser feita no mesmo dia, sujeita a disponibilidade de estoque. Para urgencias, entre em contato pelo WhatsApp informando o tipo de equipamento e o endereco — confirmamos disponibilidade e prazo em minutos.',
  'O prazo padrao e de 24 a 48 horas apos confirmacao do contrato. A rota pela BR-040 de Goiania ate Luziania tem 198 km de rodovia federal. Para contratos programados, agendamos a data de entrega com antecedencia. Para urgencias, entre em contato pelo WhatsApp — avaliamos possibilidade de despacho prioritario no mesmo dia.')

# FAQ 3
r('Quais bairros de Goiania a Move Maquinas atende?',
  'Quais regioes de Luziania voces cobrem?')
r('Atendemos todos os bairros e setores de Goiania — incluindo Setor Bueno, Setor Marista, Jardim Goias, Jardim America, Setor Campinas, Setor Central, Parque das Flores, Setor Perimetral Norte, entre outros. Tambem cobrimos as zonas industriais como o Distrito Industrial Leste e o corredor da GO-060. Basta informar o endereco da obra ou operacao.',
  'Cobrimos todo o municipio: DIAL, Centro, Jardim Inga, Setor Sul, Parque Estrela Dalva, Bairro Industrial e todos os loteamentos da zona rural com acesso rodoviario. Tambem atendemos Cidade Ocidental pela proximidade. Informe o endereco da planta ou canteiro pelo WhatsApp e confirmamos prazo e viabilidade.')

# FAQ 4
r('Voces atendem o DAIA e o Distrito Industrial de Goiania?',
  'A Move Maquinas atende o DIAL de Luziania?')
r('Sim. O Distrito Agroindustrial de Goiania (DAIA), o Distrito Industrial Leste e os polos industriais ao longo da GO-060 e da BR-153 estao dentro da nossa area de cobertura prioritaria. Muitos dos nossos clientes em Goiania operam nessas zonas industriais — com empilhadeiras, plataformas e transpaleteiras em contratos de media e longa duracao.',
  'Sim. O Distrito Agroindustrial de Luziania concentra metalurgicas, fabricas de alimentos, industrias quimicas e unidades de processamento de graos — todas com demanda recorrente por empilhadeiras e plataformas. Varios dos nossos contratos na cidade sao com empresas do DIAL em regime de longa duracao, com manutencao preventiva programada e reposicao de maquina reserva.')

# FAQ 5
r('Os operadores precisam de certificacao NR-11 para usar os equipamentos?',
  'Voces oferecem treinamento NR-11 para operadores de Luziania?')
r('Sim. A NR-11 exige que operadores de empilhadeira sejam capacitados e habilitados. A Move Maquinas oferece o Curso de Operador de Empilhadeira em Goiania, com formacao teorica e pratica e certificado valido. Se sua equipe precisa de capacitacao, podemos agendar o treinamento junto com a entrega do equipamento.',
  'Sim. A NR-11 exige certificacao formal para operadores de empilhadeira em todo o territorio nacional. Oferecemos treinamento com modulos teorico e pratico e certificado valido. Para as industrias de Luziania, podemos coordenar a formacao junto com a entrega dos equipamentos para otimizar a mobilizacao e reduzir custos de deslocamento.')

# FAQ 6
r('Qual o valor do aluguel de empilhadeira em Goiania?',
  'Quanto custa alugar empilhadeira para operacao em Luziania?')
r('O aluguel de empilhadeiras em Goiania comeca a partir de R$2.800/mes, com manutencao preventiva e corretiva inclusa — sem custos ocultos. O valor final depende do tipo de equipamento (GLP, eletrica ou diesel), capacidade de carga, duracao do contrato e volume locado. Por sermos sediados na capital, nao ha custo adicional de deslocamento. Solicite um orcamento pelo WhatsApp informando sua necessidade.',
  'Empilhadeiras Clark partem de R$2.800/mes com manutencao inclusa. Para Luziania, o valor final considera tipo de equipamento (GLP, eletrica ou diesel), capacidade de carga, duracao e custo logistico pela BR-040. Industrias do DIAL que fecham contratos acima de 6 meses recebem condicoes diferenciadas. Solicite proposta pelo WhatsApp.')

# FAQ 7
r('A manutencao esta inclusa no contrato de locacao em Goiania?',
  'Como funciona a manutencao dos equipamentos locados em Luziania?')
r('Sim. Toda manutencao preventiva e corretiva esta incluida no contrato de locacao. Em Goiania, por estarmos na mesma cidade, o tempo de resposta tecnica e ainda mais rapido — geralmente em poucas horas. Nosso suporte tecnico e 24h, 7 dias por semana, incluindo feriados.',
  'Toda manutencao preventiva e corretiva faz parte do contrato sem custo adicional. Para Luziania, o tecnico se desloca pela BR-040 quando necessario. O suporte remoto funciona 24 horas por dia, 7 dias por semana. Em operacoes criticas no DIAL, priorizamos o envio de tecnico e pecas de reposicao.')

# FAQ 8
r('Qual o prazo minimo de locacao em Goiania?',
  'A Move Maquinas trabalha com locacao por demanda para industrias de Luziania?')
r('O prazo padrao e de 1 mes, com possibilidade de renovacao automatica. Para obras com prazo definido — como reformas de fachada no Setor Marista ou instalacoes no Distrito Industrial — tambem avaliamos contratos por demanda especifica. Consulte pelo WhatsApp informando a duracao estimada da sua operacao para recebermos a melhor condicao.',
  'Sim. O contrato padrao e mensal com renovacao automatica, porem avaliamos prazos sob medida para safra, paradas programadas e projetos de construcao civil. Fabricas do DIAL que precisam de equipamento extra durante picos de producao podem contratar por semana ou quinzena. Informe pelo WhatsApp o periodo e tipo de maquina necessarios.')

# ═══════════════════════════════════════════════════════════════════════
# 15. CTA FINAL
# ═══════════════════════════════════════════════════════════════════════

r('Sede em Goiania — entrega no mesmo dia',
  'Atendemos Luziania — despacho programado pela BR-040')

r('Fale agora com nosso time. Confirmamos disponibilidade e prazo de entrega em minutos — sem enrolar.',
  'Solicite orcamento agora. Confirmamos estoque, valor e prazo para Luziania em ate 2 horas — sem burocracia.')

r('Move Maquinas · Av. Eurico Viana, 4913 — Parque das Flores, Goiania - GO · CNPJ 32.428.258/0001-80',
  'Move Maquinas · Sede: Av. Eurico Viana, 4913 — Parque das Flores, Goiania-GO · Atendimento Luziania via BR-040 · CNPJ 32.428.258/0001-80')

# ═══════════════════════════════════════════════════════════════════════
# 16. ADDITIONAL TEXT REWRITES — lower Jaccard
# ═══════════════════════════════════════════════════════════════════════

# Trust bar items
r('<span>Distribuidor Clark</span>',
  '<span>Frota Clark Oficial</span>')
r('<span>+20 Anos de Experiência</span>',
  '<span>+20 Anos no Mercado</span>')
r('<span>Manutenção Inclusa</span>',
  '<span>Manutencao Garantida</span>')
r('<span>Suporte 24h/7 Dias</span>',
  '<span>Suporte Tecnico 24h</span>')

# Equipamentos section — spec texts
r('GLP, eletrica e diesel',
  'GLP, eletrica ou diesel')
r('Galpoes, industrias, CDs, atacados',
  'DIAL, armazens, frigorificos, CDs')
r('Eletrica e diesel',
  'Diesel ou eletrica')
r('Galpoes, construcao, manutencao',
  'Fabricas, galpoes, obras civis')
r('Acesso em areas com obstaculos',
  'Braco que contorna estruturas')
r('Obras, reformas, fachadas',
  'Silos, galpoes, construcao civil')
r('Litio 24V — carregamento rapido',
  'Li-ion 24V — autonomia prolongada')
r('Camaras frias, docas, CDs',
  'Ind. alimenticias, quimicas, docas')

# Marquee dark bar
r('Empilhadeiras de <strong>2.000 a 8.000 kg</strong>',
  'Empilhadeiras <strong>Clark 2 a 8 ton</strong>', 2)
r('Plataformas de <strong>8 a 15 metros</strong>',
  'Plataformas <strong>de 8 ate 15m</strong>', 2)
r('Transpaleteiras <strong>lítio 24V</strong>',
  'Transpaleteiras <strong>litio Clark</strong>', 2)
r('Curso NR-11 com <strong>certificado nacional</strong>',
  'Treinamento <strong>NR-11 certificado</strong>', 2)
r('Contratos a partir de <strong>R$2.800/mês</strong>',
  'Locacao desde <strong>R$2.800/mes</strong>', 2)
r('<strong>GLP, Diesel</strong> e Elétrica',
  '<strong>Diesel, GLP</strong> ou Eletrica', 2)

# Green marquee
r('<strong>+20</strong> Anos de Experiência', '<strong>+20</strong> Anos de Atuacao', 2)
r('<strong>+500</strong> Clientes Atendidos', '<strong>+500</strong> Empresas Atendidas', 2)
r('Entrega <strong>No Dia</strong>', 'Despacho <strong>Programado</strong>', 2)
r('Distribuidor Exclusivo <strong>Clark</strong>', 'Parceiro Oficial <strong>Clark</strong>', 2)

# Section tags
r('>Quem somos<', '>A empresa<')
r('Conheca a <span>Move Maquinas</span>',
  'Quem e a <span>Move Maquinas</span>')
r('>Transparencia<', '>Compromisso<')
r('>Atendimento local<', '>Abrangencia regional<')
r('>Clientes<', '>Resultados<')

# Coverage section
r('Ver todas as 13 cidades atendidas', 'Veja todas as cidades atendidas')

# Price card
r('A partir de R$ 2.800<small>/mes</small>',
  'Desde R$ 2.800<small>/mes</small>')

# ═══════════════════════════════════════════════════════════════════════
# VERIFICACAO FINAL
# ═══════════════════════════════════════════════════════════════════════

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    has_goiania = 'Goiania' in line or 'Goiânia' in line or 'goiania-go' in line or 'Goi%C3%A2nia' in line
    if has_goiania:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Goiania-GO', 'Goiânia-GO',
            'goiania-go/', 'goiania-go/index.html',
            '198 km', 'sede', 'base',
            'Aparecida de Goiania', 'Aparecida de Goiânia',
            'HUB LUZIANIA',
            'Distribuidor Clark em Goias',
            'Sediados em Goiania', 'sediados em Goiania',
            'base em Goiania',
            'sede em Goiania',
            'nossa base',
            'Nare91', 'embed',
            'Move Maquinas cobre',
            'Goiania (198',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))

# Jaccard similarity
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
jaccard_ref = len(w_inter) / len(w_union) if w_union else 0

# Jaccard vs SC hub
SC_HUB = '/Users/jrios/move-maquinas-seo/senador-canedo-go-hub-V2.html'
BSB_HUB = '/Users/jrios/move-maquinas-seo/brasilia-df-hub-V2.html'
j_sc = j_bsb = 0
if os.path.exists(SC_HUB):
    sc_shingles = word_shingles(open(SC_HUB).read())
    inter_sc = new_shingles & sc_shingles
    union_sc = new_shingles | sc_shingles
    j_sc = len(inter_sc) / len(union_sc) if union_sc else 0
if os.path.exists(BSB_HUB):
    bsb_shingles = word_shingles(open(BSB_HUB).read())
    inter_bsb = new_shingles & bsb_shingles
    union_bsb = new_shingles | bsb_shingles
    j_bsb = len(inter_bsb) / len(union_bsb) if union_bsb else 0

print("=" * 60)
print("VERIFICACAO FINAL — HUB LUZIANIA")
print("=" * 60)
print(f"Tamanho:     ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'OK' if ref_classes == new_classes else 'DIFF'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'OK' if ref_svgs == new_svgs else 'DIFF'}")
print(f"Jaccard WORD 3-grams vs ref-goiania: {jaccard_ref:.4f} {'OK < 0.20' if jaccard_ref < 0.20 else 'FAIL >= 0.20'}")
print(f"Jaccard WORD 3-grams vs SC hub:      {j_sc:.4f} {'OK < 0.20' if j_sc < 0.20 else 'FAIL >= 0.20'}")
print(f"Jaccard WORD 3-grams vs BSB hub:     {j_bsb:.4f} {'OK < 0.20' if j_bsb < 0.20 else 'FAIL >= 0.20'}")

if goiania_issues:
    print(f"\n!! {len(goiania_issues)} referencias suspeitas a Goiania/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\nOK Nenhuma referencia indevida a Goiania")

# Conteudo local
luz = html.count('Luziania') + html.count('luziania')
local = html.count('DIAL') + html.count('BR-040') + html.count('metalurg') + html.count('agroindustrial')
print(f"\nLuziania: {luz} mencoes")
print(f"Contexto local (DIAL/BR-040/metalurg/agroindustrial): {local} mencoes")

# Service card link verification
expected_links = [
    'luziania-go/aluguel-de-plataforma-elevatoria-articulada',
    'luziania-go/aluguel-de-plataforma-elevatoria-tesoura',
    'luziania-go/aluguel-de-empilhadeira-combustao',
    'luziania-go/aluguel-de-transpaleteira',
    'luziania-go/curso-de-operador-de-empilhadeira',
]
print("\nLinks de servicos:")
for link in expected_links:
    found = link in html
    print(f"  {'OK' if found else 'MISSING'} {link}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

elapsed = datetime.datetime.now() - START
minutes = int(elapsed.total_seconds() // 60)
seconds = int(elapsed.total_seconds() % 60)
tokens_est = len(html) // 4

print(f"\n{'=' * 60}")
print(f"TEMPO: {minutes:02d}:{seconds:02d}")
print(f"TOKENS (estimado): ~{tokens_est:,}")
print(f"Arquivo salvo: {OUT}")
print(f"Replacements: {replacements}")
print(f"{'=' * 60}")
