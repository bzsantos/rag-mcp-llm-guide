from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.db.session import get_db_session
from assistente_corporativo.models.cliente import Cliente
from assistente_corporativo.schemas.cliente import ClienteCreate, ClienteRead

router = APIRouter()


@router.post("/", response_model=ClienteRead, status_code=status.HTTP_201_CREATED)
async def criar_cliente(payload: ClienteCreate, db: AsyncSession = Depends(get_db_session)):
    cliente = Cliente(nome=payload.nome, email=payload.email)
    db.add(cliente)
    await db.commit()
    await db.refresh(cliente)
    return cliente


@router.get("/{cliente_id}", response_model=ClienteRead)
async def obter_cliente(cliente_id: int, db: AsyncSession = Depends(get_db_session)):
    resultado = await db.execute(select(Cliente).where(Cliente.id == cliente_id))
    cliente = resultado.scalar_one_or_none()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.db.session import get_db_session
from assistente_corporativo.schemas.cliente import ClienteCreate, ClienteRead
from assistente_corporativo.services.cliente_service import ClienteService

router = APIRouter()


@router.post("/", response_model=ClienteRead, status_code=status.HTTP_201_CREATED)
async def criar_cliente(payload: ClienteCreate, db: AsyncSession = Depends(get_db_session)):
    service = ClienteService(db)
    return await service.criar(payload)


@router.get("/{cliente_id}", response_model=ClienteRead)
async def obter_cliente(cliente_id: int, db: AsyncSession = Depends(get_db_session)):
    service = ClienteService(db)
    cliente = await service.obter(cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@router.get("/", response_model=list[ClienteRead])
async def listar_clientes(db: AsyncSession = Depends(get_db_session)):
    service = ClienteService(db)
    return await service.listar()
