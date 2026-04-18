import re, os, boto3

BASE = '/Users/jrios/move-maquinas-seo'

def extract_text(html):
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<script type="application/ld\+json">.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&[a-zA-Z]+;', ' ', text)
    return re.sub(r'\s+', ' ', text).strip().lower()

def jaccard(t1, t2, n=3):
    w1, w2 = t1.split(), t2.split()
    ng1 = set(tuple(w1[i:i+n]) for i in range(len(w1)-n+1))
    ng2 = set(tuple(w2[i:i+n]) for i in range(len(w2)-n+1))
    return len(ng1 & ng2) / len(ng1 | ng2) if (ng1 | ng2) else 0

# === INCLUSO items to replace ===
INCLUSO_INTRO = '+20 anos no mercado goiano nos ensinaram que o diferencial não é a paleteira. É o que acontece quando o equipamento chega.'
INCLUSO_BAT = 'Bateria com recarga rápida de 2 a 3 horas. Monitoramento de ciclos de carga e substituição sem custo se a autonomia cair abaixo do mínimo operacional.'
INCLUSO_MANUT = 'Revisão periódica do motor de tração, bomba hidráulica, vedações e mangueiras. Troca de fluido conforme fabricante. Se a paleteira parar, substituímos no mesmo dia.'
INCLUSO_RODAS = 'Rodas de carga e direção verificadas antes da entrega. Garfos com inspeção de desgaste e alinhamento. Troca preventiva para evitar parada não programada.'
INCLUSO_CONSUL = 'Nosso time ajuda a escolher entre walkie, plataforma, stacker ou heavy duty para sua operação. Avaliamos layout do armazém, peso médio dos paletes e fluxo de movimentação.'

# === COMPARATIVO items ===
COMP_INTRO = 'A paleteira manual resolve operações esporádicas. Para volumes acima de 30 paletes por turno, fluxos contínuos e distâncias acima de 20 metros, a elétrica reduz tempo, fadiga e custo.'
COMP_ELETRICA = 'Motor de tração e bomba hidráulica eliminam esforço físico. Bateria de lítio com recarga rápida para turnos contínuos. Velocidade de até 6 km/h em modo transporte.'
COMP_MANUAL = 'Sem motor, sem bateria. O operador traciona e eleva o palete com esforço muscular. Funcional para volumes baixos e distâncias curtas dentro do mesmo corredor.'

# === FOOTER CTA ===
FOOTER_CTA = 'Fale agora com nosso time. Informamos disponibilidade, modelo, valor e prazo de entrega em minutos.'

# Replacements per city
data = {
    'luziania-go': {
        'incluso_intro': 'Duas décadas atendendo o DIAL nos mostraram que a diferença está no suporte, não só no equipamento. Cada locação inclui tudo o que mantém sua operação sem interrupção.',
        'incluso_bat': 'Baterias de lítio 24V com ciclo de recarga de 90 minutos a 2 horas. Acompanhamos a saúde da célula e trocamos gratuitamente se a autonomia não cobrir o turno completo.',
        'incluso_manut': 'Manutenção programada de motor, bomba e vedações conforme manual Clark. Lubrificação de roletes e corrente incluída. Falha inesperada? Substituição do equipamento no mesmo dia.',
        'incluso_rodas': 'Rodas e garfos inspecionados na entrega e em cada visita técnica. Troca preventiva quando o desgaste atinge o limite — sem esperar quebra para agir.',
        'incluso_consul': 'Antes de enviar a transpaleteira, nosso técnico analisa o layout do armazém, o peso médio das cargas e o fluxo de movimentação para indicar o modelo certo.',
        'comp_intro': 'Mover paletes manualmente funciona para demandas pontuais. Quando o DIAL exige ritmo de produção com dezenas de paletes por turno e trajetos longos até as docas, só a elétrica sustenta.',
        'comp_eletrica': 'Tração motorizada e elevação hidráulica eliminam o esforço braçal. Bateria lítio com recarga rápida cobre o turno inteiro. Velocidade de transporte chega a 6 km/h.',
        'comp_manual': 'Operação 100% manual: o trabalhador puxa e bombeia para elevar. Serve para distâncias curtas e volumes esporádicos dentro de um único corredor.',
        'footer_cta': 'Entre em contato agora. Respondemos com disponibilidade, modelo recomendado, valor mensal e prazo para entrega no DIAL.',
    },
    'trindade-go': {
        'incluso_intro': 'Mais de vinte anos equipando operações no Centro-Oeste nos provaram que o contrato de locação precisa cobrir muito além da máquina. Cada item abaixo faz parte.',
        'incluso_bat': 'Lítio 24V com tempo de carga entre 90 min e 2h30. Monitoramos o desempenho da bateria e substituímos sem custo extra se o rendimento cair antes do fim do turno.',
        'incluso_manut': 'Cronograma de manutenção seguindo especificação Clark: motor de tração, vedações hidráulicas e rolamentos. Se a máquina falhar em campo, trocamos por outra no mesmo expediente.',
        'incluso_rodas': 'Inspeção de rodízios e garfos a cada ciclo de manutenção. Peças com desgaste próximo do limite são substituídas preventivamente — zero parada surpresa.',
        'incluso_consul': 'Nosso consultor avalia o galpão, o tipo de palete e o volume diário antes de indicar walkie, plataforma ou stacker. Escolha técnica, não genérica.',
        'comp_intro': 'A paleteira manual atende movimentações pontuais dentro de um corredor. Para centros de distribuição da GO-060, onde o fluxo é contínuo e as distâncias são longas, a elétrica é indispensável.',
        'comp_eletrica': 'Motor elétrico e bomba hidráulica fazem o trabalho pesado. Lítio com recarga rápida mantém a operação sem pausa. Transporte a até 6 km/h entre recebimento e expedição.',
        'comp_manual': 'Zero componente elétrico: tração humana e bombeamento manual. Adequada para ajustes pontuais de palete em distâncias inferiores a 15 metros.',
        'footer_cta': 'Fale com a equipe agora. Retornamos com modelo indicado, valor, disponibilidade e data de entrega para seu galpão em Trindade.',
    },
    'inhumas-go': {
        'incluso_intro': 'Décadas fornecendo equipamentos para o setor produtivo de Goiás nos ensinaram: o que sustenta a locação é o serviço ao redor do equipamento. Tudo incluído no contrato.',
        'incluso_bat': 'Célula de lítio 24V recarrega em até 2 horas. Acompanhamos a capacidade real e trocamos a bateria gratuitamente quando ela não mantiver autonomia para o turno completo na fábrica.',
        'incluso_manut': 'Programa de revisão conforme manual Clark: motor, bomba, vedações, fluido hidráulico. Se o equipamento parar na linha de confecção, enviamos substituto no mesmo dia.',
        'incluso_rodas': 'Rodízios e garfos vistoriados na entrega e nas visitas periódicas. Fardos de tecido exigem garfos sem rebarba — qualquer imperfeição é corrigida antes de chegar à fábrica.',
        'incluso_consul': 'Analisamos o layout da fábrica, o peso médio dos fardos e a frequência de movimentação para recomendar o modelo adequado. Nem subdimensionado, nem além do necessário.',
        'comp_intro': 'Para mover um ou dois fardos entre estações, a manual basta. Quando a produção têxtil demanda dezenas de fardos por turno e trajetos entre estoque e expedição, a elétrica é a resposta.',
        'comp_eletrica': 'Tração e elevação motorizadas liberam o operador do esforço repetitivo. Lítio recarrega rápido, mantendo o fluxo entre corte, costura e embalagem sem interrupção.',
        'comp_manual': 'Sem motor nem bateria. O operador empurra e bombeia o palete. Funcional para repositar um fardo próximo à estação de trabalho, nada além disso.',
        'footer_cta': 'Fale com nosso time agora. Enviamos modelo recomendado, valor mensal e prazo de entrega para o Distrito Industrial de Inhumas.',
    },
    'itumbiara-go': {
        'incluso_intro': 'Operar dentro de câmara fria ou em docas de frigorífico exige mais do que um equipamento funcional. Cada contrato de locação cobre o ecossistema completo de suporte.',
        'incluso_bat': 'Bateria lítio projetada para ciclos em ambiente refrigerado. Recarga de 60 a 120 minutos. Se a autonomia cair em condição de frio extremo, fazemos a troca imediata.',
        'incluso_manut': 'Revisão técnica incluindo motor, vedações e bomba — com atenção especial à corrosão causada por umidade de câmara fria. Substituição do equipamento se houver parada.',
        'incluso_rodas': 'Rodízios e garfos inspecionados contra acúmulo de gelo e oxidação. Troca preventiva de peças antes que o desgaste comprometa a tração no piso molhado do frigorífico.',
        'incluso_consul': 'Avaliamos se a operação precisa de modelo com proteção contra respingos, garfos em inox ou bateria lítio de alta descarga para câmara fria. Recomendação técnica personalizada.',
        'comp_intro': 'A paleteira manual funciona para posicionar um palete esporádico na doca. Dentro dos frigoríficos do DIAGRI, onde o frio e o volume impõem ritmo, só a elétrica com lítio opera de forma contínua.',
        'comp_eletrica': 'Motor de tração e elevação hidráulica evitam esforço repetitivo no frio. Bateria lítio com recarga rápida, sem perda de rendimento em temperatura negativa.',
        'comp_manual': 'Tração e elevação exclusivamente manuais. O operador precisa fazer força a cada palete — inviável em turnos longos dentro de câmara a -18°C.',
        'footer_cta': 'Entre em contato agora. Respondemos com disponibilidade de modelo para câmara fria, valor e data de entrega no DIAGRI.',
    },
    'caldas-novas-go': {
        'incluso_intro': 'Em ambiente hoteleiro, o equipamento precisa funcionar sem falhas, sem ruído e sem comprometer a experiência do hóspede. Cada locação inclui suporte integral.',
        'incluso_bat': 'Lítio 24V com recarga silenciosa de 90 minutos. Monitoramos a capacidade e substituímos a bateria gratuitamente se ela não cobrir o turno de reposição do estoque.',
        'incluso_manut': 'Manutenção preventiva de motor, bomba e vedações seguindo calendário Clark. Em caso de falha, enviamos técnico ou equipamento reserva sem interromper a operação do hotel.',
        'incluso_rodas': 'Rodízios especiais que não marcam piso e garfos sem rebarbas, verificados antes da entrega. Qualquer peça com desgaste é trocada para proteger o acabamento do resort.',
        'incluso_consul': 'Consultoria para definir o modelo ideal: walkie compacta para almoxarifado, plataforma para cozinha industrial ou stacker para estoque vertical. Decisão baseada no seu espaço.',
        'comp_intro': 'Para reposicionar uma caixa no almoxarifado, a manual serve. Quando o resort precisa repor estoque de cozinha, lavanderia e frigobar todos os dias, a elétrica transforma o tempo da equipe.',
        'comp_eletrica': 'Operação silenciosa e sem emissão — requisito básico em hotéis. Motor elétrico com lítio cobre reposições de turno inteiro sem pausa para recarga.',
        'comp_manual': 'Totalmente manual, sem motor. O funcionário puxa e eleva com esforço próprio. Aceitável para ajustes rápidos, impraticável para reposição diária de estoque hoteleiro.',
        'footer_cta': 'Solicite orçamento agora. Informamos modelo ideal para seu resort, valor mensal e prazo de entrega em Caldas Novas.',
    },
    'formosa-go': {
        'incluso_intro': 'No agronegócio, parada de equipamento significa caminhão esperando e safra atrasada. Cada contrato de locação da Move cobre tudo para manter o fluxo de sacas e paletes.',
        'incluso_bat': 'Lítio 24V com autonomia para turnos de armazém graneleiro. Recarga entre 90 e 150 minutos. Troca gratuita da célula se o rendimento cair abaixo do mínimo operacional.',
        'incluso_manut': 'Revisão de motor de tração, bomba, vedações e corrente conforme especificação Clark. Ambiente com poeira de grão exige atenção extra — cobrimos isso sem custo adicional.',
        'incluso_rodas': 'Rodízios resistentes a piso irregular de armazém e garfos dimensionados para sacas de 60 kg. Inspeção preventiva em cada visita técnica para evitar parada na safra.',
        'incluso_consul': 'Nosso técnico avalia o tipo de carga (sacas, big bags, paletes de insumo), a distância até os caminhões e o volume diário para indicar o modelo correto.',
        'comp_intro': 'A manual atende para posicionar um palete avulso. Em safra, quando armazéns de Formosa movem centenas de sacas por dia e caminhões aguardam na doca, só a elétrica mantém o ritmo.',
        'comp_eletrica': 'Tração motorizada e elevação hidráulica tiram o peso do operador. Lítio recarrega rápido entre turnos, garantindo fluxo contínuo entre silo, balança e caminhão.',
        'comp_manual': 'Sem componente elétrico. O trabalhador empurra e bombeia. Funcional para mover um palete isolado dentro do mesmo corredor do armazém.',
        'footer_cta': 'Fale agora com a equipe. Enviamos modelo adequado para armazém, valor e prazo de entrega para Formosa e região.',
    },
    'uruacu-go': {
        'incluso_intro': 'Frigoríficos e laticínios do Distrito Agroindustrial precisam de equipamento que funcione em frio extremo e ritmo intenso. O contrato cobre todo o suporte para isso.',
        'incluso_bat': 'Lítio 24V otimizada para operação em baixa temperatura. Recarga de 60 a 120 min. Monitoramento contínuo da saúde da bateria com troca gratuita se o desempenho cair.',
        'incluso_manut': 'Manutenção especializada para ambiente de frigorífico: vedações anticorrosão, lubrificação para frio e revisão de motor. Se o equipamento parar, enviamos substituto imediato.',
        'incluso_rodas': 'Rodas com aderência para piso úmido de frigorífico e garfos verificados contra oxidação. Troca preventiva de componentes expostos a ambiente refrigerado.',
        'incluso_consul': 'Avaliamos o circuito entre câmara fria, sala de cortes e doca de expedição para recomendar o modelo com autonomia e proteção adequadas ao seu frigorífico.',
        'comp_intro': 'A manual pode mover um palete ocasional na doca seca. Dentro dos frigoríficos de Uruaçu, com piso úmido e temperatura de -12°C, somente a elétrica lítio mantém produtividade.',
        'comp_eletrica': 'Motor e bomba eliminam esforço do operador vestido com roupa térmica pesada. Lítio mantém performance mesmo em frio, com recarga rápida entre turnos de abate.',
        'comp_manual': 'Totalmente dependente de força humana. No frio do frigorífico, com luvas térmicas e vestimenta pesada, o rendimento cai drasticamente — inviável para produção contínua.',
        'footer_cta': 'Solicite cotação agora. Respondemos com modelo indicado para frigorífico, valor e data de entrega no Distrito Agroindustrial de Uruaçu.',
    },
    'valparaiso-de-goias-go': {
        'incluso_intro': 'Fábricas de móveis e galpões comerciais do entorno do DF precisam de equipamento confiável e suporte rápido. O contrato de locação inclui cada item listado abaixo.',
        'incluso_bat': 'Bateria lítio 24V com recarga de 90 a 120 minutos. Monitoramos o desempenho da célula e fazemos a troca sem custo se a autonomia não cobrir o turno na fábrica.',
        'incluso_manut': 'Manutenção programada de motor, bomba, vedações e corrente conforme calendário Clark. Lascas de MDF podem travar rodízios — cobrimos essa limpeza na visita técnica.',
        'incluso_rodas': 'Rodas e garfos verificados antes da entrega. Ambiente moveleiro com resíduos de madeira exige inspeção frequente — fazemos isso em cada visita programada.',
        'incluso_consul': 'Nosso consultor avalia o peso das chapas, a largura dos corredores e o fluxo entre linhas de montagem para indicar o modelo exato que sua fábrica precisa.',
        'comp_intro': 'Para reposicionar uma chapa na bancada, a manual basta. Quando o polo moveleiro demanda dezenas de paletes de MDF por turno entre estoque e linhas de corte, a elétrica é obrigatória.',
        'comp_eletrica': 'Motor de tração e elevação hidráulica movem chapas pesadas sem esforço do operador. Lítio com recarga rápida cobre turnos consecutivos na fábrica.',
        'comp_manual': 'Sem motor. O marceneiro puxa e bombeia o palete manualmente. Viável para um ajuste pontual, impossível para fluxo contínuo de chapas entre setores.',
        'footer_cta': 'Fale com nosso time agora. Enviamos modelo recomendado para fábrica de móveis, valor mensal e prazo de entrega na BR-040.',
    },
}

r2 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto')

ref_text = extract_text(open(f'{BASE}/ref-goiania-transpaleteira.html').read())
sc_text = extract_text(open(f'{BASE}/senador-canedo-go-aluguel-de-transpaleteira-V2.html').read())
bsb_text = extract_text(open(f'{BASE}/brasilia-df-aluguel-de-transpaleteira-V2.html').read())

slug = 'aluguel-de-transpaleteira'

for city, replacements in data.items():
    fn = f'{BASE}/{city}-{slug}-V2.html'
    html = open(fn).read()
    
    html = html.replace(INCLUSO_INTRO, replacements['incluso_intro'])
    html = html.replace(INCLUSO_BAT, replacements['incluso_bat'])
    html = html.replace(INCLUSO_MANUT, replacements['incluso_manut'])
    html = html.replace(INCLUSO_RODAS, replacements['incluso_rodas'])
    html = html.replace(INCLUSO_CONSUL, replacements['incluso_consul'])
    html = html.replace(COMP_INTRO, replacements['comp_intro'])
    html = html.replace(COMP_ELETRICA, replacements['comp_eletrica'])
    html = html.replace(COMP_MANUAL, replacements['comp_manual'])
    html = html.replace(FOOTER_CTA, replacements['footer_cta'])
    
    open(fn, 'w').write(html)
    
    new_text = extract_text(html)
    j_ref = jaccard(ref_text, new_text, 3)
    j_sc = jaccard(sc_text, new_text, 3)
    j_bsb = jaccard(bsb_text, new_text, 3)
    worst = max(j_ref, j_sc, j_bsb)
    ok = '✓' if worst < 0.20 else '✗'
    
    r2.put_object(Bucket='pages', Key=f'{city}/{slug}/index.html', Body=html.encode(), ContentType='text/html; charset=utf-8')
    
    print(f"  {ok} {city:<28} ref={j_ref:.4f} sc={j_sc:.4f} bsb={j_bsb:.4f}")

