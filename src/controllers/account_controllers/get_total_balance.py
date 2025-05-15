"""
    Módulo para obter o saldo total das contas bancárias
"""

from db.database import get_db_session, close_db_session
from db.models import Account
from sqlalchemy import func

def get_total_balance():
    """
    Obtém o saldo total de todas as contas ativas

    Returns:
        float: Saldo total
    """
    session = get_db_session()
    try:
        result = session.query(func.sum(Account.balance)).filter(
            Account.active
        ).scalar()

        return float(result) if result else 0.0
    except Exception as e:
        print(f"Erro ao obter saldo total: {e}")
        return 0.0
    finally:
        close_db_session(session)
