import { AwsClient } from 'aws4fetch';
import { readFileSync } from 'node:fs';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET = 'pages';

const client = new AwsClient({
  accessKeyId: ACCESS_KEY,
  secretAccessKey: SECRET_KEY,
  service: 's3',
  region: 'auto'
});

const cidades = [
  'anapolis-go', 'aparecida-de-goiania-go', 'brasilia-df', 'caldas-novas-go',
  'formosa-go', 'inhumas-go', 'itumbiara-go', 'luziania-go',
  'senador-canedo-go', 'trindade-go', 'uruacu-go', 'valparaiso-de-goias-go',
];

const servicos = ['pecas-e-assistencia-empilhadeira', 'manutencao-empilhadeira'];

let ok = 0, errors = 0;

for (const cidade of cidades) {
  for (const svc of servicos) {
    const localPath = `/Users/jrios/move-maquinas-seo/${cidade}/${svc}/index.html`;
    const r2Key = `move/${cidade}/${svc}/index.html`;
    const url = `${ENDPOINT}/${BUCKET}/${r2Key}`;

    try {
      const body = readFileSync(localPath);
      const res = await client.fetch(url, {
        method: 'PUT',
        body,
        headers: { 'Content-Type': 'text/html; charset=utf-8' }
      });

      if (res.ok) {
        console.log(`OK  ${cidade}/${svc}`);
        ok++;
      } else {
        const text = await res.text();
        console.error(`ERR ${cidade}/${svc}: ${res.status} ${text.slice(0, 100)}`);
        errors++;
      }
    } catch (e) {
      console.error(`ERR ${cidade}/${svc}: ${e.message}`);
      errors++;
    }
  }
}

console.log(`\nConcluído: ${ok} OK, ${errors} erros.`);
console.log(`Preview: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/move/anapolis-go/pecas-e-assistencia-empilhadeira/index.html`);
