"""
    Callbacks para operações com receitas
"""

from dash.dependencies import Input, Output, State
from dash import html
from app import app

# Importar controladores
from src.controllers.income_controllers import add_income

# Callback para adicionar uma nova receita
@app.callback(
    Output("id_test_income", "children"),
    [Input("save_income_button", "n_clicks")],
    [State("income_name", "value"),
     State("income_value", "value"),
     State("income_date", "date"),
     State("income_category", "value"),
     State("income_account", "value"),
     State("income_recurrence", "value")])
def save_income(n_clicks, description, amount, date, category_id, account_id, recurrence_type):
    """
    Função para adicionar uma nova receita ao banco de dados
    """
    if not n_clicks:
        return ""

    # Validar campos obrigatórios
    if not description or not amount or not date or not category_id or not account_id:
        return html.Div("Por favor, preencha todos os campos obrigatórios!", style={"color": "red"})

    # Converter valor para float
    try:
        amount_float = float(amount.replace("R$", "").replace(".", "").replace(",", ".").strip())
    except (ValueError, AttributeError):
        try:
            amount_float = float(amount)
        except (ValueError, TypeError):
            return html.Div("Valor inválido!", style={"color": "red"})

    # Adicionar receita
    income_id = add_income(
        description=description,
        amount=amount_float,
        date=date,
        category_id=category_id,
        account_id=account_id,
        recurrence_type=recurrence_type
    )

    if income_id:
        return html.Div("Receita adicionada com sucesso!", style={"color": "green"})
    else:
        return html.Div("Erro ao adicionar receita!", style={"color": "red"})

# Callback para limpar o formulário de receita quando o modal é fechado
@app.callback(
    [Output("income_name", "value"),
     Output("income_value", "value"),
     Output("income_category", "value"),
     Output("income_account", "value"),
     Output("income_recurrence", "value")],
    [Input("modal-income", "is_open")],
    [State("income_name", "value"),
     State("income_value", "value"),
     State("income_category", "value"),
     State("income_account", "value"),
     State("income_recurrence", "value")])
def clear_income_form(is_open, name, value, category, account, recurrence):
    """
    Função para limpar o formulário de receita quando o modal é fechado
    """
    if not is_open:
        return "", "", None, None, "unica"
    return name, value, category, account, recurrence
