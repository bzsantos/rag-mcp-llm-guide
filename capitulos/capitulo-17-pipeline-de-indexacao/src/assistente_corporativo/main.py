from assistente_corporativo.routers import documentos
app.include_router(documentos.router, prefix="/documentos", tags=["Documentos"])
