from database import db


class Produto(db.Model):

    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)

    codigo = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    descricao = db.Column(
        db.String(255)
    )

    preco = db.Column(
        db.Float,
        default=0
    )

    quantidade = db.Column(
        db.Integer,
        default=0
    )

    estoque_minimo = db.Column(
        db.Integer,
        default=5
    )

    # NOVO CAMPO
    imagem = db.Column(
        db.String(255),
        nullable=True
    )

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey("categorias.id")
    )

    fornecedor_id = db.Column(
        db.Integer,
        db.ForeignKey("fornecedores.id")
    )

    categoria = db.relationship(
        "Categoria",
        back_populates="produtos"
    )

    fornecedor = db.relationship(
        "Fornecedor",
        back_populates="produtos"
    )

    movimentacoes = db.relationship(
        "Movimentacao",
        back_populates="produto",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Produto {self.nome}>"