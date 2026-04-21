import { AwsClient } from 'aws4fetch';
import { readFileSync } from 'node:fs';
import { readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe';
const ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET = 'pages';
const BASE_LOCAL = '/Users/jrios/move-maquinas-seo';
const BASE_R2 = 'move';

const client = new AwsClient({
  accessKeyId: ACCESS_KEY,
  secretAccessKey: SECRET_KEY,
  service: 's3',
  region: 'auto'
});

function findHtmlFiles(dir, files = []) {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) {
      findHtmlFiles(full, files);
    } else if (entry === 'index.html') {
      files.push(full);
    }
  }
  return files;
}

const files = findHtmlFiles(BASE_LOCAL);
console.log(`Uploading ${files.length} files...`);

let ok = 0, fail = 0;
for (const localPath of files) {
  const rel = localPath.replace(BASE_LOCAL + '/', '');
  const r2Key = `${BASE_R2}/${rel}`;
  const url = `${ENDPOINT}/${BUCKET}/${r2Key}`;

  try {
    const body = readFileSync(localPath);
    const res = await client.fetch(url, {
      method: 'PUT',
      body,
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });

    if (res.ok) {
      ok++;
      process.stdout.write('.');
    } else {
      console.error(`\nFAIL [${res.status}]: ${r2Key}`);
      fail++;
    }
  } catch (e) {
    console.error(`\nERROR: ${r2Key} — ${e.message}`);
    fail++;
  }
}

console.log(`\n\nOK: ${ok} | FAIL: ${fail}`);
console.log(`Preview: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/move/index.html`);
