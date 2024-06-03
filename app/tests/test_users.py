import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models, schemas, crud
from app.database import Base

# Configuração do banco de dados de teste
SQLALCHEMY_DATABASE_URL = "//"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


# Criando um fixture para o banco de dados
@pytest.fixture(scope="module")
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# Teste 1: Criar um usuário
def test_create_user(db):
    user = schemas.UserCreate(username="testuser", email="teste@email.com", password="testpassword")
    user_created = crud.create_user(db, user=user)
    assert user_created.email == user.email

# Teste 2: Listar um usuário pelo email
def test_get_user(db):
    user = crud.get_user_by_email(db, email="teste@email.com")
    assert user
    assert user.email == "teste@email.com"

# Teste 3: Atualizar um usuário
def test_update_user(db):
    user = crud.get_user_by_email(db, email="teste@email.com")
    user_update = schemas.UserUpdate(email="newemail@email.com")
    updated_user = crud.update_user(db, user_id=user.id, user_update=user_update)
    assert updated_user.email == "newemail@email.com"

# Teste 4: Deletar um usuário
def test_delete_user(db):
    user = crud.get_user_by_email(db, email="newemail@email.com")
    deleted_user = crud.delete_user(db, user_id=user.id)
    assert deleted_user
    assert crud.get_user(db, user_id=user.id) is None
