from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.produtos import Produto

from services.estoque_service import EstoqueService

saida_bp = Blueprint(
    "saida",
    __name__,
    url_prefix="/saida"
)


@saida_bp.route("/", methods=["GET", "POST"])
def saida():

    produtos = Produto.query.order_by(
        Produto.nome
    ).all()

    if request.method == "POST":

        try:

            EstoqueService.saida(

                produto_id=int(request.form["produto_id"]),

                quantidade=int(request.form["quantidade"])

            )

            flash(
                "Saída registrada com sucesso!",
                "success"
            )

            return redirect(
                url_for("movimentacoes.listar")
            )

        except ValueError as erro:

            flash(
                str(erro),
                "danger"
            )

    return render_template(
        "movimentacoes/saida.html",
        produtos=produtos
    )