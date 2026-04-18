import { AwsClient } from 'aws4fetch';
import { readFileSync, existsSync } from 'node:fs';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT   = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET     = 'pages';

const FILES = [
  { local: 'blog-nr35-final-v3-adjusted.html', r2: 'move/blog/plataforma-nr35-responsabilidade/index.html' },
];

const client = new AwsClient({ accessKeyId: ACCESS_KEY, secretAccessKey: SECRET_KEY, service: 's3', region: 'auto' });

async function main() {
  for (const f of FILES) {
    const path = `/Users/jrios/move-maquinas-seo/${f.local}`;
    if (!existsSync(path)) { console.log(`SKIP ${f.local}`); continue; }
    const body = readFileSync(path);
    const url  = `${ENDPOINT}/${BUCKET}/${f.r2}`;
    const res = await client.fetch(url, { method: 'PUT', body, headers: { 'Content-Type': 'text/html; charset=utf-8' } });
    console.log(res.ok ? `✓ ${f.r2}` : `✗ ${f.r2} — ${res.status}`);
  }
  console.log(`\nhttps://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/move/blog/plataforma-nr35-responsabilidade/index.html`);
}
main();
