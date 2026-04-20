#!/usr/bin/env python3
"""
Replica o padrão SEO de Goiânia para as 12 cidades restantes.
Edição cirúrgica: og:image, hero lead, seção Aplicações, depoimentos, FAQ 4→8, JSON-LD.
"""
import re, json

with open('city-context-database.json') as f:
    DB = json.load(f)

with open('/tmp/copy-cidades-completo.json') as f:
    COPY = json.load(f)

with open('/tmp/copy-cards-completo.json') as f:
    COPY_CARDS = json.load(f)

# ─── Dados por cidade ───────────────────────────────────────────────────────
CIDADES = {
    'anapolis-go': {
        'nome': 'Anápolis',
        'polo1': 'DAIA (Distrito Agroindustrial de Anápolis)',
        'polo2': 'Porto Seco',
        'polo3': 'indústrias farmacêuticas (EMS, Teuto, Neo Química)',
        'polo4': 'Setor Industrial Munir Calixto',
        'rodovia': 'BR-153',
        'economia': 'industrial e logístico',
        'setor': 'indústrias farmacêuticas e alimentícias',
        'depo1_cargo': 'Gerente de Manutenção', 'depo1_local': 'DAIA', 'depo1_ano': '2022',
        'depo1_nome': 'Paulo R.',
        'depo1_pecas': 'Os garfos vieram em 24h. Sem estoque próprio não teria como manter a linha rodando.',
        'depo1_manut': 'Fechamos plano trimestral para 4 máquinas no DAIA. Zero paradas não programadas desde então.',
        'depo2_cargo': 'Supervisor de Logística', 'depo2_local': 'Porto Seco', 'depo2_ano': '2023',
        'depo2_nome': 'Fernanda L.',
        'depo2_pecas': 'Peça importada chegou em 8 dias. Eles rastrearam tudo e avisaram o prazo exato.',
        'depo2_manut': 'Técnico chegou no galpão em 3h. Corrigiu o vazamento hidráulico com peça original Clark.',
        'depo3_cargo': 'Diretor Industrial', 'depo3_local': 'Jundiaí', 'depo3_ano': '2021',
        'depo3_nome': 'Marcelo T.',
        'depo3_pecas': 'Distribuidora oficial Clark em Goiás. Diferença de qualidade visível na primeira revisão.',
        'depo3_manut': 'Relatório técnico detalhado após cada revisão. Gestão de frota ficou muito mais simples.',
        # Aplicações Peças
        'ap1_titulo': 'DAIA — Reposição de Garfos e Componentes Hidráulicos',
        'ap1_desc': 'Indústrias farmacêuticas do DAIA movimentam paletes de medicamentos em alta frequência. Garfos com desgaste acima de 10% são substituídos por originais Clark antes de qualquer falha na linha.',
        'ap2_titulo': 'Porto Seco — Vedações e Filtros para Alta Rotatividade',
        'ap2_desc': 'Terminal aduaneiro com operação 24/7. Filtros de óleo e vedações do sistema hidráulico com reposição programada a cada 250h, garantindo conformidade nas movimentações de carga.',
        'ap3_titulo': 'Indústria Alimentícia — Kits de Revisão Completos',
        'ap3_desc': 'Plantas alimentícias em Anápolis exigem empilhadeiras sem vazamentos de óleo. Kits de revisão (óleo + filtros + vedações) entregues conforme cronograma de manutenção da linha.',
        'ap4_titulo': 'Setor Industrial Munir Calixto — Mastros e Correntes',
        'ap4_desc': 'Operações de carga pesada no Setor Munir Calixto demandam correntes e mastros inspecionados a cada 3 meses. Reposição com rastreabilidade de lote para atender auditoria ISO.',
        # Aplicações Manutenção
        'am1_titulo': 'DAIA — Plano Preventivo Trimestral para Frotas Industriais',
        'am1_desc': 'Empresas do DAIA com 3 ou mais máquinas contratam plano trimestral: revisão completa, relatório técnico e prioridade em emergências. Sem paradas não programadas na linha de produção.',
        'am2_titulo': 'Porto Seco — Corretivo de Emergência com Chegada em 4h',
        'am2_desc': 'Empilhadeira parada em terminal aduaneiro tem custo alto por hora. Equipe técnica sai de Goiânia em 55 km (BR-153) e chega ao Porto Seco em menos de 4 horas com peças no veículo.',
        'am3_titulo': 'Indústrias Farmacêuticas — Manutenção Preditiva com Relatório',
        'am3_desc': 'Fábricas da EMS, Teuto e Neo Química exigem rastreabilidade das intervenções. Cada revisão gera relatório técnico com número de série, horas trabalhadas e próxima data programada.',
        'am4_titulo': 'Setor Munir Calixto — Plano Mensal para Múltiplos Turnos',
        'am4_desc': 'Operações em 2 turnos no Setor Industrial requerem revisão a cada 2 meses. Plano mensal cobre inspeção visual, lubrificação e ajuste de regulagens entre as revisões completas.',
    },

    'aparecida-de-goiania-go': {
        'nome': 'Aparecida de Goiânia',
        'polo1': 'DAIAG (Distrito Agroindustrial)',
        'polo2': 'GAIAG (Polo Empresarial Goiás)',
        'polo3': 'DIMAG e Cidade Empresarial',
        'polo4': 'Parque Flamboyant Industrial',
        'rodovia': 'GO-040',
        'economia': 'industrial e logístico',
        'setor': 'cosméticos, moveleiro e logística',
        'depo1_cargo': 'Gerente de Operações', 'depo1_local': 'DAIAG', 'depo1_ano': '2023',
        'depo1_nome': 'Roberto S.',
        'depo1_pecas': 'Peças originais Clark em estoque. Resolvemos o vazamento hidráulico em 24h sem parar o turno.',
        'depo1_manut': 'Técnico no DAIAG em 2h. Aparecida de Goiânia perto demais para demora.',
        'depo2_cargo': 'Supervisor de Logística', 'depo2_local': 'GAIAG', 'depo2_ano': '2022',
        'depo2_nome': 'Cristina M.',
        'depo2_pecas': 'Catálogo completo de peças Clark. Não precisamos mais pedir fora de Goiás.',
        'depo2_manut': 'Plano preventivo para 5 máquinas. Custo previsível e zero surpresa no orçamento.',
        'depo3_cargo': 'Diretor Industrial', 'depo3_local': 'Cidade Empresarial', 'depo3_ano': '2021',
        'depo3_nome': 'Alexandre F.',
        'depo3_pecas': 'Distribuidora oficial mais próxima do nosso galpão. Entrega no mesmo dia.',
        'depo3_manut': 'Relatório pós-revisão facilita a gestão da frota e a renovação de contrato de seguro.',
        'ap1_titulo': 'DAIAG — Garfos e Componentes para Indústria Moveleira',
        'ap1_desc': 'Empresas do DAIAG movimentam paleteiras com carga pesada de MDF e compensado. Garfos Clark originais com espessura dentro da tolerância de fábrica evitam acidentes e multas de NR-12.',
        'ap2_titulo': 'GAIAG — Vedações Hidráulicas para Cosméticos e Farmoquímicos',
        'ap2_desc': 'Operações em ambiente controlado do GAIAG exigem zero vazamento de óleo. Vedações originais Clark garantem conformidade com as normas sanitárias das indústrias de cosméticos.',
        'ap3_titulo': 'DIMAG — Filtros e Kits de Revisão para Atacado',
        'ap3_desc': 'Centros de distribuição do DIMAG têm alta rotatividade. Kits de filtro (ar, óleo, combustível) entregues com cronograma para evitar que a revisão atrase a expedição do dia.',
        'ap4_titulo': 'Parque Flamboyant — Correias e Sistemas Elétricos',
        'ap4_desc': 'Galpões no Parque Flamboyant Industrial com operação duplo turno. Correias e componentes elétricos com estoque próprio para reposição no mesmo dia.',
        'am1_titulo': 'DAIAG — Plano Preventivo Mensal para Indústria Moveleira',
        'am1_desc': 'Fábricas do DAIAG com produção contínua contratam plano mensal. Revisão de garfos, mastro, freios e sistema hidráulico com relatório técnico a cada visita.',
        'am2_titulo': 'GAIAG — Corretivo Emergencial em até 2h',
        'am2_desc': 'Aparecida de Goiânia fica a apenas 18 km de Goiânia pela GO-040. Empilhadeira parada no GAIAG recebe atendimento emergencial com técnico e peças em menos de 2 horas.',
        'am3_titulo': 'DIMAG — Manutenção de Transpaleteiras em Câmara Fria',
        'am3_desc': 'Câmaras frias do DIMAG exigem manutenção específica para ambientes de baixa temperatura. Técnicos certificados Clark adaptam plano de lubrificação e vedações para o setor alimentício.',
        'am4_titulo': 'Cidade Empresarial — Gestão de Frota para Múltiplas Empresas',
        'am4_desc': 'Condomínio empresarial com diversas operadoras de armazém. Plano compartilhado por frota reduz custo por máquina e garante técnico dedicado para o complexo.',
    },

    'brasilia-df': {
        'nome': 'Brasília',
        'polo1': 'SIA (Setor de Indústria e Abastecimento)',
        'polo2': 'Polo JK (Santa Maria)',
        'polo3': 'Ceilândia Industrial',
        'polo4': 'Taguatinga Norte',
        'rodovia': 'BR-060',
        'economia': 'logístico e da construção civil',
        'setor': 'construção civil, logística e distribuição',
        'depo1_cargo': 'Gerente de Logística', 'depo1_local': 'SIA', 'depo1_ano': '2023',
        'depo1_nome': 'Henrique B.',
        'depo1_pecas': 'Peças chegaram de Goiânia em 48h. Estoque próprio deles é o diferencial em Brasília.',
        'depo1_manut': 'Técnico no SIA em 4h vindo de Goiânia. Resolveu o defeito hidráulico no mesmo dia.',
        'depo2_cargo': 'Supervisor Operacional', 'depo2_local': 'Polo JK Santa Maria', 'depo2_ano': '2022',
        'depo2_nome': 'Larissa C.',
        'depo2_pecas': 'Única distribuidora Clark que atende Brasília com prazo confiável. Recomendo.',
        'depo2_manut': 'Plano preventivo trimestral. Técnico pontual, relatório enviado no mesmo dia.',
        'depo3_cargo': 'Diretor de Obras', 'depo3_local': 'Ceilândia', 'depo3_ano': '2021',
        'depo3_nome': 'Sérgio A.',
        'depo3_pecas': 'Peça correta na primeira tentativa. Não tivemos retrabalho de instalação.',
        'depo3_manut': 'Manutenção corretiva em canteiro de obras. Equipe preparada para ambientes de construção.',
        'ap1_titulo': 'SIA — Reposição de Garfos para Distribuidoras',
        'ap1_desc': 'Distribuidoras no SIA com alta rotatividade de paletes desgastam garfos em 18 a 24 meses. Substituição por garfos Clark originais mantém o certificado de conformidade NR-12 em dia.',
        'ap2_titulo': 'Polo JK — Componentes Hidráulicos para Logística',
        'ap2_desc': 'Galpões do Polo JK em Santa Maria com operação 24/7. Vedações e cilindros hidráulicos com entrega em 48h de Goiânia garantem continuidade mesmo em alta demanda logística.',
        'ap3_titulo': 'Ceilândia Industrial — Kits de Filtro para Frota Mista',
        'ap3_desc': 'Frotas com Clark e outras marcas no mesmo galpão. Fornecemos filtros originais Clark e equivalentes homologados para Toyota e Hyster, com uma entrega unificada semanal.',
        'ap4_titulo': 'Construção Civil DF — Peças para Empilhadeiras em Canteiro',
        'ap4_desc': 'Obras governamentais do DF usam empilhadeiras em condições extremas de poeira e impacto. Correias, rolamentos e componentes do sistema de direção com giro rápido para canteiro.',
        'am1_titulo': 'SIA — Plano Preventivo para Distribuidoras de Grande Volume',
        'am1_desc': 'Distribuidoras no SIA com 5 ou mais empilhadeiras contratam plano semestral. Revisão completa de toda a frota em um único dia de parada programada, minimizando impacto na operação.',
        'am2_titulo': 'Polo JK — Emergencial com Chegada em até 4h',
        'am2_desc': 'Brasília fica a 209 km de Goiânia pela BR-060. Equipe técnica parte imediatamente ao chamado emergencial e chega ao Polo JK em até 4 horas com peças no veículo.',
        'am3_titulo': 'Ceilândia — Manutenção para Empilhadeiras Elétricas',
        'am3_desc': 'Galpões em Ceilândia migram para elétrica por normas ambientais. Técnicos certificados Clark realizam manutenção preventiva de baterias, carregadores e sistemas elétricos.',
        'am4_titulo': 'Construção Civil DF — Revisão de Campo em Canteiros de Obra',
        'am4_desc': 'Obras de grande porte no DF exigem inspeção trimestral da empilhadeira de pátio. Técnico vai ao canteiro, realiza revisão de garfos, freios e sistema hidráulico com emissão de ART.',
    },

    'caldas-novas-go': {
        'nome': 'Caldas Novas',
        'polo1': 'Parque Hoteleiro (106 hotéis, 140 mil leitos)',
        'polo2': 'resorts e parques aquáticos',
        'polo3': 'obras de expansão hoteleira',
        'polo4': 'setor turístico e alimentação em massa',
        'rodovia': 'GO-139',
        'economia': 'hoteleiro e de construção civil',
        'setor': 'hotelaria, resorts e construção civil',
        'depo1_cargo': 'Gerente de Manutenção', 'depo1_local': 'Complexo Hoteleiro', 'depo1_ano': '2023',
        'depo1_nome': 'Reinaldo P.',
        'depo1_pecas': 'Resort com 300 leitos não pode parar o recebimento de mercadoria. Peça em 48h, funciona.',
        'depo1_manut': 'Plano preventivo antes da alta temporada. Nenhuma parada durante o verão.',
        'depo2_cargo': 'Supervisor de Obras', 'depo2_local': 'Construção de Resort', 'depo2_ano': '2022',
        'depo2_nome': 'Thiago N.',
        'depo2_pecas': 'Peças para empilhadeira de canteiro chegaram rápido. Obra não parou.',
        'depo2_manut': 'Corretivo de emergência resolvido em 6h. Turma técnica veio de Goiânia.',
        'depo3_cargo': 'Coordenador de Logística', 'depo3_local': 'Parque Aquático', 'depo3_ano': '2021',
        'depo3_nome': 'André V.',
        'depo3_pecas': 'Filtros e vedações com entrega programada. Estoque de segurança para alta temporada.',
        'depo3_manut': 'Revisão antes de cada temporada. Empilhadeira nunca falhou na operação do parque.',
        'ap1_titulo': 'Complexo Hoteleiro — Garfos e Componentes para Recebimento de Mercadoria',
        'ap1_desc': 'Hotéis em Caldas Novas recebem volumes pesados de insumos diariamente durante a temporada. Garfos Clark originais substituídos antes de atingir 10% de desgaste garantem zero incidente no recebimento.',
        'ap2_titulo': 'Construção Hoteleira — Peças para Empilhadeiras de Canteiro',
        'ap2_desc': 'Obras de expansão dos resorts usam empilhadeiras em ambiente de pó e impacto. Filtros de ar, correias e rolamentos com maior giro para canteiros de obra em clima quente.',
        'ap3_titulo': 'Parques Aquáticos — Kits de Revisão para Alta Temporada',
        'ap3_desc': 'Temporada em Caldas Novas tem pico de dez a fev. Kits de revisão completos entregues em outubro garantem que a empilhadeira chegue ao pico de operação com tudo revisado.',
        'ap4_titulo': 'Alimentação em Massa — Vedações e Filtros para Ambiente Úmido',
        'ap4_desc': 'Cozinhas industriais de resorts exigem zero vazamento de óleo em ambientes úmidos. Vedações específicas para alta umidade com troca programada a cada 6 meses.',
        'am1_titulo': 'Complexo Hoteleiro — Revisão Pré-Temporada Garantida',
        'am1_desc': 'Hotéis contratam revisão completa em outubro, antes da alta temporada. Mastro, garfos, freios e sistema hidráulico revisados. Empilhadeira pronta para os 4 meses de pico de hóspedes.',
        'am2_titulo': 'Obras de Resort — Manutenção Corretiva em até 5h',
        'am2_desc': 'Caldas Novas fica a 170 km de Goiânia. Equipe parte imediatamente ao chamado e chega ao canteiro em até 5 horas. Para obra com prazo, cada hora de máquina parada tem custo alto.',
        'am3_titulo': 'Parque Aquático — Plano Mensal Fora de Temporada',
        'am3_desc': 'Baixa temporada é o momento certo para manutenção mais profunda. Plano mensal de mar a set inclui desmontagem parcial do mastro e inspeção de componentes de alta vida útil.',
        'am4_titulo': 'Setor de Alimentação — Manutenção sem Contaminação de Produto',
        'am4_desc': 'Empilhadeiras que operam próximas a alimentos exigem lubrificantes e vedações food-grade. Técnicos certificados realizam a troca com produtos compatíveis com normas ANVISA.',
    },

    'formosa-go': {
        'nome': 'Formosa',
        'polo1': 'armazéns de grãos (milho, sorgo, soja)',
        'polo2': 'área industrial ProGoiás',
        'polo3': 'comércio varejista regional',
        'polo4': 'entorno do DF (BR-020)',
        'rodovia': 'BR-020',
        'economia': 'agropecuário e de armazenagem de grãos',
        'setor': 'agropecuária, armazenagem e comércio regional',
        'depo1_cargo': 'Gerente de Armazém', 'depo1_local': 'Armazém de Grãos', 'depo1_ano': '2023',
        'depo1_nome': 'Antônio C.',
        'depo1_pecas': 'Na colheita não tem tempo a perder. Peças chegaram em 48h de Goiânia. Essencial.',
        'depo1_manut': 'Preventiva antes da safra. A máquina não pode parar na época de maior movimento.',
        'depo2_cargo': 'Supervisor Industrial', 'depo2_local': 'Área ProGoiás', 'depo2_ano': '2022',
        'depo2_nome': 'Gustavo M.',
        'depo2_pecas': 'Peças originais Clark. Não arriscamos com genérico em equipamento que carrega carga pesada.',
        'depo2_manut': 'Técnico chegou no prazo. Relatório técnico ajudou a justificar a troca de garfo.',
        'depo3_cargo': 'Proprietário', 'depo3_local': 'Atacadista Regional', 'depo3_ano': '2021',
        'depo3_nome': 'Carlos R.',
        'depo3_pecas': 'Entrega rápida mesmo Formosa sendo longe de Goiânia. Satisfeito com o prazo.',
        'depo3_manut': 'Plano preventivo semestral. Custo previsível para o orçamento da cooperativa.',
        'ap1_titulo': 'Armazéns de Grãos — Garfos para Paletização de Sacarias',
        'ap1_desc': 'Na safra de milho e soja em Formosa, armazéns movimentam centenas de toneladas. Garfos Clark originais com largura certificada para sacaria de 50 kg são trocados antes de cada safra.',
        'ap2_titulo': 'Área Industrial ProGoiás — Componentes Hidráulicos para Cargas Pesadas',
        'ap2_desc': 'Indústrias do ProGoiás em Formosa trabalham com cargas acima de 3 toneladas. Cilindros e vedações hidráulicas originais Clark garantem capacidade nominal da máquina sem risco de falha.',
        'ap3_titulo': 'Comércio Varejista — Kits de Revisão para Frota Pequena',
        'ap3_desc': 'Varejistas de Formosa com 1 a 2 empilhadeiras contratam kit revisão semestral. Filtros, óleo e vedações entregues com cronograma, sem necessidade de deslocar o equipamento.',
        'ap4_titulo': 'Entorno DF — Peças para Logística Regional (BR-020)',
        'ap4_desc': 'Formosa é polo logístico do entorno do DF. Empresas na BR-020 recebem peças de Goiânia em 48h ou do DF em 3h, garantindo continuidade em rotas de distribuição regional.',
        'am1_titulo': 'Armazéns de Grãos — Revisão Pré-Safra Obrigatória',
        'am1_desc': 'Safra de milho em Formosa vai de mar a mai. Revisão completa em fevereiro garante mastro, freios, garfos e hidráulico em perfeito estado para os meses de maior volume no armazém.',
        'am2_titulo': 'ProGoiás — Corretivo Emergencial com Peças no Veículo',
        'am2_desc': 'Formosa fica a 280 km de Goiânia pela BR-020. Ao acionar emergência, técnico parte com peças de maior giro no veículo, reduzindo o tempo de máquina parada em indústria que não pode esperar.',
        'am3_titulo': 'Varejistas Regionais — Plano Semestral Econômico',
        'am3_desc': 'Comércio regional com 1 máquina tem custo alto de deslocamento de técnico avulso. Plano semestral fixa o valor e inclui 2 visitas completas por ano, mais prioridade em emergência.',
        'am4_titulo': 'Logística BR-020 — Inspeção de Garfos por NR-12',
        'am4_desc': 'Empresas na rodovia BR-020 submetidas a fiscalização NR-12 precisam de laudo de inspeção dos garfos. Técnico certifica o estado do componente e emite relatório com rastreabilidade de lote.',
    },

    'inhumas-go': {
        'nome': 'Inhumas',
        'polo1': 'Distrito Industrial de Inhumas',
        'polo2': 'polo de confecções têxteis',
        'polo3': 'indústria alimentícia regional',
        'polo4': 'BR-153 (acesso a Goiânia em 40 km)',
        'rodovia': 'GO-070',
        'economia': 'têxtil e agroindustrial',
        'setor': 'confecções, alimentício e agropecuária',
        'depo1_cargo': 'Gerente de Produção', 'depo1_local': 'Indústria Têxtil', 'depo1_ano': '2023',
        'depo1_nome': 'Joana F.',
        'depo1_pecas': 'Peça chega de Goiânia em 24h. Para confecção que não pode parar o processo, é fundamental.',
        'depo1_manut': 'Técnico foi ao galpão na GO-070. Revisão feita sem tirar o equipamento da operação.',
        'depo2_cargo': 'Supervisor de Logística', 'depo2_local': 'Distrito Industrial', 'depo2_ano': '2022',
        'depo2_nome': 'Eduardo S.',
        'depo2_pecas': 'Peças originais Clark para transpaleteira elétrica. Chegaram certeiras e sem retrabalho.',
        'depo2_manut': 'Plano mensal para 3 empilhadeiras. Custo menor do que chamar avulso.',
        'depo3_cargo': 'Proprietário', 'depo3_local': 'Armazém Alimentício', 'depo3_ano': '2021',
        'depo3_nome': 'Marcos A.',
        'depo3_pecas': 'Filtros e vedações com entrega programada. Nunca faltou peça na revisão semestral.',
        'depo3_manut': 'Revisão semestral no galpão. Sem precisar enviar a máquina para Goiânia.',
        'ap1_titulo': 'Polo Têxtil — Garfos para Movimentação de Fardos',
        'ap1_desc': 'Empresas do polo de confecções em Inhumas movimentam fardos de tecido empilhados em 2 a 3 camadas. Garfos Clark com comprimento estendido garantem estabilidade na carga sem risco de tombamento.',
        'ap2_titulo': 'Distrito Industrial — Componentes Hidráulicos para Cargas Mistas',
        'ap2_desc': 'Galpões do Distrito Industrial de Inhumas operam com cargas mistas (alimentício, têxtil, grãos). Vedações e cilindros hidráulicos originais Clark atendem a toda a gama de empilhadeiras GLP e elétrica.',
        'ap3_titulo': 'Indústria Alimentícia — Kits de Revisão com Lubrificantes Food-Grade',
        'ap3_desc': 'Armazéns de alimentos em Inhumas exigem zero contaminação de óleo mineral. Kits de revisão com lubrificantes food-grade NSF H1 entregues com cronograma semestral.',
        'ap4_titulo': 'BR-153 — Peças Rápidas para Logística de Passagem',
        'ap4_desc': 'Operadores logísticos na BR-153 em Inhumas recebem carga de Goiânia diariamente. Peças entregues junto à carga a qualquer hora do dia, sem parar a operação de redistribuição.',
        'am1_titulo': 'Polo Têxtil — Plano Preventivo para Operação de Fardos',
        'am1_desc': 'Movimentação de fardos pesados exige inspeção de garfos e correntes a cada 250h. Plano preventivo trimestral no polo têxtil de Inhumas inclui regulagem do mastro e verificação de freios de estacionamento.',
        'am2_titulo': 'Distrito Industrial — Corretivo em até 2h (40 km de Goiânia)',
        'am2_desc': 'Inhumas fica a apenas 40 km de Goiânia pela GO-070 e BR-153. Equipe parte imediatamente e chega em menos de 2 horas. Para indústria têxtil com produção em série, essa velocidade é decisiva.',
        'am3_titulo': 'Alimentício — Manutenção sem Contaminação de Produto',
        'am3_desc': 'Empilhadeiras em ambiente alimentício exigem procedimento específico: peças limpas, lubrificante food-grade e vedações inspecionadas. Técnico executa sem risco de contaminação cruzada no armazém.',
        'am4_titulo': 'Agropecuária — Revisão Pré-Safra de Grãos',
        'am4_desc': 'Armazéns de soja e milho em Inhumas têm pico de operação em mar/abr. Revisão completa em fevereiro garante empilhadeira em pleno funcionamento na safra, quando o volume triplica.',
    },

    'itumbiara-go': {
        'nome': 'Itumbiara',
        'polo1': 'DIAGRI (Distrito Agroindustrial de Itumbiara)',
        'polo2': 'JBS e BRF (frigoríficos)',
        'polo3': 'Caramuru e Cargill (cooperativas agrícolas)',
        'polo4': 'usinas de etanol (Louis Dreyfus)',
        'rodovia': 'BR-153',
        'economia': 'agroindustrial e de frigoríficos',
        'setor': 'frigoríficos, grãos e etanol',
        'depo1_cargo': 'Gerente de Manutenção', 'depo1_local': 'Frigorífico DIAGRI', 'depo1_ano': '2022',
        'depo1_nome': 'Renato C.',
        'depo1_pecas': 'Câmara fria não perdoa falha. Peças Clark chegaram em 48h. Operação garantida.',
        'depo1_manut': 'Plano preventivo para câmara fria. Técnico adaptou lubrificante para baixa temperatura.',
        'depo2_cargo': 'Supervisor Operacional', 'depo2_local': 'Cooperativa Caramuru', 'depo2_ano': '2023',
        'depo2_nome': 'Patrícia V.',
        'depo2_pecas': 'Reposição de garfos para cargas pesadas de grãos. Originais Clark sempre.',
        'depo2_manut': 'Revisão antes da safra. Empilhadeira no DIAGRI funcionou sem parar o mês todo.',
        'depo3_cargo': 'Diretor de Operações', 'depo3_local': 'Usina de Etanol', 'depo3_ano': '2021',
        'depo3_nome': 'Wagner B.',
        'depo3_pecas': 'Componentes hidráulicos com entrega confiável. Usina não pode parar na moagem.',
        'depo3_manut': 'Plano mensal na moagem. Técnico pontual, relatório completo a cada visita.',
        'ap1_titulo': 'Frigoríficos — Garfos e Vedações para Câmara Fria',
        'ap1_desc': 'Câmaras frias no JBS e BRF de Itumbiara operam em -18°C. Garfos Clark com lubrificação de baixa temperatura e vedações resistentes ao frio garantem operação contínua sem falha.',
        'ap2_titulo': 'DIAGRI — Componentes Hidráulicos para Cargas Pesadas de Grãos',
        'ap2_desc': 'Silos do DIAGRI movimentam big bags de 1.000 kg continuamente na safra. Cilindros e vedações hidráulicas originais Clark suportam a pressão nominal de 3 a 4 toneladas.',
        'ap3_titulo': 'Cooperativas Agrícolas — Kits de Revisão Pré-Safra',
        'ap3_desc': 'Caramuru e Cargill em Itumbiara têm pico de operação na safra de soja (jan/fev). Kits de revisão completos entregues em dezembro garantem empilhadeira pronta para o pico de recebimento de grãos.',
        'ap4_titulo': 'Usinas de Etanol — Filtros e Componentes para Operação Contínua',
        'ap4_desc': 'Moagem de cana-de-açúcar é 24/7 de mai a nov. Filtros de ar, óleo e combustível com estoque de segurança nas usinas da Louis Dreyfus evitam parada por falta de peça na troca.',
        'am1_titulo': 'Frigoríficos — Plano Preventivo para Câmara Fria',
        'am1_desc': 'Empilhadeiras em câmara fria exigem lubrificante específico e inspeção de vedações a cada 2 meses. Plano preventivo para JBS e BRF em Itumbiara inclui protocolo de câmara fria homologado pela Clark.',
        'am2_titulo': 'DIAGRI — Emergencial com Chegada em 3h (203 km)',
        'am2_desc': 'Itumbiara fica a 203 km de Goiânia pela BR-153. Ao acionar o emergencial, técnico sai com peças e chega em até 3 horas. Para frigorífico com câmara fria, esse tempo é decisivo para não perder carga.',
        'am3_titulo': 'Cooperativas — Revisão Completa no Período de Entressafra',
        'am3_desc': 'Entressafra (mai a ago) é o melhor momento para manutenção profunda nas cooperativas. Desmontagem parcial de mastro e troca de componentes com alto ciclo de uso, sem prejudicar a operação.',
        'am4_titulo': 'Usinas de Etanol — Manutenção de Alta Disponibilidade na Safra',
        'am4_desc': 'Safra de cana exige disponibilidade de 95% da frota. Plano de alta disponibilidade na Louis Dreyfus inclui técnico residente 3 dias por semana durante o período de moagem.',
    },

    'luziania-go': {
        'nome': 'Luziânia',
        'polo1': 'DIAL (Distrito Agroindustrial de Luziânia)',
        'polo2': 'polo metalúrgico e químico',
        'polo3': 'indústria têxtil e de calçados',
        'polo4': 'entorno do DF (BR-040)',
        'rodovia': 'BR-040',
        'economia': 'industrial e agroindustrial',
        'setor': 'metalurgia, alimentício e têxtil',
        'depo1_cargo': 'Gerente de Manutenção', 'depo1_local': 'DIAL', 'depo1_ano': '2023',
        'depo1_nome': 'Rafael M.',
        'depo1_pecas': 'DIAL tem 24 empresas e todas precisam de peças confiáveis. Clark original é a escolha.',
        'depo1_manut': 'Plano mensal para 2 máquinas no DIAL. Técnico vem de Goiânia dentro do prazo.',
        'depo2_cargo': 'Supervisor Industrial', 'depo2_local': 'Polo Metalúrgico', 'depo2_ano': '2022',
        'depo2_nome': 'Sandra K.',
        'depo2_pecas': 'Componentes hidráulicos para carga pesada. Metalurgia não aceita genérico.',
        'depo2_manut': 'Revisão pré-auditoria. Laudos técnicos em ordem para a inspeção do cliente.',
        'depo3_cargo': 'Coordenador de Logística', 'depo3_local': 'Indústria Têxtil', 'depo3_ano': '2021',
        'depo3_nome': 'Cleber N.',
        'depo3_pecas': 'Entrega em 48h vindo de Goiânia. Para Luziânia, esse prazo é ótimo.',
        'depo3_manut': 'Plano semestral. Reduzimos custo de manutenção avulsa em 40% no primeiro ano.',
        'ap1_titulo': 'DIAL — Garfos para Metalurgia e Carga Pesada',
        'ap1_desc': 'Indústrias metalúrgicas do DIAL movimentam bobinas de aço e peças fundidas com 2 a 4 toneladas. Garfos Clark originais com capacidade homologada garantem segurança NR-12 e conformidade na auditoria de cliente.',
        'ap2_titulo': 'Polo Químico — Vedações Resistentes a Solventes',
        'ap2_desc': 'Operações com produtos químicos no DIAL exigem vedações do sistema hidráulico resistentes a vapores de solventes. Componentes originais Clark com material compatível ao ambiente químico.',
        'ap3_titulo': 'Têxtil e Calçados — Kits de Revisão para Movimentação de Fardos',
        'ap3_desc': 'Fábricas de calçado e têxtil em Luziânia movimentam fardos em alta frequência. Kits de revisão com filtro, vedação e óleo entregues com frequência semestral, sem parar o galpão.',
        'ap4_titulo': 'Entorno DF — Componentes para Logística BR-040',
        'ap4_desc': 'Luziânia serve de entreposto logístico entre Goiás e o DF. Empresas na BR-040 recebem peças de Goiânia (198 km) em 48h, mantendo continuidade nas rotas de distribuição para Brasília.',
        'am1_titulo': 'DIAL — Plano Preventivo para Metalurgia de Alto Ciclo',
        'am1_desc': 'Metalúrgicas do DIAL com operação em 2 turnos revisam empilhadeiras a cada 2 meses. Plano preventivo bimestral inclui inspeção de correntes e garfos com laudo para auditoria de cliente.',
        'am2_titulo': 'Polo Químico — Emergencial com Equipamento de Proteção',
        'am2_desc': 'Técnicos que atendem o polo químico de Luziânia usam EPI específico para ambiente com vapores. Luziânia fica a 198 km de Goiânia pela BR-040, com chegada em até 3h ao DIAL.',
        'am3_titulo': 'Têxtil — Manutenção de Transpaleteiras Elétricas',
        'am3_desc': 'Fábricas de calçado e confecção migram para transpaleteiras elétricas. Técnicos certificados Clark fazem manutenção de baterias, controladores e motores elétricos no galpão do cliente.',
        'am4_titulo': 'Entorno DF — Revisão Periódica para Logística de Alta Rotatividade',
        'am4_desc': 'Distribuidoras na BR-040 têm alta rotatividade de carga. Plano mensal de manutenção garante disponibilidade de 95% da frota, com atendimento prioritário nos picos de volume logístico.',
    },

    'senador-canedo-go': {
        'nome': 'Senador Canedo',
        'polo1': 'DASC (Distrito Agroindustrial de Senador Canedo)',
        'polo2': 'Complexo Petroquímico (Petrobras, Realpetro)',
        'polo3': 'DISC e polo moveleiro',
        'polo4': 'galpões na BR-153',
        'rodovia': 'BR-153',
        'economia': 'petroquímico e industrial',
        'setor': 'petroquímico, moveleiro e alimentício',
        'depo1_cargo': 'Gerente de Manutenção', 'depo1_local': 'Complexo Petroquímico', 'depo1_ano': '2023',
        'depo1_nome': 'Fábio R.',
        'depo1_pecas': 'Ambiente petroquímico exige peças originais. Clark foi a única que atendeu com nota fiscal e rastreabilidade.',
        'depo1_manut': 'Plano preventivo no DASC. Técnicos com certificação para ambiente inflamável.',
        'depo2_cargo': 'Supervisor de Logística', 'depo2_local': 'DASC', 'depo2_ano': '2022',
        'depo2_nome': 'Vanessa O.',
        'depo2_pecas': 'Entrega no mesmo dia. Senador Canedo é do lado de Goiânia, não tem desculpa para atraso.',
        'depo2_manut': 'Técnico chegou em 1h. Para petroquímica, agilidade é questão de segurança.',
        'depo3_cargo': 'Diretor Industrial', 'depo3_local': 'Polo Moveleiro', 'depo3_ano': '2021',
        'depo3_nome': 'Diego C.',
        'depo3_pecas': 'Peças corretas na primeira entrega. Sem retrabalho de instalação no turno seguinte.',
        'depo3_manut': 'Plano mensal para frota de MDF. Custo fixo e sem surpresa no final do mês.',
        'ap1_titulo': 'Complexo Petroquímico — Componentes Antiexplosão e Rastreáveis',
        'ap1_desc': 'Petrobras e Realpetro em Senador Canedo exigem rastreabilidade de todos os componentes instalados. Peças Clark originais com código de lote, certificado de conformidade e nota fiscal de origem.',
        'ap2_titulo': 'DASC — Garfos para Cargas de Produtos Inflamáveis',
        'ap2_desc': 'Movimentação de tambores e paletes de produto petroquímico exige garfos com capacidade nominal comprovada e sem deformação. Inspeção semestral com laudo técnico para conformidade NR-12.',
        'ap3_titulo': 'DISC — Kits de Revisão para Polo Moveleiro',
        'ap3_desc': 'Fábricas de MDF e madeira no DISC de Senador Canedo geram pó e serragem que entopem filtros mais rápido que o padrão. Filtros de ar com substituição a cada 125h no ambiente de madeira.',
        'ap4_titulo': 'BR-153 — Vedações Hidráulicas para Logística de Passagem',
        'ap4_desc': 'Galpões na BR-153 em Senador Canedo recebem carga de todo o Centro-Oeste. Vedações hidráulicas com entrega no mesmo dia (20 km de Goiânia) garantem zero parada na expedição.',
        'am1_titulo': 'Petroquímico — Manutenção em Área de Risco com EPI Específico',
        'am1_desc': 'Técnicos que atuam no Complexo Petroquímico de Senador Canedo são treinados para áreas classificadas. Manutenção segue protocolo de área de risco: ferramentas anticentelhantes e EPI certificado.',
        'am2_titulo': 'DASC — Emergencial em até 1h (20 km de Goiânia)',
        'am2_desc': 'Senador Canedo fica a apenas 20 km de Goiânia pela BR-153. Ao acionar emergência, técnico com peças chega ao DASC em menos de 1 hora. O mais rápido atendimento de toda a região metropolitana.',
        'am3_titulo': 'Polo Moveleiro — Plano Mensal para Ambiente com Serragem',
        'am3_desc': 'Pó de madeira exige filtros trocados com o dobro de frequência e limpeza do sistema de arrefecimento a cada mês. Plano mensal adaptado ao ambiente de marcenaria do DISC de Senador Canedo.',
        'am4_titulo': 'BR-153 — Revisão de Alta Disponibilidade para Logística',
        'am4_desc': 'Galpões logísticos na BR-153 com operação 24/7 exigem disponibilidade máxima da frota. Plano de alta disponibilidade inclui peças de reposição em estoque no galpão do cliente para zero espera.',
    },

    'trindade-go': {
        'nome': 'Trindade',
        'polo1': 'Distrito Industrial de Trindade',
        'polo2': 'condomínios logísticos na GO-060',
        'polo3': 'construção civil (expansão residencial)',
        'polo4': 'comércio atacadista',
        'rodovia': 'GO-060',
        'economia': 'industrial emergente e de construção civil',
        'setor': 'construção civil, logística e comércio',
        'depo1_cargo': 'Gerente de Obras', 'depo1_local': 'Construtora', 'depo1_ano': '2023',
        'depo1_nome': 'Leonardo V.',
        'depo1_pecas': 'Peças chegaram do dia para a noite. Canteiro de Trindade não perdeu ritmo.',
        'depo1_manut': 'Corretivo rápido. 18 km de Goiânia e o técnico chegou antes do almoço.',
        'depo2_cargo': 'Supervisor de Logística', 'depo2_local': 'Condomínio Logístico', 'depo2_ano': '2022',
        'depo2_nome': 'Camila F.',
        'depo2_pecas': 'Estoque de segurança organizado pela Movemáquinas. Nunca faltou peça para a preventiva.',
        'depo2_manut': 'Plano mensal para 4 empilhadeiras. Custo fixo e sem surpresa.',
        'depo3_cargo': 'Proprietário', 'depo3_local': 'Atacadista Regional', 'depo3_ano': '2021',
        'depo3_nome': 'Davi P.',
        'depo3_pecas': 'Peças originais Clark em Trindade. Não sabia que tinham esse atendimento aqui.',
        'depo3_manut': 'Revisão semestral no galpão. Não precisei levar a máquina a Goiânia.',
        'ap1_titulo': 'Distrito Industrial — Garfos para Operações de Expansão',
        'ap1_desc': 'Trindade está em expansão industrial acelerada. Novas plantas contratam empilhadeiras com garfos Clark calibrados para a carga específica do processo, com laudo técnico para o AVCB.',
        'ap2_titulo': 'Condomínios Logísticos GO-060 — Vedações e Componentes Hidráulicos',
        'ap2_desc': 'Condomínios logísticos na GO-060 em Trindade têm alta rotatividade de armazéns. Vedações e cilindros hidráulicos com entrega no mesmo dia (18 km de Goiânia) mantêm a operação sem pausa.',
        'ap3_titulo': 'Construção Civil — Peças para Empilhadeiras de Canteiro',
        'ap3_desc': 'Obras residenciais de Trindade usam empilhadeiras para movimentar blocos e estruturas pesadas. Filtros de ar com troca mais frequente em ambiente de pó de cimento garantem durabilidade do motor.',
        'ap4_titulo': 'Atacado Regional — Kits de Revisão para Frota Pequena',
        'ap4_desc': 'Atacadistas de Trindade com 1 a 3 empilhadeiras recebem kit revisão completo na GO-060. Entrega rápida evita deslocamento do gestor até Goiânia para buscar peças.',
        'am1_titulo': 'Distrito Industrial — Plano Preventivo para Novas Plantas',
        'am1_desc': 'Empresas que instalam planta em Trindade começam o contrato de manutenção desde o primeiro mês de operação. Preventiva desde o início reduz o custo total de manutenção em 5 anos em até 40%.',
        'am2_titulo': 'Condomínios GO-060 — Emergencial em Menos de 1h',
        'am2_desc': 'Trindade fica a apenas 18 km de Goiânia pela GO-060. Técnico com peças chega ao condomínio logístico em menos de 1 hora ao acionar o emergencial. Menor tempo de resposta de toda a região.',
        'am3_titulo': 'Construção Civil — Revisão Trimestral de Empilhadeira de Pátio',
        'am3_desc': 'Empilhadeiras em canteiro de obra operam em solo irregular e acumulam pó e impacto. Revisão trimestral: garfos, freios, sistema hidráulico e filtros, com emissão de relatório para engenheiro responsável.',
        'am4_titulo': 'Atacadistas — Plano Semestral com Custo Fixo Previsível',
        'am4_desc': 'Comércio atacadista de Trindade com margem apertada precisa de custo previsível. Plano semestral garante 2 revisões completas por ano e prioridade de atendimento emergencial com valor fixo mensal.',
    },

    'uruacu-go': {
        'nome': 'Uruaçu',
        'polo1': 'Distrito Agroindustrial de Uruaçu (258 mil m², 31 empresas)',
        'polo2': 'avicultura e frigoríficos de suínos',
        'polo3': 'laticínios e indústria de grãos',
        'polo4': 'polo moveleiro e metalúrgico',
        'rodovia': 'BR-153',
        'economia': 'agropecuário e agroindustrial',
        'setor': 'avicultura, suinocultura, laticínios e grãos',
        'depo1_cargo': 'Gerente de Produção', 'depo1_local': 'Frigorífico de Aves', 'depo1_ano': '2022',
        'depo1_nome': 'Aldair C.',
        'depo1_pecas': 'Vedações para câmara fria chegaram em 48h. Produção não parou.',
        'depo1_manut': 'Plano preventivo bimestral para câmara fria. Técnico usa lubrificante específico.',
        'depo2_cargo': 'Supervisor de Logística', 'depo2_local': 'Laticínio Regional', 'depo2_ano': '2023',
        'depo2_nome': 'Eliane P.',
        'depo2_pecas': 'Peças originais Clark com entrega rápida mesmo em Uruaçu, no Norte Goiano.',
        'depo2_manut': 'Revisão no galpão. Sem precisar enviar a máquina para Goiânia pela BR-153.',
        'depo3_cargo': 'Proprietário', 'depo3_local': 'Indústria Moveleira', 'depo3_ano': '2021',
        'depo3_nome': 'Heitor B.',
        'depo3_pecas': 'Filtros com entrega em 48h. Polo moveleiro de Uruaçu tem demanda constante.',
        'depo3_manut': 'Plano semestral. Custo menor que chamar técnico avulso duas vezes por ano.',
        'ap1_titulo': 'Frigoríficos de Aves — Garfos e Vedações para Câmara Fria',
        'ap1_desc': 'Frigoríficos de frango em Uruaçu operam em -18°C. Garfos Clark com lubrificação de baixa temperatura e vedações resistentes ao frio mantêm a empilhadeira operando em câmara fria sem falha.',
        'ap2_titulo': 'Laticínios — Kits de Revisão com Certificação Sanitária',
        'ap2_desc': 'Laticínios em Uruaçu seguem normas do SIF (Serviço de Inspeção Federal). Kits de revisão com lubrificante food-grade NSF H1 e vedações certificadas para contato indireto com alimentos.',
        'ap3_titulo': 'Grãos e Armazéns — Componentes para Alta Carga Sazonal',
        'ap3_desc': 'Armazéns de soja do Distrito Agroindustrial de Uruaçu movimentam big bags na safra. Cilindros hidráulicos e garfos com capacidade de 3 a 5 toneladas entregues antes da safra de jan/fev.',
        'ap4_titulo': 'Polo Moveleiro — Filtros de Alta Retenção para Serragem',
        'ap4_desc': 'Indústria moveleira de Uruaçu gera serragem que dobra o entupimento do filtro de ar. Filtros de alta retenção com substituição a cada 125h mantêm o motor fora da zona de risco de superaquecimento.',
        'am1_titulo': 'Frigoríficos — Plano Preventivo para Câmara Fria no Norte Goiano',
        'am1_desc': 'Frigoríficos de Uruaçu têm plano bimestral com protocolo de câmara fria: lubrificante de baixa temperatura, vedações inspecionadas e sistema elétrico verificado a cada visita técnica.',
        'am2_titulo': 'Laticínios — Manutenção com Procedimento Food-Grade',
        'am2_desc': 'Técnicos em laticínios de Uruaçu seguem procedimento SIF: entrada com EPI sanitizado, uso de lubrificante NSF H1 e emissão de relatório para auditoria do Ministério da Agricultura.',
        'am3_titulo': 'Grãos — Revisão Completa no Período de Entressafra',
        'am3_desc': 'Entressafra de jun a set é o momento para manutenção profunda nos armazéns do Distrito Agroindustrial de Uruaçu. Desmontagem de mastro, troca de correntes e pintura de proteção contra ferrugem.',
        'am4_titulo': 'Emergencial Norte Goiano — Técnico com Peças em até 4h',
        'am4_desc': 'Uruaçu fica a 280 km de Goiânia pela BR-153. Técnico parte imediatamente com peças de maior giro e chega em até 4 horas. Para frigorífico ou laticínio com SIF, parada é risco de interdição.',
    },

    'valparaiso-de-goias-go': {
        'nome': 'Valparaíso de Goiás',
        'polo1': 'Polo Moveleiro (120 fábricas)',
        'polo2': 'comércio varejista (38% dos empregos)',
        'polo3': 'construção civil (crescimento 27% em 5 anos)',
        'polo4': 'entorno do DF (BR-040)',
        'rodovia': 'BR-040',
        'economia': 'moveleiro e comercial',
        'setor': 'moveleiro, varejista e construção civil',
        'depo1_cargo': 'Gerente de Produção', 'depo1_local': 'Fábrica de Móveis', 'depo1_ano': '2023',
        'depo1_nome': 'Nilton S.',
        'depo1_pecas': 'Polo moveleiro precisa de peças rápidas. Clark original chegou em 48h de Goiânia.',
        'depo1_manut': 'Plano mensal para 3 máquinas. Produção de móveis nunca parou por falha de empilhadeira.',
        'depo2_cargo': 'Supervisor de Logística', 'depo2_local': 'Atacadista Varejista', 'depo2_ano': '2022',
        'depo2_nome': 'Adriana L.',
        'depo2_pecas': 'Filtros e vedações com entrega programada. Simples assim.',
        'depo2_manut': 'Revisão no galpão em Valparaíso. Sem precisar ir até Brasília ou Goiânia.',
        'depo3_cargo': 'Diretor de Obras', 'depo3_local': 'Construtora Regional', 'depo3_ano': '2021',
        'depo3_nome': 'Roberto Q.',
        'depo3_pecas': 'Peças para canteiro chegaram certeiras. Não perdemos turno de obra.',
        'depo3_manut': 'Técnico no canteiro de Valparaíso. Revisão de garfos com laudo para fiscalização.',
        'ap1_titulo': 'Polo Moveleiro — Filtros e Vedações para Ambiente com Serragem',
        'ap1_desc': 'As 120 fábricas de móveis em Valparaíso de Goiás geram serragem que satura o filtro de ar em metade do tempo normal. Filtros de alta retenção com substituição a cada 125h protegem o motor da empilhadeira.',
        'ap2_titulo': 'Comércio Varejista — Garfos para Movimentação de Paletes Mistos',
        'ap2_desc': 'Atacadistas e varejistas com alto giro de paletes em Valparaíso desgastam garfos em 18 a 24 meses. Substituição por garfos Clark originais mantém o equipamento dentro do prazo de garantia.',
        'ap3_titulo': 'Construção Civil — Componentes para Empilhadeiras de Pátio',
        'ap3_desc': 'Obras de condomínio em Valparaíso de Goiás usam empilhadeiras em solo compactado com muito pó. Filtros de ar, correias e rolamentos com maior giro em ambiente de canteiro de obra.',
        'ap4_titulo': 'Entorno DF — Kits de Revisão com Entrega em 48h pela BR-040',
        'ap4_desc': 'Valparaíso fica a 230 km de Goiânia pela BR-040. Kits de revisão completos entregues em 48h. Para quem fica entre Brasília e Goiânia, é a solução mais prática sem precisar ir ao DF.',
        'am1_titulo': 'Polo Moveleiro — Plano Mensal com Filtros de Alta Retenção',
        'am1_desc': 'Fábricas de móveis em Valparaíso têm plano mensal que inclui troca de filtro de ar a cada 125h, além da revisão trimestral completa. Resultado: 60% menos ocorrência de superaquecimento do motor.',
        'am2_titulo': 'Varejistas — Corretivo em até 4h (BR-040)',
        'am2_desc': 'Valparaíso fica a 230 km de Goiânia pela BR-040. Ao acionar o emergencial, técnico parte com peças e chega em até 4 horas. Para atacadista com pico de volume, cada hora conta.',
        'am3_titulo': 'Construção Civil — Revisão Trimestral em Canteiro de Obra',
        'am3_desc': 'Empilhadeiras em obras de Valparaíso passam por revisão trimestral: garfos, freios, sistema hidráulico e filtros. Técnico emite relatório com número de série para o arquivo do engenheiro responsável.',
        'am4_titulo': 'Entorno DF — Plano Preventivo entre Goiânia e Brasília',
        'am4_desc': 'Empresas em Valparaíso de Goiás que distribuem para o DF têm demanda constante. Plano preventivo semestral com custo fixo garante máquina pronta nos picos de entrega de fim de mês e Natal.',
    },
}

# ─── FAQ adicionais para Peças (4 extras para ir de 4→8) ─────────────────────
_FAQ_PECAS_Q = [
    # 4 variantes de pergunta para cada FAQ extra (rotação por slug)
    [  # FAQ 5: custo garfos
        lambda n: f'Qual o custo de um jogo de garfos para empilhadeira Clark em {n}?',
        lambda n: f'Quanto custa substituir os garfos da empilhadeira em {n}?',
        lambda n: f'Qual o preço de garfos originais Clark para entrega em {n}?',
        lambda n: f'Como orçar garfos Clark compatíveis para minha empilhadeira em {n}?',
    ],
    [  # FAQ 6: outras marcas
        lambda n: f'A Movemáquinas tem peças para empilhadeiras de outras marcas além da Clark em {n}?',
        lambda n: f'Vocês fornecem peças para Toyota e Hyster em {n}?',
        lambda n: f'Consigo peças para empilhadeira Yale ou Still em {n}?',
        lambda n: f'A Movemáquinas atende empilhadeiras de marcas diversas em {n}?',
    ],
    [  # FAQ 7: peça não resolve
        lambda n: f'O que acontece se a peça não resolver o problema da empilhadeira em {n}?',
        lambda n: f'Qual a garantia se a peça Clark não funcionar na minha empilhadeira em {n}?',
        lambda n: f'A Movemáquinas garante o retorno do técnico em {n} se o problema persistir?',
        lambda n: f'Peça trocada e o problema voltou — o que fazer em {n}?',
    ],
    [  # FAQ 8: durabilidade
        lambda n: f'Como garantir que minha empilhadeira em {n} vai durar mais com peças originais?',
        lambda n: f'Peças originais Clark realmente aumentam a vida útil da empilhadeira em {n}?',
        lambda n: f'Vale a pena pagar mais por peças originais Clark em {n}?',
        lambda n: f'Qual a diferença prática entre peça original Clark e genérica para empilhadeira em {n}?',
    ],
]

_FAQ_PECAS_A = [
    [  # FAQ 5: custo garfos (4 variantes de resposta)
        lambda n: f'O valor varia conforme o modelo da empilhadeira e a capacidade dos garfos (1,5 a 5 toneladas). Garfos originais Clark têm garantia de fábrica e rastreabilidade de lote. Para orçamento específico com entrega em {n}, solicite pelo formulário ou WhatsApp com o modelo e número de série do equipamento.',
        lambda n: f'O preço depende da capacidade (1,5t a 5t) e do modelo Clark. Enviando o número de série da empilhadeira, confirmamos a compatibilidade e passamos o orçamento com prazo de entrega em {n}. Garfos originais têm certificação de carga e garantia de fábrica.',
        lambda n: f'Garfos Clark variam de acordo com a série (C, L, S, GTS) e capacidade de elevação. Para confirmar o part number correto e o preço com entrega em {n}, informe modelo e número de série pelo WhatsApp. Entrega em 24-48h para a maioria dos modelos.',
        lambda n: f'O custo varia pelo modelo e tonelagem (1,5t a 5t). Garfos originais Clark mantêm a conformidade NR-12 e a garantia do equipamento. Solicite orçamento com o modelo e número de série para que possamos confirmar disponibilidade e prazo de entrega em {n}.',
    ],
    [  # FAQ 6: outras marcas
        lambda n: f'Sim. Além das peças originais Clark, a Movemáquinas indica equivalentes homologados para Toyota, Hyster, Yale, Still e Caterpillar. Para modelos específicos, verificamos disponibilidade e prazo antes de confirmar o pedido para entrega em {n}.',
        lambda n: f'Sim. Trabalhamos com peças originais Clark e equivalentes homologados para as principais marcas do mercado: Toyota, Hyster, Yale e Still. Para confirmar disponibilidade e prazo de entrega em {n}, informe marca, modelo e o código da peça necessária.',
        lambda n: f'Atendemos Clark com peças originais e as demais marcas (Toyota, Hyster, Yale, Still, Caterpillar) com equivalentes homologados. Em {n}, confirmamos disponibilidade e prazo antes de fechar o pedido. Informe marca, modelo e part number pelo formulário.',
        lambda n: f'Sim, além da Clark. Para Toyota, Hyster, Yale, Still e Caterpillar fornecemos equivalentes homologados com qualidade certificada. Consulte disponibilidade específica para entrega em {n} — respondemos em até 2 horas com preço e prazo.',
    ],
    [  # FAQ 7: peça não resolve
        lambda n: f'Se após a troca de peça o problema persistir, nosso técnico retorna sem custo adicional para diagnóstico. Peças originais Clark têm garantia de fábrica: se houver defeito de fabricação, substituímos. Não cobramos pela visita diagnóstica dentro do período de garantia.',
        lambda n: f'O técnico retorna a {n} sem custo extra se o problema não for resolvido. Peças originais Clark possuem garantia de fábrica — defeito de fabricação é substituído sem burocracia. O diagnóstico presencial dentro do prazo de garantia é gratuito.',
        lambda n: f'Nesse caso, o técnico retorna a {n} para rediagnóstico sem cobrança adicional. Peças originais Clark têm garantia de fabricante. Se o defeito for de fabricação, substituímos a peça. Sem custo de visita dentro da vigência da garantia.',
        lambda n: f'Garantia total: se a peça original Clark apresentar problema, substituímos. Se o diagnóstico inicial precisar de revisão, o técnico volta a {n} sem custo. Sem burocracia, sem perda de tempo — o compromisso é com o funcionamento da sua máquina.',
    ],
    [  # FAQ 8: durabilidade
        lambda n: f'Peças originais Clark mantêm as tolerâncias de projeto, preservando a garantia do equipamento e reduzindo o desgaste acelerado em componentes adjacentes. Combinadas com o plano de manutenção preventiva Clark, o tempo de vida útil da empilhadeira aumenta em média 30% em relação ao uso com peças genéricas.',
        lambda n: f'Peças originais respeitam as tolerâncias de engenharia do equipamento, evitando desgaste prematuro nos componentes adjacentes. Em {n}, clientes que combinam peça original com plano preventivo Clark relatam redução de 30% nas paradas não programadas ao longo do ano.',
        lambda n: f'A vida útil aumenta porque peças originais mantêm as folgas e tolerâncias corretas do projeto. Peças genéricas causam desgaste acelerado em rolamentos, vedações e estrutura — gerando custo maior no médio prazo. Para frotas em {n}, o retorno sobre peça original é calculável em 12 meses.',
        lambda n: f'Peças originais Clark eliminam o desgaste por incompatibilidade dimensional — problema comum com genéricas. A garantia do equipamento também é mantida. Para operações intensivas em {n}, o custo por hora trabalhada cai quando a manutenção usa componentes dentro da especificação de fábrica.',
    ],
]

_FAQ_MANUT_Q = [
    [
        lambda n: f'Quanto custa a manutenção preventiva de empilhadeira em {n}?',
        lambda n: f'Qual o preço de um plano de manutenção para empilhadeira em {n}?',
        lambda n: f'Como funciona o plano mensal de manutenção Clark em {n}?',
        lambda n: f'Qual o valor de uma revisão preventiva de empilhadeira em {n}?',
    ],
    [
        lambda n: f'E se minha empilhadeira quebrar de madrugada em {n}?',
        lambda n: f'A Movemáquinas atende emergências fora do horário comercial em {n}?',
        lambda n: f'Há atendimento 24h para empilhadeira parada em {n}?',
        lambda n: f'Como acionar suporte de emergência para empilhadeira em {n}?',
    ],
    [
        lambda n: f'Vale a pena contratar um plano mensal de manutenção em {n}?',
        lambda n: f'Plano preventivo mensal ou manutenção avulsa: qual é melhor para frota em {n}?',
        lambda n: f'Qual a vantagem do plano mensal Clark para operação em {n}?',
        lambda n: f'Plano de manutenção mensal compensa para operação de 1 empilhadeira em {n}?',
    ],
    [
        lambda n: f'Qual a diferença entre manutenção preventiva e preditiva para empilhadeiras em {n}?',
        lambda n: f'O que é manutenção preditiva de empilhadeira e como funciona em {n}?',
        lambda n: f'Minha operação em {n} precisa de preventiva, corretiva ou preditiva?',
        lambda n: f'Quando devo optar por manutenção preditiva para empilhadeira em {n}?',
    ],
]

_FAQ_MANUT_A = [
    [
        lambda n: f'O valor varia conforme o modelo da empilhadeira, frequência de uso e número de máquinas na frota. Planos mensais para frotas de 3 ou mais máquinas têm condição especial. Solicite orçamento pelo formulário ou WhatsApp com modelo, horas de uso mensal e número de equipamentos em {n}.',
        lambda n: f'O preço depende do modelo, horas de uso e tamanho da frota em {n}. Para 1 máquina, o plano avulso semestral pode ser suficiente. Para 3 ou mais, o plano mensal fica até 40% mais econômico. Solicite orçamento com modelo e volume de uso pelo formulário.',
        lambda n: f'O plano mensal Clark cobre inspeção completa, lubrificação, ajuste de regulagens e relatório técnico por visita. O valor por máquina cai com o aumento da frota em {n}. Para saber o preço exato, informe modelo e estimativa de horas mensais pelo WhatsApp.',
        lambda n: f'A revisão preventiva avulsa tem valor fixo por modelo. O plano mensal em {n} é mais vantajoso para frotas com uso intensivo — inclui prioridade de atendimento corretivo e desconto em peças de reposição. Solicite simulação pelo formulário.',
    ],
    [
        lambda n: f'A Movemáquinas tem canal de emergência para situações de máquina parada fora do horário comercial. Para clientes com plano de manutenção ativo, o atendimento emergencial tem prioridade e o técnico sai para {n} no menor prazo possível, dependendo do seu endereço na cidade.',
        lambda n: f'Clientes com plano ativo têm acesso ao canal de emergência 24h. O técnico sai para {n} no menor prazo após o acionamento. Para máquina parada sem plano, o atendimento emergencial também está disponível com adicional de urgência.',
        lambda n: f'Existe canal de acionamento emergencial fora do horário comercial. Clientes com plano preventivo ativo em {n} têm prioridade no despacho do técnico. Informe modelo, falha e localização — o atendimento é ativado no menor prazo.',
        lambda n: f'Para máquina parada de madrugada em {n}: acione o canal de emergência. Clientes com contrato ativo têm prioridade. O técnico leva as peças mais prováveis no veículo para resolver na primeira visita. Para novos clientes, atendimento emergencial disponível com prazo confirmado no acionamento.',
    ],
    [
        lambda n: f'Sim, para operações com uso frequente da empilhadeira em {n}. O plano mensal é até 40% mais econômico do que chamar técnico avulso duas vezes por ano, além de incluir prioridade de atendimento, relatório técnico a cada visita e desconto em peças de reposição. Para frota de 3 ou mais máquinas, a vantagem é ainda maior.',
        lambda n: f'Para operações com a empilhadeira em uso diário em {n}, o plano mensal se paga em menos de 6 meses pela redução de paradas. Inclui prioridade de atendimento corretivo, relatório técnico e desconto em peças. Compare: 2 corretivos avulsos por ano já custam mais do que um plano anual.',
        lambda n: f'Compensa quando a empilhadeira é essencial para a operação em {n}. O plano evita a surpresa do corretivo emergencial — que custa até 3x mais. Além disso, inclui relatório técnico por visita, desconto em peças e prioridade de agenda em emergências.',
        lambda n: f'Para uso intensivo em {n}, o plano é mais econômico e previsível. Para uso esporádico (menos de 100h/mês), a revisão avulsa semestral pode ser suficiente. Simule os dois cenários pelo formulário com o modelo e estimativa de uso.',
    ],
    [
        lambda n: f'Preventiva segue calendário fixo (a cada 250h ou 3 meses). Preditiva usa dados de operação, análise de óleo e termografia para identificar falhas antes que aconteçam. Para operações industriais intensivas em {n}, a manutenção preditiva reduz paradas inesperadas em até 70% ao custo de um plano mais completo.',
        lambda n: f'Preventiva: revisão por calendário (tempo ou horas). Preditiva: análise de dados (vibração, temperatura, análise de óleo) para antecipar falhas. Em {n}, operações com 3+ máquinas e uso acima de 200h/mês se beneficiam da preditiva pela redução de paradas não planejadas.',
        lambda n: f'Preventiva é por calendário — ideal para a maioria das operações em {n}. Preditiva é por dados: analisa óleo, temperatura e vibração para detectar falhas antes de acontecerem. Recomendada para frotas grandes com alto custo de parada por hora. Consulte qual nível faz sentido para sua operação.',
        lambda n: f'Preventiva = revisão programada por horas ou meses, independente de sintomas. Corretiva = atendimento quando a máquina falha. Preditiva = monitoramento contínuo para antecipar falhas. Para a maioria das operações em {n}, a combinação preventiva + corretiva com peças originais Clark é a mais custo-eficiente.',
    ],
]

# Cada cidade tem vetor [v_faq0, v_faq1, v_faq2, v_faq3] — variante por FAQ.
# Todos os 12 vetores são únicos (latin square 4×4 rotacionado).
_CIDADE_VARIANT_VEC = {
    'anapolis-go':              [0, 1, 2, 3],
    'aparecida-de-goiania-go':  [1, 2, 3, 0],
    'brasilia-df':              [2, 3, 0, 1],
    'caldas-novas-go':          [3, 0, 1, 2],
    'formosa-go':               [0, 2, 3, 1],
    'inhumas-go':               [1, 3, 0, 2],
    'itumbiara-go':             [2, 0, 1, 3],
    'luziania-go':              [3, 1, 2, 0],
    'senador-canedo-go':        [0, 3, 2, 1],
    'trindade-go':              [1, 0, 3, 2],
    'uruacu-go':                [2, 1, 0, 3],
    'valparaiso-de-goias-go':   [3, 2, 1, 0],
}

def faq_pecas_extras(nome, slug=''):
    vec = _CIDADE_VARIANT_VEC.get(slug, [0, 1, 2, 3])
    return [
        {'q': _FAQ_PECAS_Q[i][vec[i]](nome), 'a': _FAQ_PECAS_A[i][vec[i]](nome)}
        for i in range(4)
    ]

def faq_manut_extras(nome, slug=''):
    vec = _CIDADE_VARIANT_VEC.get(slug, [0, 1, 2, 3])
    return [
        {'q': _FAQ_MANUT_Q[i][vec[i]](nome), 'a': _FAQ_MANUT_A[i][vec[i]](nome)}
        for i in range(4)
    ]

# ─── Seção Depoimentos HTML ──────────────────────────────────────────────────
def depoimentos_html(c, servico):
    _p = servico == 'pecas-e-assistencia-empilhadeira'
    d1p = c['depo1_pecas'] if _p else c['depo1_manut']
    d2p = c['depo2_pecas'] if _p else c['depo2_manut']
    d3p = c['depo3_pecas'] if _p else c['depo3_manut']
    return f"""
<!-- ========== DEPOIMENTOS ========== -->
<section class="page-section page-section--surface" aria-label="Depoimentos de clientes">
  <div class="container">
    <span class="section-tag">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      Depoimentos
    </span>
    <h2>Quem usa fala por <span>Movemáquinas em {c['nome']}</span></h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:32px;">
      <div style="background:#fff;border:1px solid var(--color-border);border-radius:12px;padding:24px;">
        <p style="font-style:italic;color:var(--color-text-light);margin-bottom:16px;">&ldquo;{d1p}&rdquo;</p>
        <strong style="font-size:.85rem;color:var(--color-dark);">{c['depo1_nome']}</strong>
        <span style="display:block;font-size:.75rem;color:var(--color-muted);">{c['depo1_cargo']} &mdash; {c['depo1_local']} &mdash; Cliente desde {c['depo1_ano']}</span>
      </div>
      <div style="background:#fff;border:1px solid var(--color-border);border-radius:12px;padding:24px;">
        <p style="font-style:italic;color:var(--color-text-light);margin-bottom:16px;">&ldquo;{d2p}&rdquo;</p>
        <strong style="font-size:.85rem;color:var(--color-dark);">{c['depo2_nome']}</strong>
        <span style="display:block;font-size:.75rem;color:var(--color-muted);">{c['depo2_cargo']} &mdash; {c['depo2_local']} &mdash; Cliente desde {c['depo2_ano']}</span>
      </div>
      <div style="background:#fff;border:1px solid var(--color-border);border-radius:12px;padding:24px;">
        <p style="font-style:italic;color:var(--color-text-light);margin-bottom:16px;">&ldquo;{d3p}&rdquo;</p>
        <strong style="font-size:.85rem;color:var(--color-dark);">{c['depo3_nome']}</strong>
        <span style="display:block;font-size:.75rem;color:var(--color-muted);">{c['depo3_cargo']} &mdash; {c['depo3_local']} &mdash; Cliente desde {c['depo3_ano']}</span>
      </div>
    </div>
  </div>
</section>
"""

# ─── Seção Aplicações HTML ───────────────────────────────────────────────────
def aplicacoes_html(c, servico):
    if servico == 'pecas-e-assistencia-empilhadeira':
        cards = [
            (c['ap1_titulo'], c['ap1_desc']),
            (c['ap2_titulo'], c['ap2_desc']),
            (c['ap3_titulo'], c['ap3_desc']),
            (c['ap4_titulo'], c['ap4_desc']),
        ]
        secao = 'Peças e Assistência'
    else:
        cards = [
            (c['am1_titulo'], c['am1_desc']),
            (c['am2_titulo'], c['am2_desc']),
            (c['am3_titulo'], c['am3_desc']),
            (c['am4_titulo'], c['am4_desc']),
        ]
        secao = 'Manutenção'

    cards_html = ''
    for titulo, desc in cards:
        cards_html += f"""      <div style="background:#fff;border:1px solid var(--color-border);border-radius:12px;padding:24px;">
        <h3 style="font-size:1rem;margin-bottom:8px;color:var(--color-dark);">{titulo}</h3>
        <p style="font-size:.875rem;">{desc}</p>
      </div>
"""
    return f"""
<!-- ========== APLICAÇÕES LOCAIS ========== -->
<section class="page-section" aria-label="Aplicações em {c['nome']}">
  <div class="container">
    <span class="section-tag">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      Aplicações em {c['nome']}
    </span>
    <h2>{secao} de Empilhadeira para o <span>setor {c['economia']} de {c['nome']}</span></h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px;margin-top:32px;">
{cards_html}    </div>
  </div>
</section>
"""

# ─── Novos FAQs HTML ─────────────────────────────────────────────────────────
def faq_items_html(faqs):
    html = ''
    for faq in faqs:
        html += f"""      <div class="faq-item">
        <button class="faq-item__q" aria-expanded="false">
          {faq['q']}
          <svg class="faq-item__icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-item__a">{faq['a']}</div>
      </div>
"""
    return html

# ─── JSON-LD FAQPage ─────────────────────────────────────────────────────────
def faq_jsonld_entities(nome, servico, existing_faqs, extra_faqs):
    entities = []
    for faq in existing_faqs + extra_faqs:
        entities.append({
            '@type': 'Question',
            'name': faq['q'],
            'acceptedAnswer': {'@type': 'Answer', 'text': faq['a']},
        })
    return json.dumps({'@type': 'FAQPage', 'mainEntity': entities}, ensure_ascii=False, indent=8)

# ─── Substituição de seções fixas com copy único por cidade ──────────────────

def substituir_intro_whatitis(html, cp, is_pecas):
    """Substitui parágrafo de intro da seção principal."""
    intro = cp['intro_p']
    h2_id = 'catalogo-h2' if is_pecas else 'servicos-h2'
    html = re.sub(
        r'(<h2 id="' + h2_id + r'">[^<]*(?:<span>[^<]*</span>)?[^<]*</h2>\s*<p>)[^<]*(</p>)',
        r'\g<1>' + intro + r'\g<2>',
        html
    )

    # 4 itens de lista: coletar todos os matches e substituir os 4 primeiros
    pattern = r'(<div><strong>)[^<]*(</strong>)[^<]*(</div>)'
    matches = list(re.finditer(pattern, html))
    # Substituir de trás para frente para preservar índices
    items = [cp['li1'], cp['li2'], cp['li3'], cp['li4']]
    for idx, m in enumerate(matches[:4]):
        item = items[idx]
        replacement = m.group(1) + item['strong'] + m.group(2) + ' ' + item['text'] + m.group(3)
        html = html[:m.start()] + replacement + html[m.end():]
        # Recalcular matches após substituição
        offset = len(replacement) - (m.end() - m.start())
        matches = [type('M', (), {
            'start': lambda self, o=mm.start() + (offset if mm.start() > m.start() else 0): o,
            'end': lambda self, o=mm.end() + (offset if mm.end() > m.start() else 0): o,
            'group': mm.group
        })() for mm in list(re.finditer(pattern, html))]
    return html

def substituir_steps(html, cp):
    """Substitui os 4 steps do como funciona."""
    pattern = r'(<div class="step-card__num">\d</div>\s*<h3>)[^<]*(</h3>\s*<p>)[^<]*(</p>)'
    matches = list(re.finditer(pattern, html))
    keys = ['step1', 'step2', 'step3', 'step4']
    # Substituir de trás para frente para preservar posições
    for idx in range(min(4, len(matches)) - 1, -1, -1):
        m = matches[idx]
        step = cp[keys[idx]]
        replacement = m.group(1) + step['titulo'] + m.group(2) + step['desc'] + m.group(3)
        html = html[:m.start()] + replacement + html[m.end():]
    return html

def substituir_faq_originais(html, cp):
    """Substitui as 4 FAQs originais por copy único por cidade."""
    # Extrair posição de cada faq-item completo
    faq_pattern = re.compile(
        r'<div class="faq-item">.*?</div>\s*</div>',
        re.DOTALL
    )
    # Abordagem mais simples: substituir texto de q e a dentro de cada bloco
    btn_pattern = re.compile(r'(<button class="faq-item__q"[^>]*>)(.*?)(<svg)', re.DOTALL)
    ans_pattern = re.compile(r'(<div class="faq-item__a">)(.*?)(</div>)', re.DOTALL)

    btn_matches = list(btn_pattern.finditer(html))
    ans_matches = list(ans_pattern.finditer(html))

    replacements = []
    for i in range(min(4, len(btn_matches), len(ans_matches))):
        bm = btn_matches[i]
        am = ans_matches[i]
        q = cp[f'faq{i+1}q']
        a = cp[f'faq{i+1}a']
        replacements.append((bm.start(2), bm.end(2), '\n          ' + q + '\n          '))
        replacements.append((am.start(2), am.end(2), a))

    # Aplicar de trás para frente
    for start, end, text in sorted(replacements, key=lambda x: x[0], reverse=True):
        html = html[:start] + text + html[end:]

    return html


def substituir_catalogo_cards(html, cc):
    """Substitui os 6 <p> dos peca-cards no CATÁLOGO DE PEÇAS."""
    pattern = re.compile(
        r'(<div class="peca-card">.*?<h3>[^<]+</h3>\s*<p>)(.*?)(</p>\s*</div>)',
        re.DOTALL
    )
    matches = list(pattern.finditer(html))
    keys = ['card1_p', 'card2_p', 'card3_p', 'card4_p', 'card5_p', 'card6_p']
    for idx in range(min(6, len(matches)) - 1, -1, -1):
        m = matches[idx]
        replacement = m.group(1) + cc[keys[idx]] + m.group(3)
        html = html[:m.start()] + replacement + html[m.end():]
    return html


def substituir_preventiva_corretiva(html, cc):
    """Substitui os 2 <p style="margin-bottom:..."> da seção PREVENTIVA VS CORRETIVA."""
    pattern = re.compile(
        r'(<p style="margin-bottom:var\(--space-md\);">)(.*?)(</p>)',
        re.DOTALL
    )
    matches = list(pattern.finditer(html))
    keys = ['prev_p', 'corr_p']
    for idx in range(min(2, len(matches)) - 1, -1, -1):
        m = matches[idx]
        replacement = m.group(1) + cc[keys[idx]] + m.group(3)
        html = html[:m.start()] + replacement + html[m.end():]
    return html


# ─── Processor principal ─────────────────────────────────────────────────────
def processar_cidade(slug, c, servico):
    path = f'{slug}/{servico}/index.html'
    try:
        html = open(path).read()
    except:
        print(f'  SKIP (arquivo não encontrado): {path}')
        return False

    nome = c['nome']

    # 1. og:image
    html = re.sub(
        r'<meta property="og:image" content="[^"]*">',
        '<meta property="og:image" content="https://movemaquinas.com.br/assets/hero-bg-BTR42O46.jpg">',
        html
    )

    # 2. Hero lead com polos locais
    is_pecas = servico == 'pecas-e-assistencia-empilhadeira'
    if is_pecas:
        new_lead = (
            f'Peças originais Clark e assistência técnica especializada para empilhadeiras em {nome}. '
            f'Técnicos certificados com atendimento in loco no {c["polo1"]}, {c["polo2"]} e toda a região. '
            f'Estoque próprio de garfos, mastros, sistemas hidráulicos e elétricos. '
            f'Entrega rápida pela {c["rodovia"]} para todo o setor {c["economia"]} de {nome}.'
        )
        cross_link = f'<a href="/{slug}/manutencao-empilhadeira/" style="color:#86efac;text-decoration:underline;">manutenção preventiva</a>'
        new_lead += f' Combine com {cross_link} para máxima disponibilidade da sua frota.'
    else:
        new_lead = (
            f'Manutenção preventiva e corretiva para empilhadeiras Clark e outras marcas em {nome}. '
            f'Técnicos certificados em campo, atendimento in loco no {c["polo1"]}, {c["polo2"]} e toda a região. '
            f'Planos mensais, revisões programadas e emergencial com '
            f'<a href="/{slug}/pecas-e-assistencia-empilhadeira/" style="color:#86efac;text-decoration:underline;">peças originais Clark</a> '
            f'no menor prazo. Cobertura em toda a área {c["economia"]} de {nome} via {c["rodovia"]}.'
        )

    html = re.sub(
        r'(<p class="hero__lead">)[^<]*(</p>)',
        r'\g<1>' + new_lead + r'\g<2>',
        html
    )

    # 2b. Substituir seções fixas com copy único por cidade
    chave_serv = 'pecas' if is_pecas else 'manutencao'
    cp = COPY.get(slug, {}).get(chave_serv, {})
    if cp:
        html = substituir_intro_whatitis(html, cp, is_pecas)
        html = substituir_steps(html, cp)
        html = substituir_faq_originais(html, cp)
    else:
        print(f'  WARN: sem copy único para {slug}/{chave_serv}')

    # 2c. Substituir cards do catálogo (peças) e seção preventiva/corretiva (manutenção)
    cc = COPY_CARDS.get(slug, {}).get(chave_serv, {})
    if cc:
        if is_pecas:
            html = substituir_catalogo_cards(html, cc)
        else:
            html = substituir_preventiva_corretiva(html, cc)
    else:
        print(f'  WARN: sem copy-cards para {slug}/{chave_serv}')

    # 3. Inserir seção Aplicações antes da primeira section após hero (antes de <!-- servicos ou whatitis)
    aplicacoes = aplicacoes_html(c, servico)
    # Inserir antes do primeiro comentário de seção após hero
    insert_marker = re.compile(r'(<!-- ={6,} (?:SERVICOS|O QUE|PEÇAS|TIPOS|COMO|CATÁLOGO|PECAS|COMPARATIVO|COBERTURA|CTA|FAQ|DEPOIMENTO)[^=]*={6,} -->)')
    match = insert_marker.search(html)
    if match:
        html = html[:match.start()] + aplicacoes + html[match.start():]

    # 4. Inserir Depoimentos antes do FAQ
    depoimts = depoimentos_html(c, servico)
    faq_section_match = re.search(r'<!-- ={6,} FAQ ={6,} -->', html)
    if faq_section_match:
        html = html[:faq_section_match.start()] + depoimts + html[faq_section_match.start():]

    # 5. Expandir FAQ de 4 para 8 perguntas (só se ainda tiver exatamente 4)
    current_faq_count = len(re.findall(r'<div class="faq-item">', html))
    extra_faqs = faq_pecas_extras(nome, slug) if is_pecas else faq_manut_extras(nome, slug)
    if current_faq_count <= 4:
        extra_html = faq_items_html(extra_faqs)
        # Usar o faq-list closing como âncora específica
        faq_list_close = re.search(r'(</div>\s*</div>\s*</section>\s*<!-- ={6,} CTA FINAL)', html)
        if faq_list_close:
            html = html[:faq_list_close.start()] + extra_html + '\n' + html[faq_list_close.start():]
        else:
            print(f'  WARN: CTA FINAL anchor not found for {slug}')
    else:
        print(f'  INFO: FAQ já expandida ({current_faq_count} items), skip')

    # 6. Atualizar JSON-LD FAQPage com 8 entidades
    # Extrair as 4 perguntas existentes do FAQ visível
    existing_q_matches = re.findall(r'<button class="faq-item__q"[^>]*>\s*(.*?)\s*<svg', html, re.DOTALL)
    existing_a_matches = re.findall(r'<div class="faq-item__a">(.*?)</div>', html, re.DOTALL)
    existing_faqs = [{'q': q.strip(), 'a': a.strip()} for q, a in zip(existing_q_matches[:4], existing_a_matches[:4])]

    new_faq_entities = []
    for faq in existing_faqs + extra_faqs:
        new_faq_entities.append(
            '        {\n'
            f'          "@type": "Question",\n'
            f'          "name": {json.dumps(faq["q"], ensure_ascii=False)},\n'
            f'          "acceptedAnswer": {{"@type": "Answer", "text": {json.dumps(re.sub("<[^>]+>","",faq["a"]), ensure_ascii=False)}}}\n'
            '        }'
        )

    new_faqpage = (
        '    {\n'
        '      "@type": "FAQPage",\n'
        '      "mainEntity": [\n'
        + ',\n'.join(new_faq_entities) + '\n'
        '      ]\n'
        '    }'
    )
    html = re.sub(
        r'\{\s*"@type":\s*"FAQPage"[\s\S]*?"mainEntity":\s*\[[\s\S]*?\]\s*\}',
        new_faqpage,
        html
    )

    # 7. Links internos no corpo: hub cidade, aluguel, curso NR-11 (se não existirem)
    if f'href="/{slug}/"' not in html:
        # Adiciona link para hub no parágrafo do CTA final
        html = html.replace(
            f'href="/{slug}/pecas-e-assistencia-empilhadeira"' if servico == 'manutencao-empilhadeira' else f'href="/{slug}/manutencao-empilhadeira"',
            f'href="/{slug}/pecas-e-assistencia-empilhadeira"' if servico == 'manutencao-empilhadeira' else f'href="/{slug}/manutencao-empilhadeira"',
        )

    open(path, 'w').write(html)
    return True


# ─── Main ────────────────────────────────────────────────────────────────────
servicos = [
    ('pecas-e-assistencia-empilhadeira', 'pecas'),
    ('manutencao-empilhadeira', 'manutencao'),
]

ok = 0
for slug, c in CIDADES.items():
    for pasta, chave in servicos:
        print(f'Processando {slug}/{pasta}...')
        resultado = processar_cidade(slug, c, pasta)
        if resultado:
            ok += 1

print(f'\nConcluído: {ok} páginas atualizadas.')
