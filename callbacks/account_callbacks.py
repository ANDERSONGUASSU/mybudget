"""
    Callbacks para o modal de contas
"""

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app

from controllers.account_controllers import (
    create_account,
    delete_account
)


# Callback para adicionar uma nova conta em receita
@app.callback(
    [Output("account_message_income", "children"),
     Output("account_name_income", "value"),
     Output("account_type_income", "value"),
     Output("account_balance_income", "value")],
    Input("add_account_button_income", "n_clicks"),
    State("account_name_income", "value"),
    State("account_type_income", "value"),
    State("account_balance_income", "value"),
    prevent_initial_call=True
)
def add_income_account(n_clicks, name, type_income, balance):
    """
    Adiciona uma nova conta de receita e limpa os campos
    """
    if not n_clicks or not name:
        return "", None, None, None

    # Criar nova conta
    result = create_account(name, type_income, balance)

    if result:
        # Limpar os campos e mostrar mensagem de sucesso
        return dbc.Alert(f"Conta '{name}' adicionada com sucesso!", color="success"), "", "", ""
    else:
        # Manter os campos e mostrar erro
        return dbc.Alert("Erro ao adicionar conta.", color="danger"), name, type_income, balance


# Callback para adicionar uma nova conta em despesa
@app.callback(
    [Output("account_message_expense", "children"),
     Output("account_name_expense", "value"),
     Output("account_type_expense", "value"),
     Output("account_balance_expense", "value")],
    Input("add_account_button_expense", "n_clicks"),
    State("account_name_expense", "value"),
    State("account_type_expense", "value"),
    State("account_balance_expense", "value"),
    prevent_initial_call=True
)
def add_expense_account(n_clicks, name, type_expense, balance):
    """
    Adiciona uma nova conta de despesa e limpa os campos
    """
    if not n_clicks or not name:
        return "", None, None, None

    # Criar nova conta
    result = create_account(name, type_expense, balance)

    if result:
        # Limpar os campos e mostrar mensagem de sucesso
        return dbc.Alert(f"Conta '{name}' adicionada com sucesso!", color="success"), "", "", ""
    else:
        # Manter os campos e mostrar erro
        return dbc.Alert("Erro ao adicionar conta.", color="danger"), name, type_expense, balance


# Callback para atualizar as checklists de contas usando o store
@app.callback(
    Output("delete_account_checklist_income", "options"),
    Input("accounts-store", "data")
)
def update_income_account_checklist(accounts_data):
    """
    Atualiza a checklist de contas de receita usando o store
    """
    options = [{"label": f"{acc['name']} ({acc['type']})", "value": acc['id']} for acc in accounts_data]
    return options


@app.callback(
    Output("delete_account_checklist_expense", "options"),
    Input("accounts-store", "data")
)
def update_expense_account_checklist(accounts_data):
    """
    Atualiza a checklist de contas de despesa usando o store
    """
    options = [{"label": f"{acc['name']} ({acc['type']})", "value": acc['id']} for acc in accounts_data]
    return options


# Callback para exclusão de contas em receita
@app.callback(
    Output("account_message_income", "children", allow_duplicate=True),
    Input("delete_account_button_income", "n_clicks"),
    State("delete_account_checklist_income", "value"),
    prevent_initial_call=True
)
def delete_income_account(n_clicks, account_ids):
    """
    Exclui contas de receita selecionadas
    """
    if not n_clicks or not account_ids:
        return ""

    # Excluir contas selecionadas
    success_count = 0
    error_count = 0

    for account_id in account_ids:
        result = delete_account(account_id)
        if result:
            success_count += 1
        else:
            error_count += 1

    if success_count == 0:
        result = f"Erro ao excluir {error_count} conta(s)."
        return dbc.Alert(result, color="danger")
    elif error_count == 0:
        result = f"{success_count} conta(s) excluída(s) com sucesso."
        return dbc.Alert(result, color="success")
    else:
        result = [
            f"{success_count} conta(s) excluída(s) com sucesso.",
            f"{error_count} conta(s) não puderam ser excluídas.",
            "Verifique se não estão sendo usadas em transações."
        ]
        return dbc.Alert(result, color="warning")


# Callback para exclusão de contas em despesa
@app.callback(
    Output("account_message_expense", "children", allow_duplicate=True),
    Input("delete_account_button_expense", "n_clicks"),
    State("delete_account_checklist_expense", "value"),
    prevent_initial_call=True
)
def delete_expense_account(n_clicks, account_ids):
    """
    Exclui contas de despesa selecionadas
    """
    if not n_clicks or not account_ids:
        return ""

    # Excluir contas selecionadas
    success_count = 0
    error_count = 0

    for account_id in account_ids:
        result = delete_account(account_id)
        if result:
            success_count += 1
        else:
            error_count += 1

    if success_count == 0:
        result = f"Erro ao excluir {error_count} conta(s)."
        return dbc.Alert(result, color="danger")
    elif error_count == 0:
        result = f"{success_count} conta(s) excluída(s) com sucesso."
        return dbc.Alert(result, color="success")
    else:
        result = [
            f"{success_count} conta(s) excluída(s) com sucesso.",
            f"{error_count} conta(s) não puderam ser excluídas.",
            "Verifique se não estão sendo usadas em transações."
        ]
        return dbc.Alert(result, color="warning")
