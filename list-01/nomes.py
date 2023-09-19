'''Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que
começam com a letra 'A'.'''
# Solicita ao usuário a entrada de nomes separados por vírgula
nome = input("Digite uma lista de nomes separados por espaço: ")

# Divide a string em uma lista de nomes
nomes = nome.split(" ")

# Cria uma nova lista com nomes que começam com a letra 'A'
nomes_a = []
for nome in nomes:
    if nome.strip().lower().startswith('a'): # remove espaços, transforma em minúsculo, inicia com "a"?
        nomes_a.append(nome) # itera a lista nomes_a

# Imprime a lista nomes_a
print("Nomes que começam com 'A':")
for nome in nomes_a:
    print(nome)
