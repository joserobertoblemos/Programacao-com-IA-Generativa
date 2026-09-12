import tensorflow as tf
import numpy as np
from keras import layers, models

#Valores de entrada e rede receberá para o treinamento e representa a entrada


X_train = np.array([
    -1.0,
    0.0,
    1.0,
    2.0,
    3.0,
    4.0
], dtype=float)


# y representa o valor esperado
y_train = np.array([
    -3.0,
    -1.0,
    1.0,
    3.0,
    5.0,
    7.0
], dtype= float)


# Criação do modelo
# Sequential: significa que as camadas serão executadas uma depois da outra, em sequência.
modelo = models.Sequential([
    layers.Input(shape =(1,)), # Significa que cada exemplos possui uma entrada
    layers.Dense(units=1)       # Cria uma camada densa, que é uma camada totalmente conectada #Units = 1 significa que tem apenas 1 neurônio ou 1 camada oculta
])


# Compilação do modelo  para transformar em linguagem de máquina


modelo.compile(
    optimizer = "sgd", # Define o algoritmo responsável por ajustar os pesos da rede durante o treinamento # é o sigmoide
    loss = "mean_squared_error" # Define a função para calcular o erro #tenta diminuir a quantidade de erro nos números


)


# Treinamento do modelo
modelo.fit(
    X_train,
    y_train,
    epochs = 500, # Define quantas vezes o modelo passará pelo conjunto de dados    # vai olhar 500 vezes, ou repetir 500 vezes
    verbose = 0,    # Oculta a saída do epochs, se tirar aparece todos os testes.
)


# Passando um novo dado para ser resolvido pelo modelo
entrada = np.array([[10.0]])    #Quando o x for 10 quanto será o y


previsao = modelo.predict(entrada, verbose = 0)


print("=" * 50)
print(f"Predição para x = 10. {previsao}.")
