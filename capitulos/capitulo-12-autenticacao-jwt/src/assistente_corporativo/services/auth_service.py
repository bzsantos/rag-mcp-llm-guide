from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.core.security import gerar_hash_senha, verificar_senha
from assistente_corporativo.repositories.usuario_repository import UsuarioRepository
from assistente_corporativo.schemas.usuario import UsuarioCreate


class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UsuarioRepository(db)

    async def registrar(self, dados: UsuarioCreate):
        senha_hash = gerar_hash_senha(dados.senha)
        return await self.repo.criar(email=dados.email, senha_hash=senha_hash)

    async def autenticar(self, email: str, senha: str):
        usuario = await self.repo.obter_por_email(email)
        if usuario is None or not verificar_senha(senha, usuario.senha_hash):
            return None
        return usuario
