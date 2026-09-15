# Nesse Programa vamos criar um modelo que analisa um arquivo .csv com dados de alunos. Com base nesses dados a rede neural será treinada para prever a nota de Futuros Alunos

import numpy as np
import pandas as pd
import tensorflow as tf
from keras import layers, models


# lê o arquivo csv
df = pd.read_csv("alunos2.csv")


#exibir os dados carregados
print("Dados Carregados do CSV")
print(df)




#Separação dos dados
#Informações que a rede receberá para fazer a previsão
X_train = df[[
    "idade",
    "horas_estudo",
    "faltas",
    "nota1",
    "nota2"
]].values                   # Se tiver texto vai desprezar


# Informação que representa o resultado que queremos que a rede aprenda a prever.
y_train = df["nota_final"].values


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
novo_aluno = np.array([
    [15, 1, 12, 4.0, 5.0]
], dtype=float)


# Predição
# Solicita a rede neural uma previsão para o novo aluno
previsao = modelo.predict(novo_aluno, verbose = 0)


#Resultado
print("\n" + "*" * 30)
print("Previsão da Rede Neural")
print("*"*30)
print(f"Nota Final Prevista: {previsao[0][0]:.2f}")
print("*" * 30)
