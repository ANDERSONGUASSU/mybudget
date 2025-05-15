"""
    Módulo para remover receitas
"""

from db.database import get_db_session, close_db_session
from db.models import Income
from src.controllers.account_controllers import update_account_balance

def delete_income(income_id):
    """
    Remove uma receita e atualiza o saldo da conta

    Args:
        income_id (int): ID da receita

    Returns:
        bool: True se removida com sucesso, False caso contrário
    """
    session = get_db_session()
    try:
        # Obter receita
        income = session.query(Income).filter_by(id=income_id).first()

        if not income:
            return False

        # Atualizar saldo da conta (subtrair o valor)
        update_account_balance(income.account_id, income.amount, is_credit=False)

        # Remover receita
        session.delete(income)
        session.commit()

        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao remover receita: {e}")
        return False
    finally:
        close_db_session(session)
