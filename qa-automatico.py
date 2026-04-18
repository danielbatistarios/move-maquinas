#!/usr/bin/env python3
"""
qa-automatico.py — QA automático para artigos de blog HTML.
Executa todas as verificações automatizáveis e corrige o que for possível.

Uso: python3 qa-automatico.py arquivo.html [--marca MoveMáquinas] [--entidade-central "NR-35"] [--max-marca 10]

Output:
  - Arquivo corrigido in-place (acentos, travessões, marca)
  - Relatório no terminal com warnings para itens que precisam de revisão manual
"""

import re
import sys
import argparse
from html.parser import HTMLParser


# ═══════════════════════════════════════════════════════
# MÓDULO 1 — CORREÇÃO DE ACENTOS
# ═══════════════════════════════════════════════════════

ACCENT_FIXES = {
    # ção / ções
    r'\bmanutencao\b': 'manutenção', r'\bManutencao\b': 'Manutenção',
    r'\binspecao\b': 'inspeção', r'\bInspecao\b': 'Inspeção',
    r'\bprotecao\b': 'proteção', r'\bProtecao\b': 'Proteção',
    r'\bpermissao\b': 'permissão', r'\bPermissao\b': 'Permissão',
    r'\boperacao\b': 'operação', r'\bOperacao\b': 'Operação',
    r'\blocacao\b': 'locação', r'\bLocacao\b': 'Locação',
    r'\bcomparacao\b': 'comparação',
    r'\bproducao\b': 'produção',
    r'\bcomposicao\b': 'composição',
    r'\bsituacao\b': 'situação',
    r'\bmobilizacao\b': 'mobilização',
    r'\breducao\b': 'redução',
    r'\bexecucao\b': 'execução',
    r'\bprevencao\b': 'prevenção',
    r'\bselecao\b': 'seleção',
    r'\bclassificacao\b': 'classificação',
    r'\bdocumentacao\b': 'documentação',
    r'\bautorizacao\b': 'autorização',
    r'\bcertificacao\b': 'certificação',
    r'\bsubstituicao\b': 'substituição',
    r'\bfiscalizacao\b': 'fiscalização',
    r'\bhabilitacao\b': 'habilitação',
    r'\bcapacitacao\b': 'capacitação',
    r'\binstalacao\b': 'instalação',
    r'\bfixacao\b': 'fixação',
    r'\bcorrosao\b': 'corrosão',
    r'\barticulacao\b': 'articulação',
    r'\bfuncao\b': 'função',
    r'\brelacao\b': 'relação',
    r'\bconstrucao\b': 'construção', r'\bConstrucao\b': 'Construção',
    r'\binformacao\b': 'informação',
    r'\belevacao\b': 'elevação',
    r'\bposicao\b': 'posição',
    r'\bsolucao\b': 'solução',
    r'\breposicao\b': 'reposição',
    r'\bobrigacao\b': 'obrigação',
    r'\bacao\b': 'ação', r'\bAcao\b': 'Ação',
    r'\bsecao\b': 'seção',
    r'\binstrucao\b': 'instrução',
    r'\bfundacao\b': 'fundação',
    r'\bpressao\b': 'pressão',
    r'\bconclusao\b': 'conclusão',
    r'\bcondicao\b': 'condição',
    r'\brestricao\b': 'restrição',
    r'\binfracao\b': 'infração',
    r'\bavaliacao\b': 'avaliação',
    r'\binclinacao\b': 'inclinação',
    r'\brecuperacao\b': 'recuperação',
    r'\badministracao\b': 'administração',
    r'\borganizacao\b': 'organização',
    r'\bapresentacao\b': 'apresentação',
    r'\bcontratacao\b': 'contratação',
    r'\bdepreciacao\b': 'depreciação',
    # ância / ência
    r'\bseguranca\b': 'segurança', r'\bSeguranca\b': 'Segurança',
    r'\bfrequencia\b': 'frequência',
    r'\bexperiencia\b': 'experiência',
    r'\bconsequencia\b': 'consequência',
    r'\bnegligencia\b': 'negligência',
    r'\bausencia\b': 'ausência',
    r'\bevidencia\b': 'evidência',
    r'\bexigencia\b': 'exigência',
    r'\bincidencia\b': 'incidência',
    r'\bemergencia\b': 'emergência',
    r'\breferencia\b': 'referência', r'\bReferencia\b': 'Referência',
    r'\bsequencia\b': 'sequência',
    r'\bpermanencia\b': 'permanência',
    r'\bdeficiencia\b': 'deficiência',
    r'\btendencia\b': 'tendência',
    # ário / ária / ório / ória
    r'\belevatoria\b': 'elevatória', r'\bElevatoria\b': 'Elevatória',
    r'\bperiodica\b': 'periódica',
    r'\borcamento\b': 'orçamento', r'\bOrcamento\b': 'Orçamento',
    r'\bcenario\b': 'cenário', r'\bCenario\b': 'Cenário',
    r'\bdiaria\b': 'diária', r'\bDiaria\b': 'Diária',
    r'\btecnico\b': 'técnico', r'\bTecnico\b': 'Técnico',
    r'\btecnica\b': 'técnica', r'\bTecnica\b': 'Técnica',
    r'\btecnicos\b': 'técnicos', r'\btecnicas\b': 'técnicas',
    r'\bpratico\b': 'prático', r'\bpratica\b': 'prática',
    r'\bobrigatorio\b': 'obrigatório', r'\bobrigatoria\b': 'obrigatória',
    r'\bnecessario\b': 'necessário', r'\bnecessaria\b': 'necessária',
    r'\bresponsavel\b': 'responsável',
    r'\bminimo\b': 'mínimo', r'\bminima\b': 'mínima',
    r'\bmaximo\b': 'máximo', r'\bmaxima\b': 'máxima',
    r'\brapido\b': 'rápido', r'\brapida\b': 'rápida',
    r'\bfisico\b': 'físico',
    r'\bjuridico\b': 'jurídico',
    r'\bunico\b': 'único', r'\bunica\b': 'única',
    r'\bfacil\b': 'fácil',
    r'\bdificil\b': 'difícil',
    r'\bpossivel\b': 'possível',
    r'\bviavel\b': 'viável',
    r'\bprevio\b': 'prévio', r'\bprevia\b': 'prévia',
    r'\bvalida\b': 'válida',
    r'\banalise\b': 'análise', r'\bAnalise\b': 'Análise',
    r'\beletrica\b': 'elétrica', r'\bEletrica\b': 'Elétrica',
    r'\beletrico\b': 'elétrico',
    r'\bhidraulico\b': 'hidráulico', r'\bhidraulica\b': 'hidráulica',
    r'\bacidentario\b': 'acidentário',
    r'\bprovisorio\b': 'provisório', r'\bprovisoria\b': 'provisória',
    # Acentos simples
    r'\bnao\b': 'não', r'\bNao\b': 'Não',
    r'\btambem\b': 'também',
    r'\balem\b': 'além', r'\bAlem\b': 'Além',
    r'\bate\b': 'até',
    r'\bja\b': 'já',
    r'\bso\b(?!\w)': 'só',
    r'\barea\b': 'área', r'\bArea\b': 'Área',
    r'\bacoes\b': 'ações',
    r'\bvoce\b': 'você', r'\bVoce\b': 'Você',
    r'\bestomago\b': 'estômago',
    r'\bcerebro\b': 'cérebro',
    r'\bcabeca\b': 'cabeça',
    r'\bjuridiques\b': 'juridiquês',
    r'\bmanha\b': 'manhã',
    r'\butil\b': 'útil',
    r'\binutil\b': 'inútil',
    r'\bhorario\b': 'horário',
    r'\bperiodo\b': 'período',
    r'\btermino\b': 'término',
    r'\binicio\b': 'início', r'\bInicio\b': 'Início',
    r'\bproximo\b': 'próximo', r'\bProximo\b': 'Próximo',
    r'\bproxima\b': 'próxima', r'\bProxima\b': 'Próxima',
    r'\bultimo\b': 'último', r'\bultima\b': 'última',
    r'\bObservatorio\b': 'Observatório',
    r'\bSaude\b': 'Saúde', r'\bsaude\b': 'saúde',
    r'\bcopia\b': 'cópia',
    r'\bligacao\b': 'ligação',
    r'\balguem\b': 'alguém',
    r'\bTres\b': 'Três', r'\btres\b': 'três',
    r'\bmedia\b': 'média',
    # Marca padrão
    r'\bMoveMaquinas\b': 'MoveMáquinas',
}


def fix_accents(content):
    """Corrige acentos usando word-boundary regex."""
    count = 0
    for pattern, replacement in ACCENT_FIXES.items():
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, replacement, content)
            count += matches
    return content, count


# ═══════════════════════════════════════════════════════
# MÓDULO 2 — TRAVESSÕES
# ═══════════════════════════════════════════════════════

def fix_dashes(content):
    """Remove em-dashes, substitui por ponto."""
    count = content.count('—')
    content = content.replace(' — ', '. ')
    content = content.replace('—', '. ')
    return content, count


# ═══════════════════════════════════════════════════════
# MÓDULO 3 — EXTRAÇÃO DE TEXTO (strip HTML tags)
# ═══════════════════════════════════════════════════════

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.current_tag = None
        self.skip_tags = {'style', 'script', 'svg', 'path'}
        self.in_skip = 0

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag in self.skip_tags:
            self.in_skip += 1

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_skip -= 1

    def handle_data(self, data):
        if self.in_skip <= 0:
            self.text_parts.append(data.strip())

    def get_text(self):
        return ' '.join(p for p in self.text_parts if p)


def extract_text(html):
    """Extrai texto visível do HTML."""
    parser = TextExtractor()
    parser.feed(html)
    return parser.get_text()


# ═══════════════════════════════════════════════════════
# MÓDULO 4 — ENTITY SALIENCE
# ═══════════════════════════════════════════════════════

def check_entity_salience(text, entity_central, marca, max_marca=10):
    """Verifica entity salience."""
    warnings = []

    central_count = len(re.findall(re.escape(entity_central), text, re.IGNORECASE))
    marca_count = len(re.findall(re.escape(marca), text, re.IGNORECASE))

    if marca_count > max_marca:
        warnings.append(f"⚠️  MARCA: {marca} aparece {marca_count}x (máx recomendado: {max_marca}). Reduzir.")
    elif marca_count < 4:
        warnings.append(f"⚠️  MARCA: {marca} aparece apenas {marca_count}x (mín recomendado: 6). Considerar adicionar.")

    if central_count < marca_count:
        warnings.append(f"⚠️  SALIENCE: Entidade central '{entity_central}' ({central_count}x) aparece MENOS que a marca ({marca_count}x). Desbalanceado.")

    return central_count, marca_count, warnings


# ═══════════════════════════════════════════════════════
# MÓDULO 5 — PARÁGRAFOS LONGOS
# ═══════════════════════════════════════════════════════

def check_paragraphs(content):
    """Identifica parágrafos com mais de 4 linhas (~280 caracteres)."""
    warnings = []
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)

    long_count = 0
    for i, p in enumerate(paragraphs):
        clean = re.sub(r'<[^>]+>', '', p).strip()
        # ~70 chars por linha, 4 linhas = 280 chars
        if len(clean) > 350:
            long_count += 1
            preview = clean[:80] + "..."
            warnings.append(f"⚠️  PARÁGRAFO LONGO ({len(clean)} chars, ~{len(clean)//70} linhas): \"{preview}\"")

    return long_count, warnings


# ═══════════════════════════════════════════════════════
# MÓDULO 6 — BUCKET BRIGADES
# ═══════════════════════════════════════════════════════

def check_bucket_brigades(content):
    """Conta bucket brigades e verifica frequência."""
    warnings = []

    bucket_classes = len(re.findall(r'class="bucket-bridge"', content))
    bucket_phrases = len(re.findall(
        r'Mas fica pior|E não para|Aqui é onde|boa notícia|número que muda|Na prática|Veja o que|A questão é|O ponto é',
        content, re.IGNORECASE
    ))

    total_buckets = max(bucket_classes, bucket_phrases)

    # Contar H2s para estimar frequência necessária
    h2_count = len(re.findall(r'<h2', content))

    if total_buckets < h2_count - 1:
        warnings.append(f"⚠️  BUCKET BRIGADES: encontradas {total_buckets}, recomendado pelo menos {h2_count - 1} (1 por transição entre H2s).")

    return total_buckets, warnings


# ═══════════════════════════════════════════════════════
# MÓDULO 7 — SLIPPERY SLIDES
# ═══════════════════════════════════════════════════════

def check_slippery_slides(content):
    """Verifica se há transição antes de cada H2."""
    warnings = []

    # Encontrar todos os H2s
    h2_positions = [m.start() for m in re.finditer(r'<h2', content)]

    missing = 0
    for pos in h2_positions[1:]:  # Pular o primeiro H2
        # Verificar 500 chars antes do H2
        before = content[max(0, pos-500):pos]

        has_slide = bool(re.search(
            r'slippery|Mas |Porém |Só que |A questão|próxim|Veja |O que vem|Agora ',
            before, re.IGNORECASE
        ))

        if not has_slide:
            # Pegar o texto do H2
            h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', content[pos:pos+200])
            h2_text = h2_match.group(1) if h2_match else "?"
            h2_clean = re.sub(r'<[^>]+>', '', h2_text)
            warnings.append(f"⚠️  SLIPPERY SLIDE ausente antes de: \"{h2_clean[:60]}\"")
            missing += 1

    return len(h2_positions) - 1 - missing, missing, warnings


# ═══════════════════════════════════════════════════════
# MÓDULO 8 — LINKS INTERNOS
# ═══════════════════════════════════════════════════════

def check_internal_links(content):
    """Conta links internos (href começando com /)."""
    links = re.findall(r'href="(/[^"]*)"', content)
    unique_links = set(links)
    warnings = []

    if len(unique_links) < 3:
        warnings.append(f"⚠️  LINKS INTERNOS: apenas {len(unique_links)} links únicos (mín recomendado: 3).")

    return len(links), len(unique_links), warnings


# ═══════════════════════════════════════════════════════
# MÓDULO 9 — THROAT CLEARING
# ═══════════════════════════════════════════════════════

def check_throat_clearing(text):
    """Detecta expressões de throat clearing."""
    warnings = []

    phrases = [
        'vale ressaltar', 'é importante destacar', 'nesse sentido',
        'dessa forma', 'sendo assim', 'é fundamental', 'é essencial',
        'cabe mencionar', 'convém lembrar', 'é preciso considerar',
        'diante disso', 'com base nisso', 'tendo em vista',
        'solução completa', 'compromisso com qualidade', 'excelência'
    ]

    for phrase in phrases:
        count = len(re.findall(phrase, text, re.IGNORECASE))
        if count > 0:
            warnings.append(f"⚠️  THROAT CLEARING: \"{phrase}\" encontrado {count}x. Cortar ou reescrever.")

    return warnings


# ═══════════════════════════════════════════════════════
# MÓDULO 10 — SUPERLATIVOS SEM PROVA
# ═══════════════════════════════════════════════════════

def check_superlatives(text):
    """Detecta superlativos sem prova."""
    warnings = []

    phrases = [
        'o melhor', 'a melhor', 'os melhores', 'as melhores',
        'líder', 'número um', 'incomparável', 'inigualável',
        'o maior', 'a maior', 'referência do mercado',
        'o mais completo', 'a mais completa'
    ]

    for phrase in phrases:
        count = len(re.findall(phrase, text, re.IGNORECASE))
        if count > 0:
            warnings.append(f"⚠️  SUPERLATIVO: \"{phrase}\" encontrado {count}x. Precisa de dado/fonte ou cortar.")

    return warnings


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description='QA automático para artigos de blog HTML')
    parser.add_argument('arquivo', help='Arquivo HTML para verificar')
    parser.add_argument('--marca', default='MoveMáquinas', help='Nome da marca (default: MoveMáquinas)')
    parser.add_argument('--entidade-central', default='', help='Entidade central do artigo')
    parser.add_argument('--max-marca', type=int, default=10, help='Máximo de menções da marca (default: 10)')
    parser.add_argument('--fix', action='store_true', default=True, help='Corrigir acentos e travessões (default: True)')
    parser.add_argument('--no-fix', action='store_true', help='Apenas reportar, não corrigir')

    args = parser.parse_args()

    with open(args.arquivo, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n{'='*60}")
    print(f"  QA AUTOMÁTICO — {args.arquivo}")
    print(f"{'='*60}\n")

    all_warnings = []
    fixes_applied = 0

    # ── CORREÇÕES AUTOMÁTICAS ──
    if not args.no_fix:
        print("── CORREÇÕES AUTOMÁTICAS ──\n")

        content, accent_count = fix_accents(content)
        print(f"  ✓ Acentos corrigidos: {accent_count}")
        fixes_applied += accent_count

        content, dash_count = fix_dashes(content)
        print(f"  ✓ Travessões removidos: {dash_count}")
        fixes_applied += dash_count

        # Salvar
        with open(args.arquivo, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n  Total de correções: {fixes_applied}")

    # ── VERIFICAÇÕES ──
    print(f"\n── VERIFICAÇÕES ──\n")

    text = extract_text(content)

    # Entity salience
    if args.entidade_central:
        central, marca, warnings = check_entity_salience(text, args.entidade_central, args.marca, args.max_marca)
        print(f"  Entidade central '{args.entidade_central}': {central}x")
        print(f"  Marca '{args.marca}': {marca}x")
        all_warnings.extend(warnings)
    else:
        marca_count = len(re.findall(re.escape(args.marca), text, re.IGNORECASE))
        print(f"  Marca '{args.marca}': {marca_count}x")
        if marca_count > args.max_marca:
            all_warnings.append(f"⚠️  MARCA: {args.marca} aparece {marca_count}x (máx: {args.max_marca})")

    # Parágrafos longos
    long_p, warnings = check_paragraphs(content)
    print(f"  Parágrafos longos (>350 chars): {long_p}")
    all_warnings.extend(warnings)

    # Bucket brigades
    buckets, warnings = check_bucket_brigades(content)
    print(f"  Bucket brigades: {buckets}")
    all_warnings.extend(warnings)

    # Slippery slides
    present, missing, warnings = check_slippery_slides(content)
    print(f"  Slippery slides: {present} presentes, {missing} ausentes")
    all_warnings.extend(warnings)

    # Links internos
    total_links, unique_links, warnings = check_internal_links(content)
    print(f"  Links internos: {total_links} total, {unique_links} únicos")
    all_warnings.extend(warnings)

    # Throat clearing
    warnings = check_throat_clearing(text)
    all_warnings.extend(warnings)

    # Superlativos
    warnings = check_superlatives(text)
    all_warnings.extend(warnings)

    # ── RELATÓRIO ──
    print(f"\n── RELATÓRIO ──\n")

    if all_warnings:
        print(f"  {len(all_warnings)} warnings encontrados:\n")
        for w in all_warnings:
            print(f"  {w}")
    else:
        print("  ✅ Nenhum warning. Artigo aprovado nas verificações automáticas.")

    print(f"\n{'='*60}")
    print(f"  Correções aplicadas: {fixes_applied}")
    print(f"  Warnings: {len(all_warnings)}")
    print(f"  Status: {'⚠️  REVISAR' if all_warnings else '✅ OK'}")
    print(f"{'='*60}\n")

    return 0 if not all_warnings else 1


if __name__ == '__main__':
    sys.exit(main())
