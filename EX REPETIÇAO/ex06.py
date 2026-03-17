n = int(input("Quantidade de alunos: "))
soma = 0

for i in range(n):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / n
print("Média das notas:", media)