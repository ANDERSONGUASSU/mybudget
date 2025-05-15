"""
    Controladores para operações com contas bancárias
    
    Este pacote contém módulos separados para cada operação com contas:
    - add_account: Para adicionar novas contas
    - get_accounts: Para listar contas
    - update_account_balance: Para atualizar saldo de contas
    - update_account: Para atualizar informações das contas
    - get_total_balance: Para obter saldo total
"""

from src.controllers.account_controllers.add_account import add_account
from src.controllers.account_controllers.get_accounts import get_accounts
from src.controllers.account_controllers.update_account_balance import update_account_balance
from src.controllers.account_controllers.update_account import update_account
from src.controllers.account_controllers.get_total_balance import get_total_balance

# Exportar todas as funções
__all__ = [
    'add_account',
    'get_accounts',
    'update_account_balance',
    'update_account',
    'get_total_balance'
]
