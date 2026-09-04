# Uma escola deseja analisar as notas de uma turma. Utilize o NumPy para armazenar e analisar as notas dos alunos.
# Dados
# Considere as seguintes notas:

# 6.5, 8.0, 7.5, 5.0, 9.0, 4.5, 8.5, 7.0

# Tarefas
# Crie um programa em Python usando a biblioteca Numpy que:
# Mostre todas as notas.
# Mostre quantos alunos existem no array.
# Calcule e mostre a média das notas.
# Mostre a maior nota.
# Mostre a menor nota.

# Crie um novo array chamado notas_bonus, acrescentando 1 ponto a cada nota.
# Mostre as notas após o acréscimo do bônus.

import numpy as np

notas = np.array([6.5, 8.0, 7.5, 5.0, 9.0, 4.5, 8.5, 7.0])
qtd_notas = len(notas)
media_notas = np.mean(notas)

print("Todas as notas: ", end = " ")
print(*notas, sep = ", ")
print(f"Alunos: {qtd_notas}")
print(f"A média dos alunos foi: {media_notas}")
print(f"A maior nota foi: {np.max(notas)}")
print(f"A menor nota foi: {np.min(notas)}")

notas_bonus = notas + 1
print("As notas finais com acréscimo foram: ", end = " ")
print(*notas_bonus, sep = ", ")
