# Nesse Programa vamos criar um modelo de deep Learning para prever se um cliente compra ou não compra um produto.
# Vamos usar como dados para treinamento:
#  a idade do cliente, o numero de visitas ao site, o número de produtos visualizados e o resultado da visita.
#  ou seja se ele comprou o produto ou não.

#Importação
import numpy as np
import tensorflow as tf
from keras import layers, models, callbacks


# Dados de treinamento
# [idade, visitas_ao_site, produtos_visualizados]


X = np.array ([
    [18, 1, 2],
    [22, 2, 3],
    [25, 3, 4],
    [30, 2, 2],
    [28, 5, 6],
    [35, 6, 7],
    [40, 7, 8],
    [45, 8, 9],
    [50, 6, 8],
    [32, 5, 7],
    [38, 7, 9],
    [27, 4, 5]
], dtype=float)


# Resultados das Visitas de cada viagem
# 0 não comprou e 1 comprou
y = np.array ([
    0,0,0,0,1,1,1,1,1,1,1,0
], dtype=float)


# Criação da Rede


modelo = models.Sequential ([
    layers.Input(shape=(3,)),       # porque vamos usar  a idade do cliente, o numero de visitas ao site, o número de produtos visualizados


    # Primeira camada oculta
    layers.Dense(16, activation="relu"),


    # Dropout
    layers.Dropout(0.2),


    # Segunda camada oculta
    layers.Dense(8, activation="relu"),


    # Camada de saída
    layers.Dense(1, activation="sigmoid")
])


# Compilação


modelo.compile(
    optimizer = "adam",
    loss = "binary_crossentropy", # porque vamos usar binário
    metrics = ["accuracy"]
)


# Early Stopping
parada = callbacks.EarlyStopping(
    monitor = "val_loss",       #Perda de dados utilizados para validação
    patience = 10,
    restore_best_weights = True
     
)


# Treinamento


modelo.fit(
    X,
    y,
    epochs = 200,
    validation_split = 0.2,
    callbacks = [parada],
    verbose = 0
)


# Novo Cliente


novo_cliente = np.array([
    [34, 6, 8]
], dtype=float)


# Previsão


probabilidade = modelo.predict(
    novo_cliente,
    verbose = 0
)


# Exibir Resultado


if probabilidade >= 0.5:
    resultado = "Provavelmente Comprará"
else:
    resultado = "Provavelmente não Comprará"




print("*" * 50)
print("*** Previsão do Resultado da Visita ***")
print(f"Probabilidade de compra: {probabilidade[0][0]:.2%}")
print("*" * 50)
print(f"Resultado: {resultado}\n")
