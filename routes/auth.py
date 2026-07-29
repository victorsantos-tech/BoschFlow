from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

from werkzeug.security import check_password_hash

from models.usuario import Usuario

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        senha = request.form["senha"]

        usuario = Usuario.query.filter_by(
            email=email
        ).first()

        if usuario and check_password_hash(
            usuario.senha,
            senha
        ):

            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            session["perfil"] = usuario.perfil

            flash(
                f"Bem-vindo, {usuario.nome}!",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "E-mail ou senha inválidos.",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    flash(
        "Logout realizado com sucesso.",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )