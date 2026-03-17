a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a == b or a == c or b == c:
    print("Triângulo Isósceles")
else:
    print("Não é Isósceles")