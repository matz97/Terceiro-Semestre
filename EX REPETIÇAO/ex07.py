n = int(input("Quantidade de alunos: "))
soma = 0

for i in range(n):
    nota = float(input("Digite a nota: "))
    
    if nota >= 5:
        soma += nota

print("Soma das notas >= 5:", soma)