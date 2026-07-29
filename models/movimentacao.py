from datetime import datetime

from database import db


class Movimentacao(db.Model):

    __tablename__ = "movimentacoes"

    id = db.Column(db.Integer, primary_key=True)

    tipo = db.Column(db.String(20), nullable=False)

    quantidade = db.Column(db.Integer, nullable=False)

    data = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    observacao = db.Column(db.String(255))

    produto_id = db.Column(
        db.Integer,
        db.ForeignKey("produtos.id"),
        nullable=False
    )

    produto = db.relationship(
        "Produto",
        back_populates="movimentacoes"
    )

    def __repr__(self):
        return f"<Movimentacao {self.tipo}>"