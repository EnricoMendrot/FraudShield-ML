# uvicorn api.main:app --reload

from fastapi import FastAPI

from api.database import engine, Base
from api.auth_routes import auth_router
from api.predict import predict_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FraudShield ML API",
    description="Professional Fraud Detection API for portfolio.",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(predict_router)
