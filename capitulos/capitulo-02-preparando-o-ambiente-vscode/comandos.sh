#!/usr/bin/env bash
# Comandos usados no Capítulo 2

python3 --version

python3 --version
# Python 3.13.0

# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv --version
# uv 0.5.x

mkdir assistente-corporativo
cd assistente-corporativo
code .

uv init --package .

uv venv

uv run python src/assistente_corporativo/experimento.py
# Total: R$ 270.00
