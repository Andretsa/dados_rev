'''Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
chamado “calcular_area” que retorna a área do retângulo.'''

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    
# Cria um objeto retângulo com base 5 e altura 3
meu_retangulo = Retangulo(5, 3)

# Calcula e imprime a área do retângulo
print(f'A área do retângulo é de: {meu_retangulo.calcular_area()} m²')
    