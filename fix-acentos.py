#!/usr/bin/env python3
"""
fix-acentos.py — Correção automática de acentos em HTML de blog.
Uso: python3 fix-acentos.py arquivo.html
O arquivo é corrigido in-place.
"""

import re
import sys

FIXES = {
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
    # ário / ária / ório / ória
    r'\belevatoria\b': 'elevatória', r'\bElevatoria\b': 'Elevatória',
    r'\bperiodica\b': 'periódica',
    r'\borcamento\b': 'orçamento', r'\bOrcamento\b': 'Orçamento',
    r'\bcenario\b': 'cenário', r'\bCenario\b': 'Cenário',
    r'\bdiaria\b': 'diária', r'\bDiaria\b': 'Diária',
    r'\btecnico\b': 'técnico', r'\bTecnico\b': 'Técnico',
    r'\btecnica\b': 'técnica', r'\bTecnica\b': 'Técnica',
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
    # Marca
    r'\bMoveMaquinas\b': 'MoveMáquinas',
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    count = 0
    for pattern, replacement in FIXES.items():
        matches = len(re.findall(pattern, content))
        if matches > 0:
            content = re.sub(pattern, replacement, content)
            count += matches

    # Remove em-dashes
    dashes = content.count('—')
    content = content.replace(' — ', '. ')
    content = content.replace('—', '. ')
    count += dashes

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ {filepath}: {count} correções aplicadas ({dashes} travessões removidos)")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 fix-acentos.py arquivo.html")
        sys.exit(1)
    for filepath in sys.argv[1:]:
        fix_file(filepath)
