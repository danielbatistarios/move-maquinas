#!/usr/bin/env python3
import json
import re
from pathlib import Path

def audit_page(html_file, rel_path):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return False

    json_str = match.group(1).strip()
    try:
        data = json.loads(json_str)
    except:
        return False

    graph = data.get('@graph', [data])

    for node in graph:
        node_type = node.get('@type')
        if node_type == 'Service':
            if 'serviceOffering' not in node:
                print(f"- {rel_path}")
                return True

    return False

base = Path('/Users/jrios/move-maquinas-seo')
for html_file in sorted(base.rglob('index.html')):
    if html_file.parent.name == 'assets' or '.git' in html_file.parts:
        continue
    rel_path = str(html_file.relative_to(base))
    audit_page(html_file, rel_path)
