"""
    Pacote extrats - integra todos os componentes de extratos.
"""

import dash_bootstrap_components as dbc
from dash import html
from src.components.extrats.card import get_card
from src.components.extrats.grafic import get_grafic
from src.components.extrats.table import get_table

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Página de Extratos", className="text-primary text-center my-4"),
            html.Hr(),
            dbc.Card([
                dbc.CardHeader("Tabela de Extratos", className="bg-primary text-white"),
                dbc.CardBody(*get_table())
            ], className="mb-4 border-primary"),

            dbc.Card([
                dbc.CardHeader("Informações de Extratos", className="bg-success text-white"),
                dbc.CardBody(*get_card())
            ], className="mb-4 border-success"),

            dbc.Card([
                dbc.CardHeader("Gráfico de Extratos", className="bg-info text-white"),
                dbc.CardBody([get_grafic()])
            ], className="mb-4 border-info")
        ], width=12)
    ])
], fluid=True, id="extrats", className="p-4 bg-light")
