import pytest
from calculadora import subtracao

def teste_subtracao():
    assert subtracao(10,5) == 5

def teste_subtracao_negativo():
    assert subtracao(5,-10) == 15

def teste_subtracao_negativo():
    assert subtracao(-5,-10) == 5

def teste_subtracao_numeros_reais():
    assert subtracao(5.5,10.5) == -5.0

def teste_subtracao_zero():
    assert subtracao(5,0) == 5