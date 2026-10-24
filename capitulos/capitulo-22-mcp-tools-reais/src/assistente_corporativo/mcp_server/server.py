from mcp.server.fastmcp import FastMCP

from assistente_corporativo.mcp_server.tools_clientes import registrar_tools_clientes

mcp = FastMCP("assistente-corporativo")
registrar_tools_clientes(mcp)

if __name__ == "__main__":
    mcp.run()
