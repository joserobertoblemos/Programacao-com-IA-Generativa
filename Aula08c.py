# Nesse Programa vamos criar um grafico de barras com matplotlib
import matplotlib.pyplot as plt

# Lista de nomes de produtos 
produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]

# Quantidade vendida de cada produto
quantidade = [100, 350, 225, 152]

# Criar um gráfico de barras 
# Os produtos serão apresentados no eixo x 
# As qunatidade serão apresentadas no eixo y

plt.bar(produtos, quantidade)

# Definindo o Título do gráfico
plt.title("Produtos Vendidos em Agosto-2026")

#Definindo o nome do eixo X
plt.xlabel("Produtos")

#Definindo o nome do eixo y
plt.ylabel("Quantidade Vendida")



# Exibindo o gráfico
plt.show()