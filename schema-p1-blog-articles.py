#!/usr/bin/env python3
"""
Script 3: P0 + P1 fixes for 4 blog articles
1. Remove @context from child nodes (contamination within @graph)
2. Person: add sameAs LinkedIn, image, description, hasOccupation
"""
import json, re, os
from datetime import datetime

BASE = "/Users/jrios/move-maquinas-seo/blog"

BLOG_SLUGS = [
    "alugar-ou-comprar",
    "andaime-vilao-cronograma-obra",
    "andaime-vs-plataforma-custo-real",
    "plataforma-nr35-responsabilidade"
]

def fix_blog_article(slug):
    path = os.path.join(BASE, slug, "index.html")
    if not os.path.exists(path):
        return False

    with open(path, encoding="utf-8") as f:
        html = f.read()

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if not blocks:
        return False

    try:
        data = json.loads(blocks[0])
    except json.JSONDecodeError:
        return "invalid"

    # Check if it's a @graph structure
    if "@graph" not in data:
        return "no_graph"

    graph = data.get("@graph", [])

    for node in graph:
        t = node.get("@type", "")
        types = t if isinstance(t, list) else [t]

        # ── P0: Remove @context from child nodes ────────────────────────────
        if "@context" in node:
            del node["@context"]

        # ── Person: P1 enrichment ──────────────────────────────────────────
        if "Person" in types:
            # sameAs LinkedIn
            if "sameAs" not in node:
                node["sameAs"] = ["https://www.linkedin.com/in/m%C3%A1rciolima/"]
            # image
            if "image" not in node:
                node["image"] = {
                    "@type": "ImageObject",
                    "url": "https://movemaquinas.com.br/assets/authors/marcio-lima.webp",
                    "width": 400,
                    "height": 400
                }
            # description
            if "description" not in node:
                node["description"] = "Especialista em equipamentos Clark com mais de 15 anos de experiência em locação e manutenção de máquinas de movimentação."
            # hasOccupation
            if "hasOccupation" not in node:
                node["hasOccupation"] = {
                    "@type": "Occupation",
                    "name": "Especialista em Equipamentos de Movimentação"
                }

    new_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    new_block = f'<script type="application/ld+json">{new_json}</script>'
    old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
    html_out = html[:old_match.start()] + new_block + html[old_match.end():]

    with open(path, "w", encoding="utf-8") as f:
        f.write(html_out)

    return True


if __name__ == "__main__":
    print("=== Schema P1 — Blog Articles (4 páginas) ===")
    ok = fail = skip = 0
    for slug in BLOG_SLUGS:
        path = os.path.join(BASE, slug, "index.html")
        if not os.path.exists(path):
            skip += 1
            print(f"  SKIP: {slug}")
            continue
        result = fix_blog_article(slug)
        if result is True:
            ok += 1
            print(f"  OK: {slug}")
        elif result == "invalid":
            fail += 1
            print(f"  INVALID JSON: {slug}")
        elif result == "no_graph":
            skip += 1
            print(f"  SKIP (no @graph): {slug}")
        else:
            fail += 1
            print(f"  FAIL: {slug}")

    print(f"\nOK: {ok} | FAIL: {fail} | SKIP: {skip}")
