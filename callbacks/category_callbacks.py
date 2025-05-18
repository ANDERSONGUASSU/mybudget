"""
    Callbacks para o modal de categorias
"""

from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from controllers.category_controllers import (
    create_category,
    get_categories_for_type,
    delete_category
)


# Callback para adicionar uma nova categoria
@app.callback(
    Output("category_message_income", "children"),
    Input("add_category_button_income", "n_clicks"),
    State("category_name_income", "value"),
    State("category_color_income", "value"),
    prevent_initial_call=True
)
def add_income_category(n_clicks, name, color):
    """
    Adiciona uma nova categoria de receita
    """
    if not n_clicks or not name:
        return ""

    # Criar nova categoria
    result = create_category(name, "income", color)

    if result:
        return dbc.Alert(f"Categoria '{name}' adicionada com sucesso!", color="success")
    else:
        return dbc.Alert("Erro ao adicionar categoria.", color="danger")


# Callback para adicionar uma nova categoria de despesa
@app.callback(
    Output("category_message_expense", "children"),
    Input("add_category_button_expense", "n_clicks"),
    State("category_name_expense", "value"),
    State("category_color_expense", "value"),
    prevent_initial_call=True
)
def add_expense_category(n_clicks, name, color):
    """
    Adiciona uma nova categoria de despesa
    """
    if not n_clicks or not name:
        return ""

    # Criar nova categoria
    result = create_category(name, "expense", color)

    if result:
        return dbc.Alert(f"Categoria '{name}' adicionada com sucesso!", color="success")
    else:
        return dbc.Alert("Erro ao adicionar categoria.", color="danger")


# Callback para adicionar uma nova categoria de cartão de crédito
@app.callback(
    Output("category_message_credit_card", "children"),
    Input("add_category_button_credit_card", "n_clicks"),
    State("category_name_credit_card", "value"),
    State("category_color_credit_card", "value"),
    prevent_initial_call=True
)
def add_credit_card_category(n_clicks, name, color):
    """
    Adiciona uma nova categoria de cartão de crédito
    """
    if not n_clicks or not name:
        return ""

    # Criar nova categoria
    result = create_category(name, "credit", color)

    if result:
        return dbc.Alert(f"Categoria '{name}' adicionada com sucesso!", color="success")
    else:
        return dbc.Alert("Erro ao adicionar categoria.", color="danger")


# Callbacks para atualizar as checklists de categorias
@app.callback(
    Output("delete_category_checklist_income", "options"),
    Input("add_category_button_income", "n_clicks"),
    Input("delete_category_button_income", "n_clicks")
)
def update_income_category_checklist(add_clicks, delete_clicks):
    """
    Atualiza a checklist de categorias de receita
    """
    categories = get_categories_for_type("income")
    options = [{"label": f"{cat['name']} ({cat['color']})", "value": cat['id']} for cat in categories]
    return options


@app.callback(
    Output("delete_category_checklist_expense", "options"),
    Input("add_category_button_expense", "n_clicks"),
    Input("delete_category_button_expense", "n_clicks")
)
def update_expense_category_checklist(add_clicks, delete_clicks):
    """
    Atualiza a checklist de categorias de despesa
    """
    categories = get_categories_for_type("expense")
    options = [{"label": f"{cat['name']} ({cat['color']})", "value": cat['id']} for cat in categories]
    return options


@app.callback(
    Output("delete_category_checklist_credit_card", "options"),
    Input("add_category_button_credit_card", "n_clicks"),
    Input("delete_category_button_credit_card", "n_clicks")
)
def update_credit_card_category_checklist(add_clicks, delete_clicks):

    """
    Atualiza a checklist de categorias de cartão de crédito
    """
    categories = get_categories_for_type("credit")
    options = [{"label": f"{cat['name']} ({cat['color']})", "value": cat['id']} for cat in categories]
    return options


# Callbacks para excluir categorias
@app.callback(
    Output("category_message_income", "children", allow_duplicate=True),
    Input("delete_category_button_income", "n_clicks"),
    State("delete_category_checklist_income", "value"),
    prevent_initial_call=True
)
def delete_income_categories(n_clicks, category_ids):
    """
    Exclui categorias de receita selecionadas
    """
    if not n_clicks or not category_ids:
        return ""

    # Excluir categorias selecionadas
    success_count = 0
    error_count = 0

    for category_id in category_ids:
        result = delete_category(category_id)
        if result:
            success_count += 1
        else:
            error_count += 1

    if error_count == 0:
        return dbc.Alert(f"{success_count} categoria(s) excluída(s) com sucesso!", color="success")
    elif success_count == 0:
        result = f"Erro ao excluir {error_count} categoria(s). Verifique se não estão sendo usadas em transações."
        return dbc.Alert(result, color="danger")
    else:
        result = [
            f"{success_count} categoria(s) excluída(s) com sucesso.",
            f"{error_count} categoria(s) não puderam ser excluídas.",
            "Verifique se não estão sendo usadas em transações."
        ]
        return dbc.Alert(result, color="warning")


@app.callback(
    Output("category_message_expense", "children", allow_duplicate=True),
    Input("delete_category_button_expense", "n_clicks"),
    State("delete_category_checklist_expense", "value"),
    prevent_initial_call=True
)
def delete_expense_categories(n_clicks, category_ids):
    """
    Exclui categorias de despesa selecionadas
    """
    if not n_clicks or not category_ids:
        return ""

    # Excluir categorias selecionadas
    success_count = 0
    error_count = 0

    for category_id in category_ids:
        result = delete_category(category_id)
        if result:
            success_count += 1
        else:
            error_count += 1

    if error_count == 0:
        return dbc.Alert(f"{success_count} categoria(s) excluída(s) com sucesso!", color="success")
    elif success_count == 0:
        result = f"Erro ao excluir {error_count} categoria(s). Verifique se não estão sendo usadas em transações."
        return dbc.Alert(result, color="danger")
    else:
        result = [
            f"{success_count} categoria(s) excluída(s) com sucesso.",
            f"{error_count} categoria(s) não puderam ser excluídas.",
            "Verifique se não estão sendo usadas em transações."
        ]
        return dbc.Alert(result, color="warning")


@app.callback(
    Output("category_message_credit_card", "children", allow_duplicate=True),
    Input("delete_category_button_credit_card", "n_clicks"),
    State("delete_category_checklist_credit_card", "value"),
    prevent_initial_call=True
)
def delete_credit_card_categories(n_clicks, category_ids):
    """
    Exclui categorias de cartão de crédito selecionadas
    """
    if not n_clicks or not category_ids:
        return ""

    # Excluir categorias selecionadas
    success_count = 0
    error_count = 0

    for category_id in category_ids:
        result = delete_category(category_id)
        if result:
            success_count += 1
        else:
            error_count += 1

    if error_count == 0:
        return dbc.Alert(f"{success_count} categoria(s) excluída(s) com sucesso!", color="success")
    elif success_count == 0:
        result = f"Erro ao excluir {error_count} categoria(s). Verifique se não estão sendo usadas em transações."
        return dbc.Alert(result, color="danger")
    else:
        result = [
            f"{success_count} categoria(s) excluída(s) com sucesso.",
            f"{error_count} categoria(s) não puderam ser excluídas.",
            "Verifique se não estão sendo usadas em transações."
        ]
        return dbc.Alert(result, color="warning")
