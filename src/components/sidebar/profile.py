"""
    Componente de perfil do usuário para o sidebar.
"""

from dash import html
import dash_bootstrap_components as dbc

# Componente de perfil
def get_profile():
    return [
        html.H2("Perfil", className="text-center text-primary"),
        html.Div([
            dbc.Button(
                id="btn-perfil",
                className="btn-perfil",
                children=[
                    html.Img(src="/assets/img/homem.svg", id='avatar_change',
                             alt='Avatar', className='perfil_avatar')
                ],
            ),
        ], className="d-flex justify-content-center"),
    ]
