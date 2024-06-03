# Arquivo responsável por definir o banco de dados
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados
DATABASE_URL = "url do banco de dados (não fiz)"

# Criando a engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
