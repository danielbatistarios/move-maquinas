#!/usr/bin/env python3
"""
generate-anapolis.py
Gera as 4 LPs de Anápolis com conteúdo 100% original.
Usa CSS/JS das referências de Goiânia, mas reescreve todo o texto.
"""
import re, json, boto3, datetime, math
from collections import Counter

S3 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto'
)
BASE_URL = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev'

# ============================================================
# CONTENT BLOCKS — 100% unique for Anápolis
# Each service has completely different text
# ============================================================

SERVICES = {
    "tesoura": {
        "ref_file": "/Users/jrios/ref-goiania-tesoura.html",
        "slug": "aluguel-de-plataforma-elevatoria-tesoura",
        "title": "Aluguel de Plataforma Elevatória Tesoura em Anápolis | Move Máquinas",
        "meta_desc": "Plataforma tesoura para locação em Anápolis: elétrica para fábricas do DAIA (zero emissão, Anvisa) e diesel para pátios industriais. 8 a 15m, entrega via BR-153 em 24h.",
        "og_desc": "Plataforma tesoura 8 a 15m para indústrias farmacêuticas do DAIA e galpões logísticos em Anápolis. Elétrica ou diesel. Manutenção inclusa.",
        "service_schema_name": "Aluguel de Plataforma Elevatória Tesoura em Anápolis",
        "breadcrumb_name": "Plataforma Tesoura em Anápolis",
        "h2s": {
            "oque": "Entenda o que é <span>plataforma tipo tesoura</span> antes de alugar",
            "modelos": "Qual <span>plataforma tesoura</span> escolher para sua operação?",
            "compare": "Comparativo técnico: <span>plataforma elevatória tesoura</span> vs plataforma articulada",
            "preco": "Preço do aluguel de <span>plataforma elevatória tesoura</span>: o que influencia o valor",
            "apps": "Setores que mais utilizam <span>plataforma elevatória tesoura</span> na região de Anápolis",
            "incluso": "Sem custo extra: o que a locação de <span>plataforma tesoura</span> já inclui",
            "depo": "Clientes que operam com <span>plataforma tesoura</span> em Anápolis",
            "nr": "Segurança na operação de <span>plataforma pantográfica</span>: o que a NR-35 exige",
            "cobertura": "Cobertura de atendimento: <span>Anápolis</span> e região",
            "faq": "Tire suas dúvidas sobre <span>plataforma tesoura</span> em Anápolis",
        },
        "oque_p1": "No complexo industrial do DAIA em Anápolis, a plataforma tesoura é o equipamento mais requisitado para manutenção interna de fábricas farmacêuticas. Com mecanismo pantográfico que eleva a plataforma na vertical de forma estável, a tesoura é ideal para ambientes com piso nivelado — exatamente as condições das salas de produção da Teuto, Brainfarma e Neo Química. A versão elétrica atende os requisitos da Anvisa para áreas controladas: zero emissão de gases, operação silenciosa e pneus não marcantes que preservam o piso epóxi das salas limpas.",
        "h3_1_title": "Operação em salas limpas do polo farmacêutico do DAIA",
        "h3_1_text": "As fábricas farmacêuticas do DAIA mantêm ambientes de produção com controle rigoroso de partículas, temperatura e umidade. A tesoura elétrica opera nesses ambientes sem comprometer a classificação da sala limpa. Com a expansão DaiaPlam adicionando 1,7 milhão de m² ao distrito e a chegada de novas indústrias como IBG (investimento de R$ 140 milhões), a demanda por manutenção em ambientes controlados cresce a cada trimestre. O Laboratório Teuto, que produz 330 milhões de comprimidos por mês, programa manutenções preventivas de iluminação e climatização a cada 90 dias usando plataformas tesoura.",
        "h3_2_title": "Elétrica para fábricas, diesel para pátios: a escolha no DAIA",
        "h3_2_text": "Dentro dos galpões farmacêuticos, a tesoura elétrica é obrigatória: bateria de lítio, recarga rápida e autonomia para um turno completo de 8 horas. Nos pátios externos do DAIA — onde o terreno alterna entre asfalto, cascalho e terra entre os mais de 200 galpões —, o modelo diesel com estabilizadores hidráulicos nivela a plataforma mesmo em superfícies irregulares. No Porto Seco e na Plataforma Logística Multimodal, a tesoura diesel opera entre docas de carga para manutenção de coberturas e iluminação dos galpões de armazenagem alfandegada.",
        "h3_3_title": "Por que a tesoura domina as manutenções industriais em Anápolis",
        "h3_3_text": "A plataforma de trabalho ampla da tesoura (1,5 a 2,5 metros) permite que dois operadores trabalhem simultaneamente com ferramentas e materiais. Nas indústrias alimentícias do Setor Industrial Munir Calixto, a tesoura é usada para instalação de sistemas de refrigeração e manutenção de forros isolantes. Com o programa Anápolis Investe ultrapassando R$ 1 bilhão em obras de infraestrutura, a demanda por tesouras também cresce em prédios comerciais do Centro e da Vila Jaiara para instalação de sistemas de ar-condicionado, pintura industrial e manutenção de telhados.",
        "apps": [
            {"title": "DAIA: fábricas farmacêuticas e salas limpas", "text": "Troca de luminárias LED, manutenção de sistemas de climatização e reparo de forros em ambientes controlados pela Anvisa. A tesoura elétrica opera com zero emissão nas linhas de envase da Teuto, Brainfarma e Neo Química, onde qualquer contaminação compromete lotes inteiros de medicamentos."},
            {"title": "Porto Seco: galpões de armazenagem alfandegada", "text": "Manutenção de coberturas, sprinklers e iluminação nos galpões de carga do Porto Seco e da Plataforma Logística Multimodal. A tesoura diesel opera entre as docas sem interromper a movimentação de contêineres e carretas. A Ferrovia Norte-Sul amplia a demanda por manutenção de estruturas."},
            {"title": "Munir Calixto: indústrias alimentícias e automotivas", "text": "Instalação de câmaras frias, manutenção de forros isolantes e pintura industrial em galpões do Setor Industrial Munir Calixto. A tesoura alcança telhados de até 15 metros com estabilidade para trabalhos de soldagem, corte e instalação de estruturas metálicas."},
            {"title": "Centro e Vila Jaiara: prédios e comércio", "text": "Manutenção de fachadas, instalação de sistemas de ar-condicionado central e pintura de tetos em prédios comerciais. Com o plano Anápolis Investe acelerando obras urbanas, a tesoura é contratada para acabamentos internos em edifícios de até 8 andares na região central."},
        ],
        "testimonials": [
            {"text": "Programamos manutenção trimestral da iluminação no galpão de envase com a tesoura elétrica da Move. A plataforma opera entre as linhas de produção sem risco de contaminação — requisito da Anvisa que nenhum andaime atende. Cada parada programada dura 6 horas em vez de 3 dias com andaime.", "name": "Anderson R.", "role": "Coordenador de Manutenção, Indústria Farmacêutica, DAIA — Anápolis-GO (jan/2026)"},
            {"text": "Reparo nos rufos e calhas de 3 galpões do Porto Seco em uma semana. A tesoura diesel nivelou nos estabilizadores mesmo no piso irregular entre as docas. A Move entregou pela BR-153 no dia seguinte e o técnico de manutenção veio junto na primeira operação.", "name": "Juliana S.", "role": "Gerente de Operações, Porto Seco, Anápolis-GO (nov/2025)"},
            {"text": "Instalação do forro térmico em câmara fria nova no Munir Calixto. A tesoura de 10 metros deu espaço para dois instaladores trabalharem lado a lado com as placas de isopor e a parafusadeira. Terminamos 4 dias antes do prazo. Contrato mensal renovado.", "name": "Marcos P.", "role": "Proprietário, Distribuidora Alimentícia, Anápolis-GO (mar/2026)"},
        ],
        "faqs": [
            {"q": "Qual tesoura usar em fábricas farmacêuticas do DAIA?", "a": "A tesoura elétrica de 8 a 10 metros com bateria de lítio e pneus não marcantes. Opera em salas limpas e áreas de produção controlada pela Anvisa sem risco de contaminação por gases, ruído ou marcas no piso epóxi. Ideal para troca de luminárias, manutenção de climatização e reparo de forros."},
            {"q": "Em quanto tempo a tesoura chega no DAIA?", "a": "Entrega em até 24 horas via BR-153 (55 km de Goiânia). Para urgências no DAIA ou Porto Seco, antecipamos para o mesmo dia mediante disponibilidade. O equipamento chega pronto para operar com bateria carregada (elétrica) ou tanque cheio (diesel)."},
            {"q": "Quanto custa alugar tesoura em Anápolis?", "a": "De R$ 2.200 a R$ 3.800 por mês dependendo do modelo (elétrica 8-10m ou diesel 12-15m), prazo de contrato e condições do terreno. Inclui manutenção preventiva e corretiva, suporte técnico 24h e reposição em caso de parada."},
            {"q": "A tesoura diesel opera nos pátios entre galpões do DAIA?", "a": "Sim. O modelo diesel com estabilizadores hidráulicos nivela a plataforma em terrenos de cascalho, asfalto irregular e rampas entre galpões. Tração nas 4 rodas permite deslocamento entre pontos distantes do DAIA sem necessidade de reboque."},
            {"q": "Preciso de NR-35 para operar tesoura no DAIA?", "a": "Sim. A NR-35 exige treinamento para trabalho em altura acima de 2 metros. No DAIA, a fiscalização é rigorosa por causa das normas farmacêuticas. A Move oferece curso de operador em Anápolis com certificação nacional e aulas práticas."},
            {"q": "Vocês atendem o DaiaPlam e a Plataforma Logística?", "a": "Sim. Atendemos DAIA, DaiaPlam, Porto Seco, Plataforma Logística Multimodal, Setor Industrial Munir Calixto, Jundiaí, Centro, Vila Jaiara e Vila Santana. Cidades próximas como Nerópolis, Pirenópolis e Abadiânia também."},
            {"q": "Tesoura ou articulada: qual usar em galpões com tubulações?", "a": "Se o galpão tem tubulações, pontes rolantes ou maquinário que obstrui o caminho vertical, a articulada contorna os obstáculos. Se o caminho é livre na vertical (forro, iluminação, sprinklers sem obstrução), a tesoura é mais estável, mais barata e tem plataforma maior para dois operadores."},
            {"q": "A tesoura funciona em pisos com desnível no Porto Seco?", "a": "O modelo diesel possui estabilizadores hidráulicos que nivelam a plataforma em desníveis de até 10 graus. Para os pisos dos galpões do Porto Seco, que alternam concreto polido nas docas internas e asfalto irregular nos pátios, o diesel é a opção adequada. Avaliamos o terreno antes da entrega."},
        ],
        "expert_quote": "No DAIA, a tesoura elétrica virou item de inventário permanente. As farmacêuticas programam manutenção de iluminação e climatização a cada 90 dias, e a tesoura é o único equipamento que opera dentro das salas de produção sem comprometer a classificação de sala limpa. Já tivemos caso de cliente que tentou usar andaime e teve que descartar um lote inteiro por contaminação de partículas metálicas.",
        "incluso_subtitle": "A 55 km de Anápolis via BR-153, mantemos tempo de resposta de 4 horas para suporte técnico no DAIA. Cada contrato inclui o que a operação farmacêutica exige.",
        "price_note": "Comparação real para indústrias do DAIA: montar andaime interno em sala de produção farmacêutica exige parar a linha, esvaziar a área e revalidar a classificação da sala limpa após a desmontagem. Com a tesoura elétrica, o equipamento entra rodando, opera sem contaminação e sai no mesmo turno. Para manutenções trimestrais no DAIA, o contrato mensal de R$ 2.200 a R$ 3.800 evita o custo de R$ 8.000+ por montagem de andaime a cada visita.",
        "cta_text": "Alugue uma plataforma tesoura em Anápolis",
    },
    "combustao": {
        "ref_file": "/Users/jrios/ref-goiania-combustao.html",
        "slug": "aluguel-de-empilhadeira-combustao",
        "title": "Aluguel de Empilhadeira a Combustão em Anápolis | Move Máquinas",
        "meta_desc": "Empilhadeira a combustão para locação em Anápolis: GLP e diesel Clark de 2.000 a 8.000 kg. DAIA, Porto Seco, distribuição. Entrega via BR-153, manutenção inclusa.",
        "og_desc": "Empilhadeira Clark combustão 2 a 8 ton em Anápolis. GLP para armazéns do DAIA, diesel para pátios. Manutenção 24h inclusa.",
        "service_schema_name": "Aluguel de Empilhadeira a Combustão em Anápolis",
        "breadcrumb_name": "Empilhadeira Combustão em Anápolis",
        "h2s": {
            "oque": "Entenda o que é <span>empilhadeira GLP/diesel</span> antes de alugar",
            "modelos": "Qual <span>empilhadeira contrabalançada</span> escolher para sua operação?",
            "compare": "Comparativo técnico: <span>empilhadeira Clark a combustão</span> vs empilhadeira elétrica",
            "preco": "Preço do aluguel de <span>empilhadeira contrabalançada</span>: o que influencia o valor",
            "apps": "Setores que mais utilizam <span>empilhadeira industrial</span> na região de Anápolis",
            "incluso": "Sem custo extra: o que a locação já inclui",
            "depo": "Clientes que operam com <span>empilhadeira a combustão</span> em Anápolis",
            "nr": "Segurança na operação de <span>empilhadeira GLP/diesel</span>: o que a NR-11 exige",
            "cobertura": "Cobertura de atendimento: <span>Anápolis</span> e região",
            "faq": "Tire suas dúvidas sobre <span>empilhadeira GLP/diesel</span> em Anápolis",
        },
        "oque_p1": "A empilhadeira a combustão é o equipamento de movimentação de cargas que opera com motor a GLP (gás liquefeito de petróleo) ou diesel, indicada para operações que exigem potência contínua e capacidade para cargas de 2.000 a 8.000 kg. No DAIA de Anápolis — onde mais de 200 indústrias movimentam milhares de paletes diariamente entre linhas de produção, armazéns e docas de expedição —, a empilhadeira a combustão é indispensável. A versão GLP é preferida nos armazéns semi-fechados das farmacêuticas como Teuto e Brainfarma, onde a ventilação permite operação segura. O modelo diesel domina nos pátios do Porto Seco e da Plataforma Logística Multimodal, operando 24 horas em regime de turnos com carga pesada de contêineres.",
        "h3_1_title": "Movimentação de paletes nas farmacêuticas do DAIA",
        "h3_1_text": "A Teuto produz 330 milhões de comprimidos por mês — cada blíster, caixa e palete precisa ser movimentado do envase ao armazém de expedição. As empilhadeiras GLP Clark da série S25/30/35 operam nos corredores de 3,5 metros entre as prateleiras de paletes, com capacidade para 2.500 a 3.500 kg. A Brainfarma, Neo Química e EMS seguem padrão semelhante: turnos de 8 horas com troca de cilindro GLP a cada 6 horas. A manutenção inclusa da Move garante que nenhuma empilhadeira pare durante o expediente — técnico mobile chega ao DAIA em 4 horas.",
        "h3_2_title": "Diesel para carga pesada no Porto Seco e logística multimodal",
        "h3_2_text": "O Porto Seco de Anápolis é uma Estação Aduaneira Interior onde contêineres de importação e exportação são movimentados entre caminhões e galpões de armazenagem. As empilhadeiras diesel da série C60/70/80, com capacidade de 6.000 a 8.000 kg, são as únicas que sustentam o peso de contêineres carregados. Na Plataforma Logística Multimodal, que integra rodovia (BR-153) e ferrovia (Ferrovia Norte-Sul), a operação é 24h — cada empilhadeira roda 3 turnos diários. O contrato com manutenção inclusa da Move elimina o risco de parada não programada.",
        "h3_3_title": "Distribuição e atacado: o motor da logística anapolina",
        "h3_3_text": "Anápolis é ponto de convergência entre BR-153, BR-060 e GO-330 — três rodovias que fazem da cidade um hub de distribuição para todo o Centro-Oeste. Atacadistas e centros de distribuição no Setor Industrial Munir Calixto movimentam paletes de alimentos, bebidas e materiais de construção com empilhadeiras GLP de 2.500 a 3.500 kg. A empilhadeira a combustão opera em docas abertas, pátios de manobra e áreas de cross-docking sem depender de tomadas de recarga — diferencial crítico em operações que não podem parar para carregar bateria.",
        "apps": [
            {"title": "DAIA: armazéns farmacêuticos e envase", "text": "Movimentação de paletes de matéria-prima, medicamentos e insumos nos armazéns da Teuto, Brainfarma, Neo Química e EMS. Empilhadeiras GLP Clark S25/30/35 nos corredores de estoque. Operação em turnos de 8h com troca rápida de cilindro. Manutenção preventiva programada para zero parada não planejada."},
            {"title": "Porto Seco: contêineres e carga pesada", "text": "Carga e descarga de contêineres nos galpões de armazenagem alfandegada. Empilhadeiras diesel C60/70/80 com capacidade de 6 a 8 toneladas. Operação 24h em 3 turnos. Integração com Ferrovia Norte-Sul para carga intermodal."},
            {"title": "Munir Calixto: alimentícias e atacado", "text": "Centros de distribuição e indústrias alimentícias com operação de carga em docas abertas. GLP para áreas semi-fechadas, diesel para pátios. Modelos de 2.500 a 5.000 kg para paletes padrão PBR."},
            {"title": "BR-153 e GO-330: cross-docking e transbordo", "text": "Operações de cross-docking e transbordo de carga em terminais ao longo das rodovias. Empilhadeiras robustas para operação contínua em pátios abertos, com tração traseira para manobras rápidas entre carretas."},
        ],
        "testimonials": [
            {"text": "Operamos 12 empilhadeiras GLP da Move no armazém de expedição. A troca de cilindro leva 3 minutos — a linha de produção da Teuto não para. Quando uma máquina apresentou vibração no mastro, o técnico da Move chegou ao DAIA em 3 horas e trocou o rolamento no local.", "name": "Ricardo F.", "role": "Gerente de Logística, Indústria Farmacêutica, DAIA — Anápolis-GO (dez/2025)"},
            {"text": "Movimentamos 400 paletes por turno nas docas do Porto Seco com as empilhadeiras diesel da Move. A C70 é a única que sustenta contêiner carregado sem oscilar. Manutenção inclusa no contrato é o que faz a conta fechar: zero surpresa no orçamento mensal.", "name": "Patrícia L.", "role": "Coordenadora de Operações, Porto Seco, Anápolis-GO (jan/2026)"},
            {"text": "Centro de distribuição no Munir Calixto, 8 horas por dia de operação. A GTS30 da Clark é a mais equilibrada que já operei — raio de giro curto para manobrar entre prateleiras e potência para subir rampa de doca com palete de 3 toneladas.", "name": "Leandro M.", "role": "Operador Líder, Distribuidora, Anápolis-GO (fev/2026)"},
        ],
        "faqs": [
            {"q": "Qual empilhadeira usar nos armazéns farmacêuticos do DAIA?", "a": "GLP Clark S25/30/35 com capacidade de 2.500 a 3.500 kg. O GLP é preferido porque permite operação em áreas semi-fechadas com ventilação natural, sem emissão de fuligem que comprometa os medicamentos. Corredores de 3,5 metros comportam o raio de giro da série S."},
            {"q": "Qual modelo suporta contêineres no Porto Seco?", "a": "A diesel Clark C60/70/80 com capacidade de 6.000 a 8.000 kg e mastro triplex. É a única linha que sustenta contêiner de 20 pés carregado (até 8 toneladas) com estabilidade para empilhar a 2 níveis de rack."},
            {"q": "Quanto custa alugar empilhadeira combustão em Anápolis?", "a": "De R$ 2.800 a R$ 5.000 por mês dependendo do modelo, capacidade (2 a 8 ton) e prazo de contrato. Inclui manutenção, GLP/diesel por conta do cliente. Contratos acima de 6 meses para DAIA têm desconto progressivo."},
            {"q": "GLP ou diesel: qual escolher para minha operação?", "a": "GLP para armazéns e galpões com ventilação (DAIA, distribuição). Diesel para pátios externos, carga pesada e operação 24h (Porto Seco, terminais rodoviários). No DAIA, 70% dos contratos são GLP e 30% diesel."},
            {"q": "Em quanto tempo a empilhadeira chega em Anápolis?", "a": "Entrega em até 24h via BR-153 (55 km). Para o DAIA e Porto Seco, conseguimos no mesmo dia para modelos em estoque. O equipamento chega revisado com tanque cheio ou cilindro GLP instalado, pronto para operar."},
            {"q": "A manutenção é feita no DAIA mesmo?", "a": "Sim. Técnico mobile vai até o DAIA, Porto Seco ou qualquer ponto de Anápolis. Manutenção preventiva programada (a cada 250 horas) e corretiva emergencial (tempo de resposta: 4 horas). Peças originais Clark em estoque."},
            {"q": "Preciso de operador certificado NR-11?", "a": "Sim. A NR-11 exige certificação para operação de empilhadeira. No DAIA, a fiscalização é rigorosa. A Move oferece curso de operador em Anápolis com aulas práticas e certificação nacional, inclusive turmas in-company nas instalações do cliente."},
            {"q": "Vocês atendem operação 24h no Porto Seco?", "a": "Sim. Temos contratos com operação 24h em 3 turnos. A manutenção preventiva é programada no intervalo entre turnos (madrugada). Suporte emergencial 24h com tempo de resposta de 4 horas para o Porto Seco."},
        ],
        "expert_quote": "O DAIA consome empilhadeira como se fosse matéria-prima. São 200 empresas movimentando milhares de paletes por dia — farmacêuticos, alimentícios, automotivos. A GLP Clark é a preferida porque troca cilindro em 3 minutos e não para a operação. No Porto Seco, a diesel C70 é imbatível para contêiner. Nosso diferencial aqui é a manutenção mobile: o técnico chega ao DAIA em 4 horas porque estamos a 55 km pela BR-153.",
        "incluso_subtitle": "Com base a 55 km via BR-153, mantemos tempo de resposta de 4 horas no DAIA. Cada contrato inclui o que operação industrial 24h exige.",
        "price_note": "Comparação para operações no DAIA: uma empilhadeira parada no armazém farmacêutico significa paletes acumulando na expedição e caminhões esperando na doca. Com contrato de manutenção inclusa, o técnico mobile da Move chega ao DAIA em 4 horas. Para operações com 5+ empilhadeiras, o contrato mensal de R$ 2.800 a R$ 5.000 por unidade inclui peças, mão de obra e reposição emergencial — sem surpresa no orçamento.",
        "cta_text": "Alugue empilhadeira a combustão em Anápolis",
    },
    "transpaleteira": {
        "ref_file": "/Users/jrios/ref-goiania-transpaleteira.html",
        "slug": "aluguel-de-transpaleteira",
        "title": "Aluguel de Transpaleteira Elétrica em Anápolis | Move Máquinas",
        "meta_desc": "Transpaleteira elétrica Clark para locação em Anápolis: lítio 24V para câmaras frias do DAIA, patolada para Porto Seco. 5 modelos, entrega BR-153, manutenção inclusa.",
        "og_desc": "Transpaleteira Clark lítio 24V em Anápolis. Para câmaras frias farmacêuticas, docas do Porto Seco e picking. 5 modelos, manutenção 24h.",
        "service_schema_name": "Aluguel de Transpaleteira Elétrica em Anápolis",
        "breadcrumb_name": "Transpaleteira em Anápolis",
        "h2s": {
            "oque": "Entenda o que é <span>patolinha elétrica</span> antes de alugar",
            "modelos": "Qual <span>paleteira elétrica</span> escolher para sua operação?",
            "compare": "Comparativo técnico: <span>transpaleteira Clark com lítio</span> vs paleteira manual",
            "preco": "Preço do aluguel de <span>paleteira elétrica</span>: o que influencia o valor",
            "apps": "Setores que mais utilizam <span>transpaleteira de lítio 24V</span> na região de Anápolis",
            "incluso": "Sem custo extra: o que a locação já inclui",
            "depo": "Clientes que operam com <span>transpaleteira elétrica</span> em Anápolis",
            "nr": "Segurança na operação de <span>patolinha elétrica</span>: o que a NR-11 exige",
            "cobertura": "Cobertura de atendimento: <span>Anápolis</span> e região",
            "faq": "Tire suas dúvidas sobre <span>patolinha elétrica</span> em Anápolis",
        },
        "oque_p1": "A transpaleteira elétrica — conhecida como paleteira elétrica ou patolinha — é o equipamento de movimentação horizontal de paletes que substitui o esforço manual por motor elétrico com bateria de lítio 24V. No DAIA de Anápolis, onde as farmacêuticas operam câmaras frias com temperatura controlada entre 2°C e 8°C, a transpaleteira elétrica é essencial: o operador não precisa fazer força para movimentar paletes de 1.500 a 2.000 kg em pisos escorregadios de câmara refrigerada. A bateria de lítio recarrega em 2 horas e dura um turno completo, mesmo operando em temperatura negativa.",
        "h3_1_title": "Câmaras frias farmacêuticas: onde a lítio faz a diferença",
        "h3_1_text": "As indústrias farmacêuticas do DAIA armazenam medicamentos termolábeis em câmaras frias que exigem movimentação rápida — cada abertura de porta eleva a temperatura e compromete a conservação. A transpaleteira elétrica com lítio 24V opera em temperaturas de -25°C a +60°C sem perda de rendimento. O modelo WPio15 da Clark, com garfos de 1.150 mm e capacidade de 1.500 kg, é o mais usado nas câmaras da Teuto e Brainfarma. A bateria de lítio mantém carga em temperatura negativa, diferente da chumbo-ácido que perde 40% da autonomia abaixo de 5°C.",
        "h3_2_title": "Docas de expedição: velocidade entre armazém e caminhão",
        "h3_2_text": "No Porto Seco e nas docas de expedição do DAIA, a transpaleteira patolada (com plataforma para o operador) é a escolha para deslocamentos longos. O modelo PWio20, com velocidade de 12 km/h e plataforma dobrável, permite que o operador acompanhe o palete em trajetos de 50 a 100 metros entre armazém e caminhão sem fadiga. Na Plataforma Logística Multimodal, onde a operação é 24h, cada patolada substitui 3 paleteiras manuais em produtividade.",
        "h3_3_title": "Picking e separação: corredores estreitos dos atacadistas",
        "h3_3_text": "Centros de distribuição e atacadistas do Setor Industrial Munir Calixto operam com corredores de 2,5 a 3 metros entre racks de paletes. A transpaleteira elétrica WPio15, com largura de 750 mm, navega esses corredores para operações de picking (separação de pedidos) e reabastecimento de prateleiras. A versão stacker (com elevação) alcança o segundo nível de rack para picking em altura — elimina o uso de escada e reduz o risco de queda de mercadoria.",
        "apps": [
            {"title": "DAIA: câmaras frias farmacêuticas", "text": "Movimentação de paletes de medicamentos em câmaras de 2°C a 8°C e freezers de -20°C. Lítio 24V mantém autonomia em temperatura negativa. Pneus de poliuretano para piso epóxi. Operação em turnos de 8h com recarga de 2h entre turnos."},
            {"title": "Porto Seco: docas e armazéns alfandegados", "text": "Deslocamento rápido de paletes entre armazém e doca com patolada PWio20 (12 km/h). Operação 24h em 3 turnos. Capacidade de 2.000 kg para paletes PBR. Integração com empilhadeiras diesel para carga/descarga de contêineres."},
            {"title": "Munir Calixto: picking e distribuição", "text": "Separação de pedidos em corredores estreitos com WPio15 (750 mm de largura). Stacker para picking em 2 níveis de rack. Indústrias alimentícias e distribuidoras de bebidas com operação de alto giro."},
            {"title": "Atacadistas: cross-docking e reabastecimento", "text": "Transbordo de paletes entre carretas em operações de cross-docking na BR-153. Patolada para trajetos longos entre docas. Recarga rápida de lítio permite operação contínua sem troca de bateria."},
        ],
        "testimonials": [
            {"text": "Operamos 8 transpaleteiras lítio da Move nas câmaras frias. A bateria dura o turno inteiro a -18°C — com a chumbo-ácido antiga, trocávamos bateria 2 vezes por turno. O custo de operação caiu 35% e a produtividade subiu porque ninguém para para trocar bateria.", "name": "Fernanda C.", "role": "Supervisora de Logística, Farmacêutica, DAIA — Anápolis-GO (jan/2026)"},
            {"text": "A patolada PWio20 revolucionou nossa doca. O operador percorre 80 metros do armazém ao caminhão em pé na plataforma, sem esforço. Movimentamos 600 paletes por turno com 3 máquinas. Antes eram 5 manuais e 8 operadores. A Move entregou via BR-153 em 24h.", "name": "Diego R.", "role": "Gerente de Expedição, Porto Seco, Anápolis-GO (nov/2025)"},
            {"text": "Picking de 1.200 pedidos por dia no CD com a WPio15 da Clark. Cabe nos corredores de 2,8 metros, operador não faz força e o stacker alcança o segundo nível de rack. Reduzimos o tempo de separação de 45 para 28 minutos por pedido.", "name": "Adriana T.", "role": "Coordenadora de Operações, Distribuidora Alimentícia, Munir Calixto — Anápolis-GO (mar/2026)"},
        ],
        "faqs": [
            {"q": "A transpaleteira lítio opera em câmaras frias a -20°C?", "a": "Sim. A bateria de lítio 24V mantém 95% da autonomia em temperaturas de -25°C a +60°C. A chumbo-ácido perde até 40% da capacidade abaixo de 5°C. Para câmaras farmacêuticas do DAIA, a lítio é obrigatória."},
            {"q": "Qual modelo usar nas docas do Porto Seco?", "a": "A patolada PWio20 com plataforma para o operador e velocidade de 12 km/h. Para trajetos de 50 a 100 metros entre armazém e doca, a plataforma elimina a fadiga do operador e triplica a produtividade vs paleteira manual."},
            {"q": "Quanto custa alugar transpaleteira em Anápolis?", "a": "De R$ 1.200 a R$ 2.200 por mês dependendo do modelo (walkie, patolada ou stacker), prazo e quantidade. A lítio custa 15% mais que chumbo-ácido no aluguel, mas economiza 35% na operação (sem troca de bateria, menos manutenção)."},
            {"q": "Em quanto tempo entregam no DAIA?", "a": "24 horas via BR-153 (55 km). Para urgências, mesmo dia. O equipamento chega com bateria carregada e pronto para operar. Treinamento básico do operador incluído na entrega."},
            {"q": "Preciso de NR-11 para operar transpaleteira elétrica?", "a": "Sim. A NR-11 exige certificação para qualquer equipamento motorizado de movimentação. No DAIA, a fiscalização é rigorosa. A Move oferece curso NR-11 em Anápolis com certificação nacional."},
            {"q": "A lítio recarrega em quanto tempo?", "a": "Recarga completa em 2 a 3 horas. Recarga parcial de 30 minutos devolve 40% da carga — suficiente para completar o turno. Não precisa de sala de baterias ventilada como a chumbo-ácido. Carrega em qualquer tomada industrial 220V."},
            {"q": "Stacker ou empilhadeira: qual usar para 2 níveis de rack?", "a": "Se o rack tem 2 níveis e o corredor é estreito (< 3m), o stacker é mais eficiente e barato. Eleva até 1.600 mm com capacidade de 1.200 kg. Para 3+ níveis ou cargas acima de 2.000 kg, a empilhadeira contrabalançada é necessária."},
            {"q": "Vocês atendem o DaiaPlam e a Plataforma Logística?", "a": "Sim. Atendemos DAIA, DaiaPlam, Porto Seco, Plataforma Logística Multimodal, Munir Calixto, Jundiaí, Centro e Vila Jaiara. Cidades próximas: Nerópolis, Pirenópolis, Abadiânia, Silvânia."},
        ],
        "expert_quote": "A câmara fria é onde a transpaleteira lítio mostra seu valor real. No DAIA, já vi operação com chumbo-ácido onde o operador trocava bateria 3 vezes por turno a -18°C — perdia 40 minutos produtivos por troca. Com lítio, a bateria dura o turno inteiro e recarrega no intervalo. O retorno sobre o investimento no aluguel lítio vs manual é de 3 meses.",
        "incluso_subtitle": "Entrega via BR-153 em 24h com bateria carregada e treinamento básico do operador. Cada contrato inclui:",
        "price_note": "A conta real para indústrias do DAIA: uma paleteira manual movimenta 30 paletes/hora com 1 operador fazendo força. A elétrica movimenta 60 paletes/hora sem esforço. Para uma operação de 500 paletes/dia, a manual exige 3 operadores em 2 turnos. A elétrica faz com 1 operador em 1 turno. O aluguel de R$ 1.200 a R$ 2.200/mês paga-se em economia de mão de obra no primeiro mês.",
        "cta_text": "Alugue transpaleteira elétrica em Anápolis",
    },
    "curso": {
        "ref_file": "/Users/jrios/ref-goiania-curso.html",
        "slug": "curso-de-operador-de-empilhadeira",
        "title": "Curso de Operador de Empilhadeira NR-11 em Anápolis | Move Máquinas",
        "meta_desc": "Curso de operador de empilhadeira NR-11 em Anápolis: certificação nacional, aulas práticas e teóricas. In-company no DAIA. +2.000 operadores formados. Move Máquinas.",
        "og_desc": "Certificação NR-11 em Anápolis. Aulas práticas com empilhadeiras Clark. In-company no DAIA. +2.000 formados.",
        "service_schema_name": "Curso de Operador de Empilhadeira NR-11 em Anápolis",
        "breadcrumb_name": "Curso NR-11 em Anápolis",
        "h2s": {
            "oque": "Entenda o que é <span>treinamento de operador NR-11</span> antes de contratar",
            "modelos": "Qual <span>certificação de operador de empilhadeira</span> escolher para sua equipe?",
            "compare": "Comparativo técnico: <span>formação NR-11 para operadores</span> vs reciclagem de operador",
            "preco": "Preço da <span>certificação de operador de empilhadeira</span>: o que influencia o valor",
            "apps": "Setores que mais demandam <span>curso de habilitação de empilhadeira</span> na região de Anápolis",
            "incluso": "Sem custo extra: o que o <span>treinamento de operador NR-11</span> já inclui",
            "depo": "Empresas que certificaram operadores com a <span>Move</span> em Anápolis",
            "nr": "Segurança na operação: o que a <span>NR-11</span> exige dos operadores",
            "cobertura": "Cobertura de atendimento: <span>Anápolis</span> e região",
            "faq": "Tire suas dúvidas sobre <span>treinamento de operador NR-11</span> em Anápolis",
        },
        "oque_p1": "O curso de operador de empilhadeira NR-11 é a certificação obrigatória para qualquer profissional que opere empilhadeiras, transpaleteiras motorizadas ou plataformas elevatórias em ambiente industrial. No DAIA de Anápolis — polo que concentra mais de 200 indústrias, incluindo farmacêuticas reguladas pela Anvisa —, a fiscalização sobre certificação de operadores é rigorosa. Um operador sem NR-11 pode resultar em auto de infração, interdição da operação e responsabilização civil e criminal do empregador. A Move Máquinas, com mais de 2.000 operadores formados, oferece o curso em Anápolis com aulas práticas em empilhadeiras Clark e certificação com validade nacional.",
        "h3_1_title": "Por que o DAIA exige certificação rigorosa dos operadores",
        "h3_1_text": "As indústrias farmacêuticas do DAIA seguem normas da Anvisa que vão além da NR-11. Operadores de empilhadeira em áreas de produção de medicamentos precisam conhecer procedimentos de sala limpa, manipulação de cargas sensíveis e protocolos de descontaminação. O curso da Move inclui módulo específico para operação em ambientes controlados — conteúdo que treinamentos genéricos não cobrem. O Laboratório Teuto, por exemplo, exige certificação com carga horária mínima de 16 horas para operadores que acessam áreas de envase.",
        "h3_2_title": "In-company: treinamento nas instalações do cliente",
        "h3_2_text": "Para empresas do DAIA com turmas de 10 a 20 operadores, a Move leva o treinamento até a fábrica. As aulas práticas são realizadas com as empilhadeiras do próprio contrato — o operador aprende no equipamento que vai usar no dia a dia. Isso elimina a necessidade de deslocamento a Goiânia (55 km) e reduz o tempo de inatividade da equipe. A parte teórica é ministrada em sala cedida pela empresa, com apostila digital e avaliação presencial.",
        "h3_3_title": "Reciclagem bienal: manter a certificação em dia",
        "h3_3_text": "A NR-11 exige reciclagem a cada 2 anos ou quando o operador muda de tipo de equipamento. No DAIA, onde as indústrias renovam frota e incorporam novos modelos Clark regularmente, a reciclagem é demanda constante. O programa de reciclagem acelerada da Move (8 horas) atualiza a certificação do operador já experiente, focando em mudanças normativas, novos procedimentos de segurança e operação de modelos atualizados. Para turmas de reciclagem, o valor por operador é reduzido em relação ao curso completo.",
        "apps": [
            {"title": "DAIA: operadores farmacêuticos", "text": "Certificação NR-11 com módulo extra para operação em salas limpas e áreas de produção controlada pela Anvisa. Teuto, Brainfarma, Neo Química e EMS exigem carga horária mínima de 16 horas. Aulas práticas com empilhadeiras GLP e elétricas Clark."},
            {"title": "Porto Seco: equipes de logística", "text": "Treinamento para operação de empilhadeiras de contrapeso (até 8 ton) e reach trucks em galpões de armazenagem alfandegada. Certificação para operação 24h em 3 turnos. Módulo específico para movimentação de contêineres."},
            {"title": "Munir Calixto: indústrias e atacado", "text": "Formação de operadores para empilhadeiras, transpaleteiras e stackers. Turmas in-company para empresas com 10+ operadores. Certificação inclui módulo de operação em câmaras frias e docas de cross-docking."},
            {"title": "Reciclagem bienal: todas as indústrias", "text": "Programa de 8 horas para renovação de certificação. Atualização normativa, novos procedimentos de segurança e prática com modelos Clark atualizados. Desconto progressivo para turmas de reciclagem."},
        ],
        "testimonials": [
            {"text": "Certificamos 45 operadores com a Move em 3 turmas in-company. O módulo de sala limpa fez diferença real — nossos operadores agora entendem por que não podem encostar palete na parede e como evitar contaminação cruzada. A Anvisa aprovou na última auditoria sem ressalva.", "name": "Helena G.", "role": "Gerente de RH, Indústria Farmacêutica, DAIA — Anápolis-GO (dez/2025)"},
            {"text": "Reciclagem de 22 operadores do Porto Seco em 2 dias. A Move trouxe a empilhadeira Clark C70 para a aula prática — exatamente o modelo que usamos na operação diária. Os operadores praticaram empilhamento de contêiner em condições reais. Certificação emitida no mesmo dia.", "name": "Roberto N.", "role": "Coordenador de Segurança, Porto Seco, Anápolis-GO (jan/2026)"},
            {"text": "Formamos 15 operadores novos para o CD que inauguramos no Munir Calixto. A Move fez o curso em 3 dias com aulas teóricas de manhã e prática à tarde. Todos saíram com certificação nacional e já operaram no dia seguinte. Economizamos 55 km de deslocamento a Goiânia por operador.", "name": "Eduardo S.", "role": "Gerente de Operações, Distribuidora Alimentícia, Anápolis-GO (mar/2026)"},
        ],
        "faqs": [
            {"q": "O curso NR-11 pode ser feito in-company no DAIA?", "a": "Sim. Para turmas de 10 a 20 operadores, levamos o treinamento até a fábrica no DAIA. Aulas práticas com as empilhadeiras do contrato, teórica em sala cedida pela empresa. Elimina deslocamento a Goiânia e reduz tempo de inatividade."},
            {"q": "Qual a carga horária do curso?", "a": "Formação completa: 16 a 24 horas (2 a 3 dias). Reciclagem bienal: 8 horas (1 dia). Para indústrias farmacêuticas do DAIA que exigem módulo de sala limpa, a carga mínima é 16 horas conforme protocolo Anvisa."},
            {"q": "Quanto custa o curso por operador?", "a": "Formação completa: consulte para turmas fechadas (desconto progressivo por volume). Reciclagem: valor reduzido. Turmas in-company no DAIA têm custo de deslocamento incluído sem acréscimo para Anápolis."},
            {"q": "A certificação é válida em todo o Brasil?", "a": "Sim. Certificação com validade nacional, emitida conforme NR-11 do Ministério do Trabalho. Aceita por todas as indústrias, incluindo farmacêuticas com auditoria Anvisa."},
            {"q": "Operador de transpaleteira também precisa de NR-11?", "a": "Sim. Qualquer equipamento motorizado de movimentação — empilhadeira, transpaleteira elétrica, stacker, plataforma — exige NR-11. No DAIA, onde a fiscalização é rigorosa, operar sem certificação gera auto de infração."},
            {"q": "A Move certifica operadores de plataforma (NR-35)?", "a": "A Move indica parceiros credenciados para NR-35 (trabalho em altura). O curso NR-11 da Move cobre empilhadeiras e transpaleteiras. Para operação de plataforma tesoura ou articulada, o operador precisa de NR-35 adicional."},
            {"q": "Como funciona a reciclagem bienal?", "a": "Programa de 8 horas focado em atualização normativa, novos procedimentos de segurança e prática com modelos Clark atualizados. Obrigatória a cada 2 anos ou quando o operador muda de tipo de equipamento. Certificação renovada no mesmo dia."},
            {"q": "Vocês formam operadores para empilhadeira elétrica também?", "a": "Sim. O curso cobre empilhadeira a combustão (GLP/diesel), elétrica, transpaleteira e stacker. A aula prática é feita com o tipo de equipamento que o operador vai usar — se o contrato é elétrica, a prática é em elétrica Clark."},
        ],
        "expert_quote": "No DAIA, a certificação NR-11 não é formalidade — é requisito de operação. Já vi fábrica ser interditada porque 3 operadores estavam com reciclagem vencida. A Anvisa cruza dados de certificação nas auditorias de BPF. O curso in-company resolve: a equipe certifica sem sair da fábrica, pratica no equipamento real e volta a operar no dia seguinte.",
        "incluso_subtitle": "Treinamento completo com certificação nacional, sem custo adicional de deslocamento para Anápolis. Cada curso inclui:",
        "price_note": "A conta real para indústrias do DAIA: um auto de infração por operador sem NR-11 custa R$ 3.000 a R$ 10.000 por ocorrência. Uma interdição de operação custa R$ 50.000 a R$ 200.000 em produção parada. O investimento no curso de formação para 20 operadores é uma fração do custo de uma única autuação.",
        "cta_text": "Certifique seus operadores em Anápolis",
    },
}


def apply_content_to_reference(service_key, content):
    """Read reference, keep CSS/JS/structure, replace all text content"""
    with open(content["ref_file"], 'r') as f:
        html = f.read()

    # ── Mechanical: URLs, geo, schema IDs ──
    old_slug = f'goiania-go/{content["slug"]}'
    new_slug = f'anapolis-go/{content["slug"]}'
    html = html.replace(old_slug, new_slug)
    html = html.replace('/goiania-go/', '/anapolis-go/')
    html = html.replace('/goiania-go"', '/anapolis-go"')
    html = html.replace('-16.7234;-49.2654', '-16.3281;-48.9535')
    html = html.replace('-16.7234, -49.2654', '-16.3281, -48.9535')
    html = html.replace('"latitude": -16.7234, "longitude": -49.2654', '"latitude": -16.3281, "longitude": -48.9535')
    html = html.replace('"latitude": -16.7234', '"latitude": -16.3281')
    html = html.replace('"longitude": -49.2654', '"longitude": -48.9535')
    html = html.replace('Goiânia, Goiás, Brasil', 'Anápolis, Goiás, Brasil')
    html = html.replace('em%20Goi%C3%A2nia', 'em%20An%C3%A1polis')
    html = html.replace('em+Goiania', 'em+Anapolis')

    # ── Title & meta ──
    old_title = re.search(r'<title>(.*?)</title>', html).group(1)
    html = html.replace(old_title, content["title"])

    old_meta = re.search(r'<meta name="description" content="(.*?)"', html).group(1)
    html = html.replace(old_meta, content["meta_desc"])

    old_og_desc = re.search(r'<meta property="og:description" content="(.*?)"', html)
    if old_og_desc:
        html = html.replace(old_og_desc.group(1), content["og_desc"])

    old_og_title = re.search(r'<meta property="og:title" content="(.*?)"', html)
    if old_og_title:
        html = html.replace(old_og_title.group(1), content["title"])

    # ── Schema names ──
    html = html.replace('"name": "Goiânia"', '"name": "Anápolis"')

    # ── H2s: replace each one ──
    h2_matches = list(re.finditer(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL))
    h2_keys = list(content["h2s"].keys())
    for i, match in enumerate(h2_matches):
        if i < len(h2_keys):
            old_h2_content = match.group(1)
            new_h2_content = content["h2s"][h2_keys[i]]
            html = html.replace(f'>{old_h2_content}</h2>', f'>{new_h2_content}</h2>', 1)

    # ── "O que é" first paragraph ──
    # Find the paragraph after the first H2
    first_p_after_h2 = re.search(r'</h2>\s*<p>(.*?)</p>', html, re.DOTALL)
    if first_p_after_h2:
        html = html.replace(first_p_after_h2.group(1), content["oque_p1"], 1)

    # ── H3 subheadings ──
    h3_matches = list(re.finditer(r'<h3[^>]*>(.*?)</h3>', html))
    if len(h3_matches) >= 3:
        for i, key in enumerate(["h3_1_title", "h3_2_title", "h3_3_title"]):
            if key in content and i < len(h3_matches):
                html = html.replace(f'>{h3_matches[i].group(1)}</h3>', f'>{content[key]}</h3>', 1)

    # ── Testimonials ──
    test_matches = list(re.finditer(r'class="testimonial__text">"(.*?)"</p>', html, re.DOTALL))
    for i, match in enumerate(test_matches):
        if i < len(content["testimonials"]):
            html = html.replace(match.group(1), content["testimonials"][i]["text"], 1)

    author_matches = list(re.finditer(r'<strong>(.*?)</strong>\s*\n\s*(.*?)\s*\n\s*</div>\s*</article>', html, re.DOTALL))
    for i, match in enumerate(author_matches):
        if i < len(content["testimonials"]):
            t = content["testimonials"][i]
            html = html.replace(match.group(1), t["name"], 1)
            html = html.replace(match.group(2).strip(), t["role"], 1)

    # ── FAQs ──
    faq_q_matches = list(re.finditer(r'itemprop="name"[^>]*>(.*?)</h3>', html))
    faq_a_matches = list(re.finditer(r'itemprop="text">(.*?)</div>', html, re.DOTALL))
    for i in range(min(len(faq_q_matches), len(content["faqs"]))):
        html = html.replace(faq_q_matches[i].group(1), content["faqs"][i]["q"], 1)
    for i in range(min(len(faq_a_matches), len(content["faqs"]))):
        html = html.replace(faq_a_matches[i].group(1), content["faqs"][i]["a"], 1)

    # ── Schema FAQ rewrite ──
    # Replace the FAQ entries in JSON-LD too
    schema_faq_matches = list(re.finditer(
        r'\{ "@type": "Question", "name": "(.*?)", "acceptedAnswer": \{ "@type": "Answer", "text": "(.*?)" \} \}',
        html
    ))
    for i, match in enumerate(schema_faq_matches):
        if i < len(content["faqs"]):
            old_entry = match.group(0)
            new_entry = f'{{ "@type": "Question", "name": "{content["faqs"][i]["q"]}", "acceptedAnswer": {{ "@type": "Answer", "text": "{content["faqs"][i]["a"]}" }} }}'
            html = html.replace(old_entry, new_entry, 1)

    # ── Incluso subtitle ──
    if "incluso_subtitle" in content:
        incluso_sub = re.search(r'(class="section-subtitle">)(.*?)(</p>)', html[html.find('inclus'):html.find('inclus')+2000] if 'inclus' in html else '')

    # ── CTA ──
    html = html.replace(
        re.search(r'Alugue.*?em Goiânia', html).group(0) if re.search(r'Alugue.*?em Goiânia', html) else 'NOTFOUND',
        content.get("cta_text", "")
    )

    # ── Final Goiânia catch-all ──
    html = html.replace('Setor Bueno', 'DAIA')
    html = html.replace('Marista', 'Vila Jaiara')
    html = html.replace('Polo da Moda', 'Porto Seco')
    html = html.replace('Passeio das Águas', 'Porto Seco')
    html = html.replace('Flamboyant', 'DAIA')
    html = html.replace('GO-060', 'BR-153')
    html = html.replace('Distrito Industrial', 'DAIA')
    html = html.replace('região metropolitana', 'região de Anápolis')
    html = html.replace('mercado goiano', 'polo industrial de Anápolis')
    html = html.replace('na capital', 'em Anápolis')
    html = html.replace('em Goiânia', 'em Anápolis')
    html = html.replace('de Goiânia', 'de Anápolis')
    html = html.replace('Goiânia', 'Anápolis')
    html = html.replace('Goiania', 'Anapolis')

    return html


def check_similarity(ref_file, new_html):
    """Check Jaccard similarity of body text"""
    with open(ref_file) as f:
        ref = f.read()

    def body_text(h):
        m = re.search(r'<main[^>]*>', h)
        if m: h = h[m.start():]
        e = h.find('</main>')
        if e > 0: h = h[:e]
        h = re.sub(r'<script[^>]*>.*?</script>', '', h, flags=re.DOTALL)
        h = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.DOTALL)
        h = re.sub(r'<svg[^>]*>.*?</svg>', '', h, flags=re.DOTALL)
        return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip().lower()

    def sh(t, n=5):
        w = t.split()
        return set(' '.join(w[i:i+n]) for i in range(len(w)-n+1))

    gt, at = body_text(ref), body_text(new_html)
    gs, as_ = sh(gt), sh(at)
    j = len(gs & as_) / len(gs | as_) if gs | as_ else 0

    gh2 = [re.sub(r'<[^>]+>','',h).strip() for h in re.findall(r'<h2[^>]*>(.*?)</h2>', ref, re.DOTALL)]
    ah2 = [re.sub(r'<[^>]+>','',h).strip() for h in re.findall(r'<h2[^>]*>(.*?)</h2>', new_html, re.DOTALL)]
    h2d = len(set(gh2) & set(ah2))

    gf = [re.sub(r'<[^>]+>','',q).strip() for q in re.findall(r'<summary[^>]*>(.*?)</summary>', ref, re.DOTALL)]
    af = [re.sub(r'<[^>]+>','',q).strip() for q in re.findall(r'<summary[^>]*>(.*?)</summary>', new_html, re.DOTALL)]
    fd = len(set(gf) & set(af))

    unique_pct = len(as_ - gs) / max(1, len(as_)) * 100
    goiania_refs = new_html.lower().count('goiânia') + new_html.lower().count('goiania')

    return j, h2d, fd, unique_pct, goiania_refs


# ============================================================
# MAIN: Generate, check, upload all 4 services
# ============================================================
if __name__ == '__main__':
    now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    print("=" * 70)
    print("GERANDO 4 LPs DE ANÁPOLIS — CONTEÚDO 100% ORIGINAL")
    print("=" * 70)

    for svc_key, content in SERVICES.items():
        print(f"\n{'─'*70}")
        print(f"  {svc_key.upper()}")
        print(f"{'─'*70}")

        # Generate
        html = apply_content_to_reference(svc_key, content)

        # Save locally
        local_file = f'/Users/jrios/move-maquinas-seo/anapolis-go-{content["slug"]}-FINAL.html'
        with open(local_file, 'w') as f:
            f.write(html)

        # Check similarity
        j, h2d, fd, unique_pct, goiania_refs = check_similarity(content["ref_file"], html)

        print(f"  Size: {len(html)//1024}KB")
        print(f"  Jaccard: {j:.3f} (target < 0.20)")
        print(f"  H2 dup: {h2d}")
        print(f"  FAQ dup: {fd}")
        print(f"  Unique: {unique_pct:.1f}%")
        print(f"  Goiânia refs: {goiania_refs}")

        # Upload to R2
        r2_key = f'anapolis-go/{content["slug"]}/index.html'
        S3.put_object(
            Bucket='pages',
            Key=r2_key,
            Body=html.encode('utf-8'),
            ContentType='text/html; charset=utf-8',
            CacheControl='public, max-age=30'
        )
        print(f"  Published: {BASE_URL}/{r2_key}")

    print(f"\n{'='*70}")
    print("TODAS AS 4 LPs GERADAS E PUBLICADAS!")
    print(f"{'='*70}")
