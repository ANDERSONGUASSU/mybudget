"""
    Callbacks para operações com contas
"""

from dash.dependencies import Input, Output, State
from dash import html
from app import app

# Importar controladores
from src.controllers.account_controllers import add_account, get_accounts

# Callback para adicionar uma nova conta
@app.callback(
    [Output("account_message_income", "children"),
     Output("account_name_income", "value")],
    [Input("add_account_button_income", "n_clicks")],
    [State("account_name_income", "value")])
def add_new_account_income(n_clicks, name):
    """
    Função para adicionar uma nova conta ao banco de dados
    """
    if not n_clicks or not name:
        return "", None

    # Usar valores padrão para os campos ausentes
    account_type = "corrente"  # Valor padrão
    balance_float = 0.0  # Valor padrão
    color = "#4CAF50"  # Valor padrão (verde)

    # Adicionar conta
    account_id = add_account(name, account_type, balance_float, color)

    if account_id:
        return html.Div("Conta adicionada com sucesso!", style={"color": "green"}), ""
    else:
        return html.Div("Erro ao adicionar conta!", style={"color": "red"}), name

# Callback para carregar contas
@app.callback(
    [Output("income_account", "options"),
     Output("expense_account", "options")],
    [Input("modal-income", "is_open"),
     Input("modal-expense", "is_open"),
     Input("account_message_income", "children")])
def load_accounts(is_income_open, is_expense_open, _):
    """
    Função para carregar as contas
    """
    if is_income_open or is_expense_open or _:
        accounts = get_accounts()
        return accounts, accounts
    return [], []
