"""Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos
duplicados, retornando o vetor resultante sem duplicatas."""

def remover_duplicatas(vetor):
    vetor_sem_duplicatas = []
    for elemento in vetor:
        if elemento not in vetor_sem_duplicatas:
            vetor_sem_duplicatas.extend([elemento])
    return vetor_sem_duplicatas

vetor = [5, 7, 4, 3, 6, 3, 5]
resposta = remover_duplicatas(vetor)
print(f"O vetor {vetor}, sem dupilcatas é:",resposta)
