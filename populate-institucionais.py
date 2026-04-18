#!/usr/bin/env python3
"""
populate-institucionais.py
Popula a aba "paginas institucionais" no Google Sheets da Move Maquinas.

Uso:
  python3 populate-institucionais.py
"""

import os
import gspread
from google.oauth2.service_account import Credentials

# ─── CONFIG ──────────────────────────────────────────────────────────────────

SPREADSHEET_ID   = '1_ap9dZhzgReHMsnSF38M5I02s4LM-JCZoDni5sJpV_U'
SHEET_TAB        = 'paginas institucionais'
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), 'credentials.json')

# ─── DADOS ───────────────────────────────────────────────────────────────────

HEADER = [
    'Prioridade',
    'Categoria',
    'Pagina',
    'Slug',
    'Por que / Funcao',
    'Status',
    'Observacoes',
]

PAGES = [
    # P0 — Legal (obrigatorio)
    ['P0', 'Legal',        'Politica de Privacidade',   '/politica-de-privacidade',   'LGPD — obrigatoria. Formularios, WhatsApp, cookies.',                              'Nao Iniciado', ''],
    ['P0', 'Legal',        'Termos de Uso',             '/termos-de-uso',             'Protege juridicamente o site e os conteudos.',                                      'Nao Iniciado', ''],
    ['P0', 'Legal',        'Politica de Cookies',       '/cookies',                   'LGPD + banner de consentimento. Pode ser secao da Privacidade se preferir.',        'Nao Iniciado', ''],

    # P1 — Confianca + Conversao
    ['P1', 'Confianca',    'Sobre Nos / Quem Somos',    '/sobre',                     'E-E-A-T. +20 anos, sede em Goiania, equipe, fotos reais, historia.',               'Nao Iniciado', 'Ancora a autoridade de todos os 5 clusters'],
    ['P1', 'Confianca',    'Contato',                   '/contato',                   'Centraliza telefone, WhatsApp, endereco, mapa, formulario, horario.',               'Nao Iniciado', 'Hoje esta espalhado nos CTAs das LPs'],
    ['P1', 'Confianca',    'Trabalhe Conosco',          '/trabalhe-conosco',          'Vagas de tecnico, vendedor, operador. Empresa com operacao em 4 estados.',          'Nao Iniciado', ''],

    # P2 — Estrutural (navegacao do site)
    ['P2', 'Estrutural',   'Servicos',                  '/servicos',                  'Hub de todos os 6 servicos: locacao, plataformas, pecas, cursos, manutencao, venda Clark.', 'Concluido', 'Conecta usuario da Home para cada servico especifico'],
    ['P2', 'Estrutural',   'Home',                      '/',                          'Gateway para os 5 clusters + institucional.',                                       'Nao Iniciado', 'Pagina mais importante do site'],
    ['P2', 'Estrutural',   'Todos os Equipamentos',     '/equipamentos',              'Hub de navegacao: Plataforma, Empilhadeira, Transpaleteira.',                       'Nao Iniciado', 'Conecta Clusters 1, 2 e 3'],
    ['P2', 'Estrutural',   'Todas as Cidades',          '/localizacoes',              'Hub geografico: Goiania + futuras cidades.',                                        'Nao Iniciado', 'Conecta todas as LPs locais'],
    ['P2', 'Estrutural',   'Blog / Central de Conteudo','/blog',                      'Abriga Narrativos (TOFU/MOFU/BOFO), CAPEX/OPEX, Decisao Compartilhada.',           'Nao Iniciado', 'Hub para conteudo informacional dos 5 clusters'],
    ['P2', 'Estrutural',   'Busca',                     '/busca',                     'Com 161+ paginas, busca interna vira necessidade.',                                  'Nao Iniciado', ''],

    # P3 — Autoridade + Diferenciacao
    ['P3', 'Autoridade',   'Distribuidor Clark',        '/clark',                     'Pagina dedicada a parceria exclusiva Clark.',                                        'Nao Iniciado', 'Ancora Cluster 3 (Venda) e Cluster 4 (Pecas)'],
    ['P3', 'Autoridade',   'Nossos Clientes / Cases',   '/clientes',                  'Hub para cases BOFO de todos os clusters. Depoimentos expandidos + logos.',          'Nao Iniciado', ''],
    ['P3', 'Autoridade',   'Manutencao e Suporte',      '/manutencao-e-suporte',      'Diferencial core: suporte 24h, equipe mobile, processos.',                           'Nao Iniciado', 'Conecta com Cluster 4 (Pecas)'],
    ['P3', 'Autoridade',   'FAQ Geral',                 '/perguntas-frequentes',      'Duvidas transversais: processo de locacao, documentacao, prazos, pagamento.',         'Nao Iniciado', 'Cada LP mantem FAQ especifico'],

    # P4 — Futuro (escala)
    ['P4', 'Futuro',       'Parceiros / Revendas',      '/parceiros',                 'Se expandir rede de atendimento.',                                                   'Nao Iniciado', 'Criar quando houver rede de parceiros'],
    ['P4', 'Futuro',       'Imprensa',                  '/imprensa',                  'Se houver cobertura de midia.',                                                      'Nao Iniciado', ''],
    ['P4', 'Futuro',       'Portal do Cliente',         '/portal',                    'Login para clientes ativos (contratos, chamados).',                                   'Nao Iniciado', 'Requer desenvolvimento de backend'],
    ['P4', 'Futuro',       'Sitemap HTML',              '/mapa-do-site',              'Com 161+ URLs, ajuda navegacao e crawl.',                                             'Nao Iniciado', ''],
]


# ─── EXECUCAO ────────────────────────────────────────────────────────────────

def main():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive',
    ]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(SPREADSHEET_ID)

    # Tenta abrir a aba; se nao existir, cria
    try:
        ws = sh.worksheet(SHEET_TAB)
        print(f'Aba "{SHEET_TAB}" encontrada. Limpando dados existentes...')
        ws.clear()
    except gspread.exceptions.WorksheetNotFound:
        print(f'Aba "{SHEET_TAB}" nao encontrada. Criando...')
        ws = sh.add_worksheet(title=SHEET_TAB, rows=30, cols=len(HEADER))

    # Monta todas as linhas: header + dados
    all_rows = [HEADER] + PAGES

    # Escreve tudo de uma vez (1 API call)
    ws.update(range_name='A1', values=all_rows)

    # Formata header (bold + freeze)
    ws.format('A1:G1', {
        'textFormat': {'bold': True},
        'backgroundColor': {'red': 0.15, 'green': 0.15, 'blue': 0.15},
        'textFormat': {'bold': True, 'foregroundColorStyle': {'rgbColor': {'red': 1, 'green': 1, 'blue': 1}}},
    })
    ws.freeze(rows=1)

    # Ajusta largura das colunas
    requests = [
        {'updateDimensionProperties': {
            'range': {'sheetId': ws.id, 'dimension': 'COLUMNS', 'startIndex': i, 'endIndex': i + 1},
            'properties': {'pixelSize': w},
            'fields': 'pixelSize',
        }}
        for i, w in enumerate([90, 110, 250, 250, 450, 120, 350])
    ]
    sh.batch_update({'requests': requests})

    total = len(PAGES)
    print(f'\nPronto! {total} paginas institucionais adicionadas na aba "{SHEET_TAB}".')
    print(f'Link: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit')


if __name__ == '__main__':
    main()
