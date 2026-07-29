from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
)


class PDFService:

    @staticmethod
    def gerar_produtos(produtos):

        buffer = BytesIO()

        pdf = SimpleDocTemplate(
            buffer,
            pagesize=A4
        )

        dados = [[
            "Código",
            "Nome",
            "Categoria",
            "Fornecedor",
            "Qtd",
            "Preço"
        ]]

        for produto in produtos:

            dados.append([

                produto.codigo,

                produto.nome,

                produto.categoria.nome,

                produto.fornecedor.nome,

                produto.quantidade,

                f"R$ {produto.preco:.2f}"

            ])

        tabela = Table(dados)

        tabela.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0d6efd")),

                ("TEXTCOLOR",(0,0),(-1,0),colors.white),

                ("GRID",(0,0),(-1,-1),1,colors.grey),

                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

                ("BOTTOMPADDING",(0,0),(-1,0),12),

                ("BACKGROUND",(0,1),(-1,-1),colors.beige),

            ])

        )

        pdf.build([tabela])

        buffer.seek(0)

        return buffer