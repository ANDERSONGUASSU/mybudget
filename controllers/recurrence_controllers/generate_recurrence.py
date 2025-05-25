"""
    Cria uma nova recorrência.
"""
from sqlalchemy.exc import SQLAlchemyError
from dateutil.relativedelta import relativedelta
from db.models import Income, Expense, Account





def generate_recurrence(session, base, recurrence):
    """_summary_
    Gera lançamentos futuros com base na recorrência.
    Args:
        session: Sessão SQLALchemy.
        base: Objeto base (Income ou Expense).
        recurrence: Objeto recorrência associado.
    """
    type_map = {
        'unica': lambda d, i: d,  # apenas um lançamento (não gera recorrência)
        'diaria': lambda d, i: d + relativedelta(days=i),
        'semanal': lambda d, i: d + relativedelta(weeks=i),
        'quinzenal': lambda d, i: d + relativedelta(weeks=i * 2),
        'mensal': lambda d, i: d + relativedelta(months=i),
        'bimestral': lambda d, i: d + relativedelta(months=i * 2),
        'trimestral': lambda d, i: d + relativedelta(months=i * 3),
        'semestral': lambda d, i: d + relativedelta(months=i * 6),
        'anual': lambda d, i: d + relativedelta(years=i)
    }

    recurrence_type = recurrence.type.lower()

    if recurrence_type not in type_map:
        raise ValueError(f'Tipo de recorrência inválido: {recurrence_type}')

    if recurrence_type == 'unica':
        print("Tipo única: não há lançamentos para gerar.")
        return

    for i in range(1, recurrence.frequency):
        new_date = type_map[recurrence_type](base.date, i)
        if isinstance(base, Income):
            new_transaction_type = Income(
                description=base.description,
                value=base.amount,
                date=new_date,
                category_id=base.category_id,
                account_id=base.account_id,
                recurrence_id=recurrence.id
            )
        elif isinstance(base, Expense):
            new_transaction_type = Expense(
                description=base.description,
                value=base.amount,
                date=new_date,
                category_id=base.category_id,
                account_id=base.account_id,
                recurrence_id=recurrence.id
            )
        else:
            raise TypeError(f'Tipo de base não suportado: {type(base)}')
        session.add(new_transaction_type)

        account = session.query(Account).filter_by(id=base.account_id).first()
        if account:
            if isinstance(base, Income):
                account.balance += base.amount
            elif isinstance(base, Expense):
                account.balance -= base.amount
    try:
        session.commit()
        print(f'{recurrence.frequency - 1} lançamentos gerados com sucesso ({recurrence_type}).')
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Erro ao gerar lançamentos: {e}')
