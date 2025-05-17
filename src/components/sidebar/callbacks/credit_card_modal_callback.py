"""
    Callback para o modal de cartão de crédito no sidebar.
"""

from dash.dependencies import Input, Output, State
from app import app


@app.callback(
    Output("modal-credit-card", "is_open"),
    Input("open_new_credit_card", "n_clicks"),
    State("modal-credit-card", "is_open")
)
def toggle_credit_card_modal(n_clicks, is_open):
    """
    Função para abrir o modal de adição de transação de cartão de crédito
    
    Args:
        n_clicks: Número de cliques no botão de adicionar transação de cartão
        is_open: Estado atual do modal (aberto ou fechado)
        
    Returns:
        bool: Novo estado do modal
    """
    if n_clicks:
        return not is_open
    return is_open 