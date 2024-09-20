import pytest
from calculadora import fatorial

def teste_fatorial_positivo():
    assert fatorial(5) == 120

def teste_fatorial_zero():
    assert fatorial(0) == 1

def teste_fatorial_maior_que_zero():
    assert fatorial(5) > 0

def teste_fatorial_nao_negativo():
    assert fatorial(5) >= 0
