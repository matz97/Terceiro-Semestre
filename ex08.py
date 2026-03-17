n = int(input("Quantidade de alunos: "))
soma = 0

for i in range(n):
    idade = int(input("Digite a idade: "))
    
    if idade > 25:
        soma += idade

print("Soma das idades maiores que 25:", soma)