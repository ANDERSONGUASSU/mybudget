"""
    Módulo de inicialização do dashboard.
"""

import dash_bootstrap_components as dbc
from src.components.dashboard.cards import get_cards
from src.components.dashboard.filters import get_filters
from src.components.dashboard.grafic import get_grafic

layout = dbc.Row([
    *get_cards(),
    *get_filters(),
    *get_grafic(1, 8),
    *get_grafic(2, 6),
    *get_grafic(3, 3),
    *get_grafic(4, 3),
], id="dashboard", style={"margin": "10px"})
