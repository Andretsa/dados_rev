"""Você está desenvolvendo um sistema de fila de atendimento para um banco. Os clientes entram na
fila e são atendidos pelos funcionários na ordem de chegada. Use a classe de fila para simular o
atendimento dos clientes."""

from biblioteca import Fila

class FilaAtendimento(Fila):
    def entrar_na_fila(self, cliente):
        self.enfileirar(cliente)
        print(f"Cliente '{cliente}' entrou na fila de atendimento.")

    def atender_clientes(self):
        while not self.esta_vazia():
            cliente = self.desenfileirar()
            print(f"Atendendo cliente: '{cliente}'")

fila_atendimento = FilaAtendimento()
fila_atendimento.entrar_na_fila("Cliente 1")
fila_atendimento.entrar_na_fila("Cliente 2")
fila_atendimento.atender_clientes()
