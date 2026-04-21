#!/usr/bin/env node
import { AwsClient } from 'aws4fetch';
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const ACCOUNT_ID = 'bd2efcc812524f54a8c492f90052f3bd';
const ACCESS_KEY = process.env.R2_ACCESS_KEY || '9b8005782e2f6ebd197768fabe1e07c2';
const SECRET_KEY = process.env.R2_SECRET_KEY || '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093';
const ENDPOINT = `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET = 'pub';
const R2_PREFIX = 'move';
const LOCAL_BASE = '/Users/jrios/move-maquinas-seo';
const PUB_BASE = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev';

const DRY_RUN = process.argv.includes('--dry-run');

const client = new AwsClient({
  accessKeyId: ACCESS_KEY,
  secretAccessKey: SECRET_KEY,
  service: 's3',
  region: 'auto'
});

// City slugs with schema-elite-v2.0 updates (44 pages)
const CITIES = [
  'goiania-go', 'brasilia-df', 'anapolis-go', 'aparecida-de-goiania-go',
  'uruacu-go', 'senador-canedo-go', 'trindade-go', 'inhumas-go',
  'caldas-novas-go', 'itumbiara-go', 'luziania-go', 'formosa-go'
];

const SERVICES = [
  'aluguel-de-empilhadeira-combustao',
  'aluguel-de-empilhadeira-eletrica',
  'aluguel-de-plataforma-elevatoria-articulada',
  'aluguel-de-plataforma-elevatoria-tesoura',
  'aluguel-de-transpaleteira',
  'venda-de-pecas-clark'
];

async function uploadFile(localPath, r2Path) {
  const url = `${ENDPOINT}/${BUCKET}/${r2Path}`;
  const body = readFileSync(localPath);

  if (DRY_RUN) {
    console.log(`  ✓ ${r2Path}`);
    console.log(`    → ${PUB_BASE}/${r2Path}`);
    return true;
  }

  try {
    const res = await client.fetch(url, {
      method: 'PUT',
      body,
      headers: { 'Content-Type': 'text/html; charset=utf-8' }
    });

    if (res.ok) {
      console.log(`  ✅ ${r2Path}`);
      return true;
    } else {
      const text = await res.text();
      console.error(`  ❌ ${r2Path} — ${res.status}: ${text}`);
      return false;
    }
  } catch (e) {
    console.error(`  ❌ ${r2Path} — ${e.message}`);
    return false;
  }
}

async function main() {
  console.log(`\n${DRY_RUN ? '🔍 DRY RUN' : '🚀 UPLOAD'} — Move Máquinas Schema Elite v2.0 → R2 /${R2_PREFIX}/\n`);

  let ok = 0, fail = 0, skipped = 0;
  const files = [];

  // Build file list: city hubs + services LPs
  for (const city of CITIES) {
    // City hub
    const hubPath = join(LOCAL_BASE, city, 'index.html');
    files.push({ local: hubPath, r2: `${R2_PREFIX}/${city}/index.html` });

    // Service LPs
    for (const service of SERVICES) {
      const lpPath = join(LOCAL_BASE, city, service, 'index.html');
      files.push({ local: lpPath, r2: `${R2_PREFIX}/${city}/${service}/index.html` });
    }
  }

  console.log(`Prepared ${files.length} files for upload\n`);

  for (const file of files) {
    try {
      readFileSync(file.local); // Check file exists
      const result = await uploadFile(file.local, file.r2);
      if (result) ok++;
      else fail++;
    } catch (e) {
      if (e.code === 'ENOENT') {
        skipped++;
      } else {
        console.error(`  ❌ ${file.r2} — ${e.message}`);
        fail++;
      }
    }
  }

  console.log(`\n${DRY_RUN ? 'DRY RUN' : 'UPLOAD'} complete:`);
  console.log(`  ✅ Success: ${ok}`);
  console.log(`  ⚠️  Skipped: ${skipped}`);
  console.log(`  ❌ Failed: ${fail}\n`);

  if (!DRY_RUN && ok > 0) {
    console.log(`🌐 Home: ${PUB_BASE}/${R2_PREFIX}/goiania-go/index.html\n`);
  }
}

main().catch(console.error);
