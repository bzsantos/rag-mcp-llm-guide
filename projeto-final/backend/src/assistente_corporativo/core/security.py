# src/assistente_corporativo/core/security.py
from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from assistente_corporativo.core.config import get_settings

settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)


def criar_access_token(sub: str, expires_minutes: int | None = None) -> str:
    expira = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes or settings.jwt_expire_minutes)
    payload = {"sub": sub, "exp": expira}
    return jwt.encode(payload, settings.jwt_secret_key, algorithm="HS256")


def decodificar_token(token: str) -> dict:
    return jwt.decode(token, settings.jwt_secret_key, algorithms=["HS256"])
