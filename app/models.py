# Arquivo para definir os modelos de dados que serão usados no banco de dados
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Definindo a classe User que será usada para criar a tabela de usuários
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    stories = relationship("Story", back_populates="owner")

# Definindo a classe Story que será usada para criar a tabela de histórias
class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    category = Column(String, index=True)
    content = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="stories")
