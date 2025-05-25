# src/controllers/income_controllers/create_income.py
"""
    Controlador para criar uma nova receita
"""

import datetime
from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.models import Income, Account


def create_income(description, amount, date, category_id, account_id, recurrence_id=None):
    """
    Cria uma nova receita

    Args:
        description (str): Descrição da receita
        amount (float): Valor da receita
        date (str): Data da receita no formato "YYYY-MM-DD"
        category_id (int): ID da categoria
        account_id (int): ID da conta
        recurrence_id (int, optional): ID da recorrência, se for uma receita recorrente

    Returns:
        dict: Dicionário com informações da receita criada ou None se falhar
    """
    if not description or not date or amount <= 0:
        return None

    # Converter data para objeto date de forma robusta
    income_date = None
    if isinstance(date, datetime.date) and not isinstance(date, datetime.datetime):
        income_date = date
    elif isinstance(date, datetime.datetime):
        income_date = date.date()
    elif isinstance(date, str):
        try:
            # Tenta ISO completo
            income_date = datetime.datetime.fromisoformat(date).date()
        except ValueError:
            try:
                income_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            except ValueError as e:
                print(f"Erro de tipo de dados ao converter data: {e}")
                return None
    else:
        print(f"Tipo de dado de data não suportado: {type(date)}")
        return None

    session = get_db_session()

    try:
        # Criar nova receita
        new_income = Income(
            description=description,
            amount=amount,
            date=income_date,
            category_id=category_id,
            account_id=account_id,
            recurrence_id=recurrence_id
        )

        # Adicionar ao banco de dados
        session.add(new_income)

        # Atualizar saldo da conta
        account = session.query(Account).filter_by(id=account_id).first()
        if account:
            account.balance += amount

        session.commit()

        # Retornar dados da receita criada
        return {
            'id': new_income.id,
            'description': new_income.description,
            'amount': new_income.amount,
            'date': new_income.date.strftime("%Y-%m-%d"),
            'category_id': new_income.category_id,
            'account_id': new_income.account_id,
            'recurrence_id': new_income.recurrence_id
        }
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao criar receita: {e}")
        return None
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao criar receita: {e}")
        return None
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao criar receita: {e}")
        return None
    finally:
        close_db_session(session)
