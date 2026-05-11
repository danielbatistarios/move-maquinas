#!/usr/bin/env node
/**
 * qa-pdp.mjs — QA automatizado para PDPs Clark / Move Maquinas
 * Uso: node qa-pdp.mjs clark-swx16/index.html
 *
 * Referencia: clark-s25-s35/index-v2.html
 * Score: cada check vale 1 ponto. Total exibido ao final.
 */

import { readFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dir = dirname(fileURLToPath(import.meta.url));

// ── Args ────────────────────────────────────────────────────────────────────
const arg = process.argv[2];
if (!arg) {
  console.error('Uso: node qa-pdp.mjs <path-relativo-ao-script>');
  console.error('Ex:  node qa-pdp.mjs clark-swx16/index.html');
  process.exit(1);
}

const filePath = resolve(__dir, arg);
let html;
try {
  html = readFileSync(filePath, 'utf8');
} catch {
  console.error(`Arquivo nao encontrado: ${filePath}`);
  process.exit(1);
}

// ── Helpers ─────────────────────────────────────────────────────────────────
const results = [];
let pass = 0;
let fail = 0;

function check(label, condition, hint = '') {
  const ok = Boolean(condition);
  if (ok) pass++; else fail++;
  results.push({ ok, label, hint });
}

const has    = (str) => html.includes(str);
const hasRe  = (re)  => re.test(html);
const count  = (str) => html.split(str).length - 1;

// ── BLOCO 1: HEAD ────────────────────────────────────────────────────────────
console.log('\n\x1b[1m━━━ QA PDP Clark — ' + arg + ' ━━━\x1b[0m\n');

check(
  '[HEAD] mobile-patch.css linkado',
  has('href="mobile-patch.css"'),
  'Adicionar <link rel="stylesheet" href="mobile-patch.css"> antes do </head>'
);

check(
  '[HEAD] <meta name="viewport"> presente',
  has('name="viewport"'),
  'Adicionar <meta name="viewport" content="width=device-width,initial-scale=1">'
);

check(
  '[HEAD] <meta name="description"> presente',
  has('name="description"'),
);

check(
  '[HEAD] <link rel="canonical"> presente',
  has('rel="canonical"'),
);

check(
  '[HEAD] Open Graph og:title presente',
  has('property="og:title"'),
);

check(
  '[HEAD] JSON-LD Product schema presente',
  has('"@type": "Product"') || has('"@type":"Product"'),
  'Adicionar script type="application/ld+json" com @type Product'
);

check(
  '[HEAD] Fonte Inter linkada (Google Fonts)',
  has('fonts.googleapis.com') && has('Inter'),
);

// ── BLOCO 2: ESTRUTURA SEMÂNTICA ─────────────────────────────────────────────
check(
  '[SEM] <main id="conteudo-principal"> presente',
  has('id="conteudo-principal"'),
  'Envolver todo o conteudo entre header e footer em <main id="conteudo-principal">'
);

check(
  '[SEM] Comentario <!-- HEADER --> presente',
  has('<!-- HEADER -->'),
  'Adicionar comentario <!-- HEADER --> antes da nav'
);

check(
  '[SEM] Comentario <!-- /HEADER --> presente',
  has('<!-- /HEADER -->'),
);

check(
  '[SEM] Comentario <!-- FOOTER --> presente',
  has('<!-- FOOTER -->'),
);

check(
  '[SEM] Comentario <!-- /FOOTER --> presente',
  has('<!-- /FOOTER -->'),
);

check(
  '[SEM] nav aria-label="Principal" presente',
  has('aria-label="Principal"'),
  'Adicionar aria-label="Principal" na <nav> da navbar'
);

check(
  '[SEM] nav aria-label="Abas de produto" presente',
  has('aria-label="Abas de produto"'),
  'Adicionar aria-label="Abas de produto" no prod-tabs-nav'
);

// ── BLOCO 3: SEÇÕES OBRIGATÓRIAS ─────────────────────────────────────────────
const sections = [
  ['[SEC] Hero (.hero)',                    '.hero'],
  ['[SEC] Video (#video)',                  'id="video"'],
  ['[SEC] Tabs Nav (.prod-tabs-nav)',       'class="prod-tabs-nav"'],
  ['[SEC] Visao Geral (#visao-geral)',      'id="visao-geral"'],
  ['[SEC] Quick Specs (#caracteristicas)', 'id="caracteristicas"'],
  ['[SEC] Features (.features-section)',   'class="features-section"'],
  ['[SEC] Marquee (.marquee-wrap)',         'class="marquee-wrap"'],
  ['[SEC] Fuel rows (.fuel-section)',       'class="fuel-section"'],
  ['[SEC] Fuel Compare (.fuel-compare-section)', 'class="fuel-compare-section"'],
  ['[SEC] Comparativo (#comparativo)',     'id="comparativo"'],
  ['[SEC] Custo / Factor cards (#custo)',  'id="custo"'],
  ['[SEC] Ficha Tecnica (#especificacoes)','id="especificacoes"'],
  ['[SEC] Sobre Nos (#sobre-nos)',         'id="sobre-nos"'],
  ['[SEC] Depoimentos (#depoimentos)',     'id="depoimentos"'],
  ['[SEC] FAQ primario (#faq)',            'id="faq"'],
  ['[SEC] Processo (#processo)',           'id="processo"'],
  ['[SEC] Inclusos + Orc (#contato)',      'id="contato"'],
  ['[SEC] Especialista (.specialist-section)', 'class="specialist-section"'],
  ['[SEC] Relacionados (.related-section)','class="related-section"'],
  ['[SEC] Galeria (.pgallery-section)',    'class="pgallery-section"'],
  ['[SEC] FAQ2 (.faq2-section)',           'class="faq2-section"'],
  ['[SEC] Setores (#setores)',             'id="setores"'],
  ['[SEC] Canal YouTube (.canal-section)', 'class="canal-section"'],
  ['[SEC] CTA Final (.cta-final)',         'class="cta-final"'],
  ['[SEC] Sticky Bar (.sticky-bar)',       'class="sticky-bar"'],
];

for (const [label, marker] of sections) {
  check(label, has(marker), `Secao "${marker}" nao encontrada`);
}

// ── BLOCO 4: CARROSSÉIS (cs-* pattern) ───────────────────────────────────────
const carousels = [
  ['[CS] featuresTrack (apps__grid)',  'id="featuresTrack"'],
  ['[CS] tstTrack (depoimentos)',      'id="tstTrack"'],
  ['[CS] processTrack',               'id="processTrack"'],
  ['[CS] relatedTrack',               'id="relatedTrack"'],
  ['[CS] sectorsTrack',               'id="sectorsTrack"'],
  ['[CS] canalTrack',                 'id="canalTrack"'],
  ['[CS] mqTrack (marquee)',          'id="mqTrack"'],
];

for (const [label, marker] of carousels) {
  check(label, has(marker), `Carousel "${marker}" nao encontrado — verificar cs-* pattern`);
}

// ── BLOCO 5: JS FUNCTIONS ────────────────────────────────────────────────────
const fns = [
  ['[JS] scrollTrack()',    'function scrollTrack'],
  ['[JS] scrollCarousel()', 'function scrollCarousel'],
  ['[JS] scrollSectors()',  'function scrollSectors'],
  ['[JS] loadVid()',        'function loadVid'],
  ['[JS] openLb()',         'function openLb'],
  ['[JS] closeLb()',        'function closeLb'],
  ['[JS] setStep()',        'function setStep'],
];

for (const [label, marker] of fns) {
  check(label, has(marker), `Funcao JS "${marker}" nao encontrada`);
}

// ── BLOCO 6: ACESSIBILIDADE / FAQ ────────────────────────────────────────────
check(
  '[A11Y] FAQ trigger usa <h3 role="button"> (nunca <button><h3>)',
  hasRe(/class="faq-trigger"\s+role="button"/) || hasRe(/class="faq-trigger"[^>]*role="button"/),
  'FAQ trigger deve ser <h3 class="faq-trigger" role="button" tabindex="0" aria-expanded="false">'
);

check(
  '[A11Y] FAQ trigger tem tabindex="0"',
  hasRe(/faq-trigger[^>]*tabindex="0"/) || hasRe(/tabindex="0"[^>]*faq-trigger/),
);

check(
  '[A11Y] FAQ trigger tem aria-expanded="false"',
  hasRe(/faq-trigger[^>]*aria-expanded="false"/) || hasRe(/aria-expanded="false"[^>]*faq-trigger/),
);

check(
  '[A11Y] FAQ2 trigger usa <h3 role="button">',
  hasRe(/class="faq2-trigger"\s+role="button"/) || hasRe(/class="faq2-trigger"[^>]*role="button"/),
  'FAQ2 trigger deve ser <h3 class="faq2-trigger" role="button" tabindex="0" aria-expanded="false">'
);

check(
  '[A11Y] FAQ2 tem .faq2-qmark, .faq2-trigger-text, .faq2-chevron',
  has('class="faq2-qmark"') && has('class="faq2-trigger-text"') && has('class="faq2-chevron"'),
);

check(
  '[A11Y] Apenas 1 <h1> na pagina',
  count('<h1') === 1,
  `Encontradas ${count('<h1')} ocorrencias de <h1> — deve ser exatamente 1`
);

check(
  '[A11Y] Lightbox tem aria-label ou aria-labelledby',
  hasRe(/pgallery-lb[^>]*(aria-label|role="dialog")/) || has('role="dialog"'),
  'Lightbox deve ter role="dialog" ou aria-label para acessibilidade'
);

// ── BLOCO 7: CSS CRÍTICO ─────────────────────────────────────────────────────
check(
  '[CSS] object-fit:contain em .apps__card-img img',
  has('object-fit:contain') || has('object-fit: contain'),
  'Imagens de feature card devem ter object-fit:contain — nunca cover'
);

check(
  '[CSS] NUNCA object-fit:cover em .apps__card-img',
  !hasRe(/apps__card-img[\s\S]{0,300}object-fit\s*:\s*cover/),
  'Remover object-fit:cover de dentro de .apps__card-img ou .apps__card-img img'
);

check(
  '[CSS] .sticky-bar com position:fixed',
  hasRe(/sticky-bar[\s\S]{0,200}position\s*:\s*fixed/) || hasRe(/position\s*:\s*fixed[\s\S]{0,200}sticky-bar/),
  'Sticky bar deve ter position:fixed'
);

check(
  '[CSS] CSS var(--green) definida',
  hasRe(/--green\s*:/) || has('--green:'),
);

check(
  '[CSS] CSS var(--dark) definida',
  hasRe(/--dark\s*:/) || has('--dark:'),
);

// ── BLOCO 8: CONTEÚDO / COPY ─────────────────────────────────────────────────
check(
  '[COPY] Zero travessao (—) no HTML',
  !has('—'),
  'Substituir todos os "—" por virgula ou ponto (regra global CLAUDE.md)'
);

check(
  '[COPY] Zero placeholder VIDEO_ID no HTML final',
  !has('VIDEO_ID'),
  'Substituir VIDEO_ID_* pelos IDs reais do YouTube'
);

check(
  '[COPY] Link WhatsApp presente (wa.me)',
  has('wa.me/'),
  'Adicionar link WhatsApp com wa.me/ no CTA e sticky bar'
);

check(
  '[COPY] Telefone presente (tel:)',
  has('href="tel:'),
  'Adicionar link de telefone com href="tel:"'
);

// ── BLOCO 9: TABS NAV ANCHORS ─────────────────────────────────────────────────
const tabAnchors = [
  '#visao-geral',
  '#caracteristicas',
  '#especificacoes',
  '#sobre-nos',
  '#faq',
  '#galeria',
  '#contato',
];

for (const anchor of tabAnchors) {
  check(
    `[TAB] Ancora "${anchor}" nas tabs`,
    has(`href="${anchor}"`),
    `Tab "${anchor}" nao encontrada no prod-tabs-nav`
  );
}

// ── BLOCO 10: LIGHTBOX ────────────────────────────────────────────────────────
check(
  '[LB] Lightbox .pgallery-lb presente',
  has('class="pgallery-lb"') || has('id="pgalleryLb"'),
);

check(
  '[LB] .pgallery-lb-close presente',
  has('pgallery-lb-close'),
);

check(
  '[LB] .pgallery-lb-arrow presente',
  has('pgallery-lb-arrow'),
);

// ── REPORT FINAL ─────────────────────────────────────────────────────────────
const total = pass + fail;
const score = Math.round((pass / total) * 100);

const GREEN  = '\x1b[32m';
const RED    = '\x1b[31m';
const YELLOW = '\x1b[33m';
const BOLD   = '\x1b[1m';
const RESET  = '\x1b[0m';

for (const { ok, label, hint } of results) {
  const icon  = ok ? `${GREEN}✔${RESET}` : `${RED}✘${RESET}`;
  const text  = ok ? label : `${RED}${label}${RESET}`;
  console.log(`  ${icon}  ${text}`);
  if (!ok && hint) console.log(`      ${YELLOW}→ ${hint}${RESET}`);
}

console.log('\n' + '─'.repeat(60));

const scoreColor = score >= 90 ? GREEN : score >= 70 ? YELLOW : RED;
console.log(`\n  ${BOLD}Score: ${scoreColor}${score}/100${RESET}${BOLD} — ${pass} ok / ${fail} falhas / ${total} checks${RESET}`);

if (fail === 0) {
  console.log(`\n  ${GREEN}${BOLD}Pagina aprovada no QA automatico.${RESET}`);
  console.log(`  Prosseguir para QA visual (localhost) e QA mobile (DevTools 375px).\n`);
} else {
  console.log(`\n  ${RED}${BOLD}Corrigir as ${fail} falhas antes de publicar.${RESET}\n`);
}
