"""
    Consultas para o dashboard
"""

from db.database import get_db_session, close_db_session
from db.models import Expense, CreditCardTransaction, Category, Account
from sqlalchemy import func, extract
import datetime
from db.queries.income_queries import get_monthly_income_sum
from db.queries.expense_queries import get_monthly_expense_sum


def get_monthly_summary(year, month, session=None):
    """
    Obtém um resumo financeiro do mês

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        dict: Dicionário com resumo financeiro
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        # Obter somas de receitas e despesas
        income_sum = get_monthly_income_sum(year, month, session)
        expense_sum = get_monthly_expense_sum(year, month, session)

        # Calcular saldo
        balance = income_sum - expense_sum

        # Obter datas de início e fim do mês
        start_date = datetime.date(year, month, 1)
        if month == 12:
            end_date = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            end_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

        return {
            "income": income_sum,
            "expense": expense_sum,
            "balance": balance,
            "year": year,
            "month": month,
            "start_date": start_date,
            "end_date": end_date
        }
    finally:
        if close_session:
            close_db_session(session)


def get_expense_by_category(year, month, session=None):
    """
    Obtém gastos por categoria em um determinado mês

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de dicionários com categoria e valor total
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        # Gastos de despesas diretas
        expense_by_category = session.query(
            Category.id,
            Category.name,
            Category.color,
            func.sum(Expense.amount).label('total')
        ).join(
            Expense,
            Expense.category_id == Category.id
        ).filter(
            extract('year', Expense.date) == year,
            extract('month', Expense.date) == month
        ).group_by(Category.id).all()

        # Transformar em lista de dicionários
        result = [
            {
                'id': item.id,
                'name': item.name,
                'color': item.color,
                'total': float(item.total)
            }
            for item in expense_by_category
        ]

        # Ordenar por valor (maior para menor)
        result.sort(key=lambda x: x['total'], reverse=True)

        return result
    finally:
        if close_session:
            close_db_session(session)


def get_credit_card_expense_by_category(year, month, session=None):
    """
    Obtém gastos de cartão de crédito por categoria em um determinado mês

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de dicionários com categoria e valor total
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        # Formatar mês de referência para transações de cartão
        statement_month = f"{year:04d}-{month:02d}"

        # Gastos de cartão de crédito
        cc_expense_by_category = session.query(
            Category.id,
            Category.name,
            Category.color,
            func.sum(CreditCardTransaction.amount).label('total')
        ).join(
            CreditCardTransaction,
            CreditCardTransaction.category_id == Category.id
        ).filter(
            CreditCardTransaction.statement_month == statement_month
        ).group_by(Category.id).all()

        # Transformar em lista de dicionários
        result = [
            {
                'id': item.id,
                'name': item.name,
                'color': item.color,
                'total': float(item.total)
            }
            for item in cc_expense_by_category
        ]

        # Ordenar por valor (maior para menor)
        result.sort(key=lambda x: x['total'], reverse=True)

        return result
    finally:
        if close_session:
            close_db_session(session)


def get_accounts_balance(session=None):
    """
    Obtém o saldo de todas as contas

    Args:
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de dicionários com conta e saldo
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        accounts = session.query(Account).all()

        result = [
            {
                'id': account.id,
                'name': account.name,
                'balance': account.balance
            }
            for account in accounts
        ]

        # Ordenar por saldo (maior para menor)
        result.sort(key=lambda x: x['balance'], reverse=True)

        return result
    finally:
        if close_session:
            close_db_session(session)


def get_cash_flow_last_6_months(session=None):
    """
    Obtém o fluxo de caixa dos últimos 6 meses

    Args:
        session: Sessão SQLAlchemy opcional

    Returns:
        dict: Dicionário com meses, receitas, despesas e saldos
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        today = datetime.date.today()
        months = []
        incomes = []
        expenses = []
        balances = []

        # Obter dados para os últimos 6 meses
        for i in range(5, -1, -1):
            year = today.year
            month = today.month - i

            # Ajustar para o ano anterior se necessário
            while month <= 0:
                month += 12
                year -= 1

            # Obter resumo do mês
            summary = get_monthly_summary(year, month, session)

            # Formatar nome do mês
            month_name = datetime.date(year, month, 1).strftime("%b/%Y")

            months.append(month_name)
            incomes.append(summary["income"])
            expenses.append(summary["expense"])
            balances.append(summary["balance"])

        return {
            "months": months,
            "incomes": incomes,
            "expenses": expenses,
            "balances": balances
        }
    finally:
        if close_session:
            close_db_session(session)
