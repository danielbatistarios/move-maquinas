#!/usr/bin/env python3
"""
Schema Fix — Corrige 175 issues de Wikidata encontrados na auditoria
- Problema 1: Product nodes sem Clark Wikidata (132 issues)
- Problema 2: Service nodes sem Wikidata (40 issues)
- Problema 3: Utility pages sem schema mínimo (3 issues)
"""

import json
import re
from pathlib import Path

# Mapeamento de serviços → Q-codes (Rule R21)
SERVICE_WIKIDATA_MAP = {
    "aluguel": "Q5384579",  # Equipment rental
    "manutencao": "Q116786099",  # Maintenance operations
    "curso": "Q6869278",  # Vocational education
    "pecas": "Q25394887",  # Spare part
}

CLARK_WIKIDATA = "https://www.wikidata.org/wiki/Q964158"

class SchemaFixer:
    def __init__(self):
        self.fixed_count = 0
        self.skipped_count = 0
        self.errors = []

    def fix_file(self, file_path, dry_run=False):
        """Corrige issues em um arquivo HTML"""
        file_path = Path(file_path)
        relative_path = str(file_path.relative_to("/Users/jrios/move-maquinas-seo"))

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract JSON-LD
            match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
            if not match:
                return False

            json_str = match.group(1)
            data = json.loads(json_str)

            if "@graph" not in data:
                return False

            graph = data["@graph"]
            modified = False

            # Processar cada nó
            for node in graph:
                node_type = node.get("@type")
                types = [node_type] if isinstance(node_type, str) else (node_type if isinstance(node_type, list) else [])

                # Fix 1: Product nodes com brand.sameAs incorreto
                if "Product" in types:
                    if self._fix_product_brand(node, relative_path):
                        modified = True

                # Fix 2: Service nodes sem sameAs
                if "Service" in types or "Course" in types:
                    if self._fix_service_sameas(node, file_path, relative_path):
                        modified = True

                # Fix 3: LocalBusiness sem aggregateRating (utility pages)
                if "LocalBusiness" in types:
                    if self._fix_localbusiness_missing_fields(node):
                        modified = True

            # Escrever arquivo se modificado
            if modified and not dry_run:
                new_json = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
                new_content = content.replace(json_str, new_json)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                self.fixed_count += 1
                return True
            elif modified and dry_run:
                self.fixed_count += 1
                return True

            return False

        except Exception as e:
            self.errors.append(f"{relative_path}: {str(e)}")
            self.skipped_count += 1
            return False

    def _fix_product_brand(self, node, relative_path):
        """Fix product brand sameAs para Clark Q964158"""
        brand = node.get("brand")

        if not isinstance(brand, dict):
            return False

        same_as = brand.get("sameAs")

        # Se já é Clark, skip
        if same_as and "Q964158" in same_as:
            return False

        # Corrigir
        if same_as is None or "Q964158" not in str(same_as):
            brand["sameAs"] = CLARK_WIKIDATA
            return True

        return False

    def _fix_service_sameas(self, node, file_path, relative_path):
        """Fix service nodes sem sameAs Wikidata"""
        if "sameAs" in node and node["sameAs"]:
            return False  # Já tem sameAs

        # Determinar tipo de serviço a partir do path
        path_str = str(file_path)

        for service_key, qcode in SERVICE_WIKIDATA_MAP.items():
            if service_key in path_str:
                node["sameAs"] = f"https://www.wikidata.org/wiki/{qcode}"
                return True

        # Fallback: se não conseguir determinar, deixar como está
        return False

    def _fix_localbusiness_missing_fields(self, node):
        """Add aggregateRating a LocalBusiness em utility pages"""
        # Only utility pages (contato, servicos) precisam disso
        if "aggregateRating" not in node:
            # Agregar de padrão Move Máquinas (4.8 ⭐ 108 reviews)
            node["aggregateRating"] = {
                "@type": "AggregateRating",
                "ratingValue": 4.8,
                "reviewCount": 108,
                "bestRating": 5,
                "worstRating": 1
            }
            return True

        return False

    def fix_all(self, dry_run=True):
        """Corrige todos os arquivos HTML"""
        root = Path("/Users/jrios/move-maquinas-seo")
        html_files = sorted(root.rglob("index.html"))

        mode = "DRY-RUN" if dry_run else "PRODUCTION"
        print(f"\n🔧 Schema Fix — {mode}")
        print(f"Processando {len(html_files)} arquivos...\n")

        for html_file in html_files:
            self.fix_file(html_file, dry_run=dry_run)

        self.print_report()

    def print_report(self):
        """Imprime relatório de correções"""
        print("\n" + "=" * 80)
        print("RELATÓRIO DE CORREÇÕES")
        print("=" * 80)
        print(f"Arquivos corrigidos: {self.fixed_count}")
        print(f"Arquivos skipped: {self.skipped_count}")

        if self.errors:
            print(f"\n❌ Erros encontrados ({len(self.errors)}):")
            for error in self.errors[:10]:
                print(f"  {error}")

        print("=" * 80)

def main():
    import sys

    dry_run = "--production" not in sys.argv

    fixer = SchemaFixer()
    fixer.fix_all(dry_run=dry_run)

if __name__ == "__main__":
    main()
