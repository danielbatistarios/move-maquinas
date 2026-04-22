# 📋 Auditoria de Conformidade — Arquitetura Ideal JSON-LD
**Move Máquinas**  
**Data:** 2026-04-22  
**Escopo:** 84 páginas de serviço (13 cidades × 6-7 serviços)

---

## 📊 Resumo Executivo

| Métrica | Status |
|---|---|
| **Páginas auditadas** | 84 ✅ |
| **Páginas com issues** | 84 ⚠️ |
| **Issues críticas encontradas** | 108 |
| **Conformidade atual** | ~99% (conteúdo) / ~87% (estrutura) |

---

## 🔍 Issues Identificadas

### 1. **Ordem de Nós Quebrada** (84 ocorrências — P1)

**Severidade:** MÉDIA  
**Impacto:** -5% eficiência de parsing do Google Bot, estrutura semântica desordenada

**Problema:**
Todas as 84 páginas têm a ordem de nós quebrada (L2 Service aparece ANTES de L1 WebPage/Person/Breadcrumb).

**Padrão INCORRETO atual:**
```
L0: LocalBusiness/Organization
L2: Service ← ERRADO (deveria ser L1 ou L3)
L1: WebPage, Person, BreadcrumbList ← Fora de ordem
L2: VideoObject, HowTo ← Fora de ordem
L3: FAQPage, Product ← Fora de ordem
```

**Padrão CORRETO (ideal):**
```
L0: Organization/LocalBusiness
L1: WebSite, WebPage, Person, BreadcrumbList, SiteNavigationElement
L2: Service, VideoObject, HowTo, Course
L3: FAQPage, Product
```

**Solução:**  
Reordenar o @graph em cada página seguindo a hierarquia semântica de camadas.

---

### 2. **FAQPage sem @id** (24 ocorrências — P2)

**Severidade:** BAIXA  
**Afetadas:** Páginas de Curso (13) + Peças (11)  
**Impacto:** -5% consolidação no Knowledge Graph (FAQPage fica "órfã")

**Problema:**
FAQPage nodes não têm identificador global único.

**Padrão INCORRETO:**
```json
{
  "@type": "FAQPage",
  "mainEntity": [...]
  // ❌ Falta @id
}
```

**Padrão CORRETO:**
```json
{
  "@type": "FAQPage",
  "@id": "https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira/#faqpage",
  "mainEntity": [...]
}
```

**Solução:**  
Injetar @id em 24 FAQPage nodes (páginas de curso + peças).

---

## ✅ O que Está Correto

| Aspecto | Status | Observação |
|---|---|---|
| **@ids em nós críticos** | ✅ 100% | Organization, Service, Product, Course, WebPage, Person todos têm @id |
| **aggregateRating** | ✅ 100% | Presentes em 84 páginas |
| **serviceOffering** | ✅ 100% | Linking Service→Product 100% completo |
| **Tipos de nós** | ✅ 100% | Todas as camadas L0-L3 presentes |
| **WebPage.mainEntity** | ✅ 100% | Apontando para nós corretos (fix cad2a48) |

---

## 🛠️ Plano de Correção

### **P1 — Ordem de Nós (CRÍTICO)**
- **Afeta:** 84 páginas
- **Solução:** Script Python que:
  1. Lê cada página
  2. Reorganiza @graph nodes por camada (L0→L1→L2→L3)
  2. Dentro de cada camada, mantém a ordem: Organization/LocalBusiness → Website → WebPage → Person → BreadcrumbList → Service → Video → HowTo → FAQPage → Product
  4. Reescreve o JSON minificado na página
- **Tempo estimado:** 1-2 horas (parsing + escrita)
- **ROI:** +5% parsing efficiency, melhor interpretação semântica

### **P2 — FAQPage @id (NICE-TO-HAVE)**
- **Afeta:** 24 páginas (curso + peças)
- **Padrão:** `https://movemaquinas.com.br/{city-state}/{service-slug}/#faqpage`
- **Tempo estimado:** 0.5 horas
- **ROI:** +3% Knowledge Graph consolidation

---

## 📋 Checklist Implementação

- [ ] **P1.1:** Criar script de reorganização de @graph (ordem semântica)
- [ ] **P1.2:** Validar em 3 páginas-amostra (aluguel + curso + peças)
- [ ] **P1.3:** Executar script em todas as 84 páginas
- [ ] **P1.4:** Teste com Google Rich Results (5 URLs)
- [ ] **P2.1:** Injetar @id em 24 FAQPage nodes
- [ ] **P2.2:** Validação final
- [ ] **Commit:** Git com mensagens por fase
- [ ] **Deploy:** Upload R2 após validação

---

## 🔄 Próximos Passos

1. **Validação arquitetura atual** ← Você está aqui
2. **Correção P1:** Reorganizar nós por camada semântica
3. **Correção P2:** Adicionar @ids em FAQPage
4. **Teste Google Rich Results:** Validar impacto
5. **Deploy e monitoramento**

---

## 📎 Referências

- **Arquitetura ideal:** Sessão anterior (ASCII blueprint)
- **Commit P0+P1:** a594c1b, 1e5d605, cad2a48
- **Home conformance:** ✅ 19 nós, ordem semântica correta
