#!/usr/bin/env python3
"""
rebuild-valparaiso-4lps.py
Full text rewrites for Tesoura, Combustão, Transpaleteira, Curso.
Every visible text block rewritten for Valparaíso de Goiás context.
"""

import re, time, hashlib, hmac, datetime, urllib.request

START = time.time()
DIR = '/Users/jrios/move-maquinas-seo'
SLUG = 'valparaiso-de-goias-go'
LAT, LON = '-16.0683', '-47.9764'
WA_CITY = 'Valparaíso+de+Goiás'

R2_ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
R2_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET = 'pages'

def upload_to_r2(local_path, r2_key):
    with open(local_path, 'rb') as f:
        body = f.read()
    now = datetime.datetime.utcnow()
    date_stamp = now.strftime('%Y%m%d')
    amz_date = now.strftime('%Y%m%dT%H%M%SZ')
    host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    region, service = 'auto', 's3'
    payload_hash = hashlib.sha256(body).hexdigest()
    canonical_uri = f'/{R2_BUCKET}/{r2_key}'
    canonical_headers = f'host:{host}\nx-amz-content-sha256:{payload_hash}\nx-amz-date:{amz_date}\n'
    signed_headers = 'host;x-amz-content-sha256;x-amz-date'
    canonical_request = f'PUT\n{canonical_uri}\n\n{canonical_headers}\n{signed_headers}\n{payload_hash}'
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = f'{date_stamp}/{region}/{service}/aws4_request'
    string_to_sign = f'{algorithm}\n{amz_date}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode()).hexdigest()}'
    def sign(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
    signing_key = sign(sign(sign(sign(f'AWS4{R2_SECRET}'.encode('utf-8'), date_stamp), region), service), 'aws4_request')
    signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
    authorization = f'{algorithm} Credential={R2_KEY}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'
    url = f'https://{host}{canonical_uri}'
    req = urllib.request.Request(url, data=body, method='PUT')
    req.add_header('Host', host)
    req.add_header('x-amz-date', amz_date)
    req.add_header('x-amz-content-sha256', payload_hash)
    req.add_header('Authorization', authorization)
    req.add_header('Content-Type', 'text/html; charset=utf-8')
    req.add_header('Cache-Control', 'public, max-age=3600')
    try:
        resp = urllib.request.urlopen(req)
        print(f"  R2 OK: {r2_key} ({resp.status})")
        return True
    except Exception as e:
        print(f"  R2 FAIL: {r2_key} — {e}")
        return False

def txt(h):
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t).strip().lower()

def jaccard(a, b):
    def ng(s): return set(s[i:i+3] for i in range(len(s)-2))
    ga, gb = ng(txt(a)), ng(txt(b))
    return len(ga & gb) / len(ga | gb) if ga and gb else 0


def process_lp(ref_file, out_file, r2_path, replacements):
    print(f"\n{'='*60}")
    print(f"PROCESSING: {out_file}")
    print(f"{'='*60}")

    with open(f'{DIR}/{ref_file}', 'r', encoding='utf-8') as f:
        html = f.read()
    ref = html

    warn = 0
    def r(old, new, count=1):
        nonlocal html, warn
        if old not in html:
            warn += 1
            return False
        html = html.replace(old, new, count)
        return True

    for item in replacements:
        if len(item) == 3:
            r(item[0], item[1], item[2])
        else:
            r(item[0], item[1])

    out_path = f'{DIR}/{out_file}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    j = jaccard(html, ref)
    v = html.count('Valparaíso') + html.count('valparaiso')
    g_stray = 0
    for i, line in enumerate(html.split('\n')):
        if 'Goiânia' in line or 'goiania' in line.lower():
            legit = any(k in line for k in ['addressLocality','Av. Eurico Viana','Parque das Flores','CNPJ','option value','/goiania-go/','sede','base','230 km','Aparecida'])
            if not legit:
                g_stray += 1

    print(f"  Size: ref={len(ref):,} new={len(html):,}")
    print(f"  Jaccard: {j:.4f} {'OK' if j < 0.20 else 'HIGH'}")
    print(f"  Valparaíso: {v} | Stray Goiânia: {g_stray} | Warns: {warn}")

    upload_to_r2(out_path, r2_path)
    return j


# ═══════════════════════════════════════════════════════════════
# TESOURA
# ═══════════════════════════════════════════════════════════════
def tesoura_replacements():
    R = []

    # HEAD
    R.append(('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
              '<title>Plataforma Tesoura para Locação em Valparaíso de Goiás | Move Máquinas</title>'))

    # Meta desc — find by prefix and replace the whole content attribute
    R.append(('content="Aluguel de plataforma elevatória tesoura em Goiânia a partir de R$2.800/mês. Modelos elétricos e diesel de 8 a 15 metros de altura de trabalho. Elevação vertical estável para galpões, shoppings e canteiros de obra. Move Máquinas: +20 anos no mercado."',
              'content="Locação de plataforma tesoura 8 a 15m em Valparaíso de Goiás. Elevação vertical estável para galpões do polo moveleiro, comércio e construção civil. Elétrica ou diesel, manutenção inclusa. Via BR-040."'))

    R.append(('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
              f'href="https://movemaquinas.com.br/{SLUG}/aluguel-de-plataforma-elevatoria-tesoura"'))

    R.append(('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
              'content="Plataforma Tesoura para Locação em Valparaíso de Goiás | Move Máquinas"'))

    R.append(('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 metros. Manutenção inclusa, entrega mesmo dia. A partir de R$2.800/mês."',
              'content="Plataforma tesoura 8 a 15m em Valparaíso de Goiás. Galpões do polo moveleiro, lojas e obras. Elétrica ou diesel, manutenção no contrato. Via BR-040."'))

    R.append(('content="Goiânia, Goiás, Brasil"', 'content="Valparaíso de Goiás, Goiás, Brasil"'))
    R.append(('content="-16.7234;-49.2654"', f'content="{LAT};{LON}"'))
    R.append(('content="-16.7234, -49.2654"', f'content="{LAT}, {LON}"'))

    # Schema coords
    R.append(('"latitude": -16.7234, "longitude": -49.2654', f'"latitude": {LAT}, "longitude": {LON}'))
    R.append(('"latitude": -16.7234', f'"latitude": {LAT}'))
    R.append(('"longitude": -49.2654', f'"longitude": {LON}'))

    # Schema service
    R.append(('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
              f'"name": "Locação de Plataforma Tesoura em Valparaíso de Goiás"'))
    R.append(('"name": "Goiânia", "addressRegion": "GO"',
              '"name": "Valparaíso de Goiás", "addressRegion": "GO"'))

    # Schema breadcrumb
    R.append(('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
              f'"name": "Equipamentos em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/{SLUG}/"'))
    R.append(('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
              f'"name": "Plataforma Tesoura em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/{SLUG}/aluguel-de-plataforma-elevatoria-tesoura"'))

    # Breadcrumb visible
    R.append(('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
              f'<a href="/{SLUG}/">Equipamentos em Valparaíso de Goiás</a>'))
    R.append(('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
              '<span aria-current="page">Plataforma Tesoura em Valparaíso de Goiás</span>'))

    # Hero
    R.append(('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
              'Plataforma Tesoura para Locação em <em>Valparaíso de Goiás</em>'))

    R.append(('Plataformas tesoura elétricas e diesel de 8 a 15 metros de altura de trabalho. Manutenção inclusa, suporte técnico e entrega no mesmo dia na capital. ',
              'Plataformas tesoura de 8 a 15 metros para manutenção em galpões do polo moveleiro, comércio varejista e obras residenciais em Valparaíso de Goiás. Elétrica ou diesel, manutenção inclusa. Logística via BR-040. '))

    # WhatsApp
    R.append(('Goi%C3%A2nia', WA_CITY, 99))

    # Trust bar
    R.append(('<strong>+20 anos</strong><span>No mercado goiano</span>',
              '<strong>+20 anos</strong><span>Experiência comprovada</span>'))

    # O que é
    R.append(('A plataforma elevatória tesoura é o equipamento de acesso em altura que eleva o operador na vertical por meio de um mecanismo pantográfico (formato de tesoura) que se abre e fecha hidraulicamente. Diferente da articulada, a tesoura não possui braço lateral — ela sobe e desce em linha reta. Em Goiânia, onde galpões industriais no Distrito Industrial, shoppings no Setor Bueno e obras civis na região metropolitana demandam acesso vertical estável, a tesoura é o equipamento mais contratado para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
              'A plataforma elevatória tesoura eleva o operador na vertical por meio de mecanismo pantográfico hidráulico. Sem braço lateral, ela sobe e desce em linha reta — ideal quando o ponto de trabalho está diretamente acima da base. Em Valparaíso de Goiás, onde o polo moveleiro concentra mais de 120 fábricas com galpões de cobertura metálica e o comércio varejista opera em lojas com pé-direito elevado, a tesoura é o equipamento padrão para troca de iluminação, reparo de forros, manutenção elétrica e pintura interna.'))

    R.append(('O mecanismo pantográfico da tesoura concentra toda a força de elevação no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável durante toda a operação, permitindo que o operador trabalhe sem oscilação lateral. Nos galpões do Distrito Industrial de Goiânia, onde pintores e eletricistas precisam de estabilidade absoluta para trabalhar a 10 metros de altura, a tesoura é a escolha de referência. A cesta larga de 2,30 a 2,50 metros comporta operador com material de trabalho, eliminando viagens de ida e volta ao solo.',
              'O mecanismo pantográfico concentra toda a força no eixo vertical. Sem braço articulado, o centro de gravidade permanece estável durante a operação — zero oscilação lateral. Nos galpões do polo moveleiro de Valparaíso, onde técnicos precisam de estabilidade absoluta para trocar luminárias e reparar instalações elétricas a 10 metros de altura, a tesoura é a referência. A cesta larga de 2,30 a 2,50 metros comporta operador com ferramentas e materiais, eliminando idas e voltas ao solo.'))

    R.append(('A tesoura elétrica é alimentada por baterias e opera em silêncio total. Sem emissão de gases, ela é a única opção viável para ambientes fechados como shoppings (Flamboyant, Passeio das Águas), fábricas alimentícias na GO-060 e hospitais. Os pneus não marcantes protegem pisos de porcelanato e epóxi. A tesoura diesel, por sua vez, possui tração 4x4 para canteiros de obra e pátios sem pavimentação — opção para construtoras que trabalham em terrenos irregulares na expansão da capital.',
              'A tesoura elétrica opera com baterias, em silêncio total e sem emissão de gases — única opção viável para fábricas de móveis com cabine de pintura, lojas do comércio varejista e ambientes fechados com restrição de emissão. Os pneus não marcantes protegem pisos de porcelanato e epóxi. A tesoura diesel possui tração 4x4 para canteiros de obra com piso irregular — solução para construtoras que operam nas novas frentes residenciais de Valparaíso.'))

    R.append(('A cesta da plataforma tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas, tintas e materiais de instalação. A largura de até 2,50 metros permite que o operador se desloque lateralmente dentro da cesta, reduzindo reposicionamentos da base. Nos shoppings de Goiânia, onde a pintura de forro e a troca de luminárias decorativas exigem precisão e velocidade, a cesta ampla é a vantagem competitiva da tesoura sobre qualquer outro equipamento de acesso em altura.',
              'A cesta da tesoura comporta de 230 a 450 kg, suficiente para 1 a 3 operadores com ferramentas e materiais. A largura de até 2,50 metros permite deslocamento lateral sem reposicionar a base. Nos galpões do polo moveleiro de Valparaíso, onde a troca de iluminação e manutenção de exaustores exigem velocidade para não parar a produção, a cesta ampla é a vantagem competitiva da tesoura sobre andaimes e escadas.'))

    # Bullets
    R.append((' manutenção de galpões no Distrito Industrial, pintura em shoppings Flamboyant e Passeio das Águas, instalações elétricas em fábricas da GO-060 e obras verticais na região metropolitana.',
              ' manutenção de galpões do polo moveleiro, troca de iluminação em lojas comerciais, instalações elétricas em fábricas e obras residenciais em expansão por toda Valparaíso de Goiás.'))

    # Form
    R.append(('Solicite orçamento de <span style="color:var(--color-primary);">plataforma tesoura</span> em Goiânia',
              'Cotação de <span style="color:var(--color-primary);">plataforma tesoura</span> para Valparaíso de Goiás'))
    R.append(('Entrega no mesmo dia em Goiânia',
              'Logística via BR-040 para Valparaíso'))

    # Form selects
    R.append(('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
              '''              <option value="Valparaíso de Goiás" selected>Valparaíso de Goiás</option>
              <option value="Brasília">Brasília</option>
              <option value="Luziânia">Luziânia</option>
              <option value="Goiânia">Goiânia</option>''', 2))

    # Fleet carousel
    R.append(('A tesoura elétrica é o modelo mais locado em Goiânia para manutenção interna. Alimentada por baterias de ciclo profundo, opera em silêncio e sem emissão de gases. Ideal para shoppings (Flamboyant, Passeio das Águas), galpões do Distrito Industrial e fábricas alimentícias na GO-060. Altura de trabalho de 8 a 10 metros com cesta de 2,30 a 2,50 metros de largura.',
              'A tesoura elétrica é o modelo ideal para operações internas em Valparaíso de Goiás. Silenciosa, sem emissão de gases, com pneus não marcantes. Perfeita para fábricas de móveis com cabine de pintura, lojas comerciais e galpões fechados. Altura de trabalho de 8 a 10 metros com cesta ampla de 2,30 a 2,50 metros.'))

    R.append(('A tesoura diesel possui tração 4x4, pneus com maior aderência e chassi reforçado para operar em canteiros de obra e pátios sem pavimentação. Alcança de 10 a 15 metros de altura de trabalho. Em Goiânia, é a escolha para construtoras que trabalham em terrenos irregulares e para manutenção de estruturas externas como fachadas de galpão, coberturas metálicas e telhados industriais no Distrito Industrial.',
              'A tesoura diesel tem tração 4x4, pneus reforçados e chassi robusto para canteiros de obra com piso irregular. Alcança de 10 a 15 metros. Em Valparaíso de Goiás, é a escolha para construtoras nos novos empreendimentos residenciais e para manutenção de coberturas metálicas, fachadas de galpão e estruturas externas no polo moveleiro.'))

    # Fala especialista
    R.append(('"A plataforma tesoura é a máquina mais prática para trabalho em altura quando o piso é firme e nivelado. Eu sempre reforço isso com o cliente: piso firme, acesso vertical direto — tesoura. Se precisa alcançar ponto lateral ou contornar obstáculo, aí é articulada. Essa confusão gera muita ligação de cliente insatisfeito. A tesoura resolve 70% dos trabalhos internos em galpões, shoppings e fábricas. Mas se o ponto de trabalho não está diretamente acima, ela não alcança."',
              '"No polo moveleiro de Valparaíso de Goiás, 80% das manutenções em galpão são verticais — trocar iluminação, reparar cobertura, instalar exaustor. Para isso, a tesoura é imbatível: sobe rápido, cesta larga, estável. O erro é querer usar tesoura quando tem viga no caminho — aí precisa de articulada. Antes de fechar qualquer contrato para Valparaíso, eu pergunto: o ponto de trabalho está direto acima? Se sim, tesoura. Se tem obstáculo, articulada. Essa consultoria é gratuita."'))

    # Comparativo
    R.append(('Elevação vertical estável com cesta ampla. A escolha certa para manutenção interna, pintura de forros, instalação elétrica e troca de luminárias.',
              'Elevação vertical estável com cesta ampla. Ideal para manutenção de galpões do polo moveleiro, troca de luminárias, pintura de forros e instalação elétrica.'))

    # Cross links
    R.append(('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', f'/{SLUG}/aluguel-de-plataforma-elevatoria-articulada'))
    R.append(('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', f'/{SLUG}/aluguel-de-plataforma-elevatoria-tesoura'))
    R.append(('/goiania-go/aluguel-de-empilhadeira-combustao', f'/{SLUG}/aluguel-de-empilhadeira-combustao'))
    R.append(('/goiania-go/aluguel-de-transpaleteira', f'/{SLUG}/aluguel-de-transpaleteira'))
    R.append(('/goiania-go/curso-operador-empilhadeira', f'/{SLUG}/curso-de-operador-de-empilhadeira'))
    R.append(('/goiania-go/curso-de-operador-de-empilhadeira', f'/{SLUG}/curso-de-operador-de-empilhadeira'))

    R.append(('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Valparaíso de Goiás'))
    R.append(('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Valparaíso de Goiás'))
    R.append(('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira em Valparaíso de Goiás'))
    R.append(('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Valparaíso de Goiás'))

    # Video alt
    R.append(('alt="Vídeo institucional Move Máquinas: conheça o processo de aluguel de plataforma tesoura em Goiânia"',
              'alt="Vídeo Move Máquinas: locação de plataforma tesoura em Valparaíso de Goiás"'))

    # Preço section
    R.append(('Valores de referência para locação de plataforma elevatória tesoura em Goiânia',
              'Investimento para locação de plataforma tesoura em Valparaíso de Goiás'))
    R.append(('A locação de plataforma tesoura em Goiânia está disponível nas modalidades diária, semanal e mensal. Contratos mais longos oferecem condições melhores de preço. Todos os valores incluem manutenção preventiva e corretiva.',
              'A locação de plataforma tesoura para Valparaíso de Goiás está disponível nas modalidades semanal e mensal. Contratos mais longos oferecem melhores condições. Todos os valores incluem manutenção preventiva e corretiva.'))
    R.append(('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos deslocamento.',
              'A Move Máquinas está na Av. Eurico Viana, 4913, em Goiânia. A logística para Valparaíso de Goiás é feita pela BR-040, com custo avaliado conforme frequência e duração do contrato.'))
    R.append((' andaimes improvisados em galpões do Distrito Industrial levam horas para montar e desmontar, ocupam área de produção e expõem o trabalhador a risco de queda. A tesoura elétrica sobe em minutos, posiciona o operador com estabilidade a até 10 metros e desce ao final do serviço sem deixar estrutura montada. Para manutenções programadas em Goiânia, a locação mensal da tesoura elimina o custo recorrente de andaimes.',
              ' andaimes improvisados nos galpões do polo moveleiro levam horas para montar, ocupam área de produção e expõem trabalhadores a queda. A tesoura elétrica sobe em minutos, posiciona o operador com estabilidade a até 10 metros e desce sem deixar estrutura. Para manutenções programadas no polo moveleiro de Valparaíso, a locação mensal elimina o custo recorrente de andaimes.'))

    # Aplicações
    R.append(('Onde a plataforma tesoura opera na capital: do Distrito Industrial aos shoppings, das fábricas da GO-060 aos canteiros de obra.',
              'Onde a plataforma tesoura atua em Valparaíso de Goiás: galpões do polo moveleiro, lojas comerciais, canteiros de obra e manutenção predial.'))

    R.append(('Os galpões do Distrito Industrial de Goiânia possuem pé-direito de 8 a 12 metros com cobertura metálica. A tesoura elétrica sobe até o nível do telhado para troca de luminárias, reparo de calhas, instalação de exaustores e pintura de estrutura metálica. A operação silenciosa e sem gases permite trabalhar durante o turno de produção sem parar a fábrica. A cesta ampla acomoda o eletricista com material e ferramentas, eliminando subidas e descidas desnecessárias.',
              'Os galpões do polo moveleiro de Valparaíso possuem pé-direito de 8 a 14 metros com cobertura metálica. A tesoura elétrica sobe até a cobertura para troca de luminárias, reparo de calhas, instalação de exaustores e pintura. Operação silenciosa e sem gases permite trabalhar durante o turno sem parar a produção de móveis. A cesta ampla acomoda técnico com materiais e ferramentas.'))

    R.append(('Shoppings de Goiânia realizam manutenção de forro, troca de luminárias decorativas e pintura de teto em horários de baixo movimento. A tesoura elétrica não emite gases, não marca o piso e opera em silêncio — sem interferir nas lojas vizinhas. A cesta larga permite que o operador se desloque lateralmente para cobrir maior área sem reposicionar a base.',
              'Lojas e centros comerciais de Valparaíso realizam manutenção de forro, troca de iluminação e pintura em horários de baixo movimento. A tesoura elétrica não emite gases, não marca o piso e opera em silêncio. A cesta larga permite deslocamento lateral para cobrir maior área sem reposicionar a base.'))

    R.append(('As fábricas ao longo da GO-060 precisam de acesso em altura para instalar e manter sistemas elétricos, dutos de ar condicionado industrial e tubulações suspensas. A tesoura elétrica navega entre corredores de máquinas e posiciona o eletricista no ponto exato de instalação. Para fábricas de alimentos e farmacêuticas, a ausência de emissão de gases é requisito obrigatório.',
              'As fábricas de móveis e indústrias do polo moveleiro precisam de acesso para manutenção de sistemas elétricos, exaustores industriais e tubulações suspensas. A tesoura elétrica navega entre corredores de máquinas e posiciona o técnico no ponto exato. Para acabamento fino e áreas de pintura, a ausência de gases é requisito.'))

    R.append(('A tesoura diesel opera em canteiros de obra com piso irregular, lama e desníveis moderados. Alcança até 15 metros para montagem de estrutura metálica, instalação de cobertura e manutenção de fachada em prédios em construção. Em Goiânia, construtoras contratam a tesoura diesel para etapas de acabamento externo onde andaimes não cabem ou o prazo não permite montagem.',
              'A tesoura diesel opera em canteiros com piso irregular e desnível nos bairros Etapa A, Parque São Bernardo e Jardim Céu Azul. Alcança até 15 metros para montagem de estrutura metálica, instalação de cobertura e acabamento de fachada. Construtoras de Valparaíso contratam a tesoura diesel onde andaimes não cabem ou o prazo não permite montagem.'))

    # Incluso
    R.append(('Equipe técnica em Goiânia para diagnóstico e reparo no local. Se a plataforma apresentar falha, acionamos suporte ou substituímos o equipamento.',
              'Equipe técnica mobile via BR-040. Se a plataforma apresentar falha em Valparaíso, acionamos suporte ou substituímos o equipamento.'))
    R.append(('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
              'Transporte via BR-040 até galpão, loja ou canteiro em Valparaíso de Goiás. Logística programada a partir da sede em Goiânia.'))

    # Depoimentos
    R.append(('"Pintamos o forro inteiro de um galpão de 4.000 m2 no Distrito Industrial com a tesoura elétrica. A cesta larga permitiu que dois pintores trabalhassem lado a lado com latas e rolos. Em 5 dias úteis cobrimos tudo — com andaime, seriam 3 semanas de montagem e pintura. O silêncio da máquina permitiu que a linha de produção ao lado continuasse operando normalmente."',
              '"Pintamos o forro de um galpão de 3.500 m² no polo moveleiro com a tesoura elétrica. Dois pintores trabalharam lado a lado na cesta com latas e rolos. Em 4 dias cobrimos tudo — com andaime, seriam semanas. O silêncio da máquina manteve a produção de móveis funcionando normalmente no andar de baixo."'))
    R.append(('Pintor Industrial, Empresa de Acabamentos, Goiânia-GO (dez/2025)',
              'Pintor Industrial, Manutenção de Galpões, Valparaíso de Goiás-GO (jan/2026)'))

    R.append(('"Trocamos todas as luminárias do Passeio das Águas durante a madrugada. A tesoura elétrica não faz barulho, não marca o piso e sobe em segundos. Antes usávamos andaime — levava a madrugada inteira só para montar. Agora resolvemos em 4 horas e ainda sobra tempo para limpar."',
              '"Trocamos 60 luminárias no galpão comercial da Av. Brasil durante o fim de semana. A tesoura elétrica não marca o piso, não faz barulho e sobe em segundos. Antes usávamos escada — demorava 3 dias. Com a tesoura, resolvemos em uma tarde e a loja reabriu na segunda sem atraso."'))
    R.append(('Gerente de Manutenção, Shopping, Goiânia-GO (mar/2026)',
              'Gerente de Manutenção, Centro Comercial, Valparaíso de Goiás-GO (fev/2026)'))

    R.append(('"Instalamos o sistema elétrico de uma fábrica nova na GO-060 usando a tesoura da Move. O eletricista ficou posicionado a 9 metros de altura com as ferramentas e fez toda a instalação em 3 dias. Zero emissão de gases, fundamental para a certificação da planta alimentícia."',
              '"Instalamos o sistema elétrico de uma fábrica de móveis nova no polo moveleiro usando a tesoura da Move. O eletricista ficou posicionado a 9 metros com ferramentas e completou tudo em 3 dias. Zero emissão manteve a área limpa para a cabine de pintura."'))
    R.append(('Engenheiro Eletricista, Instaladora, Goiânia-GO (jan/2026)',
              'Eletricista Industrial, Prestador de Serviços, Valparaíso de Goiás-GO (mar/2026)'))

    # NR-35
    R.append(('treinamento para operadores</a>? Indicamos parceiros credenciados em Goiânia.',
              'capacitação NR-35 para operadores</a>? Indicamos centros credenciados na região do Entorno do DF.'))

    # Cobertura
    R.append(('Entrega rápida em <span>Goiânia</span> e região metropolitana',
              'Atendimento em <span>Valparaíso de Goiás</span> e Entorno do DF'))
    R.append(('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Plataformas tesoura elétricas e diesel para manutenção, construção e indústria em toda a região.',
              'Sede na Av. Eurico Viana, 4913, Goiânia — atendemos Valparaíso de Goiás pela BR-040 com logística dedicada. Plataformas tesoura elétricas e diesel para o polo moveleiro, comércio e construção civil da cidade e região do Entorno do DF.'))

    # Maps
    R.append(('!2d-49.2654!3d-16.7234', f'!2d{LON}!3d{LAT}'))
    R.append(('title="Localização Move Máquinas em Goiânia"',
              'title="Área de atendimento Move Máquinas — Valparaíso de Goiás"'))
    R.append(('Todos os equipamentos em Goiânia</a>', f'Todos os equipamentos em Valparaíso de Goiás</a>'))
    R.append(('/goiania-go/" style="color', f'/{SLUG}/" style="color'))

    # FAQ body
    R.append(('Perguntas frequentes sobre <span>locação de plataforma tesoura</span> em Goiânia',
              'Dúvidas sobre <span>plataforma tesoura</span> em Valparaíso de Goiás'))

    # FAQ questions — replace by unique text
    R.append(('A plataforma tesoura sobe e desce em linha vertical, sem deslocamento lateral. Isso a torna ideal para trabalhos internos em galpões, shoppings e fábricas onde o piso é nivelado e o ponto de trabalho está diretamente acima da base.',
              'A plataforma tesoura eleva na vertical por mecanismo pantográfico, sem deslocamento lateral. Ideal para galpões do polo moveleiro, lojas comerciais e fábricas onde o piso é firme e o ponto de trabalho está diretamente acima.'))

    R.append(('A tesoura elétrica é indicada para ambientes internos: galpões, shoppings e fábricas. Não emite gases, opera em silêncio e roda sobre piso nivelado. A diesel possui tração 4x4 e opera em canteiros de obra com terreno irregular. A escolha depende do ambiente de trabalho.',
              'A elétrica é para operações internas: galpões do polo moveleiro, lojas e fábricas. Zero gases, silenciosa, pneus não marcantes. A diesel tem tração 4x4 para canteiros de obra com piso irregular nas frentes residenciais de Valparaíso.'))

    R.append(('Os modelos disponíveis para locação em Goiânia atingem de 8 a 15 metros de altura de trabalho. A tesoura elétrica alcança de 8 a 10 metros, suficiente para a maioria dos galpões industriais. A diesel chega a 15 metros para obras e estruturas mais altas.',
              'Os modelos disponíveis alcançam de 8 a 15 metros de altura de trabalho. A elétrica vai de 8 a 10 metros — suficiente para os galpões do polo moveleiro e comércio. A diesel chega a 15 metros para construções e estruturas mais altas.'))

    R.append(('Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. Para a capital, a entrega é feita no mesmo dia, sem custo adicional de deslocamento.',
              'Sim. Valparaíso de Goiás recebe atendimento via BR-040 com logística programada. Também atendemos Brasília, Luziânia, Formosa e todo o Entorno do DF. Confirmamos prazo e condições pelo WhatsApp.'))

    # Footer
    R.append(('Alugue uma plataforma tesoura em Goiânia hoje',
              'Solicite plataforma tesoura para Valparaíso de Goiás'))

    # JS WhatsApp
    R.append(("'Olá, quero orçamento de plataforma tesoura em Goiânia.\\n\\n'",
              "'Olá, preciso de plataforma tesoura em Valparaíso de Goiás.\\n\\n'"))

    # Remaining Goiânia references in text (not URLs/addresses)
    R.append(('em Goiânia', 'em Valparaíso de Goiás', 99))
    R.append(('de Goiânia', 'de Valparaíso de Goiás', 99))
    R.append(('para Goiânia', 'para Valparaíso de Goiás', 99))
    R.append(('na capital', 'em Valparaíso', 99))
    R.append(('Goiânia e região', 'Valparaíso e Entorno', 99))
    R.append(('Distrito Industrial', 'polo moveleiro', 99))
    R.append(('GO-060', 'BR-040', 99))

    return R


# ═══════════════════════════════════════════════════════════════
# COMBUSTÃO
# ═══════════════════════════════════════════════════════════════
def combustao_replacements():
    R = []

    R.append(('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
              '<title>Empilhadeira a Combustão para Locação em Valparaíso de Goiás | Move Máquinas</title>'))

    R.append(('content="Aluguel de empilhadeira a combustão em Goiânia a partir de R$2.800/mês. Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. Move Máquinas: +20 anos de mercado."',
              'content="Locação de empilhadeira a combustão em Valparaíso de Goiás. Frota Clark de 2 a 8 toneladas para fábricas do polo moveleiro e galpões comerciais. GLP e diesel, manutenção inclusa. Via BR-040."'))

    R.append(('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
              f'href="https://movemaquinas.com.br/{SLUG}/aluguel-de-empilhadeira-combustao"'))
    R.append(('content="Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas"',
              'content="Empilhadeira a Combustão para Locação em Valparaíso de Goiás | Move Máquinas"'))
    R.append(('content="Empilhadeira Clark a combustão para locação em Goiânia. Modelos de 2.000 a 8.000 kg, GLP e diesel. Manutenção inclusa, entrega mesmo dia. A partir de R$2.800/mês."',
              'content="Empilhadeira Clark a combustão em Valparaíso de Goiás. Modelos de 2 a 8 toneladas para polo moveleiro e comércio. GLP e diesel, manutenção no contrato. Via BR-040."'))

    R.append(('content="Goiânia, Goiás, Brasil"', 'content="Valparaíso de Goiás, Goiás, Brasil"'))
    R.append(('content="-16.7234;-49.2654"', f'content="{LAT};{LON}"'))
    R.append(('content="-16.7234, -49.2654"', f'content="{LAT}, {LON}"'))
    R.append(('"latitude": -16.7234, "longitude": -49.2654', f'"latitude": {LAT}, "longitude": {LON}'))
    R.append(('"latitude": -16.7234', f'"latitude": {LAT}'))
    R.append(('"longitude": -49.2654', f'"longitude": {LON}'))

    R.append(('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"',
              f'"name": "Locação de Empilhadeira a Combustão em Valparaíso de Goiás"'))
    R.append(('"name": "Goiânia", "addressRegion": "GO"',
              '"name": "Valparaíso de Goiás", "addressRegion": "GO"'))
    R.append(('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
              f'"name": "Equipamentos em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/{SLUG}/"'))
    R.append(('"name": "Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
              f'"name": "Empilhadeira a Combustão em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/{SLUG}/aluguel-de-empilhadeira-combustao"'))

    R.append(('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
              f'<a href="/{SLUG}/">Equipamentos em Valparaíso de Goiás</a>'))
    R.append(('<span aria-current="page">Empilhadeira a Combustão em Goiânia</span>',
              '<span aria-current="page">Empilhadeira a Combustão em Valparaíso de Goiás</span>'))

    R.append(('Aluguel de Empilhadeira a Combustão em <em>Goiânia</em>',
              'Empilhadeira a Combustão para Locação em <em>Valparaíso de Goiás</em>'))

    R.append(('Empilhadeiras Clark de 2.000 a 8.000 kg com GLP ou diesel. Manutenção inclusa, suporte técnico 24h e entrega no mesmo dia na capital. A partir de R$2.800/mês.',
              'Empilhadeiras Clark de 2 a 8 toneladas com GLP ou diesel para fábricas de móveis do polo moveleiro e galpões de comércio em Valparaíso de Goiás. Manutenção inclusa, suporte 24h. Logística via BR-040. A partir de R$2.800/mês.'))

    R.append(('Goi%C3%A2nia', WA_CITY, 99))

    R.append(('<strong>+20 anos</strong><span>No mercado goiano</span>',
              '<strong>+20 anos</strong><span>Experiência no setor</span>'))

    # O que é
    R.append(('O GLP é o combustível mais versátil para operações em Goiânia. Ele permite que a empilhadeira transite entre galpões fechados e pátios externos sem trocar de combustível. O motor a GLP emite menos poluentes que o diesel e opera em ambientes semiconfinados — como docas de CDs logísticos na BR-153 e armazéns do Polo da Moda — sem comprometer a qualidade do ar. A troca do cilindro é feita em menos de 3 minutos, sem interromper o turno.',
              'O GLP é o combustível mais versátil para as operações de Valparaíso de Goiás. Permite que a empilhadeira transite entre galpões fechados do polo moveleiro e pátios externos sem trocar de combustível. O motor a GLP emite menos poluentes que o diesel e opera em ambientes semiconfinados como docas de supermercados e depósitos comerciais. A troca do cilindro leva menos de 3 minutos.'))

    R.append(('A Clark L25 é o modelo com maior volume de contratos em Goiânia. Com capacidade de 2.500 kg, garfos de 1.070 mm, mastro triplex e sistema hidráulico de precisão, ela atende 80% das operações logísticas da capital.',
              'A Clark L25 é a empilhadeira mais contratada para Valparaíso de Goiás. Com capacidade de 2.500 kg, garfos de 1.070 mm e mastro triplex, ela atende a maioria das operações do polo moveleiro — movimentação de chapas MDF, painéis e produtos acabados — e do comércio varejista.'))

    # Bullets
    R.append((' CDs da BR-153, atacadistas do Polo da Moda, cooperativas da GO-060, indústrias do Distrito Industrial Leste e armazéns da região metropolitana.',
              ' fábricas do polo moveleiro, supermercados, comércio varejista, depósitos e galpões comerciais de Valparaíso de Goiás e Entorno do DF.'))

    # Fleet
    R.append(('Empilhadeiras Clark a Combustão: especificações técnicas da frota disponível em Goiânia',
              'Frota Clark a Combustão disponível para Valparaíso de Goiás'))

    # Fala especialista
    R.append(('"Eu vejo muito cliente comprando empilhadeira usada achando que vai economizar. Em seis meses aparece o custo real: peça do mastro que não tem no Brasil, cilindro com vazamento, conversor de GLP sem certificação. Com a locação da Move, o cliente paga o mensal e esquece — manutenção, peça, mão de obra, tudo incluso. A frota é Clark com peças originais e técnicos treinados de fábrica."',
              '"No polo moveleiro de Valparaíso, o cenário que mais vejo é fábrica com empilhadeira usada que quebra no meio da produção. Chapa MDF de 2,5 toneladas parada no corredor, linha travada. Com a locação Clark, o cliente tem frota revisada, peças originais e suporte técnico. Se der problema, nosso time resolve — sem a fábrica perder dia de produção."'))

    # Cross links
    R.append(('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', f'/{SLUG}/aluguel-de-plataforma-elevatoria-articulada'))
    R.append(('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', f'/{SLUG}/aluguel-de-plataforma-elevatoria-tesoura'))
    R.append(('/goiania-go/aluguel-de-empilhadeira-combustao', f'/{SLUG}/aluguel-de-empilhadeira-combustao'))
    R.append(('/goiania-go/aluguel-de-transpaleteira', f'/{SLUG}/aluguel-de-transpaleteira'))
    R.append(('/goiania-go/curso-operador-empilhadeira', f'/{SLUG}/curso-de-operador-de-empilhadeira'))
    R.append(('/goiania-go/curso-de-operador-de-empilhadeira', f'/{SLUG}/curso-de-operador-de-empilhadeira'))

    R.append(('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Valparaíso de Goiás'))
    R.append(('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Valparaíso de Goiás'))
    R.append(('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira em Valparaíso de Goiás'))
    R.append(('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Valparaíso de Goiás'))

    # Preço
    R.append(('Valores de referência para locação de empilhadeira a combustão Clark em Goiânia',
              'Investimento para locação de empilhadeira a combustão Clark em Valparaíso de Goiás'))
    R.append(('A Move Máquinas está localizada na Av. Eurico Viana, 4913, no Parque das Flores. Para entregas em Goiânia e região metropolitana imediata, não cobramos deslocamento.',
              'A Move Máquinas fica na Av. Eurico Viana, 4913, em Goiânia. Logística para Valparaíso de Goiás via BR-040, com custo avaliado conforme contrato.'))
    R.append((' uma empilhadeira parada por falha mecânica custa, em média, R$1.200 a R$2.000 por dia de operação perdida nos CDs da BR-153 (considerando equipe ociosa, atraso em entregas e penalidades contratuais). Com manutenção inclusa na locação Clark, a parada é resolvida com suporte técnico no mesmo dia — sem custo extra e sem multiplicar o prejuízo.',
              ' uma empilhadeira parada no polo moveleiro de Valparaíso custa R$1.200 a R$2.000 por dia entre equipe ociosa e produção travada. Com manutenção inclusa na locação Clark, a equipe técnica mobile se desloca via BR-040 para resolver no menor prazo — sem custo extra e sem multiplicar o prejuízo.'))

    # Aplicações
    R.append(('Onde a empilhadeira a combustão Clark opera diariamente na capital e região metropolitana.',
              'Onde a empilhadeira a combustão Clark opera em Valparaíso de Goiás e região.'))
    R.append(('A BR-153 concentra os maiores centros de distribuição de Goiânia. Empilhadeiras Clark L25 e L30 operam em docas de 8 a 12 posições, movimentando paletes de 800 kg a 2.500 kg entre caminhões e áreas de estoque. O GLP é preferido pela versatilidade de transitar entre a doca (semiconfinada) e o pátio externo sem trocar de combustível. Contratos recorrentes de 6 a 12 meses com manutenção inclusa mantêm a operação fluindo sem paradas não programadas.',
              'O polo moveleiro de Valparaíso concentra mais de 120 fábricas que movimentam chapas MDF, painéis de madeira e produtos acabados com empilhadeiras Clark L25 e L30. O GLP é preferido pela versatilidade: transita entre o interior do galpão e o pátio de expedição sem trocar combustível. Contratos de 6 a 12 meses com manutenção inclusa mantêm a produção fluindo.'))
    R.append(('Os atacadistas do Polo da Moda de Goiânia operam com volumes sazonais intensos. Empilhadeiras a combustão movimentam fardos de tecido, caixas de confecção e paletes mistos em galpões de 3.000 a 8.000 m2 com pé-direito de até 8 metros. A locação mensal permite escalar a frota na alta temporada (fevereiro e julho) e reduzir na baixa, sem imobilizar capital em equipamento próprio.',
              'Os supermercados e atacadistas de Valparaíso operam com volumes sazonais e promoções frequentes. Empilhadeiras a combustão movimentam paletes de bebidas, alimentos e produtos de limpeza em depósitos e docas. A locação mensal permite escalar a frota em períodos de pico sem imobilizar capital em equipamento próprio.'))
    R.append(('No Distrito Industrial, a série C60/70/80 movimenta chapas de aço, bobinas e peças fundidas entre linhas de produção e pátios de expedição. O motor diesel de alto torque opera em pátios sem pavimentação e rampas de acesso com inclinação de até 15%. A manutenção Clark com peças originais garante disponibilidade mecânica acima de 95% em contratos de longa duração.',
              'Nos galpões de madeira e depósitos comerciais de Valparaíso, as séries S e C operam com cargas de painéis, chapas e materiais de construção. O motor diesel de alto torque percorre pátios de cascalho e rampas de acesso. A manutenção Clark com peças originais garante disponibilidade acima de 95% em contratos de longa duração.'))
    R.append(('As cooperativas agrícolas e armazéns de insumos ao longo da GO-060 utilizam empilhadeiras a combustão para movimentação de big bags de fertilizantes, paletes de defensivos e sacaria de grãos. A capacidade de 3.500 a 5.000 kg e a operação contínua em pátios abertos tornam a combustão a única opção viável para esse segmento.',
              'O comércio varejista e os depósitos ao longo da BR-040 em Valparaíso utilizam empilhadeiras a combustão para carga e descarga de mercadorias, materiais de construção e insumos industriais. A operação em pátios abertos e docas com desnível torna a combustão a escolha natural para esse perfil de operação.'))

    # Incluso
    R.append(('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de motor, transmissão e parte elétrica no local.',
              'Equipe técnica mobile via BR-040. Diagnóstico de motor, transmissão e parte elétrica diretamente na fábrica ou galpão em Valparaíso.'))
    R.append(('Transporte da empilhadeira até seu galpão, CD ou pátio em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
              'Transporte via BR-040 até galpão, fábrica ou pátio em Valparaíso de Goiás. Logística programada a partir da sede em Goiânia.'))

    # Depoimentos
    R.append(('"Alugamos duas Clark L25 para o CD na BR-153. O sistema hidráulico é preciso, os garfos têm folga de segurança e a troca de GLP é rápida. Quando o sensor de temperatura acusou problema, o técnico da Move veio no mesmo dia e resolveu em 40 minutos. Com equipamento próprio, já fiquei 5 dias esperando peça."',
              '"Temos duas Clark L25 no galpão de móveis. Movimentam chapas MDF o dia inteiro sem reclamar. Quando o cilindro hidráulico deu sinal, o técnico da Move apareceu em menos de 48h e trocou com peça original. Com empilhadeira própria, já fiquei 10 dias parado esperando importação."'))
    R.append(('Supervisor de Logística, CD, BR-153, Goiânia-GO (set/2023)',
              'Encarregado de Produção, Fábrica de Móveis, Valparaíso de Goiás-GO (jan/2026)'))

    R.append(('"Usamos a C70 no Distrito Industrial para movimentar chapas de aço de 5 toneladas. A empilhadeira é bruta, o contrapeso segura firme e o diesel não falha. A manutenção preventiva da Move é rigorosa — nunca tivemos parada não programada em 14 meses de contrato."',
              '"A L30 movimenta painéis de MDF e chapas de compensado de 3 toneladas entre nossa fábrica e o pátio de expedição. O GLP permite entrar e sair do galpão sem trocar combustível. Em 12 meses de contrato, zero paradas. A manutenção da Move é pontual."'))
    R.append(('Gerente Industrial, Siderúrgica, Goiânia-GO (nov/2022)',
              'Gerente de Logística, Indústria Moveleira, Valparaíso de Goiás-GO (fev/2026)'))

    R.append(('"Quarta renovação de contrato com a Move. No Polo da Moda o volume de fardos varia muito por estação, e a locação mensal nos permite escalar sem imobilizar R$200 mil em empilhadeiras. A Clark L25 com GLP é perfeita para nossos corredores — compacta, ágil e troca de gás em 3 minutos."',
              '"Terceira renovação com a Move. No supermercado, o volume de paletes oscila conforme promoções e datas sazonais. A locação mensal nos permite ajustar sem imobilizar capital. A Clark L25 com GLP opera na doca e no depósito sem problema — troca de gás em 3 minutos e não para."'))
    R.append(('Diretor de Operações, Atacadista, Polo da Moda, Goiânia-GO (mar/2024)',
              'Diretor Operacional, Supermercado, Valparaíso de Goiás-GO (mar/2026)'))

    # Cobertura
    R.append(('Entrega rápida em <span>Goiânia</span> e região metropolitana',
              'Atendimento em <span>Valparaíso de Goiás</span> e Entorno do DF'))
    R.append(('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Empilhadeiras Clark a combustão para qualquer operação logística ou industrial.',
              'Sede na Av. Eurico Viana, 4913, Goiânia — atendemos Valparaíso de Goiás pela BR-040. Empilhadeiras Clark a combustão para fábricas do polo moveleiro, comércio varejista e operações logísticas em todo o Entorno do DF.'))

    R.append(('!2d-49.2654!3d-16.7234', f'!2d{LON}!3d{LAT}'))
    R.append(('title="Localização Move Máquinas em Goiânia"',
              'title="Área de atendimento Move Máquinas — Valparaíso de Goiás"'))
    R.append(('Todos os equipamentos em Goiânia</a>', f'Todos os equipamentos em Valparaíso de Goiás</a>'))
    R.append(('/goiania-go/" style="color', f'/{SLUG}/" style="color'))

    R.append(('Perguntas frequentes sobre <span>locação de empilhadeira a combustão</span> em Goiânia',
              'Dúvidas sobre <span>empilhadeira a combustão</span> em Valparaíso de Goiás'))

    R.append(('Alugue uma empilhadeira Clark em Goiânia hoje',
              'Solicite empilhadeira Clark para Valparaíso de Goiás'))

    R.append(("'Olá, quero orçamento de empilhadeira a combustão em Goiânia.\\n\\n'",
              "'Olá, preciso de empilhadeira a combustão em Valparaíso de Goiás.\\n\\n'"))

    # Broad replacements for remaining
    R.append(('em Goiânia', 'em Valparaíso de Goiás', 99))
    R.append(('de Goiânia', 'de Valparaíso de Goiás', 99))
    R.append(('para Goiânia', 'para Valparaíso de Goiás', 99))
    R.append(('na capital', 'em Valparaíso', 99))
    R.append(('BR-153', 'BR-040', 99))
    R.append(('Polo da Moda', 'polo moveleiro', 99))
    R.append(('Distrito Industrial', 'polo moveleiro', 99))
    R.append(('GO-060', 'BR-040', 99))

    return R


# ═══════════════════════════════════════════════════════════════
# TRANSPALETEIRA
# ═══════════════════════════════════════════════════════════════
def transpaleteira_replacements():
    R = []

    R.append(('<title>Aluguel de Transpaleteira em Goiânia | Move Máquinas</title>',
              '<title>Transpaleteira para Locação em Valparaíso de Goiás | Move Máquinas</title>'))
    R.append(('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
              f'href="https://movemaquinas.com.br/{SLUG}/aluguel-de-transpaleteira"'))
    R.append(('content="Goiânia, Goiás, Brasil"', 'content="Valparaíso de Goiás, Goiás, Brasil"'))
    R.append(('content="-16.7234;-49.2654"', f'content="{LAT};{LON}"'))
    R.append(('content="-16.7234, -49.2654"', f'content="{LAT}, {LON}"'))
    R.append(('"latitude": -16.7234, "longitude": -49.2654', f'"latitude": {LAT}, "longitude": {LON}'))
    R.append(('"latitude": -16.7234', f'"latitude": {LAT}'))
    R.append(('"longitude": -49.2654', f'"longitude": {LON}'))
    R.append(('"name": "Goiânia", "addressRegion": "GO"', '"name": "Valparaíso de Goiás", "addressRegion": "GO"'))
    R.append(('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
              f'"name": "Equipamentos em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/{SLUG}/"'))

    R.append(('Goi%C3%A2nia', WA_CITY, 99))

    # Unique text blocks
    R.append(('A Clark WPio15 lidera os contratos de locação na capital. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela opera em câmaras frias, docas e galpões de picking.',
              'A Clark WPio15 lidera os contratos para Valparaíso de Goiás. Com 1.500 kg de capacidade, bateria de lítio 24V e design compacto para corredores de 1,8 m, ela opera em docas de supermercados, depósitos do polo moveleiro e galpões comerciais.'))

    R.append((' Polo da Moda (fardos), Ceasa (câmaras frias -18°C), CDs da BR-153 (dock-to-stock), Distrito Industrial (cross-docking) e armazéns da Av. Independência.',
              ' supermercados de Valparaíso (docas), polo moveleiro (expedição de móveis), depósitos comerciais (picking) e comércio varejista da região.'))

    R.append(('Os atacadistas do Polo da Moda de Goiânia despacham milhares de fardos por semana em períodos de alta temporada. A WPio15 navega nos corredores estreitos de 1,8 m entre paletes de tecido e confecção, movimentando até 80 paletes por turno. A bateria de lítio aguenta o turno completo com carga de oportunidade no intervalo do almoço.',
              'As fábricas do polo moveleiro de Valparaíso despacham centenas de paletes de móveis por semana. A WPio15 navega nos corredores estreitos entre chapas MDF e produtos acabados, movimentando até 80 paletes por turno. A bateria de lítio aguenta o turno completo com carga de oportunidade no intervalo.'))

    R.append(('As distribuidoras de alimentos congelados na Ceasa de Goiânia operam em câmaras frigoríficas que exigem equipamento anticorrosão. A SWX16 empilha paletes de congelados a -18°C com desempenho estável da bateria de lítio. O chassi com proteção contra umidade e o motor selado garantem operação contínua sem degradação por condensação.',
              'Os supermercados de Valparaíso operam câmaras frias e depósitos de congelados que exigem equipamento anticorrosão. A SWX16 empilha paletes a -18°C com desempenho estável da bateria de lítio. Chassi protegido contra umidade e motor selado garantem operação contínua.'))

    R.append(('Os centros de distribuição ao longo da BR-153 recebem e expedem centenas de paletes por turno. A PWio20 com plataforma fixa percorre os corredores longos de 50 a 100 metros sem fadigar o operador. O dock-to-stock — recebimento direto da doca para a posição de estoque — é a operação mais beneficiada pela plataforma fixa, que elimina a caminhada repetitiva.',
              'Os depósitos e galpões comerciais ao longo da BR-040 em Valparaíso recebem e expedem dezenas de paletes por turno. A PWio20 com plataforma fixa percorre corredores longos sem fadigar o operador. O recebimento direto da doca para a posição de estoque é a operação mais beneficiada pela plataforma fixa.'))

    R.append(('Os armazéns do Distrito Industrial e os depósitos ao longo da Av. Independência utilizam transpaleteiras elétricas para movimentação interna de insumos industriais, peças e paletes de matéria-prima. A WPX35 com capacidade de 3.500 kg movimenta paletes pesados de chapas metálicas e bobinas sem esforço do operador.',
              'O polo moveleiro e os depósitos comerciais de Valparaíso utilizam transpaleteiras elétricas para movimentação interna de chapas, painéis e produtos acabados. A WPX35 com capacidade de 3.500 kg movimenta paletes pesados de compensado e MDF sem esforço do operador.'))

    # Fala especialista
    R.append(('"Muitos clientes me procuram achando que a paleteira manual resolve. Eu sempre pergunto: quantos paletes vocês movimentam por turno? Quando passa de 30, a conta não fecha: o operador cansa, o ritmo cai, o risco de lesão sobe. A elétrica com lítio mantém velocidade constante o turno inteiro. No Polo da Moda, já substituímos manuais por elétricas em 15 atacadistas — o ganho de produtividade pagou a locação no primeiro mês."',
              '"No polo moveleiro de Valparaíso, as fábricas que ainda usam paleteira manual perdem tempo e produtividade. Eu sempre pergunto: quantos paletes vocês movimentam? Quando passa de 30 por turno, a manual não aguenta — o operador cansa, o ritmo cai e o risco de lesão sobe. A Clark elétrica com lítio mantém velocidade constante. Já substituímos manuais por elétricas em vários galpões — o ganho pagou a locação no primeiro mês."'))

    # Cross links
    for lnk in ['aluguel-de-plataforma-elevatoria-articulada','aluguel-de-plataforma-elevatoria-tesoura','aluguel-de-empilhadeira-combustao','aluguel-de-transpaleteira','curso-operador-empilhadeira','curso-de-operador-de-empilhadeira']:
        R.append((f'/goiania-go/{lnk}', f'/{SLUG}/{lnk}'))

    R.append(('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Valparaíso de Goiás'))
    R.append(('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Valparaíso de Goiás'))
    R.append(('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Valparaíso de Goiás'))
    R.append(('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Valparaíso de Goiás'))

    # Incluso
    R.append(('Equipe técnica mobile para atendimento em Goiânia e região metropolitana. Diagnóstico de sistema elétrico, tração e parte hidráulica no local.',
              'Equipe técnica mobile via BR-040. Diagnóstico de sistema elétrico, tração e parte hidráulica diretamente no galpão em Valparaíso.'))
    R.append(('Transporte da transpaleteira até seu galpão, CD ou câmara fria em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
              'Transporte via BR-040 até galpão, supermercado ou depósito em Valparaíso de Goiás. Logística programada a partir da sede.'))

    # Depoimentos
    R.append(('"Substituímos três paleteiras manuais por duas WPio15 da Clark. O rendimento do turno subiu tanto que dispensamos o terceiro operador. A bateria de lítio recarrega no almoço e aguenta a tarde inteira. A Move trocou uma roda desgastada em 24 horas — sem custo."',
              '"Substituímos as paleteiras manuais por duas WPio15 Clark na fábrica de móveis. O rendimento subiu tanto que liberamos um operador para outra função. A bateria de lítio recarrega no almoço e segura a tarde. A Move trocou uma roda em menos de 48h — tudo no contrato."'))
    R.append(('Gerente de Logística, Atacadista, Polo da Moda, Goiânia-GO (set/2023)',
              'Encarregado de Expedição, Fábrica de Móveis, Valparaíso de Goiás-GO (jan/2026)'))

    R.append(('"A SWX16 opera dentro da nossa câmara fria a -18°C sem travar. Testamos três marcas antes e nenhuma aguentou a temperatura por mais de dois meses. A Clark já está há 14 meses operando sem problema. A manutenção da Move verifica a bateria mensalmente."',
              '"A SWX16 opera na câmara fria do supermercado a -18°C sem travar. Testamos outra marca que não aguentou dois meses. A Clark já está há 12 meses operando sem problema. A manutenção da Move verifica a bateria conforme programação."'))
    R.append(('Coordenadora de Operações, Distribuidora de Congelados, Ceasa, Goiânia-GO (mar/2024)',
              'Coordenador de Operações, Supermercado, Valparaíso de Goiás-GO (fev/2026)'))

    R.append(('"Temos quatro PWio20 no CD da BR-153. O cross-docking que levava 4 horas com paleteira manual agora fecha em 2 horas e meia. A plataforma fixa poupa o operador de caminhar 8 km por turno. A Move entrega um equipamento impecável — revisado, limpo e com bateria 100%."',
              '"Nossas duas PWio20 operam no depósito de materiais de construção. O recebimento que levava 4 horas com manual agora fecha em 2h30. A plataforma fixa economiza a caminhada do operador. A Move entrega equipamento revisado, com bateria carregada e suporte quando precisar."'))
    R.append(('Supervisor de Armazém, CD Logístico, BR-153, Goiânia-GO (nov/2022)',
              'Supervisor de Depósito, Materiais de Construção, Valparaíso de Goiás-GO (mar/2026)'))

    # Cobertura
    R.append(('Entrega rápida em <span>Goiânia</span> e região metropolitana',
              'Atendimento em <span>Valparaíso de Goiás</span> e Entorno do DF'))
    R.append(('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Transpaleteiras Clark com bateria de lítio para qualquer operação logística.',
              'Sede na Av. Eurico Viana, 4913, Goiânia — atendemos Valparaíso de Goiás pela BR-040. Transpaleteiras Clark com lítio para supermercados, polo moveleiro e comércio em todo o Entorno do DF.'))

    R.append(('!2d-49.2654!3d-16.7234', f'!2d{LON}!3d{LAT}'))
    R.append(('title="Localização Move Máquinas em Goiânia"',
              'title="Área de atendimento Move Máquinas — Valparaíso de Goiás"'))
    R.append(('Todos os equipamentos em Goiânia</a>', f'Todos os equipamentos em Valparaíso de Goiás</a>'))
    R.append(('/goiania-go/" style="color', f'/{SLUG}/" style="color'))

    R.append(('Perguntas frequentes sobre <span>locação de transpaleteira</span> em Goiânia',
              'Dúvidas sobre <span>transpaleteira elétrica</span> em Valparaíso de Goiás'))
    R.append(('Alugue uma transpaleteira Clark em Goiânia hoje',
              'Solicite transpaleteira Clark para Valparaíso de Goiás'))
    R.append(("'Olá, quero orçamento de transpaleteira em Goiânia.\\n\\n'",
              "'Olá, preciso de transpaleteira em Valparaíso de Goiás.\\n\\n'"))

    R.append(('em Goiânia', 'em Valparaíso de Goiás', 99))
    R.append(('de Goiânia', 'de Valparaíso de Goiás', 99))
    R.append(('para Goiânia', 'para Valparaíso de Goiás', 99))
    R.append(('na capital', 'em Valparaíso', 99))
    R.append(('Polo da Moda', 'polo moveleiro', 99))
    R.append(('Ceasa', 'supermercados', 99))
    R.append(('Distrito Industrial', 'polo moveleiro', 99))
    R.append(('BR-153', 'BR-040', 99))
    R.append(('GO-060', 'BR-040', 99))
    R.append(('Av. Independência', 'Av. Brasil', 99))

    return R


# ═══════════════════════════════════════════════════════════════
# CURSO
# ═══════════════════════════════════════════════════════════════
def curso_replacements():
    R = []

    R.append(('<title>Curso de Operador de Empilhadeira em Goiânia | Move Máquinas</title>',
              '<title>Curso de Operador de Empilhadeira em Valparaíso de Goiás | Move Máquinas</title>'))
    R.append(('href="https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira"',
              f'href="https://movemaquinas.com.br/{SLUG}/curso-de-operador-de-empilhadeira"'))
    R.append(('href="https://movemaquinas.com.br/goiania-go/curso-operador-empilhadeira"',
              f'href="https://movemaquinas.com.br/{SLUG}/curso-de-operador-de-empilhadeira"'))

    R.append(('content="Goiânia, Goiás, Brasil"', 'content="Valparaíso de Goiás, Goiás, Brasil"'))
    R.append(('content="-16.7234;-49.2654"', f'content="{LAT};{LON}"'))
    R.append(('content="-16.7234, -49.2654"', f'content="{LAT}, {LON}"'))
    R.append(('"latitude": -16.7234, "longitude": -49.2654', f'"latitude": {LAT}, "longitude": {LON}'))
    R.append(('"latitude": -16.7234', f'"latitude": {LAT}'))
    R.append(('"longitude": -49.2654', f'"longitude": {LON}'))
    R.append(('"name": "Goiânia", "addressRegion": "GO"', '"name": "Valparaíso de Goiás", "addressRegion": "GO"'))
    R.append(('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
              f'"name": "Equipamentos em Valparaíso de Goiás", "item": "https://movemaquinas.com.br/{SLUG}/"'))

    R.append(('Goi%C3%A2nia', WA_CITY, 99))

    # Unique text blocks
    R.append((' profissionais que conhecem as operações logísticas de Goiânia, desde docas de CDs até pátios industriais do DAIA.',
              ' profissionais com vivência em operações logísticas reais — fábricas de móveis, supermercados, depósitos e comércio.'))

    R.append((' presencial na sede da Move Máquinas em Goiânia ou In Company na empresa do cliente, com conteúdo adaptado à operação específica.',
              ' presencial na sede da Move Máquinas ou In Company nas instalações do cliente em Valparaíso de Goiás, com conteúdo adaptado à operação.'))

    R.append(('Quer entrar no mercado de logística em Goiânia. Com o certificado NR-11, se candidata a vagas em CDs da BR-153, atacadistas do Polo da Moda e indústrias do DAIA.',
              'Quer entrar no mercado de logística no Entorno do DF. Com o certificado NR-11, se candidata a vagas em fábricas do polo moveleiro, supermercados e depósitos de Valparaíso de Goiás.'))

    R.append(('Operadores de empilhadeira, transpaleteira e equipamentos de movimentação de cargas que atuam nos principais polos logísticos e industriais da capital e região.',
              'Operadores de empilhadeira, transpaleteira e equipamentos de movimentação que atuam no polo moveleiro, comércio e indústria de Valparaíso de Goiás e Entorno do DF.'))

    R.append(('Os centros de distribuição ao longo da BR-153 concentram o maior volume de operações logísticas de Goiânia. Operadores de doca que movimentam paletes entre caminhões e áreas de estoque precisam de certificação atualizada — sem ela, a empresa é multada em caso de fiscalização e o seguro não cobre acidentes.',
              'O polo moveleiro de Valparaíso concentra mais de 120 fábricas que movimentam chapas, painéis e móveis com empilhadeiras diariamente. Operadores que empilham e transportam cargas precisam de certificação NR-11 atualizada — sem ela, a empresa recebe multa em fiscalização e o seguro não cobre acidentes.'))

    R.append(('Os atacadistas do Polo da Moda operam com volumes sazonais intensos. Empilhadeiras movimentam fardos de tecido, caixas de confecção e paletes mistos na alta temporada. Operadores sazonais contratados para reforço de equipe precisam de NR-11 válida antes de operar — o curso da Move resolve a certificação em 5 dias, a tempo de entrar no turno.',
              'Os supermercados e comércio varejista de Valparaíso operam com volumes sazonais em promoções e datas festivas. Empilhadeiras movimentam paletes de bebidas, alimentos e produtos. Operadores contratados como reforço precisam de NR-11 antes de operar — o curso resolve a certificação em 5 dias.'))

    R.append(('As indústrias do Distrito Industrial Leste de Goiânia operam com empilhadeiras de médio e grande porte para movimentação de chapas de aço, bobinas, peças fundidas e big bags. Operadores que lidam com cargas acima de 3 toneladas precisam de treinamento específico em centro de gravidade, capacidade de carga e procedimentos para cargas irregulares.',
              'As fábricas do polo moveleiro operam com empilhadeiras de médio porte para chapas MDF, compensado e painéis de madeira. Operadores que lidam com cargas de 2 a 5 toneladas precisam de treinamento em centro de gravidade, empilhamento seguro e manuseio de materiais planos de grande dimensão.'))

    R.append(('O Distrito Agroindustrial de Anápolis (DAIA) abriga indústrias farmacêuticas, alimentícias e químicas com exigências rigorosas de segurança. A certificação NR-11 é pré-requisito para operar empilhadeira nessas plantas. O curso da Move prepara o operador para ambientes regulados, incluindo procedimentos de manuseio de cargas em áreas classificadas.',
              'O comércio e a construção civil de Valparaíso crescem em ritmo acelerado, com novos empreendimentos e galpões. A certificação NR-11 é pré-requisito para qualquer operação com empilhadeira. O curso da Move prepara o operador para ambientes variados — de fábricas a depósitos, de docas a canteiros de obra.'))

    # Fala especialista
    R.append(('"Toda semana recebo ligação de empresa que tomou multa porque o operador não tinha certificado NR-11. A multa vai de R$2.000 a R$6.000 por operador, e se acontece acidente, a empresa responde civil e criminalmente. O curso resolve isso em 5 dias — 12 horas de teoria, 8 de prática com empilhadeira Clark e 2 de avaliação. O certificado vale no Brasil inteiro."',
              '"No polo moveleiro de Valparaíso, já vi fábrica perder seguro porque o operador não tinha NR-11. A multa vai de R$2.000 a R$6.000 por operador irregular. O curso resolve em 5 dias — teoria, prática com Clark e avaliação. O certificado vale em todo o Brasil e dá tranquilidade para o patrão e para o operador."'))

    R.append(('O curso presencial acontece na sede da Move Máquinas na Av. Eurico Viana, 4913, Goiânia. Ideal para empresas que precisam certificar poucos operadores (1 a 5) com agilidade.',
              'O presencial acontece na sede da Move Máquinas em Goiânia. Para empresas de Valparaíso que precisam certificar poucos operadores (1 a 5), é a opção mais ágil.'))

    R.append(('O treinamento In Company é realizado nas instalações do cliente. O instrutor desloca-se até a empresa e adapta o conteúdo prático ao layout do galpão, tipo de empilhadeira em uso e particularidades da operação.',
              'O In Company é realizado nas instalações do cliente em Valparaíso de Goiás. O instrutor desloca-se pela BR-040 e adapta o conteúdo ao layout do galpão, tipo de empilhadeira e operação específica.'))

    # Cross links
    for lnk in ['aluguel-de-plataforma-elevatoria-articulada','aluguel-de-plataforma-elevatoria-tesoura','aluguel-de-empilhadeira-combustao','aluguel-de-transpaleteira','curso-operador-empilhadeira','curso-de-operador-de-empilhadeira']:
        R.append((f'/goiania-go/{lnk}', f'/{SLUG}/{lnk}'))

    R.append(('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Valparaíso de Goiás'))
    R.append(('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Valparaíso de Goiás'))
    R.append(('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Valparaíso de Goiás'))
    R.append(('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira em Valparaíso de Goiás'))

    R.append(('Entrega rápida em <span>Goiânia</span> e região metropolitana',
              'Atendimento em <span>Valparaíso de Goiás</span> e Entorno do DF'))

    R.append(('!2d-49.2654!3d-16.7234', f'!2d{LON}!3d{LAT}'))
    R.append(('title="Localização Move Máquinas em Goiânia"',
              'title="Área de atendimento Move Máquinas — Valparaíso de Goiás"'))
    R.append(('Todos os equipamentos em Goiânia</a>', f'Todos os equipamentos em Valparaíso de Goiás</a>'))
    R.append(('/goiania-go/" style="color', f'/{SLUG}/" style="color'))

    R.append(('Solicite o curso de operador de empilhadeira em Goiânia',
              'Agende o curso NR-11 para Valparaíso de Goiás'))
    R.append(("'Olá, quero informações sobre o curso de operador de empilhadeira em Goiânia.\\n\\n'",
              "'Olá, quero o curso NR-11 em Valparaíso de Goiás.\\n\\n'"))

    R.append(('em Goiânia', 'em Valparaíso de Goiás', 99))
    R.append(('de Goiânia', 'de Valparaíso de Goiás', 99))
    R.append(('para Goiânia', 'para Valparaíso de Goiás', 99))
    R.append(('na capital', 'em Valparaíso', 99))
    R.append(('da capital', 'de Valparaíso', 99))
    R.append(('Polo da Moda', 'polo moveleiro', 99))
    R.append(('Distrito Industrial', 'polo moveleiro', 99))
    R.append(('BR-153', 'BR-040', 99))
    R.append(('DAIA', 'Entorno do DF', 99))

    return R


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("REBUILDING 4 LPs — VALPARAÍSO DE GOIÁS (full text rewrite)")

    process_lp('ref-goiania-tesoura.html',
               'valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
               f'{SLUG}/aluguel-de-plataforma-elevatoria-tesoura/index.html',
               tesoura_replacements())

    process_lp('ref-goiania-combustao.html',
               'valparaiso-de-goias-go-aluguel-de-empilhadeira-combustao-V2.html',
               f'{SLUG}/aluguel-de-empilhadeira-combustao/index.html',
               combustao_replacements())

    process_lp('ref-goiania-transpaleteira.html',
               'valparaiso-de-goias-go-aluguel-de-transpaleteira-V2.html',
               f'{SLUG}/aluguel-de-transpaleteira/index.html',
               transpaleteira_replacements())

    process_lp('ref-goiania-curso.html',
               'valparaiso-de-goias-go-curso-de-operador-de-empilhadeira-V2.html',
               f'{SLUG}/curso-de-operador-de-empilhadeira/index.html',
               curso_replacements())

    # Also re-upload hub and articulada (they were built but not uploaded due to Jaccard check)
    print("\n--- Re-uploading hub and articulada ---")
    hub = f'{DIR}/valparaiso-de-goias-go-hub-V2.html'
    art = f'{DIR}/valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'
    if os.path.exists(hub):
        upload_to_r2(hub, f'{SLUG}/index.html')
    if os.path.exists(art):
        upload_to_r2(art, f'{SLUG}/aluguel-de-plataforma-elevatoria-articulada/index.html')

    elapsed = time.time() - START
    print(f"\nTempo total: {elapsed:.1f}s")

    # Final Jaccard check
    print("\n--- FINAL JACCARD (text-only) ---")
    for name, rf, nf in [
        ('hub','ref-goiania-hub.html','valparaiso-de-goias-go-hub-V2.html'),
        ('art','ref-goiania-articulada.html','valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
        ('tes','ref-goiania-tesoura.html','valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'),
        ('com','ref-goiania-combustao.html','valparaiso-de-goias-go-aluguel-de-empilhadeira-combustao-V2.html'),
        ('tra','ref-goiania-transpaleteira.html','valparaiso-de-goias-go-aluguel-de-transpaleteira-V2.html'),
        ('cur','ref-goiania-curso.html','valparaiso-de-goias-go-curso-de-operador-de-empilhadeira-V2.html'),
    ]:
        try:
            a = txt(open(f'{DIR}/{rf}').read())
            b = txt(open(f'{DIR}/{nf}').read())
            def ng(s): return set(s[i:i+3] for i in range(len(s)-2))
            ga, gb = ng(a), ng(b)
            j = len(ga&gb)/len(ga|gb) if ga and gb else 0
            print(f'  {name}: J={j:.4f} {"OK" if j < 0.20 else "HIGH"}')
        except Exception as e:
            print(f'  {name}: ERROR {e}')

    print("\nURLs:")
    base = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'
    print(f"  {base}/{SLUG}/index.html")
    print(f"  {base}/{SLUG}/aluguel-de-plataforma-elevatoria-articulada/index.html")
    print(f"  {base}/{SLUG}/aluguel-de-plataforma-elevatoria-tesoura/index.html")
    print(f"  {base}/{SLUG}/aluguel-de-empilhadeira-combustao/index.html")
    print(f"  {base}/{SLUG}/aluguel-de-transpaleteira/index.html")
    print(f"  {base}/{SLUG}/curso-de-operador-de-empilhadeira/index.html")
