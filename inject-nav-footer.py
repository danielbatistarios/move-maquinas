#!/usr/bin/env python3
"""
Injeta o novo megamenu (mm-nav) e footer (mm-ft) em todas as paginas HTML.

Substituicoes:
  1. <header class="hdr">...</header>  →  novo <header class="mm-nav"> + mobile overlay
  2. <footer class="ft">...</footer>   →  novo <footer class="mm-ft">
  3. Injeta CSS (bloco <style id="nav-footer-css">) antes de </style> no <head>
  4. Injeta JS antes de </body>

Protege:
  - <footer role="contentinfo"> (formulario/CTA) — NAO toca

Flags:
  --dry-run   nao modifica arquivos, apenas lista o que seria alterado
  --force     remove blocos existentes de nav-footer-css/js antes de re-injetar (v2 update)
  --pilot     processa apenas goiania-go/index.html
"""

import re
import sys
import glob
import os

DRY_RUN = '--dry-run' in sys.argv
FORCE   = '--force' in sys.argv
PILOT   = '--pilot' in sys.argv

ROOT = '/Users/jrios/move-maquinas-seo'
NAV_FOOTER = os.path.join(ROOT, 'assets/nav-footer.html')

# ── Ler componente ────────────────────────────────────────────────────────────
with open(NAV_FOOTER, encoding='utf-8') as f:
    raw = f.read()

# CSS (entre <style id="nav-footer-css"> e </style>)
css_match = re.search(r'<style id="nav-footer-css">(.*?)</style>', raw, re.DOTALL)
CSS_BLOCK = css_match.group(0) if css_match else ''

# Header (de <header class="mm-nav" até </header>)
header_match = re.search(r'<header class="mm-nav".*?</header>', raw, re.DOTALL)
HEADER_NEW = header_match.group(0) if header_match else ''

# Mobile overlay (de <div class="mm-mob" até o segundo </div> que fecha o overlay)
mob_match = re.search(r'<div class="mm-mob".*?</div>\s*\n\s*\n', raw, re.DOTALL)
MOB_NEW = mob_match.group(0).rstrip() if mob_match else ''

# Footer (de <footer class="mm-ft" até </footer>)
footer_match = re.search(r'<footer class="mm-ft".*?</footer>', raw, re.DOTALL)
FOOTER_NEW = footer_match.group(0) if footer_match else ''

# JS (de <script id="nav-footer-js"> até </script>)
js_match = re.search(r'<script id="nav-footer-js">.*?</script>', raw, re.DOTALL)
JS_BLOCK = js_match.group(0) if js_match else ''

print(f'CSS: {len(CSS_BLOCK)} chars')
print(f'Header: {len(HEADER_NEW)} chars')
print(f'Mobile overlay: {len(MOB_NEW)} chars')
print(f'Footer: {len(FOOTER_NEW)} chars')
print(f'JS: {len(JS_BLOCK)} chars')

if not all([CSS_BLOCK, HEADER_NEW, FOOTER_NEW, JS_BLOCK]):
    print('ERRO: componente incompleto — verifique nav-footer.html')
    sys.exit(1)

# ── Padroes ───────────────────────────────────────────────────────────────────

# Antigo header: hdr, page-header ou qualquer <header> sem mm-nav/mm-mob
OLD_HEADER_PAT = re.compile(
    r'<header\s+class="(?:hdr|page-header)"[^>]*>.*?</header>',
    re.DOTALL
)

# Ponto de injeção de header quando não existe nenhum: logo após <body...>
BODY_OPEN_PAT = re.compile(r'(<body[^>]*>)', re.DOTALL)

# Header mm-nav existente (para --force)
MM_HEADER_PAT = re.compile(r'<header class="mm-nav".*?</header>\s*\n*\s*<div class="mm-mob".*?</div>', re.DOTALL)
MM_HEADER_ONLY_PAT = re.compile(r'<header class="mm-nav".*?</header>', re.DOTALL)

# Mobile overlay existente (para --force)
MM_MOB_PAT = re.compile(r'<div class="mm-mob".*?(?:</div>\s*){2}', re.DOTALL)

# Antigo footer nav (todas as variações conhecidas)
# Protege <footer role="contentinfo"> (formulário CTA) — não toca
OLD_FOOTER_PAT = re.compile(
    r'<footer(?:\s+class="(?:ft|ft-std|footer)")?(?!\s+role="contentinfo")(?!\s+class="mm-ft")[^>]*>.*?</footer>',
    re.DOTALL
)

# Footer simples sem classe: <footer>...</footer> (páginas de manutenção/peças)
# Alias para reutilizar o mesmo padrão acima (já cobre <footer>)

# Footer mm-ft existente (para --force)
MM_FOOTER_PAT = re.compile(r'<footer class="mm-ft".*?</footer>', re.DOTALL)

# CSS bloco existente (para --force)
OLD_CSS_PAT = re.compile(r'<style id="nav-footer-css">.*?</style>\s*\n?', re.DOTALL)

# JS bloco existente (para --force)
OLD_JS_PAT = re.compile(r'<script id="nav-footer-js">.*?</script>\s*\n?', re.DOTALL)

# CSS injection point: antes de </style> no head (primeira ocorrencia)
CSS_INJECT_PAT = re.compile(r'(</style>)', re.DOTALL)

# JS injection: antes de </body>
JS_INJECT_PAT = re.compile(r'(</body>)', re.DOTALL)

# ── Encontrar arquivos ────────────────────────────────────────────────────────
html_files = sorted(
    glob.glob(os.path.join(ROOT, '**/index.html'), recursive=True) +
    glob.glob(os.path.join(ROOT, '404.html'))
)

# Excluir assets, nav-footer e templates
html_files = [
    f for f in html_files
    if '/assets/' not in f
    and 'nav-footer' not in f
]

if PILOT:
    html_files = [f for f in html_files if 'goiania-go/index.html' in f]

print(f'\nArquivos encontrados: {len(html_files)}')
if DRY_RUN:
    print('MODO DRY-RUN — nenhum arquivo sera modificado\n')
if FORCE:
    print('MODO FORCE — blocos existentes serao substituidos\n')

changed = 0
skipped = 0
errors = []

for fpath in html_files:
    rel = os.path.relpath(fpath, ROOT)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # ── FORCE: remover blocos antigos para permitir re-injecao ────────────────
    if FORCE:
        # Remover CSS antigo
        if 'nav-footer-css' in content:
            content = OLD_CSS_PAT.sub('', content)

        # Remover JS antigo
        if 'nav-footer-js' in content:
            content = OLD_JS_PAT.sub('', content)

        # Substituir header mm-nav existente + mobile overlay
        if 'mm-nav' in content:
            # Tenta substituir header + mob juntos (com newlines entre eles)
            combined = re.search(
                r'<header class="mm-nav".*?</header>\s*\n+\s*<div class="mm-mob".*?</div>\s*\n+\s*\n',
                content, re.DOTALL
            )
            if combined:
                content = content[:combined.start()] + HEADER_NEW + '\n\n' + MOB_NEW + '\n\n' + content[combined.end():]
                changes.append('header+mob(force)')
            else:
                # Tenta só header
                content = MM_HEADER_ONLY_PAT.sub(HEADER_NEW, content, count=1)
                changes.append('header(force)')

        # Substituir footer mm-ft existente
        if 'mm-ft' in content:
            content = MM_FOOTER_PAT.sub(FOOTER_NEW, content, count=1)
            changes.append('footer(force)')

    # ── Substituicoes normais ─────────────────────────────────────────────────

    # 1. Substituir header antigo (apenas se nao foi handled pelo force acima)
    if 'header+mob(force)' not in changes and 'header(force)' not in changes:
        if OLD_HEADER_PAT.search(content):
            content = OLD_HEADER_PAT.sub(HEADER_NEW + '\n\n' + MOB_NEW, content, count=1)
            changes.append('header')
        else:
            if 'mm-nav' not in content:
                # Nao ha header antigo nem mm-nav — injetar logo apos <body>
                if BODY_OPEN_PAT.search(content):
                    content = BODY_OPEN_PAT.sub(r'\1\n' + HEADER_NEW + '\n\n' + MOB_NEW, content, count=1)
                    changes.append('header(body-inject)')
                else:
                    errors.append(f'SEM HEADER: {rel}')

    # 2. Substituir footer antigo (apenas se nao foi handled pelo force)
    if 'footer(force)' not in changes:
        if OLD_FOOTER_PAT.search(content):
            content = OLD_FOOTER_PAT.sub(FOOTER_NEW, content, count=1)
            changes.append('footer')
        else:
            if 'mm-ft' not in content:
                errors.append(f'SEM FOOTER: {rel}')

    # 3. Injetar CSS (apenas se nao tiver ainda)
    if 'nav-footer-css' not in content:
        content = CSS_INJECT_PAT.sub(CSS_BLOCK + '\n\\1', content, count=1)
        changes.append('css')

    # 4. Injetar JS (apenas se nao tiver ainda)
    if 'nav-footer-js' not in content:
        content = JS_INJECT_PAT.sub(JS_BLOCK + '\n\\1', content, count=1)
        changes.append('js')

    if changes:
        if not DRY_RUN:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f'[OK] {rel}  ({", ".join(changes)})')
        changed += 1
    else:
        print(f'[--] {rel}  (sem mudancas)')
        skipped += 1

print(f'\n{"="*60}')
print(f'Modificados : {changed}')
print(f'Sem mudanca : {skipped}')
if errors:
    print(f'\nAVISOS ({len(errors)}):')
    for e in errors:
        print(f'  {e}')
if DRY_RUN:
    print('\n[DRY-RUN] Nenhum arquivo foi modificado.')
