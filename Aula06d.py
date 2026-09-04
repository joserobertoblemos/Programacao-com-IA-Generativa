# Nesse Programa vamos trabalhar com duas arrays relacionadas, 
# as horas de estudo de um aluno e as notas recebidas nas avaliações,
# depois do tempo de estudo
import numpy as np

# Array com o tempo de estudo
horas_estudo = np.array([2, 4, 6, 8, 10])

# Notas recebidas de acordo com o tempo de estudo 
notas = np.array([40, 50, 60, 80, 100])

print(f"Horas de estudo: {horas_estudo}")
print("*" * 30)
print(f"Notas: {notas}")
print("*" * 30)
quantidade_de_Provas = len(notas)
print(f"Quantidade de provas: {quantidade_de_Provas}")
media_horas_estudo = np.mean(horas_estudo)
media_notas = np.mean(notas)
print(f"Média de horas de estudo: {media_horas_estudo}")
print(f"Média de notas: {media_notas}")
print(f"Maior nota: {np.max(notas)}")
print(f"Menor nota: {np.min(notas)}")
print("*" * 30)

