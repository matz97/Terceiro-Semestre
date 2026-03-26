import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Tente advinhar (1 a 100):"))
    tentativas += 1
    if palpite == numero_secreto:
        print("Acertou! Tentativas:", tentativas)
        break
    elif palpite < numero_secreto:
        print("Maior...")
    else:
        print("Menor...")