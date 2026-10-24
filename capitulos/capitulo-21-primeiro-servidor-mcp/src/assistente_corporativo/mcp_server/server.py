from mcp.server.fastmcp import FastMCP

mcp = FastMCP("assistente-corporativo")


@mcp.tool()
def saudacao(nome: str) -> str:
    """Retorna uma saudação personalizada para o nome informado."""
    return f"Olá, {nome}! Bem-vindo ao Assistente Corporativo."


if __name__ == "__main__":
    mcp.run()
