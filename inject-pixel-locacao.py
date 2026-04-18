"""
Injeta Facebook Pixel + UTM capture + evento Lead nas LPs de Locação.
Pixel ID: 1089167330085055
"""

import os
import re
import glob

DIR = os.path.dirname(os.path.abspath(__file__))

# Arquivos de locação (excluindo TPL, ref-, blog-)
PATTERNS = [
    "**/*aluguel-de-empilhadeira*.html",
    "**/*aluguel-de-plataforma*.html",
    "**/*aluguel-de-transpaleteira*.html",
]
EXCLUDE = {"-TPL.", "ref-", "blog-"}

# ── Bloco A: UTM capture ──────────────────────────────────────────────────────
BLOCO_A = """<script>(function(){
  var p=new URLSearchParams(window.location.search),k=['utm_source','utm_medium','utm_campaign','utm_content','utm_term'],s=JSON.parse(sessionStorage.getItem('utm_data')||'{}'),n=false;
  k.forEach(function(x){if(p.get(x)){s[x]=p.get(x);n=true;}});
  if(n){sessionStorage.setItem('utm_data',JSON.stringify(s));}
  else if(!s.utm_source){
    var ref=document.referrer,h=ref?new URL(ref).hostname:'';
    if(/google\./i.test(h)){s.utm_source='google';s.utm_medium='organic';}
    else if(/bing\.|yahoo\.|duckduckgo\./i.test(h)){s.utm_source='microsoft';s.utm_medium='organic';}
    else if(/facebook\.|fb\./i.test(h)){s.utm_source='facebook';s.utm_medium='social';}
    else if(/instagram\./i.test(h)){s.utm_source='instagram';s.utm_medium='social';}
    else if(/tiktok\./i.test(h)){s.utm_source='tiktok';s.utm_medium='social';}
    else if(/linkedin\./i.test(h)){s.utm_source='linkedin';s.utm_medium='social';}
    else if(ref){s.utm_source='referral';s.utm_medium='referral';}
    else{s.utm_source='direct';s.utm_medium='organic';}
    sessionStorage.setItem('utm_data',JSON.stringify(s));
  }
})();</script>"""

# ── Bloco B: Meta Pixel ───────────────────────────────────────────────────────
BLOCO_B = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1089167330085055');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1089167330085055&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

INJECTION_HEAD = BLOCO_A + "\n" + BLOCO_B + "\n"

# ── Bloco C: getUtmData helper + evento Lead + CRM ───────────────────────────
# Inserido ANTES de window.open(...) dentro de handleQuoteForm
# Padrão a substituir (captura a linha do window.open)
WINDOW_OPEN_RE = re.compile(
    r"([ \t]*)(window\.open\('https://wa\.me/[^']+'\s*\+\s*encodeURIComponent\(msg\)[^;]*;)",
    re.MULTILINE,
)

def build_bloco_c(indent: str) -> str:
    return f"""{indent}var _utms = (function(){{ try {{ return JSON.parse(sessionStorage.getItem('utm_data')||'{{}}'); }} catch(e){{ return {{}}; }} }})();
{indent}var _crmMediumMap = {{ cpc:'paid',ppc:'paid',paid:'paid',paid_social:'paid',banner:'paid',display:'paid',organic:'organic',referral:'organic',email:'organic',social:'organic' }};
{indent}var _crmMedium = _crmMediumMap[_utms.medium] || 'organic';
{indent}var _crmSourceMap = {{ google:'google','google-ads':'google',googleads:'google',meta:'meta',facebook:'meta',instagram:'meta',tiktok:'tiktok',linkedin:'linkedin',microsoft:'microsoft',bing:'microsoft',email:'email',referral:'referral',partner:'partner',offline:'offline',outbound:'outbound',organic:'organic',direct:'direct' }};
{indent}var _crmSource = _crmSourceMap[_utms.source] || (_utms.source && _utms.source !== 'direct' ? 'referral' : 'direct');
{indent}var _crmChannelMap = {{ google:'google','google-ads':'google',googleads:'google',microsoft:'google',meta:'facebook',facebook:'facebook',instagram:'instagram',tiktok:'tiktok',linkedin:'linkedin',email:'email',phone:'phone',referral:'other',organic:'other',direct:'other' }};
{indent}var _crmChannel = _crmChannelMap[_utms.source] || 'other';
{indent}var _isPaid = _crmMedium === 'paid';
{indent}var _segMap = {{ google: _isPaid ? 'locacao-google-ads' : 'locacao-google-organico', microsoft: _isPaid ? 'locacao-google-ads' : 'locacao-google-organico', facebook: _isPaid ? 'locacao-facebook-ads' : 'locacao-facebook-organico', meta: _isPaid ? 'locacao-facebook-ads' : 'locacao-facebook-organico', instagram: _isPaid ? 'locacao-instagram-ads' : 'locacao-instagram-organico', tiktok: 'locacao-tiktok', linkedin: 'locacao-linkedin', email: 'locacao-email', referral: 'locacao-referral' }};
{indent}var _crmSegment = _segMap[_utms.source] || (_utms.source && _utms.source !== 'direct' ? 'locacao-outro' : 'locacao-direto');
{indent}var _leadName = (typeof nome !== 'undefined' ? nome : '') || '';
{indent}var _leadTel = (typeof tel !== 'undefined' ? tel : '') || '';
{indent}var _leadDesc = 'Locacao | ' + (_utms.source && _utms.source !== 'direct' ? 'Source: ' + _utms.source : 'Direto') + (_utms.medium && _utms.medium !== 'organic' ? ' | Medium: ' + _utms.medium : '') + (_utms.campaign ? ' | Campanha: ' + _utms.campaign : '');
{indent}var _waUrl = 'https://wa.me/5562982637300?text=' + encodeURIComponent(msg);
{indent}var _btn = btn;
{indent}var _btnOriginal = _btn ? _btn.innerHTML : null;
{indent}if (_btn) {{ _btn.disabled = true; _btn.textContent = 'Enviando...'; }}
{indent}function _abrir() {{
{indent}  if (typeof fbq === 'function') {{
{indent}    fbq('track', 'Lead', {{ content_name: 'Locação de Empilhadeira', content_category: 'locacao', value: 0, currency: 'BRL' }});
{indent}  }}
{indent}  window.open(_waUrl, '_blank', 'noopener,noreferrer');
{indent}  if (_btn) {{ _btn.disabled = false; _btn.innerHTML = _btnOriginal; }}
{indent}}}
{indent}fetch('https://backend.umdhub.com.br/api/leads/public/69b2f6d262e629a2c7a8d35a', {{
{indent}  method: 'POST', keepalive: true,
{indent}  headers: {{ 'Content-Type': 'application/json', 'X-API-Key': 'sk_live_719213e5f48228a63a4be9aa357a65dc5568f3b740008a98d14b58229d1f7150' }},
{indent}  body: JSON.stringify({{ segment: _crmSegment, description: _leadDesc, source: _crmSource, medium: _crmMedium, channel: _crmChannel, priority: 'medium', temperature: 'cold', qualifyStatus: 'pending', budget: 0, name: _leadName, company: '', position: '', emails: [], phones: [_leadTel] }})
{indent}}})
{indent}.then(_abrir).catch(_abrir);
{indent}return;"""


def collect_files() -> list[str]:
    files = set()
    for pat in PATTERNS:
        for f in glob.glob(os.path.join(DIR, pat), recursive=True):
            basename = os.path.basename(f)
            if any(ex in basename for ex in EXCLUDE):
                continue
            files.add(f)
    return sorted(files)


def inject_head(html: str) -> tuple[str, bool]:
    """Injeta blocos A+B antes de </head>. Retorna (html, changed)."""
    if "fbq('init'" in html:
        return html, False
    new_html = html.replace("</head>", INJECTION_HEAD + "</head>", 1)
    return new_html, new_html != html


def inject_bloco_c(html: str) -> tuple[str, bool]:
    """Substitui window.open simples pelo bloco C com Lead + CRM + keepalive."""
    if "_abrir()" in html or "fbq('track', 'Lead'" in html:
        return html, False

    match = WINDOW_OPEN_RE.search(html)
    if not match:
        return html, False

    indent = match.group(1)
    bloco_c = build_bloco_c(indent)
    # Remove a linha original do window.open (já está dentro de _abrir())
    new_html = WINDOW_OPEN_RE.sub(bloco_c, html, count=1)
    return new_html, new_html != html


def process_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        html = f.read()

    html, changed_head = inject_head(html)
    html, changed_body = inject_bloco_c(html)

    if changed_head or changed_body:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return "OK"
    return "SKIP"


def main():
    files = collect_files()
    print(f"Arquivos encontrados: {len(files)}")
    ok = skip = err = 0
    for path in files:
        try:
            result = process_file(path)
            basename = os.path.basename(path)
            if result == "OK":
                ok += 1
                print(f"  [OK]   {basename}")
            else:
                skip += 1
                print(f"  [SKIP] {basename}")
        except Exception as e:
            err += 1
            print(f"  [ERR]  {os.path.basename(path)}: {e}")

    print(f"\nResumo: {ok} modificados | {skip} ignorados | {err} erros")


if __name__ == "__main__":
    main()
