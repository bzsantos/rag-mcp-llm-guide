import tiktoken

tokenizador = tiktoken.get_encoding("cl100k_base")

textos = [
    "Olá",
    "computador",
    "SuperQuantumDatabaseX",
    "Funcionários possuem direito a 30 dias de férias anuais.",
]

for texto in textos:
    tokens = tokenizador.encode(texto)
    pedacos = [tokenizador.decode([t]) for t in tokens]
    print(f"{texto!r:60} -> {len(tokens)} tokens -> {pedacos}")
