import re, os, hashlib, hmac, datetime, urllib.request

DIR = '/Users/jrios/move-maquinas-seo'
SLUG = 'valparaiso-de-goias-go'
R2_KEY = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET = 'pages'

def upload_to_r2(local_path, r2_key):
    with open(local_path, 'rb') as f:
        body = f.read()
    now = datetime.datetime.utcnow()
    date_stamp = now.strftime('%Y%m%d')
    amz_date = now.strftime('%Y%m%dT%H%M%SZ')
    host = '842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com'
    region, service = 'auto', 's3'
    payload_hash = hashlib.sha256(body).hexdigest()
    canonical_uri = f'/{R2_BUCKET}/{r2_key}'
    canonical_headers = f'host:{host}\nx-amz-content-sha256:{payload_hash}\nx-amz-date:{amz_date}\n'
    signed_headers = 'host;x-amz-content-sha256;x-amz-date'
    canonical_request = f'PUT\n{canonical_uri}\n\n{canonical_headers}\n{signed_headers}\n{payload_hash}'
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = f'{date_stamp}/{region}/{service}/aws4_request'
    string_to_sign = f'{algorithm}\n{amz_date}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode()).hexdigest()}'
    def sign(key, msg): return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
    signing_key = sign(sign(sign(sign(f'AWS4{R2_SECRET}'.encode('utf-8'), date_stamp), region), service), 'aws4_request')
    signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
    authorization = f'{algorithm} Credential={R2_KEY}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'
    url = f'https://{host}{canonical_uri}'
    req = urllib.request.Request(url, data=body, method='PUT')
    req.add_header('Host', host)
    req.add_header('x-amz-date', amz_date)
    req.add_header('x-amz-content-sha256', payload_hash)
    req.add_header('Authorization', authorization)
    req.add_header('Content-Type', 'text/html; charset=utf-8')
    req.add_header('Cache-Control', 'public, max-age=3600')
    resp = urllib.request.urlopen(req)
    print(f'R2 OK: {r2_key} ({resp.status})')

upload_to_r2(f'{DIR}/valparaiso-de-goias-go-hub-V2.html', f'{SLUG}/index.html')
upload_to_r2(f'{DIR}/valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-articulada-V2.html', f'{SLUG}/aluguel-de-plataforma-elevatoria-articulada/index.html')

def txt(h):
    t = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
    t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t).strip().lower()
def ng(s): return set(s[i:i+3] for i in range(len(s)-2))
def j(a,b):
    ga,gb=ng(a),ng(b)
    return len(ga&gb)/len(ga|gb) if ga and gb else 0

print('\nFINAL TEXT-ONLY JACCARD:')
for name,rf,nf in [
    ('hub','ref-goiania-hub.html','valparaiso-de-goias-go-hub-V2.html'),
    ('art','ref-goiania-articulada.html','valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-articulada-V2.html'),
    ('tes','ref-goiania-tesoura.html','valparaiso-de-goias-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html'),
    ('com','ref-goiania-combustao.html','valparaiso-de-goias-go-aluguel-de-empilhadeira-combustao-V2.html'),
    ('tra','ref-goiania-transpaleteira.html','valparaiso-de-goias-go-aluguel-de-transpaleteira-V2.html'),
    ('cur','ref-goiania-curso.html','valparaiso-de-goias-go-curso-de-operador-de-empilhadeira-V2.html'),
]:
    a,b = txt(open(f'{DIR}/{rf}').read()), txt(open(f'{DIR}/{nf}').read())
    print(f'  {name}: {j(a,b):.4f}')
