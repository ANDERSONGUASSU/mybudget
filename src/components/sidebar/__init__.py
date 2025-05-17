"""
    Pacote sidebar - integra todos os componentes do sidebar.
"""

import dash_bootstrap_components as dbc

# Importação dos componentes do sidebar
from src.components.sidebar.header import get_header
from src.components.sidebar.profile import get_profile
from src.components.sidebar.actions import get_action_buttons
from src.components.sidebar.modals.income_modal import get_income_modal
from src.components.sidebar.modals.expense_modal import get_expense_modal
from src.components.sidebar.modals.credit_card_modal import get_credit_card_modal
from src.components.sidebar.nav import get_nav

# Importar callbacks para registro (não precisa usar diretamente)
import callbacks  # noqa

# Layout principal do sidebar
layout = dbc.Col([
    # Cabeçalho
    *get_header(),

    # Seção Perfil
    *get_profile(),

    # Seção Novo Lançamento
    *get_action_buttons(),

    # Modais
    get_income_modal(),
    get_expense_modal(),
    get_credit_card_modal(),

    # Seção Navegação
    get_nav(),
], id="sidebar")
