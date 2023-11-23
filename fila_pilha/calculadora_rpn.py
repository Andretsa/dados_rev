"""Crie uma calculadora que avalia expressões matemáticas no formato Notação Polonesa Reversa
(RPN). Use uma pilha para armazenar os operandos e operadores e realizar os cálculos."""

from biblioteca import Pilha

class CalculadoraRPN:
    def __init__(self):
        self.pilha = Pilha()

    def calcular(self, expressao):
        tokens = expressao.split()
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.pilha.empilhar(float(token))
            else:
                operando2 = self.pilha.desempilhar()
                operando1 = self.pilha.desempilhar()
                if token == '+':
                    calculo = operando1 + operando2
                elif token == '-':
                    calculo = operando1 - operando2
                elif token == '*':
                    calculo = operando1 * operando2
                elif token == '/':
                    calculo = operando1 / operando2
                elif token == '^':
                    calculo = operando1 ** operando2
                else:
                    raise ValueError(f"Operador inválido: {token}")
                self.pilha.empilhar(calculo)
        return self.pilha.desempilhar()
    
calculadora = CalculadoraRPN()
resultado = calculadora.calcular("3 4 + 2 *")
print("Resultado da expressão RPN:", resultado)
resultado = calculadora.calcular("3 4 - 2 +")
print("Resultado da expressão RPN:", resultado)
resultado = calculadora.calcular("12 4 / 4 *")
print("Resultado da expressão RPN:", resultado)