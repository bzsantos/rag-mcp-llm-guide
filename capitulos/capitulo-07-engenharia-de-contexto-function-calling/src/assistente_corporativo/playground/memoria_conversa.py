import ollama

client = ollama.Client(host="http://localhost:11434")

historico: list[dict] = [
    {"role": "system", "content": "Você é um assistente objetivo. Responda em português."}
]


def perguntar(pergunta: str) -> str:
    historico.append({"role": "user", "content": pergunta})
    resposta = client.chat(model="llama3.2:3b", messages=historico)
    texto = resposta["message"]["content"]
    historico.append({"role": "assistant", "content": texto})
    return texto


print(perguntar("Meu nome é Bruno e eu trabalho com pesquisa acadêmica."))
print(perguntar("Qual é o meu nome, e com o que eu trabalho?"))
