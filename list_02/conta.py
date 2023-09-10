'''Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
métodos “depositar” e “sacar” para manipular o saldo.'''

class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo:.2f}'
        else:
            return 'O valor do depósito deve ser maior que zero.'

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                return f'Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo:.2f}'
            else:
                return 'Saldo insuficiente para realizar o saque.'
        else:
            return 'O valor do saque deve ser maior que zero.'

# Exemplo de uso:
conta = ContaBancaria("Andrezza")
print(f"Saldo inicial de {conta.titular}: R${conta.saldo:.2f}")

print(conta.depositar(100))
print(conta.sacar(50))
print(conta.sacar(70))
