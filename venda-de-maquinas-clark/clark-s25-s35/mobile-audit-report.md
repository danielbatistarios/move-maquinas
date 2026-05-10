# Mobile Audit — index-v2.html (Clark S25-S35)
**Data:** 2026-05-10 | **Score:** 77/100 — Bom

---

## Score por Área

| Área | Score | Status |
|------|-------|--------|
| Viewport | 10/10 | OK |
| Header/Nav | 11/15 | Burger toque pequeno, sem aria, sem scroll-padding-top |
| Layout | 16/20 | canal-grid sem breakpoint tablet, 2 seções com padding px fixo |
| Touch Targets | 10/15 | Burger 38px, footer socials 36px, form inputs ~42px |
| Tipografia | 12/15 | qs-label 10px, body 14px fixo em muitos lugares |
| Efeitos/Touch | 6/10 | hover sem @media(hover:hover) em 8+ elementos, sem prefers-reduced-motion |
| Performance | 8/10 | Sem preload Inter, marquee loop infinito sem pausa |
| Footer | 4/5 | Social icons 36px (abaixo de 44px) |
| **TOTAL** | **77/100** | **Bom — aplicar P1s** |

---

## P1 — Altos (7 problemas)

- **[Efeitos]** `:hover` em `.feature-box`, `.vid-card`, `.related-card`, `.gallery-main`, `.gallery-thumb`, `.fuel-photo`, `.sector-card`, `.factor-card` sem `@media(hover:hover)` — gruda no elemento após tap em touch screen → envolver em `@media(hover:hover)`

- **[Nav]** `.nav-burger` com `padding:8px` → área de toque 38px, abaixo de 44px mínimo → `min-width:44px;min-height:44px;padding:11px`

- **[Âncoras]** Sem `scroll-padding-top` — links âncora (#visao-geral, #video, etc.) ficam escondidos atrás da nav fixa (~52px) + tabs-nav sticky (~50px) → `html{scroll-padding-top:110px}`

- **[Tipografia]** `.qs-label{font-size:10px}` — ilegível em mobile, mínimo 12px → `font-size:12px`

- **[Layout]** `.canal-grid{grid-template-columns:repeat(3,1fr)}` sem breakpoint para tablet (769-1024px) — 3 colunas apertadas → adicionar breakpoint 2 colunas em 900px

- **[Forms]** `.orc-group input{padding:11px 14px}` → altura ~42px, abaixo de 48px recomendado → `padding:13px 14px`

- **[Animações]** Sem `@media(prefers-reduced-motion:reduce)` — marquee infinito e reveal animations ativas para usuários com vestibular disorders → adicionar bloco de reduced-motion

## P2 — Melhorias (3)

- **[Performance]** Sem `<link rel="preload">` para Inter — adicionar `<link rel="preload" href="..." as="font">`

- **[Galeria]** `gallery-sidebar` sem `scroll-snap-type` — scroll de thumbs sem snap → `scroll-snap-type:x mandatory` + `scroll-snap-align:start` nos thumbs

- **[Spacing]** `.fuel-compare-section` e `.decisoes-section` com `padding:80px 0` fixo → converter para `clamp(48px,7vw,80px) 0`

---

## Como aplicar o patch

Adicione antes do `</head>` no HTML:
```html
<link rel="stylesheet" href="mobile-patch.css">
```
