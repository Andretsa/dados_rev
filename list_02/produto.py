'''Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def calcular_total(self):
        return self.preco * self.quantidade
        
produto1 = Produto("Camisa", 249.90, 2)
total_produto1 = produto1.calcular_total()
print(f"Nome do Produto: {produto1.nome}")
print(f"Preço do Produto: R${produto1.preco:.2f}")
print(f"Quantidade do Produto: {produto1.quantidade}")
print(f"Total do Produto: R${total_produto1:.2f}")
