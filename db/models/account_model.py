# db/models/account_model.py
"""
    Account model
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, text
from sqlalchemy.orm import relationship
from db.models.base import Base

class Account(Base):
    """
        Account model
    """
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, name="nome")
    type_account = Column(String(50), nullable=False, name="tipo_conta")
    balance = Column(Float, default=0.0, name="saldo")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"))

    # Relationships
    incomes = relationship("Income", back_populates="account")
    expenses = relationship("Expense", back_populates="account")

    def __repr__(self):
        return f"<Account(name='{self.name}', type_account='{self.type_account}', balance='{self.balance}')>"
