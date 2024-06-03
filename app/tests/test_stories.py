import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models, schemas, crud
from app.database import Base

# Configuração do banco de dados de teste
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# Teste 1: Criar uma história
def test_create_story(db):
    user = crud.get_user_by_email(db, email="newemail@example.com")
    story_in = schemas.StoryCreate(title="Test Story", description="Test Description")
    story = crud.create_story(db, story=story_in, user_id=user.id)
    assert story.title == story_in.title

# Teste 2: Listar uma história pelo ID
def test_get_story(db):
    story = crud.get_story(db, story_id=1)
    assert story
    assert story.title == "Test Story"

# Teste 3: Atualizar uma história
def test_update_story(db):
    story_update = schemas.StoryUpdate(title="Updated Story")
    updated_story = crud.update_story(db, story_id=1, story_update=story_update)
    assert updated_story.title == "Updated Story"

# Teste 4: Deletar uma história
def test_delete_story(db):
    story = crud.get_story(db, story_id=1)
    deleted_story = crud.delete_story(db, story_id=story.id)
    assert deleted_story
    assert crud.get_story(db, story_id=story.id) is None
