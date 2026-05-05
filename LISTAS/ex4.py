numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º numero: "))
    numeros.append(num)

print("Lista de numeros:", numeros)

soma = sum(numeros)

print("A soma dos valores: ", soma)