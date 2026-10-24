import math

import ollama

client = ollama.Client(host="http://localhost:11434")


def gerar_embedding(texto: str) -> list[float]:
    return client.embeddings(model="nomic-embed-text", prompt=texto)["embedding"]


def similaridade_cosseno(a: list[float], b: list[float]) -> float:
    produto_escalar = sum(x * y for x, y in zip(a, b))
    norma_a = math.sqrt(sum(x * x for x in a))
    norma_b = math.sqrt(sum(y * y for y in b))
    return produto_escalar / (norma_a * norma_b)


frase_base = "Quantos dias de férias eu tenho?"
frase_parecida = "Funcionário pode tirar férias?"
frase_diferente = "Qual o cardápio do restaurante?"

v_base = gerar_embedding(frase_base)
v_parecida = gerar_embedding(frase_parecida)
v_diferente = gerar_embedding(frase_diferente)

print("Similaridade (parecida):", similaridade_cosseno(v_base, v_parecida))
print("Similaridade (diferente):", similaridade_cosseno(v_base, v_diferente))
