#!/usr/bin/env python3
"""
Gerador automático de sitemap.xml para Move Máquinas.
Escaneia os diretórios publicados e gera o sitemap com lastmod real.

Uso:
  python3 generate-sitemap.py           # gera sitemap.xml
  python3 generate-sitemap.py --dry-run # imprime sem salvar
"""

import os
import sys
from datetime import datetime
from pathlib import Path

BASE_URL = "https://movemaquinas.com.br"
PROJECT_DIR = Path(__file__).parent
OUTPUT_FILE = PROJECT_DIR / "sitemap.xml"

# Slugs de serviço por cidade (ordem fixa)
SERVICES = [
    "aluguel-de-empilhadeira-combustao",
    "aluguel-de-plataforma-elevatoria-articulada",
    "aluguel-de-plataforma-elevatoria-tesoura",
    "aluguel-de-transpaleteira",
    "curso-de-operador-de-empilhadeira",
]

# Páginas estáticas com configuração manual
STATIC_PAGES = [
    {"path": "/",                    "changefreq": "weekly",  "priority": "1.0"},
    {"path": "/venda-de-maquinas-clark", "changefreq": "monthly", "priority": "0.8"},
    {"path": "/cidades-atendidas",   "changefreq": "monthly", "priority": "0.7"},
    {"path": "/servicos",            "changefreq": "monthly", "priority": "0.6"},
    {"path": "/blog",                "changefreq": "weekly",  "priority": "0.8"},
    {"path": "/sobre",               "changefreq": "yearly",  "priority": "0.5"},
    {"path": "/contato",             "changefreq": "yearly",  "priority": "0.5"},
]

def get_lastmod(file_path: Path) -> str:
    """Retorna a data de modificação real do arquivo."""
    if file_path.exists():
        mtime = file_path.stat().st_mtime
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    return datetime.today().strftime("%Y-%m-%d")

def get_city_dirs() -> list[Path]:
    """Retorna diretórios de cidades com index.html publicado."""
    cities = []
    for d in sorted(PROJECT_DIR.iterdir()):
        if not d.is_dir():
            continue
        # Padrão: nome-cidade-UF (ex: goiania-go, brasilia-df)
        parts = d.name.rsplit("-", 1)
        if len(parts) == 2 and len(parts[1]) == 2 and parts[1].isalpha():
            index = d / "index.html"
            if index.exists():
                cities.append(d)
    return cities

def get_blog_posts() -> list[Path]:
    """Retorna subdiretórios do blog com index.html."""
    blog_dir = PROJECT_DIR / "blog"
    if not blog_dir.exists():
        return []
    posts = []
    for d in sorted(blog_dir.iterdir()):
        if d.is_dir() and (d / "index.html").exists():
            posts.append(d)
    return posts

def url_entry(loc: str, lastmod: str, changefreq: str, priority: str) -> str:
    return (
        f"  <url>\n"
        f"    <loc>{BASE_URL}{loc}</loc>\n"
        f"    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>{changefreq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        f"  </url>"
    )

def build_sitemap() -> str:
    entries = []

    # Páginas estáticas
    for page in STATIC_PAGES:
        # Tenta encontrar o arquivo HTML correspondente
        path = page["path"].strip("/") or "index"
        candidate = PROJECT_DIR / path / "index.html"
        if not candidate.exists():
            candidate = PROJECT_DIR / (path + ".html")
        lastmod = get_lastmod(candidate) if candidate.exists() else datetime.today().strftime("%Y-%m-%d")
        entries.append(url_entry(page["path"], lastmod, page["changefreq"], page["priority"]))

    # Blog posts
    for post in get_blog_posts():
        slug = f"/blog/{post.name}"
        lastmod = get_lastmod(post / "index.html")
        entries.append(url_entry(slug, lastmod, "monthly", "0.8"))

    # Cidades e seus serviços
    for city_dir in get_city_dirs():
        slug = f"/{city_dir.name}"
        lastmod = get_lastmod(city_dir / "index.html")
        # Priority: goiania-go e aparecida = 0.9, demais = 0.8
        priority = "0.9" if city_dir.name in ("goiania-go", "aparecida-de-goiania-go") else "0.8"
        entries.append(url_entry(slug, lastmod, "monthly", priority))

        for service in SERVICES:
            service_dir = city_dir / service
            service_index = service_dir / "index.html"
            svc_lastmod = get_lastmod(service_index)
            svc_priority = "0.9" if city_dir.name == "goiania-go" else "0.7"
            entries.append(url_entry(f"{slug}/{service}", svc_lastmod, "monthly", svc_priority))

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "\n".join(entries)
    xml += "\n</urlset>"
    return xml

if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    sitemap = build_sitemap()

    if dry_run:
        print(sitemap)
    else:
        OUTPUT_FILE.write_text(sitemap, encoding="utf-8")
        url_count = sitemap.count("<url>")
        print(f"sitemap.xml gerado: {url_count} URLs → {OUTPUT_FILE}")
