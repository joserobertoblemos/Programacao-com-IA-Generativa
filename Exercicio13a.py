# Uma empresa deseja utilizar Deep Learning para estimar o tempo necessário para realizar a entrega de um pedido.

# Para fazer a previsão, serão utilizadas três características:

# Distância da entrega, em quilômetros;
# Quantidade de produtos no pedido;
# Nível de trânsito, representado por um valor de 1 a 10.
# A classificação do trânsito será:

# Valor	Nível de trânsito
# 0 a 39	Baixo
# 40 a 69	Moderado
# 70 a 89	Alto
# 90 a 100	Muito alto
# A saída da rede neural deverá ser o tempo estimado da entrega, em minutos.

# O arquivo entregas.csv contém dados reais de entregas realizadas anteriormente pela empresa. Esses dados deverão ser utilizados para treinar a rede neural.

# Tarefa
# Utilizando TensorFlow/Keras, desenvolva uma rede neural capaz de aprender os padrões existentes nos dados do arquivo entregas.csv e realizar previsões para novas entregas.

# Após o treinamento, utilize o modelo para estimar o tempo de entrega de um novo pedido:

# Distância: 12 km
# Quantidade de produtos: 5
# Nível de trânsito: 70
# O programa deverá apresentar o resultado aproximadamente no seguinte formato:

# ==================================================
# PREVISÃO DE ENTREGA
# ==================================================

# Distância: 12 km
# Produtos: 5
# Trânsito: 70 (Alto)

# Tempo estimado: XX.XX minutos

# ==================================================


import numpy as np
import pandas as pd
import tensorflow as tf
from keras import layers, models, callbacks

# lê o arquivo csv
df = pd.read_csv("entregas.csv")

#exibir os dados carregados
print("Dados Carregados do CSV")
print(df)

#Separação dos dados
#Informações que a rede receberá para fazer a previsão
X_train = df[[
    "distancia",
    "quantidade",
    "transito"
]].values 

# Informação que representa o resultado que queremos que a rede aprenda a prever.
y_train = df["minutos"].values

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
    X_train,
    y_train,
    epochs = 200,


    # Reserva 20% dos dados para a validação
    validation_split = 0.2,


    # Utiliza o Early Stopping
    callbacks = [parada],
    verbose = 0
)


# Gerar uma nova viagem com :
# Distância: 12 km
# Quantidade de produtos: 5
# Nível de trânsito: 70


nova_viagem = np.array([
    [12, 5, 70]
], dtype=float)


# Previsão


previsao = modelo.predict(
    nova_viagem,
    verbose = 0
)


# Exibir o resultado
if nova_viagem[0][2] <= 39:
    nivel_transito = "Baixo"
elif nova_viagem[0][2] <= 69:
    nivel_transito = "Moderado"
elif nova_viagem[0][2] <= 89:
    nivel_transito = "Alto"
else:
    nivel_transito = "Muito Alto"


print("*" * 50)
print("PREVISÃO DE ENTREGA")
print("*" * 50)
print(f"Distância: {nova_viagem[0][0]} Km")
print(f"Produtos: {nova_viagem[0][1]} Unidades")
print(f"Trânsito: {nova_viagem[0][2]} ({nivel_transito})")
print(f"Tempo Previsto: {previsao[0][0]:.2f} Minutos.")
print("*" * 50)