from assistente_corporativo.core.config import get_settings

settings = get_settings()
print(settings.database_url)
print(settings.ollama_model)
