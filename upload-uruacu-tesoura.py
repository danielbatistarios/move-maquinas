#!/usr/bin/env python3
"""Upload uruacu tesoura V2 to Cloudflare R2"""
import hashlib, hmac, datetime, urllib.request

access_key = '9b8005782e2f6ebd197768fabe1e07c2'
secret_key = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
endpoint = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
bucket = 'pages'
key = 'uruacu-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'
host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'

with open('/Users/jrios/move-maquinas-seo/uruacu-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'rb') as f:
    body = f.read()

now = datetime.datetime.utcnow()
ds = now.strftime('%Y%m%d')
amz = now.strftime('%Y%m%dT%H%M%SZ')
ph = hashlib.sha256(body).hexdigest()

def sign(k, m):
    return hmac.new(k, m.encode('utf-8'), hashlib.sha256).digest()

sk = sign(sign(sign(sign(('AWS4'+secret_key).encode('utf-8'), ds), 'auto'), 's3'), 'aws4_request')

cr = f'PUT\n/{bucket}/{key}\n\ncontent-type:text/html; charset=utf-8\nhost:{host}\nx-amz-content-sha256:{ph}\nx-amz-date:{amz}\n\ncontent-type;host;x-amz-content-sha256;x-amz-date\n{ph}'
cs = f'{ds}/auto/s3/aws4_request'
sts = f'AWS4-HMAC-SHA256\n{amz}\n{cs}\n{hashlib.sha256(cr.encode()).hexdigest()}'
sig = hmac.new(sk, sts.encode('utf-8'), hashlib.sha256).hexdigest()
auth = f'AWS4-HMAC-SHA256 Credential={access_key}/{cs}, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date, Signature={sig}'

req = urllib.request.Request(
    f'{endpoint}/{bucket}/{key}',
    data=body,
    headers={
        'Content-Type': 'text/html; charset=utf-8',
        'x-amz-content-sha256': ph,
        'x-amz-date': amz,
        'Authorization': auth,
        'Cache-Control': 'public, max-age=3600',
    },
    method='PUT'
)
try:
    with urllib.request.urlopen(req) as r:
        print(f'Upload OK: {r.status}')
        print(f'URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{key}')
except urllib.error.HTTPError as e:
    print(f'FAILED: {e.code} {e.reason}')
    print(e.read().decode()[:500])
