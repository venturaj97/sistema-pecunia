from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models import User
from app.db.database import SessionLocal
from app.schemas.user import UserCreate, UserResponse  # Certifique-se de ajustar o caminho conforme sua estrutura

router = APIRouter()

# Dependência de sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo usuário
@router.post("/create-user/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar se o usuário já existe
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    # Criar o novo usuário
    db_user = User(
        full_name=user.full_name,
        cpf=user.cpf,
        email=user.email,
        password_hash=user.password,  # Certifique-se de usar um hash seguro na prática
        is_store=user.is_store
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
