"""
    Controlador para atualizar uma conta bancária
"""

from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.queries.account_queries import get_account_by_id


def update_account(account_id, name=None, balance=None):
    """
    Atualiza uma conta bancária existente

    Args:
        account_id (int): ID da conta a ser atualizada
        name (str, optional): Novo nome da conta
        balance (float, optional): Novo saldo da conta

    Returns:
        dict: Dicionário com informações da conta atualizada ou None se falhar
    """
    session = get_db_session()

    try:
        # Buscar a conta
        account = get_account_by_id(account_id, session)

        if not account:
            return None

        # Atualizar campos fornecidos
        if name is not None:
            account.name = name

        if balance is not None:
            account.balance = balance

        # Salvar alterações
        session.commit()

        # Retornar dados atualizados
        return {
            'id': account.id,
            'name': account.name,
            'balance': account.balance
        }
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao atualizar conta: {e}")
        return None
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao atualizar conta: {e}")
        return None
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao atualizar conta: {e}")
        return None
    finally:
        close_db_session(session)
