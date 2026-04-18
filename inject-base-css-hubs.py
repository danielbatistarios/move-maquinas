#!/usr/bin/env python3
"""
inject-base-css-hubs.py — Injeta o bloco <style> base (design tokens, reset, layout)
nos 13 hubs de cidade, que só tinham CSS de componentes mas faltavam as variáveis base.
"""
import os, re

ROOT = '/Users/jrios/move-maquinas-seo'

HUBS = [
    'goiania-go', 'senador-canedo-go', 'brasilia-df', 'luziania-go',
    'trindade-go', 'inhumas-go', 'itumbiara-go', 'caldas-novas-go',
    'formosa-go', 'uruacu-go', 'valparaiso-de-goias-go',
    'aparecida-de-goiania-go', 'anapolis-go',
]

BASE_CSS = '''<style>
@font-face{font-family:'Inter';font-style:normal;font-weight:400 900;font-display:swap;src:url('/assets/fonts/inter-latin-w400.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
:root{--color-primary:#1D9648;--color-primary-btn:#16A149;--color-primary-dark:#158b3e;--color-dark:#1A1A1A;--color-text:#1a1a1a;--color-text-light:#4a5568;--color-muted:#718096;--color-surface:#f8fafb;--color-white:#ffffff;--color-border:#e2e8f0;--color-whatsapp:#25D366;--color-whatsapp-hover:#1fb855;--color-alert:#DC2626;--font-family:'Inter',system-ui,-apple-system,sans-serif;--font-h1:clamp(1.75rem,4vw,2.5rem);--font-h2:clamp(1.35rem,3vw,1.875rem);--font-h3:clamp(1.05rem,2.5vw,1.2rem);--font-body:1rem;--font-small:0.9rem;--font-caption:0.8rem;--space-xs:8px;--space-sm:16px;--space-md:24px;--space-lg:32px;--space-xl:80px;--space-2xl:96px;--radius:8px;--radius-lg:12px;--shadow-sm:0 1px 3px rgba(0,0,0,.08);--shadow-md:0 4px 12px rgba(0,0,0,.10);--shadow-lg:0 8px 24px rgba(0,0,0,.14);--container:1140px}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font-family);color:var(--color-text);line-height:1.7;background:var(--color-white);overflow-x:hidden}
img{max-width:100%;height:auto;display:block}
a{color:inherit}
ul{list-style:none}
address{font-style:normal}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
:focus-visible{outline:3px solid var(--color-primary);outline-offset:3px;border-radius:4px}
.container{max-width:var(--container);margin:0 auto;padding:0 var(--space-md)}
.scroll-progress{position:fixed;top:0;left:0;height:3px;background:var(--color-primary);z-index:9999;width:0%;transition:width .1s linear;pointer-events:none}
.reveal{opacity:0;transform:translateY(24px);transition:opacity .6s cubic-bezier(.22,1,.36,1),transform .6s cubic-bezier(.22,1,.36,1)}
.reveal.is-visible{opacity:1;transform:translateY(0)}
.reveal-stagger{transition-delay:calc(var(--stagger,0)*80ms)}
.breadcrumb{background:var(--color-surface);border-bottom:1px solid var(--color-border);padding:12px 0}
.breadcrumb__list{display:flex;align-items:center;gap:8px;list-style:none;flex-wrap:wrap;font-size:var(--font-caption);color:var(--color-muted)}
.breadcrumb__list li:not(:last-child)::after{content:"/";margin-left:8px;color:var(--color-border)}
.breadcrumb__list a{color:var(--color-primary);text-decoration:none}
.page-section{padding:var(--space-xl) 0}
.page-section--surface{background:var(--color-surface)}
.page-section--dark{background:var(--color-dark);color:var(--color-white)}
.section-tag{display:inline-flex;align-items:center;gap:6px;background:#f0fdf4;color:var(--color-primary);font-size:var(--font-caption);font-weight:700;padding:4px 12px;border-radius:100px;margin-bottom:var(--space-sm);text-transform:uppercase;letter-spacing:.06em;border:1px solid #bbf7d0}
.section-tag--white{background:rgba(255,255,255,.15);color:var(--color-white);border-color:rgba(255,255,255,.3)}
h1{font-size:var(--font-h1);font-weight:900;line-height:1.15;color:var(--color-dark)}
h2{font-size:var(--font-h2);font-weight:800;line-height:1.25;color:var(--color-dark);margin-bottom:var(--space-md)}
h2 span{color:var(--color-primary)}
h3{font-size:var(--font-h3);font-weight:700;line-height:1.3;color:var(--color-dark)}
p{color:var(--color-text-light);line-height:1.8}
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 24px;border-radius:var(--radius);font-size:1rem;font-weight:700;text-decoration:none;cursor:pointer;border:none;transition:transform .15s,box-shadow .15s,background .15s;min-height:48px;line-height:1;font-family:var(--font-family)}
.btn:hover{transform:translateY(-1px);box-shadow:var(--shadow-md)}
.btn--primary{background:var(--color-primary-btn);color:#fff}
.btn--primary:hover{background:var(--color-primary-dark)}
.hero{background:var(--color-dark);color:var(--color-white);overflow:hidden;position:relative}
.hero__bg{position:absolute;inset:0;z-index:0}
.hero__bg img{width:100%;height:100%;object-fit:cover;opacity:0.25}
.hero__layout{display:grid;grid-template-columns:1fr 400px;gap:var(--space-2xl);align-items:center;min-height:480px;padding:var(--space-xl) 0;position:relative;z-index:1}
.hero h1{color:var(--color-white);margin-bottom:var(--space-md)}
.hero h1 em{color:var(--color-primary);font-style:normal}
.hero__lead{font-size:1.05rem;color:rgba(255,255,255,.85);margin-bottom:var(--space-sm);line-height:1.8}
.hero__actions{display:flex;gap:var(--space-sm);flex-wrap:wrap;align-items:start;margin-bottom:var(--space-lg)}
.hero__card{background:var(--color-white);border-radius:var(--radius-lg);padding:var(--space-lg);box-shadow:var(--shadow-lg);color:var(--color-text)}
.hero__card-title{color:var(--color-text);margin-bottom:var(--space-md);font-size:1.1rem;font-weight:700}
.hero__card-field{margin-bottom:var(--space-md)}
.hero__card-field label{display:block;font-size:var(--font-small);font-weight:700;color:var(--color-muted);margin-bottom:4px;text-transform:uppercase;letter-spacing:.04em}
.hero__card-field select,.hero__card-field input{width:100%;padding:10px var(--space-md);border:1.5px solid var(--color-border);border-radius:var(--radius);font-family:var(--font-family);font-size:var(--font-body);color:var(--color-text);background:var(--color-white);transition:border-color .2s;appearance:auto}
.hero__card-field select:focus,.hero__card-field input:focus{border-color:var(--color-primary);outline:none}
.hero__card .btn{width:100%;justify-content:center}
.hero__card-note{font-size:var(--font-caption);color:var(--color-muted);text-align:center;margin-top:var(--space-sm)}
@media(max-width:768px){.hero__layout{grid-template-columns:1fr}.hero__card{display:none}}
</style>'''

MARKER = '<link rel="stylesheet" href="styles-cbb654b2.css">'

print('=== Injetando CSS base nos hubs ===\n')
for slug in HUBS:
    fp = os.path.join(ROOT, slug, 'index.html')
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    if BASE_CSS.strip()[:50] in content:
        print(f'  SKIP (já tem): {slug}')
        continue

    if MARKER not in content:
        print(f'  ERRO (marker não encontrado): {slug}')
        continue

    content = content.replace(MARKER, MARKER + '\n' + BASE_CSS)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  OK: {slug}')

print('\nDone.')
