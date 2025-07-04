
# Simulador de histórico de navegação

class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.vazia():
            return self.itens.pop()

    def vazia(self):
        return len(self.itens) == 0

    def limpar(self):
        self.itens = []

class Navegador:
    def __init__(self, pagina_inicial):
        self.pagina_atual = pagina_inicial
        self.historico_voltar = Pilha()
        self.historico_avancar = Pilha()

    def visitar_pagina(self, url):
        print(f"Visitando: {url}")
        self.historico_voltar.push(self.pagina_atual)
        self.pagina_atual = url
        self.historico_avancar.limpar()
        self.exibir_pagina_atual()

    def voltar(self):
        if not self.historico_voltar.vazia():
            self.historico_avancar.push(self.pagina_atual)
            self.pagina_atual = self.historico_voltar.pop()
            print("Voltando...")
        else:
            print("Não há páginas para voltar.")
        self.exibir_pagina_atual()

    def avancar(self):
        if not self.historico_avancar.vazia():
            self.historico_voltar.push(self.pagina_atual)
            self.pagina_atual = self.historico_avancar.pop()
            print("Avançando...")
        else:
            print("Não há páginas para avançar.")
        self.exibir_pagina_atual()

    def exibir_pagina_atual(self):
        print("Página atual:", self.pagina_atual)

# Simulação
nav = Navegador("inicial.com")
nav.visitar_pagina("google.com")
nav.visitar_pagina("youtube.com")
nav.visitar_pagina("chat.openai.com")

nav.voltar()  # volta para youtube
nav.voltar()  # volta para google
nav.avancar()  # avança para youtube
nav.visitar_pagina("github.com")  # limpa histórico de avançar
nav.voltar()
