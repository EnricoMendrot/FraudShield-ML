import json
import os
from datetime import datetime

LOG_DIR = "monitoring/logs"
LOG_FILE = os.path.join(LOG_DIR, "predictions.jsonl")

os.makedirs(LOG_DIR, exist_ok=True)

def log_prediction(amount: float, is_fraud: bool, probability: float, user_id: int = None):
    """
    Salva cada predição como uma linha JSON no arquivo de log.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "prediction",
        "user_id": user_id,
        "amount": amount,
        "is_fraud": is_fraud,
        "fraud_probability": round(probability, 4),
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n") 