#!/usr/bin/env python3
"""
Round 3 — Home P1 fixes (code-actionable, no client data required):
1. Person.name → full name "Márcio Rocha"
2. makesOffer → add priceCurrency + availability
3. WebPage → add hasPart: [{@id: #faqpage}]
4. Organization → add member: [{@id: #person-marcio}]
5. WebSite → add hasPart: [{@id: blog/#blog}]
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
webpage = next(n for n in graph if n.get('@type') == 'WebPage')
person  = next(n for n in graph if '#person' in str(n.get('@id', '')))

# ── 1. Person.name → full name ────────────────────────────────────────────────
person['name'] = "Márcio Rocha"
print("  Person.name → 'Márcio Rocha'")

# ── 2. makesOffer → priceCurrency + availability ─────────────────────────────
offer = org.get('makesOffer', {})
if isinstance(offer, dict):
    offer['priceCurrency'] = "BRL"
    offer['availability'] = "https://schema.org/InStock"
    print("  makesOffer.priceCurrency + availability added")

# ── 3. WebPage → hasPart: FAQPage ────────────────────────────────────────────
faq_id = "https://movemaquinas.com.br/#faqpage"
webpage['hasPart'] = [{"@id": faq_id}]
print("  WebPage.hasPart → #faqpage")

# ── 4. Organization → member: Person ─────────────────────────────────────────
person_id = "https://movemaquinas.com.br/#person-marcio"
org['member'] = [{"@id": person_id}]
print("  Organization.member → #person-marcio")

# ── 5. WebSite → hasPart: Blog ───────────────────────────────────────────────
blog_id = "https://movemaquinas.com.br/blog/#blog"
website['hasPart'] = [{"@id": blog_id}]
print("  WebSite.hasPart → blog/#blog")

# ── WRITE BACK ────────────────────────────────────────────────────────────────
new_json  = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
new_block = f'<script type="application/ld+json">{new_json}</script>'
old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
html_out  = html[:old_match.start()] + new_block + html[old_match.end():]

with open(PATH, "w") as f:
    f.write(html_out)

print("  OK: index.html saved")
