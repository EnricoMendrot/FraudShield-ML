import os

import joblib
import numpy as np
from fastapi import APIRouter, HTTPException

from monitoring.logger import log_prediction

from .schemas import TransactionSchema

predict_router = APIRouter(prefix="/predict", tags=["predict"])

# Caminho para o modelo
MODEL_PATH = "models/random_forest.pkl"


@predict_router.get("/history")
async def history():
    """
    Retrieve the history of fraud detection predictions.
    """
    return {"message": "Success: Prediction history retrieved."}


@predict_router.post("/new")
async def new_prediction(data: TransactionSchema):
    """
    Submit data for a new fraud detection prediction.
    """
    if not os.path.exists(MODEL_PATH):
        raise HTTPException(
            status_code=500,
            detail="Model file not found at models/random_forest.pkl. Please train the model first.",
        )

    try:
        model = joblib.load(MODEL_PATH)
        features = [
            data.V1,
            data.V2,
            data.V3,
            data.V4,
            data.V5,
            data.V6,
            data.V7,
            data.V8,
            data.V9,
            data.V10,
            data.V11,
            data.V12,
            data.V13,
            data.V14,
            data.V15,
            data.V16,
            data.V17,
            data.V18,
            data.V19,
            data.V20,
            data.V21,
            data.V22,
            data.V23,
            data.V24,
            data.V25,
            data.V26,
            data.V27,
            data.V28,
            data.Amount,
            data.Time,
        ]

        input_data = np.array([features])

        probability = model.predict_proba(input_data)[0][1]

        threshold = 0.6
        prediction = 1 if probability >= threshold else 0

        log_prediction(
            amount=data.Amount,
            is_fraud=bool(prediction),
            probability=float(probability),
        )

        return {
            "fraud_prediction": int(prediction),
            "fraud_probability": round(float(probability), 4),
            "status": "Fraudulent" if prediction == 1 else "Legitimate",
            "message": "Prediction processed successfully.",
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error during prediction: {str(e)}"
        ) from e
