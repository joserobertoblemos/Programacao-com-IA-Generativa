# Nesse Programa vamos criar um modelo de grupos de clientes . Vamos estudar o Aprendizado Não Supervisionado 

import numpy as np
from sklearn.cluster import KMeans

#Dados dos Clientes
#coluna 1 = quantidade de compra por ano
#Coluna 2 = valor gasto por ano

clientes = np.array([
    [2, 500],
    [3, 700],
    [2, 400],
    [10, 5000],
    [12, 6000],
    [11, 5500],
    [20, 1500],
    [22, 1800],
    [25, 2000]
])

#Criar modelo K-Means
modelo = KMeans(
    n_clusters=3,       #Procure por 3 grupos
    random_state=42,    #Controla a aleatoriedade
    n_init=10,          #Faz 10 tentativas de inicialização e escolhe a melhor

)

# Treinamento do modelo 
modelo.fit(clientes)

# Obtem o grupo de cada Cliente
grupos = modelo.labels_

#Mostra os grupos encontrados
print("Grupo de cada Cliente")
print(grupos)

#Verificando um novo Cliente
novo_cliente = [[4, 2000]]
grupo_previsto = modelo.predict(novo_cliente)
print(f"Novo Cliente alocado no Grupo {grupo_previsto[0]}")
