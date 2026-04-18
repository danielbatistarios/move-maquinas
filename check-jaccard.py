#!/usr/bin/env python3
import re
def ng(t,n=3):
    t=re.sub(r'<[^>]+>',' ',t)
    t=re.sub(r'[^a-záàâãéèêíïóôõúüç\s]','',t.lower())
    w=t.split()
    return set(' '.join(w[i:i+n]) for i in range(len(w)-n+1))
def j(a,b):
    sa,sb=ng(a),ng(b)
    return len(sa&sb)/len(sa|sb) if sa and sb else 0
B='/Users/jrios/move-maquinas-seo'
ref=open(f'{B}/ref-goiania-articulada.html').read()
sc=open(f'{B}/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html').read()
bsb=open(f'{B}/brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html').read()
print(f'SC art vs REF art: {j(sc,ref):.4f}')
print(f'BSB art vs REF art: {j(bsb,ref):.4f}')
print(f'SC art vs BSB art: {j(sc,bsb):.4f}')
rh=open(f'{B}/ref-goiania-hub.html').read()
sh=open(f'{B}/senador-canedo-go-hub-V2.html').read()
bh=open(f'{B}/brasilia-df-hub-V2.html').read()
print(f'SC hub vs REF hub: {j(sh,rh):.4f}')
print(f'BSB hub vs REF hub: {j(bh,rh):.4f}')
print(f'SC hub vs BSB hub: {j(sh,bh):.4f}')
