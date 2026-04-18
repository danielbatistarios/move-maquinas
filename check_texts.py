import re
for fname in ['ref-goiania-tesoura.html','ref-goiania-combustao.html','ref-goiania-transpaleteira.html','ref-goiania-curso.html']:
    h = open(fname).read()
    h2 = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    h2 = re.sub(r'<script[^>]*>.*?</script>', '', h2, flags=re.DOTALL)
    texts = re.findall(r'>([^<]{80,})<', h2)
    print(f'\n=== {fname} ({len(texts)} blocks) ===')
    for i,t in enumerate(texts):
        print(f'[{i}] {t[:150]}')
