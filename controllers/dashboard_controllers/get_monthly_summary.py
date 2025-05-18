"""
    Controlador para obter o resumo mensal financeiro
"""

import datetime
from db.queries.dashboard_queries import get_monthly_summary as get_summary


def get_monthly_summary(year=None, month=None):
    """
    Obtém um resumo financeiro de um mês específico.
    Se não forem fornecidos ano e mês, retorna o resumo do mês atual.

    Args:
        year (int, optional): Ano
        month (int, optional): Mês (1-12)

    Returns:
        dict: Dicionário com resumo financeiro do mês
    """
    # Se não forem fornecidos ano e mês, usar o mês atual
    if year is None or month is None:
        today = datetime.datetime.today()
        year = today.year
        month = today.month

    # Validar mês
    if month < 1 or month > 12:
        return None

    # Obter resumo do mês
    summary = get_summary(year, month)

    # Formatação adicional para a interface
    formatted_summary = {
        'income': summary['income'],
        'expense': summary['expense'],
        'balance': summary['balance'],
        'year': summary['year'],
        'month': summary['month'],
        'month_name': datetime.date(year, month, 1).strftime('%B'),
        'start_date': summary['start_date'].strftime('%Y-%m-%d'),
        'end_date': summary['end_date'].strftime('%Y-%m-%d'),
        'positive_balance': summary['balance'] >= 0
    }

    return formatted_summary
