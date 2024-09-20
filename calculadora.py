def soma(x,y):
    return x + y    

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)
    
def potencia(x,y):
    x**y