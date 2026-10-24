#!/usr/bin/env bash
# Comandos usados no Capítulo 10

uv add psycopg2-binary

uv run python src/assistente_corporativo/playground/sql_puro.py

uv add "sqlalchemy[asyncio]" asyncpg

uv run python src/assistente_corporativo/playground/testar_sqlalchemy.py
