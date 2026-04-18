#!/usr/bin/env python3
"""Upload 6 Inhumas pages to Cloudflare R2 using boto3."""
import subprocess, sys, os

# Try boto3 first, fall back to requests with AWS signature
try:
    import boto3
    from botocore.config import Config
except ImportError:
    print("Installing boto3...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'boto3', '-q'])
    import boto3
    from botocore.config import Config

ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
KEY = '9b8005782e2f6ebd197768fabe1e07c2'
SECRET = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
BUCKET = 'pages'
BASE = '/Users/jrios/move-maquinas-seo'

s3 = boto3.client('s3',
    endpoint_url=ENDPOINT,
    aws_access_key_id=KEY,
    aws_secret_access_key=SECRET,
    config=Config(signature_version='s3v4'),
    region_name='auto'
)

FILES = [
    ('inhumas-go-hub-V2.html', 'inhumas-go/index.html'),
    ('inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'inhumas-go/aluguel-de-plataforma-elevatoria-articulada/index.html'),
    ('inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'inhumas-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'),
    ('inhumas-go-aluguel-de-empilhadeira-combustao-V2.html', 'inhumas-go/aluguel-de-empilhadeira-combustao/index.html'),
    ('inhumas-go-aluguel-de-transpaleteira-V2.html', 'inhumas-go/aluguel-de-transpaleteira/index.html'),
    ('inhumas-go-curso-de-operador-de-empilhadeira-V2.html', 'inhumas-go/curso-de-operador-de-empilhadeira/index.html'),
]

ok = 0
fail = 0
for local, r2key in FILES:
    path = os.path.join(BASE, local)
    if not os.path.exists(path):
        print(f"SKIP {local} — not found")
        fail += 1
        continue
    try:
        with open(path, 'rb') as f:
            s3.put_object(
                Bucket=BUCKET,
                Key=r2key,
                Body=f.read(),
                ContentType='text/html; charset=utf-8',
                CacheControl='public, max-age=3600'
            )
        print(f"OK   {r2key}")
        ok += 1
    except Exception as e:
        print(f"ERR  {r2key} — {e}")
        fail += 1

print(f"\nDone: {ok} uploaded, {fail} failed")
print(f"URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/inhumas-go/")
