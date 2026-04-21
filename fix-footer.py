#!/usr/bin/env python3
"""
Corrige o bug do rodapé mm-ft preso dentro de blockquote.

Problema: <footer class="mm-ft"> foi injetado dentro de um <blockquote>
de depoimento. O rodapé antigo <footer> (sem classe) está correto no final.

Fix:
1. Extrai o <footer class="mm-ft">...</footer> de dentro do blockquote
2. Remove o rodapé antigo <footer> (sem classe mm-ft)
3. Insere o mm-ft no lugar certo: antes do float WA / antes de </body>
"""

import re
import os

BASE = "/Users/jrios/move-maquinas-seo"

# Páginas que NÃO devem ser tocadas (home e cidades-atendidas já estão corretas)
SKIP = {"index.html", "cidades-atendidas/index.html"}


def fix_file(rel_path):
    full_path = os.path.join(BASE, rel_path)
    with open(full_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Extrair o <footer class="mm-ft" ...>...</footer>
    m_mmft = re.search(r'<footer class="mm-ft"[^>]*>.*?</footer>', html, re.DOTALL)
    if not m_mmft:
        return f"  SKIP (sem mm-ft): {rel_path}"

    mmft_html = m_mmft.group(0)
    mmft_start = m_mmft.start()
    mmft_end = m_mmft.end()

    # Verificar se mm-ft está dentro de blockquote
    # Verificar se o último <blockquote antes do footer não foi fechado
    before_all = html[:mmft_start]
    last_bq_open = before_all.rfind('<blockquote')
    last_bq_close = before_all.rfind('</blockquote>')
    inside_blockquote = last_bq_open > last_bq_close
    if not inside_blockquote:
        return f"  SKIP (mm-ft já correto): {rel_path}"

    # 2. Remover o mm-ft de dentro do blockquote
    html = html[:mmft_start] + html[mmft_end:]

    # 3. Remover o rodapé antigo <footer> sem classe mm-ft (o legado)
    # Padrão: <footer> seguido de <div class="container"> (rodapé legado)
    html = re.sub(
        r'\n?<footer>\s*<div class="container">.*?</footer>',
        '',
        html,
        flags=re.DOTALL
    )

    # 4. Inserir mm-ft antes do float WA ou antes do </body>
    insert_marker = re.search(r'<!-- ={3,} FLOAT WA|<!-- FLOAT|<!-- ={3,} SCRIPTS|</body>', html)
    if insert_marker:
        pos = insert_marker.start()
        html = html[:pos] + "\n" + mmft_html + "\n\n" + html[pos:]
    else:
        # fallback: antes de </body>
        html = html.replace("</body>", mmft_html + "\n</body>", 1)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(html)

    return f"  OK: {rel_path}"


def main():
    results = {"ok": [], "skip": [], "error": []}

    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d != "node_modules" and not d.startswith(".")]
        for fname in files:
            if fname != "index.html":
                continue
            full = os.path.join(root, fname)
            rel = os.path.relpath(full, BASE)
            if rel in SKIP:
                results["skip"].append(rel)
                continue
            result = fix_file(rel)
            print(result)
            if "OK:" in result:
                results["ok"].append(rel)
            elif "SKIP" in result:
                results["skip"].append(rel)
            else:
                results["error"].append(result)

    print(f"\n--- Resumo ---")
    print(f"OK:    {len(results['ok'])}")
    print(f"Skip:  {len(results['skip'])}")
    print(f"Erro:  {len(results['error'])}")


if __name__ == "__main__":
    main()
