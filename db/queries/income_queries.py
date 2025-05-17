"""
    Consultas relacionadas a receitas
"""

from db.database import get_db_session, close_db_session
from db.models import Income
from sqlalchemy import func, extract


def get_income_by_id(income_id, session=None):
    """
    Obtém uma receita pelo ID

    Args:
        income_id (int): ID da receita
        session: Sessão SQLAlchemy opcional

    Returns:
        Income: Objeto da receita ou None se não encontrado
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Income).filter_by(id=income_id).first()
    finally:
        if close_session:
            close_db_session(session)


def get_incomes_by_period(start_date, end_date, session=None):
    """
    Obtém receitas em um período específico

    Args:
        start_date (date): Data inicial
        end_date (date): Data final
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Income
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Income).filter(
            Income.date >= start_date,
            Income.date <= end_date
        ).order_by(Income.date.desc()).all()
    finally:
        if close_session:
            close_db_session(session)


def get_incomes_by_month(year, month, session=None):
    """
    Obtém receitas de um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Income
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Income).filter(
            extract('year', Income.date) == year,
            extract('month', Income.date) == month
        ).order_by(Income.date.desc()).all()
    finally:
        if close_session:
            close_db_session(session)


def get_incomes_by_category(category_id, session=None):
    """
    Obtém receitas de uma categoria específica

    Args:
        category_id (int): ID da categoria
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Income
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Income).filter_by(category_id=category_id).order_by(Income.date.desc()).all()
    finally:
        if close_session:
            close_db_session(session)


def get_monthly_income_sum(year, month, session=None):
    """
    Obtém a soma de receitas em um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        session: Sessão SQLAlchemy opcional

    Returns:
        float: Soma das receitas
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        result = session.query(func.sum(Income.amount)).filter(
            extract('year', Income.date) == year,
            extract('month', Income.date) == month
        ).scalar()
        return float(result) if result else 0.0
    finally:
        if close_session:
            close_db_session(session)
