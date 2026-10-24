#!/usr/bin/env bash
# Comandos usados no Capítulo 13

uv add --dev pytest pytest-asyncio httpx

uv run pytest -v

uv run pytest tests/test_cliente_service.py -v

uv run pytest tests/test_auth_api.py -v

uv run pytest tests/test_auth_api.py -v
