"""Imagine um sistema de gerenciamento de pedidos para um restaurante. Os pedidos dos clientes são
colocados em uma fila e processados na ordem em que foram feitos. Use a classe de fila para
gerenciar os pedidos e processá-los na ordem correta."""

from biblioteca import Fila

class FilaPedidosRestaurante(Fila):
    def fazer_pedido(self, pedido):
        self.enfileirar(pedido)
        print(f"Pedido: {pedido} sendo adicionado à fila de pedidos.")

    def processar_pedidos(self):
        while not self.esta_vazia():
            pedido = self.desenfileirar()
            print(f"Processando pedido: '{pedido}'")
            
            
fila_pedidos_restaurante = FilaPedidosRestaurante()
fila_pedidos_restaurante.fazer_pedido("Pizza")
fila_pedidos_restaurante.fazer_pedido("Massa")
fila_pedidos_restaurante.processar_pedidos()
