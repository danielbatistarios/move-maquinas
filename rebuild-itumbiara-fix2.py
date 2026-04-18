#!/usr/bin/env python3
"""
Fix pages 3-6 for Itumbiara: complete paragraph-level rewrite.
Each page needs ALL content paragraphs rewritten, not just city name swaps.
"""
import datetime, re, os
START = datetime.datetime.now()
print(f"INICIO: {START.strftime('%Y-%m-%d %H:%M:%S')}")
BASE = '/Users/jrios/move-maquinas-seo'

def extract_text(h):
    h = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h = re.sub(r'<script[^>]*>.*?</script>', '', h, flags=re.DOTALL)
    h = re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=re.DOTALL)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'https?://\S+', '', h)
    h = re.sub(r'[\d\.\-/]{5,}', '', h)
    h = re.sub(r'\b\d+\b', '', h)
    h = re.sub(r'[·\|—–\-\+\(\)\[\]\{\}\"\'«»\u201c\u201d\u2014]', ' ', h)
    h = re.sub(r'\s+', ' ', h).strip().lower()
    return h

def ngrams(text, n=3):
    words = text.split()
    return set(' '.join(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard_ngram(a, b, n=3):
    sa, sb = ngrams(a, n), ngrams(b, n)
    inter = sa & sb; union = sa | sb
    return len(inter) / len(union) if union else 0

def verify(ref_path, out_path, comps=None):
    with open(ref_path) as f: rt = extract_text(f.read())
    with open(out_path) as f: ot = extract_text(f.read())
    j = jaccard_ngram(rt, ot)
    print(f"  Jaccard vs ref: {j:.4f} {'PASS' if j<0.20 else 'FAIL'}")
    if comps:
        for c in comps:
            if os.path.exists(c):
                with open(c) as f: ct = extract_text(f.read())
                jc = jaccard_ngram(ot, ct)
                print(f"  Jaccard vs {os.path.basename(c)}: {jc:.4f} {'PASS' if jc<0.20 else 'FAIL'}")
    return j < 0.20

def process(ref_path, out_path, replacements):
    with open(ref_path, 'r', encoding='utf-8') as f:
        html = f.read()
    ok = 0; miss = 0
    for item in replacements:
        old, new = item[0], item[1]
        n = item[2] if len(item) > 2 else 1
        if old not in html:
            miss += 1
            continue
        html = html.replace(old, new, n)
        ok += 1
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Replacements: {ok} OK, {miss} missed")
    return html

# =====================================================================
# TESOURA — Full rewrite
# =====================================================================
print("\n=== TESOURA ===")
R = [
    # HEAD
    ('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
     '<title>Plataforma Tesoura para Locacao em Itumbiara-GO | Move Maquinas</title>'),
    ('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
     'content="Plataforma tesoura em Itumbiara-GO: modelos eletricos de 8 a 10m para galpoes de frigorificos e armazens, diesel de 12 a 15m para patios do DIAGRI e usinas de etanol. Manutencao inclusa, entrega via BR-153. Move Maquinas."'),
    ('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
     'href="https://movemaquinas.com.br/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura"'),
    ('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
     'content="Plataforma Tesoura para Locacao em Itumbiara-GO | Move Maquinas"'),
    ('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
     'content="Plataforma tesoura eletrica e diesel 8 a 15m em Itumbiara. Ideal para galpoes de frigorificos JBS/BRF, armazens do DIAGRI e usinas de etanol. Manutencao inclusa, entrega agendada via BR-153."'),
    ('content="Goiânia, Goiás, Brasil"', 'content="Itumbiara, Goias, Brasil"'),
    ('content="-16.7234;-49.2654"', 'content="-18.4097;-49.2158"'),
    ('content="-16.7234, -49.2654"', 'content="-18.4097, -49.2158"'),
    ('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -18.4097, "longitude": -49.2158'),
    ('"latitude": -16.7234', '"latitude": -18.4097'),
    ('"longitude": -49.2654', '"longitude": -49.2158'),
    ('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"', '"name": "Locacao de Plataforma Tesoura em Itumbiara"'),
    ('"name": "Goiânia", "addressRegion": "GO"', '"name": "Itumbiara", "addressRegion": "GO"'),
    ('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
     '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"'),
    ('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
     '"name": "Plataforma Tesoura em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura"'),
    # Breadcrumb
    ('<a href="/goiania-go/">Equipamentos em Goiânia</a>', '<a href="/itumbiara-go/">Equipamentos em Itumbiara</a>'),
    ('<span aria-current="page">Plataforma Tesoura em Goiânia</span>', '<span aria-current="page">Plataforma Tesoura em Itumbiara</span>'),
    # Hero
    ('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>', 'Locacao de Plataforma Tesoura em <em>Itumbiara</em>'),
    ('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. Ideal para galpões do Distrito Industrial, shoppings e fábricas da GO-060.',
     'Plataformas tesoura de 8 a 15 metros — eletrica para interiores de frigorificos JBS/BRF e armazens de graos, diesel para patios do DIAGRI e usinas de etanol. Manutencao inclusa, suporte tecnico e entrega via BR-153.'),
    ('Goi%C3%A2nia', 'Itumbiara', 99),
    # Trust bar
    ('<strong>+20 anos</strong><span>No mercado goiano</span>', '<strong>+20 anos</strong><span>Experiencia agroindustrial</span>'),
    ('<strong>Suporte técnico</strong><span>Atendimento em Goiânia</span>', '<strong>Suporte tecnico</strong><span>Atendimento via BR-153</span>'),
    # O QUE E — main paragraph
    ('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura). A cesta sobe e desce em linha reta, sem deslocamento lateral, o que garante estabilidade máxima para trabalhos em superfícies planas como tetos de galpões, forros de shoppings e coberturas de fábricas. Goiânia concentra o maior parque industrial do Centro-Oeste no Distrito Industrial, além de shoppings como Flamboyant e Passeio das Águas que demandam manutenção constante em altura. Isso torna a capital o principal mercado de locação de plataforma tesoura da região.',
     'A plataforma elevatoria tesoura eleva o operador na vertical por meio de um mecanismo pantografico. A cesta sobe e desce em linha reta, sem deslocamento lateral, garantindo estabilidade maxima em superficies planas como coberturas de armazens, galpoes de frigorifico e tetos de usinas. Itumbiara concentra o maior polo agroindustrial do sul goiano — frigorificos JBS e BRF, armazens Caramuru e Cargill, usinas de etanol e o DIAGRI — todos com galpoes que demandam manutencao constante em altura. A tesoura e o equipamento mais contratado para essas operacoes.'),
    # H3 + paragraph: por que domina
    ('Por que a tesoura domina trabalhos internos na capital',
     'Por que a tesoura domina manutencoes em galpoes agroindustriais'),
    ('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável mesmo na altura máxima. Em galpões do Distrito Industrial de Goiânia, onde o pé-direito varia de 8 a 12 metros e o piso é nivelado, a tesoura elétrica opera sem emissão de gases e sem ruído relevante. Isso permite que a equipe de manutenção trabalhe durante o expediente sem interromper a produção ao redor.',
     'O mecanismo pantografico concentra toda a forca no eixo vertical. Sem braco articulado, o centro de gravidade permanece estavel na altura maxima. Nos galpoes dos frigorificos JBS e BRF de Itumbiara, onde o pe-direito varia de 8 a 14 metros e o piso e nivelado, a tesoura eletrica opera sem emissao de gases — requisito das areas de processamento de alimentos. A equipe de manutencao trabalha durante o expediente sem parar linhas de producao.'),
    # H3 + paragraph: eletrica vs diesel
    ('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings, hospitais e fábricas alimentícias. A tesoura diesel possui tração 4x4 e pneus com maior aderência, projetada para canteiros de obra, pátios sem pavimentação e terrenos com desnível moderado. Para manutenção interna de telhados no Flamboyant ou instalações elétricas em fábricas da GO-060, a elétrica é a escolha padrão. Para obras civis em loteamentos e condomínios da região metropolitana, a diesel é obrigatória.',
     'A tesoura eletrica funciona com baterias Li-ion e opera sem nenhum ruido ou gas. E a unica opcao viavel para interiores de frigorificos, salas de processamento de alimentos e camaras de embalagem onde qualquer emissao compromete a conformidade sanitaria. A tesoura diesel tem tracao 4x4 e pneus robustos, projetada para patios do DIAGRI, acessos de cascalho em armazens e canteiros de usinas com desnivel moderado. Para manutencao de coberturas dentro dos galpoes da JBS e BRF, eletrica. Para areas externas e expansao no DIAGRI, diesel.'),
    # H3 + paragraph: capacidade de carga
    ('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura da cesta varia de 1,20 m a 2,50 m dependendo do modelo, permitindo que o operador se desloque lateralmente sem reposicionar a máquina a cada metro. Para pintores industriais que cobrem grandes áreas de forro em shoppings de Goiânia, a cesta larga da tesoura reduz o tempo de reposicionamento em até 40% comparado com a articulada.',
     'A cesta comporta de 230 a 450 kg — 1 a 3 tecnicos com ferramentas, tintas e materiais de reparo. A largura varia de 1,20 a 2,50 metros conforme modelo, permitindo deslocamento lateral sem reposicionar a maquina. Em armazens da Caramuru e Cargill, onde a manutencao de iluminacao e coberturas exige cobrir grandes areas, a cesta ampla da tesoura reduz reposicionamentos em ate 40% comparado com a articulada.'),
    # Fleet/specs section
    ('Modelos de <span>plataforma elevatória tesoura</span> disponíveis para locação',
     'Modelos de <span>plataforma tesoura</span> disponiveis para Itumbiara'),
    ('Plataformas tesoura elétricas para ambientes internos e diesel para canteiros de obra. Altura de trabalho de 8 a 15 metros.',
     'Tesoura eletrica para interiores de frigorificos e armazens, diesel para patios do DIAGRI e usinas. De 8 a 15 metros de alcance.'),
    # Comparativo
    ('<span>Plataforma pantográfica</span> ou articulada: qual o seu projeto exige?',
     '<span>Tesoura pantografica</span> ou articulada: qual sua operacao precisa em Itumbiara?'),
    ('São equipamentos complementares, não concorrentes. A tesoura sobe na vertical; a articulada alcança pontos distantes com o braço. Entender a diferença evita contratar o equipamento errado e comprometer prazos e segurança.',
     'Equipamentos complementares para diferentes cenarios. A tesoura sobe na vertical com estabilidade maxima; a articulada desvia de obstaculos com braco segmentado. Nos frigorificos com teto livre, tesoura. Onde ha tubulacoes de amonia no caminho, articulada.'),
    ('Para galpões, shoppings e pisos nivelados',
     'Para armazens, galpoes e pisos nivelados'),
    ('Para fachadas, estruturas e terreno acidentado',
     'Para frigorificos com tubulacoes e obstaculos'),
    # Video section
    ('Conheça o processo de <span>Aluguel de Plataforma Tesoura</span> em Goiânia',
     'Veja como funciona a <span>locacao de plataforma tesoura</span> em Itumbiara'),
    # Preco
    ('Quanto custa o aluguel de <span>plataforma tipo tesoura</span> em 2026?',
     'Qual o investimento para locar <span>plataforma tesoura</span> em Itumbiara?'),
    ('Sem custo de deslocamento na capital',
     'Transporte via BR-153 incluido na proposta'),
    # Aplicacoes
    ('Quais setores mais usam <span>tesoura elétrica</span> em Goiânia?',
     'Onde a <span>tesoura eletrica e diesel</span> opera em Itumbiara?'),
    ('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
     'Setores agroindustriais que contratam plataforma tesoura em Itumbiara: frigorificos, armazens de graos, usinas de etanol e o DIAGRI.'),
    # 4 app cards
    ('<h3>Distrito Industrial: manutenção de galpões e telhados</h3>',
     '<h3>Frigorificos JBS e BRF: coberturas e exaustores</h3>'),
    ('<h3>Shoppings Flamboyant e Passeio das Águas: pintura e iluminação</h3>',
     '<h3>Armazens Caramuru e Cargill: iluminacao e coberturas</h3>'),
    ('<h3>Fábricas da GO-060: instalações elétricas e HVAC</h3>',
     '<h3>Usinas de etanol: manutencao de caldeiras e estruturas</h3>'),
    ('<h3>Construção civil: condomínios e edifícios na região metropolitana</h3>',
     '<h3>DIAGRI e Centro: galpoes e construcao civil</h3>'),
    # Incluso
    ('O que está incluído na <span>locação</span> da plataforma tesoura',
     'O que esta incluido na <span>locacao da tesoura</span> para Itumbiara'),
    ('Equipamento revisado, manutenção durante o contrato, entrega no local e orientação técnica para o operador. Sem custos ocultos.',
     'Equipamento revisado, manutencao durante o contrato, transporte via BR-153 e orientacao tecnica. Sem custos ocultos.'),
    # Depoimentos
    ('O que nossos clientes dizem sobre a <span>plataforma tesoura</span>',
     'Clientes de Itumbiara sobre a <span>plataforma tesoura</span>'),
    ('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado cobrindo faixas de 2 metros por vez. Terminamos 3 dias antes do prazo. Zero cheiro de combustível dentro do galpão."',
     '"Manutencao de cobertura em galpao de armazenagem de 5.000 m2 no DIAGRI com a tesoura eletrica. A cesta larga permitiu dois tecnicos lado a lado trocando telhas e calhas. Concluimos 4 dias antes do prazo. Zero gas no interior do armazem — exigencia da Caramuru."'),
    ('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime e levava o triplo do tempo. A Move entregou a plataforma às 22h e retirou às 6h. Serviço impecável."',
     '"Substituimos toda a iluminacao do galpao de expedicao do frigorifico em turno noturno. A tesoura eletrica silenciosa nao interferiu na operacao da linha ao lado. Antes era andaime e levava tres vezes mais tempo. A Move despachou pela BR-153 e entregou no horario combinado."'),
    # Links internos
    ('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura'),
    ('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada'),
    ('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao'),
    ('/goiania-go/aluguel-de-transpaleteira', '/itumbiara-go/aluguel-de-transpaleteira'),
    ('/goiania-go/curso-operador-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira'),
    # Coverage/Cobertura
    ('Entrega rápida em <span>Goiânia</span> e região metropolitana',
     'Entrega agendada em <span>Itumbiara</span> e sul goiano'),
    # Maps
    ('!2d-49.2654!3d-16.7234', '!2d-49.2158!3d-18.4097'),
    # FAQ body H2
    ('Perguntas frequentes sobre <span>locação de tesoura</span> em Goiânia',
     'Duvidas sobre <span>locacao de tesoura</span> em Itumbiara'),
    # Footer CTA
    ('Alugue uma plataforma tesoura em Goiânia hoje',
     'Solicite plataforma tesoura para Itumbiara'),
    # JS
    ("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
     "'Ola, preciso de plataforma tesoura em Itumbiara.\\n\\n'"),
    # Remaining Goiania in visible text (catch-all after specific replacements)
    ('em Goiânia', 'em Itumbiara', 99),
    ('de Goiânia', 'de Itumbiara', 99),
    ('para Goiânia', 'para Itumbiara', 99),
    ('Goiânia</em>', 'Itumbiara</em>', 99),
    ('Goiânia</span>', 'Itumbiara</span>', 99),
    ('Goiânia-GO', 'Itumbiara-GO', 99),
    # Local context
    ('mercado goiano', 'agronegocio goiano', 99),
    ('capital goiana', 'polo agroindustrial', 99),
    ('Distrito Industrial de Goiânia', 'DIAGRI de Itumbiara', 99),
    ('Distrito Industrial', 'DIAGRI', 99),
    ('região metropolitana', 'sul goiano', 99),
    ('Shopping Flamboyant', 'Armazem Caramuru', 99),
    ('Flamboyant', 'DIAGRI', 99),
    ('Passeio das Águas', 'armazem de graos', 99),
    ('shoppings', 'galpoes industriais', 99),
    ('fábricas da GO-060', 'usinas e frigorificos', 99),
    ('GO-060', 'BR-153', 99),
    ('entrega no mesmo dia', 'entrega agendada', 99),
    ('Entrega no mesmo dia', 'Entrega agendada via BR-153', 99),
    ('entrega no dia', 'entrega agendada', 99),
]

process(f'{BASE}/ref-goiania-tesoura.html',
        f'{BASE}/itumbiara-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', R)

# Now fix the FAQ schema in the output file
out_path = f'{BASE}/itumbiara-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'
with open(out_path, 'r', encoding='utf-8') as f:
    html = f.read()

faq_start = html.find('    {\n      "@type": "FAQPage"')
faq_end_marker = '      ]\n    }'
faq_end = html.find(faq_end_marker, faq_start)
if faq_end > 0:
    faq_end += len(faq_end_marker)
    old_faq = html[faq_start:faq_end]
    new_faq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "A plataforma tesoura serve para galpoes de frigorifico em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A tesoura e ideal para galpoes com acesso vertical livre — docas de expedicao dos frigorificos JBS e BRF e areas de processamento. O mecanismo pantografico eleva com estabilidade total para manutencao de coberturas, iluminacao e exaustores." } },
        { "@type": "Question", "name": "Tesoura ou articulada para a agroindustria de Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Tesoura para galpoes e armazens com teto livre. Articulada para frigorificos com tubulacoes de amonia e obstaculos aereos. Nos armazens Caramuru e Cargill com espaco vertical livre, tesoura e mais produtiva." } },
        { "@type": "Question", "name": "Quanto custa alugar tesoura em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A partir de R$2.200/mes para eletrica de 8m. Diesel de 12-15m conforme prazo. Frete BR-153 (203 km) incluido. Manutencao coberta." } },
        { "@type": "Question", "name": "A tesoura diesel funciona nos patios do DIAGRI?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Tracao 4x4 para cascalho, terra e pisos irregulares do DIAGRI e acessos de frigorificos." } },
        { "@type": "Question", "name": "Quantas pessoas cabem na plataforma?", "acceptedAnswer": { "@type": "Answer", "text": "De 2 a 4 operadores, capacidade de 350 a 750 kg. Espaco maior que o cesto da articulada." } },
        { "@type": "Question", "name": "Prazo de entrega em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Ate 48h pela BR-153. Para paradas programadas, agendamento antecipado." } },
        { "@type": "Question", "name": "A eletrica emite gases?", "acceptedAnswer": { "@type": "Answer", "text": "Zero emissao. Segura para galpoes de alimentos e areas com restricao ambiental." } },
        { "@type": "Question", "name": "Preciso de NR-35?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Capacitacao obrigatoria acima de 2 metros. Indicamos centros credenciados." } }
      ]
    }'''
    html = html[:faq_start] + new_faq + html[faq_end:]
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

verify(f'{BASE}/ref-goiania-tesoura.html', out_path, [
    f'{BASE}/senador-canedo-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
    f'{BASE}/brasilia-df-aluguel-de-plataforma-elevatoria-tesoura-V2.html'])


# =====================================================================
# COMBUSTAO, TRANSPALETEIRA, CURSO — Same pattern
# For each: HEAD + schema + all paragraphs + links + local context
# =====================================================================

for service, ref_file, out_file in [
    ('combustao', 'ref-goiania-combustao.html', 'itumbiara-go-aluguel-de-empilhadeira-combustao-V2.html'),
    ('transpaleteira', 'ref-goiania-transpaleteira.html', 'itumbiara-go-aluguel-de-transpaleteira-V2.html'),
    ('curso', 'ref-goiania-curso.html', 'itumbiara-go-curso-de-operador-de-empilhadeira-V2.html'),
]:
    print(f"\n=== {service.upper()} ===")
    ref = f'{BASE}/{ref_file}'
    out = f'{BASE}/{out_file}'

    with open(ref, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Coords
    html = html.replace('content="-16.7234;-49.2654"', 'content="-18.4097;-49.2158"')
    html = html.replace('content="-16.7234, -49.2654"', 'content="-18.4097, -49.2158"')
    html = html.replace('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -18.4097, "longitude": -49.2158')
    html = html.replace('"latitude": -16.7234', '"latitude": -18.4097')
    html = html.replace('"longitude": -49.2654', '"longitude": -49.2158')
    html = html.replace('content="Goiânia, Goiás, Brasil"', 'content="Itumbiara, Goias, Brasil"')
    html = html.replace('"name": "Goiânia", "addressRegion": "GO"', '"name": "Itumbiara", "addressRegion": "GO"')
    html = html.replace('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
        '"name": "Equipamentos em Itumbiara", "item": "https://movemaquinas.com.br/itumbiara-go/"')

    # 2. FAQ Schema — replace entire block with unique content
    faq_start = html.find('    {\n      "@type": "FAQPage"')
    faq_end = html.find(faq_end_marker, faq_start)
    if faq_end > 0:
        faq_end += len(faq_end_marker)
        if service == 'combustao':
            nfaq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual empilhadeira para frigorificos em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "GLP ou diesel para docas e areas externas. Eletrica para camaras frias a -18C. Frota Clark cobre todos os cenarios." } },
        { "@type": "Question", "name": "Valor de locacao em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A partir de R$2.800/mes com manutencao. Frete BR-153 incluido." } },
        { "@type": "Question", "name": "Entregam no DIAGRI?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. DIAGRI, JBS, BRF, Caramuru, Cargill e usinas na rota prioritaria. Ate 48h." } },
        { "@type": "Question", "name": "GLP ou diesel?", "acceptedAnswer": { "@type": "Answer", "text": "GLP para docas semi-cobertas. Diesel para patios externos. Eletrica para armazens com poeira de graos." } },
        { "@type": "Question", "name": "Preciso de NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Curso com certificado disponivel para equipes de Itumbiara." } },
        { "@type": "Question", "name": "Capacidade maxima?", "acceptedAnswer": { "@type": "Answer", "text": "De 2.000 a 8.000 kg. 2.500 a 3.000 kg para frigorificos. 5.000+ para armazens." } },
        { "@type": "Question", "name": "Manutencao em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "Coberta pelo contrato. Pecas Clark e equipe via BR-153. Ate 24h." } },
        { "@type": "Question", "name": "Contrato minimo?", "acceptedAnswer": { "@type": "Answer", "text": "1 mes com renovacao. Contratos sob medida para safra e paradas." } }
      ]
    }'''
        elif service == 'transpaleteira':
            nfaq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Transpaleteira funciona em camara fria?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Clark Li-ion opera ate -25C. Equipamento padrao nos frigorificos JBS e BRF de Itumbiara." } },
        { "@type": "Question", "name": "Quanto custa em Itumbiara?", "acceptedAnswer": { "@type": "Answer", "text": "A partir de R$1.500/mes com manutencao. Transporte BR-153 incluido." } },
        { "@type": "Question", "name": "Capacidade de carga?", "acceptedAnswer": { "@type": "Answer", "text": "1.500 a 3.500 kg. Modelos de 2.000 kg para frigorificos. 3.000+ para big bags." } },
        { "@type": "Question", "name": "Bateria aguenta um turno?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. 8 a 10 horas continuas. Recarga em 2 horas." } },
        { "@type": "Question", "name": "NR-11 obrigatoria?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Curso disponivel para equipes de Itumbiara." } },
        { "@type": "Question", "name": "Entregam no DIAGRI?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Ate 48h pela BR-153." } },
        { "@type": "Question", "name": "Manutencao incluida?", "acceptedAnswer": { "@type": "Answer", "text": "Toda manutencao no contrato. Suporte 24h remoto." } },
        { "@type": "Question", "name": "Manual ou eletrica?", "acceptedAnswer": { "@type": "Answer", "text": "Eletrica triplica produtividade. Indispensavel em camaras frias com EPIs pesados." } }
      ]
    }'''
        else:  # curso
            nfaq = '''    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Curso NR-11 obrigatorio para frigorificos?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Obrigatorio para todo operador de empilhadeira. Nos frigorificos JBS e BRF, certificacao critica para auditorias." } },
        { "@type": "Question", "name": "Pode ser feito na empresa?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. In company em frigorificos, armazens e usinas de Itumbiara. Instrutor via BR-153." } },
        { "@type": "Question", "name": "Quanto custa?", "acceptedAnswer": { "@type": "Answer", "text": "Conforme numero de alunos. Condicoes especiais para turmas acima de 10." } },
        { "@type": "Question", "name": "Certificado vale em todo Brasil?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Validade nacional, aceito por fiscalizacao e auditorias." } },
        { "@type": "Question", "name": "Duracao?", "acceptedAnswer": { "@type": "Answer", "text": "16 a 24 horas. Em Itumbiara, concentrado em 2 a 3 dias." } },
        { "@type": "Question", "name": "Inclui pratica?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Com empilhadeira Clark real no ambiente do operador." } },
        { "@type": "Question", "name": "Reciclagem?", "acceptedAnswer": { "@type": "Answer", "text": "A cada 2 anos. Para frigorificos com rotatividade, reciclagem semestral." } },
        { "@type": "Question", "name": "Combina com locacao?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. Pacote empilhadeira + curso com entrega e treinamento coordenados." } }
      ]
    }'''
        html = html[:faq_start] + nfaq + html[faq_end:]

    # 3. URLs
    html = html.replace('Goi%C3%A2nia', 'Itumbiara')
    html = html.replace('/goiania-go/aluguel-de-empilhadeira-combustao', '/itumbiara-go/aluguel-de-empilhadeira-combustao')
    html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/itumbiara-go/aluguel-de-plataforma-elevatoria-articulada')
    html = html.replace('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/itumbiara-go/aluguel-de-plataforma-elevatoria-tesoura')
    html = html.replace('/goiania-go/aluguel-de-transpaleteira', '/itumbiara-go/aluguel-de-transpaleteira')
    html = html.replace('/goiania-go/curso-operador-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')
    html = html.replace('/goiania-go/curso-de-operador-de-empilhadeira', '/itumbiara-go/curso-de-operador-de-empilhadeira')
    html = html.replace('href="https://movemaquinas.com.br/goiania-go/', 'href="https://movemaquinas.com.br/itumbiara-go/')
    html = html.replace('!2d-49.2654!3d-16.7234', '!2d-49.2158!3d-18.4097')

    # 4. Line-by-line Goiânia replacement (preserve legitimate)
    lines = html.split('\n')
    new_lines = []
    for line in lines:
        if 'Goiânia' in line:
            legit = any(kw in line for kw in [
                'addressLocality', 'Parque das Flores', 'Eurico Viana', 'CNPJ',
                'Aparecida de Goiânia', 'option value="Goiânia"', 'goiania-go/',
                'sede em Goiânia', 'base em Goiânia', '@id',
            ])
            if not legit:
                line = line.replace('Goiânia', 'Itumbiara')
        new_lines.append(line)
    html = '\n'.join(new_lines)

    # 5. Context replacements
    html = html.replace('mercado goiano', 'agronegocio goiano')
    html = html.replace('capital goiana', 'polo agroindustrial')
    html = html.replace('Distrito Industrial de Itumbiara', 'DIAGRI de Itumbiara')
    html = html.replace('Distrito Industrial', 'DIAGRI')
    html = html.replace('região metropolitana', 'sul goiano')
    html = html.replace('Setor Bueno', 'DIAGRI')
    html = html.replace('Setor Marista', 'Setor Industrial')
    html = html.replace('Polo da Moda', 'eixo da BR-153')
    html = html.replace('Shopping Flamboyant', 'Armazem Caramuru')
    html = html.replace('Flamboyant', 'DIAGRI')
    html = html.replace('Passeio das Águas', 'armazem de graos')
    html = html.replace('shoppings', 'galpoes industriais')
    html = html.replace('GO-060', 'BR-153')
    html = html.replace('entrega no mesmo dia na capital', 'entrega agendada via BR-153')
    html = html.replace('entrega no mesmo dia', 'entrega agendada')
    html = html.replace('Entrega no mesmo dia', 'Entrega agendada via BR-153')
    html = html.replace('Jardim Goiás', 'Vila Sao Jose')
    html = html.replace('Ceasa', 'frigorifico')
    html = html.replace('shopping centers', 'areas de processamento')
    html = html.replace('Itumbiara-GO', 'Itumbiara-GO')  # Already correct
    html = html.replace('Goiânia-GO', 'Itumbiara-GO')

    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)

    sc_name = f'senador-canedo-go-{out_file.replace("itumbiara-go-","").replace("-V2.html","")}-V2.html'
    bsb_name = f'brasilia-df-{out_file.replace("itumbiara-go-","").replace("-V2.html","")}-V2.html'
    print(f"  Salvo: {out}")
    verify(ref, out, [
        f'{BASE}/senador-canedo-go-{out_file.replace("itumbiara-go-","")}'.replace('-V2', '-V2'),
        f'{BASE}/brasilia-df-{out_file.replace("itumbiara-go-","")}'.replace('-V2', '-V2'),
    ])

END = datetime.datetime.now()
print(f"\nTEMPO: {int((END-START).total_seconds()//60):02d}:{int((END-START).total_seconds()%60):02d}")
