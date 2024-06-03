# Arquivo responsável por definir os modelos de dados que serão utilizados na aplicação
from pydantic import BaseModel
from typing import List, Optional

# Criando um modelo de dados base
class StoryBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: str

# Criando um modelo de dados para criar uma história
class StoryCreate(StoryBase):
    pass

# Criando um modelo de dados para atualizar uma história
class StoryUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]
    content: Optional[str]

# Criando um modelo de dados para uma história
class Story(StoryBase):
    id: int
    owner_id: int
    content: Optional[str] = None

    class Config:
        orm_mode = True

# Criando um modelo de dados base para um usuário
class UserBase(BaseModel):
    username: str
    email: str

# Criando um modelo de dados para criar um usuário
class UserCreate(UserBase):
    password: str

# Criando um modelo de dados para atualizar um usuário
class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]

# Criando um modelo de dados para um usuário
class User(UserBase):
    id: int
    stories: List[Story] = []

    class Config:
        orm_mode = True
