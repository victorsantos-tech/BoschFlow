from werkzeug.security import generate_password_hash

from app import app
from database import db

from models.usuario import Usuario


with app.app_context():

    email_demo = "demo@boschflow.com"


    usuario = Usuario.query.filter_by(
        email=email_demo
    ).first()


    if usuario:

        print("=" * 40)
        print("Usuário demo já existe!")
        print("=" * 40)
        print("Email: demo@boschflow.com")
        print("Senha: boschflow123")
        print("=" * 40)


    else:


        demo = Usuario(

            nome="Usuário Demonstração",

            email=email_demo,

            senha=generate_password_hash(
                "boschflow123"
            ),

            perfil="ADMIN"

        )


        db.session.add(demo)

        db.session.commit()


        print("=" * 40)
        print("Usuário demo criado com sucesso!")
        print("=" * 40)
        print("Email: demo@boschflow.com")
        print("Senha: boschflow123")
        print("=" * 40)