"""Crie uma estrutura que possa ler uma expressão matemática do tipo (2+3)*(8-9)/(7^3) e apresente
todos os operadores matemáticos existente nessa expressão, utilize a pilha para responder a questão."""

from biblioteca import Pilha
            
def obter_operadores(expressao):
    pilha = Pilha()

    for char in expressao:
        if char in "+-*/^()":
            pilha.empilhar(char)

    return pilha

# Expressão Matemática
expressao_exemplo = "(2+3)*(8-9)/(7^3)"
operadores = obter_operadores(expressao_exemplo)
print("Operadores na expressão:", operadores.itens)
