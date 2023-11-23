"""Em um sistema de comércio eletrônico, os pedidos online são processados em uma fila. Implemente
uma classe de fila que gerencie os pedidos online e processe-os na ordem de chegada."""

from biblioteca import Fila

class FilaPedidosOnline(Fila):
    def fazer_pedido_online(self, pedido):
        self.enfileirar(pedido)
        print(f"{pedido} adicionado à fila de pedidos online.")

    def processar_pedidos_online(self):
        while not self.esta_vazia():
            pedido = self.desenfileirar()
            print(f"Processando pedido online: '{pedido}'")
            
fila_pedidos_online = FilaPedidosOnline()
fila_pedidos_online.fazer_pedido_online("Produto A")
fila_pedidos_online.fazer_pedido_online("Produto B")
fila_pedidos_online.processar_pedidos_online()
