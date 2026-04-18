import re

DIR = '/Users/jrios/move-maquinas-seo'
SLUG = 'valparaiso-de-goias-go'

files = [
    f'{DIR}/valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
    f'{DIR}/valparaiso-de-goias-go-aluguel-de-empilhadeira-combustao-V2.html',
    f'{DIR}/valparaiso-de-goias-go-aluguel-de-transpaleteira-V2.html',
    f'{DIR}/valparaiso-de-goias-go-curso-de-operador-de-empilhadeira-V2.html',
]

# Fix stray service links (NOT hub links which are legitimate)
service_paths = [
    'aluguel-de-plataforma-elevatoria-articulada',
    'aluguel-de-plataforma-elevatoria-tesoura',
    'aluguel-de-empilhadeira-combustao',
    'aluguel-de-transpaleteira',
    'curso-operador-empilhadeira',
    'curso-de-operador-de-empilhadeira',
]

for fpath in files:
    h = open(fpath).read()
    changed = False
    for svc in service_paths:
        old = f'/goiania-go/{svc}'
        new = f'/{SLUG}/{svc}'
        if old in h:
            h = h.replace(old, new)
            changed = True
            print(f'  Fixed {old} in {fpath.split("/")[-1]}')
    if changed:
        open(fpath, 'w').write(h)

# Also check curso file for remaining goiania-go links
for fpath in files:
    h = open(fpath).read()
    matches = re.findall(r'goiania-go/[a-z-]+', h)
    if matches:
        print(f'\n  Remaining in {fpath.split("/")[-1]}:')
        for m in matches:
            print(f'    {m}')

print('\nDone fixing stray links')
