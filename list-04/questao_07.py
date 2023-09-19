"""Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor."""

from minha_biblioteca import selecao_ordenacao

def encontrar_terceiro_maior(vetor):
    selecao_ordenacao(vetor)
    return vetor[2]

vetor = [5, 7, 4, 3]
selecao_ordenacao(vetor)
resposta = encontrar_terceiro_maior(vetor)
print(f"O terceiro maior número do vetor{vetor} é: {resposta}")
