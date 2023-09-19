'''Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
computador e determinar o vencedor.'''

# importando o método random
import random

print("Bem-vindo ao Jogo Pedra, Papel, Tesoura!")

while True:
    try:
        usuario = input("Escolha Pedra, Papel ou Tesoura: ").lower()
        escolhas = ['pedra', 'papel', 'tesoura']

        if usuario in escolhas:
            computador = random.choice(escolhas)
            print(f"Você escolheu: {usuario}")
            print(f"O computador escolheu: {computador}")

            if usuario == computador:
                print("Empate!")
            elif (usuario == 'pedra' and computador == 'tesoura') or \
                (usuario == 'tesoura' and computador == 'papel') or \
                    (usuario == 'papel' and computador == 'pedra'):
                print("Você ganhou!")
            else:
                print("Você perdeu.")

            jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
            if jogar_novamente == 'n':
                break
            elif jogar_novamente != 's':
                print("Escolha inválida. Encerrando o jogo.")
                break
        else:
            print("Escolha inválida. Por favor, escolha entre Pedra, Papel ou Tesoura.")
    except ValueError:
        print("Escolha inválida.")
