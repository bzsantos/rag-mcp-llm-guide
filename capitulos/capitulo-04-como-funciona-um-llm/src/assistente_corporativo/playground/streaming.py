import ollama

client = ollama.Client(host="http://localhost:11434")

stream = client.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": "Conte até 5, escrevendo por extenso."}],
    stream=True,
)

for pedaco in stream:
    print(pedaco["message"]["content"], end="", flush=True)
