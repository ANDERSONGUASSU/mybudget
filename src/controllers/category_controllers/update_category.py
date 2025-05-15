"""
    Módulo para atualizar categorias
"""

from db.database import get_db_session, close_db_session
from db.models import Category

def update_category(category_id, name=None, color=None, active=None):
    """
    Atualiza uma categoria existente

    Args:
        category_id (int): ID da categoria
        name (str, optional): Novo nome
        color (str, optional): Nova cor
        active (bool, optional): Status de ativo/inativo

    Returns:
        bool: True se atualizado com sucesso, False caso contrário
    """
    session = get_db_session()
    try:
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            return False

        # Atualizar campos se fornecidos
        if name is not None:
            category.name = name
        if color is not None:
            category.color = color
        if active is not None:
            category.active = active

        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar categoria: {e}")
        return False
    finally:
        close_db_session(session)
