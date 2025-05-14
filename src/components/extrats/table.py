"""
    Pacote table - integra todos os componentes de tabelas.
"""

from dash import html, dash_table
import pandas as pd
import dash_bootstrap_components as dbc

def get_table():
    """
        Retorna a tabela de extratos com dados de exemplo.
    """
    # Dados de exemplo
    data = [
        {"Data": "05/05/2023", "Descrição": "Salário", "Categoria": "Receita", "Valor": "R$ 3.500,00", "Tipo": "Entrada"},
        {"Data": "10/05/2023", "Descrição": "Aluguel", "Categoria": "Moradia", "Valor": "R$ 1.200,00", "Tipo": "Saída"},
        {"Data": "12/05/2023", "Descrição": "Supermercado", "Categoria": "Alimentação", "Valor": "R$ 450,00", "Tipo": "Saída"},
        {"Data": "15/05/2023", "Descrição": "Freelance", "Categoria": "Receita", "Valor": "R$ 1.200,00", "Tipo": "Entrada"},
        {"Data": "18/05/2023", "Descrição": "Internet", "Categoria": "Utilidades", "Valor": "R$ 120,00", "Tipo": "Saída"},
        {"Data": "20/05/2023", "Descrição": "Dividendos", "Categoria": "Investimentos", "Valor": "R$ 720,00", "Tipo": "Entrada"},
        {"Data": "25/05/2023", "Descrição": "Restaurante", "Categoria": "Alimentação", "Valor": "R$ 180,00", "Tipo": "Saída"}
    ]

    df = pd.DataFrame(data)

    return [
        html.Div([
            dbc.Row([
                dbc.Col([
                    dash_table.DataTable(
                        data=df.to_dict('records'),
                        columns=[{"name": i, "id": i} for i in df.columns],
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold'
                        },
                        style_data_conditional=[
                            {
                                'if': {
                                    'filter_query': '{Tipo} = "Entrada"',
                                },
                                'backgroundColor': 'rgba(50, 205, 50, 0.2)',
                                'color': 'green'
                            },
                            {
                                'if': {
                                    'filter_query': '{Tipo} = "Saída"',
                                },
                                'backgroundColor': 'rgba(255, 99, 71, 0.2)',
                                'color': 'red'
                            }
                        ],
                        style_cell={
                            'textAlign': 'left',
                            'padding': '10px'
                        },
                        page_size=5,
                        sort_action='native',
                        filter_action='native',
                        style_table={'overflowX': 'auto'}
                    )
                ], width=12)
            ]),
            html.Div(id="table-output")
        ])
    ]
