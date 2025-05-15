"""
    Módulo para adicionar contas bancárias
"""

from db.database import get_db_session, close_db_session
from db.models import Account

def add_account(name, account_type, initial_balance=0.0, color="#2196F3"):
    """
    Adiciona uma nova conta bancária ao banco de dados

    Args:
        name (str): Nome da conta
        account_type (str): Tipo da conta ('checking', 'savings', 'investment')
        initial_balance (float, optional): Saldo inicial. Padrão é 0.0
        color (str, optional): Cor em hexadecimal. Padrão é azul (#2196F3)

    Returns:
        int: ID da conta criada ou None em caso de erro
    """
    session = get_db_session()
    try:
        # Verificar se já existe uma conta com o mesmo nome
        existing = session.query(Account).filter(Account.name == name).first()

        if existing:
            # Se já existe, apenas retorna o ID
            return existing.id

        # Criar nova conta
        new_account = Account(
            name=name,
            type=account_type,
            balance=initial_balance,
            color=color,
            active=True
        )

        # Adicionar ao banco e obter ID
        session.add(new_account)
        session.commit()
        session.refresh(new_account)

        return new_account.id
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar conta: {e}")
        return None
    finally:
        close_db_session(session)
