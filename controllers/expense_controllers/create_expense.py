"""
    Controlador para criar uma nova despesa
"""

import datetime
from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.models import Expense, Account

def create_expense(description, amount, date, category_id, account_id, recurrence_id=None):
    """
    Cria uma nova despesa

    Args:
        description (str): Descrição da despesa
        amount (float): Valor da despesa
        date (str): Data da despesa no formato "YYYY-MM-DD"
        category_id (int): ID da categoria
        account_id (int): ID da conta
        recurrence_id (int, optional): ID da recorrência, se for uma despesa recorrente

    Returns:
        dict: Dicionário com informações da despesa criada ou None se falhar
    """
    if not description or not date or amount <= 0:
        return None

    # Converter data de string para objeto date
    try:
        expense_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as e:
        print(f"Erro de tipo de dados ao converter data: {e}")
        return None

    session = get_db_session()

    try:
        # Criar nova despesa
        new_expense = Expense(
            description=description,
            amount=amount,
            date=expense_date,
            category_id=category_id,
            account_id=account_id,
            recurrence_id=recurrence_id
        )

        # Adicionar ao banco de dados
        session.add(new_expense)

        # Atualizar saldo da conta
        account = session.query(Account).filter_by(id=account_id).first()
        if account:
            account.balance -= amount

        session.commit()

        # Retornar dados da despesa criada
        return {
            'id': new_expense.id,
            'description': new_expense.description,
            'amount': new_expense.amount,
            'date': new_expense.date.strftime("%Y-%m-%d"),
            'category_id': new_expense.category_id,
            'account_id': new_expense.account_id,
            'recurrence_id': new_expense.recurrence_id
        }
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao criar despesa: {e}")
        return None
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao criar despesa: {e}")
        return None
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao criar despesa: {e}")
        return None
    finally:
        close_db_session(session)
