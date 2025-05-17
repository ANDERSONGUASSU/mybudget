"""
    Controlador para criar uma nova categoria
"""

from db.database import get_db_session, close_db_session
from db.models import Category


def create_category(name, category_type, color="#4CAF50"):
    """
    Cria uma nova categoria

    Args:
        name (str): Nome da categoria
        category_type (str): Tipo da categoria ('income', 'expense' ou 'credit')
        color (str, optional): Cor da categoria em formato hexadecimal

    Returns:
        dict: Dicionário com informações da categoria criada ou None se falhar
    """
    if not name or not category_type:
        return None

    # Verificar tipo válido
    valid_types = ['income', 'expense', 'credit']
    if category_type not in valid_types:
        return None

    session = get_db_session()

    try:
        # Criar nova categoria
        new_category = Category(name=name, type=category_type, color=color)

        # Adicionar ao banco de dados
        session.add(new_category)
        session.commit()

        # Retornar dados da categoria criada
        return {
            'id': new_category.id,
            'name': new_category.name,
            'type': new_category.type,
            'color': new_category.color
        }
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar categoria: {e}")
        return None
    finally:
        close_db_session(session)
