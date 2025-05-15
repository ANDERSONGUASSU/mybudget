"""
    Callbacks para operações com categorias
"""

from dash.dependencies import Input, Output, State
from dash import html
from app import app

# Importar controladores
from src.controllers.category_controllers import add_category, get_categories_by_type

# Callback para adicionar uma nova categoria
@app.callback(
    [Output("category_message_income", "children"),
     Output("category_name_income", "value")],
    [Input("add_category_button_income", "n_clicks")],
    [State("category_name_income", "value"),
     State("category_color_income", "value")])
def add_new_category_income(n_clicks, name, color):
    """
    Função para adicionar uma nova categoria ao banco de dados
    """
    if not n_clicks or not name:
        return "", None

    # Usar um tipo de categoria padrão (income)
    category_type = "income"  # Valor padrão para categorias de receita

    # Adicionar categoria
    category_id = add_category(name, category_type, color)

    if category_id:
        return html.Div("Categoria adicionada com sucesso!", style={"color": "green"}), ""
    else:
        return html.Div("Erro ao adicionar categoria!", style={"color": "red"}), name

# Callback para carregar categorias de receita
@app.callback(
    Output("income_category", "options"),
    [Input("modal-income", "is_open"),
     Input("category_message_income", "children")])
def load_income_categories(is_open, _):
    """
    Função para carregar as categorias de receita
    """
    if is_open or _:
        return get_categories_by_type("income")
    return []

# Callback para carregar categorias de despesa
@app.callback(
    Output("expense_category", "options"),
    [Input("modal-expense", "is_open"),
     Input("category_message_expense", "children")])
def load_expense_categories(is_open, _):
    """
    Função para carregar as categorias de despesa
    """
    if is_open or _:
        return get_categories_by_type("expense")
    return []

# Callback para carregar categorias de cartão de crédito
@app.callback(
    Output("credit_card_category", "options"),
    [Input("modal-credit-card", "is_open"),
     Input("category_message_credit_card", "children")])
def load_credit_card_categories(is_open, _):
    """
    Função para carregar as categorias de cartão de crédito
    """
    if is_open or _:
        return get_categories_by_type("credit")
    return []
