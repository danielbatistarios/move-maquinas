import { AwsClient } from 'aws4fetch';
import { readFileSync } from 'node:fs';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET = 'pages';
const R2_PREFIX = 'agita-morango';
const LOCAL_BASE = '/Users/jrios/agita-morango-seo';
const PUB_BASE = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev';

const DRY_RUN = process.argv.includes('--dry-run');

const client = new AwsClient({
  accessKeyId: ACCESS_KEY,
  secretAccessKey: SECRET_KEY,
  service: 's3',
  region: 'auto'
});

const files = [
  { local: 'index.html',                                r2: 'index.html',                                    mime: 'text/html' },
  { local: '404.html',                                  r2: '404.html',                                      mime: 'text/html' },
  { local: 'mobile-patch.css',                          r2: 'mobile-patch.css',                              mime: 'text/css' },
  { local: 'sobre/index.html',                          r2: 'sobre/index.html',                              mime: 'text/html' },
  { local: 'blog/index.html',                           r2: 'blog/index.html',                               mime: 'text/html' },
  { local: 'faq/index.html',                            r2: 'faq/index.html',                                mime: 'text/html' },
  { local: 'contato/index.html',                        r2: 'contato/index.html',                            mime: 'text/html' },
  { local: 'orcamento/index.html',                      r2: 'orcamento/index.html',                          mime: 'text/html' },
  { local: 'clientes/index.html',                       r2: 'clientes/index.html',                           mime: 'text/html' },
  { local: 'servicos/index.html',                       r2: 'servicos/index.html',                           mime: 'text/html' },
  { local: 'trabalhe-conosco/index.html',               r2: 'trabalhe-conosco/index.html',                   mime: 'text/html' },
  { local: 'politica-privacidade/index.html',           r2: 'politica-privacidade/index.html',               mime: 'text/html' },
  { local: 'politica-cookies/index.html',               r2: 'politica-cookies/index.html',                   mime: 'text/html' },
  { local: 'termos-de-uso/index.html',                  r2: 'termos-de-uso/index.html',                      mime: 'text/html' },
  { local: 'author/amanda-morango/index.html',          r2: 'author/amanda-morango/index.html',              mime: 'text/html' },
  { local: 'author/marcelo-gomes/index.html',           r2: 'author/marcelo-gomes/index.html',               mime: 'text/html' },
  // W0 — LPs de serviço
  { local: 'empresa-de-recreacao-em-sao-paulo/index.html',           r2: 'empresa-de-recreacao-em-sao-paulo/index.html',           mime: 'text/html' },
  // W0 — Hub B2B
  { local: 'recreacao-corporativa-sp/index.html',                    r2: 'recreacao-corporativa-sp/index.html',                    mime: 'text/html' },
  // W1 — Spokes B2B
  { local: 'ativacoes-de-marca-com-criancas-em-sao-paulo/index.html',        r2: 'ativacoes-de-marca-com-criancas-em-sao-paulo/index.html',        mime: 'text/html' },
  { local: 'eventos-infantis-para-empresas-em-sao-paulo/index.html',         r2: 'eventos-infantis-para-empresas-em-sao-paulo/index.html',         mime: 'text/html' },
  { local: 'kids-day-e-family-day-corporativo-em-sao-paulo/index.html',      r2: 'kids-day-e-family-day-corporativo-em-sao-paulo/index.html',      mime: 'text/html' },
  { local: 'terceirizacao-recreacao-infantil-sp/index.html',                 r2: 'terceirizacao-recreacao-infantil-sp/index.html',                 mime: 'text/html' },
  { local: 'recreacao-infantil-corridas-de-rua-sp/index.html',               r2: 'recreacao-infantil-corridas-de-rua-sp/index.html',               mime: 'text/html' },
  // W1 — Servicos B2C
  { local: 'colonia-de-ferias-infantil-sp/index.html',                       r2: 'colonia-de-ferias-infantil-sp/index.html',                       mime: 'text/html' },
  { local: 'animacao-infantil-para-festas-em-sp/index.html',                 r2: 'animacao-infantil-para-festas-em-sp/index.html',                 mime: 'text/html' },
  { local: 'espaco-baby-para-festa-sp/index.html',                           r2: 'espaco-baby-para-festa-sp/index.html',                           mime: 'text/html' },
  { local: 'show-musical-infantil-em-sao-paulo/index.html',                  r2: 'show-musical-infantil-em-sao-paulo/index.html',                  mime: 'text/html' },
  { local: 'oficinas-criativas-infantis-em-sp/index.html',                   r2: 'oficinas-criativas-infantis-em-sp/index.html',                   mime: 'text/html' },
  { local: 'aniversario-infantil-em-sao-paulo/index.html',                   r2: 'aniversario-infantil-em-sao-paulo/index.html',                   mime: 'text/html' },
  { local: 'baladinha-kids-e-dj-infantil-em-sao-paulo/index.html',           r2: 'baladinha-kids-e-dj-infantil-em-sao-paulo/index.html',           mime: 'text/html' },
  { local: 'camarim-infantil-para-festas-em-sao-paulo/index.html',           r2: 'camarim-infantil-para-festas-em-sao-paulo/index.html',           mime: 'text/html' },
  { local: 'personagens-para-festas-infantis-em-sao-paulo/index.html',       r2: 'personagens-para-festas-infantis-em-sao-paulo/index.html',       mime: 'text/html' },
  { local: 'festas-tematicas-em-sao-paulo/index.html',                       r2: 'festas-tematicas-em-sao-paulo/index.html',                       mime: 'text/html' },
  { local: 'festa-das-cores-em-sao-paulo/index.html',                        r2: 'festa-das-cores-em-sao-paulo/index.html',                        mime: 'text/html' },
  { local: 'festa-do-pijama-em-sao-paulo/index.html',                        r2: 'festa-do-pijama-em-sao-paulo/index.html',                        mime: 'text/html' },
  { local: 'dia-das-criancas-em-sao-paulo/index.html',                       r2: 'dia-das-criancas-em-sao-paulo/index.html',                       mime: 'text/html' },
  { local: 'carnaval-infantil-em-sao-paulo/index.html',                      r2: 'carnaval-infantil-em-sao-paulo/index.html',                      mime: 'text/html' },
  { local: 'halloween-para-festas-e-eventos-em-sao-paulo/index.html',        r2: 'halloween-para-festas-e-eventos-em-sao-paulo/index.html',        mime: 'text/html' },
  { local: 'natal-infantil-para-festas-e-eventos-em-sao-paulo/index.html',   r2: 'natal-infantil-para-festas-e-eventos-em-sao-paulo/index.html',   mime: 'text/html' },
  { local: 'pascoa-para-festas-e-eventos-em-sao-paulo/index.html',           r2: 'pascoa-para-festas-e-eventos-em-sao-paulo/index.html',           mime: 'text/html' },
  { local: 'festa-de-ano-novo-infantil-em-sao-paulo/index.html',             r2: 'festa-de-ano-novo-infantil-em-sao-paulo/index.html',             mime: 'text/html' },
  { local: 'festa-junina-infantil-em-sao-paulo/index.html',                  r2: 'festa-junina-infantil-em-sao-paulo/index.html',                  mime: 'text/html' },
  // W1 — LPs de cidade
  { local: 'recreacao-para-festa-infantil-guarulhos/index.html',             r2: 'recreacao-para-festa-infantil-guarulhos/index.html',             mime: 'text/html' },
  { local: 'recreacao-para-festa-infantil-abc/index.html',                   r2: 'recreacao-para-festa-infantil-abc/index.html',                   mime: 'text/html' },
  { local: 'animacao-infantil-zona-leste-sp/index.html',                     r2: 'animacao-infantil-zona-leste-sp/index.html',                     mime: 'text/html' },
  { local: 'recreacao-para-festa-infantil-barueri/index.html',               r2: 'recreacao-para-festa-infantil-barueri/index.html',               mime: 'text/html' },
  { local: 'recreacao-para-festa-infantil-alphaville/index.html',            r2: 'recreacao-para-festa-infantil-alphaville/index.html',            mime: 'text/html' },
  // E-E-A-T
  { local: 'equipe-de-recreadores-infantis-em-sao-paulo/index.html',        r2: 'equipe-de-recreadores-infantis-em-sao-paulo/index.html',        mime: 'text/html' },
  { local: 'cases-e-clientes-de-evento-infantil/index.html',                r2: 'cases-e-clientes-de-evento-infantil/index.html',                mime: 'text/html' },
  // Sprint 1 — Novas páginas
  { local: 'aluguel-de-brinquedos-para-festa-infantil-sp/index.html',      r2: 'aluguel-de-brinquedos-para-festa-infantil-sp/index.html',      mime: 'text/html' },
  { local: 'atelie-infantil-em-sao-paulo/index.html',                      r2: 'atelie-infantil-em-sao-paulo/index.html',                      mime: 'text/html' },
  { local: 'mesas-e-cadeiras-infantis-em-sao-paulo/index.html',            r2: 'mesas-e-cadeiras-infantis-em-sao-paulo/index.html',            mime: 'text/html' },
  // Sprint 5 — Redirects HTML
  { local: 'animadores-de-festa-infantil-em-sao-paulo/index.html',         r2: 'animadores-de-festa-infantil-em-sao-paulo/index.html',         mime: 'text/html' },
  { local: 'baladinha-kids-e-dj-em-sao-paulo/index.html',                  r2: 'baladinha-kids-e-dj-em-sao-paulo/index.html',                  mime: 'text/html' },
  { local: 'aniversarios-e-festas-infantis-em-sao-paulo/index.html',       r2: 'aniversarios-e-festas-infantis-em-sao-paulo/index.html',       mime: 'text/html' },
  { local: 'kids-day-e-family-day-em-sao-paulo/index.html',                r2: 'kids-day-e-family-day-em-sao-paulo/index.html',                mime: 'text/html' },
  { local: 'ativacoes-de-marca-experiencias-sensoriais-sp/index.html',     r2: 'ativacoes-de-marca-experiencias-sensoriais-sp/index.html',     mime: 'text/html' },
  // W1 B2B — 14 novas páginas (2026-04-20)
  { local: 'baladinha-kids-sem-dj-sp/index.html',                          r2: 'baladinha-kids-sem-dj-sp/index.html',                          mime: 'text/html' },
  { local: 'dj-infantil-para-festas-em-sao-paulo/index.html',              r2: 'dj-infantil-para-festas-em-sao-paulo/index.html',              mime: 'text/html' },
  { local: 'bolha-de-sabao-gigante-sp/index.html',                         r2: 'bolha-de-sabao-gigante-sp/index.html',                         mime: 'text/html' },
  { local: 'escultura-de-balao-para-festas-sp/index.html',                 r2: 'escultura-de-balao-para-festas-sp/index.html',                 mime: 'text/html' },
  { local: 'pintura-artistica-infantil-sp/index.html',                     r2: 'pintura-artistica-infantil-sp/index.html',                     mime: 'text/html' },
  { local: 'personalizados-para-festa-infantil-sp/index.html',             r2: 'personalizados-para-festa-infantil-sp/index.html',             mime: 'text/html' },
  { local: 'foto-polaroid-para-festa-infantil-sp/index.html',              r2: 'foto-polaroid-para-festa-infantil-sp/index.html',              mime: 'text/html' },
  { local: 'recreacao-infantil-para-escolas-sp/index.html',                r2: 'recreacao-infantil-para-escolas-sp/index.html',                mime: 'text/html' },
  { local: 'magico-para-festa-infantil-sp/index.html',                     r2: 'magico-para-festa-infantil-sp/index.html',                     mime: 'text/html' },
  { local: 'recreacao-infantil-para-hoteis-sp/index.html',                 r2: 'recreacao-infantil-para-hoteis-sp/index.html',                 mime: 'text/html' },
  { local: 'recreacao-para-festa-infantil-zona-oeste-sp/index.html',       r2: 'recreacao-para-festa-infantil-zona-oeste-sp/index.html',       mime: 'text/html' },
  { local: 'recreacao-para-festa-infantil-zona-sul-sp/index.html',         r2: 'recreacao-para-festa-infantil-zona-sul-sp/index.html',         mime: 'text/html' },
  { local: 'recreacao-para-festa-infantil-zona-norte-sp/index.html',       r2: 'recreacao-para-festa-infantil-zona-norte-sp/index.html',       mime: 'text/html' },
  { local: 'aluguel-de-brinquedos-infantis-sp/index.html',                 r2: 'aluguel-de-brinquedos-infantis-sp/index.html',                 mime: 'text/html' },
  // Sprint 2 — Novas páginas 2026-04-20
  { local: 'kids-day-corporativo-em-sao-paulo/index.html',                r2: 'kids-day-corporativo-em-sao-paulo/index.html',                mime: 'text/html' },
  { local: 'family-day-corporativo-em-sao-paulo/index.html',              r2: 'family-day-corporativo-em-sao-paulo/index.html',              mime: 'text/html' },
  { local: 'show-de-magica-infantil-em-sao-paulo/index.html',             r2: 'show-de-magica-infantil-em-sao-paulo/index.html',             mime: 'text/html' },
  { local: 'espaco-baby-infantil-para-casamentos-em-sp/index.html',       r2: 'espaco-baby-infantil-para-casamentos-em-sp/index.html',       mime: 'text/html' },
  { local: 'recreacao-a-domicilio-em-sao-paulo/index.html',               r2: 'recreacao-a-domicilio-em-sao-paulo/index.html',               mime: 'text/html' },
  { local: 'recreacao-copa-do-mundo-infantil-sp/index.html',              r2: 'recreacao-copa-do-mundo-infantil-sp/index.html',              mime: 'text/html' },
  { local: 'kids-day-e-family-day-corporativo-em-sao-paulo/index.html',   r2: 'kids-day-e-family-day-corporativo-em-sao-paulo/index.html',   mime: 'text/html' },
  // Baladinha — novo slug foco (baladinha-kids-infantil-em-sp)
  { local: 'baladinha-kids-infantil-em-sp/index.html',                   r2: 'baladinha-kids-infantil-em-sp/index.html',                   mime: 'text/html' },
  { local: 'baladinha-kids-e-dj-infantil-em-sao-paulo/index.html',       r2: 'baladinha-kids-e-dj-infantil-em-sao-paulo/index.html',       mime: 'text/html' },
];

console.log(`\n${DRY_RUN ? '🔍 DRY RUN' : '🚀 UPLOAD'} — Agita Morango → R2 /${R2_PREFIX}/\n`);

let ok = 0, fail = 0;

for (const file of files) {
  const localPath = `${LOCAL_BASE}/${file.local}`;
  const r2Key = `${R2_PREFIX}/${file.r2}`;
  const pubUrl = `${PUB_BASE}/${r2Key}`;

  // Para HTML, também publicar como "slug" sem extensão para que /slug/ resolva no R2
  const isHtml = file.mime === 'text/html';
  const r2KeyNoExt = isHtml && file.r2.endsWith('/index.html')
    ? `${R2_PREFIX}/${file.r2.replace('/index.html', '')}`
    : null;

  if (DRY_RUN) {
    console.log(`  ✓ ${file.local} → ${pubUrl}`);
    if (r2KeyNoExt) console.log(`     (também → ${PUB_BASE}/${r2KeyNoExt})`);
    ok++;
    continue;
  }

  try {
    const body = readFileSync(localPath);

    // Upload principal: slug/index.html
    const url = `${ENDPOINT}/${BUCKET}/${r2Key}`;
    const res = await client.fetch(url, {
      method: 'PUT',
      body,
      headers: { 'Content-Type': `${file.mime}; charset=utf-8` }
    });

    if (res.ok) {
      console.log(`  ✅ ${file.local}`);
      console.log(`     ${pubUrl}`);
      ok++;
    } else {
      const text = await res.text();
      console.error(`  ❌ ${file.local} — ${res.status}: ${text}`);
      fail++;
      continue;
    }

    // Upload secundário: slug (sem extensão) — permite que /slug/ resolva no R2
    if (r2KeyNoExt) {
      const url2 = `${ENDPOINT}/${BUCKET}/${r2KeyNoExt}`;
      const res2 = await client.fetch(url2, {
        method: 'PUT',
        body,
        headers: { 'Content-Type': `${file.mime}; charset=utf-8` }
      });
      if (!res2.ok) {
        const text = await res2.text();
        console.error(`  ⚠️  ${file.r2.replace('/index.html','')} (sem ext) — ${res2.status}: ${text}`);
      }
    }
  } catch (e) {
    console.error(`  ❌ ${file.local} — ${e.message}`);
    fail++;
  }
}

console.log(`\n${DRY_RUN ? 'Simulação' : 'Upload'} concluído: ${ok} OK, ${fail} erros.\n`);
if (!DRY_RUN && ok > 0) {
  console.log(`🌐 Home: ${PUB_BASE}/${R2_PREFIX}/index.html\n`);
}
