"""
    Callbacks para preencher os selects de contas nos modais
"""

from dash.dependencies import Input, Output
from app import app


# Callback para preencher o select de contas no modal de receita
@app.callback(
    Output("income_account", "options"),
    [
        Input("modal-income", "is_open"),
        Input("accounts-store", "data")
    ]
)
def preencher_contas_receita(is_open, accounts_data):
    """
    Preenche o select de contas no modal de receita
    """
    if not is_open or not accounts_data:
        return []

    options = [
        {"label": f"{acc['name']} ({acc['type']})", "value": acc['id']}
        for acc in accounts_data
    ]
    return options


# Callback para preencher o select de contas no modal de despesa
@app.callback(
    Output("expense_account", "options"),
    [
        Input("modal-expense", "is_open"),
        Input("accounts-store", "data")
    ]
)
def preencher_contas_despesa(is_open, accounts_data):
    """
    Preenche o select de contas no modal de despesa
    """
    if not is_open or not accounts_data:
        return []

    options = [
        {"label": f"{acc['name']} ({acc['type']})", "value": acc['id']}
        for acc in accounts_data
    ]
    return options


# Callback para preencher o select de cartões no modal de cartão de crédito
@app.callback(
    Output("credit_card_account", "options"),
    [
        Input("modal-credit-card", "is_open"),
        Input("credit-cards-store", "data")
    ]
)
def preencher_cartoes_credit_card(is_open, credit_cards_data):
    """
    Preenche o select de cartões no modal de cartão de crédito
    """
    if not is_open or not credit_cards_data:
        return []

    # Formatar para as opções do select
    options = [{"label": f"{card['name']}", "value": card["id"]} for card in credit_cards_data]

    return options
