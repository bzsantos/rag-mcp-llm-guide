# src/assistente_corporativo/mcp_server/client.py
from contextlib import asynccontextmanager

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PARAMS = StdioServerParameters(
    command="uv",
    args=["run", "python", "src/assistente_corporativo/mcp_server/server.py"],
)


@asynccontextmanager
async def obter_sessao_mcp():
    async with stdio_client(SERVER_PARAMS) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session
