"""
    Pacote de callbacks para o sidebar

    Este pacote contém callbacks separados para cada funcionalidade do sidebar.
"""

# Importar callbacks para registro (ordem importa para dependências)
from callbacks.store_callbacks import (
    update_accounts_store,
    update_categories_store,
    update_credit_cards_store
)
from callbacks.modals_callbacks import (
    gerenciar_todos_modais,
    fechar_modal_cartao,
    fechar_modal_despesa,
    fechar_modal_receita
)
from callbacks.category_callbacks import (
    add_income_category,
    add_expense_category,
    add_credit_card_category,
    update_income_category_checklist,
    update_expense_category_checklist,
    update_credit_card_category_checklist,
    delete_income_categories,
    delete_expense_categories,
    delete_credit_card_categories,
)
from callbacks.account_callbacks import (
    add_income_account,
    add_expense_account,
    update_income_account_checklist,
    update_expense_account_checklist,
    delete_income_account,
    delete_expense_account,
)
from callbacks.category_select_callbacks import (
    preencher_categorias_receita,
    preencher_categorias_despesa,
    preencher_categorias_cartao,
)
from callbacks.account_select_callbacks import (
    preencher_contas_receita,
    preencher_contas_despesa,
    preencher_cartoes_credit_card,
)
from callbacks.income_callbacks import (
    save_income_modal,
)




__all__ = [
    "update_accounts_store",
    "update_categories_store",
    "update_credit_cards_store",
    "gerenciar_todos_modais",
    "fechar_modal_cartao",
    "fechar_modal_despesa",
    "fechar_modal_receita",
    "add_income_category",
    "add_expense_category",
    "add_credit_card_category",
    "update_income_category_checklist",
    "update_expense_category_checklist",
    "update_credit_card_category_checklist",
    "delete_income_categories",
    "delete_expense_categories",
    "delete_credit_card_categories",
    "preencher_categorias_receita",
    "preencher_categorias_despesa",
    "preencher_categorias_cartao",
    "add_income_account",
    "add_expense_account",
    "update_income_account_checklist",
    "update_expense_account_checklist",
    "delete_income_account",
    "delete_expense_account",
    "preencher_contas_receita",
    "preencher_contas_despesa",
    "preencher_cartoes_credit_card",
    "save_income_modal"
]
