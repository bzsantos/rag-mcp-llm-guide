from assistente_corporativo.core.config import get_settings

settings = get_settings()
JWT_SECRET_KEY = settings.jwt_secret_key
