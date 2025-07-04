
# Jogo batata quente (lista encadeada)

from collections import deque
import random

def simular_batata_quente(lista_nomes, num_passes):
    fila = deque(lista_nomes)
    print("Iniciando jogo com:", list(fila))

    while len(fila) > 1:
        for _ in range(num_passes):
            pessoa = fila.popleft()
            fila.append(pessoa)
            print(f"Passando batata... agora com {pessoa}")

        eliminado = fila.popleft()
        print(f"{eliminado} foi eliminado!")

    vencedor = fila[0]
    print(f"O vencedor é {vencedor}!")
    return vencedor

# Exemplo
simular_batata_quente(["Ana", "Lewyison", "Catatau", "Dori", "Evaristo"], 7)
