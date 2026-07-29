import os

from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for,
    request
)

from config import Config
from database import db


# ==========================
# Models
# ==========================

from models.categoria import Categoria
from models.fornecedor import Fornecedor
from models.produtos import Produto
from models.usuario import Usuario
from models.movimentacao import Movimentacao


# ==========================
# Services
# ==========================

from services.dashboard_service import DashboardService


# ==========================
# Blueprints
# ==========================

from routes.auth import auth_bp
from routes.categorias import categorias_bp
from routes.produtos import produtos_bp
from routes.fornecedores import fornecedores_bp
from routes.movimentacoes import movimentacoes_bp
from routes.saidas import saida_bp
from routes.dashboard import dashboard_bp



app = Flask(__name__)


app.config.from_object(Config)


# ==========================
# Upload de imagens
# ==========================

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)



# ==========================
# Banco
# ==========================

db.init_app(app)


app.secret_key = app.config["SECRET_KEY"]



# ==========================
# Registro dos Blueprints
# ==========================

app.register_blueprint(auth_bp)

app.register_blueprint(categorias_bp)

app.register_blueprint(produtos_bp)

app.register_blueprint(fornecedores_bp)

app.register_blueprint(movimentacoes_bp)

app.register_blueprint(saida_bp)

app.register_blueprint(dashboard_bp)



# ==========================
# Proteção Login
# ==========================

@app.before_request
def verificar_login():

    rotas_livres = [

        "auth.login",

        "static"

    ]


    if session.get("usuario_id"):

        return


    if request.endpoint in rotas_livres:

        return


    if request.endpoint and request.endpoint.startswith("static"):

        return


    return redirect(
        url_for("auth.login")
    )



# ==========================
# Dashboard
# ==========================

@app.route("/")
def dashboard():


    dados = DashboardService.indicadores()


    return render_template(

        "dashboard.html",

        **dados

    )



# ==========================
# Criar tabelas
# ==========================

with app.app_context():

    db.create_all()



# ==========================
# Executar
# ==========================

if __name__ == "__main__":

    app.run(
        debug=True
    )