'''Faça um programa que leia uma lista de números e retorne a média dos números pares.'''
# Solicita a entrada do usuário
entrada = input("Digite uma lista de números separados por espaço: ")

# Divide a entrada em uma lista de strings de números
strings_de_numeros = entrada.split()
print(strings_de_numeros)

# Inicializa uma lista vazia para armazenar os números inseridos
pares = []

# Percorre as strings de números e converte cada uma em um número
for string_numero in strings_de_numeros:
    num = int(string_numero)
    print(num)
# Insere na lista apenas os números pares
    if num % 2 == 0:
        pares.append(num)
# verifica se a lista está vazia e calcula a media dos numeros pares
if not pares:
    print("A lista está vazia.")
else:
    media_pares = sum(pares)/ len(pares)
    print("A média dos números pares é: {}".format(media_pares))
