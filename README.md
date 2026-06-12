![Python](https://img.shields.io/badge/Python-3.13-4CAF50?style=flat-square&logo=python&logoColor=white&labelColor=2d6a4f&color=4CAF50)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-7C6BBB?style=flat-square&logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-F5A623?style=flat-square&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-grey?style=flat-square&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-em_breve-lightgrey?style=flat-square&logo=docker&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=flat-square&logo=poetry&logoColor=white)

# fastapi_zero 🚀

Gerenciador de tarefas com autenticação de usuários e operações CRUD completas, construído com FastAPI. Projeto desenvolvido como parte do curso [FastAPI do Zero - Dunossauro](https://fastapidozero.dunossauro.com).

> 🚧 **Em desenvolvimento** — novas funcionalidades sendo adicionadas conforme o curso avança.

---

## ✨ Funcionalidades

- ✅ Cadastro e gerenciamento de usuários
- ✅ Autenticação com JWT (Bearer Token)
- ✅ Endpoints protegidos por autenticação
- ✅ Operações CRUD completas
- ✅ Testes automatizados com cobertura de código
- ✅ Routers separados por domínio (users / auth)
- ✅ Paginação com validação via Pydantic
- 🔜 Gerenciamento de tarefas
- 🔜 Containerização com Docker
- 🔜 Deploy com PostgreSQL

---

## 🗂️ Stack

| Camada              | Tecnologia                        |
|---------------------|-----------------------------------|
| Framework           | FastAPI                           |
| ORM                 | SQLAlchemy                        |
| Migrations          | Alembic                           |
| Validação           | Pydantic                          |
| Banco de dados      | SQLite (PostgreSQL em breve)      |
| Autenticação        | JWT (PyJWT)                       |
| Gerenciador         | Poetry                            |
| Testes              | pytest + coverage                 |

---

## 🚀 Como rodar localmente

```bash
# clone o repositório
git clone https://github.com/geovanavenera/fastAPI_zero
cd fastAPI_zero

# instale as dependências
poetry install

# ative o ambiente virtual
poetry shell

# configure as variáveis de ambiente
cp .env.example .env

# rode as migrations
alembic upgrade head

# inicie o servidor
fastapi dev fastapi_zero/app.py
```

---

## ⚙️ Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL="sqlite:///database.db"
SECRET_KEY="sua-chave-secreta"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> 💡 Gere uma `SECRET_KEY` segura com `python -c "import secrets; print(secrets.token_hex(32))"`

---

## 📡 Endpoints

### Autenticação
| Método | Rota           | Descrição          |
|--------|----------------|--------------------|
| `POST` | `/auth/token`  | gerar access token |

### Usuários
| Método   | Rota           | Descrição          | Auth |
|----------|----------------|--------------------|------|
| `GET`    | `/`            | health check       | ❌   |
| `POST`   | `/users/`      | criar usuário      | ❌   |
| `GET`    | `/users/`      | listar usuários    | ❌   |
| `PUT`    | `/users/{id}`  | atualizar usuário  | ✅   |
| `DELETE` | `/users/{id}`  | deletar usuário    | ✅   |

---

## 🧪 Testes

```bash
task test
```

Cobertura de código gerada automaticamente em `htmlcov/index.html`.

---

## 📁 Estrutura do projeto
fastAPI_zero/
├── fastapi_zero/
│   ├── app.py          # rotas e endpoints
│   ├── models.py       # modelos do banco de dados
│   ├── schemas.py      # schemas Pydantic
│   ├── security.py     # autenticação JWT
│   ├── database.py     # configuração do banco
│   └── settings.py     # variáveis de ambiente
├── routers/            # rotas e endpoints
    ├── users.py
    ├── auth.py
├── migrations/         # Alembic migrations
├── tests/              # testes automatizados
    ├── conftest.py
    ├── test_app.py
    ├── test.auth.py
    ├── test_users.py
    ├── test_security.py
├── pyproject.toml
└── .env.example
---

Feito por [@geovanavenera](https://github.com/geovanavenera)
