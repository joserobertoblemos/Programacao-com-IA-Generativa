# Jogo da adivinhação 

# Nesse jogo o usuário tera que adivinhar um número sorteado pelo python entre 0 e 10. Para isso, terá 3 chances.
# A cada chance perdida, ele receberá uma dica sobre o número sorteado, informando se o mesmo é maior ou menor
# que o palpite.

import random

numero_secreto = random.randint(0,10)
tentativas = 0
acertou = False

while tentativas < 3:
    palpite = int(input("Digite seu palpite entre 0 e 10: "))
    tentativas += 1
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite > numero_secreto:
        print("O número sorteado é menor que o seu palpite.")
    else:
        print("O número sorteado é maior que o número sorteado.")

if acertou:
    print("parabéns!!! Você acertou o número secreto.")
else:
    print(f"errou!!! o número sorteado era {numero_secreto}") 