# Auditoria Completa de Schema — Move Máquinas

**Data:** 2026-04-22  
**Status:** ⚠️ 175 Issues encontradas em 53 arquivos  
**Total de arquivos:** 120

---

## Resumo Executivo

| Métrica | Valor |
|---|---|
| JSON-LD válido | 120/120 (100%) ✅ |
| Arquivos com issues | 53/120 (44%) ⚠️ |
| Erros semânticos | 132 |
| Erros Wikidata | 40 |
| Issues em utility pages | 3 |

---

## Problemas Identificados

### Problema 1: Product nodes sem Clark Wikidata (132 issues)

**Padrão:** LPs de aluguel (especialmente plataformas, transpaleteira) têm Product nodes que apontam para brand ausente ou incorreto.

**Esperado:**
```json
{
  "@type": "Product",
  "brand": {
    "@type": "Brand",
    "name": "Clark",
    "sameAs": "https://www.wikidata.org/wiki/Q964158"
  }
}
```

**Encontrado:** `brand.sameAs` apontando para URL incorreta ou vazio

**Arquivos afetados:**
- Todas as LPs de aluguel de PLATAFORMA (articulada, tesoura, transpaleteira)
- Goiânia, Brasília, Anápolis, Aparecida de Goiânia, Caldas Novas, Formosa, Inhumas, Itumbiara, Luziânia, Senador Canedo, Trindade, Uruaçu, Valparaíso
- Total: ~40 páginas × 3 produtos = **~120 Product nodes defeituosos**

**Root cause:** Fase 1 corrigiu apenas LPs de "aluguel-de-empilhadeira-combustao", mas não cobriu os outros 4 tipos de aluguel (plataformas, transpaleteira).

---

### Problema 2: Service nodes sem Wikidata (40 issues)

**Padrão:** LPs de plataformas e transpaleteira têm Service node SEM sameAs Wikidata.

**Esperado:**
```json
{
  "@type": "Service",
  "sameAs": "https://www.wikidata.org/wiki/Q5384579"  // Equipment rental
}
```

**Encontrado:** Service node com `sameAs` ausente

**Arquivos afetados:**
- aluguel-de-plataforma-elevatoria-articulada (13 cidades)
- aluguel-de-plataforma-elevatoria-tesoura (13 cidades, exceto Goiânia)
- aluguel-de-transpaleteira (13 cidades, exceto Goiânia)
- Total: ~30 páginas

---

### Problema 3: Course node na Home sem Wikidata

**Arquivo:** `/index.html`  
**Encontrado:** Course node (para "Curso de Operador") sem sameAs Wikidata

**Esperado:**
```json
{
  "@type": "Course",
  "sameAs": "https://www.wikidata.org/wiki/Q6869278"  // Vocational education
}
```

---

### Problema 4: Utility pages sem schema mínimo

**Arquivos:**
- `/contato/index.html` — LocalBusiness sem aggregateRating
- `/servicos/index.html` — LocalBusiness sem aggregateRating + openingHours

**Impacto:** Menor (páginas suporte, não LPs comerciais)

---

## Plano de Correção

### Fase A: Corrigir Product nodes (132 issues)

Script: `schema-fix-product-brand-wikidata.py`

**Lógica:**
1. Identificar todos os Product nodes
2. Se `brand.sameAs` não for Q964158, corrigir para:
   ```json
   "sameAs": "https://www.wikidata.org/wiki/Q964158"
   ```

**Escopo:**
- Todas as 120 páginas
- ~120 Product nodes defeituosos

**Estimado:** 10 min de execução

---

### Fase B: Corrigir Service nodes (40 issues)

Script: `schema-fix-service-wikidata.py`

**Lógica:**
1. Identificar todos os Service nodes
2. Mapear tipo de serviço (aluguel, curso, manutenção, peças) → Q-code
3. Injetar `sameAs` correto

**Escopo:**
- 91 LPs de serviço (52 aluguel + 13 curso + 13 manutenção + 13 peças)
- 40 Service nodes sem sameAs

**Estimado:** 10 min de execução

---

### Fase C: Utility pages (3 issues)

Manual edit ou script simples

---

## Validação Pós-Correção

1. Re-rodar `auditoria-schema-completa.py`
2. Esperar 0 issues
3. Submeter ao Google Rich Results Test (Phase 3)

---

## Timeline

- **Imediato:** Executar Fase A (Product brand fix)
- **Imediato:** Executar Fase B (Service Wikidata)
- **Imediato:** Corrigir utility pages
- **Após:** Revalidar com auditoria
- **Depois:** Google Rich Results Test (Phase 3)
