'''Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.'''

# Solicita a entrada do usuário
entrada = input("Digite uma lista de números separados por espaço: ")

# Divide a entrada em uma lista de strings de números
strings_de_numeros = entrada.split()

# Inicializa uma lista vazia para armazenar os números inteiros
numeros = []

# Percorre as strings de números e converte cada uma em um número inteiro
for string_numero in strings_de_numeros:
    num = int(string_numero)
    numeros.append(num)

maior = menor = numeros[0]
# Percorre a lista dos numeros inseridos pelo usuário
# E os compara entre si para saber o maior e menor
for num in numeros:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"O maior número digitado foi: {maior}. E o menor foi: {menor}")
