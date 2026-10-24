#!/usr/bin/env bash
# Comandos usados no Capítulo 3

docker --version
docker run hello-world

docker run -d \
  --name assistente_postgres \
  -e POSTGRES_USER=assistente \
  -e POSTGRES_PASSWORD=assistente \
  -e POSTGRES_DB=assistente_db \
  -p 5432:5432 \
  postgres:16

docker run -d \
  --name assistente_qdrant \
  -p 6333:6333 -p 6334:6334 \
  qdrant/qdrant:latest

docker run -d \
  --name assistente_ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  ollama/ollama:latest

docker exec -it assistente_ollama ollama pull llama3.2:3b

docker exec -it assistente_ollama ollama run llama3.2:3b "Explique o que é uma API em uma frase."

docker exec -it assistente_ollama ollama pull nomic-embed-text

docker rm -f assistente_postgres assistente_qdrant assistente_ollama

docker compose up -d
docker compose ps

docker exec -it assistente_ollama ollama list
# NAME                  ...
# llama3.2:3b           ...
# nomic-embed-text      ...
