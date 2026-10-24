import ollama

client = ollama.Client(host="http://localhost:11434")

documento = """
Contrato de prestação de serviços firmado entre Acme Ltda e João da Silva,
com vigência de 12 meses a partir de 01/01/2026, valor mensal de R$ 3.500,00,
rescisão mediante aviso prévio de 30 dias, foro da comarca de São Paulo/SP.
"""

prompt_ruim = f"Resuma isso: {documento}"

prompt_bom = f"""Você é um assistente jurídico. Resuma o contrato abaixo em até 4
tópicos, cobrindo exclusivamente: prazo, valor, rescisão e foro. Se alguma
informação não existir no texto, escreva "não informado". Responda em português.

Contrato:
\"\"\"{documento}\"\"\"
"""

for nome, prompt in [("RUIM", prompt_ruim), ("BOM", prompt_bom)]:
    resposta = client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])
    print(f"--- {nome} ---")
    print(resposta["message"]["content"])
    print()
