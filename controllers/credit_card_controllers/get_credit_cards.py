"""
    Controlador para obter cartões de crédito
"""

from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.queries.credit_card_queries import get_all_credit_cards, get_credit_card_by_id


def get_credit_cards():
    """
    Obtém todos os cartões de crédito

    Returns:
        list: Lista de dicionários com informações dos cartões
    """
    session = get_db_session()

    try:
        # Obter todos os cartões
        cards = get_all_credit_cards(session)

        # Converter para dicionários
        cards_dict = [
            {
                'id': card.id,
                'name': card.name,
                'limit': card.limit,
                'closing_day': card.closing_day,
                'due_day': card.due_day
            }
            for card in cards
        ]

        return cards_dict
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao obter cartões de crédito: {e}")
        return []
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao obter cartões de crédito: {e}")
        return []
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao obter cartões de crédito: {e}")
        return []
    finally:
        close_db_session(session)


def get_credit_card(card_id):
    """
    Obtém um cartão de crédito pelo ID

    Args:
        card_id (int): ID do cartão

    Returns:
        dict: Dicionário com informações do cartão ou None se não encontrado
    """
    session = get_db_session()

    try:
        # Obter o cartão pelo ID
        card = get_credit_card_by_id(card_id, session)

        if not card:
            return None

        # Converter para dicionário
        card_dict = {
            'id': card.id,
            'name': card.name,
            'limit': card.limit,
            'closing_day': card.closing_day,
            'due_day': card.due_day
        }

        return card_dict
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao obter cartão de crédito: {e}")
        return None
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao obter cartão de crédito: {e}")
        return None
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao obter cartão de crédito: {e}")
        return None
    finally:
        close_db_session(session)
