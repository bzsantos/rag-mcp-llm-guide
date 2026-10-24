# src/assistente_corporativo/rag/qdrant_client.py
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, FieldCondition, Filter, MatchValue, PointStruct, VectorParams

from assistente_corporativo.core.config import get_settings

settings = get_settings()
client = QdrantClient(url=settings.qdrant_url)

NOME_COLECAO = "documentos"
DIMENSAO_EMBEDDING = 768  # dimensão do nomic-embed-text


def garantir_colecao() -> None:
    colecoes_existentes = {c.name for c in client.get_collections().collections}
    if NOME_COLECAO not in colecoes_existentes:
        client.create_collection(
            collection_name=NOME_COLECAO,
            vectors_config=VectorParams(size=DIMENSAO_EMBEDDING, distance=Distance.COSINE),
        )


def inserir_chunk(texto: str, vetor: list[float], metadados: dict) -> str:
    ponto_id = str(uuid.uuid4())
    client.upsert(
        collection_name=NOME_COLECAO,
        points=[PointStruct(id=ponto_id, vector=vetor, payload={"texto": texto, **metadados})],
    )
    return ponto_id


def buscar_similares(
    vetor_pergunta: list[float],
    top_k: int = 5,
    documento_id: int | None = None,
    cliente_id: int | None = None,
) -> list[dict]:
    condicoes = []
    if documento_id is not None:
        condicoes.append(FieldCondition(key="documento_id", match=MatchValue(value=documento_id)))
    if cliente_id is not None:
        condicoes.append(FieldCondition(key="cliente_id", match=MatchValue(value=cliente_id)))
    filtro = Filter(must=condicoes) if condicoes else None

    resultados = client.search(
        collection_name=NOME_COLECAO, query_vector=vetor_pergunta, query_filter=filtro, limit=top_k
    )
    return [{"texto": r.payload["texto"], "score": r.score, "metadados": r.payload} for r in resultados]
