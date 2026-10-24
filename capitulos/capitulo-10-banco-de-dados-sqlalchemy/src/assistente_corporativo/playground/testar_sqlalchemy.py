import asyncio

from assistente_corporativo.db.base import Base
from assistente_corporativo.db.session import AsyncSessionLocal, engine
from assistente_corporativo.models.cliente import Cliente


async def main():
    async with engine.begin() as conexao:
        await conexao.run_sync(Base.metadata.create_all)  # cria as tabelas que ainda não existem

    async with AsyncSessionLocal() as session:
        novo_cliente = Cliente(nome="Empresa Beta", email="contato@beta.com")
        session.add(novo_cliente)
        await session.commit()
        await session.refresh(novo_cliente)
        print("Cliente criado com id:", novo_cliente.id)


asyncio.run(main())
