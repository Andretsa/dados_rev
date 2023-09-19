'''Crie uma função que verifica se um número é primo ou não'''
# Funcao que verifica se o numero é primo ou não
def verifica_primo(num):
    if num <= 0:
        return False, []
    
    div = []
    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i) # itera os divisiveis pelo numero na lista div
    
    if len(div) == 2:
        return True, div
    else:
        return False, div
# Funcao principal que solicita a entrada de um número pelo usuário
def main():
    while True:
        try:
            num = int(input("Digite um número: "))
            is_prime, divisores = verifica_primo(num)
            
            if is_prime:
                print("\nEste é um número primo.")
            else:
                print("\nEste não é um número primo.")
                
            print(f"E seus divisores são: {divisores}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro positivo.")

if __name__ == "__main__":
    main()
