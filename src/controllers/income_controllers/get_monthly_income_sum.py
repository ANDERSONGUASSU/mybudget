"""
    Módulo para obter a soma de receitas em um mês
"""

from db.database import get_db_session, close_db_session
from db.models import Income
from sqlalchemy import extract, func

def get_monthly_income_sum(year, month):
    """
    Obtém a soma de receitas em um determinado mês

    Args:
        year (int): Ano
        month (int): Mês (1-12)

    Returns:
        float: Soma das receitas no mês
    """
    session = get_db_session()
    try:
        # Obter soma das receitas no mês
        result = session.query(func.sum(Income.amount)).filter(
            extract('year', Income.date) == year,
            extract('month', Income.date) == month
        ).scalar()

        return float(result) if result else 0.0
    except Exception as e:
        print(f"Erro ao obter soma de receitas: {e}")
        return 0.0
    finally:
        close_db_session(session)
