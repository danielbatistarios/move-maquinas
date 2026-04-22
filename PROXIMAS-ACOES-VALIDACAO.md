# Próximas Ações — Validação + Monitoramento

**Fase:** 3 (Validação e Rollout Final)  
**Status:** Pronta para iniciar  
**Data de Início Recomendada:** 2026-04-23 (D+1)

---

## Checklist de Validação (24h)

### 1. Google Rich Results Test (Obrigatório)

**Ferramenta:** https://search.google.com/test/rich-results

**URLs a Testar (amostra representativa — 10 LPs):**

#### Service Type: Curso (2 LPs)
- [ ] `https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira/`
- [ ] `https://movemaquinas.com.br/brasilia-df/curso-de-operador-de-empilhadeira/`

#### Service Type: Manutenção (2 LPs)
- [ ] `https://movemaquinas.com.br/goiania-go/manutencao-empilhadeira/`
- [ ] `https://movemaquinas.com.br/brasilia-df/manutencao-empilhadeira/`

#### Service Type: Peças (2 LPs)
- [ ] `https://movemaquinas.com.br/goiania-go/pecas-e-assistencia-empilhadeira/`
- [ ] `https://movemaquinas.com.br/brasilia-df/pecas-e-assistencia-empilhadeira/`

#### Service Type: Aluguel (3 LPs) — Fase 1 validation
- [ ] `https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao/`
- [ ] `https://movemaquinas.com.br/brasilia-df/aluguel-de-empilhadeira-eletrica/`
- [ ] `https://movemaquinas.com.br/anapolis-go/aluguel-de-empilhadeira-combustao/`

#### City Hub (1 LP)
- [ ] `https://movemaquinas.com.br/goiania-go/`

### 2. Cada URL — Verificar:
- [ ] **Course schema parsing:** ✅ Valid (não há erro)
- [ ] **Service schema parsing:** ✅ Valid (não há erro)
- [ ] **Product schema parsing:** ✅ Valid (não há erro)
- [ ] **VideoObject parsing:** ✅ Valid (não há erro)
- [ ] **HowTo parsing:** ✅ Valid (não há erro)
- [ ] **AggregateRating parsing:** ✅ Valid (não há erro)
- [ ] **Offers structure:** ✅ Valid (não há erro)

### 3. Erros Encontrados (Se houver)
- [ ] Documentar erro exato
- [ ] Rodar `python3 schema-fix-phase2-elite-nodes.py --city=CIDADE --service=TIPO` para re-processar
- [ ] Re-testar no Rich Results Test

---

## Checklist de GSC (Google Search Console) — 48-72h

### 1. Sitemap Submission
- [ ] Verificar se sitemap está atualizado com todas as 52 LPs
- [ ] Arquivo esperado: `/Users/jrios/move-maquinas-seo/sitemap.xml`
- [ ] Submeter em: https://search.google.com/u/1/search-console
- [ ] Projeto: movemaquinas.com.br

### 2. Monitoramento Inicial
- [ ] Acessar Search Console → Performance
- [ ] Filtro: "Rich result" searches
- [ ] Baseline de impressões (D+0)
- [ ] Alvo: +10% impressões em D+7

### 3. Checklist de Erros GSC
- [ ] Parse errors count: ≤ 5 (aceitável)
- [ ] Mobile usability issues: 0 (novo schema não deve causar)
- [ ] Coverage issues: 0 (novo schema não deve remover URLs)

---

## Monitoramento D+7 a D+14

### Métricas a Acompanhar

| Métrica | Baseline | Target D+7 | Target D+14 |
|---|---|---|---|
| Rich snippets (impressões) | 0 | +20% | +35% |
| Featured snippets (páginas) | ~8 | +2 | +4 |
| Video SERP impressions | 0 | 50+ | 200+ |
| Product rich snippet CTR | N/A | +3% | +8% |
| Course schema appearances | 0 | 5+ | 20+ |

### Onde Monitorar
- **GSC Performance:** https://search.google.com/u/1/search-console
- **Data Studio (opcional):** Criar dashboard com métricas
- **Google Analytics:** Track "Rich result" conversions

---

## Script de Testes (Automático — Opcional)

Se precisar fazer bulk test das URLs:

```bash
#!/bin/bash
# test-rich-results-batch.sh

# Lista de URLs a testar
urls=(
  "https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira/"
  "https://movemaquinas.com.br/brasilia-df/manutencao-empilhadeira/"
  "https://movemaquinas.com.br/anapolis-go/pecas-e-assistencia-empilhadeira/"
)

for url in "${urls[@]}"; do
  echo "Testing: $url"
  # Rich Results Test API (nota: precisa autenticação OAuth)
  # curl "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run" \
  #   -H "Content-Type: application/json" \
  #   -H "Authorization: Bearer $TOKEN" \
  #   -d "{\"url\":\"$url\"}"
done
```

---

## Rollout Phases (Pós-Validação)

### Fase A: Monitoramento (D+1 a D+3)
- [ ] Validação manual de 10 URLs
- [ ] GSC sitemap submission
- [ ] Monitorar erros iniciais

### Fase B: Observação (D+3 a D+7)
- [ ] Acompanhar impressões de rich results
- [ ] Validar featured snippet lift
- [ ] Confirmar video SERP appearances

### Fase C: Análise (D+7 a D+14)
- [ ] Calcular CTR improvement
- [ ] Avaliar E-E-A-T impact no ranking
- [ ] Documentar resultados finais

### Fase D: Documentação (D+14+)
- [ ] Criar relatório final de impacto
- [ ] Arquivo: `RESULTADO-FINAL-SCHEMA-PHASE-1-2.md`
- [ ] Arquivar scripts e logs

---

## Recomendações Imediatas

### DO (Fazer)
- ✅ Testar URLs com Rich Results Test hoje
- ✅ Submeter sitemap no GSC amanhã
- ✅ Guardar screenshots de baseline (impressões/CTR antes)
- ✅ Manter logs de erros encontrados
- ✅ Priorizar erros de `<script>` ou JSON parsing

### DON'T (Não Fazer)
- ❌ Não editar arquivos HTML sem rodar scripts
- ❌ Não remover nós criados (idempotent design protege erros)
- ❌ Não desabilitar Google bots (precisam rastrear)
- ❌ Não fazer mudanças no schema até D+7 (deixar Google processar)

---

## Contato / Escalação

**Se encontrar erros críticos:**
1. Documentar erro exato (screenshot)
2. Testar em 3+ URLs (confirmar pattern)
3. Executar: `python3 schema-fix-phase2-elite-nodes.py --city=CIDADE --service=TIPO`
4. Re-testar no Rich Results Test

**Se erro persistir:**
- Revisar regra em `/Users/jrios/.claude/skills/schema-markup.md`
- Abrir issue em GitHub com screenshot + URL

---

## Próximo Passo (Este Checklist)

Após completar validação de 10 URLs, marcar como completo:

- [ ] 10/10 URLs testadas no Rich Results Test
- [ ] 0 erros críticos encontrados (ou corrigidos)
- [ ] Sitemap submetido no GSC
- [ ] Baseline de impressões registrada

**Status:** Aguardando execução manual no Rich Results Test

---

**Prepared by:** Claude Code  
**Date:** 2026-04-22 15:05 BRT  
**Próximo Review:** 2026-04-23 (Rich Results Test results)
