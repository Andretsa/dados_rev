def encontrar_maximo(vetor):
    maximo = vetor[0]
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
    return maximo

def encontrar_minimo(vetor):
    minimo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
    return minimo

def encontrar_max_min(vetor):
    minimo = vetor[0]
    maximo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
        elif elemento > maximo:
            maximo = elemento
    return maximo, minimo

vetor = [5, 7, 4, 3]
print(encontrar_maximo(vetor))
print(encontrar_minimo(vetor))
resp = encontrar_max_min(vetor)
print(resp[0], resp[1])