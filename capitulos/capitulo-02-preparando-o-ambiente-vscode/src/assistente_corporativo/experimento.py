
def calcular_total(preco: float, quantidade: int) -> float:
    subtotal = preco * quantidade
    desconto = subtotal * 0.1 if quantidade >= 10 else 0
    total = subtotal - desconto
    return total


if __name__ == "__main__":
    resultado = calcular_total(preco=25.0, quantidade=12)
    print(f"Total: R$ {resultado:.2f}")
