"""
    Pacote grafic - integra todos os componentes de gráficos.
"""

from dash import dcc
import plotly.graph_objects as go
import pandas as pd

def get_grafic():
    """
        Retorna o gráfico de extratos com dados de exemplo.
    """
    # Criar dados de exemplo para o gráfico
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    receitas = [4200, 3800, 5100, 4800, 5420, 6100]
    despesas = [3100, 3300, 3800, 3600, 3150, 3700]

    df = pd.DataFrame({
        'Mês': meses,
        'Receitas': receitas,
        'Despesas': despesas,
        'Saldo': [r - d for r, d in zip(receitas, despesas)]
    })

    # Criar um gráfico com duas linhas (receitas e despesas) e barras (saldo)
    fig = go.Figure()

    # Adicionar linha de receitas
    fig.add_trace(go.Scatter(
        x=df['Mês'],
        y=df['Receitas'],
        name='Receitas',
        line=dict(color='green', width=3),
        mode='lines+markers'
    ))

    # Adicionar linha de despesas
    fig.add_trace(go.Scatter(
        x=df['Mês'],
        y=df['Despesas'],
        name='Despesas',
        line=dict(color='red', width=3),
        mode='lines+markers'
    ))

    # Adicionar barras de saldo
    fig.add_trace(go.Bar(
        x=df['Mês'],
        y=df['Saldo'],
        name='Saldo',
        marker_color=['green' if x > 0 else 'red' for x in df['Saldo']],
        opacity=0.5
    ))

    # Configurar layout
    fig.update_layout(
        title='Receitas vs Despesas (Últimos 6 meses)',
        xaxis_title='Mês',
        yaxis_title='Valor (R$)',
        template='plotly_white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=20, r=20, t=60, b=20),
        hovermode="x unified"
    )

    return dcc.Graph(
        id="extratos-graph",
        figure=fig,
        style={"height": "400px"}
    )
