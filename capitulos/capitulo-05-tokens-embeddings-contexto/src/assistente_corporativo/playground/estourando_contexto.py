import ollama

client = ollama.Client(host="http://localhost:11434")

texto_gigante = "Isso é um teste de contexto. " * 20000  # bem mais do que o modelo suporta

resposta = client.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": f"{texto_gigante}\n\nResuma o texto acima em uma frase."}],
)
print(resposta["message"]["content"])
