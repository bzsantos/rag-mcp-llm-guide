from assistente_corporativo.rag.rag_service import RagService
import asyncio

async def main():
    service = RagService(top_k=3)
    pergunta = "e sobre o tempo de descanso?"

    contexto_normal, _ = service.montar_contexto(pergunta)
    print("=== BUSCA NORMAL ===")
    print(contexto_normal[:300])

    resultados_hyde = await service.buscar_com_hyde(pergunta)
    print("\n=== BUSCA COM HYDE ===")
    for r in resultados_hyde:
        print(f"[{r['score']:.3f}] {r['texto'][:150]}")

asyncio.run(main())
