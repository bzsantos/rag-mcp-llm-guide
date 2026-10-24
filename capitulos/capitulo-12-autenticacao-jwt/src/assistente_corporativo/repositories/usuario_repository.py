from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.models.usuario import Usuario


class UsuarioRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def obter_por_email(self, email: str) -> Usuario | None:
        resultado = await self.db.execute(select(Usuario).where(Usuario.email == email))
        return resultado.scalar_one_or_none()

    async def criar(self, email: str, senha_hash: str) -> Usuario:
        usuario = Usuario(email=email, senha_hash=senha_hash)
        self.db.add(usuario)
        await self.db.commit()
        await self.db.refresh(usuario)
        return usuario
