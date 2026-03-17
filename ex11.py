n = int(input("Quantidade de alunos: "))
soma = 0
contador = 0

for i in range(n):
    nota = float(input("Digite a nota: "))
    
    if nota > 5 and nota < 7:
        soma += nota
        contador += 1

if contador > 0:
    media = soma / contador
    print("Média das notas:", media)
else:
    print("Nenhuma nota nessa faixa.")