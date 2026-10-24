from assistente_corporativo.routers import chat
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
