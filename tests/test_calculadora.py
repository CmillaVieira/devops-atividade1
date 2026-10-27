
import pytest

from src.calculadora import calcular_total


def test_calcular_total_de_um_item():
    itens = [
        {"preco": 10, "quantidade": 2}
    ]

    resultado = calcular_total(itens)

    assert resultado == 20


def test_calcular_total_de_varios_itens():
    itens = [
        {"preco": 10, "quantidade": 2},
        {"preco": 5, "quantidade": 3}
    ]

    resultado = calcular_total(itens)

    assert resultado == 35


def test_pedido_vazio_deve_gerar_erro():
    with pytest.raises(ValueError):
        calcular_total([])


from src.calculadora import processar_pedido


def test_processar_pedido():
    itens = [
        {"preco": 10, "quantidade": 2},
        {"preco": 5, "quantidade": 3}
    ]

    resultado = processar_pedido(itens)

    assert resultado["quantidade_itens"] == 5
    assert resultado["total"] == 35
