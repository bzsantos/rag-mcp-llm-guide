from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.db.session import get_db_session
from assistente_corporativo.schemas.usuario import UsuarioCreate, UsuarioRead
from assistente_corporativo.services.auth_service import AuthService

router = APIRouter()


@router.post("/registrar", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)
async def registrar(payload: UsuarioCreate, db: AsyncSession = Depends(get_db_session)):
    service = AuthService(db)
    if await service.repo.obter_por_email(payload.email):
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    return await service.registrar(payload)


from fastapi.security import OAuth2PasswordRequestForm

from assistente_corporativo.core.security import criar_access_token

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db_session)):
    service = AuthService(db)
    usuario = await service.autenticar(form.username, form.password)
    if usuario is None:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"access_token": criar_access_token(sub=str(usuario.id)), "token_type": "bearer"}


from assistente_corporativo.core.deps import usuario_atual

@router.get("/me", response_model=UsuarioRead)
async def meu_perfil(usuario=Depends(usuario_atual)):
    return usuario
