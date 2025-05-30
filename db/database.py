"""
    Database module
"""

import os
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from db.models.base import Base
from db.models import Category, Account, CreditCard

# Define o caminho para o arquivo do banco de dados
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite')

# Cria o engine do SQLAlchemy com o caminho correto
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
Session = sessionmaker(bind=engine)

def get_db_session():
    """
        Get a database session
    """
    session = Session()
    try:
        return session
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao obter sessão do banco de dados: {e}")
        raise e


def close_db_session(session):
    """
        Close a database session
    """
    if session:
        session.close()

def init_db():
    """
        Initialize the database with tables and default data
    """
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)

    # Cria uma sessão
    session = get_db_session()

    try:
        # Verifica se já temos categorias
        if session.query(Category).count() == 0:
            # Adiciona categorias padrão
            categories = [
                Category(name="Salário", type="income", color="#4CAF50"),
                Category(name="Freelance", type="income", color="#8BC34A"),
                Category(name="Investimentos", type="income", color="#009688"),
                Category(name="Alimentação", type="expense", color="#F44336"),
                Category(name="Transporte", type="expense", color="#FF9800"),
                Category(name="Moradia", type="expense", color="#795548"),
                Category(name="Lazer", type="expense", color="#9C27B0"),
                Category(name="Saúde", type="expense", color="#E91E63"),
                Category(name="Educação", type="expense", color="#3F51B5"),
                Category(name="Compras", type="expense", color="#2196F3"),
                Category(name="Serviços", type="expense", color="#00BCD4"),
            ]
            session.add_all(categories)

        # Verifica se já temos contas
        if session.query(Account).count() == 0:
            # Adiciona contas padrão
            accounts = [
                Account(name="Conta Corrente", type_account="Corrente", balance=0.0),
                Account(name="Poupança", type_account="Poupança", balance=0.0),
            ]
            session.add_all(accounts)

        # Verifica se já temos cartões de crédito
        if session.query(CreditCard).count() == 0:
            # Adiciona cartões de crédito padrão
            credit_cards = [
                CreditCard(
                    name="Nubank",
                    limit=5000.0,
                    closing_day=26,
                    due_day=10
                ),
                CreditCard(
                    name="Itaú",
                    limit=3000.0,
                    closing_day=26,
                    due_day=10
                ),
            ]
            session.add_all(credit_cards)

        # Commit das alterações
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao inicializar o banco de dados: {e}")
        raise e
    except ValueError as e:
        session.rollback()
        print(f"Erro de tipo de dados ao inicializar o banco de dados: {e}")
        raise e
    except AttributeError as e:
        session.rollback()
        print(f"Erro de atributo ao inicializar o banco de dados: {e}")
        raise e
    finally:
        close_db_session(session)
def get_sqlite_connection():
    """
        Get a direct SQLite connection (for raw SQL if needed)
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn
