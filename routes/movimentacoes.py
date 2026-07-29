from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.produtos import Produto
from models.movimentacao import Movimentacao

from services.estoque_service import EstoqueService

movimentacoes_bp = Blueprint(
    "movimentacoes",
    __name__,
    url_prefix="/movimentacoes"
)


@movimentacoes_bp.route("/")
def listar():

    movimentacoes = (
        Movimentacao.query
        .order_by(Movimentacao.data.desc())
        .all()
    )

    return render_template(
        "movimentacoes/listar.html",
        movimentacoes=movimentacoes
    )


@movimentacoes_bp.route("/entrada", methods=["GET", "POST"])
def entrada():

    produtos = Produto.query.order_by(
        Produto.nome
    ).all()

    if request.method == "POST":

        try:

            EstoqueService.entrada(

                produto_id=int(request.form["produto_id"]),

                quantidade=int(request.form["quantidade"])

            )

            flash(
                "Entrada registrada com sucesso!",
                "success"
            )

            return redirect(
                url_for("movimentacoes.listar")
            )

        except Exception as erro:

            flash(
                str(erro),
                "danger"
            )

    return render_template(
        "movimentacoes/entrada.html",
        produtos=produtos
    )