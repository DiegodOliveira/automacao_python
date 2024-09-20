import pytest
from calculadora import divisao

def teste_divisao():
    assert divisao(6, 2) == 3

def teste_divisao_negativo():
    assert divisao(-6, 2) == -3

def teste_divisao_negativo_negativo():
    assert divisao(-6, -2) == 3

def teste_divisao_numeros_reais():
    assert divisao(5.5, 2.5) == 2.2

def teste_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        divisao(5, 0)
