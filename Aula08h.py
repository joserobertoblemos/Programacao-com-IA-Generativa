# Nesse Programa vamos fazer a ligação entre o Pandas e o matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo csv
dados = pd.read_csv("vendas.csv")

# Criar o gráfico utilizando as colunas DataFrame
plt.plot(dados["mes"], dados["vendas"])

plt.title("Vendas por mês")
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.show()