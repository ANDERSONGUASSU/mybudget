"""
    Pacote de callbacks para o sidebar
    
    Este pacote contém callbacks separados para cada funcionalidade do sidebar.
"""

# Importar todos os callbacks
from src.components.sidebar.callbacks.income_modal_callback import *
from src.components.sidebar.callbacks.expense_modal_callback import *
from src.components.sidebar.callbacks.credit_card_modal_callback import *
from src.components.sidebar.callbacks.account_modal_callback import *

# Manter o callback antigo temporariamente para compatibilidade
# TODO: Remover após migração completa para callbacks separados
from src.components.sidebar.callbacks.modals_callbacks import *
