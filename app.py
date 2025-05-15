"""
Este arquivo é o ponto de entrada do aplicativo Dash.
Ele configura o ambiente do aplicativo, define as folhas de estilo e inicializa o aplicativo.
"""

# Importações de bibliotecas padrão
import dash

# Importações para o banco de dados
from db.database import init_db, get_db_session, close_db_session

# bootstrap
BOOTSTRAP = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
# Fonts
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
# FontAwesome para ícones
FONTAWESOME = "https://use.fontawesome.com/releases/v5.15.4/css/all.css"

ESTILOS = [BOOTSTRAP, FONTS, FONTAWESOME]
DBC_CSS = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@latest/dbc.css"


app = dash.Dash(
    __name__,
    external_stylesheets=ESTILOS + [DBC_CSS],
    assets_folder='src/assets'
)

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server

# Inicializar o banco de dados
print("Inicializando banco de dados...")
init_db()
print("Banco de dados inicializado com sucesso!")

# Função para obter uma sessão do banco de dados
def get_session():
    """Retorna uma sessão do banco de dados"""
    return get_db_session()

# Função para fechar uma sessão do banco de dados
def close_session(session):
    """Fecha uma sessão do banco de dados"""
    close_db_session(session)
