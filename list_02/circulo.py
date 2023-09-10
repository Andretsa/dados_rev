'''Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
“calcular_area” que retorna a área do círculo.'''

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        # Utilizamos a função pi da biblioteca math para obter um valor mais preciso de π (pi)
        area = math.pi * (self.raio ** 2)
        return area
    
# Exemplo de uso da classe Circulo
raio_do_circulo = 5.0
circulo = Circulo(raio_do_circulo)
area_circulo = circulo.calcular_area()
#print(retangulo.calcular_area(5, 3))
print(f"A área do círculo de raio {raio_do_circulo} é {area_circulo: .2f} m²")
