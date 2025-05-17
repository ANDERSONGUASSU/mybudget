"""
    Controlador para obter o detalhamento de despesas por categoria
"""

from db.queries.dashboard_queries import get_expense_by_category, get_credit_card_expense_by_category
import datetime


def get_expense_breakdown(year=None, month=None):
    """
    Obtém o detalhamento de despesas por categoria para um mês específico.
    Se não forem fornecidos ano e mês, retorna o detalhamento do mês atual.

    Args:
        year (int, optional): Ano 
        month (int, optional): Mês (1-12)

    Returns:
        dict: Dicionário com despesas por categoria
    """
    # Se não forem fornecidos ano e mês, usar o mês atual
    if year is None or month is None:
        today = datetime.datetime.today()
        year = today.year
        month = today.month

    # Validar mês
    if month < 1 or month > 12:
        return None

    # Obter despesas diretas por categoria
    direct_expenses = get_expense_by_category(year, month)

    # Obter despesas de cartão de crédito por categoria
    cc_expenses = get_credit_card_expense_by_category(year, month)

    # Consolidar os resultados em um único dicionário
    category_map = {}

    # Adicionar despesas diretas
    for expense in direct_expenses:
        category_id = expense['id']
        category_map[category_id] = {
            'id': category_id,
            'name': expense['name'],
            'color': expense['color'],
            'direct_amount': expense['total'],
            'cc_amount': 0,
            'total_amount': expense['total']
        }

    # Adicionar despesas de cartão de crédito
    for expense in cc_expenses:
        category_id = expense['id']
        if category_id in category_map:
            # Categoria já existe, somar os valores
            category_map[category_id]['cc_amount'] = expense['total']
            category_map[category_id]['total_amount'] += expense['total']
        else:
            # Categoria nova
            category_map[category_id] = {
                'id': category_id,
                'name': expense['name'],
                'color': expense['color'],
                'direct_amount': 0,
                'cc_amount': expense['total'],
                'total_amount': expense['total']
            }

    # Converter o mapa em uma lista e ordenar por valor total
    result = list(category_map.values())
    result.sort(key=lambda x: x['total_amount'], reverse=True)

    return {
        'categories': result,
        'year': year,
        'month': month,
        'month_name': datetime.date(year, month, 1).strftime('%B')
    }
