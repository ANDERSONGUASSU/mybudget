"""
    Componente de cabeçalho do sidebar.
"""

from dash import html

# Componente de cabeçalho
def get_header():
    """
    Retorna o cabeçalho do sidebar.
    """
    return [
        html.H1("Minhas Finanças", className="text-center title"),
        html.P("Bem-vindo ao sistema de gerenciamento de finanças pessoais.",
               className="text-center text-info"),
        html.Hr(),
    ]
