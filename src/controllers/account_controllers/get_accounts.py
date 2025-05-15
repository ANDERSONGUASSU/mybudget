"""
    Módulo para listar contas bancárias
"""

from db.database import get_db_session, close_db_session
from db.models import Account

def get_accounts(active_only=True):
    """
    Obtém todas as contas bancárias

    Args:
        active_only (bool, optional): Retornar apenas contas ativas

    Returns:
        list: Lista de dicionários com id, name, type, balance e color das contas
    """
    session = get_db_session()
    try:
        query = session.query(Account)

        if active_only:
            query = query.filter(Account.active)

        accounts = query.order_by(Account.name).all()

        # Converter para formato mais simples para o frontend
        result = [
            {
                "id": account.id,
                "label": account.name,
                "value": account.id,
                "type": account.type,
                "balance": account.balance,
                "color": account.color
            }
            for account in accounts
        ]

        return result
    except Exception as e:
        print(f"Erro ao obter contas: {e}")
        return []
    finally:
        close_db_session(session)
