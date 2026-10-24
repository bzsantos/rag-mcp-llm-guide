# Assistente Inteligente Corporativo — Projeto Final

Aplicação completa construída ao longo do livro: FastAPI + PostgreSQL + Qdrant + Ollama + MCP,
com front-end em React.

## Pré-requisitos

- Python 3.13+, [uv](https://docs.astral.sh/uv/), Node.js 18+, Docker Desktop.

## 1. Subir a infraestrutura

```bash
cd backend
cp .env.example .env
docker compose up -d postgres qdrant ollama
docker exec -it assistente_ollama ollama pull llama3.2:3b
docker exec -it assistente_ollama ollama pull nomic-embed-text
```

## 2. Rodar o backend

```bash
cd backend
uv sync
uv run alembic upgrade head   # cria as tabelas (requer migrations configuradas — Capítulo 26)
uv run uvicorn assistente_corporativo.main:app --reload --app-dir src
```

A API sobe em <http://localhost:8000> (documentação interativa em `/docs`).

Para rodar os testes automatizados (Capítulo 13):

```bash
uv run pytest -v
```

## 3. Rodar o front-end

```bash
cd frontend
npm install
npm run dev
```

Acesse <http://localhost:5173>, registre um usuário via `/docs` do backend (ou crie um endpoint
de registro na tela, como exercício) e faça login.

## 4. Servidor MCP

O servidor MCP (Capítulos 20-25) é iniciado automaticamente pelo backend quando o agente
(`/chat/agente`) precisa consultar uma ferramenta — não é necessário subir um processo separado
manualmente. Para testá-lo isoladamente com o MCP Inspector:

```bash
cd backend
uv run mcp dev src/assistente_corporativo/mcp_server/server.py
```

## Estrutura

```
backend/
├── src/assistente_corporativo/
│   ├── main.py               # ponto de entrada FastAPI
│   ├── core/                  # config, segurança, exceções
│   ├── db/                    # conexão com PostgreSQL
│   ├── models/                # tabelas (SQLAlchemy)
│   ├── schemas/                # contratos da API (Pydantic)
│   ├── repositories/           # acesso a dados
│   ├── services/                # regras de negócio (RAG, agente, auth...)
│   ├── routers/                 # endpoints FastAPI
│   ├── rag/                     # embeddings, Qdrant, chunking, resiliência
│   └── mcp_server/              # servidor e cliente MCP (tools, resources, prompts)
├── tests/                        # pytest (unitários + integração)
├── migrations/                   # Alembic
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml

frontend/
├── src/
│   ├── App.jsx
│   ├── pages/ (Login.jsx, Chat.jsx)
│   └── services/api.js
└── package.json
```

## Nota importante

Este projeto é o **material didático** do livro — construído para ensinar, não para produção
irrestrita. O Capítulo 28 ("Próximos Passos") lista explicitamente o que falta para um ambiente
de produção real (indexação em background, observabilidade, multi-tenant reforçado, etc.).
