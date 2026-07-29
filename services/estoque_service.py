from database import db

from models.produtos import Produto
from models.movimentacao import Movimentacao


class EstoqueService:

    @staticmethod
    def entrada(produto_id, quantidade):

        produto = Produto.query.get_or_404(produto_id)

        produto.quantidade += quantidade

        movimentacao = Movimentacao(
            produto_id=produto.id,
            tipo="ENTRADA",
            quantidade=quantidade
        )

        db.session.add(movimentacao)
        db.session.commit()

        return produto


    @staticmethod
    def saida(produto_id, quantidade):

        produto = Produto.query.get_or_404(produto_id)

        if quantidade > produto.quantidade:
            raise ValueError("Estoque insuficiente.")

        produto.quantidade -= quantidade

        movimentacao = Movimentacao(
            produto_id=produto.id,
            tipo="SAIDA",
            quantidade=quantidade
        )

        db.session.add(movimentacao)
        db.session.commit()

        return produto