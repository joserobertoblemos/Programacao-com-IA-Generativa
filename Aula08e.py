# Nesse Programa vamos criar um gráfico de pizza

import matplotlib.pyplot as plt

#nomes das linguagens

linguagens = ["Python", "Java", "JavaScript", "C#"]

# Quantidade de alunos que escolheram cada linguagem
alunos = [30, 20, 15, 10]

# Criar o gráfico de pizza
# labels define os nomes das partes
# autopct mostra o percentual de cada parte
plt.pie(alunos, labels=linguagens, autopct="%1.1f%%")

# Título do gráfico 
plt.title("Linguagens preferidas dos alunos")

plt.show()