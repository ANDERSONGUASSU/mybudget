"""
    Consultas relacionadas a contas bancárias
"""

from db.database import get_db_session, close_db_session
from db.models import Account
from sqlalchemy import func


def get_account_by_id(account_id, session=None):
    """
    Obtém uma conta pelo ID

    Args:
        account_id (int): ID da conta
        session: Sessão SQLAlchemy opcional

    Returns:
        Account: Objeto da conta ou None se não encontrado
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Account).filter_by(id=account_id).first()
    finally:
        if close_session:
            close_db_session(session)


def get_all_accounts(session=None):
    """
    Obtém todas as contas bancárias

    Args:
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Account
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Account).order_by(Account.name).all()
    finally:
        if close_session:
            close_db_session(session)


def get_account_balance(account_id, session=None):
    """
    Obtém o saldo atual de uma conta

    Args:
        account_id (int): ID da conta
        session: Sessão SQLAlchemy opcional

    Returns:
        float: Saldo da conta
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        account = session.query(Account).filter_by(id=account_id).first()
        return account.balance if account else 0.0
    finally:
        if close_session:
            close_db_session(session)


def get_total_balance(session=None):
    """
    Obtém o saldo total de todas as contas

    Args:
        session: Sessão SQLAlchemy opcional

    Returns:
        float: Saldo total de todas as contas
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        result = session.query(func.sum(Account.balance)).scalar()
        return float(result) if result else 0.0
    finally:
        if close_session:
            close_db_session(session)
