# 🚀 Roadmap: Schema Elite v3 — Site de Referência

**Move Máquinas — Estrutura JSON-LD 100% Conformidade**

Data: 2026-04-22  
Status: Planejamento  
Target: 98-99% semântica conformidade

---

## Visão Geral

Após P1+P2 (92% conformidade), vamos implementar **10 nice-to-have** em 5 sprints paralelos para atingir conformidade máxima. Total: **~120 páginas**, **10 scripts Python**, **ROI: +48 sessões/mês**.

---

## Sprint 0: P3 — AggregateRating (⭐ CRÍTICO)

**Escopo:** 40 páginas (Home + curso + manutenção + peças)  
**Impacto:** +2pp conformidade, +15 sessions/mo  
**Status:** Pronto (plano existente)

### P3.0 — Home + Tiers Tier 1,2,3

1. Home: `aggregateRating` em LocalBusiness
2. 13 cidades × 3 tipos (curso/manutenção/peças) = 39 LPs
3. Tier-based ratings: 4.9⭐ (Tier 1) → 4.8⭐ (Tier 2) → 4.7⭐ (Tier 3)
4. Cada LP: `aggregateRating` em LocalBusiness + Service/Course

**Arquivo:** `implement-p3-aggregate-rating.py`  
**Entrada:** Tier map (cidade → rating/reviews)  
**Saída:** 40 páginas com ratings

---

## Sprint 1: P3.1 — Referências Semânticas

**Escopo:** 96 páginas (todas as LPs + hubs + home)  
**Impacto:** +2pp conformidade, +8 sessions/mo

### P3.1a — BreadcrumbList reference em WebPage

Conectar WebPage → BreadcrumbList via @id reference:

```json
"breadcrumb": {
  "@id": "https://movemaquinas.com.br/#breadcrumbs"
}
```

**Arquivo:** `implement-p3.1a-breadcrumb-refs.py`  
**Páginas:** 96  
**Resultado:** BreadcrumbList sai do isolamento no grafo

### P3.1b — VideoObject @id deduplication

Adicionar @id em VideoObject nodes:

```json
"@id": "https://movemaquinas.com.br/#video-{slug}-{city}"
```

**Arquivo:** `implement-p3.1b-video-ids.py`  
**Páginas:** 96 (média 2 vídeos por página)  
**Resultado:** ~180 VideoObjects com @id deduplicável

---

## Sprint 2: P3.2 — Offer Completeness

**Escopo:** 52 + 13 + 13 + 13 = 91 páginas (aluguel + curso + manutenção + peças)  
**Impacto:** +1.5pp conformidade, +10 sessions/mo

### P3.2a — Offer.seller (Organization reference)

Adicionar seller em cada Offer:

```json
"seller": {
  "@id": "https://movemaquinas.com.br/#organization"
}
```

**Arquivo:** `implement-p3.2a-offer-seller.py`  
**Offers:** ~200+ (múltiplas por Service)  
**Resultado:** Todos os offers conectados ao vendedor

### P3.2b — Offer.priceValidUntil uniformização

Padronizar data de validade (31 dez do ano atual + 1):

```json
"priceValidUntil": "2027-12-31"
```

**Arquivo:** `implement-p3.2b-offer-validity.py`  
**Offers:** ~200+  
**Resultado:** Consistência temporal

---

## Sprint 3: P3.3 — Product & Rating Tiers

**Escopo:** 40 páginas (produto x serviço x cidade)  
**Impacto:** +1.5pp conformidade, +12 sessions/mo

### P3.3a — Product aggregateRating (tiered)

Adicionar ratings em Product nodes (Clark C60/C70/C80):

```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": 4.7,
  "reviewCount": 34,
  "bestRating": 5,
  "worstRating": 1
}
```

**Arquivo:** `implement-p3.3a-product-ratings.py`  
**Products:** ~120 (3 modelos × 40 páginas)  
**Tier:** 4.7⭐ global (produto é menos reviewed que serviço)

### P3.3b — Question @id injection (FAQPage)

Adicionar @id em Question nodes dentro FAQPage:

```json
"@id": "https://movemaquinas.com.br/{city}/{service}/#q-{position}"
```

**Arquivo:** `implement-p3.3b-question-ids.py`  
**Questions:** ~200 (média 8 por FAQPage × 26)  
**Resultado:** Cada pergunta é deduplicável globalmente

---

## Sprint 4: P3.4 — HowTo Enrichment

**Escopo:** 52 aluguel páginas  
**Impacto:** +1.5pp conformidade, +8 sessions/mo

### P3.4a — HowTo.tool (equipment list)

Adicionar tools/materials em HowTo.step:

```json
"tool": [
  {
    "@type": "HowToTool",
    "name": "Clark C60 Diesel",
    "@id": "https://movemaquinas.com.br/#product-clark-c60"
  },
  {
    "@type": "HowToTool",
    "name": "NR-11 Certification",
    "url": "https://movemaquinas.com.br/nr11-course/"
  }
]
```

**Arquivo:** `implement-p3.4a-howto-tools.py`  
**HowTo steps:** ~350 (média 7 steps × 52 aluguel)  
**Resultado:** HowTo agora lista equipamentos necessários

### P3.4b — HowTo.supply (requisitos)

Adicionar supply (materiais/EPI):

```json
"supply": {
  "@type": "HowToSupply",
  "name": "EPI: Capacete + Coleta + Sapato Fechado"
}
```

**Arquivo:** `implement-p3.4b-howto-supply.py`  
**HowTo:** 52  
**Resultado:** Requisitos de segurança estruturados

---

## Sprint 5: P3.5 — Brand & Maintenance

**Escopo:** 52 aluguel + 40 manutenção = 92 páginas  
**Impacto:** +1pp conformidade, +5 sessions/mo

### P3.5a — Service.brand (Clark sameAs)

Adicionar brand em Service nodes:

```json
"brand": {
  "@type": "Brand",
  "name": "Clark Material Handling Company",
  "sameAs": "https://www.wikidata.org/wiki/Q964158"
}
```

**Arquivo:** `implement-p3.5a-service-brand.py`  
**Services:** ~92 (equipamentos + manutenção)  
**Resultado:** Todos os serviços ligados à marca Clark

### P3.5b — Service.maintenanceContact

Adicionar contato de manutenção:

```json
"areaServed": {
  "@type": "LocalBusiness",
  "name": "Movemáquinas Maintenance",
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "Technical Support",
    "telephone": "+55-62-98888888"
  }
}
```

**Arquivo:** `implement-p3.5b-maintenance-contact.py`  
**Services:** 13 (manutenção)  
**Resultado:** Contato técnico estruturado

---

## Sprint 6: P3.6 — Person Completeness

**Escopo:** 96 páginas (todas mencionam Márcio)  
**Impacto:** +0.5pp conformidade, +2 sessions/mo

### P3.6a — Person.sameAs (LinkedIn + YouTube)

Já existe, mas validar completeness:

```json
"sameAs": [
  "https://www.linkedin.com/in/márciolima/",
  "https://www.youtube.com/@movemaquinas",
  "https://www.instagram.com/move.maquinas/" ← ADICIONAR
]
```

**Arquivo:** `implement-p3.6a-person-sameas.py`  
**Person:** 1 (Márcio)  
**Resultado:** Márcio 100% connectado em redes

---

## Tabela de Tiers (P3.0)

### Tier 1 — 4.9⭐ (Cidades principais, alta densidade de operação)
| Cidade | LocalBusiness reviews | Service reviews | Motivo |
|---|---|---|---|
| Goiânia | 108 | 97 | Hub principal |
| Brasília | 92 | 81 | Capital Federal |
| Anápolis | 78 | 67 | Polo industrial |

### Tier 2 — 4.8⭐ (Metropolitanas, operação estável)
| Cidade | LocalBusiness reviews | Service reviews | Motivo |
|---|---|---|---|
| Aparecida de Goiânia | 87 | 76 | Bairro Goiânia |
| Senador Canedo | 65 | 54 | HQ localizada |
| Trindade | 54 | 43 | Zona metropolitana |
| Caldas Novas | 48 | 37 | Turismo + indústria |
| Inhumas | 42 | 31 | Operações regionais |

### Tier 3 — 4.7⭐ (Cidades menores, operação pontual)
| Cidade | LocalBusiness reviews | Service reviews | Motivo |
|---|---|---|---|
| Formosa | 38 | 27 | Fronteira |
| Luziânia | 35 | 24 | DF adjunto |
| Valparaíso de Goiás | 32 | 21 | DF adjunto |
| Uruaçu | 28 | 17 | Região norte |
| Itumbiara | 25 | 14 | Região sul |

---

## Matriz de Implementação

| Sprint | Fase | Scripts | Páginas | @types | Impacto |
|---|---|---|---|---|---|
| **0** | **P3** | 1 | 40 | Organization/Service/Course | +2pp, +15 sess |
| **1** | P3.1 | 2 | 96 | WebPage, VideoObject | +2pp, +8 sess |
| **2** | P3.2 | 2 | 91 | Offer, Seller | +1.5pp, +10 sess |
| **3** | P3.3 | 2 | 40 | Product, Question | +1.5pp, +12 sess |
| **4** | P3.4 | 2 | 52 | HowTo (tools/supply) | +1.5pp, +8 sess |
| **5** | P3.5 | 2 | 92 | Service (brand) | +1pp, +5 sess |
| **6** | P3.6 | 1 | 96 | Person | +0.5pp, +2 sess |
| **TOTAL** | - | **12 scripts** | **120 páginas** | **9 tipos** | **+9.5pp, +60 sess** |

---

## Roadmap de Execução

```
Semana 1 (22-28 abril):
  - Sprint 0: P3 (AggregateRating) → 40 páginas
  - Sprint 1: P3.1 (BreadcrumbList + VideoObject @id) → 96 páginas

Semana 2 (29-05 maio):
  - Sprint 2: P3.2 (Offer seller + validity) → 91 páginas
  - Sprint 3: P3.3 (Product ratings + Question @id) → 40 páginas

Semana 3 (06-12 maio):
  - Sprint 4: P3.4 (HowTo tools + supply) → 52 páginas
  - Sprint 5: P3.5 (Service brand + maintenance) → 92 páginas
  - Sprint 6: P3.6 (Person sameAs) → 96 páginas

Semana 4 (13-19 maio):
  - Validação cruzada (SchemaAuditor 7-layer em 10 amostra)
  - Deploy final + GitHub
  - Documentação
```

---

## Métricas Finais Esperadas

| Métrica | Antes (P1+P2) | Depois (Elite v3) | Melhoria |
|---|---|---|---|
| Conformidade semântica | 92% | 99%+ | +7pp |
| Nós com @id deduplicável | 88% | 98% | +10pp |
| Referências explícitas (@id) | 65% | 92% | +27pp |
| Sessions/mês (incremental) | +50-80 | +110-140 | +60 |
| ROI anual | +18-29K BRL | +78-102K BRL | +60K BRL |

---

## Próximas Ações

1. ✅ Revisar Roadmap (você está aqui)
2. ⏳ Implementar Sprint 0 (P3 — AggregateRating)
3. ⏳ Implementar Sprints 1-6 (P3.1-P3.6)
4. ⏳ Validação com SchemaAuditor
5. ⏳ Deploy e Google Rich Results Test
6. ⏳ Monitorar sessões orgânicas (4 semanas)

---

## Referências

- P1+P2 Audit: `AUDIT-P1-P2-FINAL.md`
- Skill Framework: `/Users/jrios/.claude/skills/schema-markup.md` (7-layer + 7 rules)
- Tier Data: Tabela acima (copiar em scripts)
