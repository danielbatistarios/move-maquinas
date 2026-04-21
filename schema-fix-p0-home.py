#!/usr/bin/env python3
"""
Round 2 — Home P0 fixes:
1. WebSite: add significantLink[]
2. Organization: replace telephone[] with 2× ContactPoint nodes
3. Organization: add iso6523Code, naics, vatID
"""
import json, re

PATH = "/Users/jrios/move-maquinas-seo/index.html"

with open(PATH) as f:
    html = f.read()

blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
data = json.loads(blocks[0])
graph = data['@graph']

org     = next(n for n in graph if '#organization' in str(n.get('@id', '')))
website = next(n for n in graph if '#website' in str(n.get('@id', '')))

# ── 1. WebSite: significantLink ───────────────────────────────────────────────
website['significantLink'] = [
    "https://movemaquinas.com.br/goiania-go/",
    "https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao/",
    "https://movemaquinas.com.br/goiania-go/aluguel-de-plataforma-elevatoria-tesoura/",
    "https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira/",
    "https://movemaquinas.com.br/venda-de-maquinas-clark/"
]
print("  WebSite.significantLink added")

# ── 2. Organization: 2× ContactPoint (replace telephone array) ────────────────
phones = org.pop('telephone', [])  # remove bare telephone array
org['contactPoint'] = [
    {
        "@type": "ContactPoint",
        "telephone": "+55-62-98263-7300",
        "contactType": "sales",
        "areaServed": "BR",
        "availableLanguage": "Portuguese"
    },
    {
        "@type": "ContactPoint",
        "telephone": "+55-62-98175-3350",
        "contactType": "customer support",
        "areaServed": "BR",
        "availableLanguage": "Portuguese"
    }
]
print("  Organization.contactPoint (2×) added, telephone array removed")

# ── 3. Organization: iso6523Code, naics, vatID ────────────────────────────────
org['iso6523Code'] = "0060:32428258000180"
org['naics']       = "532412"
org['vatID']       = "32428258000180"
print("  Organization.iso6523Code + naics + vatID added")

# ── WRITE BACK ────────────────────────────────────────────────────────────────
new_json  = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
new_block = f'<script type="application/ld+json">{new_json}</script>'
old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
html_out  = html[:old_match.start()] + new_block + html[old_match.end():]

with open(PATH, "w") as f:
    f.write(html_out)

print("  OK: index.html saved")
