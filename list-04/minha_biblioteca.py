def selecao_ordenacao(vetor):
    n = len(vetor)  # Obtém o tamanho do vetor
    for i in range(n):  # Loop externo para percorrer todos os elementos do vetor
        indice_minimo = i  # Define o índice mínimo como o índice atual (i)
        for j in range(i + 1, n):  # Loop interno para encontrar o índice mínimo no restante do vetor
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j  # Atualiza o índice mínimo se um elemento menor for encontrado
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]
        # Troca o elemento na posição i pelo elemento de índice mínimo encontrado
        
def ordenacao_decrescente(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range (i + 1, n):
            if vetor [j] > vetor [indice_minimo]:
                indice_minimo = j
            vetor[i], vetor [indice_minimo] = vetor [indice_minimo], vetor[i]

def contar_par_impar(vetor):
    #inicializa os contadores para os números pares e ímpares
    cp = 0
    ci = 0
    for i in vetor:
        if i % 2 == 0: # se o número for divisível por 2 é par
            cp += 1 # incremento do contador pae
        else: # senao é ímpar
            ci += 1 #incremento do contador ímpar
    return cp,ci
