"""
    Pacote de callbacks para o sidebar

    Este pacote contém callbacks separados para cada funcionalidade do sidebar.
"""

# Importar callbacks para registro (ordem importa para dependências)
from callbacks.store_callbacks import *  # Primeiro os stores
from callbacks.modals_callbacks import *
from callbacks.category_callbacks import *
from callbacks.category_select_callbacks import *
from callbacks.account_callbacks import *
from callbacks.account_select_callbacks import *
