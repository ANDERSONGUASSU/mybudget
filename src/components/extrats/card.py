"""
    Pacote card - integra todos os componentes de cards.
"""

from dash import html
import dash_bootstrap_components as dbc

def get_card():
    """
        Retorna o card de informações de extratos.
    """
    return [
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.H4("Total de Receitas"),
                    html.H3("R$ 5.420,00", className="text-success")
                ], width=4),
                dbc.Col([
                    html.H4("Total de Despesas"),
                    html.H3("R$ 3.150,00", className="text-danger")
                ], width=4),
                dbc.Col([
                    html.H4("Saldo Final"),
                    html.H3("R$ 2.270,00", className="text-primary")
                ], width=4),
            ]),
            html.Hr(),
            html.P("Últimos 30 dias", className="text-muted")
        ])
    ]
