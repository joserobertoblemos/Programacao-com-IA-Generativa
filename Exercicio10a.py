# Crie um algoritmo de treinamento por recompensa, nesse algoritmo a IA deve sortear uma cor e dentre as cores sortear uma recompensa. 
# As cores são : 
# "RED" : [5, 10, 15], 
# "GREEN" : [8, 16, 24], 
# "BLUE" : [12, 24, 36], 
# "BLACK" : [25, 50, 100]
# Para esse treinamento execute 20 tentativas no mínimo e apresente :
# tentativa: X
# cor escolhida: XXXX
# Recompensa recebida: X
# Pontuação Acumulada: X
# Ao final exiba uma mensagem de Objetivo atingido, caso a pontuação seja de 500 pontos ou mais.

import random as rd

# Recompensas Possíveis para cada cor
cores = {
    "RED" : [5, 10, 15], 
    "GREEN" : [8, 16, 24], 
    "BLUE" : [12, 24, 36], 
    "BLACK" : [25, 50, 100]
}

# Número de tentativas
tentativas = 20

# Pontuação Atual
pontuacao = 0

for tentativa in range(tentativas):
    print(f"\nTentativa {tentativa + 1}")

    # A IA escolhe uma máquina aleatória
    cor = rd.choice (["RED", "GREEN", "BLUE", "BLACK"])

    print(F"Cor escolhida: {cor}")

    # Recebe uma recompensa aleatória  de acordo com a máquina aleatória
    recompensa = rd.choice(cores[cor])

    print(f"Recompensa recebida: {recompensa}")

    # Soma a recompensa à pontuação 
    pontuacao += recompensa

    print(f"Pontuação acumulada: {pontuacao}")

print("\n========================================")
print("Treinamento encerrado")
print(f"Pontuação Final: {pontuacao}")
if pontuacao >= 500:
    print("Atingiu o objetivo")
else:
    print("não atingiu o objetivo")
print("========================================")