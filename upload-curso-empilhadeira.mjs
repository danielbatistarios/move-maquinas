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

const body = readFileSync('/Users/jrios/move-maquinas-seo/ref-goiania-curso.html');
const url = `${ENDPOINT}/${BUCKET}/goiania-go/curso-de-operador-de-empilhadeira/index.html`;

const res = await client.fetch(url, {
  method: 'PUT',
  body,
  headers: { 'Content-Type': 'text/html; charset=utf-8' }
});

console.log('Status:', res.status, res.statusText);
if (res.ok) {
  console.log('Upload OK!');
  console.log('URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/goiania-go/curso-de-operador-de-empilhadeira/index.html');
} else {
  const text = await res.text();
  console.error('Erro:', text);
}
