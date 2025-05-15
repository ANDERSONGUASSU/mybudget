"""
    Models for the database
"""

from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    """
        Category model
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, name="id")
    name = Column(String(100), nullable=False, name="nome")
    color = Column(String(20), name="cor")

    # Relationships
    incomes = relationship("Income", back_populates="category")
    expenses = relationship("Expense", back_populates="category")
    credit_card_transactions = relationship("CreditCardTransaction", back_populates="category")

    def __repr__(self):
        return f"<Category(name='{self.name}')>"

class Account(Base):
    """
        Account model
    """
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, name="id")
    name = Column(String(100), nullable=False, name="nome")
    balance = Column(Float, default=0.0, name="saldo")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"), name="data_criação")

    # Relationships
    incomes = relationship("Income", back_populates="account")
    expenses = relationship("Expense", back_populates="account")

    def __repr__(self):
        return f"<Account(name='{self.name}', balance='{self.balance}', type='{self.type}')>"


class CreditCard(Base):
    """
        Credit Card model
    """
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True, name="id")
    name = Column(String(100), nullable=False, name="nome")
    bank = Column(String(100), name="banco")
    limit_amount = Column(Float, name="limite")
    closing_day = Column(Integer, name="dia_fechamento")  # 1-31
    due_day = Column(Integer, name="dia_vencimento")  # 1-31
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"))

    # Relationships
    transactions = relationship("CreditCardTransaction", back_populates="credit_card")

    def __repr__(self):
        return f"<CreditCard(name='{self.name}', bank='{self.bank}')>"


class Recurrence(Base):
    """
        Recurrence model for recurring transactions
    """
    __tablename__ = "recurrences"

    id = Column(Integer, primary_key=True, name="id")
    type = Column(String(20), nullable=False, name="tipo")  # 'once', 'daily', 'weekly', 'monthly', 'yearly'
    frequency = Column(Integer, default=1, name="frequência")  # e.g., every 2 weeks, every 3 months
    start_date = Column(Date, nullable=False, name="data_início")
    end_date = Column(Date, name="data_fim")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"), name="data_criação")

    # Relationships
    incomes = relationship("Income", back_populates="recurrence")
    expenses = relationship("Expense", back_populates="recurrence")
    credit_card_transactions = relationship("CreditCardTransaction", back_populates="recurrence")

    def __repr__(self):
        return f"<Recurrence(type='{self.type}', start_date='{self.start_date}')>"


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


class CreditCardTransaction(Base):
    """
        Credit Card Transaction model
    """
    __tablename__ = "credit_card_transactions"

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False, name="descrição")
    amount = Column(Float, nullable=False, name="valor")
    purchase_date = Column(Date, nullable=False, name="data_compra")
    category_id = Column(Integer, ForeignKey("categories.id"), name="categoria_id")
    credit_card_id = Column(Integer, ForeignKey("credit_cards.id"), nullable=False, name="cartão_id")
    installments = Column(Integer, default=1, name="parcelas")
    installment_number = Column(Integer, default=1, name="número_parcela")
    due_date = Column(Date, name="data_vencimento")
    recurrence_id = Column(Integer, ForeignKey("recurrences.id"), name="recorrência_id")
    created_at = Column(DateTime, default=text("CURRENT_TIMESTAMP"), name="data_criação")

    # Relationships
    category = relationship("Category", back_populates="credit_card_transactions")
    credit_card = relationship("CreditCard", back_populates="transactions")
    recurrence = relationship("Recurrence", back_populates="credit_card_transactions")

    def __repr__(self):
        return (
            f"<CreditCardTransaction("
            f"description='{self.description}', "
            f"amount='{self.amount}', "
            f"date='{self.purchase_date}')>"
        )
