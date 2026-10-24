from assistente_corporativo.playground.documento_grande import documento
from assistente_corporativo.rag.chunking import chunk_fixo, chunk_fixo_com_overlap, chunk_recursivo

for nome, funcao in [
    ("fixo", lambda t: chunk_fixo(t, 200)),
    ("fixo+overlap", lambda t: chunk_fixo_com_overlap(t, 200, 50)),
    ("recursivo", lambda t: chunk_recursivo(t, 200, 50)),
]:
    chunks = funcao(documento)
    print(f"\n=== {nome}: {len(chunks)} chunks ===")
    print("Primeiro chunk:", chunks[0][:150])
