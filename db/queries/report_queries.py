"""
    Queries para relatórios financeiros
"""

from db.database import get_db_session, close_db_session
from sqlalchemy import text
from datetime import datetime, timedelta

def get_monthly_summary(year):
    """
    Obtém um resumo financeiro mensal para o ano especificado

    Args:
        year (int): Ano desejado

    Returns:
        list: Lista de dicionários com resumo por mês
    """
    session = get_db_session()
    try:
        query = text("""
            WITH MonthlyIncome AS (
                SELECT 
                    EXTRACT(MONTH FROM date) as month,
                    SUM(amount) as income
                FROM incomes
                WHERE EXTRACT(YEAR FROM date) = :year
                GROUP BY EXTRACT(MONTH FROM date)
            ),
            MonthlyExpense AS (
                SELECT 
                    EXTRACT(MONTH FROM date) as month,
                    SUM(amount) as expense
                FROM expenses
                WHERE EXTRACT(YEAR FROM date) = :year
                GROUP BY EXTRACT(MONTH FROM date)
            ),
            MonthlyCreditCard AS (
                SELECT 
                    EXTRACT(MONTH FROM date) as month,
                    SUM(amount) as credit_expense
                FROM credit_card_transactions
                WHERE EXTRACT(YEAR FROM date) = :year
                GROUP BY EXTRACT(MONTH FROM date)
            ),
            AllMonths AS (
                SELECT generate_series(1, 12) as month
            )
            
            SELECT 
                am.month,
                COALESCE(mi.income, 0) as income,
                COALESCE(me.expense, 0) as expense,
                COALESCE(mcc.credit_expense, 0) as credit_expense,
                COALESCE(mi.income, 0) - COALESCE(me.expense, 0) - COALESCE(mcc.credit_expense, 0) as balance
            FROM AllMonths am
            LEFT JOIN MonthlyIncome mi ON am.month = mi.month
            LEFT JOIN MonthlyExpense me ON am.month = me.month
            LEFT JOIN MonthlyCreditCard mcc ON am.month = mcc.month
            ORDER BY am.month
        """)

        results = session.execute(query, {"year": year}).fetchall()

        # Converter para lista de dicionários
        months = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        return [
            {
                "month": months[int(row["month"]) - 1],
                "month_num": int(row["month"]),
                "income": float(row["income"]),
                "expense": float(row["expense"]),
                "credit_expense": float(row["credit_expense"]),
                "balance": float(row["balance"])
            }
            for row in results
        ]
    finally:
        close_db_session(session)

def get_income_expense_comparison(year=None, month=None):
    """
    Obtém comparação entre receitas e despesas

    Args:
        year (int, optional): Ano desejado. Se não for fornecido, usa o ano atual
        month (int, optional): Mês desejado (1-12). Se não for fornecido, retorna dados do ano todo

    Returns:
        dict: Dicionário com receitas, despesas e saldo
    """
    session = get_db_session()
    try:
        current_date = datetime.now()
        year = year or current_date.year

        params = {"year": year}

        if month:
            income_query = """
                SELECT COALESCE(SUM(amount), 0) as total
                FROM incomes
                WHERE EXTRACT(YEAR FROM date) = :year
                AND EXTRACT(MONTH FROM date) = :month
            """
            expense_query = """
                SELECT COALESCE(SUM(amount), 0) as total
                FROM expenses
                WHERE EXTRACT(YEAR FROM date) = :year
                AND EXTRACT(MONTH FROM date) = :month
            """
            credit_query = """
                SELECT COALESCE(SUM(amount), 0) as total
                FROM credit_card_transactions
                WHERE EXTRACT(YEAR FROM date) = :year
                AND EXTRACT(MONTH FROM date) = :month
            """
            params["month"] = month
        else:
            income_query = """
                SELECT COALESCE(SUM(amount), 0) as total
                FROM incomes
                WHERE EXTRACT(YEAR FROM date) = :year
            """
            expense_query = """
                SELECT COALESCE(SUM(amount), 0) as total
                FROM expenses
                WHERE EXTRACT(YEAR FROM date) = :year
            """
            credit_query = """
                SELECT COALESCE(SUM(amount), 0) as total
                FROM credit_card_transactions
                WHERE EXTRACT(YEAR FROM date) = :year
            """

        income_total = session.execute(text(income_query), params).scalar()
        expense_total = session.execute(text(expense_query), params).scalar()
        credit_total = session.execute(text(credit_query), params).scalar()

        income_total = float(income_total) if income_total is not None else 0.0
        expense_total = float(expense_total) if expense_total is not None else 0.0
        credit_total = float(credit_total) if credit_total is not None else 0.0

        return {
            "income": income_total,
            "expense": expense_total,
            "credit_expense": credit_total,
            "total_expense": expense_total + credit_total,
            "balance": income_total - expense_total - credit_total
        }
    finally:
        close_db_session(session)

def get_category_distribution(transaction_type, year=None, month=None):
    """
    Obtém a distribuição de transações por categoria

    Args:
        transaction_type (str): Tipo de transação ('income', 'expense', 'credit')
        year (int, optional): Ano desejado. Se não for fornecido, usa o ano atual
        month (int, optional): Mês desejado (1-12). Se não for fornecido, retorna dados do ano todo

    Returns:
        list: Lista de dicionários com categoria e valores
    """
    session = get_db_session()
    try:
        current_date = datetime.now()
        year = year or current_date.year

        params = {"year": year}

        if transaction_type == 'income':
            table_name = 'incomes'
        elif transaction_type == 'expense':
            table_name = 'expenses'
        elif transaction_type == 'credit':
            table_name = 'credit_card_transactions'
        else:
            raise ValueError(f"Tipo de transação inválido: {transaction_type}")

        base_query = f"""
            SELECT 
                c.name as category_name, 
                c.color as category_color,
                SUM(t.amount) as total,
                COUNT(t.id) as count
            FROM {table_name} t
            JOIN categories c ON t.category_id = c.id
            WHERE EXTRACT(YEAR FROM t.date) = :year
        """

        if month:
            base_query += " AND EXTRACT(MONTH FROM t.date) = :month"
            params["month"] = month

        base_query += """
            GROUP BY c.name, c.color
            ORDER BY total DESC
        """

        query = text(base_query)
        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários
        return [
            {
                "category": row["category_name"],
                "color": row["category_color"],
                "value": float(row["total"]),
                "count": int(row["count"])
            }
            for row in results
        ]
    finally:
        close_db_session(session)

def get_cash_flow_by_day(start_date, end_date):
    """
    Obtém o fluxo de caixa diário em um período

    Args:
        start_date (str ou datetime): Data inicial
        end_date (str ou datetime): Data final

    Returns:
        list: Lista de dicionários com fluxo de caixa por dia
    """
    session = get_db_session()
    try:
        # Converter datas se necessário
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        elif isinstance(start_date, datetime):
            start_date = start_date.date()

        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        elif isinstance(end_date, datetime):
            end_date = end_date.date()

        query = text("""
            WITH DateSeries AS (
                SELECT date(generate_series(:start_date::timestamp, :end_date::timestamp, '1 day')) as day
            ),
            DailyIncome AS (
                SELECT date as day, SUM(amount) as income
                FROM incomes
                WHERE date BETWEEN :start_date AND :end_date
                GROUP BY date
            ),
            DailyExpense AS (
                SELECT date as day, SUM(amount) as expense
                FROM expenses
                WHERE date BETWEEN :start_date AND :end_date
                GROUP BY date
            ),
            DailyCreditCard AS (
                SELECT date as day, SUM(amount) as credit_expense
                FROM credit_card_transactions
                WHERE date BETWEEN :start_date AND :end_date
                GROUP BY date
            )
            
            SELECT 
                ds.day,
                COALESCE(di.income, 0) as income,
                COALESCE(de.expense, 0) as expense,
                COALESCE(dc.credit_expense, 0) as credit_expense,
                COALESCE(di.income, 0) - COALESCE(de.expense, 0) - COALESCE(dc.credit_expense, 0) as balance
            FROM DateSeries ds
            LEFT JOIN DailyIncome di ON ds.day = di.day
            LEFT JOIN DailyExpense de ON ds.day = de.day
            LEFT JOIN DailyCreditCard dc ON ds.day = dc.day
            ORDER BY ds.day
        """)

        params = {
            "start_date": start_date,
            "end_date": end_date
        }

        results = session.execute(query, params).fetchall()

        # Converter para lista de dicionários
        return [
            {
                "date": row["day"].strftime("%Y-%m-%d"),
                "income": float(row["income"]),
                "expense": float(row["expense"]),
                "credit_expense": float(row["credit_expense"]),
                "balance": float(row["balance"])
            }
            for row in results
        ]
    finally:
        close_db_session(session)
