"""
    Controlador para excluir uma conta bancária
"""

from db.database import get_db_session, close_db_session
from db.queries.account_queries import get_account_by_id
from db.models import Income, Expense


def delete_account(account_id):
    """
    Exclui uma conta bancária

    Args:
        account_id (int): ID da conta a ser excluída

    Returns:
        bool: True se a conta foi excluída com sucesso, False caso contrário
    """
    session = get_db_session()

    try:
        # Buscar a conta
        account = get_account_by_id(account_id, session)

        if not account:
            return False

        # Verificar se existem transações associadas à conta
        income_count = session.query(Income).filter_by(account_id=account_id).count()
        expense_count = session.query(Expense).filter_by(account_id=account_id).count()

        if income_count > 0 or expense_count > 0:
            # Não é possível excluir uma conta com transações associadas
            return False

        # Excluir a conta
        session.delete(account)
        session.commit()

        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao excluir conta: {e}")
        return False
    finally:
        close_db_session(session)
