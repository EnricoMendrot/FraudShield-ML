from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from api.database import SessionLocal

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()