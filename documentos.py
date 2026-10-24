import shutil
import tempfile
from pathlib import Path

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.core.deps import usuario_atual
from assistente_corporativo.db.session import get_db_session
from assistente_corporativo.services.indexacao_service import IndexacaoService

router = APIRouter()


@router.post("/upload")
async def upload_documento(
    cliente_id: int,
    arquivo: UploadFile,
    db: AsyncSession = Depends(get_db_session),
    _usuario=Depends(usuario_atual),
):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(arquivo.file, tmp)
        caminho_temporario = tmp.name

    service = IndexacaoService(db)
    documento = await service.indexar_documento(caminho_temporario, arquivo.filename, cliente_id)
    Path(caminho_temporario).unlink(missing_ok=True)

    return {"documento_id": documento.id, "total_chunks": documento.total_chunks}
