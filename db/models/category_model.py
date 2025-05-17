# db/models/category_model.py
"""
    Category model
"""
from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy.orm import relationship
from db.models.base import Base

class Category(Base):
    """
        Category model
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, name="nome")
    type = Column(String(50), nullable=False, name="tipo", default="despesa")
    color = Column(String(7), nullable=False, name="cor")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"))

    # Relationships
    incomes = relationship("Income", back_populates="category")
    expenses = relationship("Expense", back_populates="category")
    credit_card_transactions = relationship("CreditCardTransaction", back_populates="category")

    def __repr__(self):
        return f"<Category(name='{self.name}', type='{self.type}', color='{self.color}')>"
