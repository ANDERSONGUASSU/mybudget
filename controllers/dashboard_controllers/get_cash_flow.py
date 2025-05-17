"""
    Controlador para obter o fluxo de caixa dos últimos meses
"""

from db.queries.dashboard_queries import get_cash_flow_last_6_months


def get_cash_flow():
    """
    Obtém o fluxo de caixa dos últimos 6 meses

    Returns:
        dict: Dicionário com dados do fluxo de caixa
    """
    # Obter dados do fluxo de caixa
    cash_flow = get_cash_flow_last_6_months()

    # Preparar dados para gráficos
    chart_data = {
        'labels': cash_flow['months'],
        'datasets': [
            {
                'label': 'Receitas',
                'data': cash_flow['incomes'],
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Despesas',
                'data': cash_flow['expenses'],
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Saldo',
                'data': cash_flow['balances'],
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1,
                'type': 'line'
            }
        ]
    }

    # Calcular totais
    total_income = sum(cash_flow['incomes'])
    total_expense = sum(cash_flow['expenses'])
    total_balance = total_income - total_expense

    return {
        'chart_data': chart_data,
        'raw_data': cash_flow,
        'total_income': total_income,
        'total_expense': total_expense,
        'total_balance': total_balance,
        'positive_trend': cash_flow['balances'][-1] > cash_flow['balances'][0] if cash_flow['balances'] else False
    }
