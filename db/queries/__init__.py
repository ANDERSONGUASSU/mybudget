"""
    Queries para operações com o banco de dados
    
    Este pacote contém módulos separados para consultas específicas:
    - income_queries: Para consultas relacionadas a receitas
    - expense_queries: Para consultas relacionadas a despesas
    - credit_card_queries: Para consultas relacionadas a transações de cartão de crédito
    - category_queries: Para consultas relacionadas a categorias
    - account_queries: Para consultas relacionadas a contas
    - recurrence_queries: Para consultas relacionadas a recorrências
    - report_queries: Para consultas relacionadas a relatórios
"""

# Importar todas as queries
from db.queries.income_queries import *
from db.queries.expense_queries import *
from db.queries.credit_card_queries import *
from db.queries.category_queries import *
from db.queries.account_queries import *
from db.queries.recurrence_queries import *
from db.queries.report_queries import *
