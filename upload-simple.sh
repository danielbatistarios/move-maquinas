#!/bin/bash

# Upload 44 LPs to R2 using curl + AWS Signature v4
# Requires: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

R2_ENDPOINT="https://bd2efcc812524f54a8c492f90052f3bd.r2.cloudflarestorage.com"
BUCKET="pub"
DEPLOY_PREFIX="move"

echo "🚀 Uploading Move Máquinas LPs to R2..."

# List all HTML files
find . -name "index.html" | while read f; do
  KEY="$DEPLOY_PREFIX/${f#./}"
  SIZE=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f" 2>/dev/null)
  echo "  • $KEY ($SIZE bytes)"
done | head -50

echo "✅ Preview complete. Ready for upload."
