#!/usr/bin/env python3
"""
Segundo passe — corrige residuais não capturados no primeiro script.
"""

import os
import re
import glob

BASE = "/Users/jrios/move-maquinas-seo"
R2 = "https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/assets/clark"

# Imagem Pexels restante nas tesouras (ID 2219024)
PEXELS_EXTRA = "https://images.pexels.com/photos/2219024/pexels-photo-2219024.jpeg?auto=compress&cs=tinysrgb&w=600"

# Mapeamento de substituição por cidade para a 5ª imagem tesoura
TESOURA_5TH = {
    "anapolis": f"{R2}/transpaleteira/wpio15/wpio15_einsatz_laden_img_4262.jpg",
    "brasilia": f"{R2}/transpaleteira/swx16/clark_swx16-clipped2.jpg",
    "caldas-novas": f"{R2}/empilhadeira-combustao/l25-30-35/l20-launch-header.jpg",
    "formosa": f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_2.jpg",
    "inhumas": f"{R2}/transpaleteira/wpio20/wpio20-10.jpg",
    "itumbiara": f"{R2}/empilhadeira-combustao/gts-25-30-33/gts25_100years.jpg",
    "luziania": f"{R2}/transpaleteira/pwio20/clark_pwio20_03-.jpg",
    "senador-canedo": f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c70_clipped-for-web.jpg",
    "trindade": f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_3.jpg",
    "uruacu": f"{R2}/transpaleteira/swx16/clark_swx16_application4.jpg",
    "valparaiso-de-goias": f"{R2}/empilhadeira-combustao/gts-25-30-33/clark_gts20-33_clipped_2-for-web.jpg",
}

def get_city(fn):
    base = os.path.basename(fn)
    for c in sorted(TESOURA_5TH.keys(), key=len, reverse=True):
        if base.startswith(c):
            return c
    return None

def fix_residuals(html, filename):
    """Corrige tudo que o primeiro passe não pegou."""

    # --- Pexels restante (foto 2219024 nas tesouras) ---
    city = get_city(filename)
    if city and PEXELS_EXTRA in html:
        replacement = TESOURA_5TH.get(city, f"{R2}/empilhadeira-combustao/c60-70-75-80/c80_01.jpg")
        html = html.replace(PEXELS_EXTRA, replacement)

    # --- Outras Pexels que possam ter ficado (IDs diferentes) ---
    # Pegar todas e substituir por imagens R2
    remaining_pexels = re.findall(r'https://images\.pexels\.com/photos/\d+/pexels-photo-\d+\.jpeg\?[^"\']*', html)
    fallbacks = [
        f"{R2}/empilhadeira-combustao/c60-70-75-80/clark_c60-80_application-for-web_01.jpg",
        f"{R2}/empilhadeira-combustao/gts-25-30-33/gts20-33-application-1039443432.jpg",
        f"{R2}/empilhadeira-eletrica/lep-20-35/site_lep_factory_1.jpg",
        f"{R2}/transpaleteira/swx16/clark_swx16_application1.jpg",
    ]
    for i, purl in enumerate(set(remaining_pexels)):
        html = html.replace(purl, fallbacks[i % len(fallbacks)])

    # --- 24h / 24/7 em variações não capturadas ---
    html = re.sub(r'<strong>Suporte 24/7</strong>', '<strong>Suporte Técnico</strong>', html)
    html = re.sub(r'<strong>24h</strong>\s*suporte', '<strong>Horário comercial</strong> suporte', html)
    html = re.sub(r'Atendimento técnico 24h', 'Atendimento técnico em horário comercial', html)
    html = re.sub(r'Atendimento tecnico 24h', 'Atendimento tecnico em horario comercial', html)
    html = re.sub(r'assistência 24 horas', 'assistência em horário comercial', html)
    html = re.sub(r'assistencia 24 horas', 'assistencia em horario comercial', html)
    html = html.replace("resposta 24h", "resposta em horário comercial")
    html = html.replace("Resposta 24h", "Resposta em horário comercial")

    # --- Preços em texto corrido (FAQ, descrições) ---
    # R$2.800 em prosa → "valor sob consulta"
    html = re.sub(r'entre R\$[\d.]+ e R\$[\d.]+', 'sob consulta', html)
    html = re.sub(r'de R\$[\d.]+ a R\$[\d.]+', 'sob consulta', html)
    html = re.sub(r'Desde R\$[\d.]+/m[eê]s', 'Sob consulta', html)
    html = re.sub(r'desde R\$[\d.]+/m[eê]s', 'sob consulta', html)
    html = re.sub(r'R\$[\d.]+\s*/m[eê]s', 'valor sob consulta', html)
    html = re.sub(r'R\$[\d.]+ mensais', 'valor sob consulta', html)
    # Schema FAQ com preços inline
    html = re.sub(r'investimento mensal fica entre R\$[\d.]+ e R\$[\d.]+', 'investimento mensal é sob consulta', html)
    html = re.sub(r'investimento mensal varia entre R\$[\d.]+ e R\$[\d.]+', 'investimento mensal é sob consulta', html)
    html = re.sub(r'O valor varia de R\$[\d.]+ a R\$[\d.]+', 'O valor é sob consulta', html)
    # Price cards que sobraram
    html = re.sub(r'R\$\s*2\.?800', 'Consultar', html)
    html = re.sub(r'R\$\s*3\.?400', 'Consultar', html)
    html = re.sub(r'R\$\s*4\.?[05]00', 'Sob consulta', html)

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

        html = fix_residuals(original, fn)

        if html != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            changed += 1
            print(f"  ✓ {fn}")

    print(f"\nAlterados no passe 2: {changed}")


if __name__ == "__main__":
    main()
