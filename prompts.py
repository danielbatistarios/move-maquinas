"""
prompts.py — Prompts do Claude para geração de LPs
Move Maquinas SEO Automation
"""

PROMPT_01_FULL = """
Você é um especialista em SEO e copywriting B2B.
Escreva o conteúdo completo de uma Landing Page para a seguinte keyword principal:

[KEYWORD]
{keyword}

[CKB]
{ckb}

[MAPA_DE_LINKS]
{mapa_links}

INSTRUÇÕES:
1. Use a keyword principal como H1 (exata)
2. Escreva todos os textos em português BR, tom profissional e direto
3. Estrutura obrigatória:
   - H1: keyword exata
   - Parágrafo de abertura: contexto da cidade + problema que resolve (use o contexto_cidade abaixo)
   - H2: Equipamentos disponíveis em {city_label}
   - H2: Por que alugar com a Move Maquinas em {city_label}
   - H2: Setores que atendemos em {city_label}
   - H2: Também atendemos (ring de cidades — use os links A4 do MAPA_DE_LINKS)
   - H2: Outros equipamentos em {city_label} (cross-serviço — use os links A5 do MAPA_DE_LINKS)
   - FAQ com 5 perguntas relevantes para {city_label}
4. Insira os links do MAPA_DE_LINKS exatamente como especificado — anchor e posição
5. Breadcrumb: {breadcrumb}
6. Meta title: {keyword} | Move Maquinas
7. Meta description: máx 155 caracteres, inclua cidade e CTA

CONTEXTO DA CIDADE:
{contexto_cidade}

Retorne APENAS o conteúdo estruturado em markdown. Sem HTML ainda.
""".strip()

PROMPT_01_CONTEXT_ONLY = """
Escreva UM parágrafo de abertura (150–200 palavras) para uma Landing Page de:

Serviço: {service_label}
Cidade: {city_label} — {state_sigla}

CONTEXTO DA CIDADE:
{contexto_cidade}

O parágrafo deve:
- Mencionar {city_label} e seu contexto industrial/econômico
- Conectar esse contexto com a necessidade do serviço
- Ter tom profissional e direto (B2B)
- NÃO mencionar concorrentes
- NÃO usar emojis

Retorne APENAS o parágrafo, sem título nem marcação.
""".strip()

PROMPT_02_VISUAL = """
Você é um especialista em UI/UX para landing pages B2B.
Com base no conteúdo abaixo, defina a estratégia visual da LP.

CONTEÚDO:
{conteudo}

IDENTIDADE VISUAL MOVE MAQUINAS (obrigatório seguir):
- Verde primário: #1D9648
- Verde botões: #16A149
- Surface claro: #F3F7F5
- Footer dark: #16191C
- Tipografia: Inter (corpo) + Poppins (títulos)
- Ícones: SVG outlined — NUNCA emoji
- Estilo: industrial, sóbrio, confiança B2B

⚠️ VALIDAÇÃO OBRIGATÓRIA ANTES DE PROSSEGUIR:
Confirme que a paleta definida usa APENAS as cores acima.
Se usar navy, amber, roxo ou qualquer outra cor, RECOMECE.

Defina:
1. Estrutura de seções e ordem
2. Componentes por seção (hero, cards, grid, stats, CTA strip, FAQ, footer)
3. Hierarquia tipográfica
4. Uso de cor por seção
5. Comportamento mobile (breakpoints, reorganização)

Retorne a estratégia visual em formato estruturado.
""".strip()

PROMPT_03_HTML = """
Você é um desenvolvedor frontend especialista em landing pages de alta conversão.
Gere o HTML/CSS/JS completo e funcional em um único arquivo.

CONTEÚDO:
{conteudo}

ESTRATÉGIA VISUAL:
{estrategia_visual}

MAPA DE LINKS (use EXATAMENTE estes links e âncoras):
{mapa_links}

BREADCRUMB:
{breadcrumb}

REGRAS TÉCNICAS:
- Um único arquivo .html (sem dependências externas exceto Google Fonts)
- CSS inline no <style> dentro do <head>
- JS inline no <script> antes do </body>
- Mobile-first, responsivo
- Semântico: <header>, <main>, <section>, <footer>, <nav>
- Schema.org LocalBusiness + Service em JSON-LD
- Meta tags: title, description, og:title, og:description, og:url
- canonical: {canonical_url}

CHECKLIST DE IDENTIDADE VISUAL (valide antes de entregar):
□ Verde #1D9648 como cor primária de destaques e ícones
□ Verde #16A149 nos botões CTA
□ #F3F7F5 como background das seções claras
□ #16191C no footer
□ Tipografia Inter (corpo) + Poppins (títulos) via Google Fonts
□ Ícones SVG outlined — zero emoji no código
□ Nenhum uso de navy, amber, roxo ou cores fora da paleta
□ Hero com CTA principal acima do fold
□ Cards de equipamentos com especificações técnicas
□ Seção de stats/números
□ FAQ com accordion JS
□ Formulário de orçamento ou botão WhatsApp
□ Footer com endereço e links institucionais

Retorne APENAS o código HTML completo. Sem explicações.
""".strip()
