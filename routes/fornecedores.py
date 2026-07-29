from flask import Blueprint, render_template, request, redirect, url_for, flash

from database import db
from models.fornecedor import Fornecedor

fornecedores_bp = Blueprint(
    "fornecedores",
    __name__,
    url_prefix="/fornecedores"
)


@fornecedores_bp.route("/")
def listar():

    fornecedores = Fornecedor.query.order_by(
        Fornecedor.nome
    ).all()

    return render_template(
        "fornecedores/listar.html",
        fornecedores=fornecedores
    )


@fornecedores_bp.route("/novo", methods=["GET", "POST"])
def novo():

    if request.method == "POST":

        fornecedor = Fornecedor(

            nome=request.form["nome"],

            telefone=request.form["telefone"],

            email=request.form["email"],

            cidade=request.form["cidade"]

        )

        db.session.add(fornecedor)

        db.session.commit()

        flash("Fornecedor cadastrado!", "success")

        return redirect(url_for("fornecedores.listar"))

    return render_template("fornecedores/cadastrar.html")


@fornecedores_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    fornecedor = Fornecedor.query.get_or_404(id)

    if request.method == "POST":

        fornecedor.nome = request.form["nome"]
        fornecedor.telefone = request.form["telefone"]
        fornecedor.email = request.form["email"]
        fornecedor.cidade = request.form["cidade"]

        db.session.commit()

        flash("Fornecedor atualizado!", "success")

        return redirect(url_for("fornecedores.listar"))

    return render_template(
        "fornecedores/editar.html",
        fornecedor=fornecedor
    )


@fornecedores_bp.route("/excluir/<int:id>")
def excluir(id):

    fornecedor = Fornecedor.query.get_or_404(id)

    db.session.delete(fornecedor)

    db.session.commit()

    flash("Fornecedor removido!", "warning")

    return redirect(url_for("fornecedores.listar"))