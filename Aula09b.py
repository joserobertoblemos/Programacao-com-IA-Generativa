# Nesse Programa vamos criar um modelo de regressão linear para prever o preço de um imóvel com base no tamanho

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

# Dados para treinamento. Tamanho das casas em m² e seus respectivos preços 
# X deve ser um array 2D
X = np.array([
    [40],
    [60],
    [80],
    [100],
    [120]
]) 

# y contém os preços correspondentes 
y = np.array([200000, 300000, 400000, 500000, 600000])

# Criando o model
modelo = LinearRegression()

# Treinamento do modelo
modelo.fit(X, y)

# Qual o preço de 90 m²
tamanho_novo = [[90]]       #Deve ser um array 2D

preco_previsto = modelo.predict(tamanho_novo)

print(f"Preço para 90 m²: R$ {preco_previsto[0]:,.2f}")

# Visualização gráfica dos valores para comparar

# Criando um gráfico de dispersão
plt.scatter(X, y, color= 'red', label="Dados reais")    #label para legenda

# Plotando a reta de regressão 
plt.plot(X, modelo.predict(X), color = 'blue', label= "Reta de Regressão")  #label para legenda

#Configurando o gráfico
plt.title("Relação entre Tamanho e Preço das Casas")
plt.xlabel("Tamanho em (M²)")
plt.ylabel("Preço (R$)")
plt.legend()
plt.grid(True)
plt.show()