# uvicorn api.main:app --reload

from fastapi import FastAPI

from passlib.context import CryptContext
from dotenv import load_dotenv
import os

from api.database import engine, Base
from api.auth_routes import auth_router
from api.predict import predict_router
from fastapi.middleware.cors import CORSMiddleware

# Create database tables

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FraudShield ML API",
    description="Professional Fraud Detection API for portfolio.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(predict_router)
