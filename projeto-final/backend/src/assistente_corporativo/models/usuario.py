from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from assistente_corporativo.db.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)
