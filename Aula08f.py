# Nesse Programa vamos criar um gráfico de dispersão usando a biblioteca matplotlib

import matplotlib.pyplot as plt

# quantidade de horas estudadas por um aluno 
horas = [1, 2, 3, 4, 5, 6]

# Notas recebidas de acordo com a quantidade de horas estudadas 
notas = [20, 30, 40, 20, 70, 90]

# Criar um gráfico de dispersão 
#Cada par de valor será representado por um ponto

plt.scatter(horas, notas)

plt.title("Horas de estudo X Nota")

plt.xlabel("Horas de estudo")
plt.ylabel("Nota")
plt.grid()
plt.show()
