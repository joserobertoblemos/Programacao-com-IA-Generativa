# Nesse programa vamos utilizar técnicas de Deep Learning para prever o consumo de combustível numa viagem, 
# usando como dados a distancia em KM, a velocidade media, o peso transportado e a quantidade de combustível consumido.

import numpy as np
import tensorflow as tf
from keras import layers, models, callbacks


# Cada linha representa uma viagem.


X = np.array([
    [20, 40, 100],
    [30, 50, 150],
    [40, 60, 200],
    [50, 55, 250],
    [60, 70, 300],
    [70, 65, 350],
    [80, 75, 400],
    [35, 45, 180],
    [55, 60, 120],
    [90, 70, 450],
], dtype=float)


# Quantidade de combustível consumido em cada viagem
y = np.array([
    20.0,
    30.0,
    40.0,
    52.0,
    60.0,
    70.0,
    82.0,
    35.0,
    55.0,
    90.0


], dtype=float)


# Criação do modelo


modelo = models.Sequential([
    # Camada de entrada
    # Cada viagem possui 3 características
    layers.Input(shape=(3,)),   #Utiliza as 3 colunas e , pq é uma tupla


    # Primeira camada oculta: 16 neurônios
    layers.Dense(16, activation = "relu"),   # por causa da Regressão utiliza relu


    # Dropout: 20% dos neurônios serão temporariamente desativados
    layers.Dropout(0.2),


    # Segunda camada oculta: 8 neurônios
    layers.Dense(8, activation= "relu"),


    # A camada de saída com 1 neurônio
    layers.Dense(1)
])


# Compilação
# Criar um otimizador, diferente dos outros vamos fazer um otimizador adam. Raio de treinamento Controle de reajustes durante os treinos


otimizador = tf.keras.optimizers.Adam(
    learning_rate = 0.001
)


# Configura o treinamento
modelo.compile(
    optimizer = otimizador,


    # Utilizar o erro quadrático médio
    loss = "mean_squared_error"
)


# Early Stopping: interrompe o treinamento do modelo
# Depois de algumas épocas sem melhorias
parada = callbacks.EarlyStopping(
    # Observa o erro dos dados de validação
    monitor = "val_loss",


    # Permite até 10 épocas sem melhoria
    patience = 10,


    # Recupera os melhores pesos encontrados
    restore_best_weights = True
)


# Treinamento


historico = modelo.fit(
    X,
    y,
    epochs = 200,


    # Reserva 20% dos dados para a validação
    validation_split = 0.2,


    # Utiliza o Early Stopping
    callbacks = [parada],
    verbose = 0
)


# Gerar uma nova viagem com :
# Distância: 65 km
# Velocidade Média : 60km/h
# peso = 200 kg


nova_viagem = np.array([
    [65, 60, 200]
], dtype=float)


# Previsão


previsao = modelo.predict(
    nova_viagem,
    verbose = 0
)


# Exibir o resultado
print("*" * 50)
print("Previsão do Consumo de Combustível")
print("*" * 50)
print(f"Consumo Previsto: {previsao[0][0]:.2f} litros.")
print("*" * 50)