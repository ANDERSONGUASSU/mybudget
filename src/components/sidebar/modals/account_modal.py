"""
    Componente de modal para adição de contas.
"""

import dash_bootstrap_components as dbc
import dash.html as html


def get_add_account_modal(text):
    """
    Retorna o modal de adição de conta.
    """
    return dbc.Accordion([
        dbc.AccordionItem(
            title="Adicionar/Excluir Conta",
            children=[
                dbc.Row([
                    dbc.Col([
                        html.Legend("Adicionar Conta"),
                        dbc.Input(
                            id=f"account_name_{text}",
                            placeholder="Nome da conta",
                            className="mb-3"),
                        dbc.Input(
                            id=f"account_type_{text}",
                            placeholder="Tipo da conta",
                            className="mb-3"),
                        dbc.Input(
                            id=f"account_balance_{text}",
                            placeholder="Saldo da conta",
                            className="mb-3"),
                        dbc.Button(
                            "Adicionar",
                            id=f"add_account_button_{text}",
                            color="primary",
                            className="mb-3 btn btn-success"),
                        html.Div(id=f"account_message_{text}", className="mt-3", style={"color": "green"})
                    ], width=6, className="mb-3 p-2"),
                    dbc.Col([
                        html.Legend("Excluir Conta", className="text-danger"),
                        dbc.Checklist(
                            id=f"delete_account_checklist_{text}",
                            options=[],
                            value=[],
                            switch=True,
                            label_checked_style={'color': 'red'},
                            input_checked_style={'backgroundColor': 'blue', 'border-color': 'orange'}
                        ),
                        dbc.Button(
                            "Excluir",
                            id=f"delete_account_button_{text}",
                            color="danger",
                            className="mb-3 btn btn-danger"),
                    ], width=6, className="mb-3 p-2")
                ])
            ])
    ], id=f"add_account_modal_{text}", start_collapsed=True, flush=True)
