"""
    Consultas relacionadas a despesas
"""

from db.database import get_db_session, close_db_session
from db.models import Expense
from sqlalchemy import func, extract


def get_expense_by_id(expense_id, session=None):
    """
    Obtém uma despesa pelo ID

    Args:
        expense_id (int): ID da despesa
        session: Sessão SQLAlchemy opcional

    Returns:
        Expense: Objeto da despesa ou None se não encontrado
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Expense).filter_by(id=expense_id).first()
    finally:
        if close_session:
            close_db_session(session)


def get_expenses_by_period(start_date, end_date, session=None):
    """
    Obtém despesas em um período específico

    Args:
        start_date (date): Data inicial
        end_date (date): Data final
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Expense
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Expense).filter(
            Expense.date >= start_date,
            Expense.date <= end_date
        ).order_by(Expense.date.desc()).all()
    finally:
        if close_session:
            close_db_session(session)


def get_expenses_by_month(year, month, session=None):
    """
    Obtém despesas de um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Expense
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Expense).filter(
            extract('year', Expense.date) == year,
            extract('month', Expense.date) == month
        ).order_by(Expense.date.desc()).all()
    finally:
        if close_session:
            close_db_session(session)


def get_expenses_by_category(category_id, session=None):
    """
    Obtém despesas de uma categoria específica

    Args:
        category_id (int): ID da categoria
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Expense
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Expense).filter_by(category_id=category_id).order_by(Expense.date.desc()).all()
    finally:
        if close_session:
            close_db_session(session)


def get_monthly_expense_sum(year, month, session=None):
    """
    Obtém a soma de despesas em um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        float: Soma das despesas
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        result = session.query(func.sum(Expense.amount)).filter(
            extract('year', Expense.date) == year,
            extract('month', Expense.date) == month
        ).scalar()
        return float(result) if result else 0.0
    finally:
        if close_session:
            close_db_session(session)
