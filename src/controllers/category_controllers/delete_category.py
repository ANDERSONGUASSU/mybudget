"""
    Módulo para remover categorias (soft delete)
"""

from db.database import get_db_session, close_db_session
from db.models import Category

def delete_category(category_id):
    """
    Remove uma categoria (soft delete - apenas marca como inativa)

    Args:
        category_id (int): ID da categoria

    Returns:
        bool: True se removida com sucesso, False caso contrário
    """
    session = get_db_session()
    try:
        # Ao invés de remover, apenas desativamos a categoria
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            return False

        category.active = False
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao remover categoria: {e}")
        return False
    finally:
        close_db_session(session)
