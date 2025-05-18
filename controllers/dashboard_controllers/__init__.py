"""
    Controladores para o dashboard

    Este pacote contém controladores para gerar dados para o dashboard.
"""

from controllers.dashboard_controllers.get_cash_flow import get_cash_flow
from controllers.dashboard_controllers.get_expense_breakdown import get_expense_breakdown
from controllers.dashboard_controllers.get_monthly_summary import get_monthly_summary

__all__ = [
    'get_cash_flow',
    'get_expense_breakdown',
    'get_monthly_summary',
]
