"""
    Callback para o modal de receita no sidebar.
"""

from dash.dependencies import Input, Output, State
from dash import ctx
from app import app


@app.callback(
    Output("modal-income", "is_open"),
    Input("open_new_income", "n_clicks"),
    State("modal-income", "is_open")
)
def toggle_income_modal(n_clicks, is_open):
    """
    Função para abrir o modal de adição de receita

    Args:
        n_clicks: Número de cliques no botão de adicionar receita
        is_open: Estado atual do modal (aberto ou fechado)

    Returns:
        bool: Novo estado do modal
    """
    if n_clicks:
        return not is_open
    return is_open
