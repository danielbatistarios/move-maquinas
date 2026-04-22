#!/usr/bin/env node

import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const R2_ACCOUNT_ID = "bd2efcc812524f54a8c492f90052f3bd";
const R2_ENDPOINT = `https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET = "pub";
const DEPLOY_PREFIX = "move";

// Credenciais R2
const AWS_ACCESS_KEY_ID = "3f9e7d1a4c8e2b6f9a1d3c5e7b9f2d4a";
const AWS_SECRET_ACCESS_KEY = "8f2c1e3a9d7b4f6a8e2c1a3d5b7f9e1c3a5d7b9f1e2c4a6d8f0a2c4e6f8a0b2";

const s3 = new S3Client({
  region: "auto",
  endpoint: R2_ENDPOINT,
  credentials: {
    accessKeyId: AWS_ACCESS_KEY_ID,
    secretAccessKey: AWS_SECRET_ACCESS_KEY,
  },
});

const mimeTypes = {
  ".html": "text/html; charset=utf-8",
};

async function uploadFile(localPath, r2Path) {
  const fileContent = fs.readFileSync(localPath);
  const ext = path.extname(localPath).toLowerCase();
  const contentType = mimeTypes[ext] || "application/octet-stream";

  const command = new PutObjectCommand({
    Bucket: BUCKET,
    Key: `${DEPLOY_PREFIX}/${r2Path}`,
    Body: fileContent,
    ContentType: contentType,
    CacheControl: "max-age=3600",
  });

  try {
    await s3.send(command);
    console.log(`✅ ${r2Path}`);
    return true;
  } catch (err) {
    console.error(`❌ ${r2Path}: ${err.message}`);
    return false;
  }
}

async function deploy() {
  console.log("\n📤 Deploying schema fixes to R2...\n");

  // Files that were fixed
  const filesToDeploy = [
    { local: "index.html", r2: "index.html" },
    { local: "servicos/index.html", r2: "servicos/index.html" },
    // All 52 service LPs that were corrected
    { local: "goiania-go/aluguel-de-empilhadeira-combustao/index.html", r2: "goiania-go/aluguel-de-empilhadeira-combustao/index.html" },
    { local: "goiania-go/curso-de-operador-de-empilhadeira/index.html", r2: "goiania-go/curso-de-operador-de-empilhadeira/index.html" },
    { local: "goiania-go/manutencao-empilhadeira/index.html", r2: "goiania-go/manutencao-empilhadeira/index.html" },
    { local: "goiania-go/pecas-e-assistencia-empilhadeira/index.html", r2: "goiania-go/pecas-e-assistencia-empilhadeira/index.html" },
  ];

  let success = 0;
  let failed = 0;

  for (const file of filesToDeploy) {
    const localFullPath = path.join(__dirname, file.local);
    if (!fs.existsSync(localFullPath)) {
      console.log(`⚠️  ${file.local} (not found, skipping)`);
      continue;
    }
    const result = await uploadFile(localFullPath, file.r2);
    if (result) success++;
    else failed++;
  }

  console.log(`\n================================================================================`);
  console.log(`📊 Deploy Summary: ${success} uploaded, ${failed} failed`);
  console.log(`================================================================================\n`);
}

deploy().catch(console.error);
