import ollama

client = ollama.Client(host="http://localhost:11434", timeout=15.0)  # nunca espera mais que 15s


import httpx


class RagService:
    ...
    async def responder(self, pergunta: str) -> dict:
        contexto, fontes = self.montar_contexto(pergunta)
        prompt = PROMPT_RAG.format(contexto=contexto, pergunta=pergunta)
        try:
            resposta = client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])
        except (httpx.ConnectError, httpx.TimeoutException) as erro:
            raise ServicoIndisponivelError("O assistente de IA está indisponível no momento.") from erro

        return {
            "resposta": resposta["message"]["content"],
            "fontes": [f.get("metadados", {}).get("nome_arquivo") for f in fontes],
        }


from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

class RagService:
    ...
    @retry(
        retry=retry_if_exception_type((httpx.ConnectError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=8),
        reraise=True,
    )
    def _chamar_llm(self, prompt: str) -> str:
        resposta = client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])
        return resposta["message"]["content"]
