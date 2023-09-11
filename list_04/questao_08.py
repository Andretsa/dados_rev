from ordenacao import selecao_ordenacao

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
selecao_ordenacao(vetor)
print(encontrar_mediana(vetor))
print(vetor)