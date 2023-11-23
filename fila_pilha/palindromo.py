"""Palíndromos são palavras, frases ou sequências que mantêm sua mesma forma quando invertidos. Por
exemplo, a palavra "radar" é um palíndromo, pois se você a ler de trás para frente, ela ainda será
"radar". Construa um programa que possa ler uma palavras ou frase e dizer se ela é um Palíndromo,
use a estrutura de pilha para responder essa questão."""

from biblioteca import Pilha

def verificar_palindromo(frase):
    pilha = Pilha()
    frase = frase.lower().replace(" ", "")

    for char in frase:
        pilha.empilhar(char)

    inverso = ""
    while not pilha.vazia():
        inverso += pilha.desempilhar()

    return frase == inverso

# Palíndromo
frase_palindromo = "A man a plan a canal Panama"
resultado_palindromo = verificar_palindromo(frase_palindromo)
print(f"A frase: {frase_palindromo}.\nÉ um palíndromo?\n{resultado_palindromo}")