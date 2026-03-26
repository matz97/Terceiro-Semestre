pi = 3.14

raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

area_base = pi * (raio ** 2)
area_lateral = 2 * pi * raio * altura
area_total = 2 * area_base + area_lateral

print(f"Área total do cilindro: {area_total:.2f}")