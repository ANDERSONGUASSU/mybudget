"""
    Componente de modal para adição de cartão de crédito.
"""

from dash import html
import dash_bootstrap_components as dbc

def get_new_credit_card_modal():
    """
    Retorna o modal de adição de cartão de crédito.
    """
    return dbc.Accordion([
        dbc.AccordionItem(
            title="Adicionar/Excluir Cartão de Crédito",
            children=[
                dbc.Row([
                    dbc.Col([
                        html.Legend("Adicionar Cartão de Crédito"),
                        dbc.Input(
                            id="credit_card_new_name",
                            placeholder="Nome do cartão de crédito",
                            className="mb-3"),
                        dbc.Input(
                            id="credit_card_due_date",
                            placeholder="dia de vencimento",
                            className="mb-3"),
                        dbc.Input(
                            id="credit_card_closing_date",
                            placeholder="dia de fechamento",
                            className="mb-3"),
                        dbc.Input(
                            id="credit_card_limit",
                            placeholder="limite",
                            className="mb-3"),
                        dbc.Button(
                            "Adicionar",
                            id="add_credit_card_button",
                            color="primary",
                            className="mb-3 btn btn-success"),
                        html.Div(id="credit_card_message", className="mt-3", style={},)
                    ], width=6, className="mb-3 p-2"),
                    dbc.Col([
                        html.Legend("Excluir Cartão de Crédito", className="text-danger"),
                        dbc.Checklist(
                            id="delete_credit_card_checklist",
                            options=[],
                            value=[],
                            switch=True,
                            label_checked_style={'color': 'red'},
                            input_checked_style={'backgroundColor': 'blue', 'border-color': 'orange'}
                        ),
                        dbc.Button(
                            "Excluir",
                            id="delete_credit_card_button",
                            color="danger",
                            className="mb-3 btn btn-danger"),
                    ], width=6, className="mb-3 p-2")
                ])
            ])
    ], id="add_credit_card_modal", start_collapsed=True, flush=True)
