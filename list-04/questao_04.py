"""Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor."""

from minha_biblioteca import selecao_ordenacao

def encontrar_segundo_menor(vetor):
    selecao_ordenacao(vetor)
    return vetor[1]

vetor = [5, 7, 4, 3]
selecao_ordenacao(vetor)
resposta = encontrar_segundo_menor(vetor)
print(f"O segundo menor número do vetor{vetor} é: {resposta}")
