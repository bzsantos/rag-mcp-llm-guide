#!/usr/bin/env bash
# Comandos usados no Capítulo 26

uv add pydantic-settings

uv add alembic
uv run alembic init migrations

uv run alembic revision --autogenerate -m "cria tabelas iniciais"
uv run alembic upgrade head
