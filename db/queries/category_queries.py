"""
    Queries para operações com tabela de categorias
"""

from db.database import get_db_session, close_db_session
from sqlalchemy import text

def get_all_categories(active_only=True):
    """
    Obtém todas as categorias

    Args:
        active_only (bool, optional): Filtrar apenas categorias ativas

    Returns:
        list: Lista de dicionários com as categorias
    """
    session = get_db_session()
    try:
        base_query = """
            SELECT id, name, type, color, active
            FROM categories
        """

        params = {}

        if active_only:
            base_query += " WHERE active = :active"
            params["active"] = True

        base_query += " ORDER BY type, name"

        query = text(base_query)
        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)

def get_categories_by_type(category_type, active_only=True):
    """
    Obtém categorias de um determinado tipo

    Args:
        category_type (str): Tipo da categoria ('income', 'expense', 'credit')
        active_only (bool, optional): Filtrar apenas categorias ativas

    Returns:
        list: Lista de dicionários com as categorias
    """
    session = get_db_session()
    try:
        base_query = """
            SELECT id, name, type, color, active
            FROM categories
            WHERE type = :type
        """

        params = {"type": category_type}

        if active_only:
            base_query += " AND active = :active"
            params["active"] = True

        base_query += " ORDER BY name"

        query = text(base_query)
        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários formatados para componentes dropdown
        dropdown_options = [
            {
                "id": row["id"],
                "label": row["name"],
                "value": row["id"],
                "color": row["color"]
            }
            for row in results
        ]

        return dropdown_options
    finally:
        close_db_session(session)

def get_category_by_id(category_id):
    """
    Obtém uma categoria pelo ID

    Args:
        category_id (int): ID da categoria

    Returns:
        dict: Dados da categoria ou None se não encontrada
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT id, name, type, color, active
            FROM categories
            WHERE id = :category_id
        """)

        result = session.execute(query, {"category_id": category_id}).fetchone()

        if result:
            # Converter para dicionário
            return dict(result)
        return None
    finally:
        close_db_session(session)

def get_category_usage_count(category_id):
    """
    Obtém o número de vezes que uma categoria foi usada em transações

    Args:
        category_id (int): ID da categoria

    Returns:
        int: Número de usos da categoria
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT
                (SELECT COUNT(*) FROM incomes WHERE category_id = :category_id) +
                (SELECT COUNT(*) FROM expenses WHERE category_id = :category_id) +
                (SELECT COUNT(*) FROM credit_card_transactions WHERE category_id = :category_id)
                AS usage_count
        """)

        result = session.execute(query, {"category_id": category_id}).scalar()
        return int(result) if result is not None else 0
    finally:
        close_db_session(session)
