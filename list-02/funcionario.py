'''Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
do funcionário.'''

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self):
        return self.salario + (self.salario * 0.3)
    
funcionario1 = Funcionario("Andrezza", 10.000, "Desenvolvedora back-end")
print(f"O salário atual de {funcionario1.nome} é de : R${funcionario1.aumentar_salario():.3f}")
