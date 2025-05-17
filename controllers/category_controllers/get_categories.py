"""
    Controlador para obter categorias
"""

from db.queries.category_queries import get_all_categories, get_category_by_id, get_categories_by_type


def get_categories():
    """
    Obtém todas as categorias

    Returns:
        list: Lista de dicionários com informações das categorias
    """
    categories = get_all_categories()

    # Transformar objetos Category em dicionários
    categories_dict = [
        {
            'id': category.id,
            'name': category.name,
            'type': category.type if hasattr(category, 'type') else None,
            'color': category.color
        }
        for category in categories
    ]

    return categories_dict


def get_category(category_id):
    """
    Obtém uma categoria específica

    Args:
        category_id (int): ID da categoria

    Returns:
        dict: Dicionário com informações da categoria ou None se não encontrada
    """
    category = get_category_by_id(category_id)

    if not category:
        return None

    # Transformar objeto Category em dicionário
    category_dict = {
        'id': category.id,
        'name': category.name,
        'type': category.type if hasattr(category, 'type') else None,
        'color': category.color
    }

    return category_dict


def get_categories_for_type(category_type):
    """
    Obtém categorias por tipo

    Args:
        category_type (str): Tipo da categoria ('income', 'expense' ou 'credit')

    Returns:
        list: Lista de dicionários com informações das categorias
    """
    categories = get_categories_by_type(category_type)

    # Transformar objetos Category em dicionários
    categories_dict = [
        {
            'id': category.id,
            'name': category.name,
            'type': category.type,
            'color': category.color
        }
        for category in categories
    ]

    return categories_dict
