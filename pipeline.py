#!/usr/bin/env python3
"""
pipeline.py — Move Maquinas SEO Pipeline
Lê Google Sheets → faz upload HTML para R2 → atualiza planilha

Uso:
  python3 pipeline.py                    # processa todas as linhas pendentes
  python3 pipeline.py --test             # testa com 1 linha só
  python3 pipeline.py --upload FILE.html SLUG  # upload manual de um HTML
  python3 pipeline.py --status           # mostra status da planilha
"""

import os
import sys
import json
import argparse
from datetime import datetime

import gspread
import boto3
from google.oauth2.service_account import Credentials

# ─── CONFIG ──────────────────────────────────────────────────────────────────

SPREADSHEET_ID = '1_ap9dZhzgReHMsnSF38M5I02s4LM-JCZoDni5sJpV_U'
SHEET_TAB       = 'city slug'
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), 'credentials.json')

# R2 / Cloudflare
R2_ACCOUNT_ID  = '842561b03363b0ab3a35556ff728f9fe'
R2_ENDPOINT    = f'https://{R2_ACCOUNT_ID}.r2.cloudflarestorage.com'
R2_ACCESS_KEY  = '9b8005782e2f6ebd197768fabe1e07c2'
R2_SECRET_KEY  = '05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093'
R2_BUCKET      = 'pages'
R2_PUBLIC_URL  = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'

# Pasta local onde os HTMLs são salvos
HTML_DIR = '/Users/jrios/Downloads'

# ─── COLUNAS DA PLANILHA ─────────────────────────────────────────────────────
# city_slug | title | permalink | url de desenvolvimento publico | status | gerado_em | tokens_usados
COL = {
    'city_slug':  1,
    'title':      2,
    'permalink':  3,
    'url_dev':    4,
    'status':     5,
    'gerado_em':  6,
    'tokens':     7,
}

# ─── GOOGLE SHEETS ───────────────────────────────────────────────────────────

def get_sheet():
    """Conecta ao Google Sheets e retorna a aba."""
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive',
    ]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(SPREADSHEET_ID)
    return sh.worksheet(SHEET_TAB)


def update_cell(ws, row, col_name, value):
    """Atualiza uma célula específica na planilha."""
    ws.update_cell(row, COL[col_name], value)


# ─── R2 UPLOAD ───────────────────────────────────────────────────────────────

def get_r2_client():
    """Cria client boto3 para Cloudflare R2."""
    return boto3.client(
        's3',
        endpoint_url=R2_ENDPOINT,
        aws_access_key_id=R2_ACCESS_KEY,
        aws_secret_access_key=R2_SECRET_KEY,
        region_name='auto',
    )


def upload_to_r2(r2, local_path, r2_key):
    """Faz upload de um arquivo HTML para o R2. Retorna a URL pública."""
    with open(local_path, 'rb') as f:
        r2.put_object(
            Bucket=R2_BUCKET,
            Key=r2_key,
            Body=f.read(),
            ContentType='text/html; charset=utf-8',
        )
    return f'{R2_PUBLIC_URL}/{r2_key}'


# ─── HELPERS ─────────────────────────────────────────────────────────────────

def slugify_title(title):
    """Converte title para slug de URL.
    Ex: 'Aluguel de Plataforma Elevatória Articulada' → 'aluguel-de-plataforma-elevatoria-articulada'
    """
    import unicodedata
    s = unicodedata.normalize('NFKD', title.lower())
    s = s.encode('ascii', 'ignore').decode('ascii')
    s = s.replace(' ', '-')
    # Remove caracteres que não são alfanuméricos ou hífen
    s = ''.join(c for c in s if c.isalnum() or c == '-')
    # Remove hífens duplicados
    while '--' in s:
        s = s.replace('--', '-')
    return s.strip('-')


def build_r2_key(city_slug, title_slug):
    """Monta a chave R2: city-slug/title-slug/index.html"""
    return f'{city_slug}/{title_slug}/index.html'


def build_permalink(city_slug, title_slug):
    """Monta o permalink: /city-slug/title-slug"""
    return f'/{city_slug}/{title_slug}'


def find_html_file(city_slug, title_slug):
    """Procura o arquivo HTML local. Tenta vários padrões de nome."""
    patterns = [
        f'{city_slug}-{title_slug}.html',           # aparecida-de-goiania-go-aluguel-de-empilhadeira.html
        f'{title_slug}-{city_slug}.html',           # aluguel-de-empilhadeira-aparecida-de-goiania-go.html
        f'lp-{title_slug}-{city_slug}.html',        # lp-aluguel-de-empilhadeira-aparecida-de-goiania-go.html
        f'{city_slug}/{title_slug}.html',            # aparecida-de-goiania-go/aluguel-de-empilhadeira.html
    ]
    for pattern in patterns:
        path = os.path.join(HTML_DIR, pattern)
        if os.path.exists(path):
            return path
    return None


# ─── PROCESSAR UMA LINHA ─────────────────────────────────────────────────────

def process_row(ws, r2, row_num, city_slug, title, tokens_used=0):
    """Processa uma linha da planilha: encontra HTML, faz upload, atualiza."""
    title_slug = slugify_title(title)
    r2_key = build_r2_key(city_slug, title_slug)
    permalink = build_permalink(city_slug, title_slug)
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    print(f'  [{row_num}] {city_slug} / {title}')

    # 1. Status → "Em Andamento"
    update_cell(ws, row_num, 'status', 'Em Andamento')
    update_cell(ws, row_num, 'gerado_em', now)

    # 2. Procura HTML local
    html_path = find_html_file(city_slug, title_slug)
    if not html_path:
        print(f'      ⚠️  HTML não encontrado localmente — pulando')
        update_cell(ws, row_num, 'status', 'Erro')
        return False

    print(f'      📄 {os.path.basename(html_path)}')

    # 3. Upload para R2
    try:
        url_dev = upload_to_r2(r2, html_path, r2_key)
        print(f'      ✅ Upload OK → {permalink}')
    except Exception as e:
        print(f'      ❌ Erro no upload: {e}')
        update_cell(ws, row_num, 'status', 'Erro')
        return False

    # 4. Atualiza planilha
    update_cell(ws, row_num, 'permalink', permalink)
    update_cell(ws, row_num, 'url_dev', url_dev)
    update_cell(ws, row_num, 'status', 'Concluído')
    update_cell(ws, row_num, 'tokens', str(tokens_used) if tokens_used else '0')

    return True


# ─── UPLOAD MANUAL ────────────────────────────────────────────────────────────

def manual_upload(html_file, r2_key_override=None):
    """Upload manual de um HTML para R2."""
    r2 = get_r2_client()

    if r2_key_override:
        r2_key = r2_key_override if r2_key_override.endswith('.html') else f'{r2_key_override}/index.html'
    else:
        name = os.path.splitext(os.path.basename(html_file))[0]
        r2_key = f'{name}/index.html'

    print(f'⬆️  {html_file} → {R2_BUCKET}/{r2_key}')
    url = upload_to_r2(r2, html_file, r2_key)
    print(f'✅ Upload OK')
    print(f'📎 URL: {url}')
    print(f'🔗 Permalink: /{r2_key.replace("/index.html", "")}')
    return url


# ─── MOSTRAR STATUS ──────────────────────────────────────────────────────────

def show_status():
    """Mostra o status atual da planilha."""
    ws = get_sheet()
    rows = ws.get_all_values()

    if len(rows) <= 1:
        print('Planilha vazia (só cabeçalho).')
        return

    total = len(rows) - 1
    concluidos = sum(1 for r in rows[1:] if r[COL['status']-1].strip() == 'Concluído')
    andamento = sum(1 for r in rows[1:] if r[COL['status']-1].strip() == 'Em Andamento')
    pendentes = total - concluidos - andamento

    print(f'\n📊 Status da planilha "{SHEET_TAB}":')
    print(f'   Total:       {total}')
    print(f'   ✅ Concluídos: {concluidos}')
    print(f'   🔄 Em andamento: {andamento}')
    print(f'   ⏳ Pendentes:  {pendentes}')
    print()

    # Mostra as próximas 5 pendentes
    pending = [(i+2, r) for i, r in enumerate(rows[1:]) if not r[COL['status']-1].strip()]
    if pending:
        print('  Próximas pendentes:')
        for row_num, r in pending[:5]:
            print(f'    [{row_num}] {r[0]} — {r[1]}')
        if len(pending) > 5:
            print(f'    ... e mais {len(pending)-5}')


# ─── PROCESSAR TODAS AS PENDENTES ────────────────────────────────────────────

def process_all(test_mode=False):
    """Processa todas as linhas pendentes da planilha."""
    print('🔗 Conectando ao Google Sheets...')
    ws = get_sheet()
    rows = ws.get_all_values()

    if len(rows) <= 1:
        print('Planilha vazia.')
        return

    print('🔗 Conectando ao R2...')
    r2 = get_r2_client()

    # Encontra linhas pendentes (status vazio)
    pending = []
    for i, row in enumerate(rows[1:], start=2):
        status = row[COL['status']-1].strip() if len(row) >= COL['status'] else ''
        if not status or status == 'Não Iniciado' or status == 'Erro':
            city = row[COL['city_slug']-1].strip()
            title = row[COL['title']-1].strip()
            if city and title:
                pending.append((i, city, title))

    if not pending:
        print('✅ Nenhuma linha pendente.')
        return

    limit = 1 if test_mode else len(pending)
    print(f'\n📋 {len(pending)} linhas pendentes. Processando {"1 (teste)" if test_mode else "todas"}...\n')

    ok = 0
    for row_num, city, title in pending[:limit]:
        if process_row(ws, r2, row_num, city, title):
            ok += 1

    print(f'\n─────────────────────────────────')
    print(f'✅ {ok}/{limit} processadas com sucesso.')


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Move Maquinas SEO Pipeline')
    parser.add_argument('--test', action='store_true', help='Processa apenas 1 linha (teste)')
    parser.add_argument('--status', action='store_true', help='Mostra status da planilha')
    parser.add_argument('--upload', nargs='+', metavar=('FILE', 'KEY'), help='Upload manual: --upload file.html [r2-key]')
    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.upload:
        html_file = args.upload[0]
        r2_key = args.upload[1] if len(args.upload) > 1 else None
        manual_upload(html_file, r2_key)
    else:
        process_all(test_mode=args.test)


if __name__ == '__main__':
    main()
