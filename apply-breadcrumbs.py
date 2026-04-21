#!/usr/bin/env python3
"""
Aplica o breadcrumb padrão (faixa abaixo do hero, fundo surface, links verdes)
em todas as páginas do site Move Máquinas.

Páginas excluídas: index.html (home), cidades-atendidas/index.html
Páginas já feitas (modelos aprovados): skip automático se breadcrumb já correto.
"""

import re
import os

BASE = "/Users/jrios/move-maquinas-seo"

# CSS padrão a injetar (substitui qualquer .breadcrumb existente)
BREADCRUMB_CSS = """.breadcrumb{background:var(--color-surface);border-bottom:1px solid var(--color-border);padding:10px 0}
.breadcrumb__list{display:flex;align-items:center;gap:6px;list-style:none;flex-wrap:wrap;font-size:.78rem;color:var(--color-muted)}
.breadcrumb__list li:not(:last-child)::after{content:"›";margin-left:6px;color:var(--color-border)}
.breadcrumb__list a{color:var(--color-primary);font-weight:600;text-decoration:none;transition:opacity .15s}
.breadcrumb__list a:hover{opacity:.75}
.breadcrumb__list li:last-child{color:var(--color-text-light)}"""

# Nomes legíveis por slug de cidade
CITY_LABELS = {
    "goiania-go": "Equipamentos em Goiânia",
    "anapolis-go": "Equipamentos em Anápolis",
    "aparecida-de-goiania-go": "Equipamentos em Aparecida de Goiânia",
    "brasilia-df": "Equipamentos em Brasília",
    "caldas-novas-go": "Equipamentos em Caldas Novas",
    "formosa-go": "Equipamentos em Formosa",
    "inhumas-go": "Equipamentos em Inhumas",
    "itumbiara-go": "Equipamentos em Itumbiara",
    "luziania-go": "Equipamentos em Luziânia",
    "senador-canedo-go": "Equipamentos em Senador Canedo",
    "trindade-go": "Equipamentos em Trindade",
    "uruacu-go": "Equipamentos em Uruaçu",
}

# Nomes legíveis por slug de serviço
SERVICE_LABELS = {
    "aluguel-de-empilhadeira-combustao": "Empilhadeira a Combustão",
    "aluguel-de-plataforma-elevatoria-articulada": "Plataforma Articulada",
    "aluguel-de-plataforma-elevatoria-tesoura": "Plataforma Tesoura",
    "aluguel-de-transpaleteira": "Transpaleteira",
    "curso-de-operador-de-empilhadeira": "Curso NR-11",
    "manutencao-empilhadeira": "Manutenção de Empilhadeira",
    "pecas-e-assistencia-empilhadeira": "Peças e Assistência",
}

# Páginas a pular
SKIP = {
    "index.html",
    "cidades-atendidas/index.html",
    # Já feitos como modelos aprovados — serão re-processados normalmente
    # (o script detecta se já tem breadcrumb correto e atualiza de qualquer forma)
}

# Páginas institucionais (sem cidade/serviço)
INSTITUTIONAL = {
    "sobre/index.html": ("Sobre a Movemáquinas", None),
    "contato/index.html": ("Contato", None),
    "servicos/index.html": ("Serviços", None),
    "venda-de-maquinas-clark/index.html": ("Equipamentos Clark em Goiânia", None),
    "politica-de-privacidade/index.html": ("Política de Privacidade", None),
    "termos-de-uso/index.html": ("Termos de Uso", None),
    "cookies/index.html": ("Política de Cookies", None),
    "trabalhe-conosco/index.html": ("Trabalhe Conosco", None),
    "author/marcio-lima/index.html": ("Marcio Lima", None),
    "blog/index.html": ("Blog", None),
}

# Blog posts
BLOG_POSTS = {
    "blog/andaime-vilao-cronograma-obra/index.html": "Andaime: o Vilão do Cronograma",
    "blog/andaime-vs-plataforma-custo-real/index.html": "Andaime vs Plataforma: Custo Real",
    "blog/plataforma-nr35-responsabilidade/index.html": "Plataforma NR-35: Responsabilidade",
    "blog/alugar-ou-comprar/index.html": "Alugar ou Comprar Empilhadeira",
}


def build_breadcrumb_html(items):
    """items = list of (label, href or None)"""
    lis = []
    for i, (label, href) in enumerate(items):
        if href:
            lis.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            lis.append(f'<li><span aria-current="page">{label}</span></li>')
    ol = "\n            ".join(lis)
    return f"""<nav class="breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <ol class="breadcrumb__list">
      {ol}
    </ol>
  </div>
</nav>"""


def get_breadcrumb_items(rel_path):
    parts = rel_path.split("/")

    # Blog posts
    if rel_path in BLOG_POSTS:
        return [
            ("Home", "/"),
            ("Blog", "/blog/"),
            (BLOG_POSTS[rel_path], None),
        ]

    # Institucional
    if rel_path in INSTITUTIONAL:
        label, _ = INSTITUTIONAL[rel_path]
        return [("Home", "/"), (label, None)]

    # Hub de cidade
    if len(parts) == 2 and parts[1] == "index.html":
        city = parts[0]
        label = CITY_LABELS.get(city, city.replace("-", " ").title())
        return [("Home", "/"), (label, None)]

    # LP de serviço
    if len(parts) == 3:
        city, service, _ = parts
        city_label = CITY_LABELS.get(city, city.replace("-", " ").title())
        svc_label = SERVICE_LABELS.get(service, service.replace("-", " ").title())
        city_href = f"/{city}/"
        page_label = f"{svc_label} em {city_label.replace('Equipamentos em ', '')}"
        return [
            ("Home", "/"),
            (city_label, city_href),
            (page_label, None),
        ]

    return [("Home", "/"), (rel_path, None)]


def remove_old_breadcrumb_css(html):
    # Remove qualquer bloco de CSS relacionado a .breadcrumb dentro de <style>
    # Regex: remove regras .breadcrumb*, .breadcrumb-*, .breadcrumb__*
    def clean_style(m):
        style_content = m.group(1)
        # Remove regras .breadcrumb (qualquer variante)
        cleaned = re.sub(
            r'\.breadcrumb[\w_-]*\s*\{[^}]*\}',
            '',
            style_content,
            flags=re.DOTALL
        )
        # Remove linhas em branco extras
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
        return f'<style>{cleaned}</style>'

    return re.sub(r'<style>(.*?)</style>', clean_style, html, flags=re.DOTALL)


def inject_breadcrumb_css(html, css):
    """Injeta o CSS antes do </style> do primeiro bloco de style."""
    return re.sub(r'(</style>)', f'\n{css}\n\\1', html, count=1)


def remove_old_breadcrumb_html(html):
    """Remove qualquer <nav class="breadcrumb"...> ou <header role="banner" class="breadcrumb"...> existente."""
    # Nav breadcrumb (qualquer posição)
    html = re.sub(
        r'<nav[^>]*class="[^"]*breadcrumb[^"]*"[^>]*>.*?</nav>',
        '',
        html,
        flags=re.DOTALL
    )
    # Header breadcrumb (antigo padrão com logo)
    html = re.sub(
        r'<header[^>]*class="[^"]*breadcrumb[^"]*"[^>]*>.*?</header>',
        '',
        html,
        flags=re.DOTALL
    )
    return html


def find_insert_point(html):
    """
    Encontra o ponto de inserção: após o fechamento do hero.
    Tenta em ordem:
    1. </section> seguido de <!-- TRUST BAR ou <!-- LAYOUT ou <!-- CONTEUDO
    2. </header> (hero como header) seguido de <!-- TRUST BAR
    3. Após </section> com class hero
    4. Após o primeiro </section>
    5. Após o primeiro </header>
    """
    # Padrão 1: </section> antes de comentário de trust/layout
    m = re.search(r'(</section>)\s*\n(\s*<!--\s*(TRUST|LAYOUT|CONTEUDO|CONTENT|MAIN|CORPO|BODY))', html, re.IGNORECASE)
    if m:
        return m.start(1) + len('</section>')

    # Padrão 2: </header> antes de comentário
    m = re.search(r'(</header>)\s*\n(\s*<!--\s*(TRUST|LAYOUT|CONTEUDO|CONTENT|MAIN|CORPO|BODY))', html, re.IGNORECASE)
    if m:
        return m.start(1) + len('</header>')

    # Padrão 3: primeiro </section>
    m = re.search(r'</section>', html)
    if m:
        return m.end()

    # Padrão 4: primeiro </header>
    m = re.search(r'</header>', html)
    if m:
        return m.end()

    return None


def process_file(rel_path):
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        return f"  SKIP (não existe): {rel_path}"

    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Limpar CSS antigo e injetar novo
    html = remove_old_breadcrumb_css(html)
    html = inject_breadcrumb_css(html, BREADCRUMB_CSS)

    # 2. Remover HTML antigo do breadcrumb
    html = remove_old_breadcrumb_html(html)

    # 3. Construir novo HTML do breadcrumb
    items = get_breadcrumb_items(rel_path)
    bc_html = build_breadcrumb_html(items)

    # 4. Encontrar ponto de inserção
    insert_pos = find_insert_point(html)
    if insert_pos is None:
        return f"  ERRO (ponto de inserção não encontrado): {rel_path}"

    html = html[:insert_pos] + "\n\n" + bc_html + "\n" + html[insert_pos:]

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return f"  OK: {rel_path}"


def main():
    # Coletar todos os index.html
    all_files = []
    for root, dirs, files in os.walk(BASE):
        # Excluir node_modules e diretórios ocultos
        dirs[:] = [d for d in dirs if d != 'node_modules' and not d.startswith('.')]
        for fname in files:
            if fname == 'index.html':
                full = os.path.join(root, fname)
                rel = os.path.relpath(full, BASE)
                all_files.append(rel)

    all_files.sort()

    results = {"ok": [], "skip": [], "error": []}

    for rel in all_files:
        # Pular home e cidades-atendidas
        if rel in SKIP:
            results["skip"].append(rel)
            continue

        # Pular páginas já processadas como modelos (vão ser reprocessadas normalmente)
        result = process_file(rel)
        if "OK:" in result:
            results["ok"].append(rel)
        elif "SKIP" in result:
            results["skip"].append(rel)
        else:
            results["error"].append(result)
        print(result)

    print(f"\n--- Resumo ---")
    print(f"OK:    {len(results['ok'])}")
    print(f"Skip:  {len(results['skip'])}")
    print(f"Erro:  {len(results['error'])}")
    if results["error"]:
        print("Erros:")
        for e in results["error"]:
            print(" ", e)


if __name__ == "__main__":
    main()
