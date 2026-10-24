# Trechos ilustrativos do Capítulo 19

Estes trechos aparecem no texto do capítulo sem um arquivo-alvo explícito
(geralmente exemplos conceituais ou variações mostradas em caixas de destaque).

```python
def recuperar_com_parent(chunk_encontrado: dict, repositorio_documentos) -> str:
    documento_id = chunk_encontrado["metadados"]["documento_id"]
    return repositorio_documentos.obter_texto_completo(documento_id)
```

