# fastAPI_zero 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-purple)
![Alembic](https://img.shields.io/badge/Alembic-migrations-orange)

Gerenciador de tarefas com autenticação de usuários e operações CRUD completas, construído com FastAPI.

Projeto desenvolvido no curso FastAPI do Zero - Dunossauro.

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
