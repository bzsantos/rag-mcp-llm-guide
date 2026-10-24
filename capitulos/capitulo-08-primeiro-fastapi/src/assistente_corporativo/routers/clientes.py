from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def listar_clientes():
    return [
        {"id": 1, "nome": "Empresa Acme"},
        {"id": 2, "nome": "Empresa Beta"},
    ]
