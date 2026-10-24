# src/assistente_corporativo/mcp_server/server.py
from mcp.server.fastmcp import FastMCP

from assistente_corporativo.mcp_server.tools_clientes import registrar_tools_clientes
from assistente_corporativo.mcp_server.tools_pedidos import registrar_tools_pedidos
from assistente_corporativo.mcp_server.resources_politicas import registrar_resources_politicas
from assistente_corporativo.mcp_server.prompts_relatorios import registrar_prompts_relatorios

mcp = FastMCP("assistente-corporativo")

registrar_tools_clientes(mcp)
registrar_tools_pedidos(mcp)
registrar_resources_politicas(mcp)
registrar_prompts_relatorios(mcp)

if __name__ == "__main__":
    mcp.run()
