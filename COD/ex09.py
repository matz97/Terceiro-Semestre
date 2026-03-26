prestacao = float(input("Digite o valor da prestação :"))
taxa = float(input("Digite a taxa de juros (%0): "))
dias = int(input("Digite a quantidade de dias de atraso: "))

nova_prestacao = prestacao + (prestacao * taxa * dias /100)

print(f"Valor da nova prestação: R$ {nova_prestacao:.2f}")