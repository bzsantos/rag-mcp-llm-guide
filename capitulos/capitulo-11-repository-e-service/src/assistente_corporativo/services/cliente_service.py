from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.repositories.cliente_repository import ClienteRepository
from assistente_corporativo.schemas.cliente import ClienteCreate


class ClienteService:
    def __init__(self, db: AsyncSession):
        self.repo = ClienteRepository(db)

    async def criar(self, dados: ClienteCreate):
        return await self.repo.criar(dados)

    async def obter(self, cliente_id: int):
        return await self.repo.obter_por_id(cliente_id)

    async def listar(self):
        return await self.repo.listar()
