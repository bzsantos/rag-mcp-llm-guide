import pytest

from assistente_corporativo.schemas.cliente import ClienteCreate
from assistente_corporativo.services.cliente_service import ClienteService


class ClienteRepositoryFalso:
    """Repository falso: não toca em nenhum banco real. Guarda tudo em uma lista em memória."""

    def __init__(self):
        self.clientes_salvos = []
        self._proximo_id = 1

    async def criar(self, dados: ClienteCreate):
        cliente_fake = type("ClienteFake", (), {
            "id": self._proximo_id, "nome": dados.nome, "email": dados.email,
        })()
        self.clientes_salvos.append(cliente_fake)
        self._proximo_id += 1
        return cliente_fake


@pytest.mark.asyncio
async def test_criar_cliente_chama_repository_corretamente():
    service = ClienteService.__new__(ClienteService)  # cria sem rodar __init__ (que exige AsyncSession real)
    service.repo = ClienteRepositoryFalso()

    dados = ClienteCreate(nome="Empresa Teste", email="teste@empresa.com")
    cliente_criado = await service.criar(dados)

    assert cliente_criado.nome == "Empresa Teste"
    assert cliente_criado.email == "teste@empresa.com"
    assert len(service.repo.clientes_salvos) == 1
