usuarios_fake = {}


def registrar(email: str, senha: str):
    usuarios_fake[email] = {"senha": senha}  # 🚨 nunca faça isto de verdade


registrar("admin@empresa.com", "senha123")
print(usuarios_fake)
# {'admin@empresa.com': {'senha': 'senha123'}}
