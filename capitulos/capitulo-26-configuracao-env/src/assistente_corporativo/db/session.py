from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from assistente_corporativo.core.config import get_settings

settings = get_settings()
engine = create_async_engine(settings.database_url, echo=False)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
