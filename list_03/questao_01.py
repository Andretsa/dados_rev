'''Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o
aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).'''

class Aluno:
    def __init__(self,nome):
        self.nome = nome
        self.notas = []
        
    def adicionar_nota(self, nota):
        self.notas.append(nota)
        
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0  # Retorna 0 se não houver notas
        else:
            return sum(self.notas)/ len(self.notas)
        
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
    
# Função principal
def main():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)

    for i in range(5):
        nota = float(input(f"Digite a nota {i + 1}: "))
        aluno.adicionar_nota(nota)

    media = aluno.calcular_media()
    situacao = aluno.verificar_aprovacao()

    print(f"Nome do aluno: {aluno.nome}")
    print(f"A média do aluno é: {media:.2f}")
    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()
