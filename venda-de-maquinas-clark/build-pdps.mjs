/**
 * build-pdps.mjs
 * Gera index.html para cada modelo Clark a partir de:
 *   - clark-npx/index.html  (shell template)
 *   - {model}/pdp-content-v1.html  (conteúdo do produto)
 *
 * Uso: node build-pdps.mjs [modelo1 modelo2 ...] (sem args = todos)
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync, copyFileSync, readdirSync } from 'fs';
import { join, dirname } from 'path';

const ROOT = '/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark';
const SHELL_PATH = join(ROOT, 'clark-npx/index.html');
const ASSETS_SRC = join(ROOT, 'clark-s25-s35/assets');
const MOBILE_PATCH_SRC = join(ROOT, 'clark-s25-s35/mobile-patch.css');

// All models to process (excluding npx which is the shell reference)
const ALL_MODELS = [
  'clark-c20s',
  'clark-c60-c80',
  'clark-cop1',
  'clark-ctx70',
  'clark-gex',
  'clark-gts25-gts33',
  'clark-l25-l35',
  'clark-lep',
  'clark-lwio15',
  'clark-lxe',
  'clark-osx15',
  'clark-ppfxs20',
  'clark-ppxs20',
  'clark-psx16',
  'clark-pwio20',
  'clark-s-xe',
  'clark-s25-s35',
  'clark-s40-s60',
  'clark-se',
  'clark-srx16',
  'clark-ste',
  'clark-swx16',
  'clark-wpio15',
  'clark-wpio20',
  'clark-wpx35',
];

// Which models to actually process (CLI args or all)
const modelsArg = process.argv.slice(2);
const MODELS = modelsArg.length > 0 ? modelsArg : ALL_MODELS;

// ─────────────────────────────────────────────
// Helpers
// ─────────────────────────────────────────────

function stripHtmlComments(html) {
  return html.replace(/<!--[\s\S]*?-->/g, '');
}

/** Extract first match of a regex, return trimmed string or '' */
function extract(html, regex) {
  const m = html.match(regex);
  return m ? m[1].trim() : '';
}

/** Extract inner HTML of first element matching class */
function extractClassInner(html, cls) {
  // Match opening tag with that class (possibly with other classes/attrs)
  const openTag = new RegExp(`<(\\w+)[^>]*\\bclass="[^"]*\\b${cls}\\b[^"]*"[^>]*>`, 's');
  const m = html.match(openTag);
  if (!m) return '';
  const tag = m[1];
  const start = html.indexOf(m[0]) + m[0].length;
  // Find the matching closing tag
  let depth = 1;
  let i = start;
  while (i < html.length && depth > 0) {
    const nextOpen = html.indexOf(`<${tag}`, i);
    const nextClose = html.indexOf(`</${tag}>`, i);
    if (nextClose === -1) break;
    if (nextOpen !== -1 && nextOpen < nextClose) {
      depth++;
      i = nextOpen + 1;
    } else {
      depth--;
      if (depth === 0) return html.slice(start, nextClose).trim();
      i = nextClose + 1;
    }
  }
  return '';
}

/** Extract the FULL element (opening tag + inner + closing) matching a class */
function extractClassFull(html, cls) {
  const openTag = new RegExp(`<(\\w+)[^>]*\\bclass="[^"]*\\b${cls}\\b[^"]*"[^>]*>`, 's');
  const m = html.match(openTag);
  if (!m) return '';
  const tag = m[1];
  const start = html.indexOf(m[0]);
  const innerStart = start + m[0].length;
  let depth = 1;
  let i = innerStart;
  while (i < html.length && depth > 0) {
    const nextOpen = html.indexOf(`<${tag}`, i);
    const nextClose = html.indexOf(`</${tag}>`, i);
    if (nextClose === -1) break;
    if (nextOpen !== -1 && nextOpen < nextClose) {
      depth++;
      i = nextOpen + 1;
    } else {
      depth--;
      if (depth === 0) return html.slice(start, nextClose + `</${tag}>`.length).trim();
      i = nextClose + 1;
    }
  }
  return '';
}

/** Extract ALL elements matching a class as an array */
function extractAllClassFull(html, cls) {
  const results = [];
  let remaining = html;
  let offset = 0;
  while (true) {
    const openTag = new RegExp(`<(\\w+)[^>]*\\bclass="[^"]*\\b${cls}\\b[^"]*"[^>]*>`, 's');
    const m = remaining.match(openTag);
    if (!m) break;
    const tag = m[1];
    const start = remaining.indexOf(m[0]);
    const innerStart = start + m[0].length;
    let depth = 1;
    let i = innerStart;
    let found = false;
    while (i < remaining.length && depth > 0) {
      const nextOpen = remaining.indexOf(`<${tag}`, i);
      const nextClose = remaining.indexOf(`</${tag}>`, i);
      if (nextClose === -1) break;
      if (nextOpen !== -1 && nextOpen < nextClose) {
        depth++;
        i = nextOpen + 1;
      } else {
        depth--;
        if (depth === 0) {
          results.push(remaining.slice(start, nextClose + `</${tag}>`.length).trim());
          remaining = remaining.slice(nextClose + `</${tag}>`.length);
          found = true;
          break;
        }
        i = nextClose + 1;
      }
    }
    if (!found) break;
  }
  return results;
}

/** Extract value of a meta itemprop */
function extractMetaProp(html, prop) {
  const m = html.match(new RegExp(`<meta\\s+itemprop="${prop}"\\s+content="([^"]+)"`, 'i'));
  return m ? m[1].trim() : '';
}

/** Extract src from hero image in pdp-hero section */
function extractHeroImg(pdpHtml) {
  // First look inside pdp-hero section
  const heroSection = extractClassFull(pdpHtml, 'pdp-hero');
  if (heroSection) {
    const m = heroSection.match(/<img[^>]+src="([^"]+)"/);
    if (m) return m[1].trim();
  }
  // Fallback: any img with placeholder in name
  const m = pdpHtml.match(/src="(images\/[^"]+(?:placeholder|fundo-branco|visao-geral)[^"]*)"/);
  return m ? m[1].trim() : '';
}

/** Extract all images listed in pdp-content */
function extractAllImages(pdpHtml) {
  const imgs = [];
  const regex = /src="(images\/[^"]+)"/g;
  let m;
  while ((m = regex.exec(pdpHtml)) !== null) {
    if (!imgs.includes(m[1])) imgs.push(m[1]);
  }
  return imgs;
}

/** Extract FAQ items as array of {q, a} */
function extractFAQ(pdpHtml) {
  const faqs = [];
  // Pattern: <h3>question</h3>\n<p>answer</p>
  const faqRegex = /<h3[^>]*>([\s\S]*?)<\/h3>\s*<p[^>]*>([\s\S]*?)<\/p>/g;
  let m;
  while ((m = faqRegex.exec(pdpHtml)) !== null) {
    const q = m[1].replace(/<[^>]+>/g, '').trim();
    const a = m[2].replace(/<[^>]+>/g, '').trim();
    if (q && a) faqs.push({ q, a });
  }
  return faqs;
}

/** Extract specs table rows as array of {label, value} */
function extractSpecs(pdpHtml) {
  const specs = [];
  // Find table with 2 columns (Especificação + Valor)
  const tableMatch = pdpHtml.match(/<table[\s\S]*?<\/table>/g);
  if (!tableMatch) return specs;

  for (const table of tableMatch) {
    // Skip comparison tables (those with more than 2 columns in tbody)
    const rows = [...table.matchAll(/<tr[^>]*>([\s\S]*?)<\/tr>/g)];
    for (const row of rows) {
      const cells = [...row[1].matchAll(/<td[^>]*>([\s\S]*?)<\/td>/g)];
      if (cells.length === 2) {
        const label = cells[0][1].replace(/<[^>]+>/g, '').trim();
        const value = cells[1][1].replace(/<[^>]+>/g, '').trim();
        if (label && value) specs.push({ label, value });
      }
    }
  }
  return specs;
}

/** Extract key-findings data */
function extractKeyFindings(pdpHtml) {
  const kfSection = extractClassFull(pdpHtml, 'key-findings');
  if (!kfSection) return [];
  const cards = [];
  const cardRegex = /<div[^>]*class="[^"]*key-finding-card[^"]*"[^>]*>([\s\S]*?)<\/div>/g;
  let m;
  while ((m = cardRegex.exec(kfSection)) !== null) {
    const inner = m[1];
    const num = extract(inner, /class="[^"]*kf-number[^"]*"[^>]*>([\s\S]*?)<\//);
    const label = extract(inner, /class="[^"]*kf-label[^"]*"[^>]*>([\s\S]*?)<\//);
    if (num || label) cards.push({ num: num.replace(/<[^>]+>/g, '').trim(), label: label.replace(/<[^>]+>/g, '').trim() });
  }
  return cards;
}

/** Build the gallery block for the hero section */
function buildGallery(model, images) {
  const allImgs = images.length > 0 ? images : [`images/${model}-placeholder.jpg`];
  const mainImg = allImgs[0];
  const count = Math.min(allImgs.length, 6);

  const thumbsHtml = allImgs.slice(0, 6).map((img, i) => {
    const altText = img.replace('images/', '').replace(/-/g, ' ').replace('.jpg', '').replace('.png', '').replace('.webp', '');
    return `          <div class="gallery-thumb${i === 0 ? ' active' : ''}" data-idx="${i}">
            <img src="${img}" alt="${altText}" width="160" height="120" loading="${i === 0 ? 'eager' : 'lazy'}">
          </div>`;
  }).join('\n');

  const mainAlt = mainImg.replace('images/', '').replace(/-/g, ' ').replace('.jpg', '').replace('.png', '').replace('.webp', '');

  return { mainImg, count, thumbsHtml, mainAlt };
}

/** Build qspecs-section HTML from specs data */
function buildQspecs(specs) {
  if (!specs || specs.length === 0) return '';

  // Pick up to 6 most important specs
  const priority = ['capacidade', 'elevação', 'tensão', 'motor', 'tecnologia', 'emissão', 'normas', 'velocidade', 'peso', 'corredor'];
  const selected = [];

  // First pass: priority specs
  for (const p of priority) {
    if (selected.length >= 6) break;
    const found = specs.find(s => s.label.toLowerCase().includes(p));
    if (found && !selected.find(s => s.label === found.label)) selected.push(found);
  }

  // Fill remaining slots with whatever is available
  for (const s of specs) {
    if (selected.length >= 6) break;
    if (!selected.find(x => x.label === s.label)) selected.push(s);
  }

  const icons = {
    0: `<svg class="qspec-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="6" y="28" width="36" height="12" rx="3"/><path d="M12 28V12l12-6 12 6v16"/><path d="M18 28v-8h12v8"/></svg>`,
    1: `<svg class="qspec-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8"><line x1="24" y1="8" x2="24" y2="40"/><polyline points="14 18 24 8 34 18"/><line x1="14" y1="40" x2="34" y2="40"/></svg>`,
    2: `<svg class="qspec-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="10" y="14" width="28" height="20" rx="3"/><path d="M18 14V10a6 6 0 0112 0v4"/><line x1="24" y1="20" x2="24" y2="28"/></svg>`,
    3: `<svg class="qspec-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="24" cy="24" r="14"/><path d="M24 14v10l7 4"/></svg>`,
    4: `<svg class="qspec-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M24 8c-8 0-14 6-14 14s6 14 14 14 14-6 14-14-6-14-14-14z"/><polyline points="20 24 24 28 32 20"/></svg>`,
    5: `<svg class="qspec-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="10" y="12" width="28" height="28" rx="3"/><path d="M20 12V8a4 4 0 018 0v4"/></svg>`,
  };

  const boxes = selected.map((s, i) => {
    const val = s.value.replace(/<[^>]+>/g, '').trim();
    // Split value and unit
    const unitMatch = val.match(/^([\d.,]+)\s*([a-zA-ZçãáéíóúÇÃÁÉÍÓÚ\/\-°%]+)$/);
    let valHtml;
    if (unitMatch) {
      valHtml = `${unitMatch[1]} <span class="qspec-label">${unitMatch[2]}</span>`;
    } else {
      valHtml = val;
    }
    return `
      <div class="qspec-box">
        ${icons[i] || icons[5]}
        <div class="qspec-value">${valHtml}</div>
        <div class="qspec-label">${s.label}</div>
      </div>`;
  }).join('');

  return `
<section class="qspecs-section">
  <div class="container">
    <div class="section-tag" style="justify-content:center;margin-bottom:24px">Especificacoes Rapidas</div>
    <div class="qspecs-grid">${boxes}
    </div>
  </div>
</section>`;
}

/** Build FAQ section HTML */
function buildFaqSection(model, faqs, productName) {
  if (!faqs || faqs.length === 0) return '';

  const items = faqs.map(faq => `
      <div class="faq-item">
        <button class="faq-trigger" onclick="toggleFaq(this)" aria-expanded="false">
          <span>${faq.q}</span>
        </button>
        <div class="faq-content">
          ${faq.a}
        </div>
      </div>`).join('\n');

  const shortName = productName.replace(/ —.*/, '').replace(/\s+/g, ' ').trim();

  return `
<section class="faq-section">
  <div class="container">
    <div style="margin-bottom:40px">
      <div class="section-tag" style="justify-content:center">Perguntas Frequentes</div>
      <h2 class="section-title" style="text-align:center">${shortName}: Duvidas sobre o produto</h2>
    </div>
    <div id="faqList">
${items}
    </div>
  </div>
</section>`;
}

/** Build JSON-LD for the product */
function buildJsonLd(model, data) {
  const { productName, description, metaDesc, category, lcpImg, specs, faqs } = data;
  const url = `https://movemaquinas.com.br/venda-de-maquinas-clark/${model}`;
  const today = '2026-05-12';

  const additionalProperties = specs.slice(0, 10).map(s => ({
    '@type': 'PropertyValue',
    'name': s.label,
    'value': s.value.replace(/<[^>]+>/g, '').trim()
  }));

  const faqEntities = faqs.map(f => ({
    '@type': 'Question',
    'name': f.q,
    'acceptedAnswer': { '@type': 'Answer', 'text': f.a }
  }));

  const jsonLd = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'WebSite',
        '@id': 'https://movemaquinas.com.br/#website',
        'name': 'Move Maquinas',
        'url': 'https://movemaquinas.com.br',
        'inLanguage': 'pt-BR',
        'publisher': { '@id': 'https://movemaquinas.com.br/#organization' },
        'potentialAction': {
          '@type': 'SearchAction',
          'target': 'https://movemaquinas.com.br/?s={search_term_string}',
          'query-input': 'required name=search_term_string'
        }
      },
      {
        '@type': 'WebPage',
        '@id': `${url}/#webpage`,
        'url': url,
        'name': `${productName} | Move Maquinas Goiania`,
        'description': metaDesc,
        'inLanguage': 'pt-BR',
        'isPartOf': { '@id': 'https://movemaquinas.com.br/#website' },
        'about': { '@id': `${url}/#product` },
        'breadcrumb': { '@id': `${url}/#breadcrumb` },
        'hasPart': [{ '@id': `${url}/#faq` }],
        'datePublished': `${today}T00:00:00-03:00`,
        'dateModified': `${today}T00:00:00-03:00`,
        'speakable': {
          '@type': 'SpeakableSpecification',
          'cssSelector': ['.hero-title', '.section-title', '.faq-trigger']
        }
      },
      {
        '@type': 'Organization',
        '@id': 'https://movemaquinas.com.br/#organization',
        'name': 'Move Maquinas',
        'legalName': 'Move Maquinas Ltda',
        'url': 'https://movemaquinas.com.br',
        'logo': {
          '@type': 'ImageObject',
          'url': 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/assets/logo-move-maquinas.webp',
          'width': 120,
          'height': 30
        },
        'telephone': '+55-62-3211-1515',
        'email': 'contato@movemaquinas.com.br',
        'identifier': { '@type': 'PropertyValue', 'propertyID': 'CNPJ', 'value': '32.428.258/0001-80' },
        'contactPoint': {
          '@type': 'ContactPoint',
          'telephone': '+55-62-9-8263-7300',
          'contactType': 'sales',
          'availableLanguage': 'Portuguese'
        },
        'address': {
          '@type': 'PostalAddress',
          'streetAddress': 'Av. Eurico Viana, 4913',
          'addressLocality': 'Goiania',
          'addressRegion': 'GO',
          'postalCode': '74593-590',
          'addressCountry': 'BR'
        },
        'foundingDate': '2003',
        'numberOfEmployees': { '@type': 'QuantitativeValue', 'minValue': 20 },
        'sameAs': [
          'https://www.instagram.com/move.maquinas/',
          'https://www.linkedin.com/company/move-maquinas-oficial/',
          'https://www.youtube.com/@movemaquinas/featured'
        ]
      },
      {
        '@type': 'LocalBusiness',
        '@id': 'https://movemaquinas.com.br/#localbusiness',
        'name': 'Move Maquinas',
        'parentOrganization': { '@id': 'https://movemaquinas.com.br/#organization' },
        'url': 'https://movemaquinas.com.br',
        'telephone': '+55-62-3211-1515',
        'priceRange': '$$$$',
        'address': {
          '@type': 'PostalAddress',
          'streetAddress': 'Av. Eurico Viana, 4913',
          'addressLocality': 'Goiania',
          'addressRegion': 'GO',
          'postalCode': '74593-590',
          'addressCountry': 'BR'
        },
        'geo': { '@type': 'GeoCoordinates', 'latitude': -16.6869, 'longitude': -49.2648 },
        'openingHoursSpecification': [
          { '@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday','Tuesday','Wednesday','Thursday','Friday'], 'opens': '08:00', 'closes': '18:00' },
          { '@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Saturday', 'opens': '08:00', 'closes': '12:00' }
        ],
        'email': 'contato@movemaquinas.com.br',
        'currenciesAccepted': 'BRL',
        'paymentAccepted': 'Dinheiro, Transferencia bancaria, Boleto, Financiamento FCO, Financiamento FINAME, Leasing'
      },
      {
        '@type': 'Service',
        '@id': 'https://movemaquinas.com.br/#service-distribuicao-clark',
        'name': 'Distribuicao Exclusiva Clark Equipment em Goias',
        'serviceType': `Distribuicao exclusiva de ${category} Clark`,
        'provider': { '@id': 'https://movemaquinas.com.br/#organization' },
        'areaServed': [
          { '@type': 'State', 'name': 'Goias' },
          { '@type': 'State', 'name': 'Distrito Federal' },
          { '@type': 'State', 'name': 'Tocantins' },
          { '@type': 'State', 'name': 'Mato Grosso' }
        ]
      },
      {
        '@type': 'Brand',
        '@id': 'https://movemaquinas.com.br/#brand-clark',
        'name': 'Clark',
        'alternateName': 'Clark Equipment',
        'url': 'https://www.clarkmhc.com.br',
        'logo': 'https://www.clarkmhc.com.br/favicon.ico'
      },
      {
        '@type': 'Product',
        '@id': `${url}/#product`,
        'name': productName,
        'description': description,
        'brand': { '@id': 'https://movemaquinas.com.br/#brand-clark' },
        'manufacturer': {
          '@type': 'Organization',
          'name': 'Clark Material Handling Company',
          'alternateName': 'Clark Equipment',
          'url': 'https://www.clarkmhc.com'
        },
        'category': category,
        'url': url,
        'mainEntityOfPage': { '@id': `${url}/#webpage` },
        'datePublished': today,
        'dateModified': today,
        'image': [{ '@type': 'ImageObject', 'url': lcpImg, 'name': productName, 'representativeOfPage': true }],
        'additionalProperty': additionalProperties,
        'offers': {
          '@type': 'AggregateOffer',
          'priceCurrency': 'BRL',
          'availability': 'https://schema.org/InStock',
          'itemCondition': 'https://schema.org/NewCondition',
          'url': url,
          'seller': { '@id': 'https://movemaquinas.com.br/#localbusiness' }
        }
      },
      {
        '@type': 'BreadcrumbList',
        '@id': `${url}/#breadcrumb`,
        'itemListElement': [
          { '@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': 'https://movemaquinas.com.br' },
          { '@type': 'ListItem', 'position': 2, 'name': 'Venda Clark', 'item': 'https://movemaquinas.com.br/venda-de-maquinas-clark' },
          { '@type': 'ListItem', 'position': 3, 'name': productName, 'item': url }
        ]
      },
      ...(faqEntities.length > 0 ? [{
        '@type': 'FAQPage',
        '@id': `${url}/#faq`,
        'isPartOf': { '@id': `${url}/#webpage` },
        'mainEntity': faqEntities
      }] : [])
    ]
  };

  return JSON.stringify(jsonLd, null, 2);
}

/** Build the full JS block */
function buildJS(images) {
  const jsImages = images.map(i => `  '${i}'`).join(',\n');
  return `<script>
function toggleFaq(btn) {
  const isOpen = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', !isOpen);
  const content = btn.nextElementSibling;
  content.setAttribute('data-open', !isOpen);
}

const galleryMain = document.getElementById('galleryImg');
const galleryCounter = document.getElementById('gCount');
const thumbs = document.querySelectorAll('.gallery-thumb');
let currentIdx = 0;
const images = [
${jsImages}
];

thumbs.forEach((thumb, idx) => {
  thumb.addEventListener('click', () => {
    currentIdx = idx;
    galleryMain.src = images[currentIdx];
    galleryCounter.textContent = currentIdx + 1;
    thumbs.forEach(t => t.classList.remove('active'));
    thumb.classList.add('active');
  });
});

const hamburger = document.getElementById('mmHamburger');
const mobileMenu = document.getElementById('mmMobileOverlay');
const closeBtn = document.getElementById('mmMobileClose');
hamburger.addEventListener('click', () => {
  mobileMenu.classList.add('open');
  hamburger.setAttribute('aria-expanded', 'true');
});
closeBtn.addEventListener('click', () => {
  mobileMenu.classList.remove('open');
  hamburger.setAttribute('aria-expanded', 'false');
});

document.querySelectorAll('.mm-mob__trigger').forEach(btn => {
  btn.addEventListener('click', function() {
    const isOpen = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', !isOpen);
    const subMenu = document.getElementById(this.getAttribute('data-target'));
    subMenu.classList.toggle('open');
  });
});
</script>`;
}

/** Copy assets if missing */
function ensureAssets(modelDir) {
  const assetsTarget = join(modelDir, 'assets');
  const fontsTarget = join(assetsTarget, 'fonts');

  if (!existsSync(fontsTarget)) {
    mkdirSync(fontsTarget, { recursive: true });
    const srcFont = join(ASSETS_SRC, 'fonts/inter-latin.woff2');
    if (existsSync(srcFont)) {
      copyFileSync(srcFont, join(fontsTarget, 'inter-latin.woff2'));
      console.log('  → Copied inter-latin.woff2');
    }
  }

  const stylesSrc = join(ASSETS_SRC, 'styles-pdp.css');
  const stylesDst = join(assetsTarget, 'styles-pdp.css');
  if (!existsSync(stylesDst) && existsSync(stylesSrc)) {
    copyFileSync(stylesSrc, stylesDst);
    console.log('  → Copied styles-pdp.css');
  }

  const mobilePatchDst = join(modelDir, 'mobile-patch.css');
  if (!existsSync(mobilePatchDst) && existsSync(MOBILE_PATCH_SRC)) {
    copyFileSync(MOBILE_PATCH_SRC, mobilePatchDst);
    console.log('  → Copied mobile-patch.css');
  }
}

// ─────────────────────────────────────────────
// Main processing
// ─────────────────────────────────────────────

const shellHtml = readFileSync(SHELL_PATH, 'utf8');

// Extract the shell's static parts
// Head up to (not including) <title>
const headStart = shellHtml.indexOf('<head>') + '<head>'.length;
const titleStart = shellHtml.indexOf('<title>');

// Style block (from @font-face to </style>)
const styleBlockMatch = shellHtml.match(/<style>([\s\S]*?)<\/style>/);
const styleBlock = styleBlockMatch ? `<style>${styleBlockMatch[1]}</style>` : '';

// Nav (from <header class="mm-nav" to end of header>)
const navMatch = shellHtml.match(/<header class="mm-nav"[\s\S]*?<\/header>/);
const navHtml = navMatch ? navMatch[0] : '';

// Mobile overlay
const mobMatch = shellHtml.match(/<div class="mm-mob"[\s\S]*?<\/div>\s*(?=<main)/);
const mobHtml = mobMatch ? mobMatch[0] : '';

// Footer
const footerMatch = shellHtml.match(/<footer class="mm-ft"[\s\S]*?<\/footer>/);
const footerHtml = footerMatch ? footerMatch[0] : '';

// ─────────────────────────────────────────────

for (const model of MODELS) {
  const modelDir = join(ROOT, model);
  const pdpPath = join(modelDir, 'pdp-content-v1.html');

  if (!existsSync(pdpPath)) {
    console.log(`⚠ SKIP ${model}: no pdp-content-v1.html`);
    continue;
  }

  console.log(`\n▶ Processing ${model}...`);

  // Ensure assets are in place
  ensureAssets(modelDir);

  const pdpHtml = readFileSync(pdpPath, 'utf8');

  // Fallback names for models that have no itemprop=name nor h1
  const MODEL_NAMES = {
    'clark-cop1': 'Clark COP1 — Empilhadeira de Picking em Altura com Operador a Bordo',
    'clark-s-xe': 'Clark S-XE — Empilhadeira Elétrica para Operação Externa e Rampas (S25XE, S30XE, S35XE)',
    'clark-ste': 'Clark STE16, STE18 e STE20 — Empilhadeira Elétrica 3 Rodas para Corredor Estreito',
  };

  // ── Extract data from pdp-content ──
  const productName = extractMetaProp(pdpHtml, 'name')
    || extract(pdpHtml, /<h1[^>]*>([\s\S]*?)<\/h1>/)
    || MODEL_NAMES[model]
    || model.replace('clark-', 'Clark ').toUpperCase();
  const category = extractMetaProp(pdpHtml, 'category') || 'Empilhadeira Clark';
  const heroSubtitle = extract(pdpHtml, /class="hero-subtitle"[^>]*>([\s\S]*?)<\/p>/);
  const lcpImg = extractHeroImg(pdpHtml) || `images/${model}-placeholder.jpg`;
  const allImages = extractAllImages(pdpHtml);
  const specs = extractSpecs(pdpHtml);
  const faqs = extractFAQ(pdpHtml);
  const keyFindings = extractKeyFindings(pdpHtml);

  // Opening scene
  let openingScene = extractClassFull(pdpHtml, 'opening-scene');
  // tldr-box
  let tldrBox = extractClassFull(pdpHtml, 'tldr-box');
  // key-findings section
  let kfSection = extractClassFull(pdpHtml, 'key-findings');
  // narrative-return
  let narrativeReturn = extractClassFull(pdpHtml, 'narrative-return');

  // All pdp-section blocks (content sections)
  const pdpSections = extractAllClassFull(pdpHtml, 'pdp-section');

  // Build hero h1 and intro list from pdp-hero or direct content
  const h1Text = productName.replace(/<[^>]+>/g, '').trim();

  // Extract hero-list items from pdp-content if they exist
  const heroListSection = extractClassFull(pdpHtml, 'pdp-hero');
  let heroListHtml = '';
  if (heroListSection) {
    const listMatch = heroListSection.match(/<ul[\s\S]*?<\/ul>/);
    if (listMatch) heroListHtml = listMatch[0];
  }

  // Build short description for meta and intro paragraph
  const metaDesc = heroSubtitle
    ? heroSubtitle.replace(/<[^>]+>/g, '').trim().slice(0, 155)
    : `${h1Text}. Distribuidor exclusivo Clark em Goias. Orcamento em 1 dia util. Move Maquinas.`;
  const description = heroSubtitle
    ? heroSubtitle.replace(/<[^>]+>/g, '').trim()
    : `${h1Text}. Venda e locacao. Move Maquinas, distribuidor exclusivo Clark em Goias.`;

  const ogImage = `https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/venda-de-maquinas-clark/${model}/${lcpImg.replace('images/', '')}`;
  const pageUrl = `https://movemaquinas.com.br/venda-de-maquinas-clark/${model}`;
  const shortModel = model.replace('clark-', '').toUpperCase();

  // Build gallery
  const { mainImg, count, thumbsHtml, mainAlt } = buildGallery(model, allImages);

  // Build qspecs
  const qspecsHtml = buildQspecs(specs);

  // Build FAQ section
  const faqSectionHtml = buildFaqSection(model, faqs, h1Text);

  // Build JSON-LD
  const jsonLdStr = buildJsonLd(model, { productName: h1Text, description, metaDesc, category, lcpImg, specs, faqs });

  // Build JS
  const jsBlock = buildJS(allImages.length > 0 ? allImages : [`images/${model}-placeholder.jpg`]);

  // Seals from key findings
  const seals = keyFindings.slice(0, 4);
  const sealsHtml = seals.map(s => `
          <div class="seal-item">
            <div class="seal-item-value">${s.num} ${s.label}</div>
          </div>`).join('\n');

  // Build hero-list from tldr-box items if no explicit hero-list
  let finalHeroListHtml = heroListHtml;
  if (!finalHeroListHtml && tldrBox) {
    const items = [...tldrBox.matchAll(/<li[^>]*>([\s\S]*?)<\/li>/g)];
    if (items.length > 0) {
      const liHtml = items.slice(0, 3).map(m => {
        const text = m[1].replace(/<[^>]+>/g, '').trim();
        // First ": " becomes bold label
        const colonIdx = text.indexOf(':');
        if (colonIdx > 0 && colonIdx < 60) {
          return `          <li>
            <span class="hl-dot"></span>
            <span><strong>${text.slice(0, colonIdx + 1)}</strong>${text.slice(colonIdx + 1)}</span>
          </li>`;
        }
        return `          <li>
            <span class="hl-dot"></span>
            <span>${text}</span>
          </li>`;
      }).join('\n');
      finalHeroListHtml = `<ul class="hero-list">\n${liHtml}\n        </ul>`;
    }
  }

  // Build hero intro paragraph
  const heroIntro = `<p class="hero-intro">${description} Move Maquinas, distribuidor exclusivo Clark em Goias.</p>`;

  // Encode model name for WhatsApp URL
  const waText = encodeURIComponent(`Ola, tenho interesse no ${h1Text}. Podem me enviar orcamento?`);

  // Build the content sections HTML
  let contentSectionsHtml = '';

  // Opening scene
  if (openingScene) {
    contentSectionsHtml += `\n${openingScene}\n`;
  }

  // TLDR box
  if (tldrBox) {
    contentSectionsHtml += `\n${tldrBox}\n`;
  }

  // Key findings
  if (kfSection) {
    contentSectionsHtml += `\n${kfSection}\n`;
  }

  // PDP sections
  if (pdpSections.length > 0) {
    contentSectionsHtml += '\n' + pdpSections.join('\n') + '\n';
  }

  // Narrative return
  if (narrativeReturn) {
    contentSectionsHtml += `\n${narrativeReturn}\n`;
  }

  // Specs table section
  if (specs.length > 0) {
    const rows = specs.map(s => `          <tr><td>${s.label}</td><td><strong>${s.value.replace(/<[^>]+>/g, '').trim()}</strong></td></tr>`).join('\n');
    contentSectionsHtml += `
<section style="padding:56px 0;border-top:1px solid #e5e5e5">
  <div class="container">
    <div style="margin-bottom:40px">
      <div class="section-tag" style="justify-content:center">Ficha Tecnica</div>
      <h2 class="section-title" style="text-align:center">Especificacoes tecnicas — ${h1Text}</h2>
    </div>
    <div style="overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:14px">
        <thead>
          <tr style="background:#f3f7f5">
            <th style="padding:12px;text-align:left;border:1px solid #e5e5e5;font-weight:700">Especificacao</th>
            <th style="padding:12px;text-align:left;border:1px solid #e5e5e5;font-weight:700">Valor</th>
          </tr>
        </thead>
        <tbody>
${rows}
        </tbody>
      </table>
    </div>
  </div>
</section>`;
  }

  // ── Assemble full HTML ──
  const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${h1Text} | Move Maquinas Goiania</title>
<meta name="description" content="${metaDesc}">
<link rel="canonical" href="${pageUrl}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Move Maquinas">
<meta name="theme-color" content="#1D9648">
<meta property="og:title" content="${h1Text} | Move Maquinas">
<meta property="og:description" content="${metaDesc}">
<meta property="og:image" content="${ogImage}">
<meta property="og:type" content="product">
<meta property="og:locale" content="pt_BR">
<meta property="og:url" content="${pageUrl}">
<meta property="og:site_name" content="Move Maquinas">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${h1Text} | Move Maquinas">
<meta name="twitter:description" content="${metaDesc}">
<meta name="twitter:image" content="${ogImage}">

<link rel="preload" href="assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="${mainImg}" as="image" fetchpriority="high">
<link rel="stylesheet" href="mobile-patch.css">

${styleBlock}
<script type="application/ld+json">
${jsonLdStr}
</script>
</head>
<body>

${navHtml}

${mobHtml}

<main id="conteudo-principal">

<section class="hero">
  <div class="container">

    <ol class="hero-breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="https://movemaquinas.com.br" itemprop="item"><span itemprop="name">Inicio</span></a>
        <meta itemprop="position" content="1">
      </li>
      <span class="hbc-sep">›</span>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="https://movemaquinas.com.br/venda-de-maquinas-clark" itemprop="item"><span itemprop="name">Venda Clark</span></a>
        <meta itemprop="position" content="2">
      </li>
      <span class="hbc-sep">›</span>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span class="hbc-cur" itemprop="name">${h1Text}</span>
        <meta itemprop="position" content="3">
      </li>
    </ol>

    <div class="mobile-hero-header">
      <div class="hero-badges">
        <span class="badge badge-dark">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="11" height="11"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          Distribuidor Autorizado Clark
        </span>
        <span class="badge badge-green">Entregamos em GO, DF, TO e MT</span>
      </div>
      <p class="hero-title">${h1Text}</p>
    </div>

    <div class="hero-grid">

      <div class="gallery" id="galleryRoot">
        <div class="gallery-main" id="galleryMainClick">
          <img id="galleryImg" width="800" height="600"
            src="${mainImg}"
            alt="${mainAlt}" loading="eager">
          <div class="gallery-counter"><span id="gCount">1</span> / ${count}</div>
          <button class="gallery-main-zoom" id="galleryZoomBtn" aria-label="Ver em tela cheia">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M8 3H5a2 2 0 00-2 2v3m18 0V5a2 2 0 00-2-2h-3m0 18h3a2 2 0 002-2v-3M3 16v3a2 2 0 002 2h3"/></svg>
          </button>
        </div>
        <div class="gallery-sidebar">
${thumbsHtml}
        </div>
      </div>

      <div class="hero-info">
        <div class="hero-badges">
          <span class="badge badge-dark">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="11" height="11"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            Distribuidor Autorizado Clark
          </span>
          <span class="badge badge-green">Entregamos em GO, DF, TO e MT</span>
        </div>

        <h1 class="hero-title">${h1Text}</h1>

        ${heroIntro}

        ${finalHeroListHtml || ''}

        <div class="hero-ctas">
          <a href="https://wa.me/5562982637300?text=${waText}" class="btn-cotacao">
            Receber Cotacao Agora
          </a>
          <a href="tel:6232111515" class="btn-tel">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.63A2 2 0 012.18.18h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 8.02a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7a2 2 0 011.72 2z"/></svg>
            (62) 3211-1515
          </a>
        </div>

        <div class="hero-seals">
          ${sealsHtml || `<div class="seal-item"><div class="seal-item-value">Distribuidor Exclusivo Clark</div></div><div class="seal-item"><div class="seal-item-value">Proposta em 1 dia util</div></div>`}
        </div>
      </div>

    </div>
  </div>
</section>

${qspecsHtml}

<section style="padding:56px 0;background:#fff">
  <div class="container">
    ${contentSectionsHtml}
  </div>
</section>

${faqSectionHtml}

</main>

${footerHtml}

<link rel="stylesheet" href="assets/styles-pdp.css">

${jsBlock}
</body>
</html>`;

  const outPath = join(modelDir, 'index.html');
  writeFileSync(outPath, html, 'utf8');

  const lines = html.split('\n').length;
  console.log(`  ✓ Written ${outPath} (${lines} lines, ${Buffer.byteLength(html, 'utf8')} bytes)`);
  console.log(`    title: ${h1Text}`);
  console.log(`    lcp: ${mainImg} | images: ${allImages.length} | specs: ${specs.length} | faqs: ${faqs.length}`);
}

console.log('\n✅ Done!');
