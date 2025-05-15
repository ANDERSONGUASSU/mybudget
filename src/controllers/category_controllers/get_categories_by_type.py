"""
    Módulo para obter categorias por tipo
"""

from db.database import get_db_session, close_db_session
from db.models import Category

def get_categories_by_type(category_type, active_only=True):
    """
    Obtém categorias de um determinado tipo

    Args:
        category_type (str): Tipo da categoria ('income', 'expense', 'credit')
        active_only (bool, optional): Retornar apenas categorias ativas

    Returns:
        list: Lista de dicionários com id, name e color das categorias
    """
    session = get_db_session()
    try:
        query = session.query(Category).filter(Category.type == category_type)

        if active_only:
            query = query.filter(Category.active)

        categories = query.order_by(Category.name).all()

        # Converter para formato mais simples para o frontend
        result = [
            {
                "id": category.id,
                "label": category.name,
                "value": category.id,
                "color": category.color
            }
            for category in categories
        ]

        return result
    except Exception as e:
        print(f"Erro ao obter categorias: {e}")
        return []
    finally:
        close_db_session(session)
