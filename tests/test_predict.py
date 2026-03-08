import os
from unittest.mock import MagicMock

import joblib


def test_prediction_endpoints(client, monkeypatch):
    """
    Test to predict AI testing
    """

    monkeypatch.setattr(os.path, "exists", lambda path: True)

    mock_model = MagicMock()

    mock_model.predict_proba.return_value = [[0.2, 0.8]]

    monkeypatch.setattr(joblib, "load", lambda path: mock_model)

    payload = {
        "Time": 1.0,
        "Amount": 500.0,
        "V1": 0,
        "V2": 0,
        "V3": 0,
        "V4": 0,
        "V5": 0,
        "V6": 0,
        "V7": 0,
        "V8": 0,
        "V9": 0,
        "V10": 0,
        "V11": 0,
        "V12": 0,
        "V13": 0,
        "V14": 0,
        "V15": 0,
        "V16": 0,
        "V17": 0,
        "V18": 0,
        "V19": 0,
        "V20": 0,
        "V21": 0,
        "V22": 0,
        "V23": 0,
        "V24": 0,
        "V25": 0,
        "V26": 0,
        "V27": 0,
        "V28": 0,
    }

    response = client.post("/predict/new", json=payload)

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["fraud_prediction"] == 1  # 0.8 >= threshold 0.6
    assert json_data["status"] == "Fraudulent"
    assert json_data["fraud_probability"] == 0.8


def test_prediction_history(client):
    """
    Tests whether the prediction history responds correctly.
    """
    response = client.get("/predict/history")
    assert response.status_code == 200
    assert response.json() == {"message": "Success: Prediction history retrieved."}
