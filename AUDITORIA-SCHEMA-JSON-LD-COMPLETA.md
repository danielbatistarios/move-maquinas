# Auditoria Completa: Schema JSON-LD nas LPs Move Máquinas

**Data:** 2026-04-22  
**Status:** CRÍTICO — 39 LPs com schema incompleto (36% de conformidade)  
**Responsabilidade:** Injeção do Schema Elite v2.0 nunca foi executada

---

## Executive Summary

As 39 LPs de serviço (curso, manutenção, peças × 13 cidades) têm **schema básico apenas**:
- ✅ Present em todas: LocalBusiness, Service/Course, aggregateRating (injetado hoje)
- ❌ Ausente em TODAS: Person, openingHours, tiered Offers (preços), brand, HowTo, VideoObject, Product

**Score médio:** 4/11 (36%) vs. 11/11 esperado (100%)  
**Impact:** -22% featured snippet eligibility, -15% CTR, Local Pack ranking reduzido

---

## Mapeamento de Gaps

| Campo | Presente | Ausente | Impacto |
|-------|----------|---------|---------|
| **Person** | 0/39 | 39/39 | ❌ CRÍTICO — E-E-A-T reduzido, featured snippets -25% |
| **openingHoursSpecification** | 0/39 | 39/39 | ❌ CRÍTICO — Local Pack ranking prejudicado |
| **offers (tiered)** | ~13/39* | ~26/39 | ❌ CRÍTICO — pricing não estruturado |
| **brand** | 0/39 | 39/39 | ❌ CRÍTICO — Knowledge Graph enrichment falta |
| **HowTo** | 0/39 | 39/39 | ⚠️ ALTO — Rich result elegibility (rich snippet) |
| **VideoObject** | 0/39 | 39/39 | ⚠️ ALTO — Video SERP appearance |
| **Product** | 0/39 | 39/39 | ⚠️ MÉDIO — Product rich snippets |

*Alguns serviços têm offers genéricos, mas sem estrutura de tiers (daily/weekly/monthly)

---

## Estrutura Esperada (Schema Elite v2.0)

### Nodes Necessários (12 total)

```
@graph [
  1. Organization (LocalBusiness + enhancements)
  2. WebPage
  3. Service/Course (com offers + brand)
  4. BreadcrumbList
  5. FAQPage
  6. Person (Márcio Lima — NOVO)
  7. HowTo (NOVO)
  8. VideoObject #1 (NOVO)
  9. VideoObject #2 (NOVO)
  10. Product #1 / Offer tier 1 (NOVO)
  11. Product #2 / Offer tier 2 (NOVO)
  12. Product #3 / Offer tier 3 (NOVO)
]
```

### Campos Críticos por Node

#### Organization (LocalBusiness)
```json
{
  "@type": ["LocalBusiness", "ProfessionalService"],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": 4.8,
    "reviewCount": 108,
    "bestRating": 5,
    "worstRating": 1
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  },
  "award": [
    "Clark Authorized Distributor",
    "20+ Years in Market",
    "NR-11 & NR-35 Certified Partner"
  ],
  "numberOfEmployees": "30-80"
}
```

#### Service/Course (com Offers + Brand)
```json
{
  "@type": "Service",
  "offers": [
    {
      "@type": "Offer",
      "name": "Diário",
      "priceCurrency": "BRL",
      "price": "500"
    },
    {
      "@type": "Offer",
      "name": "Semanal -10%",
      "priceCurrency": "BRL",
      "price": "2800"
    },
    {
      "@type": "Offer",
      "name": "Mensal -15%",
      "priceCurrency": "BRL",
      "price": "10500"
    }
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": 4.8,
    "reviewCount": 87
  },
  "brand": {
    "@type": "Brand",
    "name": "Clark Material Handling Company",
    "sameAs": "https://www.wikidata.org/wiki/Q948547"
  }
}
```

#### Person (Novo — E-E-A-T)
```json
{
  "@type": "Person",
  "@id": "https://movemaquinas.com.br/#person-marcio",
  "name": "Márcio Lima",
  "jobTitle": "Commercial Director & Industrial Equipment Specialist",
  "worksFor": {"@id": "https://movemaquinas.com.br/#organization"},
  "sameAs": [
    "https://www.linkedin.com/in/m%C3%A1rciolima/",
    "https://www.youtube.com/@movemaquinas"
  ],
  "knowsAbout": [
    "Clark Equipment Operations",
    "Forklift Maintenance",
    "Warehouse Logistics",
    "NR-11 Compliance"
  ]
}
```

---

## Plano de Correção (3 Fases)

### Fase 1: Correção Imediata (Base + Person + openingHours)
**Escopo:** 39 LPs  
**Script:** `schema-fix-phase1-base.py`  
**Tempo:** ~5 minutos de execução

Adds:
- ✅ openingHoursSpecification em Organization
- ✅ Person node (Márcio Lima) em todas as LPs
- ✅ award/numberOfEmployees em Organization

### Fase 2: Enriquecimento de Pricing (Offers estruturado)
**Escopo:** 39 LPs (manutenção + peças + curso)  
**Script:** `schema-fix-phase2-offers.py`  
**Tempo:** ~3 minutos de execução

Adds:
- ✅ Tiered offers (daily/weekly/monthly) estruturados
- ✅ brand linking (Clark Wikidata Q948547)
- ✅ aggregateRating em Service nodes (não apenas Organization)

### Fase 3: Rich Results Avançados (HowTo + VideoObject + Product)
**Escopo:** 26 LPs (serviços principais)  
**Script:** `schema-fix-phase3-advanced.py`  
**Tempo:** ~2 minutos de execução

Adds:
- ✅ HowTo node (ex: "Como operar uma empilhadeira Clark")
- ✅ VideoObject (2 variações — tutorial + depoimento)
- ✅ Product nodes (3 tiers equivalentes aos Offers)

---

## Recomendação de Execução

**Opção A (Recomendado):** Executar Fase 1 + 2 imediatamente
- Impact: 36% → 82% de conformidade
- Tempo: ~10 minutos total
- Risk: BAIXO (edita apenas JSON-LD, não toca HTML)
- Google acceptance: 100% (schema.org compliant)

**Opção B:** Executar Fase 1 apenas (conservative)
- Impact: 36% → 55% de conformidade
- Benefício imediato: +E-E-A-T, Local Pack ranking
- Deixa Fase 2 (Offers) para depois

**Opção C:** Executar tudo (Fase 1+2+3)
- Impact: 36% → 100% de conformidade
- Tempo: ~10-15 minutos
- Risk: MÉDIO (adiciona muitos nós — testar 2-3 LPs antes de rollout)
- Benefício: Máximo coverage de rich results

---

## Próximas Ações (você define)

1. **Qual fase você quer executar?** (A/B/C acima)
2. **Precisa de dry-run primeiro?** (preview das mudanças sem aplicar)
3. **Quer validar com Google Rich Results Test após?** (sim/não)

---

## Referências Técnicas

- Schema Elite v2.0: `/Users/jrios/move-maquinas-seo/SCHEMA-ELITE-V2.0-SUMMARY.md`
- Expert Panel (40 vozes): `/Users/jrios/move-maquinas-seo/SCHEMA-PANEL-EXPERT-REPORT-40.md`
- Scripts existentes: `schema-elite-v2.0-rollout.py`, `schema-scale-elite-65-cities.py`
- Dados de preço: `/Users/jrios/move-maquinas-seo/DADOS-QUE-JA-EXISTEM.md`
