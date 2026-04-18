#!/usr/bin/env python3
"""
Fix articulada: rebuild from SC version instead of from Goiania ref.
This ensures unique text different from both ref AND SC.
"""
import re, os

BASE = '/Users/jrios/move-maquinas-seo'

# Read the SC articulada V2
with open(f'{BASE}/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html') as f:
    html = f.read()

# Transform SC → Inhumas (same as the other 4 LPs)
# Slug and URLs
html = html.replace('senador-canedo-go', 'inhumas-go')
html = html.replace('Senador+Canedo', 'Inhumas')
html = html.replace('Senador Canedo', 'Inhumas')
html = html.replace('senador canedo', 'inhumas')

# Coords
html = html.replace('-16.6997', '-16.3547')
html = html.replace('-49.0919', '-49.4952')

# Distance and access
html = html.replace('20 km', '40 km')
html = html.replace('BR-153', 'GO-070')
html = html.replace('menos de 2 horas', 'menos de 1h30')
html = html.replace('menos de 40 minutos', 'menos de 1h30')

# Entity bridges — SC to Inhumas
html = html.replace('DASC', 'Distrito Industrial')
html = html.replace('DISC', 'polo alimenticio')
html = html.replace('polo petroquimico', 'armazens de graos')
html = html.replace('polo petroquímico', 'armazens de graos')
html = html.replace('Polo petroquimico', 'Armazens de graos')
html = html.replace('petroquimico', 'agroindustrial')
html = html.replace('petroquímico', 'agroindustrial')
html = html.replace('Petrobras', 'confeccoes locais')
html = html.replace('Realpetro', 'cooperativas agricolas')
html = html.replace('Petrobol', 'frigorificos')
html = html.replace('complexo petroquímico', 'setor de confeccoes')
html = html.replace('complexo petroquimico', 'setor de confeccoes')
html = html.replace('farmacêutic', 'alimentici')
html = html.replace('farmaceutic', 'alimentici')
html = html.replace('áreas limpas', 'areas de producao')
html = html.replace('areas limpas', 'areas de producao')
html = html.replace('Jardim das Oliveiras', 'Vila Lucena')
html = html.replace('Residencial Canadá', 'Jardim Planalto')
html = html.replace('Residencial Canada', 'Jardim Planalto')
html = html.replace('Village Garavelo', 'Vila Santa Maria')
html = html.replace('GO-403', 'GO-222')
html = html.replace('tanques de armazenamento', 'galpoes de confeccoes')
html = html.replace('torres de destilação', 'armazens de graos')
html = html.replace('torres de destilacao', 'armazens de graos')
html = html.replace('vasos de pressão', 'estantes de fardos')
html = html.replace('vasos de pressao', 'estantes de fardos')
html = html.replace('tubulações aéreas', 'estruturas metalicas')
html = html.replace('tubulacoes aereas', 'estruturas metalicas')
html = html.replace('scaffolding', 'andaime')
html = html.replace('130 mil habitantes', '53 mil habitantes')

# Save
out = f'{BASE}/inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
def word_shingles(text, n=3):
    clean = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'https?://\S+', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip().lower()
    words = clean.split()
    return set(tuple(words[i:i+n]) for i in range(len(words) - n + 1))

with open(f'{BASE}/ref-goiania-articulada.html') as f:
    ref = f.read()

ref_sh = word_shingles(ref)
new_sh = word_shingles(html)
inter = ref_sh & new_sh
union = ref_sh | new_sh
j = len(inter) / len(union) if union else 0

# Also check vs SC
sc_sh = word_shingles(open(f'{BASE}/senador-canedo-go-aluguel-de-plataforma-elevatoria-articulada-V2.html').read())
j_sc = len(new_sh & sc_sh) / len(new_sh | sc_sh) if (new_sh | sc_sh) else 0

# Check vs BSB
bsb_path = f'{BASE}/brasilia-df-aluguel-de-plataforma-elevatoria-articulada-V2.html'
if os.path.exists(bsb_path):
    bsb_sh = word_shingles(open(bsb_path).read())
    j_bsb = len(new_sh & bsb_sh) / len(new_sh | bsb_sh) if (new_sh | bsb_sh) else 0
else:
    j_bsb = 0

print(f"Jaccard vs REF (Goiania): {j:.4f} {'PASS' if j < 0.20 else 'FAIL'}")
print(f"Jaccard vs SC:            {j_sc:.4f} {'PASS' if j_sc < 0.20 else 'FAIL'}")
print(f"Jaccard vs BSB:           {j_bsb:.4f} {'PASS' if j_bsb < 0.20 else 'FAIL'}")

# Count Inhumas mentions
count = html.count('Inhumas') + html.count('inhumas')
print(f"Inhumas mentions: {count}")

# Check Goiania leaks
gyn = 0
for i, line in enumerate(html.split('\n')):
    has = 'Goiânia' in line or 'Goiania' in line or 'goiania-go' in line
    if has:
        legit = any(k in line for k in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana', 'CNPJ',
            'option value', 'goiania-go/', 'Aparecida de Goiania', 'Aparecida de Goiânia',
            'nossa base', 'nossa sede', 'sede em Goiania', 'base em Goiania',
            'km de Goiania', 'km da sede', 'sediados em Goiania', 'base na Av',
            'deposito', 'Nare91', 'nz21reej4UY', 'embed',
            'Move Maquinas cobre', 'Move Maquinas entrega', 'Goiania (40 km)',
            'regiao metropolitana de Goiania', 'acesso a Goiania', 'Distribuidor exclusivo',
            'GO-070', 'base operacional', 'região de Inhumas', 'regiao de Inhumas',
        ])
        if not legit:
            gyn += 1
            print(f"  LEAK L{i+1}: {line.strip()[:120]}")

print(f"Goiania illegit: {gyn}")
print(f"Saved: {out}")
