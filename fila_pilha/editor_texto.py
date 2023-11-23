"""Em um programa de edição de texto, implemente a funcionalidade de "Desfazer" e "Refazer" usando
uma pilha para armazenar o histórico de comandos executados pelo usuário."""

from biblioteca import Pilha

class EditorDeTexto:
    def __init__(self):
        self.comandos = Pilha()
        self.desfeitos = Pilha()

    def executar_comando(self, comando):
        self.comandos.empilhar(comando)
        # Limpa o histórico de comandos desfeitos quando um novo comando é executado
        self.desfeitos = Pilha()

    def desfazer(self):
        comando_atual = self.comandos.desempilhar()
        if comando_atual:
            self.desfeitos.empilhar(comando_atual)
            # Simula a reversão do comando
            return "comando: " + comando_atual
        else:
            return "Nada para desfazer"

    def refazer(self):
        comando_desfeito = self.desfeitos.desempilhar()
        if comando_desfeito:
            self.comandos.empilhar(comando_desfeito)
            # executa o comando desfeito novamente
            return "comando: " + comando_desfeito
        else:
            return "Nada para refazer"

# Exemplo de uso:
editor = EditorDeTexto()
editor.executar_comando("Inserir Texto")
editor.executar_comando("Remover Linha")
print("Ações Atuais:", editor.comandos.itens)
print("Desfazendo", editor.desfazer())
print("Refazendo", editor.refazer())
