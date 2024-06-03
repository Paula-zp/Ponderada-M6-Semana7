# Arquivo com CRUD para interagir com o banco de dados
from sqlalchemy.orm import Session
import models, schemas

# Função para pegar um usuário pelo ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Função para pegar um usuário pelo email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Função para listar todos os usuários
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# Função para criar um usuário
def create_user(db: Session, user: schemas.UserCreate):
    fake_password = user.password + "senha123"
    db_user = models.User(username=user.username, email=user.email, hashed_password=fake_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Função para atualizar um usuário
def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if db_user:
        for key, value in user_update.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

# Função para deletar um usuário
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Função para listar todas as histórias
def get_stories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Story).offset(skip).limit(limit).all()

# Função para criar uma história
def create_story(db: Session, story: schemas.StoryCreate, user_id: int):
    db_story = models.Story(**story.model_dump(), owner_id=user_id)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

# Função para atualizar uma história
def update_story(db: Session, story_id: int, story_update: schemas.StoryUpdate):
    db_story = get_story(db, story_id)
    if db_story:
        for key, value in story_update.model_dump(exclude_unset=True).items():
            setattr(db_story, key, value)
        db.commit()
        db.refresh(db_story)
    return db_story

# Função para deletar uma história
def delete_story(db: Session, story_id: int):
    db_story = get_story(db, story_id)
    if db_story:
        db.delete(db_story)
        db.commit()
    return db_story

# Função para pegar uma história pelo ID
def get_story(db: Session, story_id: int):
    return db.query(models.Story).filter(models.Story.id == story_id).first()
