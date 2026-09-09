# Utilizando o arquivo alunos_notas.csv crie um gráfico de barras ou de colunas comparando a nota de cada aluno.

import pandas as pd
import matplotlib.pyplot as plt

nota_alunos = pd.read_csv("alunos_notas.csv")

plt.bar(nota_alunos["nome"], nota_alunos["nota"])

plt.title("Notas de cada Aluno")
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.25)
plt.show()

