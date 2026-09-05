#Nesse Programa vamos criar um DataFrame a partir de um arquivo CSV

import pandas as pd

#ler arquivo Criando o DataFrame a partir do arquivo .csv
alunos = pd.read_csv("alunos.csv")

print(alunos)

print("*" * 50)
print("Dados Faltantes")
print(alunos.isnull().sum())

media_idade = int(alunos["idade"].mean())
alunos["idade"] = alunos["idade"].fillna(media_idade)

menor_nota = alunos["nota"].min()
alunos["nota"] = alunos["nota"].fillna(menor_nota)

#Inserindo o dado no registro específico 
alunos.loc[9, "frequencia"] = 80

print("*" * 50)
print("Lista Alterada: ")
print(alunos)

