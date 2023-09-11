def selecao_ordenacao(vetor):
    n= len(vetor)
    for i in range(n):
        indice_minimo = i
        print(vetor)
        for j in range (i + 1, n):
            if vetor [j] < vetor [indice_minimo]:
                indice_minimo = j
        vetor[i], vetor [indice_minimo] = vetor [indice_minimo], vetor[i]

def encontrar_segundo_menor(vetor):
    selecao_ordenacao(vetor)
    return vetor[1]

vetor = [5, 7, 4, 3]

print(encontrar_segundo_menor(vetor))
print(vetor)
