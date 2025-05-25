# callbacks/income_callbacks.py
"""
    Pacote de callbacks para o modal de adição de receita

    Este pacote contém callbacks separados para cada funcionalidade do modal de adição de receita.
"""
from datetime import datetime
from dash.dependencies import Input, Output, State
from dash import callback_context
from app import app
# Importar controller de receitas
from controllers.income_controllers import create_income
from db.database import get_db_session, close_db_session

@app.callback(
    [
        Output("income_name", "value"),
        Output("income_value", "value"),
        Output("income_date", "date"),
        Output("income_category", "value"),
        Output("income_account", "value"),
        Output("income_recurrence", "value"),
        Output("income_frequency", "value"),
    ],
    [
        Input("save_income_button", "n_clicks"),
        Input("cancel_income_button", "n_clicks"),
    ],
    [
        State("income_name", "value"),
        State("income_value", "value"),
        State("income_date", "date"),
        State("income_category", "value"),
        State("income_account", "value"),
        State("income_recurrence", "value"),
        State("income_frequency", "value"),
    ]
)
def save_income_modal(save_clicks, cancel_clicks, name, value, date, category, account, recurrence, frequency):
    """
    Salva o modal de adição de receita.

    Quando o botão Salvar é clicado, salva os dados da receita no banco de dados.
    Quando o botão Cancelar é clicado, apenas limpa os campos.
    Em ambos os casos, retorna valores vazios para limpar o formulário.
    """
    ctx = callback_context

    # Se nenhum botão foi clicado, não fazer nada
    if not ctx.triggered:
        return [name, value, date, category, account, recurrence, frequency]

    # Identificar qual botão foi clicado
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "save_income_button" and save_clicks:
        if name and value and date and category and account:
            if recurrence != "unica":
                session = get_db_session()
                try:

                    create_income(
                        description=name,
                        amount=float(value),
                        date=date,
                        category_id=category,
                        account_id=account,
                        recurrence_id=None
                    )
                finally:
                    close_db_session(session)
            else:
                create_income(
                    description=name,
                    amount=float(value),
                    date=date,
                    category_id=category,
                    account_id=account,
                    recurrence_id=None
                )
    if button_id == "cancel_income_button" and cancel_clicks:
        return [None, None, datetime.now().strftime("%Y-%m-%d"), None, None, "unica", 1]

    # Limpar os campos e fechar o modal
    return [None, None, datetime.now().strftime("%Y-%m-%d"), None, None, "unica", 1]
