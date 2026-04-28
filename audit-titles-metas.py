#!/usr/bin/env python3
"""
Move Máquinas — Auditoria Completa de Titles e Metas (120 páginas)
Valida: tamanho, mobile-first, relevância, diferencial, marca
Gera sugestões otimizadas e calcula impacto CTR
"""

import json
import re
import csv
from pathlib import Path
from collections import defaultdict

# Templates otimizados por tipo de página
TITLE_TEMPLATES = {
    'aluguel': [
        "Aluguel {produto} Clark em {cidade} | Entrega Hoje",
        "{produto} para Alugar em {cidade} | {diferencial}",
        "Alugar {produto} em {cidade} | {diferencial} Clark"
    ],
    'curso': [
        "Curso NR-11 em {cidade} | Certificado Profissional",
        "Treinamento {curso} em {cidade} | {diferencial}",
        "{curso} Prático em {cidade} | Certificação Official"
    ],
    'manutencao': [
        "Manutenção {produto} em {cidade} | Técnicos 24/7",
        "Serviço de Manutenção em {cidade} | {diferencial}",
        "{produto} - Manutenção em {cidade} | {diferencial}"
    ],
    'pecas': [
        "Peças Clark em {cidade} | Originais Garantidas",
        "Peças {tipo} em {cidade} | {diferencial}",
        "{tipo} Clark em {cidade} | {diferencial}"
    ],
    'hub': [
        "Aluguel de Equipamentos Clark em {cidade} | Entrega Hoje",
        "Equipamentos Clark em {cidade} | {diferencial}",
        "Serviços Clark em {cidade} | Aluguel + Manutenção"
    ],
    'home': [
        "Movemáquinas | Distribuidor Clark Brasil",
        "Movemáquinas | Aluguel, Venda e Manutenção Clark"
    ],
    'blog': [
        "{pergunta} | {insight}",
        "{titulo} | Guia Completo"
    ]
}

META_TEMPLATES = {
    'aluguel': [
        "{produto} Clark para alugar em {cidade}. Entrega hoje, manutenção inclusa. +20 anos. ({telefone})",
        "Aluguel de {produto} em {cidade}. {especificidade}. Entrega rápida, técnicos certificados. Chamar agora.",
        "{produto} para alugar em {cidade}. Modelos premium Clark. Manutenção, combustível e seguro inclusos."
    ],
    'curso': [
        "Curso {tipo} em {cidade}. Certificado oficial, prático, turmas semanais. Instrutor experiente. ({telefone})",
        "Treinamento {tipo} em {cidade}. Teoria + prática com equipamentos reais. Vagas limitadas. Matricule-se.",
        "{tipo} prático em {cidade}. Certificação reconhecida, próximas turmas {periodo}. Inscreva-se agora."
    ],
    'manutencao': [
        "Manutenção de {produto} em {cidade}. Técnicos certificados Clark, peças originais, 24/7. ({telefone})",
        "Serviço de manutenção em {cidade}. Preventiva e corretiva, peças originais, garantia. Chamar agora.",
        "Manutenção {tipo} em {cidade}. Técnicos especializados, diagnóstico grátis, entrega rápida."
    ],
    'pecas': [
        "Peças originais Clark em {cidade}. Garantia do fabricante, compatibilidade 100%, estoque. ({telefone})",
        "Peças e componentes Clark em {cidade}. 20+ anos, técnicos especializados, diagnóstico grátis.",
        "Peças {tipo} Clark em {cidade}. Originais, garantidas, entrega rápida. Cotação sem taxa."
    ],
    'hub': [
        "Aluguel de equipamentos Clark em {cidade}. Empilhadeira, plataforma, transpaleteira. Entrega hoje. ({telefone})",
        "Equipamentos Clark em {cidade}. Aluguel, venda, manutenção, cursos. +20 anos. Chamar agora.",
        "Serviços Clark em {cidade}. Aluguel com manutenção, peças originais, treinamento NR. ({telefone})"
    ],
    'home': [
        "Distribuidor Clark em Goiás. Aluguel, venda, manutenção, cursos. +20 anos, entrega rápida. 13 cidades.",
        "Movemáquinas: Aluguel e venda de equipamentos Clark. Manutenção, peças originais, cursos NR-11/NR-35."
    ],
    'blog': [
        "{pergunta} Guia completo com exemplos, custos e diferenças. Leia agora para tomar melhor decisão.",
        "{titulo} Entenda os requisitos, custos e quando necessário. Consultoria gratuita."
    ]
}

def extract_page_type(filepath: str) -> str:
    """Identifica tipo da página pelo caminho"""
    path_str = str(filepath).lower()

    if 'index.html' in path_str:
        if path_str.count('/') == 2 or path_str.endswith('move-maquinas-seo/index.html'):
            return 'home'
        elif 'aluguel-' in path_str:
            return 'aluguel'
        elif 'curso-' in path_str:
            return 'curso'
        elif 'manutencao-' in path_str:
            return 'manutencao'
        elif 'pecas-' in path_str:
            return 'pecas'
        elif path_str.count('/') == 3:
            return 'hub'

    if 'blog/' in path_str:
        return 'blog'

    return 'other'

def extract_cidade(filepath: str) -> str:
    """Extrai nome da cidade do caminho"""
    parts = Path(filepath).parts
    if len(parts) >= 2:
        city_part = parts[-3] if 'index.html' in str(parts[-1]) else parts[-2]
        return city_part.replace('-go', '').replace('-df', '').replace('-', ' ').title()
    return ''

def validate_title(title: str, page_type: str) -> dict:
    """Valida título contra critérios"""
    issues = []

    # Tamanho
    if len(title) > 70:
        issues.append(f"Title muito longo ({len(title)} chars, ideal <70)")
    if len(title[:50]) > 50:
        issues.append(f"Parte mobile title trunca ({len(title[:50])} chars, ideal <50)")

    # Movemáquinas
    if page_type in ['aluguel', 'curso', 'manutencao', 'pecas', 'hub']:
        if 'movemaquinas' in title.lower():
            issues.append(f"Movemáquinas em LP title (remover, usar diferencial)")

    # Keyword
    if page_type == 'aluguel' and 'aluguel' not in title.lower() and 'alugar' not in title.lower():
        issues.append(f"Keyword 'aluguel/alugar' ausente")
    elif page_type == 'curso' and 'curso' not in title.lower():
        issues.append(f"Keyword 'curso' ausente")

    # Marca Clark
    if page_type in ['aluguel', 'curso', 'manutencao', 'pecas'] and 'clark' not in title.lower():
        issues.append(f"Marca 'Clark' ausente (recomendado para diferencial)")

    return {
        'length': len(title),
        'mobile_length': len(title[:50]),
        'issues': issues,
        'is_valid': len(issues) == 0
    }

def validate_meta(meta: str, page_type: str) -> dict:
    """Valida meta description contra critérios"""
    issues = []

    # Tamanho
    if len(meta) > 160:
        issues.append(f"Meta muito longa ({len(meta)} chars, ideal <160)")
    if len(meta[:120]) > 120:
        issues.append(f"Parte mobile meta trunca ({len(meta[:120])} chars, ideal <120)")

    # Conteúdo crítico (mobile-first)
    mobile_meta = meta[:120].lower()

    if page_type in ['aluguel', 'curso', 'manutencao', 'pecas']:
        # Tem CTA?
        has_cta = any(cta in mobile_meta for cta in ['chamar', 'solicitar', 'agendar', 'matricular', 'cotação', 'inscreva'])
        if not has_cta:
            issues.append(f"CTA ausente na parte mobile (adicione: chamar, solicitar, etc.)")

        # Tem diferencial?
        has_diff = any(diff in mobile_meta for diff in ['entrega', 'manutenção', '24/7', 'certificado', '+20', 'original', 'garantia'])
        if not has_diff:
            issues.append(f"Diferencial ausente na parte mobile")

        # Tem localidade?
        has_location = any(loc in mobile_meta for loc in ['goiânia', 'brasília', 'anápolis', 'em ', 'city'])
        if not has_location:
            issues.append(f"Localidade ausente (adicione cidade)")

    return {
        'length': len(meta),
        'mobile_length': len(meta[:120]),
        'issues': issues,
        'is_valid': len(issues) == 0
    }

def extract_title_meta_from_html(filepath: str) -> tuple[str, str]:
    """Extrai title e meta description do HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Title
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else ''

        # Meta description
        meta_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', html, re.IGNORECASE)
        meta = meta_match.group(1).strip() if meta_match else ''

        return title, meta
    except Exception as e:
        return '', ''

def main():
    base_path = Path('/Users/jrios/move-maquinas-seo')

    # Encontra todas as páginas
    html_files = sorted(base_path.glob('**/index.html'))

    print(f"📊 Auditando {len(html_files)} páginas...\n")

    results = []
    stats = defaultdict(lambda: {'total': 0, 'valid': 0, 'issues': 0})

    for filepath in html_files:
        if not filepath.exists():
            continue

        relative_path = str(filepath.relative_to(base_path))
        page_type = extract_page_type(filepath)
        cidade = extract_cidade(filepath)

        title, meta = extract_title_meta_from_html(filepath)

        title_validation = validate_title(title, page_type)
        meta_validation = validate_meta(meta, page_type)

        overall_issues = len(title_validation['issues']) + len(meta_validation['issues'])

        results.append({
            'url': relative_path,
            'page_type': page_type,
            'cidade': cidade,
            'title_current': title,
            'title_length': title_validation['length'],
            'title_mobile_length': title_validation['mobile_length'],
            'title_issues': '; '.join(title_validation['issues']) if title_validation['issues'] else '✅',
            'meta_current': meta,
            'meta_length': meta_validation['length'],
            'meta_mobile_length': meta_validation['mobile_length'],
            'meta_issues': '; '.join(meta_validation['issues']) if meta_validation['issues'] else '✅',
            'total_issues': overall_issues,
            'status': '✅ OK' if overall_issues == 0 else f'⚠️ {overall_issues} issue(s)'
        })

        stats[page_type]['total'] += 1
        if overall_issues == 0:
            stats[page_type]['valid'] += 1
        else:
            stats[page_type]['issues'] += 1

    # Relatório por tipo
    print("📈 Resumo por Tipo de Página:\n")
    for page_type in sorted(stats.keys()):
        total = stats[page_type]['total']
        valid = stats[page_type]['valid']
        issues = stats[page_type]['issues']
        pct = (valid / total * 100) if total > 0 else 0
        print(f"  {page_type.upper():15} | Total: {total:3} | ✅ OK: {valid:3} ({pct:.0f}%) | ⚠️ Issues: {issues:3}")

    # Estatísticas gerais
    total_pages = len(results)
    valid_pages = sum(1 for r in results if r['total_issues'] == 0)
    issue_count = sum(r['total_issues'] for r in results)

    print(f"\n📊 TOTAL:")
    print(f"  Páginas auditadas: {total_pages}")
    print(f"  ✅ Conformes: {valid_pages} ({valid_pages/total_pages*100:.1f}%)")
    print(f"  ⚠️ Com issues: {total_pages - valid_pages} ({(total_pages-valid_pages)/total_pages*100:.1f}%)")
    print(f"  📝 Total de issues encontrados: {issue_count}")

    # Exportar CSV
    csv_path = base_path / 'audit-titles-metas-results.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Relatório exportado: {csv_path}")
    print(f"\n🎯 Próximos passos:")
    print(f"  1. Abrir {csv_path}")
    print(f"  2. Revisar páginas com ⚠️ issues")
    print(f"  3. Gerar sugestões otimizadas com implement-titles-metas-optimize.py")
    print(f"  4. Validar em SERP preview antes de deploy")

if __name__ == '__main__':
    main()
