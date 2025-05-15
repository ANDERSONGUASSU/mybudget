"""
    Queries para operações com tabela de despesas
"""

from db.database import get_db_session, close_db_session
from sqlalchemy import text
from datetime import datetime

def get_expense_by_id(expense_id):
    """
    Obtém uma despesa específica pelo ID

    Args:
        expense_id (int): ID da despesa

    Returns:
        dict: Dados da despesa ou None se não encontrada
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT e.*, 
                   c.name as category_name, c.color as category_color,
                   a.name as account_name
            FROM expenses e
            LEFT JOIN categories c ON e.category_id = c.id
            LEFT JOIN accounts a ON e.account_id = a.id
            WHERE e.id = :expense_id
        """)

        result = session.execute(query, {"expense_id": expense_id}).fetchone()

        if result:
            # Converter para dicionário
            return dict(result)
        return None
    finally:
        close_db_session(session)

def get_expenses_by_period(start_date, end_date):
    """
    Obtém todas as despesas em um determinado período

    Args:
        start_date (str ou datetime): Data inicial
        end_date (str ou datetime): Data final

    Returns:
        list: Lista de dicionários com as despesas
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

        query = text("""
            SELECT e.*, 
                   c.name as category_name, c.color as category_color,
                   a.name as account_name
            FROM expenses e
            LEFT JOIN categories c ON e.category_id = c.id
            LEFT JOIN accounts a ON e.account_id = a.id
            WHERE e.date BETWEEN :start_date AND :end_date
            ORDER BY e.date DESC
        """)

        results = session.execute(query, {
            "start_date": start_date,
            "end_date": end_date
        }).fetchall()

        # Converter para lista de dicionários
        return [dict(row) for row in results]
    finally:
        close_db_session(session)

def get_monthly_expense_sum(year, month):
    """
    Obtém a soma total de despesas de um mês específico

    Args:
        year (int): Ano
        month (int): Mês (1-12)

    Returns:
        float: Soma das despesas no mês
    """
    session = get_db_session()
    try:
        query = text("""
            SELECT COALESCE(SUM(amount), 0) as total
            FROM expenses
            WHERE EXTRACT(YEAR FROM date) = :year
            AND EXTRACT(MONTH FROM date) = :month
        """)

        result = session.execute(query, {"year": year, "month": month}).scalar()
        return float(result) if result is not None else 0.0
    finally:
        close_db_session(session)

def get_expense_by_category(year, month=None):
    """
    Obtém a soma das despesas agrupadas por categoria

    Args:
        year (int): Ano
        month (int, optional): Mês (1-12). Se não for fornecido, retorna dados do ano todo

    Returns:
        list: Lista de dicionários com categoria e total
    """
    session = get_db_session()
    try:
        if month:
            query = text("""
                SELECT c.name as category_name, c.color, SUM(e.amount) as total
                FROM expenses e
                JOIN categories c ON e.category_id = c.id
                WHERE EXTRACT(YEAR FROM e.date) = :year
                AND EXTRACT(MONTH FROM e.date) = :month
                GROUP BY c.name, c.color
                ORDER BY total DESC
            """)
            params = {"year": year, "month": month}
        else:
            query = text("""
                SELECT c.name as category_name, c.color, SUM(e.amount) as total
                FROM expenses e
                JOIN categories c ON e.category_id = c.id
                WHERE EXTRACT(YEAR FROM e.date) = :year
                GROUP BY c.name, c.color
                ORDER BY total DESC
            """)
            params = {"year": year}

        results = session.execute(query, params).fetchall()
        return [dict(row) for row in results]
    finally:
        close_db_session(session)
