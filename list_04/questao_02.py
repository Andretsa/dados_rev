def selecao_ordenacao(vetor, ordem):
    n= len(vetor)
    if ordem == 0:
        for i in range(n):
            indice_minimo = i
            print(vetor)
            for j in range (i + 1, n):
                if vetor [j] < vetor [indice_minimo]:
                    indice_minimo = j
            vetor[i], vetor [indice_minimo] = vetor [indice_minimo], vetor[i]
    else:
      for i in range(n):
        indice_minimo = i
        print(vetor)
        for j in range (i + 1, n):
            if vetor [j] > vetor [indice_minimo]:
                indice_minimo = j
            vetor[i], vetor [indice_minimo] = vetor [indice_minimo], vetor[i]

vetor = [5, 7, 4, 3]
selecao_ordenacao(vetor, 0)
selecao_ordenacao(vetor, 1)