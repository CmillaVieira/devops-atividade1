
def calcular_total(itens):
    """Calcula o valor total de um pedido."""

    if not itens:
        raise ValueError("O pedido precisa ter pelo menos um item.")

    total = 0

    for item in itens:
        total += item["preco"] * item["quantidade"]

    return total
