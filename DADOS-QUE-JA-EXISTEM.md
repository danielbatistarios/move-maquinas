# Dados que JÁ EXISTEM no Schema (Não precisa coletar)

## Organização (Movemáquinas)

✅ **COMPLETO:**
- legalName: "Movemaquinas Comercio de Pecas LTDA"
- taxID: "32428258000180"
- foundingDate: "2019-01-07"
- address: Av. Eurico Viana, 4913 - Qd 5 B Lt 04, Goiânia, GO 74593-590
- geo: -16.7234, -49.2654
- logo: https://movemaquinas.com.br/assets/logo-move-maquinas.png
- description: "Distribuidor autorizado Clark. Locação e venda de..."
- areaServed: 13 cidades com geo + Wikidata sameAs
- openingHoursSpecification: Seg-Sex 08:00-18:00
- hasMap: https://maps.app.goo.gl/...
- priceRange: $$
- paymentAccepted: Cartão, Boleto, PIX, FCO
- currenciesAccepted: BRL
- dateModified: 2026-03-25
- sameAs: Google Maps, Instagram, LinkedIn, YouTube, Facebook, Grupo Legítima
- knowsAbout: 5 tópicos (Empilhadeira, Plataforma, Transpaleteira, Logística, Manutenção)
- hasOfferCatalog: 7 serviços com descrição completa
- numberOfEmployees: 30-80
- qualifications: "Distribuidor Autorizado Clark"
- availableLanguage: pt-BR
- contactPoint: 2 telefones (vendas + suporte)
- VAT/ISO codes: sim
- alternateName: 4 variações de nome
- relatedOrganization: Clube Envios
- award: 3 prêmios/certificações (Clark, NR-35, NR-11)
- Website node: @id, url, name, publisher, inLanguage

❌ **FALTA:**
- Missão/visão completa (apenas "description" genérica)
- Valores da empresa
- Fundador(es) - nome completo
- CEO/Presidente atual
- Marcos históricos (timeline 2019 → 2026)
- Publicações/Media (artigos em portais)
- Trustpilot/reviews score
- Número de clientes atendidos
- Horas/projetos completados
- Especificações de produto por tipo (capacidades, altura, dimensões)
- Documentação necessária para alugar
- Cobertura de seguro (sim/não, tipo)
- Tempos de resposta manutenção (em horas)
- Peças em estoque (lista de peças comuns)
- Tempo de entrega peças
- Garantia peças (original vs compatível)
- Duração curso NR-11 (em horas)
- Metodologia curso (presencial/híbrido/online)
- Taxa de aprovação histórica
- Instrutores credenciados (nomes, certificações)
- Responsável por atendimento em cada cidade
- Raio de atendimento (em km)
- Zonas de entrega express (24h vs 72h)
- Horários diferenciados (sábado, feriado)
- **Imagens**: fotos de equipamentos por modelo, equipe, operações, armazém
- **Vídeos**: YouTube links reais
- FAQ estruturada por tipo de serviço
- Depoimentos de clientes (com nomes, empresas)
- Case studies (projetos específicos)

---

## Pessoa (Márcio Lima)

✅ **COMPLETO:**
- name: "Márcio Rocha" (⚠️ nota: no schema está "Márcio Rocha", mas referencias anterior era "Márcio Lima")
- jobTitle: "Diretor Comercial & Especialista em Equipamentos Industriais"
- worksFor: Organization (Move Máquinas)
- url: https://movemaquinas.com.br/sobre/
- knowsAbout: 3 DefinedTerms (Empilhadeira, Plataforma, NR-35)
- description: "Diretor Comercial...20 anos de experiência..."
- familyName: "Rocha"
- givenName: "Márcio"
- image: https://movemaquinas.com.br/assets/marcio-diretor-move-maquinas.jpg
- sameAs: https://www.linkedin.com/in/m%C3%A1rciolima/
- hasOccupation: "Diretor Comercial de Equipamentos Industriais"
- award: "Especialista Certificado em Operação de Empilhadeiras Clark"

❌ **FALTA:**
- Nome completo verificado (Lima? Rocha? Ambos?)
- Formação acadêmica (escola, faculdade, ano)
- Certificações NR (NR-11, NR-35, NR-12) com datas
- Treinamentos avançados (fabricante, modelos)
- Anos de experiência TOTAL (está "20+ anos" no texto, precisa confirmar número exato)
- Histórico de posições anteriores (antes de Move)
- Empresas anteriores onde trabalhou
- Especialidades técnicas (detalhadas por tipo de equipamento)
- Tipos de clientes (indústria, construção, logística)
- Membro de associações (ABIQUIM, ABNT, etc)
- YouTube Channel pessoal (se houver)
- Instagram pessoal (se houver)
- Publicações/artigos (LinkedIn posts, etc)
- Foto de alta qualidade (600x600px HD WebP) — imagem atual pode ser 300x300
- Bio resumida 50 palavras (há descrição, mas pode ser otimizada)
- Emissão de certificados/Instrutor NR-11 autorizado?

---

## Serviços e Produtos

✅ **COMPLETO:**
- 7 serviços no hasOfferCatalog com descrição
- Service type por equipamento
- Wikidata sameAs para cada serviço
- businessFunction (LeaseOut para aluguel, Sell para venda)
- makesOffer com Product: Empilhadeira Clark
- Brand: Clark
- priceRange: R$ 500/dia (base)
- pricingDetails: 5-20 dias (0%), 21-60 dias (-10%), 60+ dias (-15%)
- availability: InStock
- Course node: name, description, educationalLevel, teaches, inLanguage
- hasOfferInstance: 2 CourseInstances (Goiânia, Anápolis)
- courseMode: Presential
- courseWorkload: PT30H

❌ **FALTA:**
- **Tabela de preços COMPLETA** (aluguel por equipamento × período)
  - Empilhadeira combustão (R$ X por dia)
  - Plataforma articulada (R$ X por dia)
  - Plataforma tesoura (R$ X por dia)
  - Transpaleteira (R$ X por dia)
  - Desconto semanal, mensal
- **Modelos específicos** (FC-25, FC-30, FC-35 com capacidade, altura, combustível)
- **Imagens** de cada modelo (WebP, 600x600px)
- **Preço do Curso NR-11** (R$) em offers.price
- **Duração curso** verificada em horas (PT30H ou PT40H?)
- **Datas próximas turmas** 
- **Taxa de aprovação** histórica (%)
- **Instrutor credenciado** (Márcio Lima é instrutor? tem certificação ativa?)
- **Documentação** necessária para alugar (RG, CNPJ, etc)
- **Cobertura de seguro** (incluída? qual valor?)
- **Tempo de resposta** manutenção (24h, 48h, etc)
- **Peças comuns em estoque** (lista)
- **Tempo entrega peças** (24h, 48h, dias úteis)
- **Garantia peças** (original Clark: 12 meses? 24 meses?)
- **Compatibilidade peças** (Clark original vs compatível)
- **Acessórios** (garfos, correntes, balanças, etc)
- **Imagens de operações** (equipe em ação, clientes)

---

## Conteúdo & SEO

✅ **COMPLETO:**
- FAQPage com 6 perguntas + respostas
- Blog com 4 artigos publicados
- ItemList: 13 cidades com names, URLs, geo, Wikidata sameAs
- BreadcrumbList (home)
- Topical Hubs: Empilhadeiras + Plataformas (CreativeWork com hasPart)
- PrivacyStatement: LGPD compliant, dataCollected, dataRetention

❌ **FALTA:**
- **FAQ expandida por tipo** (aluguel, manutenção, peças, curso = 4 seções × 5 perguntas)
- **FAQ com respostas mais técnicas** (modelos, especificações)
- **Conteúdo de blog** (18 artigos pendentes conforme memory)
- **Depoimentos estruturados** (Customer Review com rating, date, author, text)
- **Case studies** (estruturados como CreativeWork + hasPart)
- **Especificações técnicas** em Product (peso, dimensões, consumo combustível, etc)
- **Compatibilidade matriz** (qual equipamento + serviço para cada tipo de cliente)

---

## Imagens & Mídia

✅ **EXISTENTE:**
- Logo com dimensions: 300×80
- Foto do Márcio: 300×300
- Imagens em megamenu (empilhadeira combustão, c60-80, transpaleteira)
- OG image: hero-bg.jpg

❌ **FALTA COMPLETAMENTE:**
- **Fotos de cada modelo Clark** (FC-25, FC-30, GTS25, C60, C80, L25, etc)
  - Quantidade: ~14 modelos
  - Formato: WebP, 600×600px ou 1200×800px
  - Ângulos: frente, lateral, em operação
- **Fotos de operações**
  - Equipe (Márcio em ação, técnicos)
  - Clientes em uso (autorização necessária)
  - Manutenção em andamento
  - Treinamento NR-11
  - Armazém/garagem (mostrando frota)
- **Vídeos YouTube** (links reais, não apenas canal)
  - Demonstrações de operação
  - Tutoriais NR-11/NR-35
  - Depoimentos de clientes
  - Tour do armazém
  - Entrevista com Márcio
- **Foto HD do Márcio** (600×600px WebP com caption)
  - Foto atual: 300×300, precisa upgrade
- **Imagens de FAQ** (para visualizar respostas)

---

## Resumo Executivo

### A Pedir para os Donos (CRÍTICO)

| Campo | Tipo | Para | Impacto |
|---|---|---|---|
| Preço Curso NR-11 | Número (R$) | Script 2B | Sem isso, course.offers fica vazio |
| Duração Curso | Número (horas) | Script 2B | PT30H vs PT40H muda workload |
| Márcio é instrutor? | Sim/Não | Script 2B | teacher field depende disso |
| Formação Márcio | Texto | Person enrichment | educationalLevel, alumniOf |
| Foto do Márcio HD | Arquivo WebP | Person + blog | image width/height para 600px |
| Horários por cidade | JSON | Script 1 | openingHoursSpecification × 13 |
| Responsável por cidade | Nome × 13 | Schema contactPoint | ContactPoint.name por hub |

### A Pedir para os Donos (ALTA PRIORIDADE)

| Campo | Tipo | Para | Impacto |
|---|---|---|---|
| Tabela de preços | CSV (equipamento × período) | Service offers | Pricing strategy |
| Modelos Clark | Lista + specs | Product nodes | Especificações técnicas |
| Fotos de equipamentos | 14 WebP | hasOfferCatalog | +50% E-E-A-T |
| Case studies | 2-3 projetos reais | Blog/CreativeWork | Proof of work |
| Depoimentos | 5-10 clientes | Customer Review nodes | Social proof |
| FAQ técnicas | 20 Q&A | FAQPage | +LSI keywords |
| Certificações Márcio | Datas e números | Person.award | Credibilidade |

### A Pedir para os Donos (BÔNUS)

| Campo | Tipo | Para | Impacto |
|---|---|---|---|
| Vídeos YouTube | Links reais | Video nodes | +Rich results |
| Fundador(es) | Nomes | founder field | History/legacy |
| Missão/Visão | Texto (100-200 chars) | About page | Brand authority |
| Artigos publicados | Links | External mentions | Domain authority |
| Trustpilot/Google Reviews | Score + link | aggregateRating | Social proof |
| Timeline 2019-2026 | Events + numbers | History section | Growth narrative |

---

## Conclusão

**Já temos: ~70% dos dados críticos**
- Schema é robusto e bem estruturado
- Home page é uma referência de Elite schema (19 nós completos)

**Faltam: ~30% para E-E-A-T perfeito (85+/100)**
- Dados de preço + duração (Script 2B bloqueado)
- Imagens de produtos (ausentes)
- FAQ e conteúdo expandido (parcial)
- Depoimentos e case studies (ausentes)

**Ação imediata:** Coletar apenas os 7 campos CRÍTICOS da tabela acima.  
Resto pode vir em paralelo.
