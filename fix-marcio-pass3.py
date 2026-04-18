#!/usr/bin/env python3
"""
Terceiro passe — limpa referências contextuais de 24h restantes.
Valores R$ em depoimentos e multas são contextuais e devem PERMANECER.
"""

import os
import re
import glob

BASE = "/Users/jrios/move-maquinas-seo"

def fix_24h(html):
    """Remove 24h de contextos de suporte/atendimento."""
    # Suporte técnico 24h → horário comercial
    html = re.sub(r'Suporte técnico 24h', 'Suporte técnico em horário comercial', html)
    html = re.sub(r'Suporte tecnico 24h', 'Suporte tecnico em horario comercial', html)
    html = re.sub(r'suporte técnico 24h', 'suporte técnico em horário comercial', html)
    html = re.sub(r'suporte tecnico 24h', 'suporte tecnico em horario comercial', html)

    # <strong>24h</strong> equipe/suporte
    html = re.sub(r'<strong>24h</strong>\s*equipe', '<strong>Horário comercial</strong> equipe', html)
    html = re.sub(r'<strong>24h</strong>\s*suporte', '<strong>Horário comercial</strong> suporte', html)

    # Suporte técnico 24h / 7 dias
    html = re.sub(r'Suporte t[ée]cnico 24h\s*/\s*7 dias', 'Suporte técnico em horário comercial', html)

    # plantão 24h
    html = re.sub(r'plant[aã]o 24h', 'suporte técnico', html)

    return html

def main():
    patterns = [
        os.path.join(BASE, "*-V2.html"),
        os.path.join(BASE, "*-BUILT.html"),
        os.path.join(BASE, "*-FINAL.html"),
    ]
    special = ["home.html", "home-index.html", "goiania-go-index.html",
               "goiania-articulada.html", "venda-clark.html", "servicos.html",
               "author-marcio-lima.html"]

    files = []
    for p in patterns:
        files.extend(glob.glob(p))
    for s in special:
        path = os.path.join(BASE, s)
        if os.path.exists(path):
            files.append(path)
    files.extend(glob.glob(os.path.join(BASE, "ref-goiania-*.html")))
    files = sorted(set(files))

    changed = 0
    for filepath in files:
        fn = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()

        html = fix_24h(original)

        if html != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            changed += 1
            print(f"  ✓ {fn}")

    print(f"\nAlterados no passe 3: {changed}")

if __name__ == "__main__":
    main()
