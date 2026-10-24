import ollama

client = ollama.Client(host="http://localhost:11434")

resposta = client.embeddings(model="nomic-embed-text", prompt="Olá, mundo!")
vetor = resposta["embedding"]

print(f"Tipo: {type(vetor)}")
print(f"Dimensões: {len(vetor)}")
print(f"Primeiros 5 valores: {vetor[:5]}")
