"""
    Pacote cards - integra todos os componentes de cards.
"""

import dash_bootstrap_components as dbc
from dash import html

card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto"
}
def get_cards():
    """
        Retorna os cards do dashboard.
    """
    return [
        # Saldo
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Saldo"),
                    html.H5("R$ 1000,00", id="balance", style={}),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card([
                    html.I(className='fa fa-university', style=card_icon),
                ], color="warning",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"}),
            ]),
        ], width=4),
        # Receita
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Receita"),
                    html.H5("R$ 1000,00", id="income", style={}),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card([
                    html.I(className='fa fa-arrow-up', style=card_icon),
                ], color="success",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"}),
            ])
        ], width=4),
        # Despesa
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Despesa"),
                    html.H5("R$ 1000,00", id="expense", style={}),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card([
                    html.I(className='fa fa-arrow-down', style=card_icon),
                ], color="danger",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"}),
            ])
        ], width=4)
    ]
