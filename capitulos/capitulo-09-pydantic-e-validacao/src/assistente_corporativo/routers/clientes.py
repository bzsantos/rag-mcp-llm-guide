from fastapi import APIRouter

from assistente_corporativo.schemas.cliente import ClienteCreate

router = APIRouter()


@router.get("/")
def listar_clientes():
    return [
        {"id": 1, "nome": "Empresa Acme"},
        {"id": 2, "nome": "Empresa Beta"},
    ]


@router.post("/")
def criar_cliente(payload: ClienteCreate):
    return {"id": 3, "nome": payload.nome, "email": payload.email}


from fastapi import APIRouter, status

from assistente_corporativo.schemas.cliente import ClienteCreate, ClienteRead

router = APIRouter()


@router.post("/", response_model=ClienteRead, status_code=status.HTTP_201_CREATED)
def criar_cliente(payload: ClienteCreate):
    return {"id": 3, "nome": payload.nome, "email": payload.email}
