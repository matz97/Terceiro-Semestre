numeros = [4, 8, 15, 16, 23, 42, 7, 9, 12, 30]

print("Lista de numeros", numeros)

busca = int(input("Digite um número para procurar na lista: "))

if busca in numeros:
    posicao = numeros.index(busca)
    print(f"O numero {busca} esta na lista da posicao {posicao}.")
else:
    print(f"O numero {busca} nao esta na lista")

    