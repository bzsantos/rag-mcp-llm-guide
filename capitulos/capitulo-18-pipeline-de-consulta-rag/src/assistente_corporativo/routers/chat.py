from fastapi import APIRouter, Depends
from pydantic import BaseModel

from assistente_corporativo.core.deps import usuario_atual
from assistente_corporativo.rag.rag_service import RagService

router = APIRouter()


class PerguntaRequest(BaseModel):
    pergunta: str


@router.post("/")
async def chat(payload: PerguntaRequest, _usuario=Depends(usuario_atual)):
    service = RagService()
    return await service.responder(payload.pergunta)
