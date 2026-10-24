from mcp.server.fastmcp import FastMCP


def registrar_prompts_relatorios(mcp: FastMCP) -> None:
    @mcp.prompt()
    def gerar_relatorio_executivo(cliente_nome: str, periodo: str) -> str:
        """Template para gerar um relatório executivo resumido de um cliente."""
        return f"""Você é um analista de negócios. Gere um relatório executivo sobre
o cliente "{cliente_nome}" referente ao período "{periodo}", cobrindo:

1. Resumo das interações no período;
2. Pontos de atenção identificados;
3. Recomendações objetivas (máximo 3 itens).

Seja direto — o relatório será lido por diretores com pouco tempo disponível."""
