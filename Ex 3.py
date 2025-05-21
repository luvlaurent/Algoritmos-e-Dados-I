numero = int(input("Digite um número: "))
print(f"\nTabuada do {numero}")
for i in range(1, 31):
    resultado = numero * i 
    print(f"{numero} x {i:2} = {resultado}")