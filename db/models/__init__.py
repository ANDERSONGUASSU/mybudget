# db/models/__init__.py
"""
    Models for the database
"""

# Primeiro importamos a Base
from db.models.base import Base

# Em seguida, importamos todos os modelos sem dependências circulares
from db.models.category_model import Category
from db.models.account_model import Account
from db.models.recurrence_model import Recurrence
from db.models.income_model import Income
from db.models.expense_model import Expense
from db.models.credit_card_model import CreditCard
from db.models.credit_card_transaction_model import CreditCardTransaction

# Exportamos todos os modelos
__all__ = [
    'Base',
    'Category',
    'Account',
    'Recurrence',
    'Income',
    'Expense',
    'CreditCard',
    'CreditCardTransaction'
]
