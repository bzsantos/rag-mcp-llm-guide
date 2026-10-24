from assistente_corporativo.services.agente_service import AgenteService

@router.post("/agente")
async def chat_agente(payload: PerguntaRequest, _usuario=Depends(usuario_atual)):
    service = AgenteService()
    return await service.processar(payload.pergunta)
