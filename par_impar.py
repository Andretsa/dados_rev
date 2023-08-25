'''Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.'''
while True:
    try:
        num = int(input("Insira um número: "))
        if num % 2 == 0:
            print("Esse número é par.")
        else:
            print("Esse número é ímpar.")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
