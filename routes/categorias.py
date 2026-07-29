from flask import Blueprint, render_template, request, redirect, url_for, flash

from database import db
from models.categoria import Categoria

categorias_bp = Blueprint(
    "categorias",
    __name__,
    url_prefix="/categorias"
)


@categorias_bp.route("/")
def listar():

    categorias = Categoria.query.order_by(Categoria.nome).all()

    return render_template(
        "categorias/listar.html",
        categorias=categorias
    )


@categorias_bp.route("/nova", methods=["GET", "POST"])
def nova():

    if request.method == "POST":

        nome = request.form["nome"]
        descricao = request.form["descricao"]

        categoria = Categoria(
            nome=nome,
            descricao=descricao
        )

        db.session.add(categoria)
        db.session.commit()

        flash("Categoria cadastrada com sucesso!", "success")

        return redirect(url_for("categorias.listar"))

    return render_template("categorias/cadastrar.html")


@categorias_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    categoria = Categoria.query.get_or_404(id)

    if request.method == "POST":

        categoria.nome = request.form["nome"]
        categoria.descricao = request.form["descricao"]

        db.session.commit()

        flash("Categoria atualizada!", "success")

        return redirect(url_for("categorias.listar"))

    return render_template(
        "categorias/editar.html",
        categoria=categoria
    )


@categorias_bp.route("/excluir/<int:id>")
def excluir(id):

    categoria = Categoria.query.get_or_404(id)

    db.session.delete(categoria)

    db.session.commit()

    flash("Categoria removida!", "warning")

    return redirect(url_for("categorias.listar"))