"""
fix-hubs.py — Corrige estrutura HTML dos hubs de cidade:
1. Adiciona <!DOCTYPE>, <html>, <head> com title/meta/canonical/CSS
2. Remove <link rel="stylesheet"> e <link rel="preload"> do final do body
3. Recria aparecida-de-goiania-go a partir de template (404 atual)
4. Recria anapolis-go (atual é LP errada)
"""

import os, re

ROOT = '/Users/jrios/move-maquinas-seo'

# Dados por cidade: slug, nome display, wikipedia_url, contexto_local, hero_lead, hero_text, dist_goiania
CITIES = {
    'goiania-go': {
        'nome': 'Goiânia',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/goiania-go/',
        'skip_rebuild': True,  # só fix de head
    },
    'senador-canedo-go': {
        'nome': 'Senador Canedo',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/senador-canedo-go/',
        'skip_rebuild': True,
    },
    'brasilia-df': {
        'nome': 'Brasília',
        'estado': 'DF',
        'canonical': 'https://movemaquinas.com.br/brasilia-df/',
        'skip_rebuild': True,
    },
    'luziania-go': {
        'nome': 'Luziânia',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/luziania-go/',
        'skip_rebuild': True,
    },
    'trindade-go': {
        'nome': 'Trindade',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/trindade-go/',
        'skip_rebuild': True,
    },
    'inhumas-go': {
        'nome': 'Inhumas',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/inhumas-go/',
        'skip_rebuild': True,
    },
    'itumbiara-go': {
        'nome': 'Itumbiara',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/itumbiara-go/',
        'skip_rebuild': True,
    },
    'caldas-novas-go': {
        'nome': 'Caldas Novas',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/caldas-novas-go/',
        'skip_rebuild': True,
    },
    'formosa-go': {
        'nome': 'Formosa',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/formosa-go/',
        'skip_rebuild': True,
    },
    'uruacu-go': {
        'nome': 'Uruaçu',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/uruacu-go/',
        'skip_rebuild': True,
    },
    'valparaiso-de-goias-go': {
        'nome': 'Valparaíso de Goiás',
        'estado': 'GO',
        'canonical': 'https://movemaquinas.com.br/valparaiso-de-goias-go/',
        'skip_rebuild': True,
    },
}


def build_head(city_slug, city_data):
    nome = city_data['nome']
    estado = city_data['estado']
    canonical = city_data['canonical']
    title = f'Aluguel de Equipamentos em {nome} | Movemáquinas'
    description = (
        f'Locação de empilhadeiras, plataformas elevatórias e transpaleteiras em {nome} — {estado}. '
        f'Frota Clark, manutenção inclusa, entrega rápida. Movemáquinas.'
    )
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/x-icon" href="/assets/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/inter-latin-w400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles-cbb654b2.css">
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-WNLZBQ7Q');</script>
<!-- End Google Tag Manager -->
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WNLZBQ7Q"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
'''


def fix_hub(city_slug, city_data):
    filepath = os.path.join(ROOT, city_slug, 'index.html')
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # Remover bloco GTM do início (já vai no head)
    # Padrão: <!-- Google Tag Manager --> ... <!-- End Google Tag Manager (noscript) -->
    content = re.sub(
        r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager \(noscript\) -->',
        '',
        content,
        flags=re.DOTALL
    )

    # Remover <link rel="preload"> e <link rel="stylesheet"> do final do body
    content = re.sub(
        r'\s*<link rel="preload" href="[^"]*fonts[^"]*"[^>]*>\s*\n?',
        '\n',
        content
    )
    content = re.sub(
        r'\s*<link rel="stylesheet" href="styles-[^"]*\.css">\s*\n?',
        '\n',
        content
    )

    # Remover </body></html> do final para readicionar limpo
    content = re.sub(r'\s*</body>\s*</html>\s*$', '', content, flags=re.DOTALL)

    # Construir arquivo final
    head = build_head(city_slug, city_data)
    final = head + content.strip() + '\n</body>\n</html>\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final)

    print(f'  FIXED: {city_slug}')


# Fix dos 11 hubs com estrutura quebrada
print('=== Corrigindo hubs com head ausente ===')
for slug, data in CITIES.items():
    fix_hub(slug, data)

print('\nDone. Falta reconstruir aparecida-de-goiania-go e anapolis-go manualmente.')
