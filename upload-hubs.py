#!/usr/bin/env python3
"""
upload-hubs.py — Faz upload dos 13 hubs de cidade para o R2
"""
import boto3, os

ROOT = '/Users/jrios/move-maquinas-seo'
R2_ACCOUNT_ID = '842561b03363b0ab3a35556ff728f9fe'
R2_ENDPOINT   = f'https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com'
R2_ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET     = 'pages'
R2_PUBLIC_URL = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'

HUBS = [
    'goiania-go',
    'senador-canedo-go',
    'brasilia-df',
    'luziania-go',
    'trindade-go',
    'inhumas-go',
    'itumbiara-go',
    'caldas-novas-go',
    'formosa-go',
    'uruacu-go',
    'valparaiso-de-goias-go',
    'aparecida-de-goiania-go',
    'anapolis-go',
]

s3 = boto3.client(
    's3',
    endpoint_url=R2_ENDPOINT,
    aws_access_key_id=R2_ACCESS_KEY,
    aws_secret_access_key=R2_SECRET_KEY,
    region_name='auto',
)

print('=== Upload hubs de cidade para R2 ===\n')
for slug in HUBS:
    html_path = os.path.join(ROOT, slug, 'index.html')
    css_path  = os.path.join(ROOT, slug, 'styles-cbb654b2.css')

    # Upload index.html
    with open(html_path, 'rb') as f:
        s3.put_object(
            Bucket=R2_BUCKET,
            Key=f'{slug}/index.html',
            Body=f.read(),
            ContentType='text/html; charset=utf-8',
        )

    # Upload CSS (se existir na pasta do hub)
    if os.path.exists(css_path):
        with open(css_path, 'rb') as f:
            s3.put_object(
                Bucket=R2_BUCKET,
                Key=f'{slug}/styles-cbb654b2.css',
                Body=f.read(),
                ContentType='text/css; charset=utf-8',
            )
        css_status = '+ CSS'
    else:
        css_status = '(sem CSS local)'

    print(f'  OK  {slug}  {css_status}')
    print(f'      {R2_PUBLIC_URL}/{slug}/index.html')

print('\nDone.')
