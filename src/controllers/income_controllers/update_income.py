"""
    Módulo para atualizar receitas
"""

from db.database import get_db_session, close_db_session
from db.models import Income
from src.controllers.account_controllers import update_account_balance
from datetime import datetime

def update_income(income_id, description=None, amount=None, date=None,
                  category_id=None, account_id=None, notes=None):
    """
    Atualiza uma receita existente

    Args:
        income_id (int): ID da receita
        description (str, optional): Descrição da receita
        amount (float, optional): Valor da receita
        date (str ou datetime, optional): Data da receita
        category_id (int, optional): ID da categoria
        account_id (int, optional): ID da conta
        notes (str, optional): Observações

    Returns:
        bool: True se atualizada com sucesso, False caso contrário
    """
    session = get_db_session()
    try:
        # Obter receita
        income = session.query(Income).filter_by(id=income_id).first()

        if not income:
            return False

        # Salvar valor original para ajuste de saldo
        original_amount = income.amount
        original_account_id = income.account_id

        # Atualizar campos se fornecidos
        if description is not None:
            income.description = description

        if amount is not None:
            income.amount = amount

        if date is not None:
            if isinstance(date, str):
                date = datetime.strptime(date, "%Y-%m-%d")
            income.date = date

        if category_id is not None:
            income.category_id = category_id

        if account_id is not None:
            income.account_id = account_id

        if notes is not None:
            income.notes = notes

        # Atualizar saldo da conta original (remover valor antigo)
        if original_amount and original_account_id:
            update_account_balance(original_account_id, original_amount, is_credit=False)

        # Adicionar novo valor na nova conta (ou mesma conta)
        if amount is not None and account_id is not None:
            update_account_balance(account_id, amount, is_credit=True)
        elif amount is not None:
            update_account_balance(income.account_id, amount, is_credit=True)
        elif account_id is not None:
            update_account_balance(account_id, income.amount, is_credit=True)

        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar receita: {e}")
        return False
    finally:
        close_db_session(session)
