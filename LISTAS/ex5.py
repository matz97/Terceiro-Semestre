numeros = list(range(1, 21))


pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print("Numeros pares:", pares)