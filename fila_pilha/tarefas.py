"""Você está criando um aplicativo de lista de tarefas pendentes. As tarefas são adicionadas à fila e
concluídas uma por uma. Use a classe de fila para implementar a lista de tarefas e concluir as tarefas
na ordem em que foram adicionadas."""

from biblioteca import Fila

class ListaTarefas(Fila):
    def adicionar_tarefa(self, tarefa):
        self.enfileirar(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à lista de tarefas.")

    def concluir_tarefas(self):
        while not self.esta_vazia():
            tarefa = self.desenfileirar()
            print(f"Concluindo tarefa: '{tarefa}'")

lista_tarefas = ListaTarefas()
lista_tarefas.adicionar_tarefa("Estudar Python")
lista_tarefas.adicionar_tarefa("Preparar apresentação")
lista_tarefas.concluir_tarefas()
