'''Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário.'''

class Fatorial:
    def __init__(self,numero):
        self.numero = numero
        
    def calcular_fatorial(self):
        fatorial = 1
        for i in range(1, self.numero + 1):
            fatorial *= i
        print(f"O fatorial de {self.numero} é: {fatorial}")
        
# Funçãao principal
def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero < 0:
                print("Por favor, digite um número inteiro positivo.")
            else:
                f = Fatorial(numero)
                f.calcular_fatorial()
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro positivo.")
            
if __name__ == "__main__":
    main()
