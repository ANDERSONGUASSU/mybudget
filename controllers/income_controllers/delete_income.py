"""
    Controlador para deletar receitas
"""
from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.models import Account
from db.queries.income_queries import get_income_by_id


def delete_income(income_id):
    """
    Deleta uma receita pelo ID

    Args:
        income_id (int): ID da receita a ser deletada

    Returns:
        bool: True se a receita foi deletada com sucesso, False caso contrário
    """
    session = get_db_session()

    try:
        # Busca a receita pelo ID
        income = get_income_by_id(income_id, session)

        if not income:
            return False

        # Recuperar informações para ajuste de saldo
        amount = income.amount
        account_id = income.account_id

        # Ajustar saldo da conta
        account = session.query(Account).filter_by(id=account_id).first()
        if account:
            account.balance -= amount

        # Deleta a receita
        session.delete(income)
        session.commit()

        return True

    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao deletar receita: {e}")
        return False

    finally:
        close_db_session(session)
