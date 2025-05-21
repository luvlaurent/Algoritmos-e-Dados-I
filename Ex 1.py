import unicodedata #serve pro desafio extra

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

entrada = input("Insira uma palavra ou frase: ")

texto = entrada.lower().replace(" ", "")
texto = remover_acentos(texto)

if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")