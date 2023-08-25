'''Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
esse número.'''
# Inicializa a lista dos números pares
pares = []

# Solicita a entrada de um número ao usuário
# Permitindo apenas números positivos acima de 0
# Itera  e imprime a lista apenas com os números pares de 0 até o numero de entrada pelo usuário
while True:
    try:
        num = int(input("Insira um número: "))
        if num < 0:
            print("Por favor, insira um número maior que 0")
        else:
            if num % 3 == 0:
                num -= 1
            for i in range(0, num + 2, 2):
                pares.append(i)
            print("Os números pares de 0 até o número inserido que foi {} são: {}.".format(num, pares))
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")
