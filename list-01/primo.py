'''Faça um programa que determine se um número é primo ou não.'''
# Solicita a entrada de um número pelo usuário
# Imprime se o mesmo é um número primo ou não
while True:
    try:
        num = int(input("Digite um numero: "))
        if num <= 0:
            print("Por favor, digite um número inteiro positivo.")
        else:
            div = []
            for i in range(1, num + 1):
                if num % i == 0:
                    div.append(i) # itera os divisiveis pelo numero na lista div
            if len(div) == 2:
                print("\nEsse é um número primo.")
            else:
                print("\nEsse não é um número primo.")
        print(f"E seus divisores são: {div}") # imprime os numeros divisiveis pelo numero digitado
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")
        