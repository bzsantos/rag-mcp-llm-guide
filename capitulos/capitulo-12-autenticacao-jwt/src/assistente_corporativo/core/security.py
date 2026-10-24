from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)


from datetime import datetime, timedelta, timezone

from jose import jwt

JWT_SECRET_KEY = "troque-esta-chave-em-producao"  # no Capítulo 26, isso vira variável de ambiente
JWT_ALGORITHM = "HS256"


def criar_access_token(sub: str, expires_minutes: int = 60) -> str:
    expira = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload = {"sub": sub, "exp": expira}
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def decodificar_token(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
