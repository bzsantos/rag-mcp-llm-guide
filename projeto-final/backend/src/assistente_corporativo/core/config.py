from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    qdrant_url: str = "http://localhost:6333"
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2:3b"
    ollama_embed_model: str = "nomic-embed-text"
    jwt_secret_key: str
    jwt_expire_minutes: int = 60
    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
