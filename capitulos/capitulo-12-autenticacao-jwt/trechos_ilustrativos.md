# Trechos ilustrativos do Capítulo 12

Estes trechos aparecem no texto do capítulo sem um arquivo-alvo explícito
(geralmente exemplos conceituais ou variações mostradas em caixas de destaque).

```python
async def obter_por_id(self, usuario_id: int) -> Usuario | None:
    resultado = await self.db.execute(select(Usuario).where(Usuario.id == usuario_id))
    return resultado.scalar_one_or_none()
```

