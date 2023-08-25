'''calculando o fatorial de um número inteiro positivo usando a funcao factorial do módulo math'''
from math import factorial
while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
        else:
            f = factorial(numero)
            print("O fatorial de {} é: {}".format(numero, f))
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")
