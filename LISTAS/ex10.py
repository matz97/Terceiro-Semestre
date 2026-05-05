matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for linha in matriz:
    for valor in linha:
        print(valor, end="")
    print()


soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor

print("Soma de todos os elementos:", soma)

print("Diagonal principal:")
for i in range(3):
    print(matriz[i][i], end="")