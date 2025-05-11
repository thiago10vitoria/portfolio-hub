# calculadora.py

# Funções básicas de uma calculadora

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Exemplo de uso:
print("Soma:", somar(2, 3))
print("Subtração:", subtrair(5, 2))
print("Multiplicação:", multiplicar(3, 4))
print("Divisão:", dividir(10, 2))
