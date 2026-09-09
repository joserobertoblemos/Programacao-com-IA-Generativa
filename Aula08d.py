#  Nesse programa vamos criar um gráfico de barras usando matplotlib

import matplotlib.pyplot as plt

# nomes das candidatos

nomes = ["Gaspar", "Jorge", "Anabela", "Luiza", "Camila", "Carol", "Gabi"]

# Porcentagem de votos
votos = [ 35, 25, 12, 9, 6, 2, 1]

# Criar um gráfico de barras
# Nomes são o eixo x
# Votos o eixo y
plt.barh(nomes, votos)

# Inverter a ordem
plt.gca().invert_yaxis()

# Título do gráfico 
plt.title("Eleições 2026")

# Título do eixo x
plt.xlabel("Candidatos")

# Título do eixo y
plt.ylabel("Votos")
plt.show()