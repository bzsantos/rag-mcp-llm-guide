import ollama

client = ollama.Client(host="http://localhost:11434")

resposta = client.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": "O que é uma API, em uma frase?"}],
)

print(resposta["message"]["content"])
