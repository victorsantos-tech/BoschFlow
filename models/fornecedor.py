from database import db


class Fornecedor(db.Model):

    __tablename__ = "fornecedores"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(120), nullable=False)

    telefone = db.Column(db.String(20))

    email = db.Column(db.String(120))

    cidade = db.Column(db.String(100))

    produtos = db.relationship(
        "Produto",
        back_populates="fornecedor",
        lazy=True
    )

    def __repr__(self):
        return f"<Fornecedor {self.nome}>"