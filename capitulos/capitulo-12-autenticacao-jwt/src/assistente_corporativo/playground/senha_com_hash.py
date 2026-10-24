from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

senha_hash = pwd_context.hash("senha123")
print("Hash salvo no banco:", senha_hash)

print("Senha correta confere?", pwd_context.verify("senha123", senha_hash))
print("Senha errada confere?", pwd_context.verify("outrasenha", senha_hash))
