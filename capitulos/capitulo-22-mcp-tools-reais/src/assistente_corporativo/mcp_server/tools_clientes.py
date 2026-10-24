from mcp.server.fastmcp import FastMCP

from assistente_corporativo.db.session import AsyncSessionLocal
from assistente_corporativo.repositories.cliente_repository import ClienteRepository


def registrar_tools_clientes(mcp: FastMCP) -> None:
    @mcp.tool()
    async def buscar_cliente_por_id(cliente_id: int) -> dict:
        """Busca os dados cadastrais de um cliente pelo ID no banco de dados."""
        async with AsyncSessionLocal() as session:
            repo = ClienteRepository(session)
            cliente = await repo.obter_por_id(cliente_id)
            if cliente is None:
                return {"erro": f"Cliente com id {cliente_id} não encontrado."}
            return {"id": cliente.id, "nome": cliente.nome, "email": cliente.email}
