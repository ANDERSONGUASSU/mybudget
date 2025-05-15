"""
    Callbacks para controle de modais no sidebar
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
     Input("open_new_credit_card", "n_clicks"),
     Input("cancel_income_button", "n_clicks"),
     Input("cancel_expense_button", "n_clicks"),
     Input("cancel_credit_card_button", "n_clicks"),
     Input("save_income_button", "n_clicks"),
     Input("save_expense_button", "n_clicks"),
     Input("save_credit_card_button", "n_clicks")],
    [State("modal-income", "is_open"),
     State("modal-expense", "is_open"),
     State("modal-credit-card", "is_open")])
def toggle_modal(n_clicks_income, n_clicks_expense, n_clicks_credit_card,
                 n_clicks_cancel_income, n_clicks_cancel_expense, n_clicks_cancel_credit_card,
                 n_clicks_save_income, n_clicks_save_expense, n_clicks_save_credit_card,
                 is_open_income, is_open_expense, is_open_credit_card):
    """
    Função para abrir ou fechar o modal de adição de receita, despesa ou cartão de crédito
    """
    # Determina qual botão foi clicado através do contexto
    triggered_id = ctx.triggered_id if ctx.triggered_id else None

    if triggered_id == "open_new_income":
        return not is_open_income, is_open_expense, is_open_credit_card
    elif triggered_id == "open_new_expense":
        return is_open_income, not is_open_expense, is_open_credit_card
    elif triggered_id == "open_new_credit_card":
        return is_open_income, is_open_expense, not is_open_credit_card
    elif triggered_id in ["cancel_income_button", "save_income_button"]:
        return False, is_open_expense, is_open_credit_card
    elif triggered_id in ["cancel_expense_button", "save_expense_button"]:
        return is_open_income, False, is_open_credit_card
    elif triggered_id in ["cancel_credit_card_button", "save_credit_card_button"]:
        return is_open_income, is_open_expense, False
    return is_open_income, is_open_expense, is_open_credit_card

# Callback para abrir o modal de adicionar categoria
@app.callback(
    Output("modal-add-category", "is_open"),
    [Input("add_category_button", "n_clicks"),
     Input("close_add_category", "n_clicks")],
    [State("modal-add-category", "is_open")])
def toggle_add_category_modal(n_clicks_add, n_clicks_close, is_open):
    """
    Função para abrir ou fechar o modal de adição de categoria
    """
    if n_clicks_add or n_clicks_close:
        return not is_open
    return is_open

# Callback para abrir o modal de adicionar conta
@app.callback(
    Output("modal-add-account", "is_open"),
    [Input("add_account_button", "n_clicks"),
     Input("close_add_account", "n_clicks")],
    [State("modal-add-account", "is_open")])
def toggle_add_account_modal(n_clicks_add, n_clicks_close, is_open):
    """
    Função para abrir ou fechar o modal de adição de conta
    """
    if n_clicks_add or n_clicks_close:
        return not is_open
    return is_open
