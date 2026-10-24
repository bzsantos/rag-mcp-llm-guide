#!/usr/bin/env bash
# Comandos usados no Capítulo 8

uv add fastapi "uvicorn[standard]"

uv run uvicorn assistente_corporativo.main:app --reload --app-dir src

mkdir -p src/assistente_corporativo/{core,db,models,schemas,repositories,services,routers}
touch src/assistente_corporativo/{core,db,models,schemas,repositories,services,routers}/__init__.py
