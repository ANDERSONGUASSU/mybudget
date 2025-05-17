# db/models/credit_card_transaction_model.py
"""
    Credit Card Transaction model
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, text, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class CreditCardTransaction(Base):
    """
        Credit Card Transaction model
    """
    __tablename__ = "credit_card_transactions"

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False, name="descrição")
    amount = Column(Float, nullable=False, name="valor")
    date = Column(Date, nullable=False, name="data")
    installments = Column(Integer, default=1, name="parcelas")
    current_installment = Column(Integer, default=1, name="parcela_atual")
    category_id = Column(Integer, ForeignKey("categories.id"), name="categoria_id")
    credit_card_id = Column(Integer, ForeignKey("credit_cards.id"), nullable=False, name="cartão_id")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"))

    # Relationships
    category = relationship("Category", back_populates="credit_card_transactions")
    credit_card = relationship("CreditCard", back_populates="transactions")

    def __repr__(self):
        return f"<CreditCardTransaction(description='{self.description}', amount='{self.amount}', date='{self.date}')>"
