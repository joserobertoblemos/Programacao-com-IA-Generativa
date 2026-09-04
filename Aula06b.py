# Nesse Programa vamos estudar a biblioteca Numpy com calculos de % e estatisticas
import numpy as np

# Array de preços de produtos
preco = np.array([100, 150, 90, 210, 125, 50, 300])

print(f"preços originais: {preco}")
print("*" * 70)

# Aumentando os preços em 10%
precos_aumentados = preco * 1.10
print(f"Preços com aumento de 10% {precos_aumentados}")
print("*" * 70)

#Diminuindo os preços em 5%
print("Preços com desconto de 5%")
precos_descontados = preco * 0.95
print(precos_descontados)
print("\n*** ESTATISTICA ***")
precos_medios = np.mean(preco)
print(f"Média dos preços: {precos_medios}")
print("*" * 70)
print(f"Maior Preço: {np.max(preco)} ")
print(f"Menor Preço: {np.min(preco)} ")
print("*" * 70)
print(f"Primeiro preço: {preco[0]}")
print(f"Último preço: {preco[6]}")



