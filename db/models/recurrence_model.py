# db/models/recurrence_model.py
"""
    Recurrence model
"""
from sqlalchemy import Column, Integer, String, DateTime, text, Date
from sqlalchemy.orm import relationship
from db.models.base import Base

class Recurrence(Base):
    """
        Recurrence model
    """
    __tablename__ = "recurrences"

    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False, name="tipo")
    frequency = Column(Integer, nullable=False, name="frequência")
    start_date = Column(Date, nullable=False, name="data_início")
    end_date = Column(Date, name="data_fim")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"))

    # Relationships
    incomes = relationship("Income", back_populates="recurrence")
    expenses = relationship("Expense", back_populates="recurrence")

    def __repr__(self):
        return f"<Recurrence(type='{self.type}', frequency='{self.frequency}')>"
