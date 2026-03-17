n = int(input("Quantidade de alunos: "))
soma = 0
contador = 0

for i in range(n):
    idade = int(input("Digite a idade: "))
    
    if idade > 25 and idade < 40:
        soma += idade
        contador += 1

if contador > 0:
    media = soma / contador
    print("Média das idades:", media)
else:
    print("Nenhum aluno nessa faixa.")