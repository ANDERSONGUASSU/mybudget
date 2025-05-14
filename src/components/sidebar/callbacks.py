"""
    Callbacks para os componentes do sidebar.
"""

from dash.dependencies import Input, Output, State
from dash import ctx
from app import app

# Callback para abrir os modais de receita, despesa e cartão de crédito
@app.callback(
    [Output("modal-income", "is_open"),
     Output("modal-expense", "is_open"),
     Output("modal-credit-card", "is_open")],
    [Input("open_new_income", "n_clicks"),
     Input("open_new_expense", "n_clicks"),
     Input("open_new_credit_card", "n_clicks")],
    [State("modal-income", "is_open"),
     State("modal-expense", "is_open"),
     State("modal-credit-card", "is_open")])
def toggle_modal(n_clicks_income, n_clicks_expense, n_clicks_credit_card,
                 is_open_income, is_open_expense, is_open_credit_card):
    """
    Função para abrir o modal de adição de receita, despesa ou cartão de crédito
    """
    # Determina qual botão foi clicado através do contexto
    triggered_id = ctx.triggered_id if ctx.triggered_id else None

    if triggered_id == "open_new_income":
        return not is_open_income, is_open_expense, is_open_credit_card
    elif triggered_id == "open_new_expense":
        return is_open_income, not is_open_expense, is_open_credit_card
    elif triggered_id == "open_new_credit_card":
        return is_open_income, is_open_expense, not is_open_credit_card
    return is_open_income, is_open_expense, is_open_credit_card
