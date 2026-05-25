![Python](https://img.shields.io/badge/Python-3.13-4CAF50?style=flat-square&logo=python&logoColor=white&labelColor=2d6a4f&color=4CAF50)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-7C6BBB?style=flat-square&logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-F5A623?style=flat-square&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-grey?style=flat-square&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=flat-square&logo=poetry&logoColor=white)

# fast_zero 🚀

Gerenciador de tarefas com autenticação de usuários e operações CRUD completas, construído com FastAPI. Projeto desenvolvido como parte do curso FastAPI do Zero - Dunossauro.
> 🚧 Em desenvolvimento — novas funcionalidades sendo adicionadas conforme o curso avança.

---

## Stack

| Camada | Tecnologia |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Validação | Pydantic |
| Banco de dados | SQLite |
| Gerenciador de pacotes | Poetry |
| Testes | pytest + coverage |

---

## Como rodar localmente

```bash
# clone o repositório
git clone https://github.com/geovanavenera/fast_zero
cd fast_zero

# instale as dependências
poetry install

# ative o ambiente virtual
poetry shell

# configure as variáveis de ambiente
cp .env.example .env

# rode as migrations
alembic upgrade head

# inicie o servidor
fastapi dev fast_zero/app.py
```

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL="sqlite:///database.db"
```

---

## Endpoints

### Usuários

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | health check |
| `POST` | `/users/` | criar usuário |
| `GET` | `/users/` | listar usuários |
| `PUT` | `/users/{id}` | atualizar usuário |
| `DELETE` | `/users/{id}` | deletar usuário |

---

## Testes

```bash
task test
```

---

Feito por [@geovanavenera](https://github.com/geovanavenera) 
