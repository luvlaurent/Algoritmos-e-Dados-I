
# Fila de atendimento (lista encadeada)

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, valor):
        novo_no = No(valor)
        if self.fim:
            self.fim.proximo = novo_no
        self.fim = novo_no
        if self.inicio is None:
            self.inicio = novo_no

    def dequeue(self):
        if self.esta_vazia():
            return None
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return valor

    def imprimir_fila(self):
        atual = self.inicio
        fila = []
        while atual:
            fila.append(atual.valor)
            atual = atual.proximo
        print("Fila atual:", fila)

def novo_cliente(fila, nome_cliente):
    print(f"{nome_cliente} entrou na fila.")
    fila.enqueue(nome_cliente)
    fila.imprimir_fila()

def atender_cliente(fila):
    cliente = fila.dequeue()
    if cliente:
        print(f"Atendendo: {cliente}")
    else:
        print("Fila vazia.")
    fila.imprimir_fila()

# Simulação
fila = Fila()
novo_cliente(fila, "Ana")
novo_cliente(fila, "Bruno")
novo_cliente(fila, "Catarina")
novo_cliente(fila, "Duarte Coelho")

atender_cliente(fila)

novo_cliente(fila, "Joba")

while not fila.esta_vazia():
    atender_cliente(fila)
