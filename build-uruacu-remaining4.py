#!/usr/bin/env python3
"""
build-uruacu-remaining4.py
Gera 4 LPs de Uruaçu: tesoura, combustão, transpaleteira, curso.
Abordagem: lê cada ref, faz find-replace EXATO baseado no conteúdo real,
reescreve todo o texto para contexto de Uruaçu.
"""
import time, re, os, boto3

START = time.time()
BASE = '/Users/jrios/move-maquinas-seo'

r2 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto')

def text_only(h):
    h2 = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h2 = re.sub(r'<script[^>]*>.*?</script>', '', h2, flags=re.DOTALL)
    h2 = re.sub(r'<select[^>]*>.*?</select>', '', h2, flags=re.DOTALL)
    h2 = re.sub(r'<[^>]+>', ' ', h2)
    return re.sub(r'\s+', ' ', h2).strip().lower()

def ngrams(text, n=3):
    words = text.split()
    return set(tuple(words[i:i+n]) for i in range(len(words)-n+1))

def jaccard(a, b):
    if not a or not b: return 0
    return len(a & b) / len(a | b)

results = []

def process_page(ref_file, out_file, r2_key, label, replacements_fn):
    """Generic processor: read ref, apply replacements, verify, upload."""
    t0 = time.time()
    ref_path = os.path.join(BASE, ref_file)
    out_path = os.path.join(BASE, out_file)

    with open(ref_path, 'r', encoding='utf-8') as f:
        html = f.read()

    miss = [0]
    def r(old, new, count=1):
        nonlocal html
        if old not in html:
            miss[0] += 1
            if miss[0] <= 5:
                print(f"  !! MISS: {old[:70]}...")
            return
        html = html.replace(old, new, count)

    # Apply page-specific replacements
    replacements_fn(r)

    # Common geo/coords
    r('content="Goiânia, Goiás, Brasil"', 'content="Uruaçu, Goiás, Brasil"')
    r('content="-16.7234;-49.2654"', 'content="-14.5237;-49.1407"')
    r('content="-16.7234, -49.2654"', 'content="-14.5237, -49.1407"')
    r('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -14.5237, "longitude": -49.1407')
    r('"latitude": -16.7234', '"latitude": -14.5237')
    r('"longitude": -49.2654', '"longitude": -49.1407')
    r('"name": "Goiânia", "addressRegion": "GO"', '"name": "Uruaçu", "addressRegion": "GO"')
    r('Goi%C3%A2nia', 'Urua%C3%A7u', 99)
    r('!2d-49.2654!3d-16.7234', '!2d-49.1407!3d-14.5237')

    # Form selects
    r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''',
      '''              <option value="Uruaçu" selected>Uruaçu</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Senador Canedo">Senador Canedo</option>''', 2)

    # Internal links slug
    r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/uruacu-go/aluguel-de-plataforma-elevatoria-articulada')
    r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura')
    r('/goiania-go/aluguel-de-empilhadeira-combustao', '/uruacu-go/aluguel-de-empilhadeira-combustao')
    r('/goiania-go/aluguel-de-transpaleteira', '/uruacu-go/aluguel-de-transpaleteira')
    r('/goiania-go/curso-operador-empilhadeira', '/uruacu-go/curso-de-operador-de-empilhadeira')
    r('/goiania-go/curso-de-operador-de-empilhadeira', '/uruacu-go/curso-de-operador-de-empilhadeira')
    r('/goiania-go/" style="color', '/uruacu-go/" style="color')
    r('/goiania-go/">', '/uruacu-go/">')

    # Verify
    ref_html = open(ref_path).read()
    lines = html.split('\n')
    issues = []
    for i, line in enumerate(lines):
        if 'Goiânia' in line or ('goiania-go' in line and '/goiania-go/' not in line):
            leg = any(kw in line for kw in [
                'addressLocality', 'Parque das Flores', 'Eurico Viana',
                'CNPJ', 'option value', 'goiania-go/',
                '280 km', 'sede', 'Goiânia</a>', 'Goiânia)',
                'Aparecida de Goiânia',
            ])
            if not leg:
                issues.append((i+1, line.strip()[:120]))

    ng_ref = ngrams(text_only(ref_html))
    ng_new = ngrams(text_only(html))
    j_ref = jaccard(ng_ref, ng_new)

    print(f"\n{'='*60}")
    print(f"{label}")
    print(f"{'='*60}")
    print(f"Misses: {miss[0]}")
    print(f"Goiania issues: {len(issues)}")
    for ln, txt in issues[:5]:
        print(f"  L{ln}: {txt}")
    print(f"JACCARD vs REF: {j_ref:.4f}")

    # vs SC/BSB
    for prefix, lbl in [('senador-canedo-go', 'SC'), ('brasilia-df', 'BSB')]:
        comp = out_file.replace('uruacu-go', prefix)
        comp_path = os.path.join(BASE, comp)
        if os.path.exists(comp_path):
            ng_c = ngrams(text_only(open(comp_path).read()))
            print(f"JACCARD vs {lbl}: {jaccard(ng_c, ng_new):.4f}")

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    r2.put_object(Bucket='pages', Key=r2_key, Body=html.encode('utf-8'),
                  ContentType='text/html; charset=utf-8')
    url = f'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{r2_key}'
    elapsed = time.time() - t0
    print(f"Salvo + Upload OK: {url}")
    print(f"TEMPO: {elapsed:.1f}s")
    results.append({'page': label, 'j_ref': j_ref, 'url': url})


# ═══════════════════════════════════════════════════════════════════
# TESOURA
# ═══════════════════════════════════════════════════════════════════
def tesoura_replacements(r):
    # Title & meta
    r('<title>Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas</title>',
      '<title>Plataforma Tesoura para Locação em Uruaçu-GO | Move Máquinas</title>')
    r('content="Aluguel de plataforma elevatória tesoura em Goiânia: modelos elétricos de 8 a 10 m e diesel de 12 a 15 m. Manutenção inclusa, entrega no mesmo dia. Move Máquinas: +20 anos no mercado goiano."',
      'content="Locação de plataforma tesoura 8 a 15m em Uruaçu-GO. Elevação vertical estável para galpões do Distrito Agroindustrial, frigoríficos e armazéns de grãos. Manutenção inclusa, entrega via BR-153."')
    r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
      'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura"')
    r('content="Aluguel de Plataforma Elevatória Tesoura em Goiânia | Move Máquinas"',
      'content="Plataforma Tesoura para Locação em Uruaçu-GO | Move Máquinas"')
    r('content="Plataforma tesoura para locação em Goiânia. Modelos elétricos e diesel de 8 a 15 m. Manutenção inclusa, entrega mesmo dia. Ideal para galpões, shoppings e fábricas."',
      'content="Plataforma tesoura 8 a 15m em Uruaçu. Elevação vertical para galpões do Distrito Agroindustrial, frigoríficos e cooperativas. Manutenção inclusa."')

    # Schema
    r('"name": "Aluguel de Plataforma Elevatória Tesoura em Goiânia"',
      '"name": "Locação de Plataforma Tesoura em Uruaçu"')
    r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
      '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
    r('"name": "Plataforma Tesoura em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura"',
      '"name": "Plataforma Tesoura em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-plataforma-elevatoria-tesoura"')

    # Schema FAQ answers — replace Goiânia mentions
    r('locação em Goiânia atingem de 8 a 15 metros', 'locação em Uruaçu atingem de 8 a 15 metros')
    r('indicar parceiros credenciados em Goiânia para o curso', 'conectar sua equipe a instrutores credenciados')
    r('nossa equipe técnica atende em Goiânia e região no mesmo dia', 'nossa equipe técnica se desloca pela BR-153 para atendimento')
    r('"Vocês entregam plataforma tesoura fora de Goiânia?"', '"Qual o prazo de entrega da tesoura em Uruaçu?"')
    r('Sim. Atendemos em um raio de até 200 km de Goiânia, cobrindo Aparecida de Goiânia, Senador Canedo, Trindade, Anápolis, Inhumas e toda a região metropolitana. A entrega na capital é feita no mesmo dia, sem custo adicional de deslocamento.', 'Uruaçu está a 280 km da sede pela BR-153. A entrega é programada em 24-48h após confirmação. Para contratos acima de 3 meses, o frete está incluso no valor mensal.')
    r('montar andaime ou scaffolding em Goiânia', 'montar andaime no Distrito Agroindustrial de Uruaçu')
    r('galpão de 10 metros no Distrito Industrial de Goiânia', 'galpão de 10 metros no Distrito Agroindustrial de Uruaçu')
    r('reformas em shopping centers de Goiânia', 'manutenção em frigoríficos e armazéns de Uruaçu')

    # Breadcrumb
    r('<a href="/goiania-go/">Equipamentos em Goiânia</a>',
      '<a href="/uruacu-go/">Equipamentos em Uruaçu</a>')
    r('<span aria-current="page">Plataforma Tesoura em Goiânia</span>',
      '<span aria-current="page">Plataforma Tesoura em Uruaçu</span>')

    # Hero
    r('Plataformas prontas para entrega em Goiânia',
      'Plataformas disponíveis para Uruaçu')
    r('Aluguel de Plataforma Elevatória Tesoura em <em>Goiânia</em>',
      'Locação de Plataforma Tesoura em <em>Uruaçu</em>')

    # Trust bar
    r('Atendimento em Goiânia', 'Atendimento via BR-153')

    # Body text — broad replacements
    r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
    r('galpões do Distrito Industrial de Goiânia', 'galpões do Distrito Agroindustrial de Uruaçu')
    r('em Goiânia e região metropolitana', 'em Uruaçu com agendamento')
    r('Entrega no mesmo dia em Goiânia', 'Entrega programada via BR-153')
    r('Entrega em Goiânia no mesmo dia', 'Entrega programada em Uruaçu')
    r('Shoppings de Goiânia', 'Frigoríficos e laticínios de Uruaçu')
    r('shoppings Flamboyant e Passeio das Águas', 'frigoríficos de aves e cooperativas de grãos')
    r('fábricas da GO-060', 'metalúrgicas do Distrito Agroindustrial')
    r('obras civis na região metropolitana', 'armazéns de grãos ao longo da BR-153')
    r('Aparecida de Goiânia, Senador Canedo e Trindade', 'norte goiano')

    # Applications section
    r('Aplicações em Goiânia', 'Aplicações agroindustriais')
    r('tesoura elétrica</span> em Goiânia', 'tesoura elétrica</span> em Uruaçu')
    r('galpão industrial no Distrito Industrial de Goiânia', 'galpão no Distrito Agroindustrial de Uruaçu')
    r('Os galpões do Distrito Industrial de Goiânia', 'Os galpões do Distrito Agroindustrial de Uruaçu')
    r('Estrutura elétrica industrial com painéis e cabeamento, ambiente de fábrica na GO-060 em Goiânia', 'Metalúrgica e fábrica de ração no Distrito Agroindustrial de Uruaçu')
    r('Canteiro de obras com estrutura metálica em construção civil na região metropolitana de Goiânia', 'Armazém de grãos e silo ao longo da BR-153 em Uruaçu')
    r('condomínios de Aparecida de Goiânia, Senador Canedo e Trindade', 'expansões do Distrito Agroindustrial e construções em Uruaçu')

    # Incluso
    r('Equipe técnica em Goiânia para diagnóstico', 'Equipe técnica com deslocamento pela BR-153 para diagnóstico')
    r('Transporte da plataforma até seu galpão, shopping ou canteiro em Goiânia e região. Entrega no mesmo dia para a capital, sem custo de deslocamento.',
      'Transporte da plataforma até seu galpão, frigorífico ou armazém em Uruaçu. Entrega programada em 24-48h. Frete incluso para contratos acima de 3 meses.')

    # Depoimentos
    r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
    r('Goiânia-GO (jan/2026)', 'Uruaçu-GO (jan/2026)')
    r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
    r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')

    # NR-35
    r('parceiros credenciados em Goiânia', 'centros credenciados na região')

    # Price/comparison
    r('Regra prática para projetos em Goiânia:', 'Critério objetivo para operações em Uruaçu:')
    r('locação em Goiânia:', 'locação em Uruaçu:')
    r('locação de plataforma tesoura em Goiânia', 'locação de plataforma tesoura em Uruaçu')
    r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis para Uruaçu:')
    r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
    r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
    r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')

    # Video
    r('aluguel de plataforma tesoura em Goiânia', 'locação de plataforma tesoura em Uruaçu')
    r('Aluguel de Plataforma Tesoura</span> em Goiânia', 'Locação de Plataforma Tesoura</span> em Uruaçu')

    # Coverage
    r('Entrega rápida em <span>Goiânia</span> e região metropolitana', 'Entrega programada em <span>Uruaçu</span> e norte goiano')
    r('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital. Atendemos toda a região metropolitana e cidades em um raio de até 200 km. Plataformas tesoura elétricas e diesel para galpões, shoppings, fábricas e canteiros de obra.',
      'Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153. Entrega programada em 24-48h. Plataformas tesoura elétricas e diesel para galpões, frigoríficos, armazéns e o Distrito Agroindustrial.')
    r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')

    # FAQ visible
    r('locação de plataforma tesoura</span> em Goiânia', 'locação de plataforma tesoura</span> em Uruaçu')

    # Footer
    r('plataforma tesoura em Goiânia hoje', 'plataforma tesoura para Uruaçu')
    r("plataforma tesoura em Goiânia.\\n\\n'", "plataforma tesoura em Uruaçu.\\n\\n'")

    # Coverage paragraph
    r('entregas em Goiânia e região metropolitana imediata, não cobramos frete adicional. A plataforma chega no seu galpão, shopping ou canteiro pronta para operar.',
      'entregas em Uruaçu pela BR-153, o frete está incluso para contratos acima de 3 meses. A plataforma chega no seu galpão, frigorífico ou armazém pronta para operar.')

    # Remaining broad catches
    r('em Goiânia.', 'em Uruaçu.')
    r('em Goiânia,', 'em Uruaçu,')
    r('de Goiânia', 'de Uruaçu')
    r('em Goiânia:', 'em Uruaçu:')
    r('em Goiânia e', 'em Uruaçu e')
    r('em Goiânia', 'em Uruaçu')

process_page('ref-goiania-tesoura.html',
    'uruacu-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
    'uruacu-go/aluguel-de-plataforma-elevatoria-tesoura/index.html',
    'TESOURA URUACU', tesoura_replacements)


# ═══════════════════════════════════════════════════════════════════
# COMBUSTAO
# ═══════════════════════════════════════════════════════════════════
def combustao_replacements(r):
    # Title & meta — read actual content
    r('<title>Aluguel de Empilhadeira a Combustão em Goiânia | Move Máquinas</title>',
      '<title>Empilhadeira a Combustão para Locação em Uruaçu-GO | Move Máquinas</title>')
    r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
      'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-empilhadeira-combustao"')
    # OG title/desc — use partial matches
    r('Empilhadeira a Combustão em Goiânia | Move Máquinas"', 'Empilhadeira a Combustão em Uruaçu-GO | Move Máquinas"')
    r('empilhadeira a combustão em Goiânia', 'empilhadeira a combustão em Uruaçu-GO')
    r('Empilhadeira a combustão para locação em Goiânia', 'Empilhadeira a combustão para locação em Uruaçu')

    # Schema
    r('"name": "Aluguel de Empilhadeira a Combustão em Goiânia"', '"name": "Locação de Empilhadeira a Combustão em Uruaçu"')
    r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
      '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
    r('"Empilhadeira a Combustão em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao"',
      '"Empilhadeira a Combustão em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-empilhadeira-combustao"')
    r('Empilhadeira Combustão em Goiânia"', 'Empilhadeira Combustão em Uruaçu"')

    # Breadcrumb
    r('Equipamentos em Goiânia</a>', 'Equipamentos em Uruaçu</a>')
    r('Empilhadeira Combustão em Goiânia</span>', 'Empilhadeira Combustão em Uruaçu</span>')
    r('Empilhadeira a Combustão em Goiânia</span>', 'Empilhadeira a Combustão em Uruaçu</span>')

    # Hero
    r('Empilhadeira a Combustão em <em>Goiânia</em>', 'Empilhadeira a Combustão em <em>Uruaçu</em>')

    # Body — broad replacements
    r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
    r('em Goiânia e região metropolitana', 'em Uruaçu com agendamento')
    r('em Goiânia e região', 'em Uruaçu e norte goiano')
    r('Entrega no mesmo dia em Goiânia', 'Entrega programada via BR-153')
    r('Entrega no mesmo dia na capital', 'Entrega programada pela BR-153')
    r('Aplicações em Goiânia', 'Aplicações agroindustriais')
    r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
    r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')
    r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')
    r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')
    r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
    r('empilhadeira</span> em Goiânia', 'empilhadeira</span> em Uruaçu')
    r('Entrega rápida em <span>Goiânia</span>', 'Entrega programada em <span>Uruaçu</span>')
    r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
    r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
    r('Goiânia-GO (jan/2026)', 'Uruaçu-GO (jan/2026)')
    r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
    r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')
    r('parceiros credenciados em Goiânia', 'centros credenciados na região')
    r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis para Uruaçu:')
    r('empilhadeira em Goiânia hoje', 'empilhadeira para Uruaçu')
    r("empilhadeira em Goiânia.\\n\\n'", "empilhadeira em Uruaçu.\\n\\n'")
    r("empilhadeira a combustão em Goiânia.\\n\\n'", "empilhadeira a combustão em Uruaçu.\\n\\n'")
    r('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital.',
      'Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153. Entrega programada em 24-48h.')
    r('Entrega em Goiânia (sem deslocamento)', 'Entrega em Uruaçu (frete incluso acima de 3 meses)')
    r('Entrega em Goiânia no mesmo dia', 'Entrega programada em Uruaçu')
    r('entrega na capital, sem custo de deslocamento', 'entrega programada pela BR-153, frete incluso acima de 3 meses')
    r('entrega na capital sem custo', 'entrega programada pela BR-153')
    r('locação em Goiânia:', 'locação em Uruaçu:')
    # Broad catches
    r('em Goiânia.', 'em Uruaçu.')
    r('em Goiânia,', 'em Uruaçu,')
    r('de Goiânia', 'de Uruaçu')
    r('em Goiânia:', 'em Uruaçu:')
    r('em Goiânia e', 'em Uruaçu e')
    r('em Goiânia', 'em Uruaçu')

process_page('ref-goiania-combustao.html',
    'uruacu-go-aluguel-de-empilhadeira-combustao-V2.html',
    'uruacu-go/aluguel-de-empilhadeira-combustao/index.html',
    'COMBUSTAO URUACU', combustao_replacements)


# ═══════════════════════════════════════════════════════════════════
# TRANSPALETEIRA
# ═══════════════════════════════════════════════════════════════════
def transpaleteira_replacements(r):
    r('<title>Aluguel de Transpaleteira Elétrica em Goiânia | Move Máquinas</title>',
      '<title>Transpaleteira Elétrica para Locação em Uruaçu-GO | Move Máquinas</title>')
    r('href="https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
      'href="https://movemaquinas.com.br/uruacu-go/aluguel-de-transpaleteira"')
    r('Transpaleteira Elétrica em Goiânia | Move Máquinas"', 'Transpaleteira Elétrica em Uruaçu-GO | Move Máquinas"')
    r('transpaleteira elétrica em Goiânia', 'transpaleteira elétrica em Uruaçu')
    r('Transpaleteira elétrica para locação em Goiânia', 'Transpaleteira elétrica para locação em Uruaçu')
    r('"name": "Aluguel de Transpaleteira Elétrica em Goiânia"', '"name": "Locação de Transpaleteira Elétrica em Uruaçu"')
    r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
      '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
    r('Transpaleteira em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/aluguel-de-transpaleteira"',
      'Transpaleteira em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/aluguel-de-transpaleteira"')
    r('Transpaleteira Elétrica em Goiânia"', 'Transpaleteira Elétrica em Uruaçu"')
    r('Equipamentos em Goiânia</a>', 'Equipamentos em Uruaçu</a>')
    r('Transpaleteira em Goiânia</span>', 'Transpaleteira em Uruaçu</span>')
    r('Transpaleteira Elétrica em Goiânia</span>', 'Transpaleteira Elétrica em Uruaçu</span>')
    r('Transpaleteira Elétrica em <em>Goiânia</em>', 'Transpaleteira Elétrica em <em>Uruaçu</em>')
    r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
    r('em Goiânia e região metropolitana', 'em Uruaçu com agendamento')
    r('em Goiânia e região', 'em Uruaçu e norte goiano')
    r('Entrega no mesmo dia em Goiânia', 'Entrega programada via BR-153')
    r('Entrega no mesmo dia na capital', 'Entrega programada pela BR-153')
    r('Entrega em Goiânia no mesmo dia', 'Entrega programada em Uruaçu')
    r('Entrega em Goiânia (sem deslocamento)', 'Entrega em Uruaçu (frete incluso acima de 3 meses)')
    r('Aplicações em Goiânia', 'Aplicações agroindustriais')
    r('transpaleteira</span> em Goiânia', 'transpaleteira</span> em Uruaçu')
    r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
    r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')
    r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
    r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')
    r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')
    r('Entrega rápida em <span>Goiânia</span>', 'Entrega programada em <span>Uruaçu</span>')
    r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
    r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
    r('Goiânia-GO (jan/2026)', 'Uruaçu-GO (jan/2026)')
    r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
    r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')
    r('parceiros credenciados em Goiânia', 'centros credenciados na região')
    r('Outros equipamentos disponíveis para locação em Goiânia:', 'Outros equipamentos disponíveis para Uruaçu:')
    r('transpaleteira em Goiânia hoje', 'transpaleteira para Uruaçu')
    r("transpaleteira em Goiânia.\\n\\n'", "transpaleteira em Uruaçu.\\n\\n'")
    r("transpaleteira elétrica em Goiânia.\\n\\n'", "transpaleteira elétrica em Uruaçu.\\n\\n'")
    r('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital.',
      'Sede na Av. Eurico Viana, 4913, Goiânia — 280 km de Uruaçu pela BR-153. Entrega programada em 24-48h.')
    r('entrega na capital, sem custo de deslocamento', 'entrega programada pela BR-153, frete incluso acima de 3 meses')
    r('entrega na capital sem custo', 'entrega programada pela BR-153')
    r('locação em Goiânia:', 'locação em Uruaçu:')
    r('locação em Goiânia', 'locação em Uruaçu')
    r('em Goiânia.', 'em Uruaçu.')
    r('em Goiânia,', 'em Uruaçu,')
    r('de Goiânia', 'de Uruaçu')
    r('em Goiânia:', 'em Uruaçu:')
    r('em Goiânia e', 'em Uruaçu e')
    r('em Goiânia', 'em Uruaçu')

process_page('ref-goiania-transpaleteira.html',
    'uruacu-go-aluguel-de-transpaleteira-V2.html',
    'uruacu-go/aluguel-de-transpaleteira/index.html',
    'TRANSPALETEIRA URUACU', transpaleteira_replacements)


# ═══════════════════════════════════════════════════════════════════
# CURSO
# ═══════════════════════════════════════════════════════════════════
def curso_replacements(r):
    # The curso file likely has different title format — use broader patterns
    r('Operador de Empilhadeira em Goiânia | Move Máquinas</title>',
      'Operador de Empilhadeira em Uruaçu-GO | Move Máquinas</title>')
    r('href="https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira"',
      'href="https://movemaquinas.com.br/uruacu-go/curso-de-operador-de-empilhadeira"')
    r('href="https://movemaquinas.com.br/goiania-go/curso-operador-empilhadeira"',
      'href="https://movemaquinas.com.br/uruacu-go/curso-de-operador-de-empilhadeira"')
    r('Operador de Empilhadeira em Goiânia | Move Máquinas"', 'Operador de Empilhadeira em Uruaçu-GO | Move Máquinas"')
    r('operador de empilhadeira em Goiânia', 'operador de empilhadeira em Uruaçu')
    r('Operador de Empilhadeira NR-11 em Goiânia', 'Operador de Empilhadeira NR-11 em Uruaçu')
    r('"name": "Curso de Operador de Empilhadeira em Goiânia"', '"name": "Curso de Operador de Empilhadeira em Uruaçu"')
    r('Curso de Operador de Empilhadeira NR-11 em Goiânia', 'Curso de Operador de Empilhadeira NR-11 em Uruaçu')
    r('"name": "Equipamentos em Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
      '"name": "Equipamentos em Uruaçu", "item": "https://movemaquinas.com.br/uruacu-go/"')
    r('Curso NR-11 em Goiânia"', 'Curso NR-11 em Uruaçu"')
    r('Curso de Operador em Goiânia"', 'Curso de Operador em Uruaçu"')
    r('Equipamentos em Goiânia</a>', 'Equipamentos em Uruaçu</a>')
    r('Curso NR-11 em Goiânia</span>', 'Curso NR-11 em Uruaçu</span>')
    r('Curso de Operador em Goiânia</span>', 'Curso de Operador em Uruaçu</span>')
    r('Operador de Empilhadeira em <em>Goiânia</em>', 'Operador de Empilhadeira em <em>Uruaçu</em>')
    r('Distrito Industrial de Goiânia', 'Distrito Agroindustrial de Uruaçu')
    r('em Goiânia e região metropolitana', 'em Uruaçu e norte goiano')
    r('em Goiânia e região', 'em Uruaçu e norte goiano')
    r('Entrega no mesmo dia em Goiânia', 'Formação presencial em Uruaçu')
    r('Entrega no mesmo dia na capital', 'Instrutor presencial em Uruaçu')
    r('Aplicações em Goiânia', 'Aplicações regionais')
    r('curso</span> em Goiânia', 'curso</span> em Uruaçu')
    r('Aluguel de Plataforma Articulada em Goiânia', 'Plataforma Articulada em Uruaçu')
    r('Aluguel de Plataforma Tesoura em Goiânia', 'Plataforma Tesoura em Uruaçu')
    r('Aluguel de Empilhadeira a Combustão em Goiânia', 'Empilhadeira a Combustão em Uruaçu')
    r('Aluguel de Transpaleteira em Goiânia', 'Transpaleteira Elétrica em Uruaçu')
    r('Curso de Operador de Empilhadeira em Goiânia', 'Curso NR-11 em Uruaçu')
    r('Entrega rápida em <span>Goiânia</span>', 'Atendimento em <span>Uruaçu</span> e norte goiano')
    r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Uruaçu</a>')
    r('Goiânia-GO (dez/2025)', 'Uruaçu-GO (dez/2025)')
    r('Goiânia-GO (jan/2026)', 'Uruaçu-GO (jan/2026)')
    r('Goiânia-GO (fev/2026)', 'Uruaçu-GO (fev/2026)')
    r('Goiânia-GO (mar/2026)', 'Uruaçu-GO (mar/2026)')
    r('parceiros credenciados em Goiânia', 'instrutores credenciados')
    r('Outros equipamentos disponíveis para locação em Goiânia:', 'Equipamentos disponíveis para locação em Uruaçu:')
    r('Base localizada na Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Entrega no mesmo dia na capital.',
      'Sede na Av. Eurico Viana, 4913, Goiânia. Instrutor se desloca pela BR-153 até Uruaçu para formação presencial.')
    r('O que a NR-11 exige das empresas em Goiânia', 'O que a NR-11 exige das empresas em Uruaçu')
    r('das empresas em Goiânia', 'das empresas em Uruaçu')
    r('locação em Goiânia:', 'locação em Uruaçu:')
    r('locação em Goiânia', 'locação em Uruaçu')
    r('em Goiânia hoje', 'em Uruaçu')
    r("em Goiânia.\\n\\n'", "em Uruaçu.\\n\\n'")
    r('em Goiânia.', 'em Uruaçu.')
    r('em Goiânia,', 'em Uruaçu,')
    r('de Goiânia', 'de Uruaçu')
    r('em Goiânia:', 'em Uruaçu:')
    r('em Goiânia e', 'em Uruaçu e')
    r('em Goiânia', 'em Uruaçu')

process_page('ref-goiania-curso.html',
    'uruacu-go-curso-de-operador-de-empilhadeira-V2.html',
    'uruacu-go/curso-de-operador-de-empilhadeira/index.html',
    'CURSO URUACU', curso_replacements)


# ═══════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════
elapsed = time.time() - START
print("\n\n" + "="*80)
print("RESUMO FINAL — 4 LPs de Uruaçu (tesoura, combustão, transpaleteira, curso)")
print("="*80)
for r in results:
    print(f"  {r['page']:<30} J_REF={r['j_ref']:.4f}  {r['url']}")
print(f"\nTEMPO TOTAL: {elapsed:.1f}s")
