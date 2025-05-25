# src/controllers/recurrence_controllers/create_recurrence.py
"""
    Cria uma nova recorrência.
"""
import datetime
from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.models import Recurrence

def create_recurrence(recurrence_id, recurrence_type, frequency, start_date):
    """
    Cria uma nova recorrência.

    Args:
        recurrence_id (int): ID da recorrência.
        recurrence_type (str): Tipo da recorrência.
        frequency (int): Frequência da recorrência.
        start_date (datetime): Data de início da recorrência.

    Returns:
        dict: Dicionário com informações da recorrência criada ou None se falhar.
    """
    if not recurrence_id or not recurrence_type or not frequency or not start_date:
        print("Erro: Parâmetros inválidos")
        return None


    # Converter start_date para objeto date de forma robusta
    recurrence_start_date = None
    if isinstance(start_date, datetime.date) and not isinstance(start_date, datetime.datetime):
        recurrence_start_date = start_date
    elif isinstance(start_date, datetime.datetime):
        recurrence_start_date = start_date.date()
    elif isinstance(start_date, str):
        try:
            recurrence_start_date = datetime.datetime.fromisoformat(start_date).date()
        except ValueError:
            try:
                recurrence_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            except ValueError as e:
                print(f"Erro de tipo de dados ao converter data: {e}")
                return None
    else:
        print(f"Tipo de dado de data não suportado: {type(start_date)}")
        return None


    session = get_db_session()
    try:
        new_recurrence = Recurrence(
            id=recurrence_id,
            type=type,
            frequency=frequency,
            start_date=recurrence_start_date
        )
        session.add(new_recurrence)
        session.commit()
        return {
            'id': new_recurrence.id,
            'type': new_recurrence.type,
            'frequency': new_recurrence.frequency,
            'start_date': new_recurrence.start_date.strftime("%Y-%m-%d")
        }
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao criar recorrência: {e}")
        return None
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao criar recorrência: {e}")
        return None
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao criar recorrência: {e}")
        return None
    finally:
        close_db_session(session)
