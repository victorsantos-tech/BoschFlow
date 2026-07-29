from sqlalchemy import func

from database import db
from models.produtos import Produto
from models.fornecedor import Fornecedor
from models.movimentacao import Movimentacao
from models.categoria import Categoria


class DashboardService:

    @staticmethod
    def indicadores():

        # ==========================
        # Indicadores
        # ==========================

        total_produtos = Produto.query.count()

        total_fornecedores = Fornecedor.query.count()

        estoque_critico = Produto.query.filter(
            Produto.quantidade <= Produto.estoque_minimo
        ).count()

        valor_total = (
            db.session.query(
                func.sum(
                    Produto.preco * Produto.quantidade
                )
            ).scalar()
            or 0
        )

        # ==========================
        # Últimas movimentações
        # ==========================

        ultimas_movimentacoes = (
            Movimentacao.query
            .order_by(Movimentacao.data.desc())
            .limit(10)
            .all()
        )

        # ==========================
        # Entradas x Saídas
        # ==========================

        entradas = (
            Movimentacao.query
            .filter_by(tipo="ENTRADA")
            .count()
        )

        saidas = (
            Movimentacao.query
            .filter_by(tipo="SAIDA")
            .count()
        )

        # ==========================
        # Produtos por categoria
        # ==========================

        categorias = (
            db.session.query(
                Categoria.nome,
                func.count(Produto.id)
            )
            .outerjoin(
                Produto,
                Produto.categoria_id == Categoria.id
            )
            .group_by(Categoria.nome)
            .all()
        )

        categorias_labels = [categoria[0] for categoria in categorias]
        categorias_valores = [categoria[1] for categoria in categorias]

        # ==========================
        # Produtos mais movimentados
        # ==========================

        top_produtos = (
            db.session.query(
                Produto.nome,
                func.sum(Movimentacao.quantidade).label("total")
            )
            .join(
                Movimentacao,
                Movimentacao.produto_id == Produto.id
            )
            .group_by(Produto.id, Produto.nome)
            .order_by(func.sum(Movimentacao.quantidade).desc())
            .limit(5)
            .all()
        )

        # ==========================
        # Produtos em estoque crítico
        # ==========================

        produtos_criticos = (
            Produto.query
            .filter(
                Produto.quantidade <= Produto.estoque_minimo
            )
            .order_by(Produto.quantidade.asc())
            .all()
        )

        # ==========================
        # Retorno
        # ==========================

        return {
            "total_produtos": total_produtos,
            "total_fornecedores": total_fornecedores,
            "estoque_critico": estoque_critico,
            "valor_total": valor_total,
            "ultimas_movimentacoes": ultimas_movimentacoes,
            "entradas": entradas,
            "saidas": saidas,
            "categorias_labels": categorias_labels,
            "categorias_valores": categorias_valores,
            "top_produtos": top_produtos,
            "produtos_criticos": produtos_criticos,
        }