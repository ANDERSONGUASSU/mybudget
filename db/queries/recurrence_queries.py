"""
    Queries para operações com tabela de recorrências
"""

from db.database import get_db_session, close_db_session
from sqlalchemy import text
from datetime import datetime

def get_active_recurrences():
    """
    Obtém todas as recorrências ativas (que ainda não terminaram)

    Returns:
        list: Lista de dicionários com as recorrências
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT r.*, 
                   i.description as income_description, i.amount as income_amount, i.category_id as income_category_id, i.account_id as income_account_id,
                   e.description as expense_description, e.amount as expense_amount, e.category_id as expense_category_id, e.account_id as expense_account_id,
                   c.description as credit_card_description, c.amount as credit_card_amount, c.category_id as credit_card_category_id, c.credit_card_id
            FROM recurrences r
            LEFT JOIN incomes i ON r.id = i.recurrence_id
            LEFT JOIN expenses e ON r.id = e.recurrence_id
            LEFT JOIN credit_card_transactions c ON r.id = c.recurrence_id
            WHERE (r.end_date IS NULL OR r.end_date >= CURRENT_DATE)
            ORDER BY r.next_date
        """)

        results = session.execute(query).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)

def get_recurrence_by_id(recurrence_id):
    """
    Obtém uma recorrência pelo ID

    Args:
        recurrence_id (int): ID da recorrência

    Returns:
        dict: Dados da recorrência ou None se não encontrada
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT r.*, 
                   i.description as income_description, i.amount as income_amount, i.category_id as income_category_id, i.account_id as income_account_id,
                   e.description as expense_description, e.amount as expense_amount, e.category_id as expense_category_id, e.account_id as expense_account_id,
                   c.description as credit_card_description, c.amount as credit_card_amount, c.category_id as credit_card_category_id, c.credit_card_id
            FROM recurrences r
            LEFT JOIN incomes i ON r.id = i.recurrence_id
            LEFT JOIN expenses e ON r.id = e.recurrence_id
            LEFT JOIN credit_card_transactions c ON r.id = c.recurrence_id
            WHERE r.id = :recurrence_id
        """)

        result = session.execute(query, {"recurrence_id": recurrence_id}).fetchone()

        if result:
            # Converter para dicionário
            return dict(result)
        return None
    finally:
        close_db_session(session)

def get_recurrences_due_today():
    """
    Obtém todas as recorrências que vencem hoje

    Returns:
        list: Lista de dicionários com as recorrências
    """
    session = get_db_session()
    try:
        today = datetime.now().date()

        query = text("""
            SELECT r.*, 
                   i.description as income_description, i.amount as income_amount, i.category_id as income_category_id, i.account_id as income_account_id,
                   e.description as expense_description, e.amount as expense_amount, e.category_id as expense_category_id, e.account_id as expense_account_id,
                   c.description as credit_card_description, c.amount as credit_card_amount, c.category_id as credit_card_category_id, c.credit_card_id
            FROM recurrences r
            LEFT JOIN incomes i ON r.id = i.recurrence_id
            LEFT JOIN expenses e ON r.id = e.recurrence_id
            LEFT JOIN credit_card_transactions c ON r.id = c.recurrence_id
            WHERE r.next_date = :today
            AND (r.end_date IS NULL OR r.end_date >= :today)
            ORDER BY r.type
        """)

        results = session.execute(query, {"today": today}).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)

def get_upcoming_recurrences(days=7):
    """
    Obtém recorrências que vencem nos próximos dias

    Args:
        days (int, optional): Número de dias para olhar à frente

    Returns:
        list: Lista de dicionários com as recorrências
    """
    session = get_db_session()
    try:
        today = datetime.now().date()

        query = text("""
            SELECT r.*, 
                   i.description as income_description, i.amount as income_amount, i.category_id as income_category_id, i.account_id as income_account_id,
                   e.description as expense_description, e.amount as expense_amount, e.category_id as expense_category_id, e.account_id as expense_account_id,
                   c.description as credit_card_description, c.amount as credit_card_amount, c.category_id as credit_card_category_id, c.credit_card_id
            FROM recurrences r
            LEFT JOIN incomes i ON r.id = i.recurrence_id
            LEFT JOIN expenses e ON r.id = e.recurrence_id
            LEFT JOIN credit_card_transactions c ON r.id = c.recurrence_id
            WHERE r.next_date BETWEEN :today AND DATE(:today, '+' || :days || ' days')
            AND (r.end_date IS NULL OR r.end_date >= r.next_date)
            ORDER BY r.next_date
        """)

        results = session.execute(query, {"today": today, "days": days}).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)
