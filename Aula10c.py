# Nesse programa vamos treinar um modelo por recompensa de acordo com a máquina sorteada
import random as rd

# Recompensas Possíveis para cada máquina
maquinas = {
    "A" : [1,2,3],
    "B" : [3,5,7],
    "C" : [6,8,10],
}

# Número de tentativas
tentativas = 20

# Pontuação Atual
pontuacao = 0

for tentativa in range(tentativas):
    print(f"\nTentativa {tentativa + 1}")

    # A IA escolhe uma máquina aleatória
    maquina = rd.choice (["A", "B", "C"])

    print(F"Máquina escolhida: {maquina}")

    # Recebe uma recompensa aleatória  de acordo com a máquina aleatória
    recompensa = rd.choice(maquinas[maquina])

    print(f"Recompensa recebida: {recompensa}")

    # Soma a recompensa à pontuação 
    pontuacao += recompensa

    print(f"Pontuação acumulada: {pontuacao}")

print("\n========================================")
print("Treinamento encerrado")
print(f"Pontuação Final: {pontuacao}")
if pontuacao >= 100:
    print("Atingiu o objetivo")
else:
    print("não atingiu o objetivo")
print("========================================")
