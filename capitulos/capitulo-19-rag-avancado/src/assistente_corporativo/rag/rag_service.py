async def buscar_com_hyde(self, pergunta: str) -> list[dict]:
    prompt_hipotetico = f"Escreva um parágrafo respondendo hipoteticamente: {pergunta}"
    resposta_hipotetica = client.chat(
        model="llama3.2:3b", messages=[{"role": "user", "content": prompt_hipotetico}]
    )["message"]["content"]

    vetor = self._gerar_embedding(resposta_hipotetica)
    return buscar_similares(vetor, top_k=self.top_k)


async def buscar_multi_query(self, pergunta: str) -> list[dict]:
    prompt = f'Gere 3 reformulações diferentes para a pergunta abaixo, uma por linha, sem numeração:\n\n{pergunta}'
    variacoes_texto = client.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])["message"]["content"]
    variacoes = [pergunta] + [v.strip() for v in variacoes_texto.split("\n") if v.strip()]

    vistos = {}
    for variacao in variacoes:
        vetor = self._gerar_embedding(variacao)
        for r in buscar_similares(vetor, top_k=self.top_k):
            chave = r["texto"]
            if chave not in vistos or r["score"] > vistos[chave]["score"]:
                vistos[chave] = r
    return sorted(vistos.values(), key=lambda r: r["score"], reverse=True)[: self.top_k]
