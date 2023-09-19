"""Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte
quantos números pares e quantos números ímpares existem no vetor ordenado."""

from minha_biblioteca import *

vetor = [5, 7, 4, 3]
print(f"O vetor é: {vetor}")

ordenacao_decrescente(vetor)
print(f"O vetor em ordem decrescente é:\n{vetor}")

resposta = contar_par_impar(vetor)
print(f"A quantidade de números pares e ímpares no vetor {vetor} é:",resposta, "respectivamente")
