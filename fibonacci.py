'''Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.'''
# Solicita a entrada do usuário por um valor inteiro positivo
try:
    valor = int(input("Insira um valor: "))
    if  valor < 0:
        print("Por favor, insira um valor inteiro positivo.")
    else:
        fibonacci = [0, 1] # cria a lista com os primeiros números da sequencia fibonacci
        while fibonacci[-1] + fibonacci[-2] <= valor: # verifica se o termo é menor ou igual ao valor
            fibonacci.append(fibonacci[-1] + fibonacci[-2]) # itera a lista com o termo seguinte
        print("A sequência de Fibonacci até o valor inserido", valor, " é:", fibonacci)
except ValueError:
    print("Por favor, insira um valor numérico válido.")
