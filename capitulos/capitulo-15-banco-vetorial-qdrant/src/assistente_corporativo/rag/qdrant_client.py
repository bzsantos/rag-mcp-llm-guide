from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(url="http://localhost:6333")

NOME_COLECAO = "documentos"
DIMENSAO_EMBEDDING = 768  # dimensão do nomic-embed-text — confirmamos no Capítulo 5


def garantir_colecao() -> None:
    colecoes_existentes = {c.name for c in client.get_collections().collections}
    if NOME_COLECAO not in colecoes_existentes:
        client.create_collection(
            collection_name=NOME_COLECAO,
            vectors_config=VectorParams(size=DIMENSAO_EMBEDDING, distance=Distance.COSINE),
        )
        print(f"Coleção '{NOME_COLECAO}' criada.")
    else:
        print(f"Coleção '{NOME_COLECAO}' já existia.")


import uuid

from qdrant_client.models import PointStruct


def inserir_chunk(texto: str, vetor: list[float], metadados: dict) -> str:
    ponto_id = str(uuid.uuid4())
    client.upsert(
        collection_name=NOME_COLECAO,
        points=[PointStruct(id=ponto_id, vector=vetor, payload={"texto": texto, **metadados})],
    )
    return ponto_id


def buscar_similares(vetor_pergunta: list[float], top_k: int = 3) -> list[dict]:
    resultados = client.search(collection_name=NOME_COLECAO, query_vector=vetor_pergunta, limit=top_k)
    return [{"texto": r.payload["texto"], "score": r.score} for r in resultados]
