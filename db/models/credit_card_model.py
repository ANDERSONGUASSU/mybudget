# db/models/credit_card_model.py
"""
    Credit Card model
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, text
from sqlalchemy.orm import relationship
from db.models.base import Base

class CreditCard(Base):
    """
        Credit Card model
    """
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, name="nome")
    limit = Column(Float, default=0.0, name="limite")
    closing_day = Column(Integer, nullable=False, name="dia_fechamento")
    due_day = Column(Integer, nullable=False, name="dia_vencimento")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"))

    # Relationships
    transactions = relationship("CreditCardTransaction", back_populates="credit_card")

    def __repr__(self):
        return f"<CreditCard(name='{self.name}', limit='{self.limit}')>"
