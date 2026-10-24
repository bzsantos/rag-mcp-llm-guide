import json

import ollama

from assistente_corporativo.mcp_server.client import obter_sessao_mcp
from assistente_corporativo.rag.rag_service import RagService

client = ollama.Client(host="http://localhost:11434")


class AgenteService:
    def __init__(self):
        self.rag_service = RagService()

    async def _decidir_acao(self, pergunta: str, tools_schema: list[dict]) -> dict:
        descricoes = "\n".join(f"- {t['function']['name']}: {t['function']['description']}" for t in tools_schema)
        prompt = f"""Você decide se uma pergunta deve ser respondida com uma ferramenta
(Tool) ou com busca em documentos (RAG).

Ferramentas disponíveis:
{descricoes}

Pergunta do usuário: "{pergunta}"

Responda APENAS com um JSON no formato:
{{"usar_tool": true|false, "tool_nome": "<nome ou null>", "argumentos": {{...}} }}"""

        resposta = client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])
        try:
            return json.loads(resposta["message"]["content"])
        except json.JSONDecodeError:
            return {"usar_tool": False}  # degradação graciosa (Capítulo 6)

    async def processar(self, pergunta: str) -> dict:
        async with obter_sessao_mcp() as sessao:
            tools_disponiveis = await sessao.list_tools()
            tools_schema = [
                {"type": "function", "function": {"name": t.name, "description": t.description, "parameters": t.inputSchema}}
                for t in tools_disponiveis.tools
            ]

            decisao = await self._decidir_acao(pergunta, tools_schema)

            if decisao.get("usar_tool"):
                resultado_tool = await sessao.call_tool(decisao["tool_nome"], arguments=decisao.get("argumentos", {}))
                resposta_final = client.chat(
                    model="llama3.2:3b",
                    messages=[{
                        "role": "user",
                        "content": f"Pergunta: {pergunta}\nResultado da ferramenta: {resultado_tool.content}\nFormule a resposta final em português.",
                    }],
                )
                return {"resposta": resposta_final["message"]["content"], "fonte": "tool", "tool_utilizada": decisao["tool_nome"]}

            return {**await self.rag_service.responder(pergunta), "fonte": "rag"}
