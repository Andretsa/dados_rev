""" questao 01
    Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
    algoritmo de seleção."""
    
# nao é uma funcao, é um procedimento pois nao retorna um valor
from minha_biblioteca import selecao_ordenacao

vetor = [5, 7, 4, 3]
print(f"O vetor {vetor}")
selecao_ordenacao(vetor)
print(f"Ordenado é: {vetor}")
