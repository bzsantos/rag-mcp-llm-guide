from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.models.cliente import Cliente
from assistente_corporativo.schemas.cliente import ClienteCreate


class ClienteRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def criar(self, dados: ClienteCreate) -> Cliente:
        cliente = Cliente(nome=dados.nome, email=dados.email)
        self.db.add(cliente)
        await self.db.commit()
        await self.db.refresh(cliente)
        return cliente

    async def obter_por_id(self, cliente_id: int) -> Cliente | None:
        resultado = await self.db.execute(select(Cliente).where(Cliente.id == cliente_id))
        return resultado.scalar_one_or_none()

    async def listar(self) -> list[Cliente]:
        resultado = await self.db.execute(select(Cliente))
        return list(resultado.scalars().all())
