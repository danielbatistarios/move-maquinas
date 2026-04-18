#!/usr/bin/env python3
"""Upload Formosa pages to R2 using boto3 or raw HTTP."""

import hashlib, hmac, datetime, urllib.request, urllib.error, os

BASE = '/Users/jrios/move-maquinas-seo'
ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
BUCKET = 'pages'
REGION = 'auto'
SERVICE = 's3'

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def get_signature_key(key, date_stamp, region, service):
    k = sign(('AWS4' + key).encode('utf-8'), date_stamp)
    k = sign(k, region)
    k = sign(k, service)
    k = sign(k, 'aws4_request')
    return k

def upload_to_r2(local_path, r2_key):
    with open(local_path, 'rb') as f:
        payload = f.read()

    t = datetime.datetime.utcnow()
    amz_date = t.strftime('%Y%m%dT%H%M%SZ')
    date_stamp = t.strftime('%Y%m%d')

    host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    url = f'{ENDPOINT}/{BUCKET}/{r2_key}'

    payload_hash = hashlib.sha256(payload).hexdigest()

    headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'public, max-age=3600',
        'x-amz-content-sha256': payload_hash,
        'x-amz-date': amz_date,
        'Host': host,
    }

    # Canonical request
    canonical_uri = f'/{BUCKET}/{r2_key}'
    canonical_querystring = ''
    signed_headers_list = sorted(headers.keys(), key=str.lower)
    signed_headers = ';'.join(h.lower() for h in signed_headers_list)
    canonical_headers = ''.join(f'{h.lower()}:{headers[h].strip()}\n' for h in signed_headers_list)

    canonical_request = f'PUT\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{payload_hash}'
    cr_hash = hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

    credential_scope = f'{date_stamp}/{REGION}/{SERVICE}/aws4_request'
    string_to_sign = f'AWS4-HMAC-SHA256\n{amz_date}\n{credential_scope}\n{cr_hash}'

    signing_key = get_signature_key(SECRET_KEY, date_stamp, REGION, SERVICE)
    signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

    auth_header = f'AWS4-HMAC-SHA256 Credential={ACCESS_KEY}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'
    headers['Authorization'] = auth_header

    req = urllib.request.Request(url, data=payload, headers=headers, method='PUT')
    try:
        resp = urllib.request.urlopen(req)
        print(f"  OK ({resp.status}): {r2_key}")
        return True
    except urllib.error.HTTPError as e:
        print(f"  FAIL ({e.code}): {r2_key} — {e.read().decode()[:200]}")
        return False

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
        if upload_to_r2(local_path, r2_key):
            success += 1
    else:
        print(f"  MISSING: {local_path}")

print(f"\nUPLOADED: {success}/{len(pages)}")
print("\nDEV URLs:")
for _, r2_key in pages:
    print(f"  https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{r2_key}")
