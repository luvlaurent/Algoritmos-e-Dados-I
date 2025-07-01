
# Fila de impressão com prioridade

class FilaDePrioridade:
    def __init__(self):
        self.itens = []

    def enqueue(self, dado, prioridade):
        novo_item = (dado, prioridade)
        inserido = False
        for i in range(len(self.itens)):
            if prioridade < self.itens[i][1]:  # menor número = maior prioridade
                self.itens.insert(i, novo_item)
                inserido = True
                break
        if not inserido:
            self.itens.append(novo_item)
        print(f"Inserido: {dado} (prioridade {prioridade})")
        self.imprimir_fila()

    def dequeue(self):
        if not self.itens:
            return None
        item = self.itens.pop(0)
        print(f"Atendendo: {item[0]} (prioridade {item[1]})")
        self.imprimir_fila()
        return item[0]

    def imprimir_fila(self):
        print("Fila atual:", [f"{dado} (p{prioridade})" for dado, prioridade in self.itens])

# Exemplo de uso
fila = FilaDePrioridade()
fila.enqueue("Relatório Urgente", 1)
fila.enqueue("Documento Normal", 5)
fila.enqueue("E-mail Rápido", 2)

fila.dequeue()
fila.dequeue()
fila.dequeue()