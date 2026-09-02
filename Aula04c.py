# Nesse Programa vamos estudar estruturas de dados como listas
# 
# gatos = ["Gaspar", "Anabela", "Luiza", "Jorge"]

# gatos[2] = "Luiza"

alunos = ["Gaspar", "Jorge", "Luiza", "Anabela"]
print(f"O primeiro aluno da lista é {alunos[0]}.")


# Mais de uma lista
for i in range(4):
    print(f"Aluno: {alunos[i]}.")

print("=" * 40)


# Para uma lista só
for aluno in alunos:
    print(f"Aluno: {aluno}.")

# Exemplo com 2 listas
print("=" * 40)
idades = [20,30,25, 16]
for i in range(4):
    print(f"O aluno {alunos[i]} tem {idades[i]} anos.")

