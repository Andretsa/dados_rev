'''Faça um programa que calcule a média de três números inseridos pelo usuário.'''
# Solicita a entrada dos 3 números pelo usuário
n1 = int(input("Insira o seu 1º número: "))
n2 = int(input("Insira o seu 2º número: "))
n3 = int(input("Insira o seu 3º número: "))

# Calcula e imprime a media destes números
media = (n1 + n2 + n3) / 3
print("Você digitou os números: {}, {}, {}. A média deles é: {}".format(n1,n2,n3,media))
