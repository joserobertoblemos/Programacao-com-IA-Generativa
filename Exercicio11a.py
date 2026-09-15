# Criar uma rede neural com duas camadas ocultas para prever o preço de uma casa utilizando informações armazenadas em um arquivo CSV.
# Utilize como referência o Exemplo 3 — Duas Camadas Ocultas.

# 1. Use o arquivo casas2.csv
# A rede deverá utilizar cinco características:

# area
# quartos
# idade
# garagem
# banheiros

# A coluna:

# preco
# será o valor que a rede deverá aprender a prever.

# 3. Tarefa
# Crie o programa do zero que:

# Importe:

# tensorflow;

# numpy;

# pandas.

# Leia o arquivo utilizando:

# pd.read_csv()

# Separe as cinco características em X_train.

# Separe a coluna preco em y_train.

# Crie uma rede Sequential com:

# 5 entradas
#      ↓
# 8 neurônios — ReLU
#      ↓
# 4 neurônios — ReLU
#      ↓
# 1 neurônio — saída
# Compile utilizando:
# optimizer="adam"
# loss="mean_squared_error"

# Treine durante 500 épocas.

# Crie uma nova casa com os seguintes dados:

# Área       = 100 m²
# Quartos    = 3
# Idade      = 4 anos
# Garagem    = 2
# Banheiros  = 2
# Utilize:
# model.predict()

# para prever o preço.

# Exiba o preço previsto.

# Exemplo de saída
# **************************************************
# PREVISÃO DO PREÇO DA CASA
# **************************************************
# Preço previsto: R$ 390.000
# **************************************************
# O resultado poderá apresentar alguma diferença em relação aos valores do CSV.

import numpy as np
import pandas as pd
import tensorflow as tf
from keras import layers, models


# lê o arquivo csv
df = pd.read_csv("casas2.csv")      #df = Data Frame


#exibir os dados carregados
print("Dados Carregados do CSV")
print(df)




#Separação dos dados
#Informações que a rede receberá para fazer a previsão
X_train = df[[
    "area",
    "quartos",
    "idade",
    "garagem",
    "banheiros"
]].values                   # Se tiver texto vai desprezar


# Informação que representa o resultado que queremos que a rede aprenda a prever.
y_train = df["preco"].values


# Criação da rede neural
#Modelo utilizado : Sequential      # vai executar as camadas uma depois da outra
modelo = models.Sequential([
    # Camada de entrada
    # Cada aluno possui 5 características
    layers.Input(shape=(5,)),


    # Primeira camada oculta (é que a fica entre entrada e saída)
    # Criar camada com 8 neurônios e a função de ativação RELu
    layers.Dense(8, activation= "relu"),


    # Segunda camada oculta
    # Camada com quatro neurônios. Essa camada recebe os resultados produzidos pelos 8 neurônios anteriores.
    layers.Dense(4, activation="relu"),


    # Camada de saída
    # Camada com 1 neurônio. Esse neurônio produzirá a nota final prevista pela rede neural
    # Como estamos fazendo uma regressão, não utilizamos função e ativação nesse camada


    layers.Dense(1)
])


#Compilação do modelo
modelo.compile(
    # Adam para ajustar os pesos da rede
    optimizer= "adam",


    # Cálculo do erro entre a nota prevista e a nota correta
    loss="mean_squared_error"   #Calcular erro entre nota prevista e nota esperada
)


# treinamento


modelo.fit(
    X_train,
    y_train,
    epochs = 500,
    verbose = 0
)


# Novo aluno
# Vamos apresentar um aluno que não está no arquivo csv
nova_casa = np.array([
    [100, 3, 4, 2, 2]
], dtype=float)


# Predição
# Solicita a rede neural uma previsão para o novo aluno
previsao = modelo.predict(nova_casa, verbose = 0)


#Resultado
print("\n" + "*" * 30)
print("PREVISÃO DO PREÇO DA CASA")
print("*"*30)
print(f"preço previsto: {previsao[0][0]:.2f}")
print("*" * 30)