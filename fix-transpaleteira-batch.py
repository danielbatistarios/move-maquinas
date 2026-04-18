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

# NR-35 checklist items (identical across all V2s)
NR_ITEMS_OLD = [
    'Curso de operador de equipamento de movimentação com certificado válido (reciclagem periódica)',
    'Inspeção pré-operacional antes de cada turno (bateria, rodas, garfos, freios, timão)',
    'Respeito à capacidade de carga nominal indicada na plaqueta do equipamento',
    'Velocidade controlada em áreas de circulação de pedestres e cruzamentos de corredores',
    'Uso de calçado de segurança e atenção ao posicionamento dos pés em relação ao chassi',
]

# NR-35 steps (also identical)
NR_STEPS_OLD = [
    'Inspecione rodas, garfos e freio. Confirme carga da bateria acima de 30%.',
    'Posicione os garfos na base correta do palete, respeitando o centro de carga.',
    'Eleve apenas o suficiente para liberar o solo (5 a 8 cm) e transporte devagar.',
    'No destino, alinhe e desça a carga suavemente. Nunca abandone o equipamento ligado.',
]

# Per-city unique NR content
NR_ITEMS_NEW = {
    'luziania-go': [
        'Habilitação válida como operador de equipamento de movimentação — renovação obrigatória conforme calendário do DIAL',
        'Checklist visual antes de ligar: condição dos garfos, nível de carga da bateria, funcionamento do freio e buzina',
        'Carga máxima respeitada conforme plaqueta do modelo — sobrecarga danifica o sistema hidráulico e anula garantia',
        'Deslocamento reduzido nos cruzamentos entre corredores de armazéns e nas proximidades de docas de carregamento',
        'Equipamento de proteção individual obrigatório: botina com biqueira de aço e luvas para manuseio de paletes',
    ],
    'trindade-go': [
        'Certificação atualizada de operador de transpaleteira conforme NR-11 — exigência dos CDs ao longo da GO-060',
        'Verificação pré-turno: estado dos roletes, tensão da corrente, resposta do freio e indicador de bateria',
        'Limite de peso conforme especificação técnica do modelo — excesso compromete estabilidade em rampas de doca',
        'Velocidade máxima de 5 km/h em áreas internas com trânsito de pedestres e empilhadeiras',
        'Proteção pessoal mandatória: calçado de segurança com solado antiderrapante e colete refletivo em áreas de carga',
    ],
    'inhumas-go': [
        'Credenciamento de operador válido para movimentação de carga — requisito das indústrias têxteis do Distrito Industrial',
        'Rotina de inspeção antes de cada uso: garfos alinhados, bateria acima de 40%, pneus sem desgaste irregular',
        'Tonelagem nominal do equipamento sempre respeitada — fardos de tecido variam de 200 a 500 kg por unidade',
        'Circulação controlada entre as estações de corte e costura onde operários transitam a pé',
        'EPI completo: bota de segurança, luva de raspa para manusear fardos e protetor auricular em áreas de tecelagem',
    ],
    'itumbiara-go': [
        'Operador certificado conforme NR-11 e treinamento adicional de câmara fria — exigência dos frigoríficos JBS e BRF',
        'Inspeção rigorosa antes de entrar na câmara: bateria lítio com carga mínima de 50%, garfos limpos de gelo, freio testado',
        'Capacidade de carga obedecida à risca — caixas de cortes congelados pesam até 25 kg cada, paletes chegam a 1.200 kg',
        'Movimentação lenta dentro da câmara fria (-18°C) onde o piso pode ter condensação e visibilidade é reduzida',
        'Vestimenta térmica completa para operação em ambiente refrigerado, incluindo luva térmica e bota isolante',
    ],
    'caldas-novas-go': [
        'Autorização formal do hotel ou resort para operação de transpaleteira em áreas de estoque e cozinha',
        'Checagem diária: rodízios silenciosos em bom estado, bateria carregada, garfos sem rebarbas que danifiquem pisos',
        'Peso máximo respeitado conforme plaqueta — paletes de alimentos para buffet podem chegar a 800 kg',
        'Trânsito limitado ao corredor de serviço, longe das áreas de circulação de hóspedes e funcionários de atendimento',
        'Uso de calçado fechado antiderrapante e avental — padrão das cozinhas industriais dos resorts de Caldas Novas',
    ],
    'formosa-go': [
        'Documento de habilitação como operador válido — cooperativas agrícolas de Formosa exigem comprovação atualizada',
        'Vistoria pré-operação: integridade dos garfos para sacaria, carga da bateria, resposta do sistema de frenagem',
        'Capacidade nominal do modelo respeitada sem exceção — sacas de grãos pesam 60 kg, big bags chegam a 1.000 kg',
        'Percurso delimitado entre silos e caminhões, com velocidade reduzida nos trechos onde tratores e caminhões manobram',
        'Proteção individual: bota com biqueira de aço, luva de algodão para manuseio de sacas e máscara contra poeira de grãos',
    ],
    'uruacu-go': [
        'Treinamento específico para operação em ambiente frigorífico e laticínio — exigência das 31 empresas do Distrito Agroindustrial',
        'Protocolo de inspeção adaptado ao frio: verificação de bateria lítio, lubrificação dos roletes e teste de freio em piso úmido',
        'Tonelagem do modelo nunca ultrapassada — caixas de frango e cortes suínos montam paletes de até 1.100 kg',
        'Deslocamento cauteloso nas áreas de expedição onde empilhadeiras e caminhões baú operam simultaneamente',
        'Vestimenta de câmara fria obrigatória para operadores que transitam entre área seca e ambiente refrigerado a -12°C',
    ],
    'valparaiso-de-goias-go': [
        'Comprovante de qualificação como operador de transpaleteira — exigência das fábricas do polo moveleiro da BR-040',
        'Revisão antes de cada turno: garfos sem empenamento, rodízios livres de lascas de MDF, bateria funcional',
        'Carga nominal do equipamento sempre obedecida — chapas de MDF empilhadas chegam a 900 kg por palete',
        'Velocidade controlada nos corredores entre linhas de montagem onde marceneiros trabalham com ferramentas elétricas',
        'Bota de segurança com biqueira reforçada e óculos de proteção nas áreas de corte e acabamento de painéis',
    ],
}

# NR steps per city
NR_STEPS_NEW = {
    'luziania-go': [
        'Confira a carga da bateria e faça o checklist visual de garfos, rodas e freio antes de iniciar.',
        'Insira os garfos centralizados nas aberturas do palete, respeitando a marcação de centro de carga.',
        'Levante a carga apenas o necessário para folga do piso (5-8 cm) e desloque em velocidade reduzida.',
        'Posicione no local de destino, baixe a carga com suavidade e remova os garfos antes de estacionar.',
    ],
    'trindade-go': [
        'Verifique bateria, buzina e freio. Confirme que o percurso está desobstruído até o ponto de entrega.',
        'Alinhe a transpaleteira de frente para o palete e insira os garfos até o fim das aberturas.',
        'Erga a carga no mínimo necessário para vencer o desnível do piso e prossiga sem aceleração brusca.',
        'Ao chegar, desça o palete lentamente, recue a máquina e estacione com garfos abaixados.',
    ],
    'inhumas-go': [
        'Teste o freio e confirme que a bateria tem carga para o trajeto completo entre estoque e expedição.',
        'Posicione os garfos rente ao solo e avance sob o palete de fardos até a trava de encaixe.',
        'Eleve somente o suficiente para desgrudar do chão e transporte mantendo o fardo estável.',
        'Deposite na área de expedição, baixe devagar para não tombar o fardo e recolha os garfos.',
    ],
    'itumbiara-go': [
        'Fora da câmara, confirme bateria lítio acima de 50% e limpe gelo acumulado nos garfos.',
        'Dentro da câmara, insira os garfos alinhados ao palete e verifique se não há caixas deslocadas.',
        'Eleve o mínimo para transitar e mantenha velocidade reduzida — piso de câmara fria pode ter condensação.',
        'Posicione na doca de expedição, baixe devagar e retorne à câmara para o próximo palete.',
    ],
    'caldas-novas-go': [
        'Confira que os rodízios silenciosos giram livremente e a bateria tem carga para o turno de reposição.',
        'Posicione a transpaleteira em frente ao palete no estoque e encaixe os garfos nas aberturas centrais.',
        'Eleve apenas o necessário para deslocar o palete sem riscar o piso da área de serviço do resort.',
        'Entregue na cozinha ou lavanderia, baixe com cuidado e estacione no ponto designado pelo hotel.',
    ],
    'formosa-go': [
        'Revise garfos e bateria antes de entrar no armazém graneleiro — poeira de grãos exige atenção extra.',
        'Aproxime-se do palete de sacas pela frente, encaixe os garfos e verifique que a carga está estável.',
        'Erga o palete rente ao solo e percorra o trajeto até o caminhão em velocidade de passo.',
        'Posicione na carroceria do caminhão ou na área de estoque, desça suavemente e recue a máquina.',
    ],
    'uruacu-go': [
        'Antes de cada entrada na câmara fria, confirme carga de bateria e lubrifique os garfos contra oxidação.',
        'Insira os garfos sob o palete de caixas de frango ou suínos, certificando que estão centralizados.',
        'Levante o mínimo para liberar o piso e desloque devagar — visibilidade dentro do frigorífico é reduzida.',
        'Transfira para a doca de expedição, baixe o palete com suavidade e volte para buscar o próximo.',
    ],
    'valparaiso-de-goias-go': [
        'Inspecione garfos e rodízios — lascas de MDF podem travar as rodas. Confirme bateria carregada.',
        'Alinhe a transpaleteira ao palete de chapas, insira os garfos devagar para não deslocar as peças.',
        'Eleve apenas o suficiente para folga do piso e transporte sem inclinação para evitar tombamento de chapas.',
        'No ponto de entrega, baixe o palete alinhado à linha de montagem e recolha os garfos cuidadosamente.',
    ],
}

# Comparativo section text to replace
COMP_OLD = 'Transpaleteira Elétrica (Lítio 24V)'
COMP_NEW = {
    'luziania-go': 'Transpaleteira Lítio 24V para Armazéns',
    'trindade-go': 'Transpaleteira Lítio 24V para CDs',
    'inhumas-go': 'Transpaleteira Lítio 24V Têxtil',
    'itumbiara-go': 'Transpaleteira Lítio 24V Câmara Fria',
    'caldas-novas-go': 'Transpaleteira Lítio 24V Hotelaria',
    'formosa-go': 'Transpaleteira Lítio 24V Agrícola',
    'uruacu-go': 'Transpaleteira Lítio 24V Frigorífica',
    'valparaiso-de-goias-go': 'Transpaleteira Lítio 24V Moveleira',
}

# Price CTA text
PRICE_OLD = 'Cotar transpaleteira Clark agora'
PRICE_NEW = {
    'luziania-go': 'Solicitar cotação para o DIAL',
    'trindade-go': 'Pedir orçamento para Trindade',
    'inhumas-go': 'Cotar para indústria têxtil',
    'itumbiara-go': 'Orçamento para frigorífico',
    'caldas-novas-go': 'Cotação para resort ou hotel',
    'formosa-go': 'Orçar para armazém graneleiro',
    'uruacu-go': 'Cotar para Distrito Agroindustrial',
    'valparaiso-de-goias-go': 'Orçamento para polo moveleiro',
}

# Process each city
r2 = boto3.client('s3',
    endpoint_url='https://842561b03363b0ab3a35556ff728f9fe.r2.cloudflarestorage.com',
    aws_access_key_id='9b8005782e2f6ebd197768fabe1e07c2',
    aws_secret_access_key='05bafb847199adb9b99d6e3631541995be399d7e621a5132512837ed45832093',
    region_name='auto')

ref_text = extract_text(open(f'{BASE}/ref-goiania-transpaleteira.html').read())
sc_text = extract_text(open(f'{BASE}/senador-canedo-go-aluguel-de-transpaleteira-V2.html').read())
bsb_text = extract_text(open(f'{BASE}/brasilia-df-aluguel-de-transpaleteira-V2.html').read())

slug = 'aluguel-de-transpaleteira'
trindade_also = f'{BASE}/trindade-go-aluguel-de-transpaleteira-V2.html'

for city in NR_ITEMS_NEW:
    fn = f'{BASE}/{city}-{slug}-V2.html'
    if not os.path.exists(fn):
        print(f"  ✗ {city}: file not found")
        continue
    
    html = open(fn).read()
    
    # Replace NR items
    for old, new in zip(NR_ITEMS_OLD, NR_ITEMS_NEW[city]):
        html = html.replace(old, new)
    
    # Replace NR steps
    for old, new in zip(NR_STEPS_OLD, NR_STEPS_NEW[city]):
        html = html.replace(old, new)
    
    # Replace comparativo
    if city in COMP_NEW:
        html = html.replace(COMP_OLD, COMP_NEW[city])
    
    # Replace price CTA
    if city in PRICE_NEW:
        html = html.replace(PRICE_OLD, PRICE_NEW[city])
    
    # Save
    open(fn, 'w').write(html)
    
    # Verify
    new_text = extract_text(html)
    j_ref = jaccard(ref_text, new_text, 3)
    j_sc = jaccard(sc_text, new_text, 3)
    j_bsb = jaccard(bsb_text, new_text, 3)
    
    worst = max(j_ref, j_sc, j_bsb)
    ok = '✓' if worst < 0.20 else '✗'
    
    # Upload
    r2_key = f'{city}/{slug}/index.html'
    r2.put_object(Bucket='pages', Key=r2_key, Body=html.encode(), ContentType='text/html; charset=utf-8')
    
    print(f"  {ok} {city:<28} ref={j_ref:.4f} sc={j_sc:.4f} bsb={j_bsb:.4f} worst={worst:.4f} → R2 OK")

