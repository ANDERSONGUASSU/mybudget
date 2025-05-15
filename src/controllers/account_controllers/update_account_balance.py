"""
    Módulo para atualizar saldo de contas bancárias
"""

from db.database import get_db_session, close_db_session
from db.models import Account

def update_account_balance(account_id, amount, is_credit=True):
    """
    Atualiza o saldo de uma conta

    Args:
        account_id (int): ID da conta
        amount (float): Valor a ser adicionado/subtraído
        is_credit (bool, optional): True para adicionar, False para subtrair

    Returns:
        bool: True se atualizado com sucesso, False caso contrário
    """
    session = get_db_session()
    try:
        account = session.query(Account).filter_by(id=account_id).first()

        if not account:
            return False

        # Atualizar saldo
        if is_credit:
            account.balance += amount
        else:
            account.balance -= amount

        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar saldo da conta: {e}")
        return False
    finally:
        close_db_session(session)
