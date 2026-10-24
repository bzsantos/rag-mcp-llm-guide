from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = "postgresql+asyncpg://assistente:assistente@localhost:5432/assistente_db"

engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True: mostra o SQL gerado, útil para aprender
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
