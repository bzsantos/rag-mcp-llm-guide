import ollama

from assistente_corporativo.rag.qdrant_client import buscar_similares, garantir_colecao, inserir_chunk

client = ollama.Client(host="http://localhost:11434")


def gerar_embedding(texto: str) -> list[float]:
    return client.embeddings(model="nomic-embed-text", prompt=texto)["embedding"]


garantir_colecao()

frases = [
    "Funcionários possuem direito a 30 dias de férias anuais.",
    "O reembolso de viagens deve ser solicitado em até 30 dias.",
    "O cardápio do restaurante muda toda semana às segundas-feiras.",
]
for frase in frases:
    inserir_chunk(texto=frase, vetor=gerar_embedding(frase), metadados={"origem": "teste"})

pergunta = "Quantos dias de férias eu tenho?"
resultados = buscar_similares(gerar_embedding(pergunta), top_k=2)
for r in resultados:
    print(f"[{r['score']:.3f}] {r['texto']}")
