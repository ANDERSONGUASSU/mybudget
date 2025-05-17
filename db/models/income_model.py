# db/models/income_model.py
"""
    Income model
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, text, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class Income(Base):
    """
        Income model
    """
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False, name="descrição")
    amount = Column(Float, nullable=False, name="valor")
    date = Column(Date, nullable=False, name="data")
    category_id = Column(Integer, ForeignKey("categories.id"), name="categoria_id")
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False, name="conta_id")
    recurrence_id = Column(Integer, ForeignKey("recurrences.id"), name="recorrência_id")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"), name="data_criação")

    # Relationships
    category = relationship("Category", back_populates="incomes")
    account = relationship("Account", back_populates="incomes")
    recurrence = relationship("Recurrence", back_populates="incomes")

    def __repr__(self):
        return f"<Income(description='{self.description}', amount='{self.amount}', date='{self.date}')>"
