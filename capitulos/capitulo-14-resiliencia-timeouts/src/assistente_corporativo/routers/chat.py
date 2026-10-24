from fastapi import HTTPException

from assistente_corporativo.core.exceptions import ServicoIndisponivelError

@router.post("/")
async def chat(payload: PerguntaRequest, _usuario=Depends(usuario_atual)):
    service = RagService()
    try:
        return await service.responder(payload.pergunta)
    except ServicoIndisponivelError as erro:
        raise HTTPException(status_code=503, detail=str(erro))
