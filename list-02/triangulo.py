'''Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
método chamado “calcular_perimetro” que retorna o perímetro do triângulo.'''

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def calcular_perimetro(self):
        if self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Este triangulo é escaleno.")
        elif self.lado1 == self.lado2 == self.lado3:
            print("Esse triangulo é equilátero.")
        else:
            print("Esse triangulo é um isósceles.")
        return self.lado1 + self.lado2 + self.lado3
    
triangulo1 = Triangulo(4, 5, 6)
print(f"E o seu perímetro é de: {triangulo1.calcular_perimetro()} unidades.")

triangulo2 = Triangulo(3, 3, 3)
print(f"E o seu perímetro é de:  {triangulo2.calcular_perimetro()} unidades.")

triangulo3 = Triangulo(3, 3, 4)
print(f"E o seu perímetro é de:  {triangulo3.calcular_perimetro()} unidades.")
