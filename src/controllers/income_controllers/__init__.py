"""
    Controladores para operações com receitas
    
    Este pacote contém módulos separados para cada operação com receitas:
    - add_income: Para adicionar novas receitas
    - get_incomes_by_period: Para listar receitas em um período
    - get_monthly_income_sum: Para obter a soma de receitas em um mês
    - delete_income: Para remover receitas
    - update_income: Para atualizar receitas
"""

from src.controllers.income_controllers.add_income import add_income
from src.controllers.income_controllers.get_incomes_by_period import get_incomes_by_period
from src.controllers.income_controllers.get_monthly_income_sum import get_monthly_income_sum
from src.controllers.income_controllers.delete_income import delete_income
from src.controllers.income_controllers.update_income import update_income

# Exportar todas as funções
__all__ = [
    'add_income',
    'get_incomes_by_period',
    'get_monthly_income_sum',
    'delete_income',
    'update_income'
]
