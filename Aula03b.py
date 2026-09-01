# Nesse Programa vamos estudar a estrutura de desvio condicional de if, else e elif

idade = int(input("Insira sua idade: "))

if idade >= 16:
    print("Você ja pode votar.")
    print("Se não tiver título de eleitor...")
    print("Compareça a um cartório eleitoral.")
else:
    print("Você não pode votar")

print("="*(40))
print("SENAI CELSO CHARURI")
print("="*(40))

idade2 = int(input("Insira sua idade: "))

if idade2 >= 18:
    print("Você ja pode tirar a carteira")
else:
    print("Você é menor de idade")
    print("Não pode ser habilitado")

print("="*40)
print("Senai")
print("="*40)

nota = "ED"

if nota == "D":
    print("Desencolvido")
elif nota == "PD":
    print("Parcialmente Desenvolvido")
elif nota == "ED":
    print("Em Desenvolvimento")
elif nota == "ND":
    print("Não desenvolvido")
else:
    print("Nota Inválida")    