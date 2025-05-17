"""
    Callback para o modal de despesa no sidebar.
"""

from dash.dependencies import Input, Output, State
from app import app


@app.callback(
    Output("modal-expense", "is_open"),
    Input("open_new_expense", "n_clicks"),
    State("modal-expense", "is_open")
)
def toggle_expense_modal(n_clicks, is_open):
    """
    Função para abrir o modal de adição de despesa

    Args:
        n_clicks: Número de cliques no botão de adicionar despesa
        is_open: Estado atual do modal (aberto ou fechado)

    Returns:
        bool: Novo estado do modal
    """
    if n_clicks:
        return not is_open
    return is_open
