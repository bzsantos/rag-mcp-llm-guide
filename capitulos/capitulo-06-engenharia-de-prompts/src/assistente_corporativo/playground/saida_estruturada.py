import json

import ollama
from pydantic import BaseModel, ValidationError

client = ollama.Client(host="http://localhost:11434")


class ResumoContrato(BaseModel):
    prazo_vigencia: str
    valor_mensal: float | None
    permite_rescisao_antecipada: bool
    observacoes: str


documento = """
Contrato com vigência de 12 meses, valor mensal de R$ 3.500,00, podendo ser
rescindido a qualquer momento mediante aviso prévio de 30 dias.
"""

prompt = f"""Extraia as informações do contrato abaixo e responda APENAS com um
JSON válido, sem nenhum texto antes ou depois, seguindo exatamente estas chaves:
prazo_vigencia (string), valor_mensal (número ou null), permite_rescisao_antecipada
(true/false), observacoes (string).

Contrato:
\"\"\"{documento}\"\"\"
"""

resposta_bruta = client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])
texto = resposta_bruta["message"]["content"]

print("Resposta bruta do modelo:")
print(texto)

try:
    dados = json.loads(texto)
    resumo = ResumoContrato.model_validate(dados)
    print("\nValidado com sucesso:", resumo)
except (json.JSONDecodeError, ValidationError) as erro:
    print("\nFALHOU AO VALIDAR:", erro)
