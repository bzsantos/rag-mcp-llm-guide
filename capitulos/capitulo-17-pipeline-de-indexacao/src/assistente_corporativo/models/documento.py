from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from assistente_corporativo.db.base import Base


class Documento(Base):
    __tablename__ = "documentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    nome_arquivo: Mapped[str] = mapped_column(String(255))
    total_chunks: Mapped[int] = mapped_column(default=0)
