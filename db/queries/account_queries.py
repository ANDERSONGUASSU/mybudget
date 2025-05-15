"""
    Queries para operações com tabela de contas
"""

from db.database import get_db_session, close_db_session
from sqlalchemy import text

def get_all_accounts(active_only=True):
    """
    Obtém todas as contas

    Args:
        active_only (bool, optional): Filtrar apenas contas ativas

    Returns:
        list: Lista de dicionários com as contas
    """
    session = get_db_session()
    try:
        base_query = """
            SELECT id, name, type, balance, color, active
            FROM accounts
        """

        params = {}

        if active_only:
            base_query += " WHERE active = :active"
            params["active"] = True

        base_query += " ORDER BY name"

        query = text(base_query)
        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)

def get_dropdown_accounts(active_only=True):
    """
    Obtém contas formatadas para componentes dropdown

    Args:
        active_only (bool, optional): Filtrar apenas contas ativas

    Returns:
        list: Lista de dicionários formatados para dropdowns
    """
    session = get_db_session()
    try:
        base_query = """
            SELECT id, name, type, balance, color, active
            FROM accounts
        """

        params = {}

        if active_only:
            base_query += " WHERE active = :active"
            params["active"] = True

        base_query += " ORDER BY name"

        query = text(base_query)
        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários formatados para componentes dropdown
        dropdown_options = [
            {
                "id": row["id"],
                "label": f"{row['name']} (R$ {row['balance']:.2f})",
                "value": row["id"],
                "color": row["color"]
            }
            for row in results
        ]

        return dropdown_options
    finally:
        close_db_session(session)

def get_account_by_id(account_id):
    """
    Obtém uma conta pelo ID

    Args:
        account_id (int): ID da conta

    Returns:
        dict: Dados da conta ou None se não encontrada
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT id, name, type, balance, color, active
            FROM accounts
            WHERE id = :account_id
        """)

        result = session.execute(query, {"account_id": account_id}).fetchone()

        if result:
            # Converter para dicionário
            return dict(result)
        return None
    finally:
        close_db_session(session)

def get_account_usage_count(account_id):
    """
    Obtém o número de vezes que uma conta foi usada em transações

    Args:
        account_id (int): ID da conta

    Returns:
        int: Número de usos da conta
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT
                (SELECT COUNT(*) FROM incomes WHERE account_id = :account_id) +
                (SELECT COUNT(*) FROM expenses WHERE account_id = :account_id)
                AS usage_count
        """)

        result = session.execute(query, {"account_id": account_id}).scalar()
        return int(result) if result is not None else 0
    finally:
        close_db_session(session)

def get_total_balance():
    """
    Obtém o saldo total de todas as contas ativas

    Returns:
        float: Soma dos saldos de todas as contas ativas
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT COALESCE(SUM(balance), 0) as total_balance
            FROM accounts
            WHERE active = :active
        """)

        result = session.execute(query, {"active": True}).scalar()
        return float(result) if result is not None else 0.0
    finally:
        close_db_session(session)
