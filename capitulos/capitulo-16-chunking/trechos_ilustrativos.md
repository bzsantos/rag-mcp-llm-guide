# Trechos ilustrativos do Capítulo 16

Estes trechos aparecem no texto do capítulo sem um arquivo-alvo explícito
(geralmente exemplos conceituais ou variações mostradas em caixas de destaque).

```python
from assistente_corporativo.playground.documento_grande import documento
from assistente_corporativo.rag.chunking import chunk_fixo

chunks = chunk_fixo(documento, tamanho=200)
for i, c in enumerate(chunks):
    print(f"--- chunk {i} ---")
    print(c)
    print()
```

