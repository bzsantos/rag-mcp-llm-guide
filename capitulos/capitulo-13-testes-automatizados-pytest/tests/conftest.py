import pytest
from httpx import ASGITransport, AsyncClient

from assistente_corporativo.main import app


@pytest.fixture
async def cliente_http():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


import uuid


@pytest.fixture
def email_unico():
    """Gera um e-mail diferente a cada execução, evitando colisão com dados de execuções anteriores."""
    return f"pytest-{uuid.uuid4().hex[:8]}@empresa.com"
