import ollama

from assistente_corporativo.rag.qdrant_client import buscar_similares

client = ollama.Client(host="http://localhost:11434")

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
        return client.embeddings(model="nomic-embed-text", prompt=texto)["embedding"]

    def montar_contexto(self, pergunta: str) -> tuple[str, list[dict]]:
        vetor = self._gerar_embedding(pergunta)
        resultados = buscar_similares(vetor, top_k=self.top_k)
        if not resultados:
            return "Nenhum documento relevante foi encontrado.", []
        blocos = [f"[Fonte: {r.get('metadados', {}).get('nome_arquivo', '?')}]\n{r['texto']}" for r in resultados]
        return "\n\n---\n\n".join(blocos), resultados

    async def responder(self, pergunta: str) -> dict:
        contexto, fontes = self.montar_contexto(pergunta)
        prompt = PROMPT_RAG.format(contexto=contexto, pergunta=pergunta)
        resposta = client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])
        return {
            "resposta": resposta["message"]["content"],
            "fontes": [f.get("metadados", {}).get("nome_arquivo") for f in fontes],
        }
