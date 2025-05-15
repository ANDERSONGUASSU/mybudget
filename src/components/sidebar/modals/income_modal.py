"""
    Componente de modal para adição de receitas.
"""

from datetime import datetime
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.sidebar.modals.category_modal import get_add_category_modal
from src.components.sidebar.modals.account_modal import get_add_account_modal
# Modal de adição de receita
def get_income_modal():
    """
    Retorna o modal de adição de receita.
    """
    return dbc.Modal([
        dbc.ModalHeader("Adicionar Receita"),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label("Descrição"),
                    dbc.Input(id="income_name", placeholder="Nome da receita"),
                ], width=6, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Valor"),
                    dbc.Input(id="income_value", placeholder="R$ 0,00"),
                ], width=6, className="mb-3 p-2"),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data"),
                    dcc.DatePickerSingle(
                        id="income_date",
                        min_date_allowed=datetime(2020, 1, 1),
                        max_date_allowed=datetime(2030, 12, 31),
                        date=datetime.today(),
                        display_format="DD/MM/YYYY",
                        style={"width": "100%"}
                    )
                ], width=4, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Categoria"),
                    dbc.Select(
                        id="income_category",
                        options=[
                            {"label": "Salário", "value": "salario"},
                            {"label": "Investimentos", "value": "investimentos"},
                            {"label": "Freelance", "value": "freelance"},
                            {"label": "Outros", "value": "outros"}
                        ],
                        placeholder="Selecione uma categoria"
                    )
                ], width=4, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Conta"),
                    dbc.Select(
                        id="income_account",
                        options=[
                            {"label": "Conta Corrente", "value": "conta_corrente"},
                            {"label": "Poupança", "value": "poupanca"},
                            {"label": "Cartão de Crédito", "value": "cartao_credito"},
                            {"label": "Dinheiro", "value": "dinheiro"},
                            {"label": "Investimentos", "value": "investimentos"}
                        ],
                        placeholder="Selecione uma conta"
                    )
                ], width=4, className="mb-3 p-2")
            ], style={'margin-top': '25px'}),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Recorrência"),
                    dbc.Select(
                        id="income_recurrence",
                        options=[
                            {"label": "Única", "value": "unica"},
                            {"label": "Diária", "value": "diaria"},
                            {"label": "Semanal", "value": "semanal"},
                            {"label": "Quinzenal", "value": "quinzenal"},
                            {"label": "Mensal", "value": "mensal"},
                            {"label": "Bimestral", "value": "bimestral"},
                            {"label": "Trimestral", "value": "trimestral"},
                            {"label": "Semestral", "value": "semestral"},
                            {"label": "Anual", "value": "anual"}
                        ],
                        value="unica",
                        placeholder="Selecione a recorrência"
                    )
                ], width=6, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        id="income_extras",
                        options=[],
                        value=[],
                        switch=True
                    )
                ], width=6, className="mb-3 p-2"),
            ]),
            get_add_category_modal("income"),
            get_add_account_modal("income"),
        ]),
        html.Div(id="id_test_income", className="mt-3", style={},),
        dbc.ModalFooter([
            dbc.Button("Salvar", color="primary", id="save_income_button"),
            dbc.Popover(dbc.PopoverBody("Receita adicionada com sucesso!"),
                        target="save_income_button",
                        trigger="click"),
            dbc.Button("Cancelar", color="secondary", id="cancel_income_button"),
        ]),
    ], id="modal-income",
        size="xl",
        is_open=False,
        centered=True,
        backdrop=True,
        style={"backgroundColor": "rgba(17, 140, 79, 0.1)"})
