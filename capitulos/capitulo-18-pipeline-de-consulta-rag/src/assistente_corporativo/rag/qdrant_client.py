def buscar_similares(vetor_pergunta: list[float], top_k: int = 5) -> list[dict]:
    resultados = client.search(collection_name=NOME_COLECAO, query_vector=vetor_pergunta, limit=top_k)
    return [{"texto": r.payload["texto"], "score": r.score, "metadados": r.payload} for r in resultados]
