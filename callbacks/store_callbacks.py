"""
    Callbacks para gerenciar os stores de dados (contas, categorias, cartões)
"""

from dash.dependencies import Input, Output
from app import app

from controllers.account_controllers import get_accounts
from controllers.category_controllers import get_categories, get_categories_for_type
from controllers.credit_card_controllers import get_credit_cards


# Callback para carregar as contas no store
@app.callback(
    Output("accounts-store", "data"),
    [
        Input("add_account_button_income", "n_clicks"),
        Input("add_account_button_expense", "n_clicks"),
        Input("delete_account_button_income", "n_clicks"),
        Input("delete_account_button_expense", "n_clicks")
    ]
)
def update_accounts_store(add_income_clicks, add_expense_clicks, delete_income_clicks, delete_expense_clicks):
    """
    Atualiza o store de contas sempre que houver alterações
    """
    # Buscar todas as contas do banco de dados
    accounts = get_accounts()
    return accounts


# Callback para carregar as categorias no store
@app.callback(
    Output("categories-store", "data"),
    [
        Input("add_category_button_income", "n_clicks"),
        Input("add_category_button_expense", "n_clicks"),
        Input("add_category_button_credit_card", "n_clicks"),
        Input("delete_category_button_income", "n_clicks"),
        Input("delete_category_button_expense", "n_clicks"),
        Input("delete_category_button_credit_card", "n_clicks")
    ]
)
def update_categories_store(add_income_clicks, add_expense_clicks, add_credit_card_clicks,
                            delete_income_clicks, delete_expense_clicks, delete_credit_card_clicks):
    """
    Atualiza o store de categorias sempre que houver alterações
    """
    # Buscar todas as categorias
    categories = get_categories()

    # Organizar por tipo
    categories_by_type = {
        "income": get_categories_for_type("income"),
        "expense": get_categories_for_type("expense"),
        "credit": get_categories_for_type("credit")
    }

    return {
        "all": categories,
        "by_type": categories_by_type
    }


# Callback para carregar os cartões de crédito no store
@app.callback(
    Output("credit-cards-store", "data"),
    [
        Input("add_credit_card_button", "n_clicks")
        # Adicione outros triggers se houver botões para excluir cartões
    ]
)
def update_credit_cards_store(add_clicks):
    """
    Atualiza o store de cartões de crédito sempre que houver alterações
    """
    # Buscar todos os cartões de crédito
    credit_cards = get_credit_cards()
    return credit_cards
