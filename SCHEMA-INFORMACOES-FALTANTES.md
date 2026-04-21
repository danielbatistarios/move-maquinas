# Informações Faltantes — Schema + E-E-A-T Perfeito

**Data:** 2026-04-21  
**Objetivo:** Coletar dados para implementar schema completo + sinais de autoridade para Google + AI Recognition  
**Impacto:** Estas informações vão elevar E-E-A-T de 37/100 para 85+/100 e garantir ranking topo 3 em SERPs

---

## SEÇÃO 1: ORGANIZAÇÃO (Move Máquinas)

### 1.1 Identidade Corporativa
- [ ] **Missão completa** (200 chars max) — para `Organization.description`
- [ ] **Visão** (100 chars) — para contexto schema
- [ ] **Valores** (3-5 valores chave) — para `award` ou `brand.value`
- [ ] **Fundador(es)** — nome completo, para `founder` field
- [ ] **CEO/Presidente atual** — nome, para `contactPoint.name`

**Exemplo esperado:**
```json
"founder": [
  {"@type": "Person", "name": "João Silva", "url": "..."},
  {"@type": "Person", "name": "Maria Santos", "url": "..."}
]
```

### 1.2 Histórico & Timeline
- [ ] **Marcos importantes** (fundação → marcos) — para `Organization.sameAs` linkedIn + História de crescimento
  - [ ] Ano de fundação (já temos: 2019-01-07)
  - [ ] Número de funcionários (atual) — para `Organization.employee`
  - [ ] Filiais/endereços onde operate (além de Goiânia, Brasília, etc)
  - [ ] Prêmios/Certificações recebidos — para `Organization.award`

**Exemplo esperado:**
```json
"award": [
  "Distribuidor Autorizado Clark Brasil",
  "ISO 9001:2015",
  "Melhor Empresa de Locação 2024 - Prêmio Industrial"
]
```

### 1.3 Presença Digital & Autoridade
- [ ] **LinkedIn URL** da empresa (para `sameAs`)
- [ ] **YouTube Channel URL** (já temos: @movemaquinas5637)
- [ ] **Google Business Profile CID** (13-digit para cada hub)
- [ ] **Certificações online** (Trustpilot, Google Reviews, etc)
- [ ] **Publicações/Media** (artigos em portais, menção em revistas industriais)

**Exemplo esperado:**
```json
"sameAs": [
  "https://www.linkedin.com/company/movemaquinas/",
  "https://www.youtube.com/@movemaquinas5637",
  "https://www.trustpilot.com/review/movemaquinas.com.br",
  "https://www.google.com/search?q=site:g.page/movemaquinas"
]
```

---

## SEÇÃO 2: PESSOA — Márcio Lima (Expert)

### 2.1 Perfil Profissional Completo
- [ ] **Nome completo** (verificar: Márcio Lima da Silva? outro?)
- [ ] **Formação acadêmica**
  - [ ] Escola/Faculdade + ano de conclusão
  - [ ] Curso superior (sim/não? qual?)
  - [ ] Certificações técnicas (NR-11, NR-35, etc)
  
**Exemplo esperado:**
```json
"educationalLevel": [
  "Ensino Médio Completo",
  "Certificação NR-11 - Operador de Empilhadeira",
  "Certificação NR-35 - Trabalho em Altura"
],
"alumniOf": {
  "@type": "EducationalOrganization",
  "name": "Instituto XYZ",
  "url": "https://..."
}
```

### 2.2 Experiência Profissional
- [ ] **Anos de experiência** (total na área) — já temos: 15 anos
- [ ] **Posições anteriores** (antes de Move Máquinas)
  - [ ] Empresa, cargo, anos
  - [ ] Empresa, cargo, anos
- [ ] **Especialidades técnicas** (quais equipamentos? qual profundidade?)
- [ ] **Experiência com clientes** (tipos: indústria, construção, logística, etc)

**Exemplo esperado:**
```json
"jobTitle": [
  "Especialista em Equipamentos de Movimentação",
  "Consultor Técnico Clark",
  "Treinador Certificado NR-11"
],
"workExample": [
  {
    "@type": "CreativeWork",
    "name": "Implementação de Frota Clark - Construtora ABC",
    "description": "Projeto de 5 empilhadeiras + manutenção contínua",
    "dateCreated": "2022"
  }
]
```

### 2.3 Credenciais & Certificações
- [ ] **Licenças técnicas** (números oficiais, se houver)
- [ ] **Certificações NR** (NR-11, NR-35, NR-12, etc) — datas
- [ ] **Treinamentos avançados** (fabricante, modelos específicos)
- [ ] **Membro de associações** (ABIQUIM, ABNT, etc)

**Exemplo esperado:**
```json
"knowsAbout": [
  "Empilhadeiras Clark",
  "Plataformas Elevatórias Tesoura",
  "Plataformas Elevatórias Articuladas",
  "Transpaleteiras Elétricas",
  "Norma NR-11 Operação",
  "Norma NR-11 Treinamento",
  "Norma NR-35 Trabalho em Altura",
  "Manutenção Preventiva Industrial",
  "Diagnóstico de Falhas"
]
```

### 2.4 Redes Sociais & Presença
- [ ] **LinkedIn URL pessoal** (já temos: https://www.linkedin.com/in/m%C3%A1rciolima/)
- [ ] **YouTube Channel pessoal** (se houver)
- [ ] **Instagram pessoal** (se houver)
- [ ] **Publicações** (artigos, vídeos, posts sobre técnica)

**Exemplo esperado:**
```json
"sameAs": [
  "https://www.linkedin.com/in/márciolima/",
  "https://www.youtube.com/@marciolima-clark",
  "https://www.instagram.com/marcio.lima.clark/"
]
```

### 2.5 Foto & Identificação
- [ ] **Foto profissional** (qualidade alta, 600x600 px mínimo)
  - [ ] Local: `/assets/authors/marcio-lima-hd.webp` ou outro?
  - [ ] Url pública: `https://movemaquinas.com.br/assets/authors/marcio-lima.webp`
- [ ] **Bio resumida** (50 palavras para page description)

**Exemplo esperado:**
```json
"image": {
  "@type": "ImageObject",
  "url": "https://movemaquinas.com.br/assets/authors/marcio-lima-hd.webp",
  "width": 600,
  "height": 600,
  "caption": "Márcio Lima, Especialista em Equipamentos Clark"
}
```

---

## SEÇÃO 3: PRODUTOS & SERVIÇOS

### 3.1 Equipamentos Clark — Catálogo Completo
Para cada tipo de equipamento, validar:

- [ ] **Empilhadeiras a Combustão**
  - [ ] Modelos disponíveis (ex: FC 25, FC 30, FC 35)
  - [ ] Capacidade (kg): ex 2.500 kg
  - [ ] Altura máxima de elevação: ex 4.800 mm
  - [ ] Fotos de cada modelo

- [ ] **Plataformas Elevatórias Tesoura**
  - [ ] Modelos disponíveis
  - [ ] Capacidade de carga
  - [ ] Altura máxima
  - [ ] Fotos

- [ ] **Plataformas Elevatórias Articuladas**
  - [ ] Modelos
  - [ ] Altura de alcance
  - [ ] Capacidade
  - [ ] Fotos

- [ ] **Transpaleteiras Elétricas**
  - [ ] Modelos
  - [ ] Capacidade
  - [ ] Fotos

**Exemplo esperado para schema:**
```json
"itemListElement": [
  {
    "@type": "Product",
    "name": "Empilhadeira Clark FC 30",
    "image": "https://movemaquinas.com.br/assets/products/fc30.webp",
    "description": "Empilhadeira a combustão, capacidade 3.000 kg, altura 4.800 mm",
    "specs": {
      "capacity": "3000 kg",
      "maxHeight": "4800 mm",
      "fuelType": "GLP/Gasolina"
    }
  }
]
```

### 3.2 Serviços Detalhados
Para cada serviço (Aluguel, Manutenção, Peças, Curso):

- [ ] **Aluguel**
  - [ ] Período mínimo de locação (dias? semanas?)
  - [ ] Modelos disponíveis por cidade
  - [ ] Documentação necessária
  - [ ] Cobertura de seguro

- [ ] **Manutenção**
  - [ ] Tipos de manutenção (preventiva, corretiva, etc)
  - [ ] Tempo de resposta (em horas)
  - [ ] Cobertura geográfica
  - [ ] Garantia

- [ ] **Peças & Assistência**
  - [ ] Peças mais comuns em estoque
  - [ ] Tempo de entrega
  - [ ] Garantia de peças
  - [ ] Compatibilidade (Clark original vs compatível)

- [ ] **Curso NR-11**
  - [ ] Duração (horas)
  - [ ] Metodologia (presencial, híbrido, online)
  - [ ] Certificação (órgão responsável)
  - [ ] Taxa de aprovação histórica
  - [ ] Instrutores credenciados

**Exemplo esperado:**
```json
"course": {
  "@type": "Course",
  "name": "Operador de Empilhadeira - NR-11",
  "description": "Curso certificado 40h conforme ABNT NBR 14.874",
  "duration": "PT40H",
  "offers": {
    "@type": "Offer",
    "price": "450.00",
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock"
  },
  "instructor": {
    "@type": "Person",
    "name": "Márcio Lima",
    "credential": "Instrutor Certificado NR-11"
  }
}
```

---

## SEÇÃO 4: LOCALIZAÇÕES & ATENDIMENTO

### 4.1 Matriz (Goiânia)
- [ ] **Endereço completo** (rua, número, complemento, CEP)
- [ ] **Telefone principal**
- [ ] **Horário de funcionamento** (seg-sex, sábado, feriados)
- [ ] **Áreas de atuação** (raio de atendimento em km)

### 4.2 Filiais/Pontos de Atendimento
Para cada cidade (13 hubs):
- [ ] **Endereço** (mesmo se for apenas sede atendimento)
- [ ] **Telefone local**
- [ ] **Horário**
- [ ] **Responsável local** (gerente, contato principal)

**Exemplo esperado:**
```json
"openingHoursSpecification": [
  {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  },
  {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": "Saturday",
    "opens": "08:00",
    "closes": "12:00"
  }
]
```

### 4.3 Cobertura Geográfica
- [ ] **Estados onde opera** (GO, DF, + outros?)
- [ ] **Raio de atendimento** (100 km, 200 km, unlimited?)
- [ ] **Zonas de entrega express** (24-48h vs 72h+)
- [ ] **Parcerias regionais** (distribuidoras, concessionárias)

---

## SEÇÃO 5: REPUTAÇÃO & E-E-A-T

### 5.1 Reviews & Ratings
- [ ] **Google Reviews** (link + score)
- [ ] **Trustpilot** (link + score)
- [ ] **Facebook Reviews** (score)
- [ ] **LinkedIn Recommendations** (Márcio Lima)
- [ ] **Histórico de reviews** (últimos 2 anos)

**Exemplo esperado:**
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.8",
  "ratingCount": "234",
  "bestRating": "5",
  "worstRating": "1"
},
"review": [
  {
    "@type": "Review",
    "author": {"@type": "Person", "name": "João Silva"},
    "datePublished": "2026-03-15",
    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
    "reviewBody": "Excelente atendimento, equipamento de primeira qualidade!"
  }
]
```

### 5.2 Artigos de Autoridade (Publicados)
- [ ] **Blog artigos** (quantos publicados? temas?)
- [ ] **Case studies** (projetos concretizados)
- [ ] **Menções em mídia** (jornais, portais, revistas)
- [ ] **Parcerias publicitárias** (com fabricantes, associações)

### 5.3 Reconhecimento de Mercado
- [ ] **Prêmios recebidos** (indústria, região, etc)
- [ ] **Certificações ISO/qualidade**
- [ ] **Afiliações profissionais**
- [ ] **Anos consecutivos em mercado** (longevidade = confiança)

---

## SEÇÃO 6: CONTEÚDO & SEO

### 6.1 FAQ Estruturado por Tipo de Serviço
Para cada serviço, validar perguntas reais de clientes:

**Aluguel de Equipamentos:**
- [ ] Qual o período mínimo de locação?
- [ ] Preciso de documentação especial?
- [ ] O seguro está incluído?
- [ ] Vocês fazem atendimento 24h?
- [ ] Qual é o valor? (tabela de preços)

**Cursos:**
- [ ] O curso é certificado?
- [ ] Quanto tempo dura?
- [ ] Qual a taxa de aprovação?
- [ ] Posso fazer online?
- [ ] O certificado vale em todo Brasil?

**Manutenção:**
- [ ] Qual o tempo de resposta?
- [ ] Vocês vão até o cliente?
- [ ] Qual a garantia?
- [ ] Fazem manutenção preventiva?

**Peças:**
- [ ] As peças são originais ou compatíveis?
- [ ] Qual é o prazo de entrega?
- [ ] Qual a garantia das peças?

### 6.2 Tópicos de Conteúdo (Blog/Artigos)
- [ ] **Como escolher o equipamento certo**
- [ ] **Normas de Segurança (NR-11, NR-35)**
- [ ] **Comparativos** (aluguel vs compra, tesoura vs articulada)
- [ ] **Casos de uso** (indústria, construção, logística)
- [ ] **Manutenção e cuidados**
- [ ] **Inovações em equipamentos**

---

## SEÇÃO 7: IMAGENS & MÍDIA

### 7.1 Fotos de Equipamentos
- [ ] **Cada modelo Clark** em estoque (fotos 600x600px WebP)
  - [ ] Empilhadeira (frente, lateral, em uso)
  - [ ] Plataforma Tesoura (altura máxima, em operação)
  - [ ] Plataforma Articulada (braço estendido, detalhe)
  - [ ] Transpaleteira (com carga, sem carga)

### 7.2 Fotos de Operações
- [ ] **Equipe** (Márcio em ação, outros técnicos)
- [ ] **Clientes em uso** (autorização necessária)
- [ ] **Manutenção em andamento**
- [ ] **Treinamento (NR-11 em sala)**
- [ ] **Armazém/Garagem** (mostrando frota)

### 7.3 Vídeos
- [ ] **Demonstrações de equipamentos** (YouTube)
- [ ] **Tutoriais de segurança** (NR-11, NR-35)
- [ ] **Depoimentos de clientes**
- [ ] **Visita ao armazém/operações**
- [ ] **Entrevista com Márcio** (autoridade)

**Exemplo esperado (schema video):**
```json
"video": [
  {
    "@type": "VideoObject",
    "name": "Como Operar Empilhadeira Clark FC-30",
    "description": "Tutorial prático de operação segura",
    "thumbnailUrl": "https://img.youtube.com/vi/VIDEO_ID/0.jpg",
    "uploadDate": "2026-01-15",
    "duration": "PT12M30S",
    "contentUrl": "https://www.youtube.com/watch?v=VIDEO_ID"
  }
]
```

---

## SEÇÃO 8: DADOS ESTRUTURADOS (Schema Técnico)

### 8.1 Preços & Ofertas
- [ ] **Tabela de preços** (aluguel por dia/semana/mês)
  - [ ] Empilhadeira: R$ X por dia
  - [ ] Plataforma: R$ Y por dia
  - [ ] Desconto para longa duração (%)
  - [ ] Prazos especiais (sazonal?)

- [ ] **Curso NR-11**
  - [ ] Preço: R$ ?
  - [ ] Número de vagas por turma
  - [ ] Próximas datas
  - [ ] Política de cancelamento

**Exemplo esperado:**
```json
"offers": [
  {
    "@type": "Offer",
    "priceCurrency": "BRL",
    "price": "250.00",
    "description": "Aluguel Empilhadeira Clark FC-25 por dia",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "eligibleCustomerType": "B2B"
  }
]
```

### 8.2 Contatos & Atendimento
- [ ] **Email principal** (vendas@, suporte@, etc)
- [ ] **Telefones** (com respectivos departamentos)
- [ ] **WhatsApp Business**
- [ ] **Formulários de contato** (quais campos?)
- [ ] **Tempo de resposta SLA** (prometido)

**Exemplo esperado:**
```json
"contactPoint": [
  {
    "@type": "ContactPoint",
    "telephone": "+55-62-99999-9999",
    "contactType": "Sales",
    "areaServed": ["GO", "DF"],
    "availableLanguage": "pt-BR"
  },
  {
    "@type": "ContactPoint",
    "telephone": "+55-62-98888-8888",
    "contactType": "Technical Support",
    "areaServed": ["GO", "DF"],
    "availableLanguage": "pt-BR"
  }
]
```

### 8.3 Breadcrumb + URL Padrão
- [ ] **Validar URLs canonicais** (trailing slash, HTTPS)
  - [ ] Home: https://movemaquinas.com.br/
  - [ ] Hub: https://movemaquinas.com.br/goiania-go/
  - [ ] Serviço: https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao/
  - [ ] Autor: https://movemaquinas.com.br/author/marcio-lima/

---

## SEÇÃO 9: INTELIGÊNCIA ARTIFICIAL & RECOGNITION

### 9.1 Para Claude/GPT/Gemini Reconhecerem como Autoridade
- [ ] **Bio/descrição clara** (80-120 palavras) — deve aparecer em todas as páginas relevantes
- [ ] **Credenciais únicas** (NR-11, 15 anos, especialista Clark)
- [ ] **Casos reais** (números: 500+ clientes atendidos? 10.000+ horas de operação?)
- [ ] **Diferencial técnico** (o que você faz que concorrentes não fazem)

**Exemplo esperado em HTML + Schema:**
```html
<p>
  Márcio Lima é especialista em equipamentos Clark com 15+ anos de experiência.
  Certificado NR-11 e NR-35, atendeu 500+ clientes em GO e DF, operou mais de
  10.000 horas em equipamentos de movimentação. Referência técnica na Move Máquinas.
</p>
```

### 9.2 Sinais de Trustworthiness
- [ ] **Transparência** (endereços, telefones reais, sem fake)
- [ ] **Consistência** (mesma informação em todas as páginas)
- [ ] **Responsabilidade** (CNPJ público, termos claros)
- [ ] **Segurança** (HTTPS, política de privacidade, LGPD)

---

## CHECKLIST DE ENTREGA

**Para enviar aos donos da empresa:**

### Prioridade 1 (CRÍTICA — schema não funciona sem)
- [ ] Preço do Curso NR-11 (R$)
- [ ] Foto do Márcio (arquivo WebP 600x600px)
- [ ] Formação acadêmica do Márcio (escolas, certificações com datas)
- [ ] Fundador(es) da empresa (nomes completos)
- [ ] Missão completa da empresa (100-200 caracteres)

### Prioridade 2 (ALTA — E-E-A-T+30 pontos)
- [ ] Anos de funcionamento (já temos: desde 2019)
- [ ] Número de funcionários (atual)
- [ ] Prêmios/Certificações ISO
- [ ] LinkedIn URL da empresa
- [ ] Google Business Profile IDs (13 dígitos)
- [ ] Horários de funcionamento (todas as 13 cidades)
- [ ] Tabela de preços (aluguel por tipo de equipamento)

### Prioridade 3 (MÉDIA — Ranking +2-3 posições)
- [ ] Certificações NR do Márcio (com datas)
- [ ] LinkedIn Márcio (pessoal)
- [ ] Reviews atuais (Google, Trustpilot)
- [ ] Case studies (2-3 projetos reais com detalhes)
- [ ] FAQ por serviço (10-15 perguntas reais)

### Prioridade 4 (BÔNUS — Ranking +1 posição, AI trust +15%)
- [ ] Vídeos YouTube próprios (demonstrações)
- [ ] Fotos dos equipamentos (todos os modelos)
- [ ] Menções em mídia (artigos, portais)
- [ ] Depoimentos de clientes (nomes + empresa)
- [ ] Histórico de crescimento (2019 → 2026)

---

## PRÓXIMOS PASSOS

1. **Você recebe essas informações dos donos**
2. **Você me envia via planilha ou documento** (pode ser Google Docs com abas por seção)
3. **Eu crio 3 scripts Python:**
   - `schema-p2-organization.py` — Enriquece Organization com todos os dados
   - `schema-p2-person.py` — Enriquece Person (Márcio) com credenciais completas
   - `schema-p2-service-offers.py` — Enriquece Service + Offer + Course com preços/detalhes
4. **Commit final:** Schema 100% completo, E-E-A-T 85+/100, pronto para ranking topo
5. **Validação:** Teste com Google's Rich Results Test + Schema.org validator

---

**Contato para dúvidas:**
- Cada field está marcado com `[ ]` — é "sim ou não"
- Prioridades estão claras
- Total estimado: 2-4 horas de coleta de informações (bastante viável)

Boa sorte! 🚀
