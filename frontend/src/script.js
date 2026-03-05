const features = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'];

const samples = [
    {
        type: 'safe',
        description: 'Transação Comum - Baixo Valor',
        data: { "V1": -1.3598, "V2": -0.0728, "V3": 2.5363, "V4": 1.3782, "V5": -0.3383, "V6": 0.4624, "V7": 0.2396, "V8": 0.0987, "V9": 0.3638, "V10": 0.0908, "V11": -0.5516, "V12": -0.6178, "V13": -0.9914, "V14": -0.3112, "V15": 1.4682, "V16": -0.4704, "V17": 0.208, "V18": 0.0258, "V19": 0.404, "V20": 0.2514, "V21": -0.0183, "V22": 0.2778, "V23": -0.1105, "V24": 0.0669, "V25": 0.1285, "V26": -0.1891, "V27": 0.1336, "V28": -0.0211, "Amount": 0.2450, "Time": -0.9950 }
    },
    {
        type: 'fraud',
        description: 'Transação Suspeita - Padrão de Fraude Confirmado',
        data: { "V1": -2.3122, "V2": 1.952, "V3": -1.6099, "V4": 3.9979, "V5": -0.5222, "V6": -1.4265, "V7": -2.5374, "V8": 1.3917, "V9": -2.77, "V10": -2.7723, "V11": 3.202, "V12": -2.9, "V13": -0.5953, "V14": -4.2893, "V15": 0.3898, "V16": -1.1407, "V17": -2.83, "V18": -0.0168, "V19": 0.417, "V20": 0.1269, "V21": 0.5172, "V22": -0.035, "V23": -0.4652, "V24": 0.3201, "V25": 0.0445, "V26": 0.1778, "V27": 0.2611, "V28": -0.1433, "Amount": -0.3074, "Time": -0.9894 }
    },
    {
        type: 'safe',
        description: 'Transação Comum - Valor Médio',
        data: { "V1": 1.1918, "V2": 0.2662, "V3": 0.1665, "V4": 0.4482, "V5": 0.06, "V6": -0.0823, "V7": -0.0788, "V8": 0.0851, "V9": -0.2554, "V10": -0.1669, "V11": 1.6127, "V12": 1.0652, "V13": 0.489, "V14": -0.1437, "V15": 0.6355, "V16": 0.4639, "V17": -0.1148, "V18": -0.1834, "V19": -0.1457, "V20": -0.069, "V21": -0.2258, "V22": -0.6387, "V23": 0.1013, "V24": -0.34, "V25": 0.1672, "V26": 0.1259, "V27": -0.0089, "V28": 0.0147, "Amount": -0.2698, "Time": -0.9950 }
    },
    {
        type: 'fraud',
        description: 'Transação Suspeita - Valor Alto em Sequência',
        data: { "V1": -3.0435, "V2": -3.1573, "V3": 1.0885, "V4": 2.2886, "V5": 1.3598, "V6": -1.0648, "V7": 0.3256, "V8": -0.0678, "V9": -0.271, "V10": -0.4229, "V11": -1.6628, "V12": 0.5307, "V13": 0.9744, "V14": -0.0913, "V15": -0.4194, "V16": -0.586, "V17": -0.4792, "V18": -0.2445, "V19": -1.2867, "V20": 2.1023, "V21": 0.6617, "V22": 0.4355, "V23": 1.3759, "V24": -0.2938, "V25": 0.28, "V26": -0.1452, "V27": -0.2528, "V28": 0.0357, "Amount": 7.0825, "Time": -0.9949 }
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

    // Feedback visual
    const btn = document.querySelector('.btn-generate');
    btn.style.transform = 'Scale(0.95)';
    setTimeout(() => btn.style.transform = 'Scale(1)', 100);

    console.log(`Simulando: ${sample.description}`);
}

// Função principal de predição vinculada ao botão do Front-end
async function predict() {
    // 1. O Front prepara o pedido (coletando dados do formulário)
    const data = {};
    features.forEach(f => {
        data[f] = parseFloat(document.getElementById(f).value);
    });

    const loading = document.getElementById('loading');
    const panel = document.getElementById('resultPanel');

    loading.style.display = 'block';
    panel.style.display = 'none';

    try {
        // 2. O Front envia o pedido para a URL do Back (FastAPI)
        const response = await fetch('http://localhost:8000/predict/new', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        // 3. O Front recebe a resposta do modelo de ML vinda do Back-end
        const result = await response.json();

        console.log("Resposta da API:", result);

        // Atualiza a interface com o resultado real
        panel.className = 'result-panel';
        panel.classList.add(result.fraud_prediction === 1 ? 'result-fraud' : 'result-safe');

        document.getElementById('resultTitle').innerText = result.status.toUpperCase();
        document.getElementById('resultText').innerText = result.fraud_prediction === 1
            ? 'Warning: This transaction has a high risk of fraud!'
            : 'Transaction verified and considered secure.';
        document.getElementById('resultProb').innerText = `Probability of Fraud: ${(result.fraud_probability * 100).toFixed(2)}%`;

        panel.style.display = 'block';
    } catch (error) {
        alert('Error connecting to the API. Please ensure the backend is running on localhost:8000');
    } finally {
        loading.style.display = 'none';
    }
}
