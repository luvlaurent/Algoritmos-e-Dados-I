
frase = input("Digite uma frase: ").lower()
vogais = consoantes = espacos = outros = 0
lista_vogais = "aeiou"

for letra in frase:
    if letra in lista_vogais:
        vogais += 1
    elif letra.isalpha():  # Se é letra mas não vogal, é consoante
        consoantes += 1
    elif letra.isspace():
        espacos += 1
    else:
        outros += 1
print("\n--- Resultado ---")
print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
print(f"Espaços: {espacos}")
print(f"Outros caracteres: {outros}")