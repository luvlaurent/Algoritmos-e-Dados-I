
#Invertendo palavras com pilhas
#respeita caracteres minúsculos e maiusculos
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

def inverter_string(texto):
    pilha = Pilha()
    for caractere in texto:
        pilha.push(caractere)
    
    invertida = ''
    while not pilha.vazia():
        invertida += pilha.pop()
    
    return invertida
print(inverter_string("Casa"))
