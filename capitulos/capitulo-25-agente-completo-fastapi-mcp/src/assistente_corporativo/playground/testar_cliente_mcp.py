import asyncio

from assistente_corporativo.mcp_server.client import obter_sessao_mcp


async def main():
    async with obter_sessao_mcp() as sessao:
        tools = await sessao.list_tools()
        for t in tools.tools:
            print(f"- {t.name}: {t.description}")


asyncio.run(main())
