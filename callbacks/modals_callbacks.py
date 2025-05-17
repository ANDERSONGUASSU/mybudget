from dash import callback_context as ctx
from app import app
from dash.dependencies import Input, Output, State

@app.callback(
    Output("modal-income", "is_open"),
    Output("modal-expense", "is_open"),
    Output("modal-credit-card", "is_open"),
    Input("botao-receita", "n_clicks"),
    Input("botao-despesa", "n_clicks"),
    Input("botao-cartao", "n_clicks"),
    State("modal-income", "is_open"),
    State("modal-expense", "is_open"),
    State("modal-credit-card", "is_open"),
    prevent_initial_call=True
)
def gerenciar_todos_modais(n_clicks_receita, n_clicks_despesa, n_clicks_cartao, is_open_income, is_open_expense, is_open_credit_card):
    # Identificar qual botão foi clicado
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == "botao-receita":
        return True, False, False  # Abre modal de receita, fecha os outros
    elif trigger_id == "botao-despesa":
        return False, True, False  # Abre modal de despesa, fecha os outros
    elif trigger_id == "botao-cartao":
        return False, False, True  # Abre modal de cartão, fecha os outros
    else:
        return False, False, False  # Fecha todos por padrão
