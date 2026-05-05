import random

numeros = [random.randint(1, 100) for _ in range(10)]

print("Lista original:", numeros)

crescente = sorted(numeros)
print("Ordem crescente", crescente)

decrescente = sorted(numeros, reverse=True)
print("Ordem decrescente:", decrescente)