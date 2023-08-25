'''Faça um programa que calcule a média de três números inseridos pelo usuário.'''
numeros = []

for i in range(3):
    numero = int(input(f"Insira o {i+1}º número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
print("Você digitou os números:", ", ".join(map(str, numeros)), ". A média deles é: {:.2f}".format(media))
#a função map() converte cada elemento da lista numeros em uma string
