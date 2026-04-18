#!/usr/bin/env python3
import re
B='/Users/jrios/move-maquinas-seo'
files = [
    'caldas-novas-go-hub-V2.html',
    'caldas-novas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
    'caldas-novas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
    'caldas-novas-go-aluguel-de-empilhadeira-combustao-V2.html',
    'caldas-novas-go-aluguel-de-transpaleteira-V2.html',
    'caldas-novas-go-curso-de-operador-de-empilhadeira-V2.html',
]
for f in files:
    h = open(f'{B}/{f}').read()
    cn = h.lower().count('caldas novas')
    hotel = h.lower().count('hotel') + h.lower().count('resort')
    go139 = h.lower().count('go-139')
    faq_count = h.count('"@type": "Question"')
    stale = 0
    for line in h.split('\n'):
        if 'Goiânia' in line or 'Goiania' in line:
            if not any(p in line for p in ['addressLocality','Parque das Flores','Av. Eurico','CNPJ','74593','option value','goiania-go/','pub-bd2efcc','Distribuidor exclusivo','170 km','GO-139','sede em Goiânia','base em Goiânia','Sede na','sede na','Caldas Novas-Goiânia','acesso Goiânia']):
                stale += 1
    name = f.replace('caldas-novas-go-','').replace('-V2.html','')[:35]
    print(f'{name:35s} CN:{cn:3d} hotel/resort:{hotel:3d} GO-139:{go139:2d} FAQs:{faq_count} stale:{stale}')
