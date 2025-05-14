"""
    Pacote grafic - integra todos os componentes de gráficos.
"""

import dash_bootstrap_components as dbc
from dash import dcc

def get_grafic(num, width):
    """
        Retorna o gráfico do dashboard.
    """
    return [
        dbc.Col(
            dbc.Card(
                dcc.Graph(id=f"grafic-{num}", style={"height": "100%", "padding": "10px"}),
            ), width=width, style={"margin-top": "10px"}
        )
    ]
