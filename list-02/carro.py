'''Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
chamado “detalhes” que retorna uma string com as informações do carro.'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def detalhes(self):
        return f"O carro é da marca: {self.marca}, modelo: {self. modelo}, ano: {self. ano}."
    
carro1 = Carro("Hyundai", "HB20", 2013)
print(carro1.detalhes())
