n = int(input("Quantos números deseja inserir? "))

numeros = []

for i in range(n):
    valor = float(input("Digite um número:"))
    numeros.append(valor)

print("Maior:", max(numeros))
print("Menor:", min(numeros))
print("Media:", sum(numeros) / len(numeros))