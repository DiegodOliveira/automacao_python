import pytest
from calculadora import soma

def teste_soma():
    assert soma(5,2) == 7

def teste_soma_negativo():
    assert soma(-5,2) == -3

def teste_soma_negativo_negativo():
    assert soma(-5,-2) == -7

def teste_soma_numeros_reais():
    assert soma(5.5,2.5) == 8



