# Imports
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Importamos os componentes da nossa aplicação para poder alterá-los durante o teste
from api.main import app
from api.database import Base
from api.dependencies import get_session


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_fraud_shield.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def create_databasetest():
    """
    This fixture creates the test database before the tests start
    and cleans it up after they finish.
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    engine.dispose() # Limpa as conexões para liberar o arquivo no Windows
    
    # To delete the test database file after the tests
    if os.path.exists("./test_fraud_shield.db"):
        os.remove("./test_fraud_shield.db")

def override_get_session():
    """
    This function overrides the get_session in dependency.py to use the test database.
    """
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_session] = override_get_session

@pytest.fixture
def client():
    """
    This fixture creates a test client that we will use to make fake HTTP requests.
    """
    with TestClient(app) as c:
        yield c
