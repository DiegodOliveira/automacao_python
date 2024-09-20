import pytest
from calculadora import multiplicacao

def teste_multiplicacao():
    assert multiplicacao(2,5) == 10

def teste_multiplicacao_negativo():
    assert multiplicacao(-2,5) == -10

def teste_multiplicacao_negativo_negativo():
    assert multiplicacao(-2, -5) == 10

def teste_multiplicacao_numero_real():
    assert multiplicacao(2.5 , 5.5) == 13.75

def teste_multiplicacao_zero():
    assert multiplicacao(5,0) == 0

def teste_multiplicacao_nao_zero():
    assert not multiplicacao(5,0) == 5