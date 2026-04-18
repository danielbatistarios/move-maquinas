#!/usr/bin/env python3
"""
upload-formosa.py
Upload all 6 Formosa pages to R2 and print summary.
"""

import subprocess, time, os
from datetime import datetime

START = datetime.now()
BASE = '/Users/jrios/move-maquinas-seo'

R2_ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
R2_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET = 'pages'

# Configure AWS CLI for R2
env = os.environ.copy()
env['AWS_ACCESS_KEY_ID'] = R2_KEY
env['AWS_SECRET_ACCESS_KEY'] = R2_SECRET
env['AWS_DEFAULT_REGION'] = 'auto'

def upload(local_path, r2_key):
    cmd = [
        'aws', 's3', 'cp', local_path,
        f's3://{R2_BUCKET}/{r2_key}',
        '--endpoint-url', R2_ENDPOINT,
        '--content-type', 'text/html; charset=utf-8',
        '--cache-control', 'public, max-age=3600'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode == 0:
        print(f"  OK: {r2_key}")
    else:
        print(f"  FAIL: {r2_key} — {result.stderr[:200]}")
    return result.returncode == 0

pages = [
    ('formosa-go-hub-V2.html', 'formosa-go/index.html'),
    ('formosa-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', 'formosa-go/aluguel-de-plataforma-elevatoria-articulada/index.html'),
    ('formosa-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', 'formosa-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'),
    ('formosa-go-aluguel-de-empilhadeira-combustao-V2.html', 'formosa-go/aluguel-de-empilhadeira-combustao/index.html'),
    ('formosa-go-aluguel-de-transpaleteira-V2.html', 'formosa-go/aluguel-de-transpaleteira/index.html'),
    ('formosa-go-curso-de-operador-de-empilhadeira-V2.html', 'formosa-go/curso-de-operador-de-empilhadeira/index.html'),
]

print("="*60)
print("UPLOADING FORMOSA PAGES TO R2")
print("="*60)

success = 0
for local_name, r2_key in pages:
    local_path = f'{BASE}/{local_name}'
    if os.path.exists(local_path):
        if upload(local_path, r2_key):
            success += 1
    else:
        print(f"  MISSING: {local_path}")

elapsed = datetime.now() - START
print(f"\n{'='*60}")
print(f"UPLOADED: {success}/{len(pages)}")
print(f"TEMPO UPLOAD: {int(elapsed.total_seconds())}s")
print(f"{'='*60}")

# Print URLs
print("\nDEV URLs:")
for _, r2_key in pages:
    print(f"  https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{r2_key}")
