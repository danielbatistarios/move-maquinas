// Injeta links de Peças e Manutenção nos 13 hubs de cidade
import { readFileSync, writeFileSync } from 'fs';

const cidades = [
  { slug: 'anapolis-go', nome: 'Anápolis' },
  { slug: 'aparecida-de-goiania-go', nome: 'Aparecida de Goiânia' },
  { slug: 'brasilia-df', nome: 'Brasília' },
  { slug: 'caldas-novas-go', nome: 'Caldas Novas' },
  { slug: 'formosa-go', nome: 'Formosa' },
  { slug: 'goiania-go', nome: 'Goiânia' },
  { slug: 'inhumas-go', nome: 'Inhumas' },
  { slug: 'itumbiara-go', nome: 'Itumbiara' },
  { slug: 'luziania-go', nome: 'Luziânia' },
  { slug: 'senador-canedo-go', nome: 'Senador Canedo' },
  { slug: 'trindade-go', nome: 'Trindade' },
  { slug: 'uruacu-go', nome: 'Uruaçu' },
  { slug: 'valparaiso-de-goias-go', nome: 'Valparaíso de Goiás' },
];

// SVG icons
const iconPecas = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M4.93 4.93a10 10 0 0 0 0 14.14"/><line x1="12" y1="2" x2="12" y2="6"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="4.22" y1="4.22" x2="7.05" y2="7.05"/><line x1="16.95" y1="16.95" x2="19.78" y2="19.78"/></svg>`;
const iconManutencao = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>`;
const arrowSvg = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>`;

let ok = 0, skip = 0;

for (const { slug, nome } of cidades) {
  const path = `/Users/jrios/move-maquinas-seo/${slug}/index.html`;
  let html;
  try { html = readFileSync(path, 'utf8'); } catch { console.log(`SKIP (sem hub): ${slug}`); skip++; continue; }

  // Já tem linkagem?
  if (html.includes(`/${slug}/pecas-e-assistencia-empilhadeira`)) {
    console.log(`SKIP (já tem): ${slug}`);
    skip++;
    continue;
  }

  // 1. Injetar 2 servico-cards após o card de curso (--stagger:4)
  // Encontrar o fechamento do card de curso
  const cursoPattern = /(<a href="\/[^"]+\/curso-de-operador-de-empilhadeira\/" class="servico-card[^"]*"[^>]*>[\s\S]*?<\/a>)(\s*\n\s*<\/div>)/;
  const cardsPecas = `
      <a href="/${slug}/pecas-e-assistencia-empilhadeira/" class="servico-card reveal reveal-stagger" style="--stagger:5">
        <div class="servico-card__icon">${iconPecas}</div>
        <div class="servico-card__name">Peças e Assistência</div>
        <p class="servico-card__desc">Peças originais Clark e assistência técnica especializada para empilhadeiras. Garfos, mastros, sistemas hidráulicos, elétricos e pneumáticos.</p>
        <span class="servico-card__cta">Peças e Assistência para Empilhadeira em ${nome} ${arrowSvg}</span>
      </a>

      <a href="/${slug}/manutencao-empilhadeira/" class="servico-card reveal reveal-stagger" style="--stagger:6">
        <div class="servico-card__icon">${iconManutencao}</div>
        <div class="servico-card__name">Manutenção de Empilhadeira</div>
        <p class="servico-card__desc">Manutenção preventiva e corretiva para todas as marcas. Planos mensais, revisões programadas e atendimento emergencial em ${nome}.</p>
        <span class="servico-card__cta">Manutenção de Empilhadeira em ${nome} ${arrowSvg}</span>
      </a>`;

  let newHtml = html.replace(cursoPattern, (_, card, closing) => card + cardsPecas + closing);

  if (newHtml === html) {
    // fallback: inserir antes do fechamento da grid de serviços
    console.log(`WARN (pattern fallback): ${slug}`);
    newHtml = html.replace(/(\s*<\/div>\s*<\/div>\s*<\/section>\s*<!-- ?servicos)/,
      cardsPecas + '$1');
  }

  // 2. Injetar links no footer
  // Procurar o <li> do curso no footer e adicionar depois
  const footerCursoPattern = /(<li><a href="\/[^"]+\/curso-de-operador-de-empilhadeira[^"]*">[^<]+<\/a><\/li>)/;
  const footerLinks = `$1
    <li><a href="/${slug}/pecas-e-assistencia-empilhadeira">Peças e Assistência Empilhadeira</a></li>
    <li><a href="/${slug}/manutencao-empilhadeira">Manutenção de Empilhadeira</a></li>`;

  newHtml = newHtml.replace(footerCursoPattern, footerLinks);

  writeFileSync(path, newHtml, 'utf8');
  console.log(`OK: ${slug}`);
  ok++;
}

console.log(`\nConcluído: ${ok} hubs atualizados, ${skip} pulados.`);
