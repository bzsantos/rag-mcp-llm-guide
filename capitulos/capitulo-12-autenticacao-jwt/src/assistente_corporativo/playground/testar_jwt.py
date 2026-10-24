from assistente_corporativo.core.security import criar_access_token, decodificar_token

token = criar_access_token(sub="42")
print("Token gerado:", token)

payload = decodificar_token(token)
print("Payload decodificado:", payload)
