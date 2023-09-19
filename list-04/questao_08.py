"""Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do
meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um
número ímpar de elementos."""

def encontrar_mediana(vetor):
    vetor_ordenado = sorted(vetor)
    n = len(vetor)
    if n %2 ==0:
        meio1 = vetor_ordenado[n//2 - 1]
        meio2 = vetor_ordenado[n//2]
        return (meio1 + meio2) /2
    else:
        return vetor_ordenado [ n // 2]

vetor = [5, 7, 4, 3]
print(f"A mediana do vetor {vetor} é:", encontrar_mediana(vetor))
