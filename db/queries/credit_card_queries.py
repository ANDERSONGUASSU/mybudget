"""
    Consultas relacionadas a cartões de crédito
"""

from db.database import get_db_session, close_db_session
from db.models import CreditCard, CreditCardTransaction
from sqlalchemy import func
import datetime


def get_credit_card_by_id(credit_card_id, session=None):
    """
    Obtém um cartão de crédito pelo ID

    Args:
        credit_card_id (int): ID do cartão de crédito
        session: Sessão SQLAlchemy opcional

    Returns:
        CreditCard: Objeto do cartão de crédito ou None se não encontrado
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(CreditCard).filter_by(id=credit_card_id).first()
    finally:
        if close_session:
            close_db_session(session)


def get_all_credit_cards(session=None):
    """
    Obtém todos os cartões de crédito

    Args:
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos CreditCard
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(CreditCard).order_by(CreditCard.name).all()
    finally:
        if close_session:
            close_db_session(session)


def get_credit_card_transaction_by_id(transaction_id, session=None):
    """
    Obtém uma transação de cartão de crédito pelo ID

    Args:
        transaction_id (int): ID da transação
        session: Sessão SQLAlchemy opcional

    Returns:
        CreditCardTransaction: Objeto da transação ou None se não encontrado
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(CreditCardTransaction).filter_by(id=transaction_id).first()
    finally:
        if close_session:
            close_db_session(session)


def get_credit_card_statement(card_id, year, month, session=None):
    """
    Obtém a fatura do cartão de crédito para um mês específico

    Args:
        card_id (int): ID do cartão
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        dict: Dicionário com transações e total da fatura
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        # Formatar mês de referência no formato YYYY-MM
        statement_month = f"{year:04d}-{month:02d}"

        # Buscar transações do cartão para o mês de referência
        transactions = session.query(CreditCardTransaction).filter(
            CreditCardTransaction.credit_card_id == card_id,
            CreditCardTransaction.statement_month == statement_month
        ).order_by(CreditCardTransaction.purchase_date).all()

        # Calcular total da fatura
        total = sum(t.amount for t in transactions)

        # Obter dados do cartão
        card = session.query(CreditCard).filter_by(id=card_id).first()

        return {
            "transactions": transactions,
            "total": total,
            "card": card,
            "statement_month": statement_month
        }
    finally:
        if close_session:
            close_db_session(session)


def get_credit_card_transactions_by_period(card_id, start_date, end_date, session=None):
    """
    Obtém transações de cartão de crédito em um período específico

    Args:
        card_id (int): ID do cartão
        start_date (date): Data inicial
        end_date (date): Data final
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos CreditCardTransaction
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(CreditCardTransaction).filter(
            CreditCardTransaction.credit_card_id == card_id,
            CreditCardTransaction.purchase_date >= start_date,
            CreditCardTransaction.purchase_date <= end_date
        ).order_by(CreditCardTransaction.purchase_date.desc()).all()
    finally:
        if close_session:
            close_db_session(session)


def get_credit_card_available_limit(card_id, session=None):
    """
    Calcula o limite disponível em um cartão de crédito

    Args:
        card_id (int): ID do cartão
        session: Sessão SQLAlchemy opcional

    Returns:
        float: Limite disponível
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        # Obter informações do cartão
        card = session.query(CreditCard).filter_by(id=card_id).first()

        if not card:
            return 0.0

        # Obter o mês atual para a fatura
        today = datetime.date.today()
        statement_month = f"{today.year:04d}-{today.month:02d}"

        # Calcular o total de compras pendentes (não pagas) na fatura atual
        current_statement_total = session.query(func.sum(CreditCardTransaction.amount)).filter(
            CreditCardTransaction.credit_card_id == card_id,
            CreditCardTransaction.statement_month == statement_month
        ).scalar() or 0.0

        # Limite disponível = limite total - valor usado
        available_limit = card.limit_amount - float(current_statement_total)

        return available_limit
    finally:
        if close_session:
            close_db_session(session)
