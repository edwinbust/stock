from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default='user')  # 'user' o 'admin'
    status = Column(TINYINT(1), default=0)  # TINYINT(1) en lugar de Boolean
    photo = Column(String(200))

    # Relación con transacciones de usuario
    investments = relationship('FundTransaction', back_populates='user')


class FundOperation(Base):
    __tablename__ = 'fund_operations'
    id = Column(Integer, primary_key=True)
    funde_inv = Column(Float, nullable=False)  # Inversión total del fondo
    profit_funde = Column(Float, nullable=False)  # Ganancia total en criptomoneda
    funde_porc_share = Column(Float, nullable=False)  # Porcentaje de ganancia del fondo
    funde_now = Column(Float, nullable=False)  # Saldo total del fondo
    timestamp = Column(DateTime, default=datetime.now, nullable=False)  # Marca de tiempo
    
    # Relación con transacciones del fondo
    transactions = relationship('FundTransaction', back_populates='operation')


class FundTransaction(Base):
    __tablename__ = 'fund_transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    operation_id = Column(Integer, ForeignKey('fund_operations.id'), nullable=False)
    inv_user = Column(Float, nullable=False)  # Inversión del usuario
    profit_user = Column(Float, nullable=False)  # Ganancia del usuario en criptomoneda
    porc_share = Column(Float, nullable=False)  # Porcentaje de participación del usuario
    share_now = Column(Float, nullable=False)  # Saldo actual del usuario
    is_latest = Column(TINYINT(1), default=1)

    # Relaciones con usuarios y operaciones
    user = relationship('User', back_populates='investments')
    operation = relationship('FundOperation', back_populates='transactions')
