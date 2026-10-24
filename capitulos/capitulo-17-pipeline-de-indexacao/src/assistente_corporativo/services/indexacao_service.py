import ollama
from sqlalchemy.ext.asyncio import AsyncSession

from assistente_corporativo.models.documento import Documento
from assistente_corporativo.rag.chunking import chunk_recursivo
from assistente_corporativo.rag.qdrant_client import inserir_chunk

client = ollama.Client(host="http://localhost:11434")


class IndexacaoService:
    def __init__(self, db: AsyncSession):
        self.db = db

    def _extrair_texto(self, caminho_arquivo: str) -> str:
        from pypdf import PdfReader
        leitor = PdfReader(caminho_arquivo)
        return "\n\n".join(p.extract_text() or "" for p in leitor.pages)

    def _gerar_embedding(self, texto: str) -> list[float]:
        return client.embeddings(model="nomic-embed-text", prompt=texto)["embedding"]

    async def indexar_documento(self, caminho_arquivo: str, nome_arquivo: str, cliente_id: int) -> Documento:
        texto = self._extrair_texto(caminho_arquivo)
        chunks = chunk_recursivo(texto, tamanho_max=800, overlap=150)

        documento = Documento(cliente_id=cliente_id, nome_arquivo=nome_arquivo, total_chunks=len(chunks))
        self.db.add(documento)
        await self.db.commit()
        await self.db.refresh(documento)

        for indice, chunk in enumerate(chunks):
            vetor = self._gerar_embedding(chunk)
            inserir_chunk(
                texto=chunk,
                vetor=vetor,
                metadados={
                    "documento_id": documento.id,
                    "cliente_id": cliente_id,
                    "nome_arquivo": nome_arquivo,
                    "chunk_index": indice,
                },
            )
        return documento
