import math
import time

import ollama

client = ollama.Client(host="http://localhost:11434")


def gerar_embedding(texto: str) -> list[float]:
    return client.embeddings(model="nomic-embed-text", prompt=texto)["embedding"]


def similaridade_cosseno(a: list[float], b: list[float]) -> float:
    produto = sum(x * y for x, y in zip(a, b))
    return produto / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


documentos = [f"Documento número {i} sobre um assunto qualquer da empresa." for i in range(200)]

inicio = time.perf_counter()
vetores_documentos = [gerar_embedding(doc) for doc in documentos]
pergunta_vetor = gerar_embedding("Qual assunto está no documento 150?")

melhores = sorted(
    ((similaridade_cosseno(pergunta_vetor, v), i) for i, v in enumerate(vetores_documentos)),
    reverse=True,
)[:3]
fim = time.perf_counter()

print(f"Tempo total: {fim - inicio:.2f}s para {len(documentos)} documentos")
print("Top 3:", melhores)
