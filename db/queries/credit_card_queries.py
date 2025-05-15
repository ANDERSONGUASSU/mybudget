"""
    Queries para operações com tabela de transações de cartão de crédito
"""

from db.database import get_db_session, close_db_session
from sqlalchemy import text
from datetime import datetime

def get_credit_card_transaction_by_id(transaction_id):
    """
    Obtém uma transação de cartão de crédito pelo ID

    Args:
        transaction_id (int): ID da transação

    Returns:
        dict: Dados da transação ou None se não encontrada
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT t.*, 
                   c.name as category_name, c.color as category_color,
                   cc.name as credit_card_name
            FROM credit_card_transactions t
            LEFT JOIN categories c ON t.category_id = c.id
            LEFT JOIN credit_cards cc ON t.credit_card_id = cc.id
            WHERE t.id = :transaction_id
        """)

        result = session.execute(query, {"transaction_id": transaction_id}).fetchone()

        if result:
            # Converter para dicionário
            return dict(result)
        return None
    finally:
        close_db_session(session)

def get_credit_card_transactions_by_period(start_date, end_date, credit_card_id=None):
    """
    Obtém todas as transações de cartão de crédito em um determinado período

    Args:
        start_date (str ou datetime): Data inicial
        end_date (str ou datetime): Data final
        credit_card_id (int, optional): ID do cartão para filtrar

    Returns:
        list: Lista de dicionários com as transações
    """
    session = get_db_session()
    try:
        # Converter datas se necessário
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        elif isinstance(start_date, datetime):
            start_date = start_date.date()

        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        elif isinstance(end_date, datetime):
            end_date = end_date.date()

        params = {
            "start_date": start_date,
            "end_date": end_date
        }

        base_query = """
            SELECT t.*, 
                   c.name as category_name, c.color as category_color,
                   cc.name as credit_card_name
            FROM credit_card_transactions t
            LEFT JOIN categories c ON t.category_id = c.id
            LEFT JOIN credit_cards cc ON t.credit_card_id = cc.id
            WHERE t.date BETWEEN :start_date AND :end_date
        """

        if credit_card_id:
            base_query += " AND t.credit_card_id = :credit_card_id"
            params["credit_card_id"] = credit_card_id

        base_query += " ORDER BY t.date DESC"

        query = text(base_query)
        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)

def get_monthly_credit_card_sum(year, month, credit_card_id=None):
    """
    Obtém a soma total de transações de cartão de crédito de um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)
        credit_card_id (int, optional): ID do cartão para filtrar

    Returns:
        float: Soma das transações no mês
    """
    session = get_db_session()
    try:
        params = {"year": year, "month": month}

        base_query = """
            SELECT COALESCE(SUM(amount), 0) as total
            FROM credit_card_transactions
            WHERE EXTRACT(YEAR FROM date) = :year
            AND EXTRACT(MONTH FROM date) = :month
        """

        if credit_card_id:
            base_query += " AND credit_card_id = :credit_card_id"
            params["credit_card_id"] = credit_card_id

        query = text(base_query)
        result = session.execute(query, params).scalar()
        return float(result) if result is not None else 0.0
    finally:
        close_db_session(session)

def get_credit_card_transaction_by_category(year, month=None, credit_card_id=None):
    """
    Obtém a soma das transações de cartão de crédito agrupadas por categoria

    Args:
        year (int): Ano
        month (int, optional): Mês (1-12). Se não for fornecido, retorna dados do ano todo
        credit_card_id (int, optional): ID do cartão para filtrar

    Returns:
        list: Lista de dicionários com categoria e total
    """
    session = get_db_session()
    try:
        params = {"year": year}

        base_query = """
            SELECT c.name as category_name, c.color, SUM(t.amount) as total
            FROM credit_card_transactions t
            JOIN categories c ON t.category_id = c.id
            WHERE EXTRACT(YEAR FROM t.date) = :year
        """

        if month:
            base_query += " AND EXTRACT(MONTH FROM t.date) = :month"
            params["month"] = month

        if credit_card_id:
            base_query += " AND t.credit_card_id = :credit_card_id"
            params["credit_card_id"] = credit_card_id

        base_query += " GROUP BY c.name, c.color ORDER BY total DESC"

        query = text(base_query)
        results = session.execute(query, params).fetchall()
        return [dict(row) for row in results]
    finally:
        close_db_session(session)

def get_pending_credit_card_installments(credit_card_id=None):
    """
    Obtém as parcelas pendentes de cartão de crédito

    Args:
        credit_card_id (int, optional): ID do cartão para filtrar

    Returns:
        list: Lista de dicionários com as parcelas pendentes
    """
    session = get_db_session()
    try:
        params = {}

        base_query = """
            SELECT t.*, 
                   c.name as category_name, c.color as category_color,
                   cc.name as credit_card_name,
                   (t.installments - t.current_installment) as remaining_installments
            FROM credit_card_transactions t
            LEFT JOIN categories c ON t.category_id = c.id
            LEFT JOIN credit_cards cc ON t.credit_card_id = cc.id
            WHERE t.installments > 1 AND t.current_installment < t.installments
        """

        if credit_card_id:
            base_query += " AND t.credit_card_id = :credit_card_id"
            params["credit_card_id"] = credit_card_id

        base_query += " ORDER BY t.date DESC"

        query = text(base_query)
        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)
