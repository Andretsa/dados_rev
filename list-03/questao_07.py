'''Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura
e peso.'''

class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
    
    def calcular_imc(self):
        return self.peso / (self.altura * self.altura)

def main():
    peso = float(input("Digite o peso da pessoa em quilogramas: "))
    altura = float(input("Digite a altura da pessoa em metros: "))
    
    pessoa = Pessoa(peso, altura)
    imc = pessoa.calcular_imc()
    
    print(f"O IMC da pessoa é: {imc:.2f}")

if __name__ == "__main__":
    main()
