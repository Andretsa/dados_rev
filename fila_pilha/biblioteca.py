#classe usada para exercícios que envolvem Fila
class Fila:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None
        
#classe usada para exercícios que envolvem Pilha  
class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return None
        