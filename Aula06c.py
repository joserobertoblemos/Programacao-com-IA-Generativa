# Nesse Programa vamos estudar as arrays do Numpy em forma de matriz, 
# ou seja dados organizados em linhas e colunas
import numpy as np

# Criando uma matriz
matriz_valores = np.array([
    [5, 15, 25, 35], 
    [13, 19, 27, 40],
    [42, 23, 64, 8]
])

print(f"Matriz: \n{matriz_valores}")
print("*" * 30)
print(f"Dimensão da Matriz: \n{matriz_valores.shape}")
print(f"Linha 0, coluna 1: \n {matriz_valores[0][1]}")
print(f"Somente linha 2: \n {matriz_valores[1]}")
