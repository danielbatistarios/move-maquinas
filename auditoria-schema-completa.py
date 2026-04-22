#!/usr/bin/env python3
"""
Auditoria Completa de Schema JSON-LD — Move Máquinas
Verifica: Wikidata, Wikipedia, JSON-LD syntax, node types, semantic correctness
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

# Wikidata/Wikipedia mapping esperado (Rule R21)
EXPECTED_WIKIDATA = {
    "Equipment rental": {
        "qcode": "Q5384579",
        "wikipedia": "https://en.wikipedia.org/wiki/Equipment_rental",
        "label": "Equipment rental service"
    },
    "Maintenance, Repair and Operations": {
        "qcode": "Q116786099",
        "wikipedia": "https://en.wikipedia.org/wiki/Maintenance_repair_operations",
        "label": "MRO (Maintenance, Repair, Operations)"
    },
    "Vocational education": {
        "qcode": "Q6869278",
        "wikipedia": "https://en.wikipedia.org/wiki/Vocational_education",
        "label": "Vocational training/education"
    },
    "Spare part": {
        "qcode": "Q25394887",
        "wikipedia": "https://en.wikipedia.org/wiki/Spare_part",
        "label": "Equipment spare parts"
    }
}

# Clark brand validation
CLARK_BRAND = {
    "qcode": "Q964158",
    "wikipedia": "https://en.wikipedia.org/wiki/Clark_Materials_Handling",
    "label": "Clark Equipment / Clark brand"
}

class SchemaAuditor:
    def __init__(self):
        self.issues = defaultdict(list)
        self.passes = defaultdict(list)
        self.stats = {
            "total_files": 0,
            "valid_json": 0,
            "invalid_json": 0,
            "wikidata_errors": 0,
            "missing_nodes": 0,
            "semantic_errors": 0,
        }

    def audit_file(self, file_path):
        """Audita um arquivo HTML e retorna erros + passes"""
        file_path = Path(file_path)
        self.stats["total_files"] += 1

        relative_path = str(file_path.relative_to("/Users/jrios/move-maquinas-seo"))

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract JSON-LD
            match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
            if not match:
                self.issues[relative_path].append("❌ JSON-LD script tag não encontrada")
                return

            json_str = match.group(1)

            # Validar JSON syntax
            try:
                data = json.loads(json_str)
                self.stats["valid_json"] += 1
            except json.JSONDecodeError as e:
                self.stats["invalid_json"] += 1
                self.issues[relative_path].append(f"❌ JSON inválido: {str(e)}")
                return

            # Auditar @graph
            if "@graph" not in data:
                self.issues[relative_path].append("❌ @graph não encontrada")
                return

            graph = data["@graph"]

            # Auditar cada node
            for idx, node in enumerate(graph):
                self._audit_node(node, relative_path, idx)

        except Exception as e:
            self.issues[relative_path].append(f"❌ Erro ao processar: {str(e)}")

    def _audit_node(self, node, file_path, node_idx):
        """Audita um nó individual da @graph"""
        node_type = node.get("@type")

        # Converter @type para lista se for string
        if isinstance(node_type, str):
            types = [node_type]
        elif isinstance(node_type, list):
            types = node_type
        else:
            self.issues[file_path].append(f"  Node #{node_idx}: @type inválido: {node_type}")
            return

        # Auditar Service nodes (Wikidata semantic correctness)
        if "Service" in types or "Course" in types:
            self._audit_service_node(node, file_path, node_idx)

        # Auditar Product nodes (Brand linking)
        if "Product" in types:
            self._audit_product_node(node, file_path, node_idx)

        # Auditar Person nodes
        if "Person" in types:
            self._audit_person_node(node, file_path, node_idx)

        # Auditar HowTo nodes
        if "HowTo" in types:
            self._audit_howto_node(node, file_path, node_idx)

        # Auditar VideoObject nodes
        if "VideoObject" in types:
            self._audit_video_node(node, file_path, node_idx)

        # Auditar LocalBusiness
        if "LocalBusiness" in types:
            self._audit_localbusiness_node(node, file_path, node_idx)

    def _audit_service_node(self, node, file_path, node_idx):
        """Verifica Service/Course nodes contra Wikidata"""
        same_as = node.get("sameAs")

        if not same_as:
            self.issues[file_path].append(f"  Node #{node_idx} ({node.get('@type')}): ❌ sameAs ausente")
            self.stats["wikidata_errors"] += 1
            return

        # sameAs pode ser string ou list
        same_as_list = [same_as] if isinstance(same_as, str) else same_as

        # Verificar se aponta para Wikidata (não deve apontar para brand)
        wikidata_found = False
        for url in same_as_list:
            if "wikidata.org" in url:
                wikidata_found = True
                qcode = url.split("/")[-1]

                # Validar Q-code contra mapa esperado
                valid = False
                for expected_concept, expected_data in EXPECTED_WIKIDATA.items():
                    if qcode == expected_data["qcode"]:
                        valid = True
                        self.passes[file_path].append(f"  Node #{node_idx}: ✅ Service.sameAs {qcode} válido ({expected_concept})")
                        break

                if not valid:
                    self.issues[file_path].append(f"  Node #{node_idx}: ⚠️ Q-code {qcode} não reconhecido para Service")
                    self.stats["wikidata_errors"] += 1

        # Verificar se aponta para Clark (ERRO)
        for url in same_as_list:
            if "Q964158" in url or "clark" in url.lower():
                self.issues[file_path].append(f"  Node #{node_idx}: ❌ ERRO CRÍTICO: Service aponta para Clark (brand), não service type!")
                self.stats["semantic_errors"] += 1

    def _audit_product_node(self, node, file_path, node_idx):
        """Verifica Product nodes contra Brand Wikidata"""
        brand = node.get("brand")

        if not brand:
            self.issues[file_path].append(f"  Node #{node_idx} (Product): ⚠️ brand ausente")
            return

        same_as = brand.get("sameAs") if isinstance(brand, dict) else None

        if not same_as:
            self.issues[file_path].append(f"  Node #{node_idx} (Product): ⚠️ brand.sameAs ausente")
            return

        # Product deve apontar para Clark Q964158
        same_as_list = [same_as] if isinstance(same_as, str) else same_as

        valid_clark = False
        for url in same_as_list:
            if "Q964158" in url:
                valid_clark = True
                self.passes[file_path].append(f"  Node #{node_idx}: ✅ Product.brand.sameAs = Q964158 (Clark)")
                break

        if not valid_clark:
            self.issues[file_path].append(f"  Node #{node_idx} (Product): ❌ brand.sameAs não aponta para Clark (Q964158)")
            self.stats["semantic_errors"] += 1

    def _audit_person_node(self, node, file_path, node_idx):
        """Verifica Person nodes"""
        name = node.get("name")
        knows_about = node.get("knowsAbout")
        same_as = node.get("sameAs")

        if not name:
            self.issues[file_path].append(f"  Node #{node_idx} (Person): ❌ name ausente")
            return

        if not knows_about:
            self.issues[file_path].append(f"  Node #{node_idx} (Person): ⚠️ knowsAbout ausente")

        if not same_as:
            self.issues[file_path].append(f"  Node #{node_idx} (Person): ⚠️ sameAs (social links) ausente")

        if name and knows_about and same_as:
            self.passes[file_path].append(f"  Node #{node_idx}: ✅ Person node completo ({name})")

    def _audit_howto_node(self, node, file_path, node_idx):
        """Verifica HowTo nodes"""
        step_list = node.get("step", [])

        if len(step_list) < 5:
            self.issues[file_path].append(f"  Node #{node_idx} (HowTo): ⚠️ Apenas {len(step_list)} steps (esperado 7+)")
        else:
            self.passes[file_path].append(f"  Node #{node_idx}: ✅ HowTo com {len(step_list)} steps")

    def _audit_video_node(self, node, file_path, node_idx):
        """Verifica VideoObject nodes"""
        duration = node.get("duration")
        upload_date = node.get("uploadDate")
        thumbnail = node.get("thumbnailUrl")

        issues = []
        if not duration:
            issues.append("duration ausente")
        if not upload_date:
            issues.append("uploadDate ausente")
        if not thumbnail:
            issues.append("thumbnailUrl ausente")

        if issues:
            self.issues[file_path].append(f"  Node #{node_idx} (VideoObject): ⚠️ {', '.join(issues)}")
        else:
            self.passes[file_path].append(f"  Node #{node_idx}: ✅ VideoObject completo")

    def _audit_localbusiness_node(self, node, file_path, node_idx):
        """Verifica LocalBusiness nodes"""
        agg_rating = node.get("aggregateRating")
        opening_hours = node.get("openingHoursSpecification")

        if not agg_rating:
            self.issues[file_path].append(f"  Node #{node_idx} (LocalBusiness): ⚠️ aggregateRating ausente")
        if not opening_hours:
            self.issues[file_path].append(f"  Node #{node_idx} (LocalBusiness): ⚠️ openingHoursSpecification ausente")

    def print_report(self):
        """Imprime relatório de auditoria"""
        print("\n" + "=" * 80)
        print("AUDITORIA COMPLETA — JSON-LD Schema Move Máquinas")
        print("=" * 80)

        # Estatísticas gerais
        print(f"\n📊 ESTATÍSTICAS GERAIS:")
        print(f"  Total de arquivos processados: {self.stats['total_files']}")
        print(f"  JSON válido: {self.stats['valid_json']}")
        print(f"  JSON inválido: {self.stats['invalid_json']}")
        print(f"  Erros Wikidata: {self.stats['wikidata_errors']}")
        print(f"  Erros semânticos: {self.stats['semantic_errors']}")

        # Issues encontradas
        if self.issues:
            print(f"\n❌ ISSUES ENCONTRADAS ({len(self.issues)} arquivos com problemas):")
            for file_path in sorted(self.issues.keys()):
                print(f"\n  📄 {file_path}")
                for issue in self.issues[file_path]:
                    print(f"     {issue}")
        else:
            print(f"\n✅ Nenhuma issue encontrada!")

        # Passes (amostra)
        if self.passes:
            total_passes = sum(len(v) for v in self.passes.values())
            print(f"\n✅ VALIDAÇÕES PASSANDO (amostra de {min(20, total_passes)}):")
            count = 0
            for file_path in sorted(self.passes.keys()):
                for pass_msg in self.passes[file_path]:
                    if count < 20:
                        print(f"  {pass_msg}")
                        count += 1
                    else:
                        break

        # Summary
        print(f"\n{'=' * 80}")
        total_issues = sum(len(v) for v in self.issues.values())
        if total_issues == 0:
            print("✅ AUDITORIA COMPLETA — TODOS OS SCHEMAS VÁLIDOS")
        else:
            print(f"⚠️ ENCONTRADAS {total_issues} ISSUES — REVISAR ACIMA")
        print("=" * 80)

def main():
    auditor = SchemaAuditor()

    # Auditar todos os HTML files
    root = Path("/Users/jrios/move-maquinas-seo")
    html_files = sorted(root.rglob("index.html"))

    print(f"🔍 Auditando {len(html_files)} arquivos HTML...")

    for html_file in html_files:
        auditor.audit_file(html_file)

    auditor.print_report()

if __name__ == "__main__":
    main()
