FROM python:3.13-slim

RUN pip install --no-cache-dir uv

WORKDIR /code
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY src ./src
COPY migrations ./migrations
COPY alembic.ini ./

CMD ["uv", "run", "uvicorn", "assistente_corporativo.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]
