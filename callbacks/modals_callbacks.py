"""
    Callbacks para gerenciar todos os modais
"""

from dash import callback_context as ctx
from dash.dependencies import Input, Output, State
from app import app

@app.callback(
    Output("modal-income", "is_open"),
    Output("modal-expense", "is_open"),
    Output("modal-credit-card", "is_open"),
    Input("open_new_income", "n_clicks"),
    Input("open_new_expense", "n_clicks"),
    Input("open_new_credit_card", "n_clicks"),
    State("modal-income", "is_open"),
    State("modal-expense", "is_open"),
    State("modal-credit-card", "is_open"),
    prevent_initial_call=True
)
def gerenciar_todos_modais(
    n_clicks_receita,
    n_clicks_despesa,
    n_clicks_cartao,
    is_open_income,
    is_open_expense,
    is_open_credit_card
):
    """
    Gerencia todos os modais
    """
    # Identificar qual botão foi clicado
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == "open_new_income":
        return True, False, False  # Abre modal de receita, fecha os outros
    elif trigger_id == "open_new_expense":
        return False, True, False  # Abre modal de despesa, fecha os outros
    elif trigger_id == "open_new_credit_card":
        return False, False, True  # Abre modal de cartão, fecha os outros
    else:
        return False, False, False  # Fecha todos por padrão


# Callback para fechar o modal de receita ao clicar em Cancelar
@app.callback(
    Output("modal-income", "is_open", allow_duplicate=True),
    Input("cancel_income_button", "n_clicks"),
    State("modal-income", "is_open"),
    prevent_initial_call=True
)
def fechar_modal_receita(n_clicks, is_open):
    """
    Fecha o modal de receita ao clicar em Cancelar
    """
    if n_clicks:
        return False
    return is_open


# Callback para fechar o modal de despesa ao clicar em Cancelar
@app.callback(
    Output("modal-expense", "is_open", allow_duplicate=True),
    Input("cancel_expense_button", "n_clicks"),
    State("modal-expense", "is_open"),
    prevent_initial_call=True
)
def fechar_modal_despesa(n_clicks, is_open):
    """
    Fecha o modal de despesa ao clicar em Cancelar
    """

    if n_clicks:
        return False
    return is_open


# Callback para fechar o modal de cartão de crédito ao clicar em Cancelar
@app.callback(
    Output("modal-credit-card", "is_open", allow_duplicate=True),
    Input("cancel_credit_card_button", "n_clicks"),
    State("modal-credit-card", "is_open"),
    prevent_initial_call=True
)
def fechar_modal_cartao(n_clicks, is_open):
    """
    Fecha o modal de cartão de crédito ao clicar em Cancelar
    """
    if n_clicks:
        return False
    return is_open
