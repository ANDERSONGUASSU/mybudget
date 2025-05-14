"""
    Componente de botões de ação (receita e despesa) para o sidebar.
"""

from dash import html
import dash_bootstrap_components as dbc

# Componente de botões de ação
def get_action_buttons():
    """
    Retorna os botões de ação para o sidebar.
    """
    return [
        dbc.Row([
            dbc.Col([
                dbc.Button(
                    className="btn-income action-button",
                    id="open_new_income",
                    children=[
                        '+ Receita'
                    ],
                ),
            ], width=6, className="d-flex justify-content-center"),

            dbc.Col([
                dbc.Button(
                    className="btn-expense action-button",
                    id="open_new_expense",
                    children=[
                        '- Despesa'
                    ],
                ),
            ], width=6, className="d-flex justify-content-center")
        ], className="buttons-row g-2"),

        dbc.Row([
            dbc.Col([
                dbc.Button(
                    className="btn-credit-card action-button",
                    id="open_new_credit_card",
                    color="danger",
                    children=[
                        html.I(className="fas fa-credit-card me-2"),
                        'Cartão de Crédito'
                    ],
                ),
            ], width=12, className="d-flex justify-content-center mt-2")
        ], className="buttons-row"),

        html.Hr(),
    ]
