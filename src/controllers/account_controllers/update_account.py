"""
    Módulo para atualizar informações de contas bancárias
"""

from db.database import get_db_session, close_db_session
from db.models import Account

def update_account(account_id, name=None, account_type=None, color=None, active=None):
    """
    Atualiza uma conta existente

    Args:
        account_id (int): ID da conta
        name (str, optional): Novo nome
        account_type (str, optional): Novo tipo
        color (str, optional): Nova cor
        active (bool, optional): Status de ativo/inativo

    Returns:
        bool: True se atualizado com sucesso, False caso contrário
    """
    session = get_db_session()
    try:
        account = session.query(Account).filter_by(id=account_id).first()

        if not account:
            return False

        # Atualizar campos se fornecidos
        if name is not None:
            account.name = name
        if account_type is not None:
            account.type = account_type
        if color is not None:
            account.color = color
        if active is not None:
            account.active = active

        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar conta: {e}")
        return False
    finally:
        close_db_session(session)
