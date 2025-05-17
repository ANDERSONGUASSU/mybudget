"""
    Callbacks para o modal de contas bancárias no sidebar.
"""

from dash.dependencies import Input, Output, State
from app import app
from controllers.account_controllers.create_account import create_account
from controllers.account_controllers.get_accounts import get_accounts
from controllers.account_controllers.delete_account import delete_account


@app.callback(
    Output("account_message_income", "children"),
    Input("add_account_button_income", "n_clicks"),
    State("account_name_income", "value"),
    prevent_initial_call=True
)
def add_account_income(n_clicks, account_name):
    """
    Adiciona uma nova conta bancária através do modal de receitas

    Args:
        n_clicks: Número de cliques no botão de adicionar conta
        account_name: Nome da nova conta

    Returns:
        str: Mensagem de sucesso ou erro
    """
    if not n_clicks or not account_name:
        return ""

    result = create_account(name=account_name)

    if result:
        return f"Conta '{account_name}' adicionada com sucesso!"
    else:
        return "Erro ao adicionar conta. Tente novamente."


@app.callback(
    Output("account_message_expense", "children"),
    Input("add_account_button_expense", "n_clicks"),
    State("account_name_expense", "value"),
    prevent_initial_call=True
)
def add_account_expense(n_clicks, account_name):
    """
    Adiciona uma nova conta bancária através do modal de despesas

    Args:
        n_clicks: Número de cliques no botão de adicionar conta
        account_name: Nome da nova conta

    Returns:
        str: Mensagem de sucesso ou erro
    """
    if not n_clicks or not account_name:
        return ""

    result = create_account(name=account_name)

    if result:
        return f"Conta '{account_name}' adicionada com sucesso!"
    else:
        return "Erro ao adicionar conta. Tente novamente."


@app.callback(
    [Output("delete_account_checklist_income", "options"),
     Output("delete_account_checklist_expense", "options")],
    [Input("add_account_button_income", "n_clicks"),
     Input("add_account_button_expense", "n_clicks"),
     Input("delete_account_button_income", "n_clicks"),
     Input("delete_account_button_expense", "n_clicks")]
)
def update_account_checklists(n_add_income, n_add_expense, n_del_income, n_del_expense):
    """
    Atualiza as listas de contas disponíveis para exclusão

    Returns:
        tuple: Opções de contas para os checklists
    """
    # Buscar todas as contas
    accounts = get_accounts()

    # Formatar as opções para os checklists
    options = [{"label": account["name"], "value": account["id"]} for account in accounts]

    # Retornar as mesmas opções para ambos os checklists
    return options, options


@app.callback(
    [Output("account_message_income", "children", allow_duplicate=True),
     Output("delete_account_checklist_income", "value")],
    Input("delete_account_button_income", "n_clicks"),
    State("delete_account_checklist_income", "value"),
    prevent_initial_call=True
)
def delete_account_income(n_clicks, account_ids):
    """
    Exclui as contas selecionadas no modal de receitas

    Args:
        n_clicks: Número de cliques no botão de excluir conta
        account_ids: Lista de IDs das contas a serem excluídas

    Returns:
        tuple: (Mensagem de sucesso/erro, Lista vazia para resetar a seleção)
    """
    if not n_clicks or not account_ids:
        return "", []

    success_count = 0
    failed_count = 0

    # Tentar excluir cada conta selecionada
    for account_id in account_ids:
        result = delete_account(account_id)
        if result:
            success_count += 1
        else:
            failed_count += 1

    # Preparar mensagem
    message = ""
    if success_count > 0:
        message += f"{success_count} conta(s) excluída(s) com sucesso. "
    if failed_count > 0:
        message += f"{failed_count} conta(s) não puderam ser excluídas (possuem transações)."

    # Retornar mensagem e lista vazia para resetar a seleção
    return message, []


@app.callback(
    [Output("account_message_expense", "children", allow_duplicate=True),
     Output("delete_account_checklist_expense", "value")],
    Input("delete_account_button_expense", "n_clicks"),
    State("delete_account_checklist_expense", "value"),
    prevent_initial_call=True
)
def delete_account_expense(n_clicks, account_ids):
    """
    Exclui as contas selecionadas no modal de despesas

    Args:
        n_clicks: Número de cliques no botão de excluir conta
        account_ids: Lista de IDs das contas a serem excluídas

    Returns:
        tuple: (Mensagem de sucesso/erro, Lista vazia para resetar a seleção)
    """
    if not n_clicks or not account_ids:
        return "", []

    success_count = 0
    failed_count = 0

    # Tentar excluir cada conta selecionada
    for account_id in account_ids:
        result = delete_account(account_id)
        if result:
            success_count += 1
        else:
            failed_count += 1

    # Preparar mensagem
    message = ""
    if success_count > 0:
        message += f"{success_count} conta(s) excluída(s) com sucesso. "
    if failed_count > 0:
        message += f"{failed_count} conta(s) não puderam ser excluídas (possuem transações)."

    # Retornar mensagem e lista vazia para resetar a seleção
    return message, []
