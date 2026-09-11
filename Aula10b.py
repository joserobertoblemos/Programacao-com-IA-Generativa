# Nesse Programa vamos treinar um modelo utilizando o treinamento por recompensa do Machine learning 

import random as rd

# O robo começa na posição 0
posicao = 0

# A recompensa está na posição 5

objetivo = 5

# número de tentativas
tentativas = 10

for tentativa in range(tentativas):

    print(f"\ntentativa: {tentativa + 1}")      # porque range começa do 0
    print(f"posição atual: {posicao}")          # para ver se consegue chegar no objetivo

    # O robo escolhe uma ação aleatória
    acao = rd.choice(["direita", "esquerda"])   #Sorteia entre palavras
    print(f"Ação escolhida: {acao}") 

    # executa a ação 
    if acao == "direita":
        posicao += 1
    else:
        posicao -= 1

    # Verificar o resultado
    if posicao == objetivo:

        # Recompensa
        print(f"posição {posicao} RECOMPENSA! O robô atingiu o objetivo")

        # Volta para o início
        posicao = 0
    elif posicao < 0:

        # Pusição
        print("PUNIÇÂO! O robô saiu do caminho")

        # Voltar ao início 
        posicao = 0
    else:
        # Nenhuma recompensa ou punição
        print("Nenhuma recompensa. O robô continua aprendendo.")