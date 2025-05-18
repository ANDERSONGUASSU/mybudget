"""
    Controlador para atualizar uma categoria existente
"""

from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.models import Category


def update_category(category_id, name=None, category_type=None, color=None):
    """
    Atualiza uma categoria existente

    Args:
        category_id (int): ID da categoria a ser atualizada
        name (str, optional): Novo nome da categoria
        category_type (str, optional): Novo tipo da categoria ('income', 'expense' ou 'credit')
        color (str, optional): Nova cor da categoria em formato hexadecimal

    Returns:
        dict: Dicionário com informações da categoria atualizada ou None se falhar
    """
    if not category_id:
        return None

    # Verificar tipo válido, se fornecido
    valid_types = ['income', 'expense', 'credit']
    if category_type and category_type not in valid_types:
        return None

    session = get_db_session()

    try:
        # Buscar a categoria no banco de dados
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            return None

        # Atualizar campos se fornecidos
        if name:
            category.name = name
        if category_type:
            category.type = category_type
        if color:
            category.color = color

        # Salvar alterações
        session.commit()

        # Retornar dados da categoria atualizada
        return {
            'id': category.id,
            'name': category.name,
            'type': category.type,
            'color': category.color
        }
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao atualizar categoria: {e}")
        return None
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao atualizar categoria: {e}")
        return None
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao atualizar categoria: {e}")
        return None
    finally:
        close_db_session(session)
