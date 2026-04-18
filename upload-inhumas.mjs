/**
 * upload-inhumas.mjs — Upload 6 Inhumas pages to R2
 */
import { AwsClient } from 'aws4fetch';
import { readFileSync, existsSync } from 'node:fs';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT   = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET     = 'pages';
const BASE       = '/Users/jrios/move-maquinas-seo';

const FILES = [
  { local: 'inhumas-go-hub-V2.html',                                       r2: 'inhumas-go/index.html' },
  { local: 'inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', r2: 'inhumas-go/aluguel-de-plataforma-elevatoria-articulada/index.html' },
  { local: 'inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',   r2: 'inhumas-go/aluguel-de-plataforma-elevatoria-tesoura/index.html' },
  { local: 'inhumas-go-aluguel-de-empilhadeira-combustao-V2.html',          r2: 'inhumas-go/aluguel-de-empilhadeira-combustao/index.html' },
  { local: 'inhumas-go-aluguel-de-transpaleteira-V2.html',                  r2: 'inhumas-go/aluguel-de-transpaleteira/index.html' },
  { local: 'inhumas-go-curso-de-operador-de-empilhadeira-V2.html',          r2: 'inhumas-go/curso-de-operador-de-empilhadeira/index.html' },
];

const client = new AwsClient({ accessKeyId: ACCESS_KEY, secretAccessKey: SECRET_KEY, service: 's3', region: 'auto' });

async function main() {
  let ok = 0, fail = 0;
  for (const f of FILES) {
    const path = `${BASE}/${f.local}`;
    if (!existsSync(path)) { console.log(`SKIP ${f.local} — not found`); fail++; continue; }
    const body = readFileSync(path);
    const url = `${ENDPOINT}/${BUCKET}/${f.r2}`;
    try {
      const res = await client.fetch(url, { method: 'PUT', body, headers: { 'Content-Type': 'text/html; charset=utf-8' } });
      if (res.ok) { console.log(`OK  ${f.r2}`); ok++; }
      else { console.log(`ERR ${f.r2} — ${res.status}`); fail++; }
    } catch(e) { console.log(`ERR ${f.r2} — ${e.message}`); fail++; }
  }
  console.log(`\nDone: ${ok} uploaded, ${fail} failed`);
  console.log(`URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/`);
}
main();
