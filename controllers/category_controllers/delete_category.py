"""
    Controlador para excluir uma categoria
"""

from sqlalchemy.exc import SQLAlchemyError
from db.database import get_db_session, close_db_session
from db.models import Category, Income, Expense, CreditCardTransaction


def delete_category(category_id):
    """
    Exclui uma categoria

    Args:
        category_id (int): ID da categoria a ser excluída

    Returns:
        bool: True se a exclusão for bem-sucedida, False caso contrário
    """
    if not category_id:
        return False

    session = get_db_session()

    try:
        # Buscar a categoria no banco de dados
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            return False

        # Verificar se a categoria está sendo usada em transações
        income_count = session.query(Income).filter_by(category_id=category_id).count()
        expense_count = session.query(Expense).filter_by(category_id=category_id).count()
        credit_card_count = session.query(CreditCardTransaction).filter_by(category_id=category_id).count()

        # Se a categoria estiver em uso, não permitir exclusão
        if income_count > 0 or expense_count > 0 or credit_card_count > 0:
            print(f"Não é possível excluir a categoria {category.name} pois está em uso")
            return False

        # Excluir a categoria
        session.delete(category)
        session.commit()

        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao excluir categoria: {e}")
        return False
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao excluir categoria: {e}")
        return False
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao excluir categoria: {e}")
        return False
    finally:
        close_db_session(session)


def delete_category_with_reassign(category_id, new_category_id):
    """
    Exclui uma categoria e reatribui suas transações para outra categoria

    Args:
        category_id (int): ID da categoria a ser excluída
        new_category_id (int): ID da categoria para reatribuir as transações

    Returns:
        bool: True se a exclusão e reatribuição forem bem-sucedidas, False caso contrário
    """
    if not category_id or not new_category_id or category_id == new_category_id:
        return False

    session = get_db_session()

    try:
        # Buscar as categorias no banco de dados
        category = session.query(Category).filter_by(id=category_id).first()
        new_category = session.query(Category).filter_by(id=new_category_id).first()

        if not category or not new_category:
            return False

        # Reatribuir transações para a nova categoria
        session.query(Income).filter_by(category_id=category_id).update({"category_id": new_category_id})
        session.query(Expense).filter_by(category_id=category_id).update({"category_id": new_category_id})
        session.query(CreditCardTransaction).filter_by(category_id=category_id).update(
            {"category_id": new_category_id}
        )

        # Excluir a categoria antiga
        session.delete(category)
        session.commit()

        return True
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao excluir categoria e reatribuir transações: {e}")
        return False
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao excluir categoria e reatribuir transações: {e}")
        return False
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao excluir categoria e reatribuir transações: {e}")
        return False
    finally:
        close_db_session(session)
