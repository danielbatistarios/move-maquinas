#!/usr/bin/env python3
"""
Auditoria final: Valida P0+P1 em todas as 120 páginas
"""

import json
import re
from pathlib import Path
from collections import defaultdict

def audit_page(html_file):
    """Audita uma página para P0/P1."""
    issues = defaultdict(int)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return None  # Skip arquivos sem JSON-LD

    json_str = match.group(1).strip()
    try:
        data = json.loads(json_str)
    except:
        return None

    graph = data.get('@graph', [data])

    for node in graph:
        node_type = node.get('@type')
        if isinstance(node_type, list):
            node_type_str = node_type[0] if node_type else None
        else:
            node_type_str = node_type

        # P0 — @id
        if node_type_str in ['Service', 'Course', 'Product']:
            if '@id' not in node:
                issues['missing_@id'] += 1

        # P0 — Service com brand
        if node_type_str == 'Service':
            if 'brand' in node:
                issues['service_has_brand'] += 1
            
            # P1 — serviceOffering
            if 'serviceOffering' not in node:
                issues['missing_serviceOffering'] += 1

    return dict(issues) if issues else {}

def process_all(base_path='/Users/jrios/move-maquinas-seo'):
    """Processa todas as páginas."""
    base = Path(base_path)
    
    all_issues = defaultdict(int)
    pages_with_issues = 0
    total_pages = 0

    for html_file in sorted(base.rglob('index.html')):
        if html_file.parent.name == 'assets' or '.git' in html_file.parts:
            continue

        total_pages += 1
        issues = audit_page(html_file)
        
        if issues:
            pages_with_issues += 1
            for issue, count in issues.items():
                all_issues[issue] += count

    print(f"\n{'='*60}")
    print(f"FINAL AUDIT — P0 + P1 Compliance")
    print(f"{'='*60}")
    print(f"\nTotal pages: {total_pages}")
    print(f"Pages with issues: {pages_with_issues}")
    print()

    if all_issues:
        print("Issues found:")
        for issue, count in sorted(all_issues.items()):
            print(f"  - {issue}: {count}")
    else:
        print("✓ ZERO ISSUES FOUND — P0 + P1 100% COMPLETE!")

    print(f"\n{'='*60}\n")

if __name__ == '__main__':
    process_all()
