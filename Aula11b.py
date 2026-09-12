# Nesse programa a rede neural aprenderá a identificar se um aluno provavelmente será aprovado ou reprovado com base nas horas de estudo

import numpy as np
import tensorflow as tf
from keras import layers, models

# Nesse exemplo o modelo espera os dados organizados em linhas e colunas
# Cada linha representa as horas que um aluno estoudou

X_train = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
], dtype = float)       #TensorFlow precisa que seja float

# resultados esperados
# utilizaremos classificação binária
# 0 -> Reprovado
# 1 -> aprovado

y_train = np.array([
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1
], dtype= float)

# Criação do modelo
modelo = models.Sequential([
    layers.Input(shape=(1,)),
    layers.Dense(1, activation = "sigmoid")   # o Sigmoid produz valores entre 0 e 1
])

# Compilação do modelo
modelo.compile(
    optimizer = "adam", # Adam é um algoritmo utilizado para ajustar os pesos de rede durante o treinamento. O objetivo é diminuir o erro das previsões 
    loss = "binary_crossentropy",    # Defini a função de perda, ficar somento no 0 e no 1.
    metrics = ["accuracy"] # Calcula a acurácia durante o treinamento
)

# Treinamento 
modelo.fit(
    X_train,
    y_train,
    epochs = 500,
    verbose = 0
)

#Novos alunos
novos_alunos = np.array([
    [2],
    [4],
    [6],
    [9]
], dtype= float)

# Predição 
previsoes = modelo.predict(novos_alunos, verbose = 0)

# Exibição dos resultados 
for i in range (len(novos_alunos)):

    horas = novos_alunos[i][0]
    probabilidade = previsoes[i][0]

    print("=" * 50)
    print(
        f"{horas :.0f} horas -> "
        f"probabilidade de aprovação : "
        f"{probabilidade:.2%}"
    )