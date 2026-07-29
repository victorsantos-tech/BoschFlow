from database import db


class Categoria(db.Model):

    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False, unique=True)

    descricao = db.Column(db.String(255))

    produtos = db.relationship(
        "Produto",
        back_populates="categoria",
        lazy=True
    )

    def __repr__(self):
        return f"<Categoria {self.nome}>"