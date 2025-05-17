"""
    Controlador para obter despesas
"""

from db.queries.expense_queries import (
    get_expense_by_id,
    get_expenses_by_period,
    get_expenses_by_month,
    get_expenses_by_category
)
import datetime


def get_expense(expense_id):
    """
    Obtém uma despesa específica

    Args:
        expense_id (int): ID da despesa

    Returns:
        dict: Dicionário com informações da despesa ou None se não encontrada
    """
    expense = get_expense_by_id(expense_id)

    if not expense:
        return None

    # Transformar objeto Expense em dicionário
    expense_dict = {
        'id': expense.id,
        'description': expense.description,
        'amount': expense.amount,
        'date': expense.date.strftime("%Y-%m-%d"),
        'category_id': expense.category_id,
        'category_name': expense.category.name if expense.category else None,
        'account_id': expense.account_id,
        'account_name': expense.account.name if expense.account else None
    }

    return expense_dict


def get_expenses_for_period(start_date, end_date):
    """
    Obtém despesas em um período específico

    Args:
        start_date (str): Data inicial no formato "YYYY-MM-DD"
        end_date (str): Data final no formato "YYYY-MM-DD"

    Returns:
        list: Lista de dicionários com informações das despesas
    """
    # Converter datas de string para objetos date
    try:
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        return []

    expenses = get_expenses_by_period(start, end)

    # Transformar objetos Expense em dicionários
    expenses_dict = [
        {
            'id': expense.id,
            'description': expense.description,
            'amount': expense.amount,
            'date': expense.date.strftime("%Y-%m-%d"),
            'category_id': expense.category_id,
            'category_name': expense.category.name if expense.category else None,
            'account_id': expense.account_id,
            'account_name': expense.account.name if expense.account else None
        }
        for expense in expenses
    ]

    return expenses_dict


def get_expenses_for_month(year, month):
    """
    Obtém despesas de um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)

    Returns:
        list: Lista de dicionários com informações das despesas
    """
    expenses = get_expenses_by_month(year, month)

    # Transformar objetos Expense em dicionários
    expenses_dict = [
        {
            'id': expense.id,
            'description': expense.description,
            'amount': expense.amount,
            'date': expense.date.strftime("%Y-%m-%d"),
            'category_id': expense.category_id,
            'category_name': expense.category.name if expense.category else None,
            'account_id': expense.account_id,
            'account_name': expense.account.name if expense.account else None
        }
        for expense in expenses
    ]

    return expenses_dict


def get_expenses_for_category(category_id):
    """
    Obtém despesas de uma categoria específica

    Args:
        category_id (int): ID da categoria

    Returns:
        list: Lista de dicionários com informações das despesas
    """
    expenses = get_expenses_by_category(category_id)

    # Transformar objetos Expense em dicionários
    expenses_dict = [
        {
            'id': expense.id,
            'description': expense.description,
            'amount': expense.amount,
            'date': expense.date.strftime("%Y-%m-%d"),
            'category_id': expense.category_id,
            'category_name': expense.category.name if expense.category else None,
            'account_id': expense.account_id,
            'account_name': expense.account.name if expense.account else None
        }
        for expense in expenses
    ]

    return expenses_dict
