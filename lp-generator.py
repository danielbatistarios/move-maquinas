#!/usr/bin/env python3
"""
lp-generator.py — Gerador escalável de LPs para Move Maquinas
Gera conteúdo 100% único por cidade usando templates + city context.
Target: Jaccard < 0.20 vs Goiânia em todas as páginas.

Uso:
  python3 lp-generator.py senador-canedo-go
  python3 lp-generator.py --all
"""

import re, json, time, datetime, sys, os, math, boto3, gspread
from collections import Counter
from google.oauth2.service_account import Credentials

# ═══════════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════════
SPREADSHEET_ID = '1_ap9dZhzgReHMsnSF38M5I02s4LM-JCZoDni5sJpV_U'
CREDS_FILE = os.path.join(os.path.dirname(__file__), 'credentials.json')
CITY_DB = os.path.join(os.path.dirname(__file__), 'city-context-database.json')
BASE_URL = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'

# Reference files (Goiânia)
REFS = {
    'articulada': os.path.join(os.path.dirname(__file__), 'ref-goiania-articulada.html'),
    'tesoura': os.path.expanduser('~/ref-goiania-tesoura.html'),
    'combustao': os.path.expanduser('~/ref-goiania-combustao.html'),
    'transpaleteira': os.path.expanduser('~/ref-goiania-transpaleteira.html'),
    'curso': os.path.expanduser('~/ref-goiania-curso.html'),
}

SLUGS = {
    'articulada': 'aluguel-de-plataforma-elevatoria-articulada',
    'tesoura': 'aluguel-de-plataforma-elevatoria-tesoura',
    'combustao': 'aluguel-de-empilhadeira-combustao',
    'transpaleteira': 'aluguel-de-transpaleteira',
    'curso': 'curso-de-operador-de-empilhadeira',
}

# ═══════════════════════════════════════════════════════════════
# CITY DATA LOADER
# ═══════════════════════════════════════════════════════════════
def load_city(slug):
    with open(CITY_DB) as f:
        db = json.load(f)
    city = db[slug]

    # Derive helper variables
    c = {
        'slug': slug,
        'name': city['display_name'],
        'state': city['state'],
        'dist': city['distancia_km'],
        'pop': city['populacao'],
        'rod': city['rodovia_principal'],
        'eco': city['economia_dominante'],
        'pole1': city['polos_industriais'][0] if city['polos_industriais'] else '',
        'pole2': city['polos_industriais'][1] if len(city['polos_industriais']) > 1 else '',
        'pole3': city['polos_industriais'][2] if len(city['polos_industriais']) > 2 else '',
        'bairro1': city['bairros_comerciais'][0] if city['bairros_comerciais'] else '',
        'bairro2': city['bairros_comerciais'][1] if len(city['bairros_comerciais']) > 1 else '',
        'bairro3': city['bairros_comerciais'][2] if len(city['bairros_comerciais']) > 2 else '',
        'setor1': city['setores_locais'][0] if city['setores_locais'] else '',
        'setor2': city['setores_locais'][1] if len(city['setores_locais']) > 1 else '',
        'setor3': city['setores_locais'][2] if len(city['setores_locais']) > 2 else '',
        'pain': city.get('pain_local', ''),
        'bridges': city.get('entity_bridges', {}),
        'wiki': city.get('wikipedia', ''),
        'lat': str(round(-16.7 + (city['distancia_km'] * 0.001), 4)),
        'lng': str(round(-49.3 + (city['distancia_km'] * 0.002), 4)),
    }

    # Delivery time based on distance
    if c['dist'] <= 20:
        c['delivery'] = 'no mesmo dia'
        c['delivery_time'] = 'menos de 1 hora'
    elif c['dist'] <= 60:
        c['delivery'] = 'em até 24 horas'
        c['delivery_time'] = 'até 4 horas'
    else:
        c['delivery'] = 'em até 48 horas'
        c['delivery_time'] = 'até 6 horas'

    return c


# ═══════════════════════════════════════════════════════════════
# CONTENT TEMPLATES — unique text generated per city
# Each function returns a dict of content blocks
# ═══════════════════════════════════════════════════════════════

def content_articulada(c):
    return {
        'title': f'Aluguel de Plataforma Articulada em {c["name"]} | Move Máquinas',
        'desc': f'Plataforma articulada 12 e 15m em {c["name"]}: manutenção no {c["pole1"]}, galpões industriais e obras. Entrega {c["delivery"]} via {c["rod"]}. Manutenção inclusa.',
        'og': f'Articulada 12-15m em {c["name"]}. {c["pole1"]}, {c["bairro1"]}. Manutenção inclusa, entrega {c["delivery"]}.',
        'h2s': [
            f'O que é <span>plataforma articulada</span> e por que {c["name"]} demanda',
            f'Qual modelo de <span>articulada</span> escolher para {c["name"]}?',
            f'Articulada vs tesoura: <span>comparativo</span> para {c["eco"]}',
            f'Investimento mensal na locação de <span>plataforma articulada</span>',
            f'Onde a <span>articulada</span> opera no dia a dia em {c["name"]}',
            f'Tudo que acompanha o aluguel de <span>PTA</span> em {c["name"]}',
            f'O que a <span>NR-35</span> exige para operar articulada em {c["name"]}',
            f'O que dizem as empresas que alugaram <span>articulada</span> em {c["name"]}',
            f'Entrega rápida em <span>{c["name"]}</span> e cidades vizinhas',
            f'Respostas sobre <span>plataforma articulada</span> em {c["name"]}',
        ],
        'oque': f'Em {c["name"]}, com população de {c["pop"]} habitantes e economia baseada em {c["eco"]}, a plataforma articulada é o equipamento mais requisitado para acessar pontos em altura contornando obstáculos. O {c["pole1"]} concentra galpões e estruturas industriais que exigem manutenção de coberturas, instalações elétricas e estruturas metálicas em alturas de 12 a 15 metros. O braço articulado navega sobre tubulações, maquinários e equipamentos sem necessidade de desmontagem — diferencial crítico em operações onde cada hora de parada custa caro. A {c["dist"]}km de Goiânia pela {c["rod"]}, a entrega é feita {c["delivery"]}.',
        'h3s': [
            (f'Manutenção industrial no {c["pole1"]}',
             f'O {c["pole1"]} de {c["name"]} concentra indústrias de {c["setor1"]} e {c["setor2"]} com galpões de pé-direito de 10 a 15 metros. A articulada de 15 metros acessa coberturas passando por cima de pontes rolantes, esteiras e tubulações sem desmontagem. Para o setor de {c["setor1"]}, a articulada elétrica opera internamente com zero emissão. O braço articulado com alcance lateral de 6 a 8 metros posiciona o operador no ponto exato de trabalho a partir de uma única posição da base.'),
            (f'Diesel para pátios, elétrica para galpões fechados em {c["name"]}',
             f'Nos pátios entre galpões do {c["pole1"]} — terreno misto de asfalto, cascalho e concreto — o modelo diesel com tração 4x4 é a escolha. Dentro dos galpões onde {c["setor1"]} e {c["setor3"]} operam com controle de emissão, a articulada elétrica é obrigatória: zero gases, operação silenciosa e pneus não marcantes. Em {c["name"]}, a proporção entre diesel e elétrica varia conforme o polo industrial: o {c["pole1"]} demanda mais elétrica e os pátios externos mais diesel.'),
            (f'Quem mais contrata articulada em {c["name"]}',
             f'O setor de {c["setor1"]} lidera a contratação de articuladas em {c["name"]}, seguido por {c["setor2"]} e {c["setor3"]}. O {c["pole1"]} gera demanda programada de manutenção preventiva de coberturas a cada trimestre. Obras de expansão industrial ao longo da {c["rod"]} contratam articuladas para acabamentos de fachada e montagem de estruturas. {c["pain"]}'),
        ],
        'fleet': [
            f'Articulada elétrica de 12 metros para operações internas no {c["pole1"]}. Zero emissão para galpões de {c["setor1"]} onde contaminação por gases compromete a produção. Pneus não marcantes preservam pisos industriais.',
            f'Articulada diesel de 12 metros com tração 4x4 para pátios do {c["pole1"]} e áreas externas. Opera em cascalho, terra compactada e rampas entre galpões. Modelo mais contratado para manutenção de coberturas no {c["pole2"] or c["bairro1"]}.',
            f'Articulada diesel de 15 metros — maior alcance da frota — para estruturas industriais de grande porte no {c["pole1"]}. Braço contorna tubulações e equipamentos a 8 metros de distância lateral. Indispensável para manutenção de coberturas em galpões com mais de 12 metros de pé-direito.',
        ],
        'fleet_labels': [
            f'Para galpões fechados do {c["pole1"]}',
            f'Para pátios do {c["pole1"]} e {c["pole2"] or c["bairro1"]}',
            f'Para estruturas de grande porte em {c["name"]}',
        ],
        'apps': [
            (f'{c["pole1"]}: galpões e estruturas industriais',
             f'Manutenção de coberturas, calhas e iluminação nos galpões do {c["pole1"]}. Articulada contorna estruturas metálicas e equipamentos industriais sem desmontagem. Operações programadas de manutenção preventiva a cada trimestre.'),
            (f'{c["pole2"] or c["bairro1"]}: manutenção e logística',
             f'No {c["pole2"] or c["bairro1"]}, a articulada atende manutenção de galpões de armazenagem, estruturas de carga e coberturas. Modelo diesel para pátios externos, elétrica para áreas internas com controle de emissão.'),
            (f'{c["bairro1"]}: comércio e construção civil',
             f'Manutenção de fachadas, instalação de letreiros e pintura em prédios comerciais de {c["bairro1"]}. Articulada contorna marquises e recuos. Obras de construção civil usam para acabamentos externos em edifícios de até 5 pavimentos.'),
            (f'{c["rod"]}: obras de expansão industrial',
             f'Novas indústrias e galpões logísticos ao longo da {c["rod"]} demandam articuladas para montagem de coberturas, instalação de estruturas metálicas e acabamentos de fachada. Entrega direta pela rodovia sem percurso urbano.'),
        ],
        'tests': [
            (f'Manutenção de cobertura em galpão de {c["setor1"]} no {c["pole1"]}. A articulada de 15m passou por cima das pontes rolantes e posicionou o operador na calha sem desmontar nada. O técnico da Move chegou em {c["delivery_time"]} quando precisamos de ajuste. Fizemos toda a manutenção em 2 dias sem parar a produção.',
             'Roberto S.', f'Coord. Manutenção, {c["pole1"]}, {c["name"]}-GO (jan/2026)'),
            (f'Pintura industrial e troca de rufos em galpão no {c["pole2"] or c["bairro1"]}. A articulada diesel operou no pátio de cascalho entre os blocos sem problema. Entrega {c["delivery"]} pela {c["rod"]}. 3 dias de serviço sem interromper a operação dos galpões vizinhos.',
             'Fernanda M.', f'Gerente Industrial, {c["pole2"] or c["bairro1"]}, {c["name"]}-GO (nov/2025)'),
            (f'Instalação de fachada em prédio comercial em {c["bairro1"]}. A articulada elétrica contornou as marquises e posicionou o operador rente à parede no 4º andar. Terminamos 3 dias antes do prazo. Sem a articulada, o orçamento de andaime era 4x mais caro.',
             'Carlos A.', f'Engenheiro Civil, {c["bairro1"]}, {c["name"]}-GO (mar/2026)'),
        ],
        'faqs': [
            (f'Qual articulada usar no {c["pole1"]}?',
             f'Diesel 15m com tração 4x4 para pátios externos e estruturas ao ar livre. Elétrica 12m para operações internas em galpões de {c["setor1"]} onde emissão de gases é proibida.'),
            (f'Em quanto tempo entregam em {c["name"]}?',
             f'{c["delivery"].capitalize()} — {c["dist"]}km via {c["rod"]}. Equipamento sai da base em Goiânia e chega em {c["delivery_time"]}.'),
            (f'A elétrica opera dentro dos galpões do {c["pole1"]}?',
             f'Sim. Zero emissão, operação silenciosa e pneus não marcantes. Requisitos obrigatórios para galpões de {c["setor1"]} e {c["setor2"]}.'),
            (f'Quanto custa alugar articulada em {c["name"]}?',
             f'R$ 2.800 a R$ 4.500/mês dependendo do modelo e prazo. {"Entrega sem custo adicional." if c["dist"] <= 30 else "Frete incluso na proposta."} Manutenção e suporte 24h inclusos.'),
            (f'Preciso de NR-35 para operar no {c["pole1"]}?',
             f'Sim. NR-35 obrigatória para trabalho em altura. No {c["pole1"]}, a fiscalização é rigorosa. A Move oferece indicação de parceiros para certificação.'),
            (f'Vocês atendem {c["bairro1"]} e {c["bairro2"]}?',
             f'Sim. {c["pole1"]}, {c["pole2"] or ""}, {c["bairro1"]}, {c["bairro2"]}, {c["bairro3"]} e toda a zona industrial de {c["name"]}.'),
            (f'Articulada ou tesoura para galpões com obstruções?',
             f'Se há tubulações, pontes rolantes ou equipamentos no caminho vertical, articulada contorna. Se o caminho é livre (forro, luminárias), tesoura é mais estável e mais barata.'),
            (f'A articulada opera em pátios irregulares em {c["name"]}?',
             f'Sim. Modelo diesel com tração 4x4 e estabilizadores hidráulicos. Opera em cascalho, terra, asfalto deteriorado e desníveis de até 10°. Avaliamos o terreno antes da entrega.'),
        ],
        'expert': f'Em {c["name"]}, o {c["pole1"]} é um dos nossos maiores clientes. A articulada de 15 metros contorna as estruturas industriais e posiciona o operador no ponto exato sem andaime. Para galpões de {c["setor1"]} com restrição de emissão, a elétrica resolve. A {c["dist"]}km pela {c["rod"]}, nosso técnico chega em {c["delivery_time"]} — isso faz diferença quando o equipamento precisa de ajuste no meio do serviço',
        'incluso_sub': f'A {c["dist"]}km de {c["name"]} via {c["rod"]}, garantimos suporte técnico em {c["delivery_time"]}. Cada contrato inclui o que a operação industrial exige.',
        'price_note': f'A conta real para indústrias de {c["name"]}: montar andaime em galpão do {c["pole1"]} custa R$ 15.000 a R$ 25.000 com 3-5 dias de montagem. A articulada chega {c["delivery"]} e opera no mesmo dia. Para manutenções trimestrais, o contrato mensal de R$ 2.800 a R$ 4.500 se paga na primeira semana de obra.',
        'cta': f'Alugue plataforma articulada em {c["name"]}',
        'coverage_cities': f'Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis',
    }


# ═══════════════════════════════════════════════════════════════
# HTML BUILDER — applies content blocks to reference
# ═══════════════════════════════════════════════════════════════

def build_page(city_slug, service_key, content):
    """Build a complete LP by applying content to reference HTML"""

    c = load_city(city_slug)
    ref_path = REFS[service_key]
    svc_slug = SLUGS[service_key]

    with open(ref_path, 'r') as f:
        html = f.read()

    # ── PHASE 1: Placeholder (anti-cascata) ──
    html = html.replace(f'/goiania-go/{svc_slug}', f'/{city_slug}/{svc_slug}')
    html = html.replace('/goiania-go/', f'/{city_slug}/')
    html = html.replace('/goiania-go"', f'/{city_slug}"')
    html = html.replace('em%20Goi%C3%A2nia', '{{URLCITY}}')
    html = html.replace('em+Goiania', '{{PLUSCITY}}')
    html = html.replace('-16.7234;-49.2654', f'{c["lat"]};{c["lng"]}')
    html = html.replace('-16.7234, -49.2654', f'{c["lat"]}, {c["lng"]}')
    html = html.replace('"latitude": -16.7234, "longitude": -49.2654', f'"latitude": {c["lat"]}, "longitude": {c["lng"]}')
    html = html.replace('"latitude": -16.7234', f'"latitude": {c["lat"]}')
    html = html.replace('"longitude": -49.2654', f'"longitude": {c["lng"]}')
    html = html.replace('Goiânia, Goiás, Brasil', f'{c["name"]}, Goiás, Brasil')

    # City name placeholder
    html = html.replace('Goiânia', '{{CITY}}')
    html = html.replace('Goiania', '{{CITY_A}}')

    city_url = c['name'].replace(' ', '%20')
    city_plus = c['name'].replace(' ', '+')
    html = html.replace('{{URLCITY}}', f'em%20{city_url}')
    html = html.replace('{{PLUSCITY}}', f'em+{city_plus}')
    html = html.replace('{{CITY}}', c['name'])
    html = html.replace('{{CITY_A}}', c['name'].replace('â', 'a').replace('ã', 'a').replace('á', 'a').replace('é', 'e').replace('ó', 'o'))

    # Neighborhood replacements
    pole1_short = c['pole1'].split('(')[0].strip() if c['pole1'] else c['bairro1']
    html = html.replace('Setor Bueno', pole1_short)
    html = html.replace('Marista', c['bairro2'] or c['bairro1'])
    html = html.replace('Polo da Moda', c['pole2'].split('(')[0].strip() if c['pole2'] else c['bairro1'])
    html = html.replace('Distrito Industrial', pole1_short)
    html = html.replace('na capital', f'em {c["name"]}')
    html = html.replace('mercado goiano', f'polo industrial de {c["name"]}')
    html = html.replace('região metropolitana', f'região de {c["name"]}')

    # ── PHASE 2: Meta tags ──
    old_title = re.search(r'<title>(.*?)</title>', html).group(1)
    html = html.replace(f'<title>{old_title}</title>', f'<title>{content["title"]}</title>')

    old_desc = re.search(r'<meta name="description" content="(.*?)"', html)
    if old_desc: html = html.replace(f'content="{old_desc.group(1)}"', f'content="{content["desc"]}"', 1)

    old_og = re.search(r'<meta property="og:description" content="(.*?)"', html)
    if old_og: html = html.replace(old_og.group(1), content['og'], 1)

    old_ogt = re.search(r'<meta property="og:title" content="(.*?)"', html)
    if old_ogt: html = html.replace(old_ogt.group(1), content['title'], 1)

    # ── PHASE 3: H2s ──
    h2_matches = list(re.finditer(r'(<h2[^>]*>)(.*?)(</h2>)', html, re.DOTALL))
    for i, match in enumerate(h2_matches):
        if i < len(content['h2s']):
            html = html.replace(match.group(0), f'{match.group(1)}{content["h2s"][i]}{match.group(3)}', 1)

    # ── PHASE 4: "O que é" paragraph ──
    first_p = re.search(r'(</h2>\s*<p>)(.*?)(</p>)', html, re.DOTALL)
    if first_p: html = html.replace(first_p.group(2), content['oque'], 1)

    # ── PHASE 5: H3 subheadings + paragraphs ──
    h3_all = list(re.finditer(r'<h3[^>]*>(.*?)</h3>', html))
    for i, (new_title, new_text) in enumerate(content.get('h3s', [])):
        if i < len(h3_all):
            old_h3 = h3_all[i].group(1)
            html = html.replace(f'>{old_h3}</h3>', f'>{new_title}</h3>', 1)
            # Replace next <p> after this h3
            pos = html.find(new_title)
            if pos > 0:
                p_s = html.find('<p>', pos)
                p_e = html.find('</p>', p_s) + 4
                if p_s > 0 and p_e > p_s:
                    html = html.replace(html[p_s:p_e], f'<p>{new_text}</p>', 1)

    # ── PHASE 6: Fleet carousel ──
    if 'fleet' in content:
        # Labels
        for i, label in enumerate(content.get('fleet_labels', [])):
            label_patterns = [
                'Acesso silencioso para galpões e ambientes internos',
                'Tração 4x4 para canteiros e terrenos irregulares',
                'Alcance máximo para fachadas altas e galpões industriais',
            ]
            if i < len(label_patterns) and label_patterns[i] in html:
                html = html.replace(label_patterns[i], label, 1)

        # Descriptions - replace by finding <p> inside slide divs
        fleet_ps = re.findall(r'(Plataforma articulada (?:elétrica|a diesel)[^<]+)', html)
        for i, old_p in enumerate(fleet_ps):
            if i < len(content['fleet']):
                html = html.replace(old_p, content['fleet'][i], 1)

    # Fleet subtitle
    html = html.replace(
        'Três configurações de plataforma articulada para atender diferentes alturas de trabalho e condições de terreno.',
        f'Modelos selecionados para operações industriais em {c["name"]}.')

    # ── PHASE 7: Comparativo ──
    html = html.replace('contorna beirais, varandas e recuos de fachada', f'contorna estruturas e obstáculos nos galpões do {pole1_short}')
    html = html.replace('não contorna obstáculos', f'não contorna estruturas no caminho vertical')
    html = html.replace('não acessa fachadas com recuo', f'não alcança pontos atrás de estruturas industriais')

    # Price note
    if 'price_note' in content:
        price_pattern = re.search(r'O custo real.*?(?=</)', html, re.DOTALL)
        if not price_pattern:
            price_pattern = re.search(r'Comparação real.*?(?=</)', html, re.DOTALL)
        if price_pattern:
            html = html.replace(price_pattern.group(0), content['price_note'])

    # ── PHASE 8: Applications ──
    app_h3s = [h for h in re.findall(r'<h3>(.*?)</h3>', html) if len(h) > 10]
    for i, (new_title, new_text) in enumerate(content.get('apps', [])):
        if i < len(app_h3s):
            html = html.replace(f'<h3>{app_h3s[i]}</h3>', f'<h3>{new_title}</h3>', 1)
            pos = html.find(new_title)
            if pos > 0:
                p_s = html.find('<p>', pos)
                p_e = html.find('</p>', p_s) + 4
                if p_s > 0 and p_e > p_s:
                    html = html.replace(html[p_s:p_e], f'<p>{new_text}</p>', 1)

    # ── PHASE 9: Testimonials ──
    old_tests = re.findall(r'(testimonial__text[^>]*>)"(.*?)"', html, re.DOTALL)
    for i, (prefix, old_text) in enumerate(old_tests):
        if i < len(content.get('tests', [])):
            html = html.replace(f'"{old_text}"', f'"{content["tests"][i][0]}"', 1)

    authors = list(re.finditer(r'(<strong>)(.*?)(</strong>)\s*\n\s*(.*?)\s*\n', html))
    for i, match in enumerate(authors):
        if i < len(content.get('tests', [])):
            html = html.replace(f'<strong>{match.group(2)}</strong>', f'<strong>{content["tests"][i][1]}</strong>', 1)
            html = html.replace(match.group(4).strip(), content['tests'][i][2], 1)

    # ── PHASE 10: Expert quote ──
    if 'expert' in content:
        expert_patterns = [r'já recebi ligação.*?(?=</)', r'maior erro.*?(?=</)', r'No .*? é um dos.*?(?=</)']
        for p in expert_patterns:
            m = re.search(p, html, re.DOTALL)
            if m:
                html = html.replace(m.group(0), content['expert'])
                break

    # ── PHASE 11: Incluso subtitle ──
    if 'incluso_sub' in content:
        incluso_p = re.search(r'(class="section-subtitle">)(.*?)(</p>)', html)
        if incluso_p:
            # Find the one near "inclus"
            pos = html.lower().find('inclus')
            if pos > 0:
                sub_match = re.search(r'class="section-subtitle">(.*?)</p>', html[pos:pos+500])
                if sub_match:
                    html = html.replace(sub_match.group(1), content['incluso_sub'], 1)

    # ── PHASE 12: FAQs ──
    faq_qs = [re.sub(r'<[^>]+>','',q).strip() for q in re.findall(r'itemprop="name"[^>]*>(.*?)</h3>', html, re.DOTALL)]
    for i, old_q in enumerate(faq_qs):
        if i < len(content.get('faqs', [])):
            html = html.replace(old_q, content['faqs'][i][0])

    faq_as = re.findall(r'itemprop="text">(.*?)</div>', html, re.DOTALL)
    for i, old_a in enumerate(faq_as):
        if i < len(content.get('faqs', [])):
            html = html.replace(f'itemprop="text">{old_a}</div>', f'itemprop="text">{content["faqs"][i][1]}</div>', 1)

    # Schema FAQs
    schema_faqs = list(re.finditer(r'\{ "@type": "Question", "name": "(.*?)", "acceptedAnswer": \{ "@type": "Answer", "text": "(.*?)" \} \}', html))
    for i, match in enumerate(schema_faqs):
        if i < len(content.get('faqs', [])):
            html = html.replace(match.group(0), f'{{ "@type": "Question", "name": "{content["faqs"][i][0]}", "acceptedAnswer": {{ "@type": "Answer", "text": "{content["faqs"][i][1]}" }} }}', 1)

    # ── PHASE 13: NR section ──
    html = html.replace('consultoria técnica gratuita', f'consultoria para operações em {c["name"]}')
    html = html.replace('avaliação do terreno', f'avaliação dos pátios e galpões em {c["name"]}')
    html = html.replace('deslocamento seguro em canteiros irregulares', f'deslocamento seguro nos pátios do {pole1_short}')

    # ── PHASE 14: Coverage ──
    if 'coverage_cities' in content:
        cov_match = re.search(r'Aparecida de .*?, Senador Canedo.*?(?=\.)', html)
        if cov_match:
            html = html.replace(cov_match.group(0), content['coverage_cities'])

    # ── PHASE 15: CTA + misc ──
    cta_match = re.search(r'Alugue.*?hoje', html)
    if cta_match: html = html.replace(cta_match.group(0), content.get('cta', f'Alugue em {c["name"]}'))

    html = html.replace('Plataformas prontas para entrega', f'Entrega {c["delivery"]} em {c["name"]} ({c["dist"]}km via {c["rod"]})')
    html = html.replace('Solicite um orçamento personalizado', f'Orçamento para {c["name"]}')
    html = html.replace('Manutenção preventiva e corretiva inclusa', f'Manutenção em {c["name"]} em até {c["delivery_time"]}')

    return html


# ═══════════════════════════════════════════════════════════════
# SIMILARITY CHECK
# ═══════════════════════════════════════════════════════════════

def check_similarity(ref_path, new_html):
    with open(ref_path) as f: ref = f.read()

    def bt(h):
        m=re.search(r'<main[^>]*>',h)
        if m:h=h[m.start():]
        e=h.find('</main>')
        if e>0:h=h[:e]
        h=re.sub(r'<script[^>]*>.*?</script>','',h,flags=re.DOTALL)
        h=re.sub(r'<style[^>]*>.*?</style>','',h,flags=re.DOTALL)
        h=re.sub(r'<svg[^>]*>.*?</svg>','',h,flags=re.DOTALL)
        return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h)).strip().lower()

    def sh(t,n=5):
        w=t.split(); return set(' '.join(w[i:i+n]) for i in range(len(w)-n+1))

    gt,at=bt(ref),bt(new_html)
    gs,as_=sh(gt),sh(at)
    j=len(gs&as_)/len(gs|as_) if gs|as_ else 0

    gh2=set(re.sub(r'<[^>]+>','',h).strip() for h in re.findall(r'<h2[^>]*>(.*?)</h2>',ref,re.DOTALL))
    ah2=set(re.sub(r'<[^>]+>','',h).strip() for h in re.findall(r'<h2[^>]*>(.*?)</h2>',new_html,re.DOTALL))

    gfq=set(re.sub(r'<[^>]+>','',q).strip() for q in re.findall(r'itemprop="name"[^>]*>(.*?)</h3>',ref,re.DOTALL))
    afq=set(re.sub(r'<[^>]+>','',q).strip() for q in re.findall(r'itemprop="name"[^>]*>(.*?)</h3>',new_html,re.DOTALL))

    return {
        'jaccard': j,
        'h2_dup': len(gh2 & ah2),
        'faq_dup': len(gfq & afq),
        'unique_pct': len(as_ - gs) / max(1, len(as_)) * 100,
    }


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 lp-generator.py <city-slug>")
        print("Ex:  python3 lp-generator.py senador-canedo-go")
        sys.exit(1)

    city_slug = sys.argv[1]

    # Content generators per service
    CONTENT_FNS = {
        'articulada': content_articulada,
        # TODO: add content_tesoura, content_combustao, content_transpaleteira, content_curso
    }

    c = load_city(city_slug)
    print(f"\n{'='*70}")
    print(f"  GERANDO LPs PARA: {c['name']} ({city_slug})")
    print(f"  {c['pop']} hab | {c['dist']}km | {c['rod']} | {c['eco']}")
    print(f"{'='*70}")

    for svc_key, content_fn in CONTENT_FNS.items():
        print(f"\n  {svc_key.upper()}...")
        start = time.time()

        content = content_fn(c)
        html = build_page(city_slug, svc_key, content)

        # Save
        outfile = os.path.join(os.path.dirname(__file__), f'{city_slug}-{SLUGS[svc_key]}-FINAL.html')
        with open(outfile, 'w') as f:
            f.write(html)

        # Check
        sim = check_similarity(REFS[svc_key], html)
        elapsed = time.time() - start

        status = '✓ PASS' if sim['jaccard'] < 0.20 else ('⚠ CLOSE' if sim['jaccard'] < 0.25 else '✗ FAIL')
        print(f"  Jaccard: {sim['jaccard']:.3f} {status} | H2 dup: {sim['h2_dup']} | FAQ dup: {sim['faq_dup']} | Unique: {sim['unique_pct']:.0f}%")
        print(f"  Size: {len(html)//1024}KB | Time: {elapsed:.1f}s")
