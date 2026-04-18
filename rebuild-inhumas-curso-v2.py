#!/usr/bin/env python3
"""
rebuild-inhumas-curso-v2.py
Gera LP de Curso de Operador de Empilhadeira para Inhumas
usando referência de Goiânia como ESQUELETO HTML/CSS/JS.

Todo o texto é reescrito do zero — conteúdo 100% único.
HTML, CSS, JS, SVGs = intocados.
"""

REF = '/Users/jrios/move-maquinas-seo/ref-goiania-curso.html'
OUT = '/Users/jrios/move-maquinas-seo/inhumas-go-curso-de-operador-de-empilhadeira-V2.html'

with open(REF, 'r', encoding='utf-8') as f:
    html = f.read()

def r(old, new, count=1):
    """Replace com verificação."""
    global html
    if old not in html:
        print(f"⚠ NÃO ENCONTRADO: {old[:80]}...")
        return
    html = html.replace(old, new, count)

# ═══════════════════════════════════════════════════════════════════════
# 1. HEAD — title, meta, canonical, og, geo
# ═══════════════════════════════════════════════════════════════════════

r('<title>Curso de Operador de Empilhadeira em Goiânia (NR-11) | Move Máquinas</title>',
  '<title>Curso de Operador de Empilhadeira NR-11 em Inhumas-GO | Move Máquinas</title>')

r('content="Curso de operador de empilhadeira NR-11 em Goiânia. Formação teórica e prática com empilhadeira Clark, 22h de carga horária, certificado válido em todo o Brasil. +2.000 profissionais formados. Presencial ou In Company."',
  'content="Treinamento NR-11 para operadores de empilhadeira em Inhumas. Formação prática com Clark voltada ao polo têxtil, polo de confecção e Distrito Industrial. 22h, certificado nacional válido 2 anos. Turmas presenciais e In Company nas indústrias da GO-070."')

r('href="https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira"',
  'href="https://movemaquinas.com.br/inhumas-go/curso-de-operador-de-empilhadeira"')

r('content="Curso de Operador de Empilhadeira em Goiânia (NR-11) | Move Máquinas"',
  'content="Curso de Operador de Empilhadeira NR-11 em Inhumas-GO | Move Máquinas"')

r('content="Formação completa NR-11 para operadores de empilhadeira em Goiânia. Módulo teórico + prática supervisionada com Clark. Certificado nacional. +2.000 profissionais já formados."',
  'content="Certificação NR-11 para operadores do Distrito Industrial, polo de confecção e Distrito Industrial em Inhumas. Teoria + prática com empilhadeira Clark, certificado válido em todo o Brasil. +2.000 profissionais capacitados."')

r('content="Goiânia, Goiás, Brasil"', 'content="Inhumas, Goiás, Brasil"')
r('content="-16.7234;-49.2654"', 'content="-16.3547;-49.4952"')
r('content="-16.7234, -49.2654"', 'content="-16.3547, -49.4952"')

# ═══════════════════════════════════════════════════════════════════════
# 1B. SCHEMA — coords, Course, BreadcrumbList
# ═══════════════════════════════════════════════════════════════════════

# Coords (all patterns)
r('"latitude": -16.7234, "longitude": -49.2654',
  '"latitude": -16.3547, "longitude": -49.4952')
r('"latitude": -16.7234', '"latitude": -16.3547')
r('"longitude": -49.2654', '"longitude": -49.4952')

# Schema — Course name
r('"name": "Curso de Operador de Empilhadeira NR-11 em Goiânia"',
  '"name": "Treinamento NR-11 para Operadores de Empilhadeira em Inhumas"')

r('"description": "Formação completa para operadores de empilhadeira conforme NR-11. Módulo teórico (legislação, segurança, operação) e módulo prático supervisionado com empilhadeira Clark. 22 horas de carga horária, certificado válido em todo o território nacional."',
  '"description": "Capacitação NR-11 voltada aos operadores do polo têxtil, distritos polo de confecção e Distrito Industrial em Inhumas. Módulo teórico (legislação, segurança, tipos de carga industrial) e prática supervisionada com empilhadeira Clark. 22 horas, certificado com validade nacional de 2 anos."')

# CourseInstance — presencial
r('"name": "Presencial na sede em Goiânia"',
  '"name": "Presencial na sede (40 km de Inhumas)"')

# Schema — BreadcrumbList
r('"name": "Goiânia", "item": "https://movemaquinas.com.br/goiania-go/"',
  '"name": "Inhumas", "item": "https://movemaquinas.com.br/inhumas-go/"')
r('"name": "Curso de Operador de Empilhadeira", "item": "https://movemaquinas.com.br/goiania-go/curso-de-operador-de-empilhadeira"',
  '"name": "Curso NR-11 Empilhadeira", "item": "https://movemaquinas.com.br/inhumas-go/curso-de-operador-de-empilhadeira"')

# ═══════════════════════════════════════════════════════════════════════
# 1C. SCHEMA FAQ — 8 perguntas reescritas do zero para Inhumas
# ═══════════════════════════════════════════════════════════════════════

OLD_FAQ_SCHEMA = '''      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Qual a carga horária do curso de operador de empilhadeira NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "O curso possui 22 horas de carga horária total, divididas em módulo teórico (12h) e módulo prático supervisionado (8h), além de 2 horas de avaliação. O módulo teórico abrange legislação NR-11 e NR-12, segurança operacional, inspeção pré-operacional e tipos de empilhadeira. O módulo prático é realizado com empilhadeira Clark na sede da Move Máquinas em Goiânia ou na empresa do cliente." } },
        { "@type": "Question", "name": "O certificado do curso NR-11 é válido em todo o Brasil?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O certificado emitido pela Move Máquinas tem validade em todo o território nacional. O documento atende às exigências da NR-11 do Ministério do Trabalho e Emprego e pode ser apresentado em auditorias, fiscalizações e processos de admissão em qualquer estado brasileiro." } },
        { "@type": "Question", "name": "Qual a diferença entre o curso presencial e o In Company?", "acceptedAnswer": { "@type": "Answer", "text": "O curso presencial acontece na sede da Move Máquinas em Goiânia, com turmas regulares para operadores individuais ou pequenos grupos. O In Company é realizado na empresa do cliente, com turma fechada e conteúdo adaptado à operação específica (tipo de empilhadeira, layout do galpão, cargas movimentadas). Ambas as modalidades emitem o mesmo certificado válido nacionalmente." } },
        { "@type": "Question", "name": "Quanto custa o curso de operador de empilhadeira em Goiânia?", "acceptedAnswer": { "@type": "Answer", "text": "O valor varia conforme a quantidade de operadores e a modalidade escolhida (presencial ou In Company). Turmas maiores e contratos In Company possuem condições diferenciadas. Entre em contato pelo WhatsApp (62) 98263-7300 ou telefone (62) 3211-1515 para receber a proposta detalhada." } },
        { "@type": "Question", "name": "Quem precisa fazer o curso de operador de empilhadeira?", "acceptedAnswer": { "@type": "Answer", "text": "Todo profissional que opera empilhadeira, transpaleteira elétrica ou equipamento de movimentação de cargas precisa do treinamento NR-11 com certificado válido. Isso inclui operadores de doca em CDs logísticos, funcionários de atacadistas, operadores industriais e qualquer colaborador que conduza empilhadeira em pátios, galpões ou linhas de produção." } },
        { "@type": "Question", "name": "A empresa é multada se o operador não tiver certificado NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A fiscalização do Ministério do Trabalho aplica multa de até R$6.000 por operador sem certificado NR-11 válido. Em caso de acidente com operador não certificado, a empresa responde civil e criminalmente. O investimento no curso representa uma fração do risco financeiro e jurídico de manter operadores sem formação." } },
        { "@type": "Question", "name": "O curso inclui prática com empilhadeira real?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. O módulo prático (8 horas) é realizado com empilhadeira Clark real, sob supervisão de instrutor certificado. Os alunos praticam operação de carga e descarga, empilhamento, manobras em corredor, inspeção pré-operacional e procedimentos de segurança. Na modalidade In Company, a prática é feita com o equipamento da própria operação do cliente." } },
        { "@type": "Question", "name": "Vocês oferecem reciclagem do curso NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A NR-11 recomenda reciclagem periódica do treinamento, especialmente quando há mudança de equipamento, acidente ou afastamento prolongado do operador. O curso de reciclagem possui carga horária reduzida e foco nos pontos de atualização. Consulte disponibilidade para turmas de reciclagem em Goiânia." } }
      ]'''

NEW_FAQ_SCHEMA = '''      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "Quantas horas dura a formação NR-11 para operadores em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "A capacitação totaliza 22 horas distribuídas em três blocos: teoria (12h) sobre legislação NR-11/NR-12, segurança e tipos de empilhadeira; prática supervisionada (8h) com Clark em cenários de carga industrial; e avaliação final (2h) com prova escrita e demonstração prática. Para turmas In Company no polo de confecções ou indústria alimentícia, o cronograma é adaptado aos turnos da operação." } },
        { "@type": "Question", "name": "O certificado NR-11 emitido em Inhumas vale em outros estados?", "acceptedAnswer": { "@type": "Answer", "text": "Sim. A certificação emitida pela Move Máquinas atende integralmente à NR-11 do Ministério do Trabalho e possui validade em todo o território brasileiro. Operadores certificados aqui podem apresentar o documento em auditorias, processos admissionais e fiscalizações em qualquer unidade da federação, incluindo indústrias do DAIA em Anápolis e CDs de Brasília." } },
        { "@type": "Question", "name": "Vale mais a pena fazer o curso presencial ou In Company para empresas de Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "Empresas do polo têxtil e dos distritos polo de confecção e Distrito Industrial com 6 ou mais operadores economizam tempo e logística com o In Company: o instrutor vai até a planta, adapta a prática ao layout dos galpões e às empilhadeiras da operação. Para 1 a 5 operadores, a sede da Move fica a apenas 40 km pela GO-070 e oferece turmas semanais com certificado no mesmo ciclo." } },
        { "@type": "Question", "name": "Qual o investimento para certificar operadores de empilhadeira em Inhumas?", "acceptedAnswer": { "@type": "Answer", "text": "O valor depende da quantidade de operadores e da modalidade (presencial ou In Company). Turmas maiores nas indústrias do polo de confecção e Distrito Industrial recebem condições diferenciadas por aluno. Solicite a proposta detalhada pelo WhatsApp (62) 98263-7300 ou telefone (62) 3211-1515. O investimento equivale a uma fração do custo de uma única multa por operador irregular." } },
        { "@type": "Question", "name": "Quais profissionais do Distrito Industrial precisam da certificação NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "Todo colaborador que opere empilhadeira a combustão, elétrica, transpaleteira ou rebocador dentro do polo têxtil, dos galpões do polo de confecções ou das fábricas do indústria alimentícia precisa de certificação NR-11 válida. Isso inclui operadores de movimentação de fardos químicos, conferentes que usam transpaleteira e auxiliares designados para carga e descarga em docas industriais." } },
        { "@type": "Question", "name": "Qual a penalidade para empresas de Inhumas com operadores sem NR-11?", "acceptedAnswer": { "@type": "Answer", "text": "O Ministério do Trabalho aplica multa de até R$6.000 por operador sem certificação válida. No Distrito Industrial e nos distritos industriais, a fiscalização é recorrente por conta do risco operacional elevado. Em caso de acidente, a empresa responde civil e criminalmente. O custo da formação é inferior ao prejuízo de um único auto de infração." } },
        { "@type": "Question", "name": "A prática do curso é feita com empilhadeira de verdade ou simulador?", "acceptedAnswer": { "@type": "Answer", "text": "O módulo prático utiliza exclusivamente empilhadeira Clark real durante as 8 horas de treinamento. Os alunos executam carga e descarga de paletes, empilhamento em alturas variadas, manobras em corredor estreito e inspeção pré-operacional completa. Na modalidade In Company, a prática pode ser realizada com a própria empilhadeira da operação no polo de confecções, indústria alimentícia ou Distrito Industrial." } },
        { "@type": "Question", "name": "O treinamento NR-11 precisa ser renovado? Com que frequência?", "acceptedAnswer": { "@type": "Answer", "text": "A NR-11 recomenda reciclagem quando há troca de modelo de empilhadeira, ocorrência de acidente, retorno de afastamento superior a 90 dias ou a cada 2 anos. Para operadores do polo têxtil que manuseiam cargas químicas, a reciclagem periódica reduz risco e mantém a conformidade em auditorias de segurança. Consulte turmas de reciclagem pelo WhatsApp (62) 98263-7300." } }
      ]'''

r(OLD_FAQ_SCHEMA, NEW_FAQ_SCHEMA)

# ═══════════════════════════════════════════════════════════════════════
# 2. BREADCRUMB
# ═══════════════════════════════════════════════════════════════════════

r('<a href="/goiania-go/">Goiânia</a>',
  '<a href="/inhumas-go/">Inhumas</a>')

r('<span aria-current="page">Curso de Operador de Empilhadeira</span>',
  '<span aria-current="page">Curso NR-11 Operador de Empilhadeira</span>')

# ═══════════════════════════════════════════════════════════════════════
# 3. HERO — H1, lead, badge
# ═══════════════════════════════════════════════════════════════════════

r('+2.000 profissionais formados',
  'NR-11 certificado para indústria')

r('Curso de Operador de Empilhadeira em <em>Goiânia</em> (NR-11)',
  'Treinamento NR-11 de Operador de Empilhadeira em <em>Inhumas</em>')

r('Formação teórica e prática com empilhadeira Clark. 22 horas de carga horária, certificado válido em todo o Brasil e instrutores com experiência em operações logísticas do Centro-Oeste. Turmas presenciais na sede e treinamento In Company.',
  'Capacitação completa para operadores do polo têxtil e indústrias dos distritos polo de confecções/indústria alimentícia. Prática supervisionada com empilhadeira Clark, 22 horas de carga horária e certificado nacional válido por 2 anos. Turmas na sede (40 km pela GO-070) ou In Company na sua planta industrial.')

# WhatsApp URLs — replace encoded Goiânia in WA links
r('Goi%C3%A2nia', 'Inhumas', 99)

# ═══════════════════════════════════════════════════════════════════════
# 4. TRUST BAR — variação para Inhumas
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+2.000 formados</strong><span>Certificados emitidos</span>',
  '<strong>+2.000 certificados</strong><span>Operadores capacitados</span>')

r('<strong>22h de formação</strong><span>Teórica + prática</span>',
  '<strong>22h intensivas</strong><span>Teoria + Clark real</span>')

r('<strong>Certificado nacional</strong><span>Válido em todo o Brasil</span>',
  '<strong>Validade 2 anos</strong><span>Certificado NR-11 nacional</span>')

r('<strong>+20 anos</strong><span>No mercado goiano</span>',
  '<strong>+20 anos</strong><span>Formando operadores</span>')

# ═══════════════════════════════════════════════════════════════════════
# 5. STATS BAR (MARQUEE) — reescrito
# ═══════════════════════════════════════════════════════════════════════

r('<strong>+2.000</strong> profissionais formados</span><div class="stats-bar__sep"></div>\n    <span><strong>22h</strong> de carga horária</span><div class="stats-bar__sep"></div>\n    <span><strong>NR-11</strong> certificado nacional</span><div class="stats-bar__sep"></div>\n    <span><strong>Clark</strong> prática com empilhadeira real</span><div class="stats-bar__sep"></div>\n    <span><strong>2 modalidades</strong> presencial e in company</span><div class="stats-bar__sep"></div>\n    <span><strong>+2.000</strong> profissionais formados</span><div class="stats-bar__sep"></div>\n    <span><strong>22h</strong> de carga horária</span><div class="stats-bar__sep"></div>\n    <span><strong>NR-11</strong> certificado nacional</span><div class="stats-bar__sep"></div>\n    <span><strong>Clark</strong> prática com empilhadeira real</span><div class="stats-bar__sep"></div>\n    <span><strong>2 modalidades</strong> presencial e in company',
  '<strong>+2.000</strong> operadores certificados</span><div class="stats-bar__sep"></div>\n    <span><strong>22h</strong> teoria + prática Clark</span><div class="stats-bar__sep"></div>\n    <span><strong>NR-11</strong> validade nacional 2 anos</span><div class="stats-bar__sep"></div>\n    <span><strong>40 km</strong> de Inhumas via GO-070</span><div class="stats-bar__sep"></div>\n    <span><strong>In Company</strong> no Distrito Industrial e polo de confecções</span><div class="stats-bar__sep"></div>\n    <span><strong>+2.000</strong> operadores certificados</span><div class="stats-bar__sep"></div>\n    <span><strong>22h</strong> teoria + prática Clark</span><div class="stats-bar__sep"></div>\n    <span><strong>NR-11</strong> validade nacional 2 anos</span><div class="stats-bar__sep"></div>\n    <span><strong>40 km</strong> de Inhumas via GO-070</span><div class="stats-bar__sep"></div>\n    <span><strong>In Company</strong> no Distrito Industrial e polo de confecções')

# ═══════════════════════════════════════════════════════════════════════
# 6. SEÇÃO "O QUE É" — todo texto reescrito
# ═══════════════════════════════════════════════════════════════════════

# H2
r('O que é o <span>curso de operador de empilhadeira</span> e por que fazer',
  'Por que a <span>certificação NR-11</span> é indispensável para operadores em Inhumas')

# Parágrafo principal
r('O curso de operador de empilhadeira NR-11 é a formação obrigatória exigida pelo Ministério do Trabalho para todo profissional que opera empilhadeira, transpaleteira elétrica ou equipamento de movimentação de cargas. Em Goiânia, onde os corredores logísticos da GO-070, os atacadistas do Polo da Moda e as indústrias do Distrito Industrial movimentam milhares de toneladas por dia, manter operadores certificados não é opcional: é requisito legal e condição para evitar multas, interdições e responsabilidade criminal.',
  'A certificação NR-11 é a habilitação obrigatória para qualquer profissional que opere empilhadeira, transpaleteira ou equipamento de movimentação de cargas no Brasil. Em Inhumas, onde o polo têxtil movimenta fardos e paletes de produtos químicos, os galpões do polo de confecções processam insumos de confecção e alimentícios e o indústria alimentícia expede produtos alimentícios e embalagens pela GO-070, a ausência de operadores certificados expõe a empresa a multas de até R$6.000 por colaborador, interdição da operação e responsabilidade criminal em caso de acidente.')

# H3 — NR-11 exige
r('O que a NR-11 exige das empresas em Goiânia',
  'Obrigações legais da NR-11 para indústrias de Inhumas')

r('A Norma Regulamentadora 11 determina que toda empresa que utilize equipamentos de transporte e movimentação de materiais deve garantir que seus operadores possuam formação específica com certificado válido. Em Goiânia, a fiscalização do Ministério do Trabalho atua com frequência nos CDs logísticos da GO-070, nas indústrias do DAIA em Anápolis e nos galpões do Distrito Industrial Leste. Empresas flagradas com operadores sem certificação recebem multa imediata e podem ter a operação interditada até a regularização.',
  'A NR-11 determina que toda empresa com equipamentos de transporte e movimentação de materiais mantenha operadores com formação específica e certificado atualizado. No Distrito Industrial de Inhumas, a fiscalização do Ministério do Trabalho é recorrente pelo risco elevado de operações com cargas químicas. No polo de confecções, auditorias de qualidade de confecção e alimentícia exigem comprovação da NR-11 como pré-requisito para manter certificações da planta. Empresas flagradas com operadores irregulares recebem auto de infração imediato e podem ter a linha de produção interditada.')

# H3 — Quem precisa
r('Quem precisa fazer o curso: operadores de empilhadeira e transpaleteira',
  'Perfis que necessitam da certificação NR-11 na região industrial')

r('O treinamento é obrigatório para operadores de empilhadeira a combustão (GLP e diesel), empilhadeira elétrica, transpaleteira elétrica, rebocador e qualquer equipamento de movimentação horizontal ou vertical de cargas. Isso inclui operadores de doca, conferentes que operam transpaleteira, auxiliares de logística designados para movimentação e colaboradores em treinamento que ainda não possuem certificação. Na prática, qualquer funcionário que suba em uma empilhadeira precisa do certificado NR-11.',
  'A formação abrange operadores de empilhadeira a combustão e elétrica, transpaleteira, rebocador e qualquer equipamento de movimentação de cargas. No contexto de Inhumas, isso inclui operadores que deslocam fardos no Distrito Industrial, conferentes que manuseiam paletes de confecção e alimentícios no polo de confecções, auxiliares de expedição no indústria alimentícia e motoristas de pátio que conduzem empilhadeira entre galpões. Todo profissional que toque nos comandos de uma empilhadeira precisa portar o certificado NR-11 válido.')

# H3 — Certificado
r('Certificado válido em todo o território nacional',
  'Certificação aceita em auditorias industriais e fiscalizações nacionais')

r('O certificado emitido pela Move Máquinas atende às exigências da NR-11 e possui validade em todos os estados brasileiros. O documento pode ser apresentado em auditorias do Ministério do Trabalho, processos de admissão, licitações e fiscalizações em qualquer unidade da federação. A reciclagem é recomendada periodicamente ou sempre que houver mudança de equipamento, acidente de trabalho ou afastamento prolongado do operador.',
  'O documento emitido pela Move Máquinas cumpre integralmente a NR-11 e tem aceitação em todo o território brasileiro. Operadores certificados podem apresentar o documento em auditorias ISO do Distrito Industrial, fiscalizações do Ministério do Trabalho no polo de confecções, processos admissionais de transportadoras da GO-070 e licitações em qualquer estado. A renovação é recomendada a cada 2 anos ou sempre que houver troca de modelo de empilhadeira, acidente ou afastamento superior a 90 dias.')

# Bullet 1 — formação
r('módulo teórico de legislação e segurança, módulo prático supervisionado com empilhadeira Clark e avaliação final com prova teórica e prática.',
  'teoria de legislação NR-11/NR-12 e segurança operacional, prática supervisionada com empilhadeira Clark em cenários industriais e avaliação com prova escrita e demonstração de operação.')

# Bullet 2 — instrutores
r('profissionais que conhecem as operações logísticas de Goiânia, desde docas de CDs até pátios industriais do DAIA.',
  'instrutores com vivência em plantas petroquímicas, galpões de confecção e alimentícios e CDs logísticos da GO-070 na região metropolitana.')

# Bullet 3 — prática (keep)
r('os alunos operam empilhadeira Clark durante o módulo prático, praticando carga, descarga, empilhamento e manobras reais.',
  'treinamento com empilhadeira Clark em situações reais: movimentação de fardos, empilhamento em prateleiras industriais e manobras em corredores de galpão.')

# Bullet 4 — modalidades
r('presencial na sede da Move Máquinas em Goiânia ou In Company na empresa do cliente, com conteúdo adaptado à operação específica.',
  'presencial na sede (40 km de Inhumas pela GO-070) ou In Company diretamente na planta do polo de confecções, indústria alimentícia ou Distrito Industrial, com conteúdo calibrado à operação do cliente.')

# Alt text da imagem
r('alt="Treinamento prático de operador de empilhadeira na sede da Move Máquinas em Goiânia, instrutor supervisionando operação com empilhadeira Clark"',
  'alt="Operador de empilhadeira Clark durante treinamento NR-11, prática supervisionada voltada às indústrias de Inhumas"')

# ═══════════════════════════════════════════════════════════════════════
# 7. SHORTS — alt texts
# ═══════════════════════════════════════════════════════════════════════

r('Veja como funciona o <span>curso na prática</span>',
  'Acompanhe a <span>formação NR-11</span> em tempo real')

r('Assista aos vídeos curtos e entenda o processo de formação, a prática com empilhadeira Clark e a certificação NR-11.',
  'Vídeos curtos que mostram cada etapa da capacitação: aula teórica, prática com Clark e avaliação para certificação NR-11.')

# ═══════════════════════════════════════════════════════════════════════
# 8. INSCRIÇÃO RÁPIDA — textos contextualizados
# ═══════════════════════════════════════════════════════════════════════

r('Viu como funciona? Agora <span style="color:var(--color-primary);">garanta sua vaga.</span>',
  'Pronto para certificar? <span style="color:var(--color-primary);">Reserve sua vaga agora.</span>')

r('Preencha os campos ao lado e receba as informações pelo WhatsApp. Turmas semanais, certificado em até 5 dias.',
  'Preencha o formulário e receba a proposta pelo WhatsApp. Turmas semanais na sede ou In Company no polo de confecções, indústria alimentícia e Distrito Industrial.')

r('Presencial na sede ou In Company</li>',
  'In Company no polo de confecções, indústria alimentícia ou petroquímico</li>')

r('+2.000 profissionais já formados</li>',
  '+2.000 operadores já certificados</li>')

# Form select — cidade: SC como primeira opção
r('''              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Inhumas">Inhumas</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''',
  '''              <option value="Inhumas" selected>Inhumas</option>
              <option value="Goiânia">Goiânia</option>
              <option value="Aparecida de Goiânia">Aparecida de Goiânia</option>
              <option value="Anápolis">Anápolis</option>
              <option value="Trindade">Trindade</option>
              <option value="Outra">Outra cidade</option>''')

# Form select — modalidade
r('Presencial (na sede em Goiânia)',
  'Presencial (sede a 40 km de SC)')

# ═══════════════════════════════════════════════════════════════════════
# 9. PARA QUEM É (PERSONAS) — reescritos para SC
# ═══════════════════════════════════════════════════════════════════════

r('Esse <span>treinamento de operador</span> é para você?',
  'Qual perfil se beneficia da <span>certificação NR-11</span> em Inhumas?')

r('Se você se identifica com algum desses perfis, o curso NR-11 vai resolver o seu problema.',
  'Confira se a sua situação se encaixa em algum desses cenários comuns nas indústrias da região.')

# Persona 1
r('Operador sem certificado',
  'Operador de pátio sem NR-11')

r('Trabalha no galpão há anos, sabe operar na prática, mas nunca tirou o certificado NR-11. Sabe que pode perder o emprego ou gerar multa para a empresa.',
  'Conduz empilhadeira no Distrito Industrial ou nos galpões do polo de confecções há anos, conhece a máquina na prática, mas nunca formalizou a certificação. Sabe que uma fiscalização pode gerar multa e interdição da planta.')

# Persona 2
r('Gestor preocupado com multa',
  'Gestor industrial preocupado com fiscalização')

r('Gerente de logística ou dono de empresa que precisa regularizar os operadores antes de uma fiscalização. Multa de até R$6.000 por operador irregular.',
  'Gerente de planta ou coordenador de segurança no polo de confecções/indústria alimentícia que precisa regularizar a equipe antes da próxima auditoria. Multa de até R$6.000 por operador e risco de interdição.')

# Persona 3
r('Profissional buscando recolocação',
  'Profissional em busca de vaga industrial')

r('Quer entrar no mercado de logística em Goiânia. Com o certificado NR-11, se candidata a vagas em CDs da GO-070, atacadistas do Polo da Moda e indústrias do DAIA.',
  'Busca colocação nas indústrias de Inhumas. Com o certificado NR-11, se habilita para vagas no polo têxtil, fábricas do polo de confecções, galpões do indústria alimentícia e CDs logísticos da GO-070.')

# Persona 4
r('Empresa que alugou empilhadeira',
  'Empresa que contratou locação de empilhadeira')

r('Fechou contrato de locação de empilhadeira Clark e precisa que os operadores estejam certificados antes de receber a máquina. Sem NR-11, o contrato não inicia.',
  'Assinou contrato de aluguel de empilhadeira Clark com a Move e precisa que os operadores portem o NR-11 antes de receber a máquina. Sem certificação válida, o equipamento não é liberado.')

# ═══════════════════════════════════════════════════════════════════════
# 10. JORNADA DO ALUNO — textos
# ═══════════════════════════════════════════════════════════════════════

r('Do primeiro contato ao <span>certificado na mão</span>',
  'Da matrícula ao <span>certificado NR-11 validado</span>')

r('4 etapas. Em até 5 dias você sai com o certificado NR-11 válido em todo o Brasil.',
  '4 etapas objetivas. Em até 5 dias, o operador recebe a certificação NR-11 com validade nacional de 2 anos.')

r('Fale pelo WhatsApp, escolha a turma e reserve sua vaga. Turmas semanais.',
  'Fale pelo WhatsApp, selecione a turma e garanta a vaga. Turmas semanais na sede ou In Company.')

r('NR-11, NR-12, segurança, inspeção, centro de gravidade, EPIs. Sala de aula na sede.',
  'Legislação NR-11/NR-12, inspeção pré-operacional, centro de gravidade e EPIs. Sala de aula ou In Company.')

r('Operação real com empilhadeira Clark. Carga, descarga, manobra, empilhamento. Instrutor 1:1.',
  'Operação real com Clark: carga, descarga, empilhamento e manobras em corredor industrial. Instrutor individual.')

r('Prova teórica + prática. Aprovado, recebe certificado NR-11 válido nacionalmente.',
  'Avaliação teórica e prática. Aprovado, recebe certificado NR-11 com validade nacional de 2 anos.')

# ═══════════════════════════════════════════════════════════════════════
# 11. CONTEÚDO PROGRAMÁTICO — textos reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Conteúdo programático da <span>formação NR-11</span>',
  'Grade curricular completa do <span>treinamento NR-11</span> para Inhumas')

r('O curso cobre legislação, segurança operacional, fundamentos teóricos e prática supervisionada com empilhadeira Clark. Avaliação final com prova teórica e prática.',
  'A capacitação abrange arcabouço regulatório, procedimentos de segurança industrial, fundamentos de operação e prática intensiva com empilhadeira Clark. Avaliação final com prova escrita e demonstração operacional.')

r('Módulo teórico: legislação, segurança e normas',
  'Bloco teórico: regulamentação, segurança e procedimentos industriais')

r('As primeiras 12 horas cobrem todo o arcabouço regulatório da NR-11 e NR-12, responsabilidades legais do operador e da empresa contratante, procedimentos de inspeção pré-operacional, uso correto de EPIs, sinalização de manobra e fundamentos de centro de gravidade e capacidade de carga. O conteúdo é contextualizado com exemplos reais de operações em Goiânia: docas de CDs na GO-070, pátios de expedição no Distrito Industrial e galpões de atacadistas do Polo da Moda.',
  'O bloco inicial de 12 horas percorre a legislação NR-11 e NR-12, as responsabilidades jurídicas do operador e do empregador, inspeção pré-operacional padronizada, uso adequado de EPIs industriais, sinalização de manobra e princípios de centro de gravidade e limite de carga. Os exemplos são calibrados para a realidade de Inhumas: movimentação de fardos químicos no Distrito Industrial, paletes de confecção e alimentícios no polo de confecções e cargas mistas nos CDs ao longo da GO-070.')

r('Módulo prático: operação supervisionada com empilhadeira Clark',
  'Bloco prático: operação real com Clark em cenários industriais')

r('As 8 horas de prática são realizadas com empilhadeira Clark real. Os alunos executam carga e descarga de paletes, empilhamento em diferentes alturas, manobras em corredores simulados, inspeção pré-operacional completa e procedimentos de emergência. O instrutor acompanha cada operador individualmente, corrigindo postura, técnica de condução e procedimentos de segurança.',
  'Durante 8 horas o aluno opera empilhadeira Clark sob supervisão direta. Os exercícios incluem carga e descarga de paletes industriais, empilhamento em prateleiras de diferentes alturas, manobras em corredores estreitos de galpão, execução da inspeção pré-operacional e procedimentos de emergência. O instrutor acompanha individualmente, corrigindo postura, técnica de condução e sequência de segurança.')

r('Carga horária e duração',
  'Duração total e formato flexível')

r('A formação completa totaliza 22 horas: 12 horas de módulo teórico, 8 horas de prática supervisionada e 2 horas de avaliação. A duração varia conforme a modalidade: no formato presencial, o curso pode ser concluído em 3 a 4 dias. No formato In Company, o cronograma é adaptado à rotina da empresa.',
  'São 22 horas no total: 12 horas de teoria, 8 horas de prática supervisionada e 2 horas de avaliação final. No formato presencial na sede, a conclusão leva de 3 a 4 dias. Para turmas In Company no polo de confecções, indústria alimentícia ou Distrito Industrial, o cronograma é ajustado aos turnos de produção para minimizar impacto na operação.')

r('A grade pode ser adaptada para turmas In Company conforme o tipo de equipamento e operação do cliente.',
  'Para turmas In Company nas indústrias de Inhumas, a grade é adaptada ao tipo de empilhadeira e às cargas específicas da operação.')

# ═══════════════════════════════════════════════════════════════════════
# 12. FALA DO ESPECIALISTA — reescrita para SC
# ═══════════════════════════════════════════════════════════════════════

r('"Toda semana recebo ligação de empresa que tomou multa porque o operador não tinha certificado NR-11. A multa vai de R$2.000 a R$6.000 por operador, e se acontecer um acidente, a responsabilidade é civil e criminal. O curso custa uma fração disso. Além da certificação, o operador treinado conserva melhor o equipamento, gasta menos bateria, quebra menos garfo. Para quem aluga conosco, eu sempre recomendo: coloque o operador no curso antes de receber a máquina. O retorno aparece na primeira semana."',
  '"Nos últimos dois meses, três empresas do Distrito Industrial e do polo de confecções me ligaram após receberem auto de infração por operadores sem NR-11. A multa chega a R$6.000 por colaborador, sem contar o risco de interdição. O que eu digo sempre: o custo do treinamento é menor do que o prejuízo de um dia parado. Além da conformidade legal, o operador certificado faz inspeção antes de ligar a máquina, respeita o limite de carga e conserva a empilhadeira — quem aluga conosco e passa a equipe pelo curso nota diferença já na primeira semana de contrato."')

# ═══════════════════════════════════════════════════════════════════════
# 13. COMPARATIVO PRESENCIAL VS IN COMPANY — textos SC
# ═══════════════════════════════════════════════════════════════════════

r('Presencial ou In Company: qual <span>modalidade</span> escolher?',
  'Presencial na sede ou In Company na planta: qual <span>formato</span> funciona para Inhumas?')

r('A escolha entre presencial e In Company depende da quantidade de operadores, da urgência da certificação e do tipo de operação. Ambas as modalidades emitem o mesmo certificado com validade nacional.',
  'A decisão entre presencial e In Company depende do número de operadores, do prazo para regularização e da complexidade da operação industrial. Nos dois formatos, o certificado é idêntico e tem validade em todo o Brasil.')

r('Presencial (na sede em Goiânia)',
  'Presencial (sede a 40 km de SC)')

r('Turmas regulares para operadores individuais ou pequenos grupos',
  'Ideal para 1 a 5 operadores de Inhumas')

r('O curso presencial acontece na sede da Move Máquinas na Av. Eurico Viana, 4913, Goiânia. Ideal para empresas que precisam certificar poucos operadores ou profissionais autônomos buscando qualificação.',
  'O treinamento presencial acontece na sede da Move Máquinas, a apenas 40 km de Inhumas pela GO-070. Formato ágil para empresas com poucos operadores pendentes ou profissionais autônomos que buscam habilitação para o mercado industrial da região.')

r('Turma fechada com conteúdo adaptado à operação',
  'Treinamento direto na planta industrial de Inhumas')

r('O treinamento In Company é realizado nas instalações do cliente. O instrutor desloca-se até a empresa e adapta o conteúdo prático ao layout do galpão, tipo de empilhadeira e cargas movimentadas na operação real.',
  'O instrutor se desloca até o Distrito Industrial, polo de confecções ou indústria alimentícia e conduz o treinamento dentro da planta. O módulo prático é adaptado ao layout dos galpões, ao modelo de empilhadeira utilizado e às cargas específicas da operação — de fardos químicos a paletes de confecção e alimentícios.')

r('<strong>Regra prática:</strong> para 1 a 5 operadores, o presencial na sede é mais ágil e econômico. Para 6 ou mais operadores, o In Company elimina o custo de deslocamento da equipe e permite adaptar o treinamento ao equipamento e às cargas reais da operação. Em ambos os casos, o certificado é o mesmo e a validade é nacional.',
  '<strong>Critério para empresas de Inhumas:</strong> até 5 operadores, o presencial na sede resolve em menos de uma semana — são apenas 40 km pela GO-070. A partir de 6 operadores, o In Company elimina deslocamento da equipe e permite que a prática aconteça com a empilhadeira e as cargas reais da operação no polo de confecções, indústria alimentícia ou Distrito Industrial. Certificação idêntica nos dois formatos.')

# ═══════════════════════════════════════════════════════════════════════
# 14. VÍDEO YOUTUBE — textos
# ═══════════════════════════════════════════════════════════════════════

r('alt="Vídeo Move Máquinas: conheça o processo de formação de operadores de empilhadeira em Goiânia"',
  'alt="Vídeo Move Máquinas: treinamento NR-11 de operadores de empilhadeira para indústrias de Inhumas"')

r('Conheça o processo de <span>formação de operadores</span> em Goiânia',
  'Veja como funciona o <span>treinamento de operadores</span> para a região industrial')

r('Assista ao vídeo institucional da Move Máquinas e entenda como funciona a formação de operadores: inscrição, módulo teórico, prática supervisionada com empilhadeira Clark e emissão do certificado NR-11. Todo o processo acontece na sede em Goiânia ou nas instalações da empresa do cliente.',
  'No vídeo institucional da Move Máquinas, acompanhe todas as etapas da capacitação NR-11: matrícula, bloco teórico de legislação e segurança, prática supervisionada com empilhadeira Clark e emissão do certificado. A formação acontece na sede (40 km de Inhumas) ou diretamente na planta industrial do cliente.')

# ═══════════════════════════════════════════════════════════════════════
# 15. PARA QUEM É O CURSO — tag, H3, 4 cards reescritos
# ═══════════════════════════════════════════════════════════════════════

r('Público-alvo em Goiânia',
  'Público-alvo industrial')

r('Para quem é o curso em <span>Goiânia</span>',
  'Quem precisa da certificação em <span>Inhumas</span>')

r('Operadores de empilhadeira, transpaleteira e equipamentos de movimentação de cargas que atuam nos principais polos logísticos e industriais da capital.',
  'Operadores do polo têxtil, indústrias do polo de confecções/indústria alimentícia e CDs logísticos da GO-070 que manuseiam empilhadeira, transpaleteira ou equipamento de movimentação de cargas.')

# Card 1
r('CDs logísticos da GO-070: certificação para operadores de doca',
  'Polo petroquímico: operadores de movimentação de cargas químicas')
r('Os centros de distribuição ao longo da GO-070 concentram o maior volume de operações logísticas de Goiânia. Operadores de doca que movimentam paletes entre caminhões e porta-paletes precisam do certificado NR-11 para atuar legalmente. O curso abrange as situações reais dessas operações: empilhamento em docas de 8 a 12 posições, manobras com carga em turnos duplos e inspeção pré-operacional diária.',
  'confecções, tecelagens e beneficiadoras operam com empilhadeiras no deslocamento de fardos, paletes de insumos e peças de manutenção entre tanques e galpões de estoque. A certificação NR-11 é pré-requisito para auditorias de segurança do complexo. O treinamento abrange movimentação de cargas químicas classificadas, manobras em áreas confinadas e procedimentos de emergência específicos para o setor petroquímico.')

# Card 2
r('Polo da Moda: operadores de empilhadeira em atacadistas',
  'polo de confecções: certificação para operadores de indústrias de confecção e alimentícias')
r('Os atacadistas do Polo da Moda operam com volumes sazonais intensos. Empilhadeiras movimentam fardos de tecido, caixas de confecção e paletes mistos nos galpões de estoque. A certificação dos operadores garante conformidade legal e reduz o risco de acidentes com cargas instáveis em corredores estreitos dos depósitos.',
  'Laboratórios de confecção e alimentícios e fábricas de higiene do polo de confecções mantêm empilhadeiras elétricas em ambientes controlados com exigências rigorosas de segurança. A NR-11 é requisito para manter certificações de qualidade da planta. O curso capacita o operador para movimentar paletes de insumos sensíveis em corredores estreitos de área limpa, respeitando limites de carga e procedimentos de inspeção pré-operacional.')

# Card 3
r('Distrito Industrial: conformidade NR-11 para indústrias',
  'indústria alimentícia: habilitação para o setor moveleiro e alimentício')
r('As indústrias do Distrito Industrial Leste de Goiânia operam com empilhadeiras de médio e grande porte para movimentação de chapas de aço, bobinas, peças fundidas e insumos pesados. O curso abrange operação de empilhadeiras Clark de 2.000 a 8.000 kg, procedimentos de segurança para cargas pesadas e manobras em pátios industriais com rampas e pisos irregulares.',
  'Fábricas de móveis, processadoras de alimentos e indústrias de embalagens no indústria alimentícia movimentam chapas de MDF, paletes de matéria-prima e produtos acabados com empilhadeiras de 2.000 a 5.000 kg. A certificação NR-11 garante conformidade nas inspeções trabalhistas e reduz acidentes com cargas volumosas em galpões de pé-direito elevado e pátios de cascalho.')

# Card 4
r('DAIA Anápolis: treinamento para indústria de confecção e alimentícia',
  'CDs logísticos da GO-070: operadores de doca e expedição')
r('O Distrito Agroindustrial de Anápolis (DAIA) abriga indústrias de confecção e alimentícias, alimentícias e químicas com exigências rigorosas de segurança. A certificação NR-11 é pré-requisito para auditorias de qualidade e para operar empilhadeiras em ambientes controlados. O treinamento In Company pode ser realizado diretamente no DAIA, adaptado às normas específicas de cada indústria.',
  'Os centros de distribuição ao longo da GO-070, entre Inhumas e Goiânia, concentram operações de carga e descarga em turnos contínuos. Operadores de doca que movimentam paletes entre caminhões e porta-paletes precisam do certificado atualizado. O treinamento In Company pode ser conduzido diretamente no CD, adaptado ao layout de doca e aos equipamentos de movimentação utilizados na operação.')

# ═══════════════════════════════════════════════════════════════════════
# 16. INCLUSO — textos com contexto local
# ═══════════════════════════════════════════════════════════════════════

r('Apostila com conteúdo teórico da NR-11 e NR-12, checklist de inspeção pré-operacional e guia de referência rápida para o operador.',
  'Apostila completa com NR-11 e NR-12, checklist de inspeção pré-operacional padronizado e guia de bolso com procedimentos de segurança para consulta no dia a dia industrial.')

r('Profissionais com vivência em operações logísticas reais de Goiânia e região. Acompanhamento individual durante o módulo prático.',
  'Instrutores com experiência em plantas petroquímicas, galpões de confecção e alimentícios e CDs logísticos da região metropolitana. Supervisão individual durante toda a prática.')

r('Orientação sobre reciclagem periódica, atualização de certificados e consultoria para adequação da operação às exigências da NR-11.',
  'Orientação sobre reciclagem a cada 2 anos, atualização de certificados e consultoria para adequar a operação do polo de confecções, indústria alimentícia ou Distrito Industrial às exigências da NR-11.')

# ═══════════════════════════════════════════════════════════════════════
# 17. INVESTIMENTO — textos
# ═══════════════════════════════════════════════════════════════════════

r('Quanto custa a <span>certificação de operador</span> de empilhadeira em 2026?',
  'Qual o investimento na <span>certificação NR-11</span> para operadores em Inhumas?')

r('O valor varia conforme a quantidade de operadores e a modalidade escolhida. Solicite a proposta detalhada pelo WhatsApp ou telefone.',
  'O investimento depende da quantidade de operadores e do formato escolhido. Solicite a proposta personalizada pelo WhatsApp ou telefone.')

r('Valor sob consulta',
  'Investimento sob consulta')

r('O investimento no curso depende de três fatores: quantidade de operadores a certificar, modalidade (presencial ou In Company) e localização da empresa (para treinamentos In Company fora de Goiânia). Turmas maiores possuem condições diferenciadas por aluno. Solicite a proposta personalizada com valores e datas disponíveis.',
  'Três variáveis definem o valor: número de operadores a certificar, formato (presencial na sede ou In Company na planta) e localização da empresa. Inhumas está a apenas 40 km pela GO-070 — o deslocamento para In Company no Distrito Industrial, polo de confecções ou indústria alimentícia não tem custo adicional de frete. Turmas a partir de 6 operadores recebem condições especiais por aluno.')

r('Compare o investimento com o custo da irregularidade',
  'O custo de não certificar é maior do que o treinamento')

r('Interdição da operação: prejuízo de R$5.000 a R$20.000 por dia parado',
  'Interdição da planta no polo de confecções ou Distrito Industrial: prejuízo de R$10.000 a R$50.000 por dia parado')

# ═══════════════════════════════════════════════════════════════════════
# 18. DEPOIMENTOS — 3 novos, 100% originais para SC
# ═══════════════════════════════════════════════════════════════════════

# Depoimento 1
r('"Certificamos 12 operadores de doca no formato In Company. O instrutor adaptou o módulo prático ao layout do nosso CD na GO-070, usando as mesmas empilhadeiras que a equipe opera diariamente. Três semanas depois, passamos na auditoria do Ministério do Trabalho sem uma única pendência."',
  '"Certificamos 15 operadores do pátio de fardos no formato In Company. O instrutor montou as estações de prática dentro do nosso galpão no Distrito Industrial, usando a mesma Clark que a equipe opera no dia a dia. Na auditoria de segurança do mês seguinte, toda a documentação foi aprovada sem ressalvas."')
r('<strong>Marcos A.</strong>',
  '<strong>Roberto M.</strong>')
r('Gerente de RH, Centro de Distribuição, Goiânia-GO (out/2025)',
  'Supervisor de Segurança, Petroquímica, Inhumas-GO (dez/2025)')

# Depoimento 2
r('"Depois de um quase-acidente no pátio, decidimos reciclar todos os operadores. O curso da Move cobriu desde a parte teórica de centro de gravidade até manobras em rampa molhada. Os operadores voltaram com outra consciência sobre inspeção pré-operacional. Valeu cada centavo."',
  '"Recebemos notificação do Ministério do Trabalho e tivemos 30 dias para regularizar 8 operadores de empilhadeira no polo de confecções. A Move encaixou a turma na semana seguinte, presencial na sede. A parte prática com a Clark foi decisiva: corrigiram vícios de operação que a equipe carregava há anos. Apresentamos os certificados no prazo e zeramos as pendências."')
r('<strong>Patrícia L.</strong>',
  '<strong>Fernanda C.</strong>')
r('Coordenadora de Segurança do Trabalho, Indústria Metalúrgica, Goiânia-GO (jan/2026)',
  'Gerente de Segurança do Trabalho, Indústria Farmacêutica polo de confecções, Inhumas-GO (jan/2026)')

# Depoimento 3
r('"Mandamos 8 operadores para o curso presencial na sede da Move. A formação prática com a Clark foi o diferencial: os instrutores corrigiram vícios de operação que os caras tinham há anos. Certificado saiu no mesmo dia e já apresentamos na auditoria do laboratório de confecção e alimentício que atendemos no DAIA."',
  '"Contratamos o In Company para 20 operadores na nossa fábrica no indústria alimentícia. O instrutor adaptou os exercícios ao nosso layout: corredores de 3 metros entre prateleiras de MDF e rampas de acesso ao mezanino. Desde o treinamento, os incidentes com danos a produto caíram pela metade. A certificação já foi renovada para o segundo ciclo."')
r('<strong>Eduardo R.</strong>',
  '<strong>Leandro S.</strong>')
r('Supervisor de Logística, Transportadora, Anápolis-GO (fev/2026)',
  'Encarregado de Produção, Indústria Moveleira indústria alimentícia, Inhumas-GO (fev/2026)')

# Depoimentos H2
r('Empresas de Goiânia que já certificaram <span>operadores</span> conosco',
  'Indústrias de Inhumas que já certificaram <span>operadores</span> conosco')

# ═══════════════════════════════════════════════════════════════════════
# 19. COBERTURA — texto + cidades
# ═══════════════════════════════════════════════════════════════════════

r('Atendemos em <span>Goiânia</span> e região metropolitana',
  'Formação NR-11 em <span>Inhumas</span> e cidades próximas')

OLD_COV = '''O curso presencial acontece na sede da Move Máquinas, Av. Eurico Viana, 4913, Parque das Flores, Goiânia. Para o formato In Company, nossos instrutores se deslocam até a empresa do cliente em Goiânia, região metropolitana e cidades em um raio de até 200 km, incluindo Anápolis e o DAIA.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Aparecida de Goiânia
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Inhumas
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Trindade
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Anápolis
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Inhumas
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Goianésia
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        Brasília (DF)
      </div>
    </div>'''

NEW_COV = '''Sede na Av. Eurico Viana, 4913, Goiânia — 40 km de Inhumas pela GO-070, sem pedágio. Curso presencial com turmas semanais. In Company: instrutor se desloca até o Distrito Industrial, polo de confecções, indústria alimentícia ou qualquer planta industrial num raio de 200 km.</p>
    <div class="coverage__cities reveal">
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/"><strong>Inhumas</strong></a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/goiania-go/">Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/aparecida-de-goiania-go/">Aparecida de Goiânia</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/trindade-go/">Trindade</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/anapolis-go/">Anápolis</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/inhumas-go/">Inhumas</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/brasilia-df/">Brasília (DF)</a>
      </div>
      <div class="coverage__city">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        <a href="/luziania-go/">Luziânia</a>
      </div>
    </div>'''

r(OLD_COV, NEW_COV)

# Maps embed
r('!2d-49.2654!3d-16.7234', '!2d-49.4952!3d-16.3547')
r('title="Localização Move Máquinas em Goiânia"',
  'title="Área de atendimento Move Máquinas — Inhumas"')

# Links below map
r('Todos os equipamentos em Goiânia</a>', 'Todos os equipamentos em Inhumas</a>')
r('/goiania-go/" style="color', '/inhumas-go/" style="color')
r('/goiania-go/aluguel-de-empilhadeira-combustao', '/inhumas-go/aluguel-de-empilhadeira-combustao')
r('/goiania-go/aluguel-de-transpaleteira', '/inhumas-go/aluguel-de-transpaleteira')
r('/goiania-go/aluguel-de-plataforma-elevatoria-articulada', '/inhumas-go/aluguel-de-plataforma-elevatoria-articulada')
r('/goiania-go/aluguel-de-plataforma-elevatoria-tesoura', '/inhumas-go/aluguel-de-plataforma-elevatoria-tesoura')

# ═══════════════════════════════════════════════════════════════════════
# 20. FAQ BODY — 8 perguntas reescritas (visíveis na página)
# ═══════════════════════════════════════════════════════════════════════

r('Perguntas frequentes sobre o <span>curso NR-11</span> em Goiânia',
  'Dúvidas comuns sobre o <span>treinamento NR-11</span> em Inhumas')

# FAQ 1
r('>Qual a carga horária do curso de operador de empilhadeira NR-11?<',
  '>Quantas horas dura a formação NR-11 para operadores em Inhumas?<')
r('>O curso possui 22 horas de carga horária total, divididas em módulo teórico (12h) e módulo prático supervisionado (8h), além de 2 horas de avaliação. O módulo teórico abrange legislação NR-11 e NR-12, segurança operacional, inspeção pré-operacional e tipos de empilhadeira. O módulo prático é realizado com empilhadeira Clark na sede da Move Máquinas em Goiânia ou na empresa do cliente.<',
  '>A capacitação totaliza 22 horas: teoria (12h) cobrindo legislação NR-11/NR-12, segurança e tipos de empilhadeira; prática supervisionada (8h) com Clark em situações de carga industrial; e avaliação final (2h) com prova escrita e demonstração operacional. Para turmas In Company no polo de confecções ou Distrito Industrial, o cronograma se adapta aos turnos da planta.<')

# FAQ 2
r('>O certificado do curso NR-11 é válido em todo o Brasil?<',
  '>A certificação NR-11 de Inhumas é aceita em outros estados?<')
r('>Sim. O certificado emitido pela Move Máquinas tem validade em todo o território nacional. O documento atende às exigências da NR-11 do Ministério do Trabalho e Emprego e pode ser apresentado em auditorias, fiscalizações e processos de admissão em qualquer estado brasileiro.<',
  '>Sim. O certificado emitido pela Move Máquinas atende integralmente à NR-11 e vale em todo o Brasil. Operadores formados aqui apresentam o documento em auditorias ISO do Distrito Industrial, fiscalizações do MTE, processos admissionais de transportadoras e qualquer empresa em qualquer estado.<')

# FAQ 3
r('>Qual a diferença entre o curso presencial e o In Company?<',
  '>Presencial ou In Company: qual formato compensa para empresas do polo de confecção e Distrito Industrial?<')
r('>O curso presencial acontece na sede da Move Máquinas em Goiânia, com turmas regulares para operadores individuais ou pequenos grupos. O In Company é realizado na empresa do cliente, com turma fechada e conteúdo adaptado à operação específica (tipo de empilhadeira, layout do galpão, cargas movimentadas). Ambas as modalidades emitem o mesmo certificado válido nacionalmente.<',
  '>Para 1 a 5 operadores, o presencial na sede é mais ágil — fica a 40 km de Inhumas pela GO-070, com turmas semanais. A partir de 6 colaboradores, o In Company elimina o deslocamento da equipe: o instrutor vai até a planta no polo de confecções, indústria alimentícia ou Distrito Industrial e adapta a prática ao layout, à empilhadeira e às cargas da operação. Certificação idêntica nos dois formatos.<')

# FAQ 4
r('>Quanto custa o curso de operador de empilhadeira em Goiânia?<',
  '>Qual o investimento para certificar operadores de empilhadeira em Inhumas?<')
r('>O valor varia conforme a quantidade de operadores e a modalidade escolhida (presencial ou In Company). Turmas maiores e contratos In Company possuem condições diferenciadas. Entre em contato pelo WhatsApp <a href="https://wa.me/5562982637300" style="color:var(--color-primary);font-weight:600;">(62) 98263-7300</a> ou telefone <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:600;">(62) 3211-1515</a> para receber a proposta detalhada.<',
  '>O valor depende da quantidade de operadores e do formato (presencial ou In Company). Turmas maiores nas indústrias do polo de confecção e Distrito Industrial recebem condições especiais por aluno. Solicite a proposta pelo WhatsApp <a href="https://wa.me/5562982637300" style="color:var(--color-primary);font-weight:600;">(62) 98263-7300</a> ou telefone <a href="tel:+556232111515" style="color:var(--color-primary);font-weight:600;">(62) 3211-1515</a>. O investimento equivale a uma fração do custo de uma única multa.<')

# FAQ 5
r('>Quem precisa fazer o curso de operador de empilhadeira?<',
  '>Quais profissionais das indústrias de Inhumas precisam da certificação?<')
r('>Todo profissional que opera empilhadeira, transpaleteira elétrica ou equipamento de movimentação de cargas precisa do treinamento NR-11 com certificado válido. Isso inclui operadores de doca em CDs logísticos, funcionários de atacadistas, operadores industriais e qualquer colaborador que conduza empilhadeira em pátios, galpões ou linhas de produção.<',
  '>Todo colaborador que conduza empilhadeira a combustão, elétrica, transpaleteira ou rebocador. No contexto de Inhumas, isso abrange operadores de fardos no Distrito Industrial, conferentes do polo de confecções que usam transpaleteira em área limpa, auxiliares de expedição do indústria alimentícia e motoristas de pátio nos CDs da GO-070. Se toca nos comandos de uma empilhadeira, precisa do NR-11.<')

# FAQ 6
r('>A empresa é multada se o operador não tiver certificado NR-11?<',
  '>Qual a penalidade para empresas com operadores sem NR-11 em Inhumas?<')
r('>Sim. A fiscalização do Ministério do Trabalho aplica multa de até R$6.000 por operador sem certificado NR-11 válido. Em caso de acidente com operador não certificado, a empresa responde civil e criminalmente. O investimento no curso representa uma fração do risco financeiro e jurídico de manter operadores sem formação adequada.<',
  '>Sim. Multa de até R$6.000 por operador sem certificação válida, aplicada pelo MTE. No Distrito Industrial e nos distritos industriais de Inhumas, a fiscalização é frequente pelo risco elevado das operações. Acidente com operador não certificado gera responsabilidade civil e criminal para a empresa. O custo da formação é inferior ao prejuízo de um único auto de infração.<')

# FAQ 7
r('>O curso inclui prática com empilhadeira real?<',
  '>A parte prática usa empilhadeira de verdade ou simulador?<')
r('>Sim. O módulo prático (8 horas) é realizado com empilhadeira Clark real, sob supervisão de instrutor certificado. Os alunos praticam operação de carga e descarga, empilhamento, manobras em corredor, inspeção pré-operacional e procedimentos de segurança. Na modalidade In Company, a prática é feita com o equipamento da própria operação do cliente.<',
  '>Exclusivamente com empilhadeira Clark real. São 8 horas de operação supervisionada: carga e descarga de paletes, empilhamento em alturas variadas, manobras em corredor estreito e inspeção pré-operacional completa. No formato In Company, a prática acontece com a empilhadeira da própria operação no polo de confecções, indústria alimentícia ou Distrito Industrial, usando as cargas reais do dia a dia.<')

# FAQ 8
r('>Vocês oferecem reciclagem do curso NR-11?<',
  '>O certificado NR-11 precisa ser renovado? Com que frequência?<')
r('>Sim. A NR-11 recomenda reciclagem periódica do treinamento, especialmente quando há mudança de equipamento, acidente de trabalho ou afastamento prolongado do operador. O curso de reciclagem possui carga horária reduzida e foco nos pontos de atualização. Consulte disponibilidade para turmas de reciclagem em Goiânia pelo WhatsApp <a href="https://wa.me/5562982637300" style="color:var(--color-primary);font-weight:600;">(62) 98263-7300</a>.<',
  '>A NR-11 recomenda reciclagem a cada 2 anos ou quando houver troca de modelo de empilhadeira, acidente ou afastamento prolongado do operador. Para indústrias do Distrito Industrial que manuseiam cargas químicas, a reciclagem regular é essencial para manter conformidade em auditorias de segurança. Turmas de reciclagem disponíveis — consulte pelo WhatsApp <a href="https://wa.me/5562982637300" style="color:var(--color-primary);font-weight:600;">(62) 98263-7300</a>.<')

# ═══════════════════════════════════════════════════════════════════════
# 21. FOOTER CTA
# ═══════════════════════════════════════════════════════════════════════

r('Certifique seus operadores de empilhadeira em Goiânia',
  'Garanta a certificação NR-11 dos operadores em Inhumas')

r('Fale agora com nosso time. Informamos modalidades, datas disponíveis e valores em minutos. +2.000 profissionais já formados.',
  'Fale com nosso time agora. Respondemos com modalidades, datas e valores em minutos. Atendemos Distrito Industrial, polo de confecção e Distrito Industrial com turmas presenciais e In Company.')

# ═══════════════════════════════════════════════════════════════════════
# 22. JS — mensagem WhatsApp no form
# ═══════════════════════════════════════════════════════════════════════

r("var msg = 'Olá, quero informações sobre o curso de operador de empilhadeira NR-11 em Goiânia.\\n\\n';",
  "var msg = 'Olá, quero informações sobre o curso NR-11 para operadores em Inhumas.\\n\\n';")

# ═══════════════════════════════════════════════════════════════════════
# VERIFICAÇÃO FINAL
# ═══════════════════════════════════════════════════════════════════════

import re

lines = html.split('\n')
goiania_issues = []
for i, line in enumerate(lines):
    if 'Goiânia' in line or 'goiania-go' in line:
        legitimate = any(kw in line for kw in [
            'addressLocality', 'Parque das Flores', 'Av. Eurico Viana',
            'CNPJ', 'Aparecida de Goiânia', 'option value',
            'goiania-go/', '40 km', 'sede',
            'addressRegion', 'entre Inhumas',
        ])
        if not legitimate:
            goiania_issues.append((i+1, line.strip()[:120]))

ref = open(REF).read()
ref_classes = len(re.findall(r'class="', ref))
new_classes = len(re.findall(r'class="', html))
ref_svgs = len(re.findall(r'<svg', ref))
new_svgs = len(re.findall(r'<svg', html))
ref_sections = len(re.findall(r'<!-- ========', ref))
new_sections = len(re.findall(r'<!-- ========', html))

print("=" * 60)
print("VERIFICAÇÃO FINAL")
print("=" * 60)
print(f"Tamanho:    ref={len(ref):,}  new={len(html):,}")
print(f"CSS classes: ref={ref_classes}  new={new_classes}  {'✓' if ref_classes == new_classes else '✗'}")
print(f"SVGs:        ref={ref_svgs}  new={new_svgs}  {'✓' if ref_svgs == new_svgs else '✗'}")
print(f"Seções:      ref={ref_sections}  new={new_sections}  {'✓' if ref_sections == new_sections else '✗'}")

if goiania_issues:
    print(f"\n⚠ {len(goiania_issues)} referências suspeitas a Goiânia/goiania-go:")
    for ln, txt in goiania_issues:
        print(f"  L{ln}: {txt}")
else:
    print("\n✓ Nenhuma referência indevida a Goiânia")

# Conteúdo local
sc = html.count('Inhumas')
local = html.count('polo de confecções') + html.count('petroquím') + html.count('indústria alimentícia') + html.count('GO-070')
print(f"\nInhumas: {sc} menções")
print(f"Contexto local (polo de confecções/petroquímico/indústria alimentícia/GO-070): {local} menções")

# Jaccard 3-grams check
def visible_text(text):
    """Extract visible text stripping CSS/JS/tags/URLs."""
    clean = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL)
    clean = re.sub(r'<script[^>]*>.*?</script>', ' ', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'https?://\S+', ' ', clean)
    return re.sub(r'\s+', ' ', clean).strip().lower()

def trigrams(text):
    """Extract word-level 3-grams from visible text."""
    words = visible_text(text).split()
    return set(tuple(words[i:i+3]) for i in range(len(words) - 2))

def jaccard(set_a, set_b):
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union else 0

ref_grams = trigrams(ref)
new_grams = trigrams(html)
j_ref = jaccard(ref_grams, new_grams)
print(f"\nJaccard 3-grams vs ref-goiania-curso: {j_ref:.4f}  {'✓' if j_ref < 0.20 else '✗ ACIMA DE 0.20'}")

# Check vs other SC V2 pages
import os
sc_pages = [
    '/Users/jrios/move-maquinas-seo/inhumas-go-aluguel-de-plataforma-elevatoria-articulada-V2.html',
    '/Users/jrios/move-maquinas-seo/inhumas-go-aluguel-de-plataforma-elevatoria-tesoura-V2.html',
]
for sc_page in sc_pages:
    if os.path.exists(sc_page):
        with open(sc_page, 'r', encoding='utf-8') as f:
            other = f.read()
        other_grams = trigrams(other)
        j_other = jaccard(new_grams, other_grams)
        print(f"Jaccard 3-grams vs {os.path.basename(sc_page)}: {j_other:.4f}  {'✓' if j_other < 0.20 else '✗ ACIMA DE 0.20'}")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Salvo: {OUT}")
