import ollama

client = ollama.Client(host="http://localhost:11434")

for _ in range(2):
    resposta = client.chat(
        model="llama3.2:3b",
        messages=[{"role": "user", "content": "Complete a frase: o céu é da cor..."}],
    )
    print(resposta["message"]["content"])
    print("---")
