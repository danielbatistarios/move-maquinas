// QA: Verifica se cada stepId do CRM UMDHub está recebendo leads
const steps = {
  'curso':         '69b2f6d262e629a2c7a8d35a',
  'pecas':         '69b31f0662e629a2c7a8eb98',
  'manutencao':    '69c19bc96278ca3a22396ee5',
  'venda-aluguel': '69e6552effd38d3be6386d5d',
};

const API_KEY = 'sk_live_719213e5f48228a63a4be9aa357a65dc5568f3b740008a98d14b58229d1f7150';

console.log('QA CRM — Move Máquinas\n');

for (const [nome, stepId] of Object.entries(steps)) {
  try {
    const res = await fetch(`https://backend.umdhub.com.br/api/leads/public/${stepId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-API-Key': API_KEY },
      body: JSON.stringify({
        segment: `qa-teste-${nome}`,
        description: `[QA TEST] Verificacao automatica — ${new Date().toISOString()}`,
        source: 'direct',
        medium: 'organic',
        channel: 'other',
        priority: 'low',
        temperature: 'cold',
        qualifyStatus: 'pending',
        budget: 0,
        name: 'QA Bot',
        company: '',
        position: '',
        emails: [],
        phones: []
      })
    });

    const body = await res.text().catch(() => '');
    const status = res.ok ? '✓' : '✗';
    console.log(`${status} ${nome.padEnd(14)} stepId: ${stepId}  →  HTTP ${res.status}`);
    if (!res.ok) console.log(`  Resposta: ${body.slice(0, 200)}`);
  } catch (err) {
    console.log(`✗ ${nome.padEnd(14)} stepId: ${stepId}  →  ERRO: ${err.message}`);
  }
}
