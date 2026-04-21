#!/usr/bin/env node

import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";
import * as readline from "readline";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const R2_ACCOUNT_ID = "bd2efcc812524f54a8c492f90052f3bd";
const R2_ENDPOINT = `https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com`;
const BUCKET = "pub";
const DEPLOY_PREFIX = "move";

const AWS_ACCESS_KEY_ID = process.env.R2_ACCESS_KEY;
const AWS_SECRET_ACCESS_KEY = process.env.R2_SECRET_KEY;

if (!AWS_ACCESS_KEY_ID || !AWS_SECRET_ACCESS_KEY) {
  console.error("❌ R2_ACCESS_KEY or R2_SECRET_KEY not set");
  process.exit(1);
}

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
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".webp": "image/webp",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".woff2": "font/woff2",
  ".woff": "font/woff",
  ".ttf": "font/ttf",
  ".map": "application/json",
};

function getMimeType(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  return mimeTypes[ext] || "application/octet-stream";
}

async function uploadFile(localPath, s3Key) {
  const fileContent = fs.readFileSync(localPath);
  const contentType = getMimeType(localPath);

  const params = {
    Bucket: BUCKET,
    Key: s3Key,
    Body: fileContent,
    ContentType: contentType,
    CacheControl: localPath.includes("/assets/") ? "max-age=31536000" : "max-age=3600",
  };

  try {
    await s3.send(new PutObjectCommand(params));
    const url = `https://pub-${R2_ACCOUNT_ID}.r2.dev/${s3Key}`;
    return { success: true, url };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

function walkDir(dir, fileList = []) {
  const files = fs.readdirSync(dir);

  files.forEach((file) => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (
      stat.isDirectory() &&
      !file.startsWith(".") &&
      file !== "node_modules"
    ) {
      walkDir(filePath, fileList);
    } else if (stat.isFile() && !file.startsWith(".")) {
      fileList.push(filePath);
    }
  });

  return fileList;
}

function getRelativePath(filePath) {
  return path.relative(__dirname, filePath).replace(/\\/g, "/");
}

async function main() {
  const dryRun = process.argv.includes("--dry-run");
  const mode = dryRun ? "DRY RUN" : "DEPLOY";

  console.log(`\n🚀 Move Máquinas → R2 /${DEPLOY_PREFIX}/ (${mode})\n`);

  const allFiles = walkDir(__dirname);
  const filesToUpload = allFiles.filter((f) => {
    const rel = getRelativePath(f);
    return (
      (f.endsWith(".html") ||
        f.endsWith(".css") ||
        f.endsWith(".js") ||
        f.endsWith(".json") ||
        f.endsWith(".webp") ||
        f.endsWith(".jpg") ||
        f.endsWith(".png") ||
        f.endsWith(".svg") ||
        f.endsWith(".woff2")) &&
      !rel.startsWith("node_modules") &&
      !rel.startsWith(".git")
    );
  });

  console.log(`Found ${filesToUpload.length} files to upload\n`);

  let successCount = 0;
  let failureCount = 0;

  for (const filePath of filesToUpload) {
    const relativePath = getRelativePath(filePath);
    const s3Key = `${DEPLOY_PREFIX}/${relativePath}`;
    const url = `https://pub-${R2_ACCOUNT_ID}.r2.dev/${s3Key}`;

    if (dryRun) {
      console.log(`  ✓ ${relativePath}`);
      console.log(`    → ${url}`);
    } else {
      const result = await uploadFile(filePath, s3Key);
      if (result.success) {
        console.log(`  ✓ ${relativePath}`);
        successCount++;
      } else {
        console.log(`  ✗ ${relativePath}: ${result.error}`);
        failureCount++;
      }
    }
  }

  console.log(`\n${dryRun ? "DRY RUN COMPLETE" : "UPLOAD COMPLETE"}`);
  if (!dryRun) {
    console.log(`✅ Uploaded: ${successCount}`);
    console.log(`❌ Failed: ${failureCount}\n`);
  }
}

main().catch(console.error);
