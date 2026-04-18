"""
Link Audit — Move Máquinas
Gera link-audit.html + link-audit.csv com análise completa de linkagem interna.
Uso: python3 link-audit.py
"""

import glob, os, csv, re
from html.parser import HTMLParser
from collections import defaultdict
from datetime import datetime

ROOT = '/Users/jrios/move-maquinas-seo'
SITE_BASE = '/'

GENERIC_ANCHORS = {
    'clique aqui', 'saiba mais', 'acesse', 'veja mais', 'leia mais',
    'aqui', 'link', 'clique', 'acesse aqui', 'veja', 'confira', 'mais'
}

# ── Parser ──────────────────────────────────────────────────────────────────

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.title = ''
        self.in_a = False
        self.in_title = False
        self.current_href = ''
        self.current_text = ''
        self.current_title_text = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        if tag == 'a':
            self.in_a = True
            d = dict(attrs)
            self.current_href = d.get('href', '')
            self.current_text = ''

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'a' and self.in_a:
            self.links.append((self.current_href, self.current_text.strip()))
            self.in_a = False

    def handle_data(self, data):
        if self.in_title:
            self.current_title_text += data
        if self.in_a:
            self.current_text += data


def file_to_url(filepath):
    rel = filepath.replace(ROOT, '').replace('/index.html', '') or '/'
    return rel if rel else '/'


def classify_anchor(text, href):
    t = text.lower().strip()
    if not t or t in GENERIC_ANCHORS:
        return 'genérica'
    if re.search(r'\b(empilhadeira|plataforma|transpaleteira|clark|locação|aluguel|curso|operador|combustão|elétrica|tesoura|articulada)\b', t, re.I):
        return 'rica (keyword)'
    if re.search(r'\b(goiânia|brasília|aparecida|trindade|anápolis|inhumas|uruaçu|caldas|luziânia|valparaíso|formosa|itumbiara|senador)\b', t, re.I):
        return 'rica (cidade)'
    return 'descritiva'


def classify_link_type(href, current_url):
    if not href or href.startswith('#') or href.startswith('javascript'):
        return 'âncora/js'
    if href.startswith('mailto:'):
        return 'email'
    if href.startswith('tel:') or href.startswith('https://wa.me'):
        return 'telefone/whatsapp'
    if href.startswith('http'):
        return 'externo'
    return 'interno'


# ── Crawl ────────────────────────────────────────────────────────────────────

files = sorted(glob.glob(f'{ROOT}/**/index.html', recursive=True))
pages = {}   # url -> {title, filepath, links_out: [(href, anchor, type, anchor_type)]}

for filepath in files:
    url = file_to_url(filepath)
    parser = LinkParser()
    try:
        with open(filepath, encoding='utf-8', errors='ignore') as f:
            content = f.read()
        parser.feed(content)
    except Exception:
        continue

    title = parser.current_title_text.strip() or url
    links_out = []
    for href, text in parser.links:
        ltype = classify_link_type(href, url)
        if ltype != 'interno':
            continue
        # Normalizar href para URL canônica
        if href.endswith('/index.html'):
            href = href[:-len('/index.html')]
        if href == '':
            href = '/'
        href = href.rstrip('/') or '/'
        anchor_type = classify_anchor(text, href)
        links_out.append({
            'href': href,
            'anchor': text,
            'anchor_type': anchor_type,
        })

    pages[url] = {
        'title': title,
        'filepath': filepath.replace(ROOT + '/', ''),
        'links_out': links_out,
    }

all_urls = set(pages.keys())

# Contar links recebidos
links_in = defaultdict(list)
for src_url, data in pages.items():
    for link in data['links_out']:
        target = link['href'].rstrip('/') or '/'
        links_in[target].append({'from': src_url, 'anchor': link['anchor'], 'anchor_type': link['anchor_type']})

# ── Análise ──────────────────────────────────────────────────────────────────

rows = []
for url, data in sorted(pages.items()):
    out = data['links_out']
    inc = links_in.get(url, [])
    genericas = [l for l in out if l['anchor_type'] == 'genérica']
    ricas = [l for l in out if 'rica' in l['anchor_type']]
    descritivas = [l for l in out if l['anchor_type'] == 'descritiva']
    is_orphan = len(inc) == 0 and url != '/'
    rows.append({
        'url': url,
        'title': data['title'],
        'filepath': data['filepath'],
        'links_out_total': len(out),
        'links_in_total': len(inc),
        'anchor_rica': len(ricas),
        'anchor_descritiva': len(descritivas),
        'anchor_generica': len(genericas),
        'is_orphan': is_orphan,
        'links_in_detail': inc,
        'links_out_detail': out,
    })

orphans = [r for r in rows if r['is_orphan']]
total_pages = len(rows)
total_internal_links = sum(r['links_out_total'] for r in rows)
total_genericas = sum(r['anchor_generica'] for r in rows)


# ── CSV ──────────────────────────────────────────────────────────────────────

csv_path = f'{ROOT}/link-audit.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Título', 'Links Enviados', 'Links Recebidos',
                     'Âncoras Ricas', 'Âncoras Descritivas', 'Âncoras Genéricas', 'Órfã?'])
    for r in rows:
        writer.writerow([
            r['url'], r['title'],
            r['links_out_total'], r['links_in_total'],
            r['anchor_rica'], r['anchor_descritiva'], r['anchor_generica'],
            'SIM' if r['is_orphan'] else ''
        ])

print(f'CSV salvo: {csv_path}')


# ── HTML ─────────────────────────────────────────────────────────────────────

def badge(text, color):
    return f'<span style="background:{color};color:#fff;padding:2px 8px;border-radius:4px;font-size:12px;font-weight:600">{text}</span>'

def anchor_badge(atype):
    colors = {'rica (keyword)': '#1D9648', 'rica (cidade)': '#2563eb', 'descritiva': '#6b7280', 'genérica': '#dc2626'}
    return badge(atype, colors.get(atype, '#6b7280'))

rows_sorted_orphan = sorted(rows, key=lambda r: (not r['is_orphan'], r['links_in_total']))

table_rows = ''
for r in rows_sorted_orphan:
    orphan_badge = badge('ÓRFÃ', '#dc2626') if r['is_orphan'] else ''

    # Tooltip de links recebidos
    inc_detail = ''
    for lk in r['links_in_detail'][:8]:
        inc_detail += f'<div style="font-size:11px;padding:2px 0;border-bottom:1px solid #f0f0f0">{lk["from"]} <span style="color:#6b7280">→</span> {anchor_badge(lk["anchor_type"])} <em>{lk["anchor"][:40]}</em></div>'
    if len(r['links_in_detail']) > 8:
        inc_detail += f'<div style="font-size:11px;color:#6b7280">...+{len(r["links_in_detail"])-8} mais</div>'

    out_detail = ''
    for lk in r['links_out_detail'][:8]:
        out_detail += f'<div style="font-size:11px;padding:2px 0;border-bottom:1px solid #f0f0f0">{lk["href"]} {anchor_badge(lk["anchor_type"])} <em>{lk["anchor"][:40]}</em></div>'
    if len(r['links_out_detail']) > 8:
        out_detail += f'<div style="font-size:11px;color:#6b7280">...+{len(r["links_out_detail"])-8} mais</div>'

    bg = '#fff5f5' if r['is_orphan'] else '#fff'
    table_rows += f'''
    <tr style="background:{bg}" class="page-row" data-orphan="{"1" if r["is_orphan"] else "0"}">
      <td style="font-family:monospace;font-size:12px;color:#1D9648">{r["url"]}</td>
      <td style="font-size:12px;max-width:220px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" title="{r["title"]}">{r["title"][:60]}</td>
      <td style="text-align:center">
        <span class="expandable" onclick="toggle(this)">{r["links_out_total"]} ▾</span>
        <div class="detail" style="display:none;text-align:left;padding:4px;background:#f9f9f9;border:1px solid #eee;margin-top:4px">{out_detail or "<em>nenhum</em>"}</div>
      </td>
      <td style="text-align:center">
        <span class="expandable" onclick="toggle(this)">{r["links_in_total"]} ▾</span>
        <div class="detail" style="display:none;text-align:left;padding:4px;background:#f9f9f9;border:1px solid #eee;margin-top:4px">{inc_detail or "<em>nenhum</em>"}</div>
      </td>
      <td style="text-align:center">{badge(r["anchor_rica"], "#1D9648") if r["anchor_rica"] else "—"}</td>
      <td style="text-align:center">{badge(r["anchor_descritiva"], "#6b7280") if r["anchor_descritiva"] else "—"}</td>
      <td style="text-align:center">{badge(r["anchor_generica"], "#dc2626") if r["anchor_generica"] else "—"}</td>
      <td style="text-align:center">{orphan_badge}</td>
    </tr>'''

orphan_list = ''.join(f'<li><code>{r["url"]}</code> — {r["title"][:60]}</li>' for r in orphans)

html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Link Audit — Move Máquinas</title>
<style>
  body {{ font-family: Inter, sans-serif; margin: 0; background: #f5f5f5; color: #222; }}
  .header {{ background: #1D9648; color: white; padding: 20px 32px; }}
  .header h1 {{ margin: 0; font-size: 22px; }}
  .header p {{ margin: 4px 0 0; opacity: .8; font-size: 13px; }}
  .container {{ max-width: 1400px; margin: 0 auto; padding: 24px; }}
  .cards {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; margin-bottom: 24px; }}
  .card {{ background: #fff; border-radius: 8px; padding: 16px 20px; box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
  .card .num {{ font-size: 28px; font-weight: 700; color: #1D9648; }}
  .card .label {{ font-size: 12px; color: #6b7280; margin-top: 2px; }}
  .card.warn .num {{ color: #dc2626; }}
  table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
  th {{ background: #1D9648; color: #fff; padding: 10px 12px; text-align: left; font-size: 12px; font-weight: 600; }}
  td {{ padding: 8px 12px; border-bottom: 1px solid #f0f0f0; vertical-align: top; }}
  tr:last-child td {{ border-bottom: none; }}
  .expandable {{ cursor: pointer; color: #1D9648; font-weight: 600; text-decoration: underline dotted; }}
  .filters {{ margin-bottom: 16px; display: flex; gap: 12px; align-items: center; }}
  .filters button {{ padding: 6px 14px; border: 1px solid #ddd; border-radius: 6px; cursor: pointer; background: #fff; font-size: 13px; }}
  .filters button.active {{ background: #1D9648; color: #fff; border-color: #1D9648; }}
  .orphan-section {{ background: #fff; border-radius: 8px; padding: 20px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
  .orphan-section h2 {{ margin: 0 0 12px; font-size: 16px; color: #dc2626; }}
  .orphan-section li {{ font-size: 13px; padding: 3px 0; }}
  code {{ background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 12px; }}
  input[type=text] {{ padding: 7px 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 13px; width: 280px; }}
</style>
</head>
<body>
<div class="header">
  <h1>Link Audit — Move Máquinas</h1>
  <p>Gerado em {datetime.now().strftime("%d/%m/%Y %H:%M")} · {total_pages} páginas · {total_internal_links} links internos</p>
</div>
<div class="container">

  <div class="cards">
    <div class="card"><div class="num">{total_pages}</div><div class="label">Páginas analisadas</div></div>
    <div class="card"><div class="num">{total_internal_links}</div><div class="label">Links internos totais</div></div>
    <div class="card warn"><div class="num">{len(orphans)}</div><div class="label">Páginas órfãs</div></div>
    <div class="card warn"><div class="num">{total_genericas}</div><div class="label">Âncoras genéricas</div></div>
    <div class="card"><div class="num">{sum(r["anchor_rica"] for r in rows)}</div><div class="label">Âncoras ricas (keyword/cidade)</div></div>
  </div>

  {"" if not orphans else f"""
  <div class="orphan-section">
    <h2>⚠ Páginas Órfãs ({len(orphans)}) — sem nenhum link recebido</h2>
    <ul>{orphan_list}</ul>
  </div>
  """}

  <div class="filters">
    <input type="text" id="search" placeholder="Filtrar por URL ou título..." oninput="filterTable()">
    <button class="active" onclick="setFilter('all', this)">Todas</button>
    <button onclick="setFilter('orphan', this)">Só Órfãs</button>
    <button onclick="setFilter('no-orphan', this)">Sem Órfãs</button>
  </div>

  <table id="main-table">
    <thead>
      <tr>
        <th>URL</th>
        <th>Título</th>
        <th>Links Enviados</th>
        <th>Links Recebidos</th>
        <th>Ricas KW</th>
        <th>Descritivas</th>
        <th>Genéricas</th>
        <th>Órfã?</th>
      </tr>
    </thead>
    <tbody>{table_rows}</tbody>
  </table>
</div>

<script>
function toggle(el) {{
  const detail = el.nextElementSibling;
  detail.style.display = detail.style.display === 'none' ? 'block' : 'none';
}}

let currentFilter = 'all';

function setFilter(type, btn) {{
  currentFilter = type;
  document.querySelectorAll('.filters button').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filterTable();
}}

function filterTable() {{
  const q = document.getElementById('search').value.toLowerCase();
  document.querySelectorAll('#main-table .page-row').forEach(row => {{
    const url = row.cells[0].textContent.toLowerCase();
    const title = row.cells[1].textContent.toLowerCase();
    const isOrphan = row.dataset.orphan === '1';
    const matchSearch = !q || url.includes(q) || title.includes(q);
    const matchFilter = currentFilter === 'all' ||
      (currentFilter === 'orphan' && isOrphan) ||
      (currentFilter === 'no-orphan' && !isOrphan);
    row.style.display = matchSearch && matchFilter ? '' : 'none';
  }});
}}
</script>
</body>
</html>'''

html_path = f'{ROOT}/link-audit.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'HTML salvo: {html_path}')
print(f'\n=== RESUMO ===')
print(f'Páginas: {total_pages}')
print(f'Links internos: {total_internal_links}')
print(f'Órfãs: {len(orphans)}')
print(f'Âncoras genéricas: {total_genericas}')
print(f'Âncoras ricas: {sum(r["anchor_rica"] for r in rows)}')
if orphans:
    print(f'\nÓrfãs:')
    for r in orphans:
        print(f'  {r["url"]}')
