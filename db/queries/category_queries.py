"""
    Consultas relacionadas a categorias
"""

from db.database import get_db_session, close_db_session
from db.models import Category


def get_category_by_id(category_id, session=None):
    """
    Obtém uma categoria pelo ID

    Args:
        category_id (int): ID da categoria
        session: Sessão SQLAlchemy opcional

    Returns:
        Category: Objeto da categoria ou None se não encontrado
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Category).filter_by(id=category_id).first()
    finally:
        if close_session:
            close_db_session(session)


def get_all_categories(session=None):
    """
    Obtém todas as categorias

    Args:
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Category
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Category).order_by(Category.name).all()
    finally:
        if close_session:
            close_db_session(session)


def get_categories_by_type(category_type, session=None):
    """
    Obtém categorias por tipo

    Args:
        category_type (str): Tipo da categoria ('income', 'expense', 'credit')
        session: Sessão SQLAlchemy opcional

    Returns:
        list: Lista de objetos Category
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        return session.query(Category).filter_by(type=category_type).order_by(Category.name).all()
    finally:
        if close_session:
            close_db_session(session)
