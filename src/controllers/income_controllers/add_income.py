"""
    Módulo para adicionar receitas ao sistema
"""

from datetime import datetime
from db.database import get_db_session, close_db_session
from db.models import Income, Recurrence
from src.controllers.account_controllers import update_account_balance

def add_income(description, amount, date, category_id, account_id, recurrence_type="unica", notes=None):
    """
    Adiciona uma nova receita ao banco de dados

    Args:
        description (str): Descrição da receita
        amount (float): Valor da receita
        date (str ou datetime): Data da receita (formato YYYY-MM-DD se string)
        category_id (int): ID da categoria
        account_id (int): ID da conta
        recurrence_type (str, optional): Tipo de recorrência ('unica', 'diaria', 'semanal', etc.)
        notes (str, optional): Observações

    Returns:
        int: ID da receita criada ou None em caso de erro
    """
    session = get_db_session()
    try:
        # Converter data para objeto datetime se for string
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d").date()
        elif isinstance(date, datetime):
            date = date.date()

        # Criar recorrência se não for única
        recurrence_id = None
        if recurrence_type != "unica":
            new_recurrence = Recurrence(
                type=recurrence_type,
                start_date=date,
                frequency=1  # Padrão é frequência 1 (a cada semana, a cada mês, etc.)
            )
            session.add(new_recurrence)
            session.flush()  # Para obter o ID da recorrência
            recurrence_id = new_recurrence.id

        # Criar nova receita
        new_income = Income(
            description=description,
            amount=amount,
            date=date,
            category_id=category_id,
            account_id=account_id,
            recurrence_id=recurrence_id,
            notes=notes
        )

        # Adicionar ao banco e obter ID
        session.add(new_income)
        session.commit()
        session.refresh(new_income)

        # Atualizar saldo da conta
        update_account_balance(account_id, amount, is_credit=True)

        return new_income.id
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar receita: {e}")
        return None
    finally:
        close_db_session(session)
