#!/usr/bin/env python3
"""
QA Phase 1: Críticas (P0) — Correções obrigatórias
1. Adicionar inLanguage="pt-BR" a todas as WebPages (32 service pages)
2. Adicionar dateModified a todas as WebPages (28 service pages)
3. Verificar taxID + foundingDate em Organization (institucionais)
"""
import json, re, os
from datetime import datetime

BASE = "/Users/jrios/move-maquinas-seo"
ORG_ID = "https://movemaquinas.com.br/#organization"

def add_inlanguage_datemodified():
    """Adiciona inLanguage e dateModified a todas as WebPages"""
    modified_count = 0

    # Procurar todos os index.html do site
    for root, dirs, files in os.walk(BASE):
        if "index.html" not in files:
            continue

        path = os.path.join(root, "index.html")

        # Pular alguns diretórios
        if any(skip in path for skip in ["assets", "node_modules", ".git"]):
            continue

        with open(path, encoding="utf-8") as f:
            html = f.read()

        # Encontrar JSON-LD
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
        if not blocks:
            continue

        try:
            data = json.loads(blocks[0])
        except json.JSONDecodeError:
            continue

        # Se for @graph, processar cada nó
        if "@graph" in data:
            graph = data["@graph"]
            modified = False

            for node in graph:
                t = node.get("@type", "")
                types = t if isinstance(t, list) else [t]

                # WebPage: adicionar inLanguage e dateModified
                if any(tp in types for tp in ["WebPage", "AboutPage", "ContactPage", "ProfilePage"]):
                    if "inLanguage" not in node:
                        node["inLanguage"] = "pt-BR"
                        modified = True
                    if "dateModified" not in node:
                        node["dateModified"] = datetime.now().isoformat()
                        modified = True

            if modified:
                new_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
                new_block = f'<script type="application/ld+json">{new_json}</script>'
                old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
                html_out = html[:old_match.start()] + new_block + html[old_match.end():]

                with open(path, "w", encoding="utf-8") as f:
                    f.write(html_out)

                modified_count += 1

    return modified_count


def verify_organization_fields():
    """Verifica se Organization tem taxID + foundingDate em páginas institucionais"""
    issues = []

    institutional_paths = [
        "sobre",
        "contato",
        "politica-de-privacidade",
        "termos-de-uso",
        "cookies",
        "trabalhe-conosco"
    ]

    for slug in institutional_paths:
        path = os.path.join(BASE, slug, "index.html")
        if not os.path.exists(path):
            continue

        with open(path, encoding="utf-8") as f:
            html = f.read()

        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
        if not blocks:
            continue

        try:
            data = json.loads(blocks[0])
        except json.JSONDecodeError:
            continue

        graph = data.get("@graph", [])
        org = next((n for n in graph if "Organization" in str(n.get("@type", ""))), None)

        if org:
            modified = False
            if "taxID" not in org:
                org["taxID"] = "32428258000180"
                modified = True
            if "foundingDate" not in org:
                org["foundingDate"] = "2019-01-07"
                modified = True

            if modified:
                new_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
                new_block = f'<script type="application/ld+json">{new_json}</script>'
                old_match = re.search(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
                html_out = html[:old_match.start()] + new_block + html[old_match.end():]

                with open(path, "w", encoding="utf-8") as f:
                    f.write(html_out)

                issues.append((slug, "Organization updated with taxID + foundingDate"))

    return issues


if __name__ == "__main__":
    print("=== QA Phase 1: Correções Críticas ===\n")

    print("[1/2] Adicionando inLanguage + dateModified a todas as WebPages...")
    modified = add_inlanguage_datemodified()
    print(f"  ✓ {modified} páginas atualizadas\n")

    print("[2/2] Verificando Organization taxID + foundingDate em institucionais...")
    org_fixes = verify_organization_fields()
    for slug, msg in org_fixes:
        print(f"  ✓ {slug}: {msg}")

    print(f"\n✅ QA Phase 1 Completa: {modified + len(org_fixes)} páginas corrigidas")
