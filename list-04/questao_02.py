"""
Esta função ordena um vetor de inteiros em ordem crescente ou decrescente 
usando o algoritmo de seleção.
Parâmetros:
- vetor: Uma lista de inteiros a ser ordenada.
- ordem: Um valor inteiro. Use 0 para ordenação crescente e 1 para ordenação decrescente.
A função modifica o vetor original para que ele fique ordenado de acordo com a ordem especificada.
"""
from minha_biblioteca import *

def selecionar_ordem(vetor, ordem):
    n= len(vetor)  # Obtém o tamanho do vetor
    if ordem == 0: # ordem crescente
        selecao_ordenacao(vetor)
    else: #ordena por ordem decrescente
        ordenacao_decrescente(vetor)

vetor = [5, 7, 4, 3]
print(f"O vetor a ser ordenado é:\n{vetor}")
selecionar_ordem(vetor, 0)
print(f"O vetor em ordem crescente é:\n{vetor}")
selecionar_ordem(vetor, 1)
print(f"O vetor em ordem decrescente é:\n{vetor}")
