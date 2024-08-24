from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Configurar a string de conexão com o banco de dados
DATABASE_URL = "postgresql://teste:teste@localhost/teste-db"

# Criar o engine
engine = create_engine(DATABASE_URL)

# Criar uma factory para as sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
