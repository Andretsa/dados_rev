'''Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa,
dependendo da escolha do usuário.'''

class Temperatura:
    def __init__(self, temperatura):
        self.temperatura = temperatura
    
    def converter(self, escolha):
        if escolha == "Fahrenheit":
            return self.temperatura * 1.8 + 32
        elif escolha == "Celsius":
            return (self.temperatura - 32) / 1.8

def main():
    while True:
        try:
            temperatura = float(input("Digite a temperatura a ser convertida (digite '0' para sair): "))
            if temperatura == 0:
                break
            
            escolha = input("Escolha a unidade de temperatura (Celsius ou Fahrenheit): ").capitalize()
            
            if escolha != "Celsius" and escolha != "Fahrenheit":
                print("Escolha de unidade de temperatura inválida.")
            else:
                temp = Temperatura(temperatura)
                if escolha == "Celsius":
                    resultado = temp.converter("Fahrenheit")
                    print(f"{temperatura:.2f} ºCelsius equivalem a {resultado:.2f} ºFahrenheit.")
                else:
                    resultado = temp.converter("Celsius")
                    print(f"{temperatura:.2f} ºFahrenheit equivalem a {resultado:.2f} ºCelsius.")
        except ValueError:
            print("Entrada inválida. Certifique-se de que a temperatura seja um número válido.")

if __name__ == "__main__":
    main()
