'''Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
“calcular_media” que retorna a média das notas do aluno.'''

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
        
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0  # Retorna 0 se não houver notas
        else:
            media = sum(self.notas)/ len(self.notas)
            return f"A média das notas de {self.nome} é: {media:.2f}"
        
aluno1 = Aluno("Amita", [8.5, 9.5, 10.0])
print(aluno1.calcular_media())
