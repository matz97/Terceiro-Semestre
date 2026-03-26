a = int(input("Digite a média de A :"))

b = int(input("Digite a média de B :"))

c = int(input("Digite a média de C :"))

d = int(input("Digite a média de D :"))


if a != 3 :
    print("Erro: a média de A deve ser igual a 3!")
else:
    print("Numero correto!")

if b != 4:
    print("Erro : a média de B deve ser igual a 4!")
else:
    print("Número correto!")

if c != 2:
    print("Erro: a média de C deve ser igual a 2!")
else:
    print("Número correto!")

if d != 5:
    print("Erro: a média de D deve ser igual a 5!")
else:
    print("Número correto!")


soma = a + b + c + d 

print("A soma de todas as médias é :", soma)