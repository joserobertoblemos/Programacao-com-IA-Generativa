# Nesse Programa vamos vamor criar um gráfico de tipo histograma usando a biblioteca do matplotlib
import matplotlib.pyplot as plt

#Notas dos alunos
notas = [5, 6, 7, 7, 8, 8, 9, 9, 10]

# Criar um histograma
# Bins5 divide os dados em 5 intervalos
plt.hist(notas, bins=5)

plt.title("Distribuição de notas")
plt.ylabel("Quantidade e alunos")
plt.xlabel("Notas")
plt.grid()
plt.show()