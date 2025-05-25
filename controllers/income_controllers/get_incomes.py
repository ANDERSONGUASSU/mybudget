"""
    Controlador para obter receitas
"""

import datetime
from db.queries.income_queries import (
    get_income_by_id,
    get_incomes_by_period,
    get_incomes_by_month,
    get_incomes_by_category
)


def get_income(income_id):
    """
    Obtém uma receita específica

    Args:
        income_id (int): ID da receita

    Returns:
        dict: Dicionário com informações da receita ou None se não encontrada
    """
    income = get_income_by_id(income_id)

    if not income:
        return None

    # Transformar objeto Income em dicionário
    income_dict = {
        'id': income.id,
        'description': income.description,
        'amount': income.amount,
        'date': income.date.strftime("%Y-%m-%d"),
        'category_id': income.category_id,
        'category_name': income.category.name if income.category else None,
        'account_id': income.account_id,
        'account_name': income.account.name if income.account else None
    }

    return income_dict


def get_incomes_for_period(start_date, end_date):
    """
    Obtém receitas em um período específico

    Args:
        start_date (str): Data inicial no formato "YYYY-MM-DD"
        end_date (str): Data final no formato "YYYY-MM-DD"

    Returns:
        list: Lista de dicionários com informações das receitas
    """
    # Converter datas de string para objetos date
    try:
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError as e:
        print(f"Erro de tipo de dados ao converter datas: {e}")
        return []

    incomes = get_incomes_by_period(start, end)

    # Transformar objetos Income em dicionários
    incomes_dict = [
        {
            'id': income.id,
            'description': income.description,
            'amount': income.amount,
            'date': income.date.strftime("%Y-%m-%d"),
            'category_id': income.category_id,
            'category_name': income.category.name if income.category else None,
            'account_id': income.account_id,
            'account_name': income.account.name if income.account else None
        }
        for income in incomes
    ]

    return incomes_dict


def get_incomes_for_month(year, month):
    """
    Obtém receitas de um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)

    Returns:
        list: Lista de dicionários com informações das receitas
    """
    incomes = get_incomes_by_month(year, month)

    # Transformar objetos Income em dicionários
    incomes_dict = [
        {
            'id': income.id,
            'description': income.description,
            'amount': income.amount,
            'date': income.date.strftime("%Y-%m-%d"),
            'category_id': income.category_id,
            'category_name': income.category.name if income.category else None,
            'account_id': income.account_id,
            'account_name': income.account.name if income.account else None
        }
        for income in incomes
    ]

    return incomes_dict


def get_incomes_for_category(category_id):
    """
    Obtém receitas de uma categoria específica

    Args:
        category_id (int): ID da categoria

    Returns:
        list: Lista de dicionários com informações das receitas
    """
    incomes = get_incomes_by_category(category_id)

    # Transformar objetos Income em dicionários
    incomes_dict = [
        {
            'id': income.id,
            'description': income.description,
            'amount': income.amount,
            'date': income.date.strftime("%Y-%m-%d"),
            'category_id': income.category_id,
            'category_name': income.category.name if income.category else None,
            'account_id': income.account_id,
            'account_name': income.account.name if income.account else None
        }
        for income in incomes
    ]

    return incomes_dict
