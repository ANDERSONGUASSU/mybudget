"""
    Componente de navegação do sidebar.
"""

from dash import html
import dash_bootstrap_components as dbc

# Componente de navegação
def get_nav():
    """
        Retorna a navegação do sidebar.
    """
    return dbc.Nav([
        dbc.NavLink(
            href="/dashboard",
            active="exact",
            className="btn-NavLink",
            children=[
                html.I(className="fas fa-chart-line me-2"),
                html.Span("Dashboard")
            ],
        ),
        dbc.NavLink(
            href="/extratos",
            active="exact",
            className="btn-NavLink",
            children=[
                html.I(className="fas fa-list-alt me-2"),
                html.Span("Extratos")
            ],
        ),
    ],
        vertical=True,
        pills=True,
        id="sidebar-nav",
        className="sidebar-nav")
