#!/usr/bin/env python3
"""Upload Formosa tesoura V2 to Cloudflare R2."""

import urllib.request, hashlib, hmac, datetime

ENDPOINT = "https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com"
ACCESS_KEY = "9b8005782e2f6ebd197768fabe1e07c2"
SECRET_KEY = "05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093"
BUCKET = "pages"
R2_KEY = "formosa-go/aluguel-de-plataforma-elevatoria-tesoura/index.html"

with open("/Users/jrios/move-maquinas-seo/formosa-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html", "rb") as f:
    body = f.read()

now = datetime.datetime.utcnow()
datestamp = now.strftime("%Y%m%d")
amzdate = now.strftime("%Y%m%dT%H%M%SZ")
region = "auto"
service = "s3"
content_hash = hashlib.sha256(body).hexdigest()
canonical_uri = f"/{BUCKET}/{R2_KEY}"
host = "842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com"
headers_to_sign = {"host": host, "x-amz-content-sha256": content_hash, "x-amz-date": amzdate, "content-type": "text/html; charset=utf-8"}
signed_headers = ";".join(sorted(headers_to_sign.keys()))
canonical_headers = "".join(f"{k}:{headers_to_sign[k]}\n" for k in sorted(headers_to_sign.keys()))
canonical_request = f"PUT\n{canonical_uri}\n\n{canonical_headers}\n{signed_headers}\n{content_hash}"
credential_scope = f"{datestamp}/{region}/{service}/aws4_request"
string_to_sign = f"AWS4-HMAC-SHA256\n{amzdate}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode()).hexdigest()}"

def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

signing_key = sign(sign(sign(sign(("AWS4" + SECRET_KEY).encode("utf-8"), datestamp), region), service), "aws4_request")
signature = hmac.new(signing_key, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
authorization = f"AWS4-HMAC-SHA256 Credential={ACCESS_KEY}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}"

url = f"{ENDPOINT}/{BUCKET}/{R2_KEY}"
req = urllib.request.Request(url, data=body, method="PUT")
req.add_header("Authorization", authorization)
req.add_header("x-amz-content-sha256", content_hash)
req.add_header("x-amz-date", amzdate)
req.add_header("Content-Type", "text/html; charset=utf-8")
req.add_header("Host", host)

try:
    resp = urllib.request.urlopen(req)
    print(f"Upload OK: {resp.status}")
    print(f"URL: https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/{R2_KEY}")
except Exception as e:
    print(f"Upload FAILED: {e}")
    if hasattr(e, "read"):
        print(e.read().decode()[:500])
