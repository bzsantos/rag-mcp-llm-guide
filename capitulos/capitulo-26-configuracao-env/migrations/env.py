from assistente_corporativo.db.base import Base
from assistente_corporativo.models import cliente, documento, usuario  # noqa: F401 — registra os models
from assistente_corporativo.core.config import get_settings

target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", get_settings().database_url.replace("+asyncpg", "+psycopg2"))
