"""Imagine que você está desenvolvendo um navegador web simplificado. Use uma pilha para armazenar
o histórico de páginas visitadas pelos usuários e implementar as funcionalidades de voltar e avançar
na navegação."""
from biblioteca import Pilha

class NavegadorWeb:
    def __init__(self):
        self.historico = Pilha()
        self.futuro = Pilha()

    def visitar_pagina(self, pagina):
        self.historico.empilhar(pagina)
        # Limpa o histórico futuro quando uma nova página é visitada
        self.futuro = Pilha()

    def voltar(self):
        pagina_atual = self.historico.desempilhar()
        if pagina_atual:
            self.futuro.empilhar(pagina_atual)
            return self.historico.topo()
        else:
            return None

    def avancar(self):
        pagina_futura = self.futuro.desempilhar()
        if pagina_futura:
            self.historico.empilhar(pagina_futura)
            return pagina_futura
        else:
            return None

# Navegador
navegador = NavegadorWeb()
navegador.visitar_pagina("www.google.com")
navegador.visitar_pagina("www.exemplo.com")
navegador.visitar_pagina("www.outrapagina.com")
print("Páginas visitadas:", navegador.historico.itens)
print("Página Atual:", navegador.historico.topo())
print("Voltando para:", navegador.voltar())
print("Avançando para:", navegador.avancar())
print("Voltando para:", navegador.voltar())
print("Voltando para:", navegador.voltar())
