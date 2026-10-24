from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/clientes")
def listar_clientes():
    clientes_fake = [
        {"id": 1, "nome": "Empresa Acme"},
        {"id": 2, "nome": "Empresa Beta"},
    ]
    return clientes_fake


@app.post("/clientes")
def criar_cliente(nome: str):
    return {"id": 3, "nome": nome}


from fastapi import FastAPI

from assistente_corporativo.routers import clientes

app = FastAPI(title="Assistente Inteligente Corporativo")

app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
