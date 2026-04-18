import re
def get_text(t):
    c=re.sub(r'<style[^>]*>.*?</style>','',t,flags=re.DOTALL)
    c=re.sub(r'<script[^>]*>.*?</script>','',c,flags=re.DOTALL)
    c=re.sub(r'<[^>]+>',' ',c);c=re.sub(r'https?://\S+','',c)
    return re.sub(r'\s+',' ',c).strip().lower()
def ws(t,n=3):
    w=t.split()
    return set(tuple(w[i:i+n]) for i in range(len(w)-n+1))
rt=get_text(open('/Users/jrios/move-maquinas-seo/ref-goiania-articulada.html').read())
nt=get_text(open('/Users/jrios/move-maquinas-seo/trindade-go-aluguel-de-plataforma-elevatoria-articulada-V2.html').read())
rs=ws(rt);ns=ws(nt);shared=rs&ns
for s in sorted([' '.join(x) for x in shared]):
    print(s)
print(f'---Total shared: {len(shared)}, union: {len(rs|ns)}')
