# P0 Corrections — Clark PDPs (Move Máquinas)

## Contexto
Auditoria SCP (score 0-10, gate ≥8.0) identificou 9 PDPs com GAPS CRÍTICOS (score <8.0).
Todas as 9 foram corrigidas com o mesmo padrão de 3 fixes P0.

## Padrão P0 aplicado em todas as páginas
1. **Autoridade Move Máquinas** — upgradar menções genéricas para incluir "mais de 20 anos" e/ou "+500 clientes industriais no Centro-Oeste"
2. **Inline CTAs mid-page** — 2 CTAs por página, contextuais, ancorados em `href="#proposta"` ou `href="#formulario-proposta"`
3. **Seção ROI/TCO** — inserida antes do FAQ, com tabela de custos comparativos e R$ reais específicos do produto
4. **Form ID** — `id="formulario-proposta"` adicionado ao `<form>` do CTA final

## CKB Move Máquinas (dados usados nos textos)
- CNPJ: 32.428.258/0001-80
- Localização: Goiânia-GO, atende Centro-Oeste
- Experiência: mais de 20 anos
- Clientes: mais de 500 clientes industriais
- Posição Clark: revendedor/distribuidor autorizado Clark Centro-Oeste
- Prazo de proposta: 1 dia útil

## Páginas corrigidas

### clark-c60-c80 — score 6.75 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-c60-c80/pdp-content-v1.html`
Produto: Empilhadeira combustão Clark C60/C70/C75/C80 (6-8t), motor Cummins 67kW, freio disco 10.000h
ROI inserido: economia de freio disco R$17.500-60.000 em 10.000h vs freio a tambor, payback 24-36 meses

### clark-s40-s60 — score 6.75 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-s40-s60/pdp-content-v1.html`
Produto: Empilhadeira combustão Clark S40/S45/S50s/S55s/S60 (4-6t), motor Kubota V3800, CSS stability system
ROI inserido: freio R$12.500-40.000 economia, tombamento R$80-150k custo evitado com CSS

### clark-osx15 — score 7.25 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-osx15/pdp-content-v1.html`
Produto: Stacker Over/Under Clark OSX15 (1.500kg), rack duplo double-deep
ROI inserido: comparativo aluguel galpão adicional vs compra OSX15 (já existia, foi upgradeado com autoridade)

### clark-c20s — score 7.50 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-c20s/pdp-content-v1.html`
Produto: Empilhadeira combustão Clark C20s (2t), GLP/gasolina, operação mista interno/externo
ROI inserido: terceirização R$180-350/hora, parada doca R$3.000-8.000/turno, comparativo 5 anos

### clark-wpio15 — score 7.50 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-wpio15/pdp-content-v1.html`
Produto: Paleteira elétrica Clark WPio15 (1.500kg), Li-Ion 24V, recarga 2,5h
ROI inserido: payback Li-Ion vs lead-ácido, simulação personalizada pela Move Máquinas

### clark-npx — score 7.75 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-npx/pdp-content-v1.html`
Produto: Order picker elétrico Clark NPX (1.000kg), plataforma elevável até 5.000mm, Li-Ion 24V
ROI inserido: erro de separação R$200-800/ocorrência, R$22k-88k/mês com 5 erros/dia, redução 70% com picking no nível

### clark-lwio15 — score 7.75 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-lwio15/pdp-content-v1.html`
Produto: Paleteira elétrica light duty Clark LWio15 (1.500kg), Li-Ion 24V 20Ah
ROI inserido: 82h/mês economizadas (15min/viagem x 15 viagens x 22 dias), R$1.640/mês a R$20/h operador

### clark-s-xe — score 7.75 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-s-xe/pdp-content-v1.html`
Produto: Empilhadeira elétrica Clark S-XE Renegade (S25XE/S30XE/S35XE), 80V LFP, pneu superelástico, 27% gradeabilidade
ROI inserido: GLP R$800-1.600/mês eliminado, manutenção motor combustão R$1.200-2.400/ano, economia 36m = R$61k-122k

### clark-psx16 — score 7.75 → ≥8.0
Arquivo: `/Users/jrios/move-maquinas-seo/venda-de-maquinas-clark/clark-psx16/pdp-content-v1.html`
Produto: Stacker elétrico walkie Clark PSX16 (1.600kg), elevação até 5.500mm, carga de oportunidade 24/7
ROI inserido: bateria reserva lead-ácido R$4k-8k evitada, manutenção mensal R$150-300 eliminada, economia 4 anos R$20k-40k

## Observações
- WhatsApp `https://wa.me/556299999999` permanece como placeholder em todas as páginas (não é P0)
- Todos os CTAs inline apontam para `#proposta` ou `#formulario-proposta` (âncora do form no rodapé da página)
- Nenhuma seção de conteúdo existente foi removida ou reescrita — apenas adições
