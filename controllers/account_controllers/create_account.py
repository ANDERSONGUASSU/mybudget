"""
    Controlador para criar uma nova conta bancária
"""

from db.database import get_db_session, close_db_session
from db.models.account_model import Account


def create_account(name, type, balance=0.0):
    """
    Cria uma nova conta bancária

    Args:
        name (str): Nome da conta
        balance (float, optional): Saldo inicial da conta

    Returns:
        dict: Dicionário com informações da conta criada ou None se falhar
    """
    if not name:
        return None

    session = get_db_session()

    try:
        # Criar nova conta
        new_account = Account(name=name, type=type, balance=balance)

        # Adicionar ao banco de dados
        session.add(new_account)
        session.commit()

        # Retornar dados da conta criada
        return {
            'id': new_account.id,
            'name': new_account.name,
            'type': new_account.type,
            'balance': new_account.balance
        }
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar conta: {e}")
        return None
    finally:
        close_db_session(session)
