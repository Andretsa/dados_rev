'''def ordenaca0_decrescente(vetor):
     for i in range(n):
        indice_minimo = i
        print(vetor)
        for j in range (i + 1, n):
            if vetor [j] > vetor [indice_minimo]:
                indice_minimo = j
            vetor[i], vetor [indice_minimo] = vetor [indice_minimo], vetor[i]'''

def contar_par_impar(vetor):
    cp = 0
    ci = 0
    for i in vetor:
        if i %2 == 0:
            cp += 1
        else:
            ci += 1
    return cp,ci

vetor = [5, 7, 4, 3]

