
def calcular_total(itens):
    """Calcula o valor total de um pedido."""

    if not itens:
        raise ValueError("O pedido precisa ter pelo menos um item.")

    total = 0

    for item in itens:
        total += item["preco"] * item["quantidade"]

    return total

def processar_pedido(itens):
    """Retorna a quantidade de unidades e o total do pedido."""

    total = calcular_total(itens)
    quantidade_itens = sum(item["quantidade"] for item in itens)

    return {
        "quantidade_itens": quantidade_itens,
        "total": total
    }
