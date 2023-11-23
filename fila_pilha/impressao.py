"""Você está desenvolvendo um sistema de fila de impressão para uma empresa. Os documentos são
adicionados à fila e impressos na ordem em que foram recebidos. Implemente um programa Python
que use a classe de fila para simular esse processo."""

from biblioteca import Fila

class FilaImpressao(Fila):
    def adicionar_documento(self, documento):
        self.enfileirar(documento)
        print(f"Documento: {documento}  foi adicionado à fila de impressão.")

    def imprimir_documentos(self):
        while not self.esta_vazia():
            documento = self.desenfileirar()
            print(f"Imprimindo documento: {documento}")

fila_impressao = FilaImpressao()
fila_impressao.adicionar_documento("Contrato")
fila_impressao.adicionar_documento("Relatório")
fila_impressao.imprimir_documentos()