from fastapi import APIRouter

predict_router = APIRouter(prefix="/predict", tags=["predict"])

@predict_router.get("/history")
async def history():
    """
    Retrieve the history of fraud detection predictions.
    """
    return {"message": "Aqui você vê o histórico de predições"}

@predict_router.post("/new")
async def new_prediction():
    """
    Submit data for a new fraud detection prediction.
    """
    return {"message": "Aqui você faz uma nova predição"}