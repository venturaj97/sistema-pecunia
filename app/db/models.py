from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    cpf = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    is_store = Column(Boolean, default=False)

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)
    payer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    payee_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    payer = relationship('User', foreign_keys=[payer_id], backref="payer_transactions")
    payee = relationship('User', foreign_keys=[payee_id], backref="payee_transactions")
