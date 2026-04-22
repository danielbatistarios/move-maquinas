#!/usr/bin/env python3
"""
Fix remaining 2 schema issues:
1. Home — add sameAs to Course node
2. Servicos — add openingHoursSpecification to LocalBusiness
"""

import json
import re
from pathlib import Path

def fix_home_course():
    """Fix /index.html Course node — add sameAs Q6869278"""
    file_path = Path("/Users/jrios/move-maquinas-seo/index.html")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if not match:
        return False

    json_str = match.group(1)
    data = json.loads(json_str)
    graph = data["@graph"]

    # Find Course node
    for node in graph:
        if node.get("@type") == "Course":
            if "sameAs" not in node:
                node["sameAs"] = "https://www.wikidata.org/wiki/Q6869278"
                new_json = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
                new_content = content.replace(json_str, new_json)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print("✅ /index.html — Course.sameAs added")
                return True

    return False

def fix_servicos_opening_hours():
    """Fix /servicos/index.html LocalBusiness — add openingHoursSpecification"""
    file_path = Path("/Users/jrios/move-maquinas-seo/servicos/index.html")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if not match:
        return False

    json_str = match.group(1)
    data = json.loads(json_str)
    graph = data["@graph"]

    # Find LocalBusiness node
    for node in graph:
        if "LocalBusiness" in (node.get("@type") if isinstance(node.get("@type"), list) else [node.get("@type")]):
            if "openingHoursSpecification" not in node:
                node["openingHoursSpecification"] = {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                    "opens": "08:00",
                    "closes": "18:00"
                }
                new_json = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
                new_content = content.replace(json_str, new_json)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print("✅ /servicos/index.html — openingHoursSpecification added")
                return True

    return False

if __name__ == "__main__":
    print("\n🔧 Fixing remaining 2 schema issues...\n")

    fix_home_course()
    fix_servicos_opening_hours()

    print("\n✅ Done\n")
