
def chunk_fixo(texto: str, tamanho: int = 200) -> list[str]:
    return [texto[i:i + tamanho].strip() for i in range(0, len(texto), tamanho) if texto[i:i + tamanho].strip()]



def chunk_fixo_com_overlap(texto: str, tamanho: int = 200, overlap: int = 50) -> list[str]:
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fim = inicio + tamanho
        chunks.append(texto[inicio:fim].strip())
        inicio += tamanho - overlap
    return [c for c in chunks if c]



def chunk_recursivo(texto: str, tamanho_max: int = 300, overlap: int = 50) -> list[str]:
    separadores = ["\n\n", "\n", ". ", " "]
    return _dividir(texto, separadores, tamanho_max, overlap)


def _dividir(texto: str, separadores: list[str], tamanho_max: int, overlap: int) -> list[str]:
    if len(texto) <= tamanho_max or not separadores:
        return chunk_fixo_com_overlap(texto, tamanho_max, overlap)

    separador, restantes = separadores[0], separadores[1:]
    partes = [p for p in texto.split(separador) if p.strip()]

    chunks, buffer = [], ""
    for parte in partes:
        candidato = f"{buffer}{separador}{parte}" if buffer else parte
        if len(candidato) <= tamanho_max:
            buffer = candidato
        else:
            if buffer:
                chunks.append(buffer.strip())
            buffer = parte if len(parte) <= tamanho_max else ""
            if not buffer and len(parte) > tamanho_max:
                chunks.extend(_dividir(parte, restantes, tamanho_max, overlap))
    if buffer:
        chunks.append(buffer.strip())
    return chunks
