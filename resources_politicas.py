from mcp.server.fastmcp import FastMCP

POLITICAS = {
    "ferias": "Funcionários possuem direito a 30 dias de férias anuais, após 12 meses de trabalho.",
    "reembolso": "Reembolsos de viagem devem ser solicitados em até 30 dias, com nota fiscal anexada.",
}


def registrar_resources_politicas(mcp: FastMCP) -> None:
    @mcp.resource("politica://{tema}")
    def obter_politica(tema: str) -> str:
        """Retorna o texto da política da empresa referente ao tema informado."""
        return POLITICAS.get(tema, f"Nenhuma política encontrada para o tema '{tema}'.")
