from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.core.security import decodificar_token
from assistente_corporativo.db.session import get_db_session
from assistente_corporativo.repositories.usuario_repository import UsuarioRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def usuario_atual(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db_session)):
    erro = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    try:
        payload = decodificar_token(token)
        usuario_id = int(payload["sub"])
    except (JWTError, KeyError, ValueError):
        raise erro

    repo = UsuarioRepository(db)
    usuario = await repo.obter_por_id(usuario_id) if hasattr(repo, "obter_por_id") else None
    if usuario is None:
        raise erro
    return usuario
