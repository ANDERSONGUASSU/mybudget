"""
    Pacote de consultas ao banco de dados

    Este pacote contém módulos separados com consultas específicas para cada entidade do sistema.
"""

from .account_queries import (
    get_account_by_id,
    get_all_accounts,
    get_account_balance,
    get_total_balance
)
from .category_queries import (
    get_all_categories,
    get_categories_by_type,
    get_category_by_id
)
from .credit_card_queries import (
    get_all_credit_cards,
    get_credit_card_available_limit,
    get_credit_card_by_id,
    get_credit_card_statement,
    get_credit_card_transaction_by_id,
    get_credit_card_transactions_by_period
)
from .dashboard_queries import (
    get_accounts_balance,
    get_cash_flow_last_6_months,
    get_credit_card_expense_by_category,
    get_expense_by_category,
    get_monthly_summary,
)
from .expense_queries import (
    get_expense_by_id,
    get_expenses_by_category,
    get_expenses_by_month,
    get_expenses_by_period,
    get_monthly_expense_sum
)
from .income_queries import (
    get_income_by_id,
    get_incomes_by_category,
    get_incomes_by_month,
    get_incomes_by_period,
    get_monthly_income_sum
)


__all__ = [
    "get_account_by_id",
    "get_all_accounts",
    "get_account_balance",
    "get_total_balance",
    "get_all_categories",
    "get_categories_by_type",
    "get_category_by_id",
    "get_all_credit_cards",
    "get_credit_card_available_limit",
    "get_credit_card_by_id",
    "get_credit_card_statement",
    "get_credit_card_transaction_by_id",
    "get_credit_card_transactions_by_period",
    "get_accounts_balance",
    "get_cash_flow_last_6_months",
    "get_credit_card_expense_by_category",
    "get_expense_by_category",
    "get_monthly_summary",
    "get_expense_by_id",
    "get_expenses_by_category",
    "get_expenses_by_month",
    "get_expenses_by_period",
    "get_monthly_expense_sum",
    "get_income_by_id",
    "get_incomes_by_category",
    "get_incomes_by_month",
    "get_incomes_by_period",
    "get_monthly_income_sum",
]
