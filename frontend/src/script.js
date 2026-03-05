const features = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'];

// Exemplos reais do dataset (Legítimo e Fraude)
const samples = [
    {
        type: 'safe',
        data: { "Time": 0.0, "V1": -1.3598, "V2": -0.0727, "V3": 2.5363, "V4": 1.3781, "V5": -0.3383, "V6": 0.4623, "V7": 0.2395, "V8": 0.0986, "V9": 0.3637, "V10": 0.0907, "V11": -0.5515, "V12": -0.6178, "V13": -0.9913, "V14": -0.3111, "V15": 1.4681, "V16": -0.4704, "V17": 0.2079, "V18": 0.0257, "V19": 0.4039, "V20": 0.2514, "V21": -0.0183, "V22": 0.2778, "V23": -0.1104, "V24": 0.0669, "V25": 0.1285, "V26": -0.1891, "V27": 0.1335, "V28": -0.0211, "Amount": 149.62 }
    },
    {
        type: 'fraud',
        data: { "Time": 406.0, "V1": -2.3122, "V2": 1.9519, "V3": -1.6098, "V4": 3.9979, "V5": -0.5221, "V6": -1.4265, "V7": -2.5373, "V8": 1.3916, "V9": -2.7700, "V10": -2.7722, "V11": 3.2020, "V12": -2.8999, "V13": -0.5952, "V14": -4.2892, "V15": 0.3897, "V16": -1.1407, "V17": -2.8300, "V18": -0.0168, "V19": 0.4169, "V20": 0.1269, "V21": 0.5172, "V22": -0.0350, "V23": -0.4652, "V24": 0.3201, "V25": 0.0445, "V26": 0.1778, "V27": 0.2611, "V28": -0.1432, "Amount": 0.0 }
    },
    {
        type: 'safe',
        data: { "Time": 1.0, "V1": 1.1918, "V2": 0.2661, "V3": 0.1664, "V4": 0.4481, "V5": 0.0600, "V6": -0.0823, "V7": -0.0788, "V8": 0.0851, "V9": -0.2554, "V10": -0.1669, "V11": 1.6127, "V12": 1.0652, "V13": 0.4890, "V14": -0.1437, "V15": 0.6355, "V16": 0.4639, "V17": -0.1148, "V18": -0.1833, "V19": -0.1457, "V20": -0.0690, "V21": -0.2257, "V22": -0.6386, "V23": 0.1012, "V24": -0.3398, "V25": 0.1671, "V26": 0.1258, "V27": -0.0089, "V28": 0.0147, "Amount": 2.69 }
    }
];

document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('inputGrid');

    // Criar os inputs dinamicamente
    features.forEach(f => {
        const div = document.createElement('div');
        div.className = 'input-group';
        div.innerHTML = `
            <label>${f}</label>
            <input type="number" id="${f}" step="any" value="0">
        `;
        grid.appendChild(div);
    });
});

function generateRandom() {
    const sample = samples[Math.floor(Math.random() * samples.length)];
    features.forEach(f => {
        document.getElementById(f).value = sample.data[f];
    });

    // Highlight feedback
    const btn = document.querySelector('.btn-generate');
    btn.style.transform = 'Scale(0.95)';
    setTimeout(() => btn.style.transform = 'Scale(1)', 100);
}

async function predict() {
    const data = {};
    features.forEach(f => {
        data[f] = parseFloat(document.getElementById(f).value);
    });

    const loading = document.getElementById('loading');
    const panel = document.getElementById('resultPanel');

    loading.style.display = 'block';
    panel.style.display = 'none';

    try {
        const response = await fetch('http://localhost:8000/predict/new', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        panel.className = 'result-panel';
        panel.classList.add(result.fraud_prediction === 1 ? 'result-fraud' : 'result-safe');

        document.getElementById('resultTitle').innerText = result.status.toUpperCase();
        document.getElementById('resultText').innerText = result.fraud_prediction === 1
            ? '⚠️ Alerta: Esta transação possui alto risco de fraude!'
            : '✅ Transação verificada e considerada segura.';
        document.getElementById('resultProb').innerText = `Probabilidade de Fraude: ${(result.fraud_probability * 100).toFixed(2)}%`;

        panel.style.display = 'block';
    } catch (error) {
        alert('Erro ao conectar com a API. Certifique-se que o backend está rodando em localhost:8000');
    } finally {
        loading.style.display = 'none';
    }
}
