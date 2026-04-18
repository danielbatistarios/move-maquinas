#!/usr/bin/env python3
"""
template-extractor.py
Extrai template com {{placeholders}} da referência de Goiânia.
Preserva TODA a estrutura HTML/CSS/JS. Substitui apenas texto visível.
"""
import re, json, os

DIR = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(DIR, 'ref-goiania-articulada.html')

with open(REF, 'r') as f:
    html = f.read()

# ═══════════════════════════════════════════════
# REPLACEMENTS: text → placeholder
# Order matters: longer/specific strings first
# ═══════════════════════════════════════════════

replacements = []

def R(old, placeholder):
    """Register a replacement"""
    replacements.append((old, '{{' + placeholder + '}}'))

# ── META ──
R('Aluguel de Plataforma Elevatória Articulada em Goiânia | Move Máquinas', 'META_TITLE')
R('Aluguel de plataforma elevatória articulada em Goiânia a partir de R$2.800/mês. Modelos de 12 e 15 metros, diesel ou elétrica. Braço articulado com alcance lateral para fachadas, galpões e obras verticais. Move Máquinas: +20 anos no mercado.', 'META_DESC')
R('Plataforma articulada para locação em Goiânia. Modelos de 12 a 15 metros com alcance lateral. Manutenção inclusa, entrega mesmo dia. R$2.800 a R$4.000/mês.', 'META_OG_DESC')

# ── GEO ──
R('Goiânia, Goiás, Brasil', 'GEO_PLACENAME')
R('-16.7234;-49.2654', 'GEO_POSITION')
R('-16.7234, -49.2654', 'GEO_ICBM')

# ── SCHEMA (will be replaced as whole block) ──
# Find the JSON-LD block
schema_match = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', html, re.DOTALL)
if schema_match:
    R(schema_match.group(2), 'SCHEMA_JSON')

# ── BREADCRUMB ──
R('Equipamentos em Goiânia', 'BREADCRUMB_CITY')
R('Plataforma Articulada em Goiânia', 'BREADCRUMB_PAGE')

# ── HERO ──
R('Plataformas prontas para entrega', 'HERO_BADGE')
R('Aluguel de Plataforma Elevatória Articulada em <em>Goiânia</em>', 'HERO_H1')

# Find hero lead paragraph
hero_lead = re.search(r'class="hero__lead">(.*?)</p>', html, re.DOTALL)
if hero_lead:
    R(hero_lead.group(1), 'HERO_LEAD')

# ── TRUST BAR ──
trust_badges = re.findall(r'class="trust-badge__text">(.*?)</span>', html)
for i, badge in enumerate(trust_badges):
    R(badge, f'TRUST_BADGE_{i}')

# ── STATS BAR ──
stats_track = re.search(r'class="stats-bar__track">(.*?)</div>', html, re.DOTALL)
if stats_track:
    R(stats_track.group(1).strip(), 'STATS_CONTENT')

# ── H2s ──
h2_ids = ['oque-h2', 'specs-h2', 'compare-h2', 'preco-h2', 'apps-h2', 'incluso-h2', 'depo-h2', 'nr35-h2', 'cobertura-h2', 'faq-h2']
h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
for i, h2 in enumerate(h2_matches):
    R(h2, f'H2_{i}')

# ── "O QUE É" paragraphs ──
# First paragraph after H2
oque_section = html[html.find('aria-labelledby="oque-h2"'):html.find('<!-- ========== SHORTS')]
oque_paras = re.findall(r'<p>(.*?)</p>', oque_section, re.DOTALL)
for i, para in enumerate(oque_paras):
    if len(para) > 80:
        R(para, f'OQUE_P{i}')

# H3s in "O que é"
oque_h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', oque_section)
for i, h3 in enumerate(oque_h3s):
    R(h3, f'OQUE_H3_{i}')

# Checklist items in "O que é"
checklist_items = re.findall(r'<div><strong>(.*?)</strong>(.*?)</div>', oque_section, re.DOTALL)
for i, (bold, rest) in enumerate(checklist_items):
    R(f'<strong>{bold}</strong>{rest}', f'CHECKLIST_{i}')

# ── SHORTS subtitle ──
shorts_section = html[html.find('SHORTS COMERCIAIS'):html.find('COTAÇÃO RÁPIDA')]
shorts_h3 = re.search(r'class="section-title">(.*?)</h3>', shorts_section, re.DOTALL)
if shorts_h3:
    R(shorts_h3.group(1), 'SHORTS_TITLE')
shorts_sub = re.search(r'class="section-subtitle">(.*?)</p>', shorts_section, re.DOTALL)
if shorts_sub:
    R(shorts_sub.group(1), 'SHORTS_SUB')

# ── COTAÇÃO FORM ──
form_section = html[html.find('COTAÇÃO RÁPIDA'):html.find('MODELOS DISPONÍVEIS')]
form_h3 = re.search(r'Solicite orçamento de.*?</h3>', form_section, re.DOTALL)
if form_h3:
    R(form_h3.group(0).split('>')[1].replace('</h3',''), 'FORM_TITLE')
form_desc = re.search(r'Preencha os campos.*?</p>', form_section, re.DOTALL)
if form_desc:
    R(form_desc.group(0).split('>')[1].replace('</p',''), 'FORM_DESC')

# Form delivery line
form_delivery = re.findall(r'Entrega.*?</li>', form_section)
if form_delivery:
    delivery_text = re.sub(r'<[^>]+>', '', form_delivery[0])
    R(delivery_text.strip(), 'FORM_DELIVERY')

# ── FLEET CAROUSEL ──
fleet_section = html[html.find('MODELOS DISPONÍVEIS'):html.find('FALA DO ESPECIALISTA')]
fleet_sub = re.search(r'class="section-subtitle">(.*?)</p>', fleet_section, re.DOTALL)
if fleet_sub:
    R(fleet_sub.group(1), 'FLEET_SUB')

# Fleet slide descriptions
fleet_descs = re.findall(r'class="fleet-carousel__subtitle">(.*?)</p>', fleet_section, re.DOTALL)
for i, desc in enumerate(fleet_descs):
    R(desc, f'FLEET_SUBTITLE_{i}')

fleet_paras = []
for m in re.finditer(r'</div>\s*<p>(.*?)</p>\s*<div class="fleet-carousel__specs">', fleet_section, re.DOTALL):
    fleet_paras.append(m.group(1))
for i, para in enumerate(fleet_paras):
    R(para, f'FLEET_DESC_{i}')

fleet_consultoria = re.search(r'Dúvida sobre qual modelo.*?</p>', fleet_section, re.DOTALL)
if fleet_consultoria:
    text = re.sub(r'<[^>]+>', '', fleet_consultoria.group(0))
    R(text.strip(), 'FLEET_CONSULTORIA')

# ── EXPERT QUOTE ──
expert_section = html[html.find('FALA DO ESPECIALISTA'):html.find('COMPARATIVO')]
expert_text = re.search(r'class="expert-quote__text"[^>]*>"(.*?)"', expert_section, re.DOTALL)
if expert_text:
    R(expert_text.group(1), 'EXPERT_QUOTE')

# ── COMPARATIVO ──
compare_section = html[html.find('COMPARATIVO'):html.find('MOBILE FORM')]
compare_intro = re.search(r'class="compare__intro">(.*?)</p>', compare_section, re.DOTALL)
if compare_intro:
    R(compare_intro.group(1), 'COMPARE_INTRO')

# Compare card descriptions
compare_h3s = re.findall(r'<h3>(.*?)</h3>', compare_section)
for i, h3 in enumerate(compare_h3s):
    R(h3, f'COMPARE_H3_{i}')

compare_paras = re.findall(r'<p>(.*?)</p>', compare_section, re.DOTALL)
for i, para in enumerate(compare_paras):
    if len(para) > 60 and 'compare__intro' not in para:
        R(para, f'COMPARE_P{i}')

# Compare verdict
verdict = re.search(r'class="compare__verdict.*?<p><strong>(.*?)</p>', compare_section, re.DOTALL)
if verdict:
    R(verdict.group(1), 'COMPARE_VERDICT')

# Compare links
compare_links = re.findall(r'<a href="(/goiania-go/[^"]+)"[^>]*>(.*?)</a>', compare_section)
for i, (href, text) in enumerate(compare_links):
    R(text, f'COMPARE_LINK_TEXT_{i}')
    R(href, f'COMPARE_LINK_HREF_{i}')

# ── PRICE ──
price_section = html[html.find('QUANTO CUSTA'):html.find('APLICAÇÕES REAIS')]
price_sub = re.search(r'class="section-subtitle">(.*?)</p>', price_section, re.DOTALL)
if price_sub:
    R(price_sub.group(1), 'PRICE_SUB')

price_note = re.search(r'class="price__note.*?<p>(.*?)</p>', price_section, re.DOTALL)
if price_note:
    R(price_note.group(1), 'PRICE_NOTE')

# ── APPLICATIONS ──
apps_section = html[html.find('APLICAÇÕES REAIS'):html.find('O QUE ESTÁ INCLUSO')]
apps_sub = re.search(r'class="section-subtitle">(.*?)</p>', apps_section, re.DOTALL)
if apps_sub:
    R(apps_sub.group(1), 'APPS_SUB')

app_h3s = re.findall(r'<h3>(.*?)</h3>', apps_section)
for i, h3 in enumerate(app_h3s):
    R(h3, f'APP_TITLE_{i}')

app_paras = re.findall(r'<p>(.*?)</p>', apps_section, re.DOTALL)
for i, para in enumerate(app_paras):
    if len(para) > 60 and 'section-subtitle' not in para:
        R(para, f'APP_DESC_{i}')

app_imgs = re.findall(r'alt="(.*?)"', apps_section)
for i, alt in enumerate(app_imgs):
    if len(alt) > 20:
        R(alt, f'APP_IMG_ALT_{i}')

# ── INCLUSO ──
incluso_section = html[html.find('O QUE ESTÁ INCLUSO'):html.find('DEPOIMENTOS')]
incluso_sub = re.search(r'class="section-subtitle">(.*?)</p>', incluso_section, re.DOTALL)
if incluso_sub:
    R(incluso_sub.group(1), 'INCLUSO_SUB')

incluso_titles = re.findall(r'<strong>(.*?)</strong>', incluso_section)
for i, title in enumerate(incluso_titles):
    R(title, f'INCLUSO_TITLE_{i}')

incluso_descs = re.findall(r'</strong>\s*<p>(.*?)</p>', incluso_section, re.DOTALL)
for i, desc in enumerate(incluso_descs):
    R(desc, f'INCLUSO_DESC_{i}')

# ── TESTIMONIALS ──
test_section = html[html.find('DEPOIMENTOS'):html.find('NR-35')]
test_texts = re.findall(r'class="testimonial__text">"(.*?)"', test_section, re.DOTALL)
for i, text in enumerate(test_texts):
    R(text, f'TEST_TEXT_{i}')

test_names = re.findall(r'<strong>(.*?)</strong>', test_section)
for i, name in enumerate(test_names):
    R(name, f'TEST_NAME_{i}')

test_roles = re.findall(r'</strong>\s*\n\s*(.*?)\s*\n\s*</div>', test_section, re.DOTALL)
for i, role in enumerate(test_roles):
    role = role.strip()
    if len(role) > 10:
        R(role, f'TEST_ROLE_{i}')

# ── NR-35 ──
nr_section = html[html.find('NR-35'):html.find('COBERTURA')]
nr_paras = re.findall(r'<p>(.*?)</p>', nr_section, re.DOTALL)
for i, para in enumerate(nr_paras):
    if len(para) > 60:
        R(para, f'NR_P{i}')

nr_strongs = re.findall(r'<strong>(.*?)</strong>', nr_section)
for i, s in enumerate(nr_strongs):
    if len(s) > 10:
        R(s, f'NR_STRONG_{i}')

# ── COBERTURA ──
cov_section = html[html.find('COBERTURA'):html.find('FAQ')]
cov_sub = re.search(r'class="section-subtitle">(.*?)</p>', cov_section, re.DOTALL)
if cov_sub:
    R(cov_sub.group(1), 'COV_SUB')

cov_paras = re.findall(r'<p>(.*?)</p>', cov_section, re.DOTALL)
for i, para in enumerate(cov_paras):
    if len(para) > 60 and 'section-subtitle' not in para:
        R(para, f'COV_P{i}')

# ── FAQ questions + answers ──
faq_section = html[html.find('<!-- ========== FAQ'):html.find('<!-- ========== FOOTER')]
faq_qs = re.findall(r'itemprop="name"[^>]*>(.*?)</h3>', faq_section, re.DOTALL)
for i, q in enumerate(faq_qs):
    q_clean = re.sub(r'<[^>]+>', '', q).strip()
    R(q_clean, f'FAQ_Q_{i}')

faq_as = re.findall(r'itemprop="text">(.*?)</div>', faq_section, re.DOTALL)
for i, a in enumerate(faq_as):
    R(a, f'FAQ_A_{i}')

# ── CTA FOOTER ──
cta_section = html[html.find('FOOTER CTA'):html.find('STICKY CTA')]
cta_h3 = re.search(r'id="cta-h2">(.*?)</h3>', cta_section, re.DOTALL)
if cta_h3:
    R(cta_h3.group(1), 'CTA_TITLE')

cta_sub = re.search(r'class="cta-final__sub">(.*?)</p>', cta_section, re.DOTALL)
if cta_sub:
    R(cta_sub.group(1), 'CTA_SUB')

# ── URL slugs ──
R('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', 'PAGE_URL')
R('/goiania-go/', 'CITY_URL/')
R('goiania-go', 'CITY_SLUG')

# ── WhatsApp message ──
R('em%20Goi%C3%A2nia', 'WA_CITY_ENCODED')
R('em+Goiania', 'WA_CITY_PLUS')

# ── Remaining city name (catch-all LAST) ──
R('Goiânia', 'CITY_NAME')
R('Goiania', 'CITY_NAME_ASCII')

# ═══════════════════════════════════════════════
# APPLY ALL REPLACEMENTS
# ═══════════════════════════════════════════════
template = html
applied = 0
for old, placeholder in replacements:
    if old in template:
        template = template.replace(old, placeholder)
        applied += 1

# ═══════════════════════════════════════════════
# SAVE TEMPLATE
# ═══════════════════════════════════════════════
outfile = os.path.join(DIR, 'template-articulada.html')
with open(outfile, 'w') as f:
    f.write(template)

# Count placeholders
placeholder_count = len(re.findall(r'\{\{[A-Z_0-9]+\}\}', template))
remaining_goiania = template.count('Goiânia') + template.count('Goiania')

print(f"Template saved: {outfile}")
print(f"Size: {len(template)//1024}KB")
print(f"Replacements applied: {applied}/{len(replacements)}")
print(f"Placeholders in template: {placeholder_count}")
print(f"Remaining 'Goiânia': {remaining_goiania}")

# List all placeholders
placeholders = sorted(set(re.findall(r'\{\{([A-Z_0-9]+)\}\}', template)))
print(f"\nPlaceholders ({len(placeholders)}):")
for p in placeholders:
    count = template.count('{{' + p + '}}')
    print(f"  {{{{{p}}}}} x{count}")

PYEOF
