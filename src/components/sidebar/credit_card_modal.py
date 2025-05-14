"""
    Componente de modal para adição de transações de cartão de crédito.
"""

from datetime import datetime
from dash import dcc, html
import dash_bootstrap_components as dbc

from src.components.sidebar.category_modal import get_add_category_modal

# Modal de adição de transação de cartão de crédito
def get_credit_card_modal():
    """
    Retorna o modal de adição de transação de cartão de crédito.
    """
    return dbc.Modal([
        dbc.ModalHeader("Cartão de Crédito"),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label("Descrição"),
                    dbc.Input(id="credit_card_name", placeholder="Nome da transação"),
                ], width=6, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Valor"),
                    dbc.Input(id="credit_card_value", placeholder="R$ 0,00"),
                ], width=6, className="mb-3 p-2"),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data da Compra"),
                    dcc.DatePickerSingle(
                        id="credit_card_date",
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
                        id="credit_card_category",
                        options=[
                            {"label": "Alimentação", "value": "alimentacao"},
                            {"label": "Transporte", "value": "transporte"},
                            {"label": "Saúde", "value": "saude"},
                            {"label": "Educação", "value": "educacao"},
                            {"label": "Lazer", "value": "lazer"},
                            {"label": "Vestuário", "value": "vestuario"},
                            {"label": "Assinaturas", "value": "assinaturas"},
                            {"label": "Outros", "value": "outros"}
                        ],
                        placeholder="Selecione uma categoria"
                    )
                ], width=4, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Cartão"),
                    dbc.Select(
                        id="credit_card_account",
                        options=[
                            {"label": "Nubank", "value": "nubank"},
                            {"label": "Itaú", "value": "itau"},
                            {"label": "Santander", "value": "santander"},
                            {"label": "Bradesco", "value": "bradesco"},
                            {"label": "Outro", "value": "outro"}
                        ],
                        placeholder="Selecione um cartão"
                    )
                ], width=4, className="mb-3 p-2")
            ], style={'margin-top': '25px'}),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Parcelas"),
                    dbc.InputGroup([
                        dbc.Select(
                            id="credit_card_installments",
                            options=[
                                {"label": f"{i}x", "value": i} for i in range(1, 13)
                            ],
                            value=1
                        ),
                        dbc.InputGroupText("parcelas")
                    ])
                ], width=4, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Data de Vencimento"),
                    dcc.DatePickerSingle(
                        id="credit_card_due_date",
                        min_date_allowed=datetime(2020, 1, 1),
                        max_date_allowed=datetime(2030, 12, 31),
                        date=datetime.today().replace(day=1).replace(month=datetime.today().month + 1 if datetime.today().month < 12 else 1),
                        display_format="DD/MM/YYYY",
                        style={"width": "100%"}
                    )
                ], width=4, className="mb-3 p-2"),
                dbc.Col([
                    dbc.Label("Status"),
                    dbc.RadioItems(
                        id="credit_card_status",
                        options=[
                            {"label": "Pendente", "value": "pendente"},
                            {"label": "Pago", "value": "pago"}
                        ],
                        value="pendente",
                        inline=True
                    )
                ], width=4, className="mb-3 p-2")
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Observações"),
                    dbc.Textarea(
                        id="credit_card_notes",
                        placeholder="Observações adicionais...",
                        style={"height": "80px"}
                    )
                ], width=12, className="mb-3 p-2"),
            ]),
            get_add_category_modal("credit_card"),
        ]),
        html.Div(id="id_test_credit_card", className="mt-3", style={},),
        dbc.ModalFooter([
            dbc.Button("Salvar", color="primary", id="save_credit_card_button"),
            dbc.Popover(dbc.PopoverBody("Transação de cartão adicionada com sucesso!"),
                        target="save_credit_card_button",
                        trigger="click"),
            dbc.Button("Cancelar", color="secondary", id="cancel_credit_card_button"),
        ]),
    ], id="modal-credit-card",
        size="xl",
        is_open=False,
        centered=True,
        backdrop=True,
        style={"backgroundColor": "rgba(220, 53, 69, 0.1)"})
