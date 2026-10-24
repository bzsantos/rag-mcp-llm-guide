from mcp.server.fastmcp import FastMCP

from assistente_corporativo.db.session import AsyncSessionLocal


def registrar_tools_pedidos(mcp: FastMCP) -> None:
    @mcp.tool()
    async def criar_pedido(cliente_id: int, produto: str, quantidade: int) -> dict:
        """Cria um novo pedido para o cliente informado. Retorna o ID do pedido criado."""
        if quantidade <= 0:
            return {"erro": "Quantidade deve ser maior que zero."}
        # Nesta versão simplificada, apenas simulamos a criação — em um projeto real,
        # existiria um PedidoRepository seguindo o mesmo padrão do ClienteRepository.
        return {"pedido_id": 999, "status": "criado (simulado)"}
