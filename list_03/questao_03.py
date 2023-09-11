'''Crie uma função que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
desconsiderando espaços e pontuação).'''

def verifica_palindromo(frase):
    frase = frase.replace(' ','').lower()
    inverso = ""
    frase = ''.join(filter(str.isalpha, frase))
    for i in range(len(frase) - 1, -1, -1):
        inverso += frase[i]
    print(inverso)
    if frase == inverso:
        return True
    else:
        return False

frase = input("Digite uma frase ou palavra: ")
if verifica_palindromo(frase):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
