import json

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")  # Ollama ignora a chave

estoque = {"notebook": 15, "mouse": 50, "teclado": 20}


def consultar_estoque(produto: str) -> int:
    """Função Python real — é isso que será executado quando o modelo 'chamar' a ferramenta."""
    return estoque.get(produto.lower(), 0)


tools = [
    {
        "type": "function",
        "function": {
            "name": "consultar_estoque",
            "description": "Consulta a quantidade disponível de um produto no estoque.",
            "parameters": {
                "type": "object",
                "properties": {"produto": {"type": "string", "description": "Nome do produto"}},
                "required": ["produto"],
            },
        },
    }
]

messages = [
    {"role": "system", "content": "Você é um assistente de vendas. Use ferramentas quando necessário."},
    {"role": "user", "content": "Vocês têm notebook disponível?"},
]

primeira_resposta = client.chat.completions.create(model="llama3.2:3b", messages=messages, tools=tools)
