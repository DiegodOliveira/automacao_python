import pytest
from calculadora import potencia

def teste_potencia():
    assert potencia(2, 3) == 8

def teste_potencia_negativo():
    assert potencia(-2, 3) == -8

def teste_potencia_negativo_par():
    assert potencia(-2, 2) == 4

def teste_potencia_numeros_reais():
    assert potencia(2.5, 2) == 6.25

def teste_potencia_zero():
    assert potencia(0, 5) == 0
    assert potencia(5, 0) == 1
