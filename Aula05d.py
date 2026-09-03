#   Nesse programa vamos estudar a biblioteca random para valores aleatórios
import random

valor1 = random.random() * 100    #.random() vai de 0.0 até 0.9999999999999 aleatóriamente
print(f"{valor1:.0f}")
print("*" * 30)

# gera um número aleatório dentro do intervalo

for i in range(6):
    valor2 = random.randint(1,60)   
    print(valor2, end = " ")
print("*" * 30)

# gera um valor aleatório de uma lista 
gatos = ["Gaspar", "Jorge", "Anabela", "Luiza", "Galego"]
gato_sorteado = random.choice(gatos)
print(gato_sorteado)
print("*" * 30)

# Embaralha a lista original
random.shuffle(gatos)
print(f"Nova lista de gatos {gatos}")