#!/usr/bin/env python3
"""
Fix 4 remaining issues in home @graph:
1. FAQ — 3 answers with < 3 sentences → expand to 3+ sentences with named entities
2. AggregateRating — remove (no Review[] data) — safer than keeping unverifiable
3. Person — add sameAs LinkedIn + fix url trailing slash
4. openingHoursSpecification — add specialOpeningHoursSpecification (feriados)
"""
import json, re

PATH = "/Users/jrios/move-maquinas-seo/index.html"

with open(PATH) as f:
    html = f.read()

blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
data = json.loads(blocks[0])
graph = data['@graph']

org    = next(n for n in graph if '#organization' in str(n.get('@id', '')))
person = next(n for n in graph if '#person' in str(n.get('@id', '')))
faq    = next(n for n in graph if n.get('@type') == 'FAQPage')

# ── 1. EXPAND FAQ ANSWERS ─────────────────────────────────────────────────────
FAQ_FIXES = {
    "Quais equipamentos a Movemáquinas oferece?": {
        "text": (
            "A Movemáquinas oferece locação de empilhadeiras a combustão e elétricas Clark, "
            "plataformas elevatórias tipo tesoura e articulada, e transpaleteiras elétricas. "
            "Todos os equipamentos são da marca Clark, líder mundial no segmento de movimentação de cargas. "
            "O portfólio completo atende operações industriais, logísticas e de construção civil em Goiás, DF, Tocantins e Mato Grosso."
        )
    },
    "Qual a área de atendimento?": {
        "text": (
            "A Movemáquinas atende Goiânia e região metropolitana com entrega em até 24 horas, "
            "além das cidades de Anápolis, Aparecida de Goiânia, Senador Canedo, Trindade, Inhumas, "
            "Itumbiara, Caldas Novas, Formosa, Luziânia, Valparaíso de Goiás, Brasília (DF) e Uruaçu. "
            "Consulte disponibilidade em outras cidades do interior de Goiás pelo WhatsApp (62) 98263-7300."
        )
    },
    "Como solicitar orçamento?": {
        "text": (
            "O orçamento pode ser solicitado pelo WhatsApp (62) 98263-7300, pelo e-mail ou pelo formulário de contato no site. "
            "A equipe comercial responde em horário comercial, segunda a sexta das 8h às 18h. "
            "Informe o modelo desejado, a cidade de entrega e o período de locação para receber uma proposta personalizada."
        )
    },
}

for q in faq.get('mainEntity', []):
    name = q.get('name', '')
    if name in FAQ_FIXES:
        q['acceptedAnswer']['text'] = FAQ_FIXES[name]['text']

# ── 2. REMOVE AggregateRating (no Review[] — vulnerable to deindexation) ─────
if 'aggregateRating' in org:
    del org['aggregateRating']
    print("  Removed aggregateRating (no Review[] data)")

# ── 3. PERSON — sameAs + trailing slash ──────────────────────────────────────
person['sameAs'] = ["https://www.linkedin.com/company/move-maquinas-oficial/"]
person['url'] = "https://movemaquinas.com.br/sobre/"
print("  Person sameAs + url fixed")

# ── 4. openingHoursSpecification — add specialOpeningHours (feriados) ─────────
org['specialOpeningHoursSpecification'] = [
    {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": "PublicHolidays",
        "opens": "00:00",
        "closes": "00:00"
    }
]
print("  specialOpeningHoursSpecification added")

# ── WRITE BACK ────────────────────────────────────────────────────────────────
new_schema_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
new_block = f'<script type="application/ld+json">{new_schema_json}</script>'

old_block_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
html_out = html[:old_block_match.start()] + new_block + html[old_block_match.end():]

with open(PATH, "w") as f:
    f.write(html_out)

print("  OK: index.html saved")
