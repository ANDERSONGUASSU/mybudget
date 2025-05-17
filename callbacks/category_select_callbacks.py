"""
    Callbacks para preencher os selects de categorias nos modais
"""

from dash.dependencies import Input, Output
from app import app

from controllers.category_controllers import get_categories_for_type


# Callback para preencher o select de categorias de receita no modal de receita
@app.callback(
    Output("income_category", "options"),
    [
        Input("modal-income", "is_open"),
        Input("add_category_button_income", "n_clicks"),
        Input("delete_category_button_income", "n_clicks")
    ]
)
def preencher_categorias_receita(is_open, add_clicks, delete_clicks):
    """
    Preenche o select de categorias no modal de receita
    """
    if not is_open and add_clicks is None and delete_clicks is None:
        return []

    # Buscar categorias de receita no banco de dados
    categories = get_categories_for_type("income")

    # Formatar para as opções do select
    options = [{"label": cat["name"], "value": cat["id"]} for cat in categories]

    return options


# Callback para preencher o select de categorias de despesa no modal de despesa
@app.callback(
    Output("expense_category", "options"),
    [
        Input("modal-expense", "is_open"),
        Input("add_category_button_expense", "n_clicks"),
        Input("delete_category_button_expense", "n_clicks")
    ]
)
def preencher_categorias_despesa(is_open, add_clicks, delete_clicks):
    """
    Preenche o select de categorias no modal de despesa
    """
    if not is_open and add_clicks is None and delete_clicks is None:
        return []

    # Buscar categorias de despesa no banco de dados
    categories = get_categories_for_type("expense")

    # Formatar para as opções do select
    options = [{"label": cat["name"], "value": cat["id"]} for cat in categories]

    return options


# Callback para preencher o select de categorias de cartão de crédito no modal de cartão de crédito
@app.callback(
    Output("credit_card_category", "options"),
    [
        Input("modal-credit-card", "is_open"),
        Input("add_category_button_credit_card", "n_clicks"),
        Input("delete_category_button_credit_card", "n_clicks")
    ]
)
def preencher_categorias_cartao(is_open, add_clicks, delete_clicks):
    """
    Preenche o select de categorias no modal de cartão de crédito
    """
    if not is_open and add_clicks is None and delete_clicks is None:
        return []

    # Buscar categorias de cartão de crédito no banco de dados
    categories = get_categories_for_type("credit")

    # Se não tiver categorias específicas para cartão de crédito, usar as de despesa
    if not categories:
        categories = get_categories_for_type("expense")

    # Formatar para as opções do select
    options = [{"label": cat["name"], "value": cat["id"]} for cat in categories]

    return options
