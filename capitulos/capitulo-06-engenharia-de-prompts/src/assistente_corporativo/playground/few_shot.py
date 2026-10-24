import ollama

client = ollama.Client(host="http://localhost:11434")

def classificar_sem_exemplos(comentario: str) -> str:
    prompt = f'Classifique o sentimento como POSITIVO, NEGATIVO ou NEUTRO: "{comentario}"'
    return client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])["message"]["content"]


def classificar_com_exemplos(comentario: str) -> str:
    prompt = f"""Classifique o sentimento do comentário como POSITIVO, NEGATIVO ou NEUTRO.
Responda APENAS com a palavra da classificação, nada mais.

Comentário: "Entrega rápida e produto de ótima qualidade."
Sentimento: POSITIVO

Comentário: "O produto chegou quebrado e o suporte não respondeu."
Sentimento: NEGATIVO

Comentário: "Recebi o produto conforme descrito no anúncio."
Sentimento: NEUTRO

Comentário: "{comentario}"
Sentimento:"""
    return client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])["message"]["content"]


comentario_teste = "Achei ok, nada excepcional, mas cumpriu o prometido."

print("SEM exemplos:", classificar_sem_exemplos(comentario_teste))
print("COM exemplos:", classificar_com_exemplos(comentario_teste))
