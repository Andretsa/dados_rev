"""Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem
usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`."""

def encontrar_max_min(vetor):
    minimo = vetor[0]
    maximo = vetor[0]
    for elemento in vetor:
        if elemento > minimo:
            maximo = elemento
        elif elemento < maximo:
            minimo = elemento
    return maximo, minimo

vetor = [5, 7, 4, 3]
print(f"O vetor é: {vetor}")
resp = encontrar_max_min(vetor)
print("O elemento máximo do vetor é:",resp[0], "\nE o seu elemento mínimo é: ",resp[1])
