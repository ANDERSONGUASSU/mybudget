"""
    Componente de modal para adição de categorias.
"""

import dash_bootstrap_components as dbc
import dash.html as html


def get_add_category_modal(text):
    """
    Retorna o modal de adição de categoria.
    """
    return dbc.Accordion([
        dbc.AccordionItem(
            title="Adicionar/Excluir Categoria",
            children=[
                dbc.Row([
                    dbc.Col([
                        html.Legend("Adicionar Categoria"),
                        dbc.Input(
                            id=f"category_name_{text}",
                            placeholder="Nome da categoria",
                            className="mb-3"),
                        dbc.Input(
                            id=f"category_color_{text}",
                            type="color", value="#000000",
                            className="mb-3"),
                        dbc.Button(
                            "Adicionar",
                            id=f"add_category_button_{text}",
                            color="primary",
                            className="mb-3 btn btn-success"),
                        html.Div(id=f"category_message_{text}", className="mt-3", style={},)
                    ], width=6, className="mb-3 p-2"),
                    dbc.Col([
                        html.Legend("Excluir Categoria", className="text-danger"),
                        dbc.Checklist(
                            id=f"delete_category_checklist_{text}",
                            options=[],
                            value=[],
                            switch=True,
                            label_checked_style={'color': 'red'},
                            input_checked_style={'backgroundColor': 'blue', 'border-color': 'orange'}
                        ),
                        dbc.Button(
                            "Excluir",
                            id=f"delete_category_button_{text}",
                            color="danger",
                            className="mb-3 btn btn-danger"),
                    ], width=6, className="mb-3 p-2")
                ])
            ])
    ], id=f"add_category_modal_{text}", start_collapsed=True, flush=True)
