from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    cpf: str
    email: EmailStr
    password: str
    is_store: bool = False

class UserResponse(BaseModel):
    id: int
    full_name: str
    cpf: str
    email: EmailStr
    balance: float
    is_store: bool

    class Config:
        orm_mode = True
