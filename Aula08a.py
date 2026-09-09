# Nesse Programa vamos fazer uma revisão da biblioteca pandas e estudar como criar um fltro dos dados

import pandas as pd

# Criando os dados

dados = {
    "nome" : ["Ana", "Carlos", "João", "Maria", "Pedro", "Carol", "Camila"],
    "idade" : [17, 18, 16, 17, 18, 15, 19],
    "nota"  : [8.5, 7.0, 5.5, 9.0, 6.5, 8.0, 5.0]
}

# Criar o DataFrame dos dados 

alunos = pd.DataFrame(dados)

print("*** todos os alunos ***")
print(alunos)

media_idade = alunos["idade"].mean()
media_nota = alunos["nota"].mean()

print("="*30)
print(f"idade média dos alunos: {media_idade:.0f}.")
print(f"nota média dos alunos: {media_nota:.1f}.")
print("="*30)

numero_alunos = alunos["idade"].count()
numero_aprovados = [alunos["nota"] >= 7]    
numero_reprovados = [alunos["nota"] < 7]

print(f"Total de alunos: {numero_alunos}")
print("="*30)
print(("*** todos os alunos Aprovados ***"))
print(numero_aprovados)
print("="*30)
print("*** todos os alunos Reprovados ***")
print(numero_reprovados)

