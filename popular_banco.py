from app import app
from database import db

from models.categoria import Categoria
from models.fornecedor import Fornecedor
from models.produtos import Produto


with app.app_context():

    # ==========================
    # CATEGORIAS
    # ==========================

    categorias = [
        "Sensores",
        "Automação Industrial",
        "Acionamentos",
        "Motores",
        "Fontes",
        "Identificação"
    ]

    categorias_db = {}

    for nome in categorias:

        categoria = Categoria.query.filter_by(nome=nome).first()

        if not categoria:
            categoria = Categoria(nome=nome)
            db.session.add(categoria)
            db.session.flush()

        categorias_db[nome] = categoria

    # ==========================
    # FORNECEDORES
    # ==========================

    fornecedores = [
        "Bosch",
        "Bosch Rexroth"
    ]

    fornecedores_db = {}

    for nome in fornecedores:

        fornecedor = Fornecedor.query.filter_by(nome=nome).first()

        if not fornecedor:

            fornecedor = Fornecedor(
                nome=nome,
                telefone="(19) 99999-9999",
                email=f"{nome.lower().replace(' ', '')}@boschflow.com"
            )

            db.session.add(fornecedor)
            db.session.flush()

        fornecedores_db[nome] = fornecedor

    # ==========================
    # PRODUTOS
    # ==========================

    produtos = [

        ("BOS001","Sensor Indutivo M12","Sensores","Bosch",45,10,189.90),
        ("BOS002","Sensor Fotoelétrico","Sensores","Bosch",30,8,249.90),
        ("BOS003","Sensor Capacitivo","Sensores","Bosch",18,5,229.90),
        ("BOS004","Sensor Ultrassônico","Sensores","Bosch",12,4,699.90),
        ("BOS005","Encoder Incremental","Sensores","Bosch",15,5,799.90),

        ("BOS006","CLP CtrlX Core","Automação Industrial","Bosch",8,2,4590.00),
        ("BOS007","Módulo Entrada Digital","Automação Industrial","Bosch",16,5,890.00),
        ("BOS008","Módulo Saída Digital","Automação Industrial","Bosch",14,5,930.00),
        ("BOS009","Painel IHM 7 Polegadas","Automação Industrial","Bosch",5,2,2890.00),
        ("BOS010","Controlador Industrial","Automação Industrial","Bosch",9,3,3990.00),

        ("BOS011","Inversor de Frequência","Acionamentos","Bosch Rexroth",12,3,2850.00),
        ("BOS012","Soft Starter","Acionamentos","Bosch Rexroth",10,3,1890.00),
        ("BOS013","Drive Servo","Acionamentos","Bosch Rexroth",6,2,5990.00),
        ("BOS014","Conversor Industrial","Acionamentos","Bosch Rexroth",8,3,3290.00),
        ("BOS015","Controlador de Movimento","Acionamentos","Bosch Rexroth",4,2,7590.00),

        ("BOS016","Servo Motor 750W","Motores","Bosch Rexroth",7,2,6990.00),
        ("BOS017","Motor Trifásico","Motores","Bosch Rexroth",18,5,2590.00),
        ("BOS018","Motor Brushless","Motores","Bosch Rexroth",9,3,4990.00),
        ("BOS019","Motor Linear","Motores","Bosch Rexroth",3,1,11990.00),
        ("BOS020","Redutor Industrial","Motores","Bosch Rexroth",5,2,3890.00),

        ("BOS021","Fonte 24V 5A","Fontes","Bosch",28,5,329.90),
        ("BOS022","Fonte 24V 10A","Fontes","Bosch",19,5,489.90),
        ("BOS023","UPS Industrial","Fontes","Bosch",6,2,1890.00),
        ("BOS024","Fonte Modular","Fontes","Bosch",14,4,659.90),
        ("BOS025","Transformador Industrial","Fontes","Bosch",10,3,1290.00),

        ("BOS026","Leitor RFID","Identificação","Bosch",9,2,1590.00),
        ("BOS027","Tag RFID Industrial","Identificação","Bosch",120,20,35.90),
        ("BOS028","Scanner Código de Barras","Identificação","Bosch",11,3,890.00),
        ("BOS029","Impressora de Etiquetas","Identificação","Bosch",5,2,1990.00),
        ("BOS030","Terminal Coletor de Dados","Identificação","Bosch",8,2,3290.00),

    ]

    adicionados = 0

    for codigo, nome, categoria, fornecedor, quantidade, minimo, preco in produtos:

        existe = Produto.query.filter_by(codigo=codigo).first()

        if existe:
            continue

        produto = Produto(
            codigo=codigo,
            nome=nome,
            descricao=f"{nome} utilizado em ambiente industrial.",
            preco=preco,
            quantidade=quantidade,
            estoque_minimo=minimo,
            categoria=categorias_db[categoria],
            fornecedor=fornecedores_db[fornecedor]
        )

        db.session.add(produto)
        adicionados += 1

    db.session.commit()

    print("=" * 50)
    print("Banco populado com sucesso!")
    print(f"{adicionados} produtos adicionados.")
    print("=" * 50)