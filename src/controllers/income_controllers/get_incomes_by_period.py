"""
    Módulo para listar receitas por período
"""

from datetime import datetime
from db.database import get_db_session, close_db_session
from db.models import Income

def get_incomes_by_period(start_date, end_date):
    """
    Obtém todas as receitas em um determinado período

    Args:
        start_date (str ou datetime): Data inicial (formato YYYY-MM-DD se string)
        end_date (str ou datetime): Data final (formato YYYY-MM-DD se string)

    Returns:
        list: Lista de dicionários com informações das receitas
    """
    session = get_db_session()
    try:
        # Converter datas para objetos datetime se forem strings
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        elif isinstance(start_date, datetime):
            start_date = start_date.date()

        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        elif isinstance(end_date, datetime):
            end_date = end_date.date()

        # Query para obter receitas no período
        incomes = session.query(Income).filter(
            Income.date >= start_date,
            Income.date <= end_date
        ).order_by(Income.date.desc()).all()

        # Converter para formato mais simples para o frontend
        result = []
        for income in incomes:
            # Obter nomes de categoria e conta
            category_name = income.category.name if income.category else "Sem categoria"
            account_name = income.account.name if income.account else "Sem conta"

            # Adicionar ao resultado
            result.append({
                "id": income.id,
                "description": income.description,
                "amount": income.amount,
                "date": income.date.strftime("%Y-%m-%d"),
                "category_id": income.category_id,
                "category_name": category_name,
                "account_id": income.account_id,
                "account_name": account_name,
                "is_recurring": income.recurrence_id is not None,
                "notes": income.notes
            })

        return result
    except Exception as e:
        print(f"Erro ao obter receitas: {e}")
        return []
    finally:
        close_db_session(session)
