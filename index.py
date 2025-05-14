"""
    Este arquivo é o ponto de entrada do aplicativo.
    Ele define a estrutura básica do aplicativo, incluindo o layout
    e a lógica de roteamento.
"""

from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from src.components.sidebar import layout as sidebar_layout
from src.components.dashboard import layout as dashboard_layout
from src.components.extrats import layout as extrats_layout


# Elemento div para conteúdo da página
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col(
            [
                dcc.Location(id="url"),
                sidebar_layout,
            ], md=2, style={"backgroundColor": "#f8f9fa", "height": "100vh"}),
        dbc.Col(
            [
                content  # Aqui será renderizado o conteúdo da página atual
            ], md=10, style={"backgroundColor": "white", "height": "100vh"})
    ]),
], fluid=True)


# callback para renderizar a página correspondente ao pathname
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page(pathname):
    """
        Renderiza a página correspondente ao pathname.
    """
    if pathname == "/" or pathname == "/dashboard":
        return dashboard_layout
    elif pathname == "/extratos":
        return extrats_layout
    else:
        return html.Div([
            html.H1("404: Página não encontrada", className="text-danger"),
            html.Hr(),
            html.P(f"A página {pathname} não existe.")
        ])


if __name__ == "__main__":
    app.run(debug=True)
