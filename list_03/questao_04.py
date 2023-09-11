'''Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.'''

#Função para calcular a soma dos dígitos de um número
def soma_digitos(numero):
    soma = 0
    #converte o numero em uma string
    numero_str = str(numero)
    #percorre essa string somando cada um dos seus numeros
    for numero in numero_str:
        soma += int(numero)
    return soma

def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero < 0:
                print("Por favor, digite um número inteiro positivo.")
            else:
                resultado = soma_digitos(numero)
                print(f"A soma dos dígitos do número {numero} é: {resultado}.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro positivo sem pontuações.")
            
if __name__ == "__main__":
    main()
