"""
    Controlador para atualizar uma receita
"""

import datetime
from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.models import Account
from db.queries import get_income_by_id


def _parse_date(date_str):
    """Converte string de data para objeto date"""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        print(f"Erro de tipo de dados ao converter data: {e}")
        return None


def _update_account_balances(session, old_account_id, new_account_id, old_amount, new_amount):
    """Atualiza os saldos das contas envolvidas na transação"""
    # Retirar o valor antigo da conta antiga
    old_account = session.query(Account).filter_by(id=old_account_id).first()
    if not old_account:
        return False

    old_account.balance -= old_amount

    # Se a conta não mudou, apenas ajusta o saldo
    if new_account_id == old_account_id:
        old_account.balance += new_amount
        return True

    # Se a conta mudou, atualiza o saldo da nova conta
    new_account = session.query(Account).filter_by(id=new_account_id).first()
    if not new_account:
        return False

    new_account.balance += new_amount
    return True


def update_income(
    income_id, description=None, amount=None, date=None,
    category_id=None, account_id=None, recurrence_id=None
):
    """
    Atualiza uma receita existente

    Args:
        income_id (int): ID da receita a ser atualizada
        description (str, optional): Nova descrição da receita
        amount (float, optional): Novo valor da receita
        date (str, optional): Nova data da receita no formato "YYYY-MM-DD"
        category_id (int, optional): ID da nova categoria
        account_id (int, optional): ID da nova conta
        recurrence_id (int, optional): ID da nova recorrência

    Returns:
        dict: Dicionário com informações da receita atualizada ou None se falhar
    """
    session = get_db_session()

    try:
        # Obter a receita existente
        income = get_income_by_id(income_id, session)
        if not income:
            return None

        # Armazenar os valores antigos para ajustar o saldo da conta
        old_amount = income.amount
        old_account_id = income.account_id

        # Dicionário de campos atualizáveis
        updates = {
            'description': description,
            'amount': amount,
            'category_id': category_id,
            'account_id': account_id,
            'recurrence_id': recurrence_id
        }

        # Atualizar os campos da receita
        for field, value in updates.items():
            if value is not None:
                setattr(income, field, value)

        # Tratar a data separadamente por precisar de conversão
        if date is not None:
            income_date = _parse_date(date)
            if not income_date:
                return None
            income.date = income_date

        # Ajustar saldos das contas se necessário
        if amount is not None or account_id is not None:
            new_account_id = account_id if account_id is not None else old_account_id
            new_amount = amount if amount is not None else old_amount

            success = _update_account_balances(
                session, old_account_id, new_account_id, old_amount, new_amount
            )
            if not success:
                session.rollback()
                return None

        # Commitar as alterações
        session.commit()

        return {
            "id": income.id,
            "description": income.description,
            "amount": income.amount,
            "date": income.date.strftime("%Y-%m-%d"),
            "category_id": income.category_id,
            "account_id": income.account_id,
            "recurrence_id": income.recurrence_id
        }
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro de banco de dados ao atualizar a receita: {e}")
        return None
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao atualizar a receita: {e}")
        return None
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao atualizar a receita: {e}")
        return None
    finally:
        close_db_session(session)
