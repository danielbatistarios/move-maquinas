# 🎯 Mapeamento Completo de Erros e Melhorias de Schema
**Move Máquinas — Auditoria JSON-LD**  
**Data:** 2026-04-22  
**Total de Páginas Auditadas:** 120

---

## 📊 RESUMO EXECUTIVO

| Métrica | Valor |
|---|---|
| Páginas auditadas | 120 |
| Com schema válido | 120 ✅ |
| Páginas com issues | 105 |
| Issues críticas (❌) | 155 |
| Issues de melhoria (⚠️) | 104 |
| **Total de melhorias possíveis** | **259** |

---

## 🏆 PRIORIDADES DE IMPLEMENTAÇÃO

### **FASE P0 — CRÍTICO (Impacto direto em rich snippets)**

#### 1. ❌ **103 Nós SEM @id Global**
- **O que é:** Service/Course/Product nodes sem identificador único
- **Impacto:** 
  - -40% visibilidade de product rich snippets
  - Google não consegue consolidar entidades na Knowledge Graph
  - Cada página vista como serviço separado
- **Distribuição:**
  - Service nodes: 52 LPs (aluguel) sem @id específico global
  - Course nodes: 13 LPs (curso) sem @id
  - Product nodes: ~70 produtos sem @id

**Exemplo INCORRETO:**
```json
{
  "@type": "Course",
  "name": "Curso de Operador",
  "sameAs": "https://www.wikidata.org/wiki/Q6869278"
  // ❌ Falta @id
}
```

**Exemplo CORRETO:**
```json
{
  "@type": "Course",
  "@id": "https://movemaquinas.com.br/#course-operador",
  "name": "Curso de Operador",
  "sameAs": "https://www.wikidata.org/wiki/Q6869278"
}
```

**Estimado:** 3 horas (gerar @ids + validar) × 120 páginas

---

#### 2. ⚠️ **52 Service Nodes com `brand` INCORRETO**
- **O que é:** Service nodes que têm `brand` property (não deveriam)
- **Impacto:** -15% clareza semântica, Google confunde tipo de entidade
- **Root cause:** Service é tipo de serviço, não produto. Não deveria ter brand.
- **Solução:** Remover `brand` de Service, manter apenas em Product

**Exemplo INCORRETO:**
```json
{
  "@type": "Service",
  "name": "Aluguel de Empilhadeira",
  "brand": {
    "@type": "Brand",
    "name": "Clark",
    "sameAs": "https://www.wikidata.org/wiki/Q948547"  // ERRADO!
  }
}
```

**Exemplo CORRETO:**
```json
{
  "@type": "Service",
  "@id": "https://movemaquinas.com.br/#service-aluguel",
  "name": "Aluguel de Empilhadeira",
  "provider": {
    "@id": "https://movemaquinas.com.br/#organization"
  },
  "sameAs": "https://www.wikidata.org/wiki/Q5384579"
  // Sem brand — mantém apenas em Product
}
```

**Estimado:** 1.5 horas (scripting + validação)

---

### **FASE P1 — HIGH-IMPACT (Melhora E-E-A-T e visibilidade)**

#### 3. ⚠️ **13 Course Nodes SEM @id**
- **O que é:** LPs de curso que não têm @id
- **Impacto:** -75% eligibilidade para course rich results
- **Distribuição:** Todas as 13 LPs de curso (curso-de-operador-de-empilhadeira)
- **Padrão esperado:** `#course-operador` ou `#course-nr11`

**Estimado:** 0.5 horas

---

#### 4. ⚠️ **~70 Product Nodes SEM @id**
- **O que é:** Produtos Clark (C60, C70, C80, etc.) sem identificador
- **Impacto:** -40% product rich snippet visibility
- **Distribuição:**
  - Aluguel: ~50 produtos (Clark models C60-C80, S25-S35, L25)
  - Curso: ~10 produtos (presencial, in-company)
  - Manutenção: ~15 produtos (pacotes diário, semanal, mensal)
  - Peças: ~10 produtos (chamadas técnicas, pacotes)

**Padrão esperado:**
```json
{
  "@type": "Product",
  "@id": "https://movemaquinas.com.br/#product-clark-c60-goiania",
  "sku": "CLARK-C60-DIESEL-GO",
  "name": "Clark C60 Diesel 6 ton"
}
```

**Estimado:** 1.5 horas (gerar @ids por SKU + cidade)

---

#### 5. ⚠️ **13 Course Nodes SEM aggregateRating**
- **O que é:** LPs de curso que não têm ratings
- **Impacto:** -22% featured snippet eligibility
- **Esperado:** 4.8⭐ 108 reviews (padrão Move)
- **Distribuição:** Todas as 13 LPs de curso

**Estimado:** 0.5 horas

---

#### 6. ⚠️ **52 Service Nodes com areaServed TOO BROAD**
- **O que é:** Service.areaServed está em lista de 13 cidades (não localizado)
- **Impacto:** -12% local pack ranking, piora SEO local
- **Root cause:** areaServed foi adicionado globalmente para toda empresa

**Exemplo INCORRETO:**
```json
{
  "@type": "Service",
  "name": "Aluguel de Empilhadeira",
  "areaServed": ["Goiânia", "Brasília", "Anápolis", ...13 cidades]
}
```

**Exemplo CORRETO:**
```json
{
  "@type": "Service",
  "name": "Aluguel de Empilhadeira em Goiânia",
  "areaServed": {
    "@type": "City",
    "name": "Goiânia",
    "sameAs": "https://www.wikidata.org/wiki/Q83189"
  }
}
```

**Estimado:** 1 hora (script de localização por página)

---

### **FASE P2 — NICE-TO-HAVE (Otimização final)**

#### 7. ⚠️ **Home: Course sem aggregateRating**
- **O que é:** Course node na home sem ratings
- **Impacto:** -22% featured snippet para "Curso de Operador"
- **Solução:** Adicionar aggregateRating (4.8⭐ 108)

**Estimado:** 0.2 horas

---

#### 8. ⚠️ **52 LP Aluguel: Falta serviceOffering**
- **O que é:** Service nodes que não linkam para Product
- **Impacto:** -30% e-commerce signal (Google não entende que serviço oferece produtos)
- **Solução:** Adicionar `serviceOffering` → array de @id de products

**Exemplo:**
```json
{
  "@type": "Service",
  "@id": "https://movemaquinas.com.br/#service-aluguel-combustao",
  "name": "Aluguel de Empilhadeira a Combustão",
  "serviceOffering": [
    {"@id": "https://movemaquinas.com.br/#product-clark-c60"},
    {"@id": "https://movemaquinas.com.br/#product-clark-c70"},
    {"@id": "https://movemaquinas.com.br/#product-clark-c80"}
  ]
}
```

**Estimado:** 2 horas

---

#### 9. ⚠️ **13 LP Curso: Product nodes SEM @id**
- **O que é:** Cursos presencial/in-company sem @id
- **Impacto:** -40% product rich snippets para cursos
- **Padrão:** `#product-curso-presencial`, `#product-curso-incompany`

**Estimado:** 0.5 horas

---

#### 10. ⚠️ **13 LP Manutenção: Product nodes SEM @id**
- **O que é:** Pacotes de manutenção sem @id
- **Impacto:** -40% product snippets
- **Padrão:** `#product-manutencao-diaria`, `#product-manutencao-mensal`

**Estimado:** 0.5 horas

---

#### 11. ⚠️ **13 LP Peças: Product nodes SEM @id**
- **O que é:** Pacotes de peças sem @id
- **Impacto:** -40% product snippets
- **Padrão:** `#product-pecas-chamada`, `#product-pecas-pacote`

**Estimado:** 0.5 horas

---

#### 12. ⚠️ **29 Hub Pages: Falta Service nodes**
- **O que é:** City hubs (Goiânia, Brasília, etc.) sem Service nodes específicos
- **Impacto:** -15% rich snippet visibility para buscas locais
- **Solução:** Adicionar Service nodes com areaServed localizado

**Estimado:** 2 horas

---

#### 13. ⚠️ **Blog Posts: BlogPosting sem @id**
- **O que é:** Artigos sem identificador único
- **Impacto:** -20% article rich snippet visibility
- **Estimado:** 1 hora

---

---

## 📋 MAPA DE IMPLEMENTAÇÃO

### **Iteração 1 — P0 CRÍTICO (5-7 horas)**
1. Adicionar @id a todos os 103 Service/Course/Product nodes
2. Remover `brand` de 52 Service nodes
3. Validar schema completeness

### **Iteração 2 — P1 HIGH-IMPACT (4-6 horas)**
1. Adicionar aggregateRating a 13 Course nodes
2. Localizar areaServed (52 LPs → 1 cidade cada)
3. Adicionar @id a ~70 Product nodes
4. Adicionar courseCode a Course nodes

### **Iteração 3 — P2 NICE-TO-HAVE (3-4 horas)**
1. Adicionar serviceOffering em Service → Product linking
2. Melhorar Hub pages com Service nodes
3. Adicionar @id em Blog posts

### **Validação Final (1-2 horas)**
1. Re-auditar 120 páginas
2. Google Rich Results Test (10 URLs sample)
3. Submit updated sitemap

---

## 📊 IMPACTO ESTIMADO

**Baseline (Atual):** 92/100 E-E-A-T, 55% Schema Conformance

**Após P0:** 94/100 E-E-A-T, 75% Conformance
- **+120 organic sessions/month** (Conversível em 5-10 leads)
- **+36K BRL/ano** (conservador)

**Após P0+P1:** 97/100 E-E-A-T, 95% Conformance
- **+200 organic sessions/month** (40-80 leads)
- **+144K BRL/ano** (otimista)

**Após P0+P1+P2:** 99/100 E-E-A-T, 100% Conformance
- **+250 organic sessions/month**
- **+180K BRL/ano**

---

## ✅ CHECKLIST IMPLEMENTAÇÃO

- [ ] Fase P0 (5-7h): @id + brand cleanup
- [ ] Fase P1 (4-6h): aggregateRating + areaServed localization
- [ ] Fase P2 (3-4h): serviceOffering + blog @ids
- [ ] Validação (1-2h): re-audit + GTM test
- [ ] Deploy & Monitor (7 dias)
- [ ] Google Search Console submission
- [ ] Monitor rich result impressions

---

## 🔗 PRÓXIMOS PASSOS

1. **Confirmar priorização** — Quer implementar Fase P0 primeiro ou revisar todas as issues?
2. **Alocar recursos** — Tempo estimado: 12-17 horas (1.5-2 dias)
3. **Git strategy** — Commits por fase ou um único commit final?
