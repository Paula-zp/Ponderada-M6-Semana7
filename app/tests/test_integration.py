# Teste de integração
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Configuração do banco de dados de teste
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Teste 1: Criar um usuário
def test_create_user():
    response = client.post("/users/", json={"username": "integrationuser", "email": "integration@example.com", "password": "integrationpassword"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "integration@example.com"

# Teste 2: Criar uma história
def test_create_story():
    response = client.post("/stories/", json={"title": "Integration Story", "description": "Integration Description"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Integration Story"