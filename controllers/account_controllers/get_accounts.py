"""
    Controlador para obter contas bancárias
"""

from db.queries.account_queries import get_all_accounts, get_account_by_id


def get_accounts():
    """
    Obtém todas as contas bancárias

    Returns:
        list: Lista de dicionários com informações das contas
    """
    accounts = get_all_accounts()

    # Transformar objetos Account em dicionários para facilitar o uso na interface
    accounts_dict = [
        {
            'id': account.id,
            'name': account.name,
            'type_account': account.type_account,
            'balance': account.balance
        }
        for account in accounts
    ]

    return accounts_dict


def get_account(account_id):
    """
    Obtém uma conta bancária específica

    Args:
        account_id (int): ID da conta

    Returns:
        dict: Dicionário com informações da conta ou None se não encontrada
    """
    account = get_account_by_id(account_id)

    if not account:
        return None

    # Transformar objeto Account em dicionário
    account_dict = {
        'id': account.id,
        'name': account.name,
        'type_account': account.type_account,
        'balance': account.balance
    }

    return account_dict
