#!/usr/bin/env python3
"""Upload Inhumas tesoura V2 to R2."""
import hashlib, hmac, datetime, urllib.request, urllib.error

ENDPOINT = 'https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
ACCESS_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
SECRET_KEY = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
BUCKET = 'pages'
KEY = 'inhumas-go/aluguel-de-plataforma-elevatoria-tesoura/index.html'
FILE = '/Users/jrios/move-maquinas-seo/inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'

with open(FILE, 'rb') as f:
    body = f.read()

now = datetime.datetime.utcnow()
datestamp = now.strftime('%Y%m%d')
amzdate = now.strftime('%Y%m%dT%H%M%SZ')
region = 'auto'
service = 's3'
host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'

payload_hash = hashlib.sha256(body).hexdigest()
canonical_uri = '/' + BUCKET + '/' + KEY

canonical_headers = (
    'content-type:text/html\n'
    'host:' + host + '\n'
    'x-amz-content-sha256:' + payload_hash + '\n'
    'x-amz-date:' + amzdate + '\n'
)
signed_headers = 'content-type;host;x-amz-content-sha256;x-amz-date'

canonical_request = '\n'.join([
    'PUT', canonical_uri, '',
    canonical_headers, signed_headers, payload_hash
])

algorithm = 'AWS4-HMAC-SHA256'
credential_scope = '/'.join([datestamp, region, service, 'aws4_request'])
string_to_sign = '\n'.join([
    algorithm, amzdate, credential_scope,
    hashlib.sha256(canonical_request.encode()).hexdigest()
])

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

signing_key = sign(sign(sign(sign(
    ('AWS4' + SECRET_KEY).encode('utf-8'), datestamp),
    region), service), 'aws4_request')

signature = hmac.new(
    signing_key, string_to_sign.encode('utf-8'), hashlib.sha256
).hexdigest()

authorization = (
    algorithm + ' Credential=' + ACCESS_KEY + '/' + credential_scope +
    ', SignedHeaders=' + signed_headers +
    ', Signature=' + signature
)

url = ENDPOINT + '/' + BUCKET + '/' + KEY
req = urllib.request.Request(url, data=body, method='PUT')
req.add_header('Content-Type', 'text/html')
req.add_header('x-amz-content-sha256', payload_hash)
req.add_header('x-amz-date', amzdate)
req.add_header('Authorization', authorization)
req.add_header('Cache-Control', 'public, max-age=3600')

try:
    resp = urllib.request.urlopen(req)
    print('Upload OK: ' + str(resp.status))
    print('URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/' + KEY)
except urllib.error.HTTPError as e:
    print('Erro ' + str(e.code) + ': ' + e.read().decode()[:500])
