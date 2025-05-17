# db/models/expense_model.py
"""
    Expense model
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, text, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class Expense(Base):
    """
        Expense model
    """
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False, name="descrição")
    amount = Column(Float, nullable=False, name="valor")
    date = Column(Date, nullable=False, name="data")
    category_id = Column(Integer, ForeignKey("categories.id"), name="categoria_id")
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False, name="conta_id")
    recurrence_id = Column(Integer, ForeignKey("recurrences.id"), name="recorrência_id")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"))

    # Relationships
    category = relationship("Category", back_populates="expenses")
    account = relationship("Account", back_populates="expenses")
    recurrence = relationship("Recurrence", back_populates="expenses")

    def __repr__(self):
        return f"<Expense(description='{self.description}', amount='{self.amount}', date='{self.date}')>"
