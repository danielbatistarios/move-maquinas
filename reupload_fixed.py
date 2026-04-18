import hashlib, hmac, datetime, urllib.request

R2_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET = 'pages'
DIR = '/Users/jrios/move-maquinas-seo'
SLUG = 'valparaiso-de-goias-go'

def upload(local_path, r2_key):
    with open(local_path, 'rb') as f:
        body = f.read()
    now = datetime.datetime.utcnow()
    ds = now.strftime('%Y%m%d')
    ad = now.strftime('%Y%m%dT%H%M%SZ')
    host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    ph = hashlib.sha256(body).hexdigest()
    cu = f'/{R2_BUCKET}/{r2_key}'
    ch = f'host:{host}\nx-amz-content-sha256:{ph}\nx-amz-date:{ad}\n'
    sh = 'host;x-amz-content-sha256;x-amz-date'
    cr = f'PUT\n{cu}\n\n{ch}\n{sh}\n{ph}'
    alg = 'AWS4-HMAC-SHA256'
    cs = f'{ds}/auto/s3/aws4_request'
    sts = f'{alg}\n{ad}\n{cs}\n{hashlib.sha256(cr.encode()).hexdigest()}'
    def s(k,m): return hmac.new(k, m.encode('utf-8'), hashlib.sha256).digest()
    sk = s(s(s(s(f'AWS4{R2_SECRET}'.encode(), ds), 'auto'), 's3'), 'aws4_request')
    sig = hmac.new(sk, sts.encode(), hashlib.sha256).hexdigest()
    auth = f'{alg} Credential={R2_KEY}/{cs}, SignedHeaders={sh}, Signature={sig}'
    req = urllib.request.Request(f'https://{host}{cu}', data=body, method='PUT')
    req.add_header('Host', host)
    req.add_header('x-amz-date', ad)
    req.add_header('x-amz-content-sha256', ph)
    req.add_header('Authorization', auth)
    req.add_header('Content-Type', 'text/html; charset=utf-8')
    req.add_header('Cache-Control', 'public, max-age=3600')
    resp = urllib.request.urlopen(req)
    print(f'OK: {r2_key} ({resp.status})')

uploads = [
    (f'{DIR}/valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html', f'{SLUG}/aluguel-de-plataforma-elevatoria-tesoura/index.html'),
    (f'{DIR}/valparaiso-de-goias-go-aluguel-de-empilhadeira-combustao-V2.html', f'{SLUG}/aluguel-de-empilhadeira-combustao/index.html'),
    (f'{DIR}/valparaiso-de-goias-go-aluguel-de-transpaleteira-V2.html', f'{SLUG}/aluguel-de-transpaleteira/index.html'),
]

for local, r2 in uploads:
    upload(local, r2)
