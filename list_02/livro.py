'''Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
chamado “detalhes” que retorna uma string com as informações do livro.'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def detalhes(self):
        return (f"Título do livro: {self.titulo}, Autor: {self.autor}")
        
livro1 = Livro("Harry Potter e o Cálice de Fogo", "J.K. Rowling")
print(livro1.detalhes())
