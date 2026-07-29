from app import app
from database import db

from models.produtos import Produto


imagens = {

    "BOS001": "sensor_capacitivo.jpg",

    "BOS002": "sensor fotoeletrico industrial.png",

    "BOS006": "plc industrial.jpg",

    "BOS022": "fonte_industrial.jpg"

}



with app.app_context():


    for codigo, imagem in imagens.items():

        produto = Produto.query.filter_by(
            codigo=codigo
        ).first()


        if produto:

            produto.imagem = imagem

            print(
                f"{produto.nome} -> {imagem}"
            )


        else:

            print(
                f"{codigo} não encontrado"
            )


    db.session.commit()


print("Imagens atualizadas com sucesso!")