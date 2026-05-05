frutas = ["banana", "maca", "laranja", "uva", "manga"]

print("Lista de frutas:", frutas)

remover = input("Digite o nome da fruta que deseja remover:")

if remover in frutas:
    frutas.remove(remover)
    print("Fruta removida com sucesso!")

else:
    print("Fruta nao encontrada na lista.")


print("Lista atualizada", frutas)


