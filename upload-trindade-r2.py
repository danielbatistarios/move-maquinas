#!/usr/bin/env python3
"""Upload all 6 Trindade pages to R2."""

import boto3
from datetime import datetime

R2_ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
R2_ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET = 'pages'
BASE = '/Users/jrios/move-maquinas-seo'

s3 = boto3.client('s3',
    endpoint_url=R2_ENDPOINT,
    aws_access_key_id=R2_ACCESS_KEY,
    aws_secret_access_key=R2_SECRET_KEY,
    region_name='auto'
)

pages = [
    ('trindade-go-hub-V2.html', 'trindade-go/index.html'),
    ('trindade-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'trindade-go/aluguel-de-plataforma-elevatoria-articulada/index.html'),
    ('trindade-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'trindade-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'),
    ('trindade-go-aluguel-de-empilhadeira-combustao-V2.html', 'trindade-go/aluguel-de-empilhadeira-combustao/index.html'),
    ('trindade-go-aluguel-de-transpaleteira-V2.html', 'trindade-go/aluguel-de-transpaleteira/index.html'),
    ('trindade-go-curso-de-operador-de-empilhadeira-V2.html', 'trindade-go/curso-de-operador-de-empilhadeira/index.html'),
]

start = datetime.now()

for local_file, r2_key in pages:
    local_path = f'{BASE}/{local_file}'
    try:
        with open(local_path, 'rb') as f:
            content = f.read()
        s3.put_object(
            Bucket=R2_BUCKET,
            Key=r2_key,
            Body=content,
            ContentType='text/html; charset=utf-8',
        )
        size_kb = len(content) / 1024
        print(f'✓ {r2_key} ({size_kb:.0f} KB)')
    except Exception as e:
        print(f'✗ {r2_key}: {e}')

elapsed = datetime.now() - start
print(f'\nUpload concluído em {elapsed.total_seconds():.1f}s')
print(f'URL base: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/')
for _, key in pages:
    print(f'  https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{key}')
