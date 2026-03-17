contador = 0

for i in range(100):
    idade = int(input("Digite a idade: "))
    
    if idade == 30:
        contador += 1

print("Quantidade de alunos com 30 anos:", contador)