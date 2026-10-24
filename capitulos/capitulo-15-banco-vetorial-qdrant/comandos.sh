#!/usr/bin/env bash
# Comandos usados no Capítulo 15

uv add qdrant-client

uv run python src/assistente_corporativo/playground/criar_colecao.py

uv run python src/assistente_corporativo/playground/testar_qdrant.py
