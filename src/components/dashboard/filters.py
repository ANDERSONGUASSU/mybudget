"""
    Pacote filters - integra todos os componentes de filtros.
"""
from datetime import datetime, timedelta

import dash_bootstrap_components as dbc
from dash import html, dcc
def get_filters():
    """
        Retorna os filtros do dashboard.
    """
    return [
        dbc.Col([
            dbc.Card([

                html.Legend("Filtar Lançamentos", className="card-title"),
                # Categorias da receita
                html.Label("Categorias da receita"),
                html.Div([
                    dcc.Dropdown(
                        id="income-categories",
                        clearable=False,
                        multi=True,
                        style={"width": "100%"},
                        persistence=True,
                        persistence_type="session",
                    ),
                ]),
                # Categorias da despesa
                html.Label("Categorias da despesa", style={"margin-top": "10px"}),
                html.Div([
                    dcc.Dropdown(
                        id="expense-categories",
                        clearable=False,
                        multi=True,
                        style={"width": "100%"},
                        persistence=True,
                        persistence_type="session",
                    ),
                ]),
                # Período de Análise
                html.Label("Período de Análise", style={"margin-top": "10px"}),
                html.Div([
                    dcc.DatePickerRange(
                        id="date-picker-config",
                        end_date_placeholder_text="Data...",
                        start_date=datetime.now() - timedelta(days=30),
                        end_date=datetime.now(),
                        updatemode="singledate",
                        style={"zIndex": "100"},
                        display_format="DD/MM/YYYY",
                    ),
                ])
            ], style={"padding": "20px", "height": "100%"})
        ], width=4, style={"margin-top": "10px"})
    ]
