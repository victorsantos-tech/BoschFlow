# BoschFlow

Sistema web de gerenciamento de estoque desenvolvido em Python utilizando Flask.

O BoschFlow simula um sistema de controle de estoque industrial, permitindo o gerenciamento de produtos, fornecedores, categorias e movimentações de entrada e saída.

O projeto foi desenvolvido com foco em desenvolvimento backend, integração com banco de dados e criação de uma aplicação web completa utilizando arquitetura organizada por módulos.


## Funcionalidades

### Autenticação

- Login de usuários
- Controle de sessão
- Usuário administrador


### Produtos

- Cadastro de produtos
- Edição e exclusão
- Pesquisa de produtos
- Controle de quantidade em estoque
- Definição de estoque mínimo
- Upload de imagens dos produtos


### Estoque

- Registro de entradas
- Registro de saídas
- Histórico de movimentações


### Cadastros

- Gerenciamento de categorias
- Gerenciamento de fornecedores


### Dashboard

Painel com informações do estoque:

- Quantidade de produtos cadastrados
- Quantidade de fornecedores
- Produtos com estoque crítico
- Valor total do estoque
- Indicadores de movimentação


### Relatórios

- Exportação de produtos em Excel
- Geração de relatórios em PDF


---

# Tecnologias utilizadas

## Backend

- Python
- Flask
- SQLAlchemy


## Banco de dados

- SQLite


## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap


## Bibliotecas

- OpenPyXL
- ReportLab
- Werkzeug


---

# Estrutura do projeto

```
BoschFlow/

├── app.py
├── config.py
├── database.py
├── criar_admin.py
├── popular_banco.py

├── models/
│   ├── produto.py
│   ├── usuario.py
│   ├── fornecedor.py
│   └── categoria.py

├── routes/
│   ├── produtos.py
│   ├── fornecedores.py
│   ├── categorias.py
│   └── movimentacoes.py

├── services/
│   └── pdf_service.py

├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/

├── screenshot/

└── requirements.txt
```

---

# Acesso de demonstração

Para testar o sistema:

```
Email:
demo@boschflow.com

Senha:
boschflow123
```

---

# Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/victorsantos-tech/BoschFlow.git
```

Entre na pasta:

```bash
cd BoschFlow
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python app.py
```

Acesse:

```
http://127.0.0.1:5000
```

---

# Screenshots

## Login

![Login](screenshot/login.png)


## Dashboard

![Dashboard](screenshot/dashboard.png)


## Produtos

![Produtos](screenshot/produtos.png)


## Cadastro de Produto

![Cadastro](screenshot/cadastro.png)


## Controle de Estoque

![Estoque](screenshot/estoque.png)


---

# Objetivo do projeto

Projeto desenvolvido para praticar desenvolvimento de aplicações web completas, envolvendo backend, banco de dados, autenticação, gerenciamento de estoque e criação de interfaces administrativas.

---

# Autor

**Victor Santos**

Engenharia de Software