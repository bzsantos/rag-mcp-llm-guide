from assistente_corporativo.routers import auth
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
