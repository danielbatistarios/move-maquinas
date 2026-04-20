import { AwsClient } from 'aws4fetch';
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT   = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET     = 'pages';
const PREFIX     = 'move';

const ROOT  = '/Users/jrios/move-maquinas-seo';
const PILOT = process.argv.includes('--pilot');  // so goiania-go/index.html
const DRY   = process.argv.includes('--dry-run');

const client = new AwsClient({
  accessKeyId: ACCESS_KEY,
  secretAccessKey: SECRET_KEY,
  service: 's3',
  region: 'auto'
});

function walk(dir) {
  const out = [];
  for (const f of readdirSync(dir)) {
    const full = join(dir, f);
    if (statSync(full).isDirectory()) out.push(...walk(full));
    else if (f === 'index.html' || f === '404.html') out.push(full);
  }
  return out;
}

// Coletar arquivos
let files = walk(ROOT).filter(f =>
  !f.includes('/assets/') && !f.includes('nav-footer')
);

if (PILOT) {
  files = files.filter(f => f.includes('goiania-go/index.html'));
}

console.log(`Arquivos a subir: ${files.length}${DRY ? ' [DRY-RUN]' : ''}`);
let ok = 0, fail = 0;

for (const file of files) {
  const rel  = relative(ROOT, file);
  const key  = `${PREFIX}/${rel}`;
  const url  = `${ENDPOINT}/${BUCKET}/${key}`;
  const body = readFileSync(file);

  if (DRY) {
    console.log(`[dry] ${key}`);
    continue;
  }

  try {
    const res = await client.fetch(url, {
      method: 'PUT',
      headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'public, max-age=3600' },
      body
    });
    if (res.ok) { console.log(`[ok]  ${key}`); ok++; }
    else { console.error(`[err] ${key} — ${res.status}`); fail++; }
  } catch (e) {
    console.error(`[err] ${key} — ${e.message}`); fail++;
  }
}

if (!DRY) console.log(`\nok=${ok} fail=${fail}`);
