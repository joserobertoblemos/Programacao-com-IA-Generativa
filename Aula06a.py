# Nesse Programa vamos estudar alguns exemplos da biblioteca numpy

import numpy as np

notas_lista = [7.555, 6, 5.5, 10, 8.5]
print(notas_lista)

print("*" * 30)
notas = np.array(notas_lista)
print(notas)

# Adiciona 0.5 ponto em todas as notas
notas_ponto = notas + 0.5

print("Notas apos adicionar 0.5 ponto: ")
print(notas_ponto)
