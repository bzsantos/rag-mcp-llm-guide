# src/assistente_corporativo/rag/rag_service.py
import json

import httpx
import ollama
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from assistente_corporativo.core.config import get_settings
from assistente_corporativo.core.exceptions import ServicoIndisponivelError
from assistente_corporativo.rag.circuit_breaker import CircuitBreaker
from assistente_corporativo.rag.qdrant_client import buscar_similares

settings = get_settings()
client = ollama.Client(host=settings.ollama_url, timeout=15.0)

_circuit_breaker = CircuitBreaker(max_falhas=3, tempo_reset_segundos=30)

PROMPT_RAG = """Você é o assistente corporativo da empresa. Responda à pergunta do
usuário utilizando APENAS as informações do CONTEXTO abaixo. Se a resposta não
estiver no contexto, diga claramente que não encontrou essa informação nos
documentos disponíveis — não invente.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

Responda em português, de forma objetiva, e cite o nome do arquivo-fonte entre
colchetes ao final de cada afirmação, ex.: [politica_rh.pdf]."""


class RagService:
    def __init__(self, top_k: int = 5):
        self.top_k = top_k

    def _gerar_embedding(self, texto: str) -> list[float]:
        return client.embeddings(model=settings.ollama_embed_model, prompt=texto)["embedding"]

    def montar_contexto(self, pergunta: str, cliente_id: int | None = None) -> tuple[str, list[dict]]:
        vetor = self._gerar_embedding(pergunta)
        resultados = buscar_similares(vetor, top_k=self.top_k, cliente_id=cliente_id)
        if not resultados:
            return "Nenhum documento relevante foi encontrado.", []
        blocos = [f"[Fonte: {r.get('metadados', {}).get('nome_arquivo', '?')}]\n{r['texto']}" for r in resultados]
        return "\n\n---\n\n".join(blocos), resultados

    @retry(
        retry=retry_if_exception_type((httpx.ConnectError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=8),
        reraise=True,
    )
    def _chamar_llm(self, prompt: str) -> str:
        resposta = client.chat(model=settings.ollama_model, messages=[{"role": "user", "content": prompt}])
        return resposta["message"]["content"]

    def _chamar_llm_protegido(self, prompt: str) -> str:
        if _circuit_breaker.circuito_aberto():
            raise ServicoIndisponivelError("O assistente de IA está temporariamente desativado após falhas consecutivas.")
        try:
            resultado = self._chamar_llm(prompt)
            _circuit_breaker.registrar_sucesso()
            return resultado
        except (httpx.ConnectError, httpx.TimeoutException):
            _circuit_breaker.registrar_falha()
            raise ServicoIndisponivelError("O assistente de IA está indisponível no momento.")

    async def responder(self, pergunta: str, cliente_id: int | None = None) -> dict:
        contexto, fontes = self.montar_contexto(pergunta, cliente_id)
        prompt = PROMPT_RAG.format(contexto=contexto, pergunta=pergunta)
        resposta_texto = self._chamar_llm_protegido(prompt)
        return {
            "resposta": resposta_texto,
            "fontes": [f.get("metadados", {}).get("nome_arquivo") for f in fontes],
        }

    async def buscar_com_hyde(self, pergunta: str) -> list[dict]:
        prompt_hipotetico = f"Escreva um parágrafo respondendo hipoteticamente: {pergunta}"
        resposta_hipotetica = self._chamar_llm_protegido(prompt_hipotetico)
        vetor = self._gerar_embedding(resposta_hipotetica)
        return buscar_similares(vetor, top_k=self.top_k)

    async def buscar_multi_query(self, pergunta: str) -> list[dict]:
        prompt = f'Gere 3 reformulações diferentes para a pergunta abaixo, uma por linha, sem numeração:\n\n{pergunta}'
        variacoes_texto = self._chamar_llm_protegido(prompt)
        variacoes = [pergunta] + [v.strip() for v in variacoes_texto.split("\n") if v.strip()]

        vistos: dict[str, dict] = {}
        for variacao in variacoes:
            vetor = self._gerar_embedding(variacao)
            for r in buscar_similares(vetor, top_k=self.top_k):
                chave = r["texto"]
                if chave not in vistos or r["score"] > vistos[chave]["score"]:
                    vistos[chave] = r
        return sorted(vistos.values(), key=lambda r: r["score"], reverse=True)[: self.top_k]
