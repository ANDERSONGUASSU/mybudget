"""
    Módulo para adicionar categorias
"""

from db.database import get_db_session, close_db_session
from db.models import Category

def add_category(name, category_type, color="#4CAF50"):
    """
    Adiciona uma nova categoria ao banco de dados

    Args:
        name (str): Nome da categoria
        category_type (str): Tipo da categoria ('income', 'expense', 'credit')
        color (str, optional): Cor em hexadecimal. Padrão é verde (#4CAF50)

    Returns:
        int: ID da categoria criada ou None em caso de erro
    """
    session = get_db_session()
    try:
        # Verificar se já existe uma categoria com o mesmo nome e tipo
        existing = session.query(Category).filter(
            Category.name == name,
            Category.type == category_type
        ).first()

        if existing:
            # Se já existe, apenas retorna o ID
            return existing.id

        # Criar nova categoria
        new_category = Category(
            name=name,
            type=category_type,
            color=color,
            active=True
        )

        # Adicionar ao banco e obter ID
        session.add(new_category)
        session.commit()
        session.refresh(new_category)

        return new_category.id
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar categoria: {e}")
        return None
    finally:
        close_db_session(session)
