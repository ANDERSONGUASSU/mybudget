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


def update_category_in_db(category_id, name=None, category_type=None, color=None, session=None):
    """
    Atualiza uma categoria no banco de dados

    Args:
        category_id (int): ID da categoria
        name (str, optional): Novo nome da categoria
        category_type (str, optional): Novo tipo da categoria
        color (str, optional): Nova cor da categoria
        session: Sessão SQLAlchemy opcional

    Returns:
        Category: Objeto da categoria atualizada ou None se falhar
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        # Buscar a categoria
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            return None

        # Atualizar campos
        if name:
            category.name = name
        if category_type:
            category.type = category_type
        if color:
            category.color = color

        session.commit()
        return category
    except Exception as e:
        if session:
            session.rollback()
        print(f"Erro ao atualizar categoria: {e}")
        return None
    finally:
        if close_session:
            close_db_session(session)


def delete_category_from_db(category_id, session=None):
    """
    Exclui uma categoria do banco de dados

    Args:
        category_id (int): ID da categoria
        session: Sessão SQLAlchemy opcional

    Returns:
        bool: True se a exclusão for bem-sucedida, False caso contrário
    """
    close_session = False
    if not session:
        session = get_db_session()
        close_session = True

    try:
        # Buscar a categoria
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            return False

        # Excluir a categoria
        session.delete(category)
        session.commit()
        return True
    except Exception as e:
        if session:
            session.rollback()
        print(f"Erro ao excluir categoria: {e}")
        return False
    finally:
        if close_session:
            close_db_session(session)
