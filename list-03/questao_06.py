'''Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes
nela.'''

from unidecode import unidecode

class ContadorDeVogais:
    def __init__(self):
        self.vogais = ["a", "e", "i", "o", "u"]

    def contar_vogais(self, frase):
        frase_sem_acentos = unidecode(frase.lower())
        soma = 0
        for letra in frase_sem_acentos:
            if letra.isalpha() and letra in self.vogais:
                soma += 1
        return soma

def main():
    contador = ContadorDeVogais()
    frase = input("Digite uma frase: ")
    quantidade_vogais = contador.contar_vogais(frase)
    print(f"A quantidade de vogais na frase é: {quantidade_vogais}")

if __name__ == "__main__":
    main()
    