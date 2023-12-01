"""Imagine uma árvore binária representando uma árvore genealógica. 
Cada nó possui informações  sobre um membro da família.
Desenvolva um código em Python para criar e imprimir essa árvore."""

class No:
    def __init__(self, nome, ano_nascimento, filhos = None):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.filhos = filhos if filhos is not None else []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

def imprimir_arvore(no, nivel=0):
    if no is not None:
        print("  " * nivel + f"{no.nome} ({no.ano_nascimento})")
        for filho in no.filhos:
            imprimir_arvore(filho, nivel + 1)

# Criando a árvore genealógica
avo_paterno = No("Avo Paterno", 1938, [])
avo_materno = No("Avo Materno", 1934, [])
pai = No("Pai", 1965, [])
mae = No("Mae", 1967, [])
vo_paterno = No("Vo Paterno", 1933, [])
vo_materno = No("Vo Materno", 1937, [])
eu = No("Eu", 1990, [])

eu.adicionar_filho(pai)
eu.adicionar_filho(mae)
pai.adicionar_filho(avo_paterno)
pai.adicionar_filho(vo_paterno)
mae.adicionar_filho(avo_materno)
mae.adicionar_filho(vo_materno)


# Imprimindo a árvore genealógica
imprimir_arvore(eu)
