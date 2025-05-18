"""
    Callbacks para preencher os selects de categorias nos modais
"""

from dash.dependencies import Input, Output
from app import app


# Callback para preencher o select de categorias de receita no modal de receita
@app.callback(
    Output("income_category", "options"),
    [
        Input("modal-income", "is_open"),
        Input("categories-store", "data")
    ]
)
def preencher_categorias_receita(is_open, categories_data):
    """
    Preenche o select de categorias no modal de receita
    """
    if not is_open or not categories_data:
        return []

    # Buscar categorias de receita do store
    categories = categories_data["by_type"]["income"]

    # Formatar para as opções do select
    options = [{"label": cat["name"], "value": cat["id"]} for cat in categories]

    return options


# Callback para preencher o select de categorias de despesa no modal de despesa
@app.callback(
    Output("expense_category", "options"),
    [
        Input("modal-expense", "is_open"),
        Input("categories-store", "data")
    ]
)
def preencher_categorias_despesa(is_open, categories_data):
    """
    Preenche o select de categorias no modal de despesa
    """
    if not is_open or not categories_data:
        return []

    # Buscar categorias de despesa do store
    categories = categories_data["by_type"]["expense"]

    # Formatar para as opções do select
    options = [{"label": cat["name"], "value": cat["id"]} for cat in categories]

    return options


# Callback para preencher o select de categorias de cartão de crédito no modal de cartão de crédito
@app.callback(
    Output("credit_card_category", "options"),
    [
        Input("modal-credit-card", "is_open"),
        Input("categories-store", "data")
    ]
)
def preencher_categorias_cartao(is_open, categories_data):
    """
    Preenche o select de categorias no modal de cartão de crédito
    """
    if not is_open or not categories_data:
        return []

    # Buscar categorias de cartão de crédito do store
    categories = categories_data["by_type"]["credit"]

    # Se não tiver categorias específicas para cartão de crédito, usar as de despesa
    if not categories:
        categories = categories_data["by_type"]["expense"]

    # Formatar para as opções do select
    options = [{"label": cat["name"], "value": cat["id"]} for cat in categories]

    return options
