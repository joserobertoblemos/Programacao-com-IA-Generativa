# Nesse programa vamos estudar a biblioteca matplotlib para criar gráficos e visualizações

import matplotlib.pyplot as plt

# lista com os meses
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

# lista contendo a quantidade de vendas de cada mes
vendas = [100, 120, 150, 130, 180, 210]

# Criar um gráfico de linhas
# o 1° parametro representa o eixo x
# o 2° parametro representa o eixo y
plt.plot(meses, vendas)

# Definir o título do gráfico
plt.title("Vendas por Mês")

# Definir o nome do eixo x
plt.xlabel("Meses")

#Definir o nome do eixo y
plt.ylabel("Qtd em Milhares")

plt.show()