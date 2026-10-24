# src/assistente_corporativo/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from assistente_corporativo.core.config import get_settings
from assistente_corporativo.routers import auth, chat, clientes, documentos


@asynccontextmanager
async def lifespan(app: FastAPI):
    # aqui entrariam rotinas de inicialização (ex.: garantir coleção do Qdrant)
    yield


app = FastAPI(title="Assistente Inteligente Corporativo", version="1.0.0", lifespan=lifespan)

settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(documentos.router, prefix="/documentos", tags=["Documentos"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])


@app.get("/health", tags=["Infra"])
async def health_check():
    return {"status": "ok"}
